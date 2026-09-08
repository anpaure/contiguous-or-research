# Selected cross-half axes: a target-level all-cuts theorem and two whole-cell counter-cuts

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
 M=\lfloor m/d\rfloor,\qquad d=\Theta(\log m),       \tag{0.1}
\]

and split each \(2d\)-coordinate macroblock into two \(d\)-sets.  At
local source rank \(k\), use an ordered rank-dependent bijection between
the halves and toggle the first split pair.  Thus one eligible macroblock
supplies one physical cross-half \(Q_1\)-axis.

For a lower target \(T\), define

\[
 a_i^-(T)=\#\{\text{empty pairs before the first split pair in block }i
                 \text{ under the source-rank frame}\}.        \tag{0.2}
\]

The upper statistic \(a_i^+(T)\) counts full pairs before the first split.
The audited abundance theorem says that a typical target has
\((1/3+o(1))M\) blocks with \(a_i^pm>0\), while every protected depth is
\(q=o(M)\).

This note determines exactly how far that abundance can be converted into
Hall expansion.

1. **Positive target-to-block theorem.**  After deleting
   \(e^{-\Omega(M)}\) of either signed target layer, one can assign
   \(h=o(M/\log M)\) distinct compatible blocks to every target so that
   every block receives exactly a floor or ceiling of the average load.
   Every deficient cut has a certificate involving either one omitted
   block or \(O(\log M)\) omitted blocks.  Thus no union over arbitrary
   target subsets is needed at this layer.

2. **Exact fixed-depth compression.**  The number of raw rooted
   \(q\)-block lifts of a lower target is

   \[
      D_q(T)=2^q e_q(a_1^-(T),\ldots,a_M^-(T)).       \tag{0.3}
   \]

   Within one local-rank-profile fibre this degree formula gives exact
   Hall expansion, and globally it gives both a target-degree certificate
   and a one-source inverse-degree certificate.  Any surviving deficient
   family must mix a dense collection of adjacent rank profiles.

3. **Random/symmetric selection is false.**  At
   \(q=A\sqrt m\), a typical target satisfies

   \[
     \log{D_q(T)\over\binom Mq}
       =-\left({3\over2}+o(1)\right){q^2\over M}
         +{2q^2\over m}.                              \tag{0.4}
   \]

   Since \(M=m/d\), the first term is \(-\Theta_A(d)\).  A uniform
   priority, uniform compiler conjugate, or any proposal whose edge
   likelihood is distorted by only
   \(\exp(o(q^2/M))\) leaves a \(1-o(1)\) fraction of typical lower
   targets uncovered.  The upper sign has the identical obstruction.
   A successful selection needs a target-chart-dependent likelihood tilt
   of order \(\exp((3/2+o(1))q^2/M)\).

4. **Fixed first-priority selection is also false.**  Selecting the first
   \(r\) eligible macroblocks concentrates a linear fraction of all
   deletion-run mass on the first \(2r\) macroblocks.  It has a linear
   point-margin/floor defect whenever \(2r/M\) stays below one.  A fixed
   order inside each macroblock has a second geometric availability cut.

5. **Common-depth dynamics are solved inside one cell.**  A two-scale
   round-robin construction gives one literal owner permutation on a
   \(Q_t\)-cell whose windows through depth \(h\) are geodesic, obey
   \(G_1(G_sX)=G_{s+1}X\), and have injective lower and upper shadows.

The precise unproved step is the indivisible-cell lift.  The positive Hall
theorem assigns blocks targetwise; one owner-disjoint \(Q_e\)-cell must
choose one common axis set and one common compiler for all its owners,
depths, and signs.  Equations (0.3)--(0.4) prove that a symmetric random
lift cannot do this.  No universal deterministic Hall counterexample to an
adaptively target-biased whole-cell selection is proved.

## 1. Exact local compatibility and its finite enumerator

