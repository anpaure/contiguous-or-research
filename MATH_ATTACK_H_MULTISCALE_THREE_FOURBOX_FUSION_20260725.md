# Mathematical attack H: multiscale three/four-box fusion

Date: 2026-07-25

## 0. Outcome

This attack does **not** prove

\[
\nu(k)\le(1+o(1))W(k).
\tag{0.1}
\]

It proves two complementary theorems which settle two ends of the
reset/seam problem but do not bridge them.

1. **Middle-productive global fusion exists.**  An exact middle wreath
   factor has a literal realization of length

   \[
   W+\frac{2H+1}{2m+1}W
   =W+o(W)
   \qquad(H=O(\sqrt m)),
   \tag{0.2}
   \]

   in which every baseline position owns a distinct middle target and a
   distinct upper-middle target.  After one coordinate relabelling, these
   same baseline positions provide \(\rho W-o(W)\) genuine cross-parent
   endpoint coincidences adjacent to any positive-mass compact three- or
   four-box family.  Every interval is explicit.  Thus isolated arm resets
   and connector cost are not intrinsic for the two central ranks.  This
   does not show that the same endpoints serve the sloped-shoulder target
   families in the endpoint dual.

2. **Thin/fresh multiscale shell fusion is impossible even at the equal
   four-box point.**  In the exact complementary-shell decomposition of
   \([0,R]^4\), arbitrary ambient witnesses force

   \[
   \mathcal C_R
   \ge
   \left(\frac{289}{3456}-o(1)\right)W_R-2D,
   \qquad n=W_R+D,
   \tag{0.3}
   \]

   units of same-side cross-shell endpoint sharing.  The sharing has an
   exact laminar decomposition over every fusion tree.  A hierarchy of
   height \(h_R\) with at most \(s_R\) typed portal sites at each node can
   have near-width length only if

   \[
   h_Rs_R
   \ge
   \left(\frac{289}{10368}-o(1)\right)R^2.
   \tag{0.4}
   \]

   Hence logarithmic-depth fusion with line-scale or
   \(R\,\mathrm{polylog}\,R\) interfaces is ruled out, even when a root
   portal may touch \(\Theta(R)\) descendants.

Together these theorems sharply constrain the surviving mechanism.  A
successful construction must use baseline middle-owning positions as
portals, a surface-scale interface, or coherent high-degree reuse, and it
must solve multidepth target surjectivity.  Thin fresh seam engineering
cannot finish the proof.  The wreath construction realizes linear
cross-parent sharing at ranks \(m,m+1\), but its noncentral cyclic
intervals may repeat, so it does not discharge the shoulder ledger, cover
every rank, or produce a universal OR word.

No finite search, SAT solver, web search, or numerical experiment is used.

---

## 1. Exact wreath portal fusion

Let

\[
K=2m+1,
\qquad
W=\binom Km.
\]

A wreath is represented by a cyclic order

\[
\pi=(z_0,z_1,\ldots,z_{K-1}).
\]

For cyclic subscripts, put

\[
I_\pi(j,r)=\{z_j,z_{j+1},\ldots,z_{j+r-1}\}.
\tag{1.1}
\]

An exact middle wreath factor \(\mathcal F\) is a family of \(W/K\)
wreaths whose length-\(m\) cyclic intervals partition
\(\binom{[K]}m\).  Such factors are already known exactly.

Fix

\[
1\le H<m.
\]

For one wreath define

\[
E_j=I_\pi(j,m-H),
\qquad 0\le j<K.
\tag{1.2}
\]

### Theorem 1.1 (literal cyclic-arm fusion)

Emit the nonzero block

\[
\boxed{
E_0,E_1,\ldots,E_{K-1},E_0,E_1,\ldots,E_{2H}.}
\tag{1.3}
\]

For every original occurrence \(E_j\), \(0\le j<K\), and every

\[
1\le t\le2H+2,
\]

the physical \(t\)-term interval starting at that occurrence has union

\[
\boxed{
\bigvee_{u=0}^{t-1}E_{j+u}
=I_\pi(j,m-H+t-1).}
\tag{1.4}
\]

In particular, the same physical left endpoint witnesses the full
saturated flag of ranks

\[
m-H,m-H+1,\ldots,m+H+1.
\tag{1.5}
\]

