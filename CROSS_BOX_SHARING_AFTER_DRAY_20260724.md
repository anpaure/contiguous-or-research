# Cross-box sharing after the dominant-ray obstruction

Date: 2026-07-24

## 0. Verdict

This note does not prove the constant-one contiguous-OR theorem. It proves
an exact cross-box accounting theorem for the three-block Boolean SCD
decomposition and a corresponding sparse-portal no-go.

The audited dominant-ray theorem says that a positive family of three-chain
boxes has a genuine quadratic local excess over its width. That excess
cannot be dismissed merely by saying that intervals may cross box seams.
For any global Boolean word there are two exact ledgers:

1. projecting every global letter to every product box gives a valid local
   range-maximum word, so the sum of the standalone local costs is paid by
   total **letter--box activity**;
2. restricting chosen global witnesses to a product box gives the two
   orthogonal endpoint-chain partitions used in the local plateau dual, so
   the same quadratic excess is paid by total **endpoint--box sharing**.

For three equal blocks of even size \(s\), any global construction of
near-width length \(n=W(3s)+o(W(3s))\) is forced by these ledgers to have

\[
 \boxed{\text{cross-box sharing capacity }=\Omega(W(3s)).}
\]

Consequently, a construction of length \(W(3s)+o(W(3s))\) cannot be made
from boxwise words joined by only \(o(W(3s))\) portal positions if each
portal interacts with only \(O(1)\) boxes. In particular, one
\(O(\sqrt s)\)-long bounded-degree portal corridor per product box is too
small. A successful cross-box construction must instead use either

* a linear number of shared physical positions;
* corridors of the full local surface scale \(\Omega(s)\) per box; or
* positions of unbounded box degree, hence genuinely global rather than
  nearest-neighbour sharing.

This is a repair-capacity theorem, not a general impossibility theorem.
High-degree global sharing remains a real escape route.

No web search or finite computation is used below.

## 1. The three-block SCD partition

Let \(s\) be even and split a set of \(3s\) Boolean coordinates into three
blocks

\[
 X_1\sqcup X_2\sqcup X_3.
\]

Fix an arbitrary saturated symmetric-chain decomposition
\(\mathcal D_i\) of \(2^{X_i}\). Write a chain of edge height \(p\) as

\[
 C_0\subset C_1\subset\cdots\subset C_p,
 \qquad C_t=C_0\cup\{e_1,\ldots,e_t\}.
 \tag{1.1}
\]

A triple \(\mathbf C=(C^{(1)},C^{(2)},C^{(3)})\) is a product box

\[
 \mathcal B_{\mathbf C}
 =\bigl\{
 C^{(1)}_x\cup C^{(2)}_y\cup C^{(3)}_z:
 0\le x\le p,\ 0\le y\le q,\ 0\le z\le r
 \bigr\}.
 \tag{1.2}
\]

The boxes partition \(2^{[3s]}\). Since every factor chain is symmetric,
the local middle layer of the box is the global rank-\(3s/2\) layer. If
\(w(p,q,r)\) is the width of the grid
\([0,p]\times[0,q]\times[0,r]\), then

\[
 \boxed{
 \sum_{\mathbf C}w(p_{\mathbf C},q_{\mathbf C},r_{\mathbf C})
 =\binom{3s}{3s/2}=:W_{3s}.}
 \tag{1.3}
\]

Indeed, each box contributes exactly \(w(p,q,r)\) points to the global
middle layer, and the boxes partition that layer.

For brevity put

\[
 W_s=\binom{s}{s/2},
 \qquad
 \mathscr B_s=|\mathcal D_1||\mathcal D_2||\mathcal D_3|=W_s^3.
 \tag{1.4}
\]

## 2. Exact letter-projection ledger

For a product box \(\mathcal B=\mathcal B_{\mathbf C}\), define

\[
 \pi_{\mathcal B}(A)_i
 =\max\bigl(\{t:e^{(i)}_t\in A\}\cup\{0\}\bigr),
 \qquad i=1,2,3,
 \tag{2.1}
\]

for every Boolean mask \(A\subseteq[3s]\). Coordinates belonging to the
bottom of a chain, or outside its variable set, are ignored. The crucial
identity is the exact join law