Fix one ordered perfect matching of the two halves of a macroblock.  For a
local target \(T\) of rank \(k-1\), an empty pair \(j\) supplies the two
source endpoints \(T+a_j,T+b_j\).  This is the selected first-split edge
of source rank \(k\) if and only if no pair preceding \(j\) is split in
\(T\).  Hence (0.2) is exactly the number of local source edges whose
intersection is \(T\).  Dually, \(a_k^+(U)\) is exactly the number of
source-rank-\(k\) edges whose union is a local \((k+1)\)-target \(U\).

If \(x\) marks local rank and \(z\) marks \(a^-\), the split-containing
states have polynomial

\[
\begin{aligned}
 F_d(x,z)
 &=2x\sum_{j=1}^d(x^2+z)^{j-1}(1+x)^{2(d-j)}\\
 &=\frac{2x\big((1+x)^{2d}-(x^2+z)^d\big)}{1+2x-z}. \tag{1.1}
\end{aligned}
\]

The no-split states contribute \((x^2+z)^d\): every empty pair lies before
the formal first-split index \(d+1\).  Only the all-full state has
\(a^-=0\) among these states.

Under an independent Bernoulli-\(p\) tilt, put

\[
 e=(1-p)^2,\qquad f=p^2,\qquad s=2p(1-p).            \tag{1.2}
\]

The exact finite probability generating function is

\[
 \mathbb E z^{a^-}
 =s\,{1-(f+ez)^d\over1-f-ez}+(f+ez)^d.              \tag{1.3}
\]

As \(d\to\infty\), this tends to \(s/(1-f-ez)\).  With

\[
                         b^-=2a^-,                   \tag{1.4}
\]

the limiting first two moments are

\[
 \mu:=\mathbb E b^-={1-p\over p},\qquad
 \operatorname{Var}(b^-)=2\mu+\mu^2,qquad
 \mathbb E(b^-)^2=2\mu+2\mu^2.                     \tag{1.5}
\]

At \(p=1/2\), \(\mu=1\), the variance is three, and the finite no-split
correction is \(O(d^2 2^{-d})\).

The exact incompatibility probability is obtained by setting the empty
count to zero:

\[
 \boxed{
 \beta_d^-(p)
 ={2p\over1+p}(1-p^{2d})+p^{2d}.}                   \tag{1.6}
\]

For the upper sign,

\[
 \boxed{
 \beta_d^+(p)
 ={2(1-p)\over2-p}(1-(1-p)^{2d})+(1-p)^{2d}.}       \tag{1.7}
\]

Both are \(2/3+o(1)\) uniformly at the protected central ranks.

## 2. A low-complexity target-to-block all-cuts theorem

The following abstract form is the useful statement.

### Theorem 2.1 (one-or-logarithm witness theorem)

Let \(\mathcal T\) be a set of \(n\) demands and let \([M]\) be a block
set.  Each \(T\in\mathcal T\) has a compatible set \(E(T)\subseteq[M]\).
Suppose that, for some fixed \(\beta<1\), every set \(L\subseteq[M]\) with
\(|L|\le C_0\log M\) satisfies

\[
 {1\over n}|\{T:E(T)\cap L=\varnothing\}|
 \le(\beta+o(1))^{|L|},                              \tag{2.1}
\]

uniformly, and every demand has at least \(h\) compatible blocks.  If

\[
                         h=o(M/\log M),               \tag{2.2}
\]

then every demand can be assigned \(h\) distinct compatible blocks so
that every block degree is

\[
             \left\lfloor{hn\over M}\right\rfloor
        \quad\text{or}\quad
             \left\lceil{hn\over M}\right\rceil.    \tag{2.3}
\]

At every one of the \(h\) matching rounds, a failed Hall cut would have a
certificate consisting of either one omitted block or
\(C_0\log M\) omitted blocks.

#### Proof