At lengths \(H+1\) and \(H+2\), respectively, it witnesses

\[
X_{\pi,j}=I_\pi(j,m),
\qquad
Y_{\pi,j}=I_\pi(j,m+1).
\tag{1.6}
\]

Across an exact factor, the \(X_{\pi,j}\) partition rank \(m\), the
\(Y_{\pi,j}\) partition rank \(m+1\), and concatenating the blocks gives
one literal word of exact length

\[
\boxed{
W+\frac{2H+1}{K}W.}
\tag{1.7}
\]

#### Proof

The \(t\) sets in the left side of (1.4) are consecutive cyclic intervals
of common length \(m-H\), with consecutive starting points.  Their union
runs from \(z_j\) through

\[
z_{j+m-H+t-2}.
\]

Its length is \(m-H+t-1\).  Since

\[
m-H+t-1
\le m+H+1
<2m+1=K,
\]

the interval has not wrapped all the way around the coordinate cycle, and
its union is exactly the cyclic interval in (1.4).  The repeated prefix in
(1.3) supplies the terms after \(E_{K-1}\), so every displayed witness is
physically contiguous inside its own block.

Putting \(t=H+1\) and \(t=H+2\) gives (1.6).  By definition of an exact
wreath factor, the \(X_{\pi,j}\) partition rank \(m\).  Moreover

\[
[K]\setminus I_\pi(j,m+1)
=I_\pi(j+m+1,m).
\tag{1.8}
\]

Complementation is a bijection from rank \(m\) to rank \(m+1\).
Equation (1.8) therefore shows that the \(Y_{\pi,j}\) also form an exact
partition.

There are \(W/K\) wreaths, and each block in (1.3) has \(K+2H+1\)
letters.  This proves (1.7).  Every \(E_j\) has size \(m-H\ge1\), so the
word satisfies the nonzero-letter convention. \(\square\)

### Corollary 1.2 (sublinear total reset cost)

If \(H=O(\sqrt m)\), then the total duplicate-prefix and intercomponent
cost is

\[
\frac{2H+1}{K}W
=O\left(\frac{W}{\sqrt m}\right)
=o(W).
\tag{1.9}
\]

Every one of the \(W\) original positions is middle-productive: its
\((H+1)\)-term interval is one of the \(W\) distinct middle targets.
Thus the long portal arms have been fused into the width baseline itself;
only the \(o(W)\) duplicated prefixes are resets.

---

## 2. Cross-parent endpoint sharing on the same baseline

Fix a partition of \([K]\) into \(b\) coordinate blocks, where
\(b\ge2\) is fixed, and fix an SCD in each block.  Their products partition
the Boolean lattice into \(b\)-chain boxes.

Let \(\mathscr C\) be any family of these boxes, and define its selected
upper-middle layer

\[
\mathcal U=
\left\{
Y\in\binom{[K]}{m+1}:
Y\text{ belongs to a box in }\mathscr C
\right\}.
\tag{2.1}
\]

### Theorem 2.1 (exact cross-parent incidence)

Assume

\[
|\mathcal U|\ge\rho W
\tag{2.2}
\]

for some fixed \(\rho>0\).  There is one coordinate relabelling of the
word in Theorem 1.1 for which the selected common-left endpoint sharing
excess is at least

\[
\boxed{
|\mathcal U|-\frac{bW}{m+1}
\ge \rho W-o(W).}
\tag{2.3}
\]

The two targets used at each shared endpoint are globally distinct and
their witnessing intervals are the literal intervals in Theorem 1.1.
Moreover, they are legitimate local middle targets of their respective
product boxes.  Indeed, if the factor-chain lower ranks are \(a_i\) and
their heights are \(h_i=n_i-2a_i\), then

\[
\sum_i h_i=K-2\sum_i a_i
\]

is odd.  The lower and upper central local ranks of the product box
therefore translate respectively to

\[
\sum_i a_i+\frac{\sum_i h_i-1}{2}=m,
\qquad
\sum_i a_i+\frac{\sum_i h_i+1}{2}=m+1.
\]