\[
 \pi_{\mathcal B}(A\cup A')
 =\max\{\pi_{\mathcal B}(A),\pi_{\mathcal B}(A')\}
 \tag{2.2}
\]

coordinatewise.

### Lemma 2.1 -- projection of a global word

Let \(A=(A_1,\ldots,A_n)\) be a nonzero Boolean word covering every mask in
\(\mathcal B\). Apply \(\pi_{\mathcal B}\) to its letters and delete every
zero image. The resulting word is a nonzero range-maximum word covering
every nonzero point of
\([0,p]\times[0,q]\times[0,r]\).

#### Proof

The embedded grid point \((x,y,z)\) is

\[
 T=C^{(1)}_x\cup C^{(2)}_y\cup C^{(3)}_z.
\]

Choose a global witnessing interval \(I\) with
\(\bigcup_{j\in I}A_j=T\). Equation (2.2) gives

\[
 \max_{j\in I}\pi_{\mathcal B}(A_j)
 =\pi_{\mathcal B}(T)=(x,y,z).
\]

If the target is not the local origin, at least one image in \(I\) is
nonzero. Deleting zero images merely compresses \(I\); the retained images
from \(I\) remain consecutive and have the same maximum. This proves the
claim. \(\square\)

For a global letter \(A_j\), define its product-box activity degree

\[
 d_j=\#\{\mathcal B:\pi_{\mathcal B}(A_j)\ne(0,0,0)\}.
 \tag{2.3}
\]

### Theorem 2.2 -- exact activity ledger

Every universal Boolean word satisfies

\[
 \boxed{
 \sum_{\mathcal B}g_3(p_{\mathcal B},q_{\mathcal B},r_{\mathcal B})
 \le \sum_{j=1}^n d_j.}
 \tag{2.4}
\]

#### Proof

By Lemma 2.1, the number of nonzero projected letters for a fixed box is at
least its \(g_3\)-value. Sum this inequality over the boxes and reverse the
order of summation. \(\square\)

Define

\[
 Z=\#\{j:d_j=0\},
 \qquad
 \mathcal C_{\rm let}=\sum_{j:d_j\ge2}(d_j-1).
 \tag{2.5}
\]

Then

\[
 \sum_jd_j=n-Z+\mathcal C_{\rm let}.
 \tag{2.6}
\]

Thus, writing

\[
 \Delta_s=
 \sum_{\mathcal B}
 \bigl(g_3(p_{\mathcal B},q_{\mathcal B},r_{\mathcal B})
       -w(p_{\mathcal B},q_{\mathcal B},r_{\mathcal B})\bigr),
 \tag{2.7}
\]

equations (1.3), (2.4), and (2.6) give the exact sharing inequality

\[
 \boxed{
 \mathcal C_{\rm let}
 \ge \Delta_s-(n-W_{3s})+Z.}
 \tag{2.8}
\]

This is the first precise sense in which local excess may be amortized:
one physical letter is counted once for every local projected word in which
it is nonzero. There is no free seam saving outside this incidence ledger.

## 3. Endpoint restriction survives every seam

The preceding ledger counts activity whether or not a letter is used in a
chosen witness. There is also a sharper witness-level statement.

Consider an embedded grid box of heights \(p,q,r\), where

\[
 r\ge p+q,
 \qquad w=(p+1)(q+1),
 \qquad H=r-p-q.
 \tag{3.1}
\]

The full plateau layers are the local ranks

\[
 p+q,p+q+1,\ldots,r,
 \tag{3.2}
\]

each of size \(w\). Choose arbitrary global witnessing intervals for all
targets in these layers. Let \(C_L\) be the number of distinct physical
left endpoints among the chosen witnesses, and \(C_R\) the analogous
number of right endpoints.

### Lemma 3.1 -- translated plateau endpoint inequality

Irrespective of all targets and word letters outside the box,

\[
 \boxed{
 (C_L-w)+(C_R-w)\ge \frac{wH}{r}.}
 \tag{3.3}
\]

#### Proof

Group the selected box targets by common left endpoint. Targets in one
group form an inclusion chain, because extending an interval to the right
only increases its union. The right-endpoint groups are chains for the
same reason. The two partitions are orthogonal: a left group and a right
group cannot share two distinct targets, since that would assign two
different unions to one physical interval.

We audit one endpoint partition with \(C=w+\delta\) chains. In two
consecutive plateau layers, the sets of occupied chains both have size
\(w\), so their intersection has size at least \(w-\delta\). Every common
chain supplies a genuine grid cover. Across the \(H\) adjacent layer
pairs, the partition therefore uses at least

\[
 H(w-\delta)
 \tag{3.4}
\]

grid covers.

Put \(\phi(x,y,z)=x+y\), so \(0\le\phi\le p+q\). The bottom and top
plateau layers have the same \(\phi\)-multiset. Exactly \(w\) partition
chains meet each boundary; the other \(\delta\) starts and the other
\(\delta\) ends are internal. Telescoping \(\phi\) on all chains shows
that the total horizontal increase is at most

\[
 (p+q)\delta.
 \tag{3.5}
\]

Hence the number of covers in the \(z\)-direction used by this partition
is at least

\[
 H(w-\delta)-(p+q)\delta=Hw-r\delta.
 \tag{3.6}
\]

There are exactly \(wH\) vertical covers in the plateau slab. A vertical
cover cannot occur in both endpoint partitions, by their orthogonality.
Applying (3.6) to both partitions gives

\[
 2Hw-r\bigl((C_L-w)+(C_R-w)\bigr)\le wH,
\]

which is (3.3). Notice that no interval is required to stay inside the
box. Only its target and its physical endpoint are used. \(\square\)

This is the exact seam certificate. A witness may cross any number of box
boundaries, and may use arbitrary foreign letters. It is still charged to
its two physical endpoints, and Lemma 3.1 remains valid.

## 4. A positive-density family of dominant boxes

The edge-height distribution of the chains in an SCD of \(B_s\) is fixed.
For \(h\equiv s\pmod2\), the number of height-\(h\) chains is

\[
 a_s(h)
 =\binom{s}{(s-h)/2}-\binom{s}{(s-h)/2-1}.
 \tag{4.1}
\]

This follows by subtracting the number of chains which have already begun
one rank earlier.

### Lemma 4.1 -- Gaussian chain-height windows

For fixed \(0<a<b<\infty\),

\[
 \frac1{W_s}
 \sum_{\substack{a\sqrt s\le h\le b\sqrt s\\h\equiv s\ (2)}}
 a_s(h)
 \longrightarrow
 \kappa(a,b):=e^{-a^2/2}-e^{-b^2/2}>0.
 \tag{4.2}
\]

#### Proof

Uniformly for \(h=u\sqrt s\) in a fixed compact positive interval,
Stirling's formula and (4.1) give

\[
 \frac{a_s(h)}{W_s}
 =\frac{2u}{\sqrt s}e^{-u^2/2}+o(s^{-1/2}).
 \tag{4.3}
\]

The admissible heights are spaced by \(2\), so (4.3) is the Riemann sum
for

\[
 \int_a^b u e^{-u^2/2}\,du
 =e^{-a^2/2}-e^{-b^2/2}.
 \quad\square
\]

Take the fixed windows

\[
 I_s=[\sqrt s,1.1\sqrt s],
 \qquad
 J_s=[3\sqrt s,3.1\sqrt s],
 \tag{4.4}
\]

with the necessary parity rounding. Let \(L_s\) and \(K_s\) be the
numbers of chains with heights in \(I_s\) and \(J_s\), respectively. By
Lemma 4.1,

\[
 L_s=(\kappa_L+o(1))W_s,
 \qquad
 K_s=(\kappa_H+o(1))W_s,
 \tag{4.5}
\]

where

\[
 \kappa_L=e^{-1/2}-e^{-121/200}>0,
 \qquad
 \kappa_H=e^{-9/2}-e^{-961/200}>0.
 \tag{4.6}
\]

Call a product box **dominant** when its first two chain heights lie in
\(I_s\) and its third lies in \(J_s\). There are \(L_s^2K_s\) such boxes.
For every sufficiently large \(s\), a dominant box satisfies

\[
 r-p-q\ge0.7\sqrt s,
 \qquad
 \frac{r-p-q}{r}\ge\frac15,
 \qquad
 w=(p+1)(q+1)\ge s.
 \tag{4.7}
\]

Consequently Lemma 3.1 forces endpoint excess at least \(w/5\) in each
dominant box. The standalone range-maximum obstruction gives the parallel
letter statement

\[
 g_3(p,q,r)-w
 \ge \frac{w(r-p-q)}{2r}
 \ge\frac{w}{10}.
 \tag{4.8}
\]

Finally, central-binomial asymptotics give

\[
 \frac{sW_s^3}{W_{3s}}\longrightarrow\frac{2\sqrt3}{\pi}.
 \tag{4.9}
\]

Equations (4.5)--(4.9) show that there is an absolute constant
\(\delta_0>0\) such that, for all sufficiently large even \(s\),

\[
 \boxed{
 \sum_{\mathcal B}
 \bigl(g_3(\mathcal B)-w(\mathcal B)\bigr)
 \ge\delta_0W_{3s},}
 \tag{4.10}
\]

Here every positive-height unselected box contributes nonnegatively because
\(g_3(p,q,r)\ge w(p,q,r)\): grouping represented targets by a common
right endpoint gives a chain partition with at most as many chains as
word positions. The only exception is the all-zero abstract box, for which
\(g_3=0\) and \(w=1\). The number of such product boxes is

\[
 \left(
 W_s-\binom{s}{s/2-1}
 \right)^3
 =
 \left(\frac{W_s}{s/2+1}\right)^3
 =o(W_{3s}).
 \tag{4.10a}
\]

Thus their total negative contribution is absorbed by decreasing the fixed
constant \(\delta_0\).

The aggregate endpoint excess from the dominant boxes is at least

\[
 \boxed{
 \sum_{\mathcal B\ {\rm dominant}}
 \frac{w_{\mathcal B}(r_{\mathcal B}-p_{\mathcal B}-q_{\mathcal B})}
      {r_{\mathcal B}}
 \ge 2\delta_0W_{3s}.}
 \tag{4.11}
\]

For example, after increasing the threshold in \(s\), one may take any

\[
 0<\delta_0<
 \frac{\sqrt3}{80\pi}\,\kappa_L^2\kappa_H.
 \tag{4.12}
\]

The numerical size of this deliberately conservative constant is
irrelevant; its positivity is the point.

## 5. Forced global endpoint sharing

Fix one witnessing interval for every Boolean mask represented by a
universal word \(A=(A_1,\ldots,A_n)\).

For a dominant product box use all its plateau targets. For every other
box use only its local middle layer. For a physical position \(j\), let

\[
 \ell_j=\#\{\mathcal B:j\text{ is a left endpoint of at least one
 selected target of }\mathcal B\},
 \tag{5.1}
\]

and define \(r_j\) analogously for right endpoints. Put

\[
 \mathcal C_{\partial}
 =\sum_{j=1}^n
 \bigl((\ell_j-1)_++(r_j-1)_+\bigr).
 \tag{5.2}
\]

### Theorem 5.1 -- endpoint-sharing lower bound

For all sufficiently large even \(s\), every universal Boolean word on
\(3s\) coordinates satisfies

\[
 \boxed{
 \mathcal C_{\partial}
 \ge 2\delta_0W_{3s}-2(n-W_{3s}).}
 \tag{5.3}
\]

#### Proof

For every box, either endpoint partition needs at least \(w_{\mathcal B}\)
chains to contain its local middle antichain. Lemma 3.1 adds the displayed
excess for every dominant box. Hence, by (1.3) and (4.11),

\[
 \sum_{\mathcal B}(C_L(\mathcal B)+C_R(\mathcal B))
 \ge 2W_{3s}+2\delta_0W_{3s}.
 \tag{5.4}
\]

Double counting endpoint--box incidences gives

\[
 \sum_{\mathcal B}C_L(\mathcal B)=\sum_j\ell_j,
 \qquad
 \sum_{\mathcal B}C_R(\mathcal B)=\sum_jr_j.
 \tag{5.5}
\]

For nonnegative integers \(x_j\),

\[
 \sum_jx_j
 \le n+\sum_j(x_j-1)_+.
 \tag{5.6}
\]

Apply (5.6) to \(\ell_j\) and \(r_j\), combine with (5.4)--(5.5), and
rearrange. \(\square\)

Thus a width-scale word must not merely contain seam-crossing intervals.
Its selected witnesses must reuse physical left and right endpoints across
a linear number of box incidences.

## 6. Sparse bounded-capacity portals cannot amortize the gap

The exact ledgers immediately give a clean architecture-level no-go.

### Corollary 6.1 -- endpoint portal capacity

Suppose at most \(P_s\) physical positions have \(\ell_j\ge2\) or
\(r_j\ge2\), and suppose

\[
 \ell_j,r_j\le D
 \tag{6.1}
\]

for an absolute constant \(D\). Then

\[
 \boxed{
 n\ge
 (1+\delta_0)W_{3s}-(D-1)P_s.}
 \tag{6.2}
\]

In particular, if \(P_s=o(W_{3s})\), then

\[
 n\ge(1+\delta_0-o(1))W_{3s}.
 \tag{6.3}
\]

#### Proof

Under (6.1),

\[
 \mathcal C_{\partial}\le2(D-1)P_s.
\]

Substitute this in (5.3) and divide by two. \(\square\)

### Corollary 6.2 -- letter portal capacity

Suppose at most \(P_s\) letters have \(d_j\ge2\), and all of them satisfy
\(d_j\le D\). Then

\[
 \boxed{
 n\ge
 (1+\delta_0)W_{3s}-(D-1)P_s+Z.}
 \tag{6.4}
\]

This is (2.8), (4.10), and
\(\mathcal C_{\rm let}\le(D-1)P_s\).

The number of product boxes is

\[
 \mathscr B_s=W_s^3=\Theta(W_{3s}/s).
 \tag{6.5}
\]

Therefore a scheme in which every multiply used position belongs to one
of at most one designated portal corridor of length \(u_s=o(s)\) per box
has at most

\[
 P_s\le u_s\mathscr B_s=o(W_{3s})
 \tag{6.6}
\]

portal positions, even before overlaps are removed. If each portal is
shared by only \(O(1)\) neighbouring boxes, Corollary 6.1 or 6.2 rules out
length \(W_{3s}+o(W_{3s})\). In particular,

\[
 u_s=O(\sqrt s)
\]

is insufficient. The local box sides have scale \(R=\Theta(\sqrt s)\),
so this says that \(O(R)\)-length seams cannot amortize the
\(\Theta(R^2)\) local gaps. Bounded-degree sharing needs
\(\Omega(R^2)=\Omega(s)\) corridor capacity per box.

## 7. Why this does not rule out the global conjecture

The bounded-degree qualification is essential. Product-box projection
degree can be enormous.

For one block SCD, let \(v_x\) be the number of chains in which coordinate
\(x\) is a variable increment. Summing over coordinates and chains gives

\[
 \sum_{x\in X_i}v_x
 =\sum_{C\in\mathcal D_i}\operatorname{height}(C)
 =2^s-W_s.
 \tag{7.1}
\]

Hence some coordinate satisfies

\[
 v_x\ge\frac{2^s-W_s}{s}.
 \tag{7.2}
\]

The singleton letter \(\{x\}\) then has nonzero projection in

\[
 v_xW_s^2
 \tag{7.3}
\]

three-block product boxes. This degree grows exponentially. A small
number of such high-degree letters has enough raw incidence capacity to
evade Corollary 6.2. Likewise, one physical endpoint can in principle be
used by witnesses belonging to many boxes.

The theorem therefore separates two notions which were previously easy to
conflate:

* **local seam sharing:** a portal is reused by a bounded number of nearby
  boxes; this cannot erase the audited local quadratic gap unless the
  portal corridors already have quadratic local size;
* **genuine global sharing:** a letter or endpoint simultaneously serves an
  unbounded family of boxes; this is not excluded and is exactly the kind
  of mechanism a successful product construction now needs.

Raw incidence is necessary but not sufficient. High-degree letters must
still avoid contaminating every selected interval, and high-degree
endpoints must still support compatible nested suffix unions. No theorem
here constructs that chronology.

There is one other escape consistent with the theorem: fuse a bounded
number of adjacent children using a packet word whose entire
\(\Theta(s)=\Theta(R^2)\) surface is shared. This is not a short-seam
repair; it pays exactly the corridor scale forced by Corollary 6.1. Thus a
four-box adjacent-packet theorem remains viable, but an \(O(R)\)-connector
version of it does not.

## 8. Seam audit and exact scope

The places where cross-box contamination could have invalidated the
argument have all been isolated:

1. **Projected intervals.** A global witness has every letter contained in
   its target. The join homomorphism (2.2) therefore gives the exact local
   maximum. Deleting zero projections preserves contiguity after
   compression.
2. **Crossing witnesses.** Lemma 3.1 never assumes a witness is contained
   in a boxwise subword. It uses only its two physical endpoints and its
   target.
3. **Translated bases.** Chain-bottom coordinates are ignored by
   \(\pi_{\mathcal B}\); they are common to every target of the translated
   box and do not alter the local maximum coordinates.
4. **Vertical capacity.** The \(wH\) covers in Lemma 3.1 are internal grid
   covers of one product box. Orthogonality forbids the two endpoint
   partitions from sharing one; no assertion about covers in another box
   is needed.
5. **Global middle accounting.** Equation (1.3) is exact because every
   product box is symmetric about global rank \(3s/2\).
6. **Positive aggregate mass.** The Gaussian windows have a fixed positive
   fraction of all block chains, while each selected box contributes
   \(\Theta(s)\). Equation (4.9) converts their total into
   \(\Theta(W_{3s})\).

What is proved is the boxed forced-sharing theorem and its sparse
bounded-capacity portal corollaries. What is not proved is a lower bound
against unbounded-degree global sharing, a four-box fusion theorem, an MTF
realization of the required incidence, or the constant-one conjecture.

The exact surviving cross-box target is now:

\[
 \boxed{
 \begin{gathered}
 \text{construct a width-scale word whose letters and witness endpoints}\\
 \text{have }\Omega(W)\text{ useful cross-box incidence, concentrated in}\\
 \text{unbounded-degree global portals, while preserving all interval pins.}
 \end{gathered}}
\]

That is genuinely different from concatenating local \(g_3\)-words with
short seams.