Assign one new block per demand in each round.  In round \(t<h\), forbid
the \(t\) blocks already assigned to a demand.  Give every block capacity
\(p\) or \(p+1\), where \(p=\lfloor n/M\rfloor\), with the high-capacity
blocks rotated so that the cumulative capacities after \(h\) rounds are
exactly (2.3).

Fix a demand family \(U\), let \(K\) be its current block neighborhood,
and put \(R=[M]\setminus K\), \(|R|=s\).  If \(R\ne\varnothing\), choose
\(i\in R\).  Every member of \(U\) is either originally incompatible with
\(i\) or used \(i\) in an earlier round.  Hence

\[
 |U|\le(\beta+o(1))n+t(p+1).                        \tag{2.4}
\]

If \(|K|\ge(\beta+o(1))M+2t\), its capacity is at least the right side of
(2.4), for all large \(n\), and Hall holds.

Otherwise \(s\ge(1-\beta-o(1))M-2t\).  For every \(T\in U\), every block
of \(R\) not previously assigned to \(T\) is originally incompatible with
\(T\).  Average over all \(\ell=C_0\log M\) subsets of \(R\).  Some
\(L\subseteq R\) is disjoint from the previous assignments of at least

\[
 |U|{\binom{s-t}{\ell}\over\binom s\ell}            \tag{2.5}
\]

members of \(U\).  Those members are incompatible with every block of
\(L\), so (2.1) gives

\[
 |U|\le n(\beta+o(1))^\ell
              {\binom s\ell\over\binom{s-t}\ell}.   \tag{2.6}
\]

Condition (2.2) makes the binomial ratio \(\exp(o(1))\).  Choose the fixed
constant \(C_0\) so that the right side is less than \(n/M^2\).  If
\(K\ne\varnothing\), one block already has capacity at least
\(p\ge n/(2M)\), so Hall again holds.  If \(K=\varnothing\), a demand in
\(U\) would have used all its compatible blocks before round \(h\),
contrary to the minimum-degree hypothesis.  Thus every capacitated Hall
cut passes.  Integral bipartite matching gives the next round, and
iteration proves the theorem. \(\square\)

### Corollary 2.2 (application to first-split targets)

For either sign and every protected rank, discard the targets having fewer
than \(h\) compatible macroblocks.  If \(h=o(M/\log M)\), their number is
\(e^{-\Omega(M)}N_q\).  The remaining targets admit the assignments in
Theorem 2.1 with exact floor/ceiling block degrees.

#### Proof

Before conditioning on total rank, distinct macroblocks are independent,
and (1.6)--(1.7) give compatible probability \(1/3+o(1)\).  Chernoff gives
the exceptional bound.  For any \(L=O(\log M)\) fixed blocks, the
probability of joint incompatibility is the product of their local
probabilities.  Conditioning on rank \(m\pm q\) changes it by \(1+o(1)\),
because the event involves \(O(d\log M)=O((\log m)^2)\) coordinates and
\(q=o(M)\).  Thus (2.1) holds with \(\beta=2/3\). \(\square\)

Theorem 2.1 is the requested low-complexity witness theorem at the
target-to-block layer.  It already couples the *block list* through all
prefix depths for one demand.  It does not make targetwise lists belonging
to different targets into one common whole-cell axis set.

## 3. Exact fixed-depth source compression

Let a lower target \(T\) have local-rank profile
\(t=(t_1,\ldots,t_M)\), and abbreviate

\[
                         a_i(T)=a^-_{i,t_i+1}(T_i).   \tag{3.1}
\]

For a \(q\)-set \(J\subseteq[M]\), a compatible source raises precisely
the ranks in \(J\).  In each chosen block there are \(a_i(T)\) local
matching edges and two choices of endpoint.  Therefore the number of
source owners of profile \(t+\mathbf1_J\) is exactly

\[
                         2^q\prod_{i\in J}a_i(T).     \tag{3.2}
\]