Here the sharing excess means the following restricted, completely
literal ledger.  At the original start corresponding to a pair \((X,Y)\),
count the number of distinct product boxes containing the selected targets
\(X\) and (when \(Y\in\mathcal U\)) \(Y\), minus one; then sum over the
original starts.  Thus every counted unit is an actual common-left
endpoint incidence between two product boxes.

#### Proof

Relabel all coordinates uniformly, and denote the relabelling by \(\sigma\).
Fix one cover

\[
X_{\pi,j}\lessdot Y_{\pi,j}.
\]

Conditional on the image of \(X_{\pi,j}\), the added coordinate is uniform
among its \(m+1\) missing coordinates.  A point of a product of \(b\)
chains has at most \(b\) upper covers in its own box, one for each factor
chain.  Hence

\[
\Pr\bigl(
\sigma X_{\pi,j},\sigma Y_{\pi,j}
\text{ lie in one product box}
\bigr)
\le\frac{b}{m+1}.
\tag{2.4}
\]

For every relabelling, the images of the \(Y_{\pi,j}\) are the entire
rank-\((m+1)\) layer exactly once.  Thus exactly \(|\mathcal U|\) of them
lie in \(\mathcal U\).

Let \(C_{\rm all}(\sigma)\) count all pairs for which \(X\) and \(Y\)
lie in one box, and let \(C_{\mathcal U}(\sigma)\) count only those among
them with \(Y\in\mathcal U\).  Summing (2.4) over all \(W\) pairs gives

\[
\mathbb E C_{\rm all}(\sigma)\le\frac{bW}{m+1}.
\]

Choose a relabelling attaining this upper bound.  At every original
physical start select the \(X\)-witness; when \(Y\in\mathcal U\), also
select the \(Y\)-witness.  If their boxes differ, this one physical start
is a left endpoint for two selected boxes and contributes one unit of
sharing excess.  If their boxes agree, it contributes none.  Therefore the
sharing excess is exactly \(|\mathcal U|-C_{\mathcal U}(\sigma)\), which
is at least

\[
|\mathcal U|-C_{\rm all}(\sigma),
\]

which proves (2.3).  Exactness and global distinctness of the \(X\)'s and
\(Y\)'s were proved in Theorem 1.1. \(\square\)

### Corollary 2.2 (compact three- and four-box sectors)

For \(b=3\), take any fixed positive SCD-height windows defining a
positive-mass family of dominant three-boxes.  For \(b=4\), take any fixed
compact positive window of balanced four-box heights.  In both cases
there is a constant \(\rho>0\) for which (2.2) holds.

#### Proof

For block sizes \(\alpha_iK+O(1)\), a uniform SCD chain height divided by
\(\sqrt K\) has a nondegenerate Rayleigh limit.  Every fixed positive
height window therefore contains a fixed positive fraction of the factor
chains.

For completeness, this height statement follows directly from the exact
chain count.  In an SCD of \(B_n\), the number of chains of height
\(h=n-2r\) is

\[
\binom nr-\binom n{r-1}
=\binom nr\frac{h+1}{n-r+1}.
\tag{2.5a}
\]

Stirling's formula, uniformly for \(h\) in a fixed positive
\(\sqrt n\)-window, gives the Rayleigh density after summing over the
allowed parity class.  In particular every window with nonempty interior
has a positive limiting fraction of the \(W(n)\) chains.

For three selected factor chains of heights \(\Theta(\sqrt K)\), the
upper-central coefficient of their product is
\(\Theta(K)\), uniformly on a compact window with positive lower height.
Indeed, choose two local coordinates in sufficiently short central
intervals of length \(c\sqrt K\); the central-sum equation forces the
third coordinate, which remains legal when \(c>0\) is chosen uniformly
small.  This gives \(\Omega(K)\), while the two free coordinates give
the matching \(O(K)\) bound.  The number of selected
boxes is a fixed positive fraction of
\(\prod_{i=1}^3W(\alpha_iK)\), and

\[
K\frac{\prod_{i=1}^3W(\alpha_iK)}{W(K)}
=\Theta(1).
\tag{2.5}
\]

Here and in (2.6), Stirling gives the displayed ratio uniformly on fixed
positive block proportions.  Thus their upper-middle layers contain
\(\Theta(W)\) targets.

For four chains in a compact positive window, the central coefficient is
\(\Theta(K^{3/2})\).  One elementary lower bound chooses the first three
local coordinates independently in fixed subintervals of length
\(c\sqrt K\) about their midpoints; the fourth coordinate is then forced
and remains legal after choosing \(c>0\) small enough uniformly on the
compact window.  Also

\[
K^{3/2}\frac{\prod_{i=1}^4W(\alpha_iK)}{W(K)}
=\Theta(1).
\tag{2.6}
\]

Hence the selected four-boxes again contribute \(\rho W\) upper-middle
targets for some fixed \(\rho>0\). \(\square\)

Combining Corollaries 1.2 and 2.2 gives a literal
\(W+o(W)\)-length word which covers both central ranks and supplies linear
cross-parent sharing on baseline positions.  This has the same linear
cardinality scale as the sharing forced by the three/four-box duals, but
the target families differ: nothing above proves that these particular
central endpoints serve the dual's sloped shoulders or paired shell
children.  The word does not cover all noncentral targets.

---

## 3. The ambient shoulder toll inside the equal shell

We now prove that thin/fresh multiscale seams cannot replace the
middle-productive mechanism above.

Let

\[
B(p,q,c)=[0,p]\times[0,q]\times[0,c],
\qquad
c\ge p+q.
\]

Put

\[
P=p+q,
\qquad
V=(p+1)(q+1).
\]

Assume \(P>0\).  Equivalently for the ambient application below, every
selected abstract target is a required nonzero target after its rank
translation.  This excludes only the unshifted one-point base for which
the zero-target convention would otherwise matter.

Choose one actual ambient witnessing interval for every target whose
abstract rank lies from \(P-k\) through \(c+k\), where

\[
0\le k\le\min(p,q).
\]

The witnessing word and its intervals may leave the three-box.  Group the
selected targets by common left endpoint and, separately, by common right
endpoint.  Let \(C_L,C_R\) be the numbers of nonempty classes.

### Lemma 3.1 (exact ambient sloped-band toll)

One has

\[
\boxed{
(c+2k)(C_L+C_R-2V)
\ge
(c-P+2k)V
+\frac{k(k+1)(k-6P-4)}3.}
\tag{3.1}
\]

#### Proof

For the two-dimensional base \([0,p]\times[0,q]\), no coordinate cap is
active below rank \(k\).  Put

\[
F=\frac{k(k+1)}2,
\qquad
E=\frac{k(k+1)(k+2)}6,
\qquad
M=\frac{k(k+1)(k-1)}3,
\tag{3.2}
\]

and

\[
J=c-P+2k.
\]

Here \(F\) is the number of omitted base points at either extreme
boundary, \(E\) is the cumulative shoulder omission on one side, and
\(M\) is the sum of the ranks of the omitted low base points.

The band has \(J+1\) layers, boundary size \(V-F\), and total target
count

\[
T=(J+1)V-2E.
\tag{3.3}
\]

Its vertical target-cover capacity is

\[
A_v=T-V=JV-2E.
\tag{3.4}
\]

Use the transverse potential \(\phi(x,y,z)=x+y\).  Its upper-minus-lower
boundary difference is

\[
\Delta_\phi=PF-2M.
\tag{3.5}
\]

Consider one endpoint partition with \(C\) classes.  If adjacent layer
sizes are \(b_i,b_{i+1}\), their occupied class sets intersect in at least
\(b_i+b_{i+1}-C\).  Summing over the \(J\) transitions forces at least

\[
2T-2(V-F)-JC
\tag{3.6}
\]

selected target covers in the partition.  Exactly \(V-F\) classes meet
each extreme boundary; all other starts and ends are internal.
Telescoping \(\phi\) bounds the transverse covers in (3.6) by

\[
\Delta_\phi+P(C-(V-F)).
\tag{3.7}
\]

Thus this partition uses at least

\[
2T-2(V-F)-\Delta_\phi+P(V-F)-(J+P)C
\tag{3.8}
\]

vertical covers.  The two endpoint partitions cannot use the same
vertical target cover: otherwise two distinct targets would have the same
left and right endpoints and hence the same witnessing interval.  Adding
(3.8) for \(C_L,C_R\), and comparing with (3.4), gives

\[
2\bigl(2T-2(V-F)-\Delta_\phi+P(V-F)\bigr)
-(J+P)(C_L+C_R)
\le A_v.
\tag{3.9}
\]