For fixed \(t,J\), distinct targets have disjoint source sets: the chosen
source and \(J\) recover its first-split intersections.  Different \(J\)'s
have different source-rank profiles.  This proves (0.3), and more strongly:

### Theorem 3.1 (profile-fibre Hall identity)

If \(\mathcal A\) lies inside one local-rank-profile fibre, then

\[
 |N(\mathcal A)|=\sum_{T\in\mathcal A}D_q(T).        \tag{3.3}
\]

For an arbitrary target family, every middle source has at most
\(\binom Mq\) lower \(q\)-neighbors.  Hence

\[
 |N(\mathcal A)|
 \ge {1\over\binom Mq}\sum_{T\in\mathcal A}D_q(T),  \tag{3.4}
\]

and

\[
 \max_{\mathcal A}(|\mathcal A|-|N(\mathcal A)|)
 \le\sum_T\left(1-{D_q(T)\over\binom Mq}\right)_+. \tag{3.5}
\]

Thus every target with \(D_q(T)\ge\binom Mq\) may be retained without
creating any Hall cut.  Formula (3.3) also shows that a deficient family
cannot be confined to one rank-profile fibre.

There is a second compression which is often sharper.  In an arbitrary
bipartite target--source graph, put

\[
 d(T)=|N(T)|,qquad
 Z(X)=\sum_{T\sim X}{1\over d(T)}.                   \tag{3.6}
\]

### Theorem 3.2 (inverse-degree overload certificate)

A maximum target--source matching leaves at most

\[
                         \sum_X(Z(X)-1)_+             \tag{3.7}
\]

targets unmatched.

#### Proof

Give an edge \(TX\) weight

\[
 w_{TX}={1\over d(T)\max\{1,Z(X)\}}.                \tag{3.8}
\]

The load at every source is at most one.  Its total fractional mass is

\[
 \sum_X\min\{Z(X),1\}
 =|\mathcal T|-\sum_X(Z(X)-1)_+,                    \tag{3.9}
\]

because \(\sum_XZ(X)=|\mathcal T|\).  Bipartite matching integrality
gives an integral matching of at least this size. \(\square\)

Equations (3.5) and (3.7) replace an exponential all-subsets audit by an
\(L^1\) target-degree or one-source-load estimate.  They do not enforce
whole-packet chronology or the upper sign.

## 4. The birthday-entropy obstruction to uniform selection

Let

\[
                         b_i(T)=2a_i^-(T).            \tag{4.1}
\]

Then \(D_q(T)=e_q(b_1,\ldots,b_M)\).  Put

\[
 S_1=\sum_i b_i,qquad S_2=\sum_i b_i^2.             \tag{4.2}
\]

When \(q\max_i b_i/S_1=o(1)\), comparison of weighted and uniform
sampling without replacement gives the elementary birthday expansion

\[
 \log {e_q(b)\over\binom Mq}
 =q\log{S_1\over M}
  -\binom q2\left({S_2\over S_1^2}-{1\over M}\right)
  +o(q^2/M).                                         \tag{4.3}
\]

Indeed, multiply \(S_1^q/q!\) by the probability that \(q\) independent
draws from weights \(b_i/S_1\) are distinct, and divide by the analogous
uniform formula.  Inclusion--exclusion for the first collision proves
(4.3); the third-order error is \(O(q^3/M^2)\) here.

For a typical exact-rank lower target, equivalence of ensembles and (1.5)
give

\[
 {S_1\over M}=\mu+o(1),\qquad
 {S_2\over M}=2\mu+2\mu^2+o(1),                    \tag{4.4}
\]

where

\[
 p={m-q\over2m},\qquad \mu={1-p\over p}={m+q\over m-q}.       \tag{4.5}
\]

Substitution in (4.3) yields

\[
 \boxed{
 \log {D_q(T)\over\binom Mq}
 =q\log\mu
  -{1\over2}\left(1+{2\over\mu}\right){q(q-1)\over M}
  +o(q^2/M+1).}                                      \tag{4.6}
\]