Substitute (3.2)--(3.5), use \(J+P=c+2k\), and collect terms.  The result
is exactly (3.1).  No step used box-confined letters or witnesses.
\(\square\)

### Corollary 3.2 (the \(1/8\)-shoulder constant)

For

\[
(p,q,c,k)=
\left(s,s,2s,\left\lfloor\frac s8\right\rfloor\right)
\tag{3.10}
\]

and, for \(s\ge2\), for

\[
(p,q,c,k)=
\left(
s-1,s-1,2s,
\left\lfloor\frac{s-1}{8}\right\rfloor
\right),
\tag{3.11}
\]

Lemma 3.1 gives

\[
C_L+C_R-2V
\ge
\left(\frac{289}{3456}+o(1)\right)s^2.
\tag{3.12}
\]

#### Proof

Put \(x=1/8\).  In both cases the leading numerator in (3.1), divided by
\(s^3\), is

\[
2x-4x^2+\frac{x^3}{3}
=\frac{289}{1536}.
\]

The denominator \(c+2k\) is

\[
\left(\frac94+o(1)\right)s.
\]

Their quotient is \(289/3456\).  Floors and the shifts by one in (3.11)
affect only \(O(s)\). \(\square\)

---

## 4. Equal four-box cross-shell sharing

Let

\[
Q_R=[0,R]^4,
\qquad
W_R=w(Q_R)
=\frac{2R^3+6R^2+7R+3}{3}.
\tag{4.1}
\]

Indeed, the middle coefficient of \((1+x+\cdots+x^R)^4\) is

\[
\binom{2R+3}{3}-4\binom{R+2}{3}
=\frac{2R^3+6R^2+7R+3}{3};
\]

the standard symmetric-chain decomposition of a product of chains shows
that this middle coefficient is its width.

For \(s\ge1\), define

\[
S_s=[0,s]^2,
\qquad
h_s(j)=
\begin{cases}
(0,j),&0\le j\le s,\\
(j-s,s),&s\le j\le2s,
\end{cases}
\tag{4.1a}
\]

\[
H_s=\{h_s(j):0\le j\le2s\},
\qquad
I_s=\{1,\ldots,s\}\times\{0,\ldots,s-1\},
\tag{4.1b}
\]

and take the actual disjoint packets

\[
\mathcal A_s=S_s\times H_s,
\qquad
\mathcal B_s=H_s\times I_s.
\tag{4.1c}
\]

They satisfy

\[
[0,s]^4
=\mathcal A_s\mathbin{\dot\cup}\mathcal B_s
 \mathbin{\dot\cup}(I_s\times I_s).
\tag{4.1d}
\]

Indeed, \([0,s]^2=H_s\mathbin{\dot\cup}I_s\), and expanding
\((H_s\mathbin{\dot\cup}I_s)^2\) in the order “second pair first” gives
exactly the three pieces in (4.1d).

Put

\[
\tau_s=(R-s,0,R-s,0).
\tag{4.1e}
\]

Iterating (4.1d) gives the exact complementary-shell partition

\[
Q_R=
\{\tau_0\}
\mathbin{\dot\cup}
\bigdotcup_{s=1}^R
\bigl(\tau_s+(\mathcal A_s\mathbin{\dot\cup}\mathcal B_s)\bigr),
\tag{4.2}
\]

To verify the iteration literally, translation identifies

\[
\tau_s+(I_s\times I_s)
=\tau_{s-1}+[0,s-1]^4.
\]

Peeling successively from \(s=R\) to \(s=1\) leaves the single point
\(\tau_0\), proving (4.2).

Moreover,

\[
\mathcal A_s\cong[0,s]^2\times[0,2s],
\qquad
\mathcal B_s\cong[0,s-1]^2\times[0,2s],
\tag{4.3}
\]

as ranked products, except that the displayed abstract coordinates for
\(\mathcal B_s\) have actual rank offset one because \(I_s\) starts in
rank one.  In particular,

\[
w(\mathcal A_s)=(s+1)^2,
\qquad
w(\mathcal B_s)=s^2.
\tag{4.4}
\]

Thus

\[
W_R
=1+\sum_{s=1}^R\bigl((s+1)^2+s^2\bigr).
\tag{4.5}
\]

For every shell child with \(s\ge2\), choose the shoulder witnesses from
Corollary 3.2.  For \(\mathcal A_1\), use Lemma 3.1 with \(k=0\).  The
remaining child \(\mathcal B_1\) has width one;
choose any one translated middle target and one of its literal witnesses.
This gives one left and one right class and no shoulder toll, changing the
later aggregate only by \(O(1)\).

For a physical position \(j\), let \(\ell_j\) be the number of shell
children using it as a selected left endpoint, and define \(r_j\)
similarly.  Put

\[
\mathcal C_R
=\sum_j(\ell_j-1)_+
+\sum_j(r_j-1)_+.
\tag{4.6}
\]

### Theorem 4.1 (equal-shell endpoint-sharing toll)

If a universal ambient word has length

\[
n=W_R+D,
\]

then

\[
\boxed{
\mathcal C_R
\ge
\left(\frac{289}{3456}-o(1)\right)W_R
-2D.}
\tag{4.7}
\]

All witnesses may cross every shell and fusion seam.

#### Proof

The \(\mathcal A_s\) band is centred at abstract rank \(2s\).
The embedded base of \(\mathcal B_s\) has rank one, so its abstract
plateau rank \(2s-1\) also has embedded rank \(2s\).  Translation by
\(\tau_s\) places both width layers at the global middle rank \(2R\).
Hence the width sum in (4.5) is the exact selected middle-antichain
ledger.

For \(s\ge2\), Corollary 3.2 gives a toll

\[
2\frac{289}{3456}s^2+O(s)
\]

for the two children at radius \(s\).  The separately handled radius-one
children alter the sum by only \(O(1)\).  Summing yields

\[
\Gamma_R
=\frac{289}{5184}R^3+O(R^2)
=\left(\frac{289}{3456}+o(1)\right)W_R.
\tag{4.8}
\]

Therefore

\[
\sum_{\text{children}}(C_L+C_R)
\ge2(W_R-1)+\Gamma_R.
\tag{4.9}
\]

On the other hand, double counting endpoint--child incidences gives

\[
\sum_{\text{children}}(C_L+C_R)
=\sum_j\ell_j+\sum_jr_j
\le2n+\mathcal C_R.
\tag{4.10}
\]

Combining (4.8)--(4.10) gives

\[
\mathcal C_R\ge\Gamma_R-2D-2,
\]

which is (4.7). \(\square\)

For one packet \(\mathcal A_s\cup\mathcal B_s\), a word of combined width
plus \(o(s^2)\) consequently needs at least

\[
\left(\frac{289}{1728}-o(1)\right)s^2
\tag{4.11}
\]

typed same-side endpoint coincidences.  An \(o(s^2)\)-support seam cannot
prove the packet lemma.

---

## 5. Exact laminar sharing identity and hierarchy ceiling

Let \(\mathcal T\) be any rooted fusion tree whose leaves are the
\(2R\) shell children.  For an internal node \(v\), a physical position
\(j\), and a side \(\sigma\in\{L,R\}\), let

\[
a_{v,j,\sigma}
\]

be the number of child subtrees of \(v\) which contain at least one leaf
using \(j\) as a \(\sigma\)-endpoint.

### Lemma 5.1 (exact laminar multiplicity)

One has

\[
\boxed{
\mathcal C_R
=
\sum_{v\text{ internal}}\sum_j\sum_{\sigma\in\{L,R\}}
(a_{v,j,\sigma}-1)_+.}
\tag{5.1}
\]

#### Proof

Fix one typed site \((j,\sigma)\), and let \(S\) be its nonempty set of
incident leaves.  For every internal \(v\), let \(a_v(S)\) be the number
of child subtrees meeting \(S\).  We claim

\[
|S|-1=\sum_v(a_v(S)-1)_+.
\tag{5.2}
\]

Induct on the minimal subtree spanning \(S\).  If its root meets
\(a\) child subtrees in sets of sizes \(n_1,\ldots,n_a\), the induction
hypothesis in those subtrees gives

\[
\sum_{i=1}^a(n_i-1)+(a-1)
=|S|-1.
\]

This is (5.2).  Summing it over all typed sites proves (5.1).
\(\square\)

### Corollary 5.2 (bounded arity)