At \(q=A\sqrt m\), \(M=m/d\), this is exactly (0.4).  The empirical
moment fluctuations contribute \(O(\sqrt d)=o(d)\), so the statement holds
for \(1-o(1)\) of the exact-rank target layer.

### Corollary 4.1 (bounded-distortion random selection fails)

Suppose a selected-axis/row proposal chooses every compatible rooted
\(q\)-lift with probability at most

\[
                         {K\over\binom Mq}.           \tag{4.7}
\]

If \(\log K=o(q^2/M)\) and \(q\gg\sqrt M\), then a \(1-o(1)\) fraction of
typical lower targets have selected expected load \(o(1)\), and hence are
uncovered with probability \(1-o(1)\).  The same holds above.

In particular, a uniform random priority, a uniformly conjugated compiler,
and independent uniform cell choices fail at every Gaussian depth.

There is an information-theoretic form.  Let \(P\) be the source-uniform,
option-uniform proposal and let \(\pi\) be its target marginal.  If \(U\)
is uniform on targets, then

\[
 D(U\Vert\pi)
 =\left({3\over2}+o(1)\right){q^2\over M}-{q^2\over m}.        \tag{4.8}
\]

Any law whose target marginal is uniform must therefore change the
proposal by likelihood ratio at least
\(\exp((3/2-o(1))q^2/M)\) somewhere.  This is a capacity invariant against
bounded-state symmetric randomization, not against an adaptive global
matching.

At \(p=1/2\), the lower and upper variables \(b^-,b^+\) each have variance
three and covariance one.  Their correlation is only \(1/3\).  Hence the
two required exponential tilts are coupled but are not the same tilt.

## 5. The fixed-priority point-margin counter-cut

Suppose a product cell selects its first \(r\) eligible macroblocks.  In a
fixed ordered \(d\)-pair block, the exact middle-owner count whose first
split pair is position \(j\) is

\[
 R_j=[x^m],2x(1+x^2)^{j-1}(1+x)^{2m-2j}.           \tag{5.1}
\]

Uniformly for \(d=o(\sqrt m)\),

\[
                         {R_j\over W}
 =(1+O(d^2/m))2^{-j}.                                \tag{5.2}
\]

The no-split probability is
\((1+O(d^2/m))2^{-d}\).  Let \(\varepsilon\) be its weighted value.
If fewer than \(r\) of the first \(2r\) blocks are eligible, at least
\(r\) of those blocks are ineligible, so Markov's inequality bounds this
cell mass by \(2\varepsilon\).

Let \(A\) denote total deletion-run mass over the retained factor.  On the
remaining cells, every selected block lies among the first \(2r\)
macroblocks, containing only \(4dr\) physical coordinates out of
\(2dM\).  Therefore

\[
 \boxed{
 \sum_x\left(D_x-\left\lfloor{A\over2dM}\right\rfloor\right)_+
 \ge A\left(1-2\varepsilon-{2r\over M}\right).}     \tag{5.3}
\]

For example, \(r=M/4\) leaves a \((1/2-o(1))A\) point-margin defect.  Thus
the deterministic selector used only to prove owner near-tiling cannot be
the constant-one selector.

There is also a fixed-order within-block cut.  Fair use of the \(d\) pair
positions requires frequency

\[
                         \lambda={r\over Md},         \tag{5.4}
\]

whereas position \(j\) has availability
\(p_j=(1+o(1))2^{-j}\).  Hence every selector using one fixed physical
order has normalized deficit at least

\[
 {1\over d\lambda}\sum_{j=1}^d(\lambda-p_j)_+
 \ge1-{\log_2(Md/r)+2\over d}-o(1).                 \tag{5.5}
\]

Rank-dependent order conjugates can evade (5.5); block hashing without
such conjugates cannot.

## 6. Exact common-depth dynamics inside one product cell