If the fusion tree has arity at most \(b\), and \(P_{v,\sigma}\) is the
set of actual positions shared across at least two child subtrees of \(v\)
on side \(\sigma\), then

\[
\boxed{
\sum_{v,\sigma}|P_{v,\sigma}|
\ge\frac{\mathcal C_R}{b-1}.}
\tag{5.3}
\]

Indeed,

\[
(a_{v,j,\sigma}-1)_+
\le(b-1)\mathbf1_{\{a_{v,j,\sigma}\ge2\}},
\]

and (5.3) follows from (5.1).

Thus every bounded-arity hierarchy whose total actual node-side interface
support is \(o(W_R)\) has

\[
D\ge
\left(\frac{289}{6912}-o(1)\right)W_R.
\tag{5.4}
\]

This conclusion concerns actual repeated endpoint sites, not merely the
declared connector length.  A cross-seam interval may begin deep inside a
child epoch, in which case that baseline position belongs to
\(P_{v,\sigma}\) and is charged correctly.

### Theorem 5.3 (hierarchical thin-portal ceiling)

Assume every leaf has at most \(h_R\) internal ancestors and define

\[
s_R=\max_{v\text{ internal}}
\left|\{(j,\sigma):a_{v,j,\sigma}\ge2\}\right|.
\tag{5.4a}
\]

Thus \(s_R\) is the maximum number of genuinely shared typed sites at one
node.  Then

\[
\boxed{
\mathcal C_R\le2Rh_Rs_R.}
\tag{5.5}
\]

Consequently, \(D=o(W_R)\) requires

\[
\boxed{
h_Rs_R
\ge
\left(\frac{289}{10368}-o(1)\right)R^2.}
\tag{5.6}
\]

If \(s_R\) counts untyped physical positions rather than left/right typed
sites, the constant in (5.6) is \(289/20736\).

#### Proof

At a fixed node \(v\), one typed site contributes at most

\[
|L(v)|-1,
\]

where \(L(v)\) is the descendant-leaf set.  Therefore

\[
\mathcal C_R
\le s_R\sum_v|L(v)|.
\]

Double counting leaf--ancestor pairs gives

\[
\sum_v|L(v)|\le(2R)h_R,
\]

which proves (5.5).

By Theorem 4.1,

\[
\mathcal C_R
\ge
\frac{289}{5184}R^3-2D-O(R^2).
\]

Combine this with (5.5).  If \(D=o(R^3)\), division by \(2R\) gives
(5.6).  One physical position can be typed on both sides, producing the
factor two in the untyped version. \(\square\)

In particular, a dyadic hierarchy with \(h_R=O(\log R)\) needs

\[
s_R=\Omega(R^2/\log R)
\tag{5.7}
\]

typed sites at some node.  A line-scale
\(O(R\,\mathrm{polylog}\,R)\) interface at every node is insufficient.
This remains true even if a root site has descendant degree
\(\Theta(R)\).

### Corollary 5.4 (minimum number of cross-radius portal positions)

All selected shoulder targets in Theorem 4.1 lie in global ranks

\[
[2R-H_R,2R+H_R],
\qquad
H_R=\left\lceil\frac R8\right\rceil.
\]

For \(\mathcal B_s\), the abstract band acquires the rank-one embedding
offset, so its deviations from local rank \(2s\) are at most

\[
1+\left\lfloor\frac{s-1}{8}\right\rfloor
=\left\lceil\frac s8\right\rceil\le H_R.
\]

The \(\mathcal A_s\) deviations are only \(\lfloor s/8\rfloor\), so no
selected endpoint target lies outside the displayed global band.

At one fixed typed endpoint (left or right) they form a chain and hence
contain at most one target of each rank.  If \(P_R\) is the number of
physical positions with any cross-shell same-side reuse, then

\[
\mathcal C_R\le4H_RP_R.
\]

For \(D=o(W_R)\), Theorem 4.1 therefore gives

\[
\boxed{
P_R
\ge
\left(\frac{289}{2592}-o(1)\right)R^2.}
\tag{5.8}
\]

If only \(O(R^2)\) positions are used, their average endpoint-box excess
degree is \(\Omega(R)\).  Thus sparse support is possible only through
coherent unbounded cross-radius reuse.

---

## 6. Exact logical status

### Unconditional advances

The following are proved above.

1. Exact wreath factors admit a literal \(W+O(HW/m)\) portal word with all
   \(W\) positions middle-productive.
2. The same word covers both central ranks exactly.
3. One relabelling supplies \(\rho W-o(W)\) globally distinct,
   central-rank cross-parent endpoint coincidences adjacent to every
   positive-mass compact three/four-box family.  The other box in a pair
   need not belong to that family.
4. Equal complementary shells require a positive fraction of \(W_R\) in
   cross-shell endpoint sharing under arbitrary ambient witnesses.
5. Every bounded-arity thin/fresh hierarchy, and every logarithmic-depth
   hierarchy with \(R\,\mathrm{polylog}\,R\)-scale node interfaces, pays
   linear excess.

Thus two rigorous facts replace the reset heuristic: fresh thin portals
are too small in the stated hierarchical architectures, while baseline
middle-productive portals exist with \(o(W)\) total reset cost at the two
central ranks.  Identifying those portals with the shoulder incidences is
still unproved.

### Smallest remaining lemma

The word in Theorem 1.1 has a full depth-\(H\) cyclic flag at every
baseline position.  Unlike ranks \(m\) and \(m+1\), its noncentral targets
need not be globally distinct.  Relabelling preserves those repetitions.

The smallest remaining high-degree extraction statement is:

> **Pointed cyclic-flag extraction — UNPROVED.**  For every fixed
> \(A>0\), with \(H=\lceil A\sqrt m\rceil\), find one exact wreath factor
> and \(O(W/H)\) pointed starts whose depth-\(H\) cyclic flags contain
> \(\Omega(W)\) globally distinct targets in the prescribed audited
> sloped-shoulder families of the compact three/four-box sector, with
> distinct product boxes within each pointed flag and with total
> endpoint--box incidence at least the corresponding endpoint-dual demand.

This would give sparse high-degree portals via Theorem 1.1 with no new
connector cost.  It still would not by itself prove universality at every
depth.  The full constant-one theorem requires the stronger common-factor
multidepth surjectivity/balancing statement, or an equally strong residual
repair theorem.

### Adversarial audit

1. **No fractional ownership.**  The wreath factor is exact, every block
   is an actual nonzero word, and every witness in (1.4) is one physical
   interval.
2. **Wraparound.**  The repeated prefix has \(2H+1\) terms, exactly enough
   for the longest \(2H+2\)-term interval starting at \(E_{K-1}\).
3. **Upper-middle distinctness.**  It follows from the exact complement
   identity (1.8), not from a random-shadow heuristic.
4. **Cross-box probability.**  Only the \(b\) internal upper covers of a
   product-box point are counted.  Conditional on \(X\), the added
   coordinate is uniform among all \(m+1\) possibilities.
5. **No sparse-degree overclaim.**  Theorem 2.1 uses a linear number of
   baseline positions of degree two.  It does not prove that
   \(O(W/H)\) pointed flags contain globally distinct noncentral targets.
   Nor does it prove that its central-rank pairs are the sloped-shoulder or
   paired-child incidences counted in Theorem 4.1.
6. **Ambient shell witnesses.**  Lemma 3.1 uses only endpoint chain
   partitions and target-poset covers; witnesses may cross every shell
   seam.
7. **Rank offset in \(\mathcal B_s\).**  Its embedded base has rank one.
   Abstract rank \(2s-1\) therefore aligns with the rank-\(2s\) layer of
   \(\mathcal A_s\), and translation puts both at global rank \(2R\).
8. **Actual interface sites.**  The hierarchy theorem counts all repeated
   endpoint positions, including starts lying deep inside child epochs.
   Connector length alone is not its hypothesis.
9. **Scope of the no-go.**  A root surface with \(\Theta(R^2)\) shared
   sites, a depth-\(\Theta(R)\) comb, or unrestricted baseline reuse is not
   excluded.  Theorem 1.1 explicitly realizes the baseline-reuse escape.
10. **No universality claim.**  The constructed word covers two central
    ranks and supplies generic cross-box sharing of the correct linear
    cardinality scale, but it does not identify those pairs with the
    shoulder ledger or cover all nonzero masks.  Therefore (0.1) remains
    open.