The outer obstruction is not caused by an inability to fuse depths inside
one cell.

### Theorem 6.1 (two-scale cell rotor)

Let \(t=hs\), with \(h\mid2^s\).  Partition the \(t\) physical axes of a
\(Q_t\)-cell into \(h\) labelled groups of size \(s\).  On group \(i\),
choose an oriented Hamilton Gray cycle \(P_i\) of \(Q_s\) and a phase

\[
                         c_i(P_i u)=c_i(u)+1\pmod h. \tag{6.1}
\]

For \(x=(x_0,\ldots,x_{h-1})\), put

\[
 \sigma(x)=\sum_i c_i(x_i)\pmod h,                  \tag{6.2}
\]

and let \(R\) apply \(P_{\sigma(x)}\) to that group and fix the others.
Then \(R\) is a physical owner permutation,

\[
 \sigma(Rx)=\sigma(x)+1,qquad
 R^h=P_0\times\cdots\times P_{h-1}.                 \tag{6.3}
\]

Every window of at most \(h\) moves touches distinct groups and is
geodesic.  Its private flags satisfy

\[
                         G_1(G_jX)=G_{j+1}X.          \tag{6.4}
\]

At every \(q\le h\), both the lower and upper shadow maps are injective
inside the cell.

#### Proof

Advancing one child phase increments (6.2), so the active groups occur in
cyclic order.  At the head, applying the inverse of group
\(\sigma-1\) recovers the unique predecessor; hence \(R\) is bijective.
After \(h\) moves every group has advanced once, proving (6.3).

A \(q\)-window changes one axis in each of \(q\) distinct groups, hence is
geodesic and (6.4) follows by literal tail shift.  A lower shadow identifies
the touched groups by their one-unit local rank deficit.  In each touched
group it identifies the used undirected Gray edge; the fixed orientation
of \(P_i\) recovers its directed tail.  It displays every untouched child
state literally.  Thus it recovers the root.  The upper proof is dual.
\(\square\)

Choosing \(s\ge\lceil\log_2h\rceil\) gives
\(t=O(h\log h)\).  Since a typical logarithmic-block product cell has
\(\Theta(m/\log m)\) axes, it contains such a rotor for every
\(h\log h=o(m/\log m)\), including the required slowly super-Gaussian
heights.  The theorem is one common all-depth, two-sign construction
inside a cell; it does not prevent two different cells from emitting the
same physical target.

## 7. Exact boundary after the all-cuts attack

The following are proved.

* Targetwise compatible-block abundance upgrades to an integral balanced
  \(h\)-fold assignment with one-or-logarithm Hall witnesses.
* The raw fixed-depth source graph has exact degree and profile-fibre Hall
  formulas, plus the inverse-degree overload certificate (3.7).
* Uniform or bounded-distortion random selected-axis rules are rigorously
  closed by the entropy loss (4.6)--(4.8).
* The first-priority deterministic owner tiling is closed by the point
  margin (5.3).
* One cell admits an exact common-depth rotor with literal power consistency
  and both signed shadow injections.

The remaining theorem cannot be stated targetwise.  One product cell is an
indivisible owner component: it must choose one axis set and one compiler
context for all of its owners.  Theorem 2.1 chooses different block lists
for different targets, while Theorem 6.1 assumes that the cell list has
already been fixed.  A valid completion must simultaneously:

1. lift the balanced target-to-block assignment to whole cell choices;
2. bias those choices by the exponential inverse chart multiplicity forced
   by (4.8);
3. control collisions between different target rank profiles and different
   chosen block sets;
4. use the same choice at every depth and for both signs; and
5. retain the laminar SCD census and literal endpoint closure.

No low-complexity theorem presently proves that lift.  Conversely, the
counter-cuts here refute symmetric randomization and fixed priority, not an
adaptive deterministic whole-cell matching.  This is the precise proved
boundary.
