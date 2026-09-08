# Self-containment audit for the direct punctured route

**Date:** 2026-08-22

**Scope:** read-only audit of Sections 4.3--4.6 of
MASTER_HANDOFF.md.  This file gives insertion-ready proofs; it does not
edit the handoff.

## 1. Verdict

The four sections accurately state the frozen results, but they are not
mathematically self-contained.  The following assertions currently depend
on external files:

1. Section 4.3: deck injectivity; the two target degrees; optimality of the
   uniform fractional matching; the pair-codegree formula and inventory;
   the expansion and path localization of the internal pair mass; the
   first-bite expectation; the maximum pair codegree; and the
   common-partial-transversal counterexample.
2. Section 4.4: the punctured-circulant density inequality and all three
   inputs to the global boundary-codegree theorem.
3. Section 4.5: the connected-polymer/exponential-formula estimate; the
   factorial expansion producing annealed duplicate control; and the
   rooted covariance/polymer proof of the fixed-target variance bound.
4. Section 4.6: the infinitesimal drift identity; the deduction of the
   third overlap moment from the boundary theorem; the isolated-count
   covariance lemma; the Jensen bite estimate; and the empirical-floor
   bootstrap.

The blocks below are concise insertion-ready proofs for Sections 4.3--4.6.
They may be inserted at the indicated points without relying on the cited
theorem files for validity.

## 2. Insertion after the displayed polymer estimate in Section 4.5

Insert the following immediately after
\(\mathcal P_2(z)\le c_1(z^2/r^2+z^4/r^2)\).

### Proof of the polymer estimate

Write a nonempty edge subgraph of \(B_r\) as the disjoint union of its
connected components.  In a graph of maximum degree four, an exploration
from a prescribed root vertex encodes every connected \(m\)-edge subgraph
by one of at most \(A^m\) bounded-choice exploration words, for an absolute
constant \(A\).  Thus the total activity \(z^m r^{-v}\) of connected
\(m\)-edge subgraphs is at most
\[
        bA^m z^m r^{-v}.
\]
For \(m=1,2,3\), simplicity and triangle-freeness give
\(v\ge2,3,4\), respectively.  The graph is triangle-free for \(b\ge11\):
three signed steps from \(\{1,3\}\) have odd integer sum of absolute value
at most nine and hence cannot vanish modulo \(b\).  The finitely many
smaller \(b\) are absorbed into the constants.  For \(m\ge4\), the density
bound \(m\le2(v-1)\) gives \(v\ge m/2+1\).  Consequently, if \(\eta_j\)
denotes the sum of \(m^j\) times the activities of connected polymers, and
\(\eta_2^{\ge2}\) omits the one-edge polymers, then for
\(z\le c_0\sqrt r\), after decreasing \(c_0\),
\[
\eta_0=O(z/r+z^4/r^2),\quad
\eta_1=O(z/r+z^4/r^2),\quad
\eta_2^{\ge2}=O(z^2/r^2+z^4/r^2).
\]
Dropping mutual vertex-disjointness between components only enlarges the
sum.  For \(|T|\ge2\),
\(|T|^2\le2|T|(|T|-1)\).  Marking the ordered pair of distinguished
edges either inside one nontrivial component or in two components, and
then applying the exponential formula, gives
\[
\mathcal P_2(z)
 \le2e^{\eta_0}\bigl(\eta_2^{\ge2}+\eta_1^2\bigr)
 =O(z^2/r^2+z^4/r^2).
\]
This proves the asserted estimate.

## 3. Insertion after the annealed duplicate bound in Section 4.5

Insert the following immediately after the boxed estimate for
\(\mathcal E_x(e)/(rd_x)\).

### Proof of annealed regeneration

Let \(t_F=|e\cap F|\) and put \(a=x^{-1}-1\).  If \(F\) overlaps \(e\) in
\(\ell\) lower and \(m\) middle targets, then, conditional on retaining
all targets of \(e\), its additional retention probability is
\(x^{2r-\ell}y^{2r-m}\).  Because \(y\ge x\), after division by
\(d_x=D_Mx^{2r}y^{2r-1}\) this is at most
\(yx^{-t_F}/D_M\).  Also
\((t-1)_+\le\binom t2\), and
\[
\binom t2x^{-t}
=x^{-2}\sum_{s=2}^t\binom ts\binom s2a^{s-2}.
\]
Double-counting pairs \((F,T)\) with
\(T\in\binom{e\cap F}{s}\) therefore gives
\[
\frac{\mathcal E_x(e)}{rd_x}
\le {y\over rD_Mx^2}
\sum_{s=2}^{4r}\binom s2a^{s-2}
\sum_{T\in\binom es}\deg(T).
\]
Apply the boundary-codegree theorem, set \(z=Ca\), and use
\(\binom s2\le s^2/2\).  For \(a>0\), the last double sum divided by
\(D_M\) is at most
\[
 {r^2\over2a^2}\mathcal P_2(Ca)=O_C(1+a^2).
\]
For \(a=0\) the same statement is the continuous limit, or follows
directly from the \(s=2\) term.  Since
\(\alpha<1/3\) gives \(Ca=o(\sqrt r)\), and
\(y/x=1+O(1/(rx))\), it follows that
\[
\frac{\mathcal E_x(e)}{rd_x}
=O_C\!\left({1+a^2\over rx}\right)
=O_C\!\left({1\over rx^3}\right)=o(1)
\]
uniformly for \(x\ge r^{-\alpha}\).

## 4. Insertion after the fixed-target variance display in Section 4.5

Insert the following immediately after the displayed variance bound.

### Proof of the fixed-target variance bound

Condition on retaining \(v\), and write
\[
 X_v=\sum_{F\ni v}I_F,
\]
where \(I_F\) says that every target of \(F-\{v\}\) is retained.
All \(I_F\) have the same mean \(w_v\), so
\(\mu_v=\mathbb EX_v=d(v)w_v\).  If
\(t=|F\cap G|\), every common target other than \(v\) has retention
probability at least \(x\), whence
\[
 {\mathbb E(I_FI_G)\over\mathbb EI_F\,\mathbb EI_G}
 \le x^{-(t-1)}.
\]
With \(a=x^{-1}-1\),
\[
x^{-(t-1)}-1
=\sum_{\varnothing\ne S\subseteq(F\cap G)-\{v\}}a^{|S|}.
\]
Fixing \(F\), summing over \(G\), separating diagonal variances, and
double-counting \(G\) containing \(\{v\}\cup S\) gives
 \[
 {\operatorname{Var}X_v\over\mu_v^2}
 \le {1\over\mu_v}+
 {1\over d(v)}
 \sum_{\varnothing\ne S\subseteq F-\{v\}}
 a^{|S|}\deg(\{v\}\cup S).
\]

Let \(R\) be the boundary edge representing \(v\) in \(B(F)\), and set
\(z=Ca\).  The boundary-codegree theorem and \(d(v)\ge D_M\) bound the last
term, up to one absolute factor, by
\[
\sum_{\varnothing\ne S\subseteq E(B_r)-\{R\}}
 z^{|S|}r^{2-|V(R\cup S)|}.
\]
To estimate this rooted sum, decompose \(R\cup S\) into its component
containing \(R\) and its other components.  The unrooted component
activity from the preceding polymer proof is
\(\eta_0=O(z/r+z^4/r^2)\).  A root component with one added edge costs
\(O(z/r)\); with two added edges it costs \(O(z^2/r^2)\), by
triangle-freeness; and with at least three added edges the density bound
gives the geometric tail
\[
\sum_{m\ge4}A^m z^{m-1}r^{1-m/2}=O(z^3/r).
\]
Dropping disjointness of the other components multiplies this by at most
\(e^{\eta_0}\), while the possibility of no added root edge and at least
one remote component contributes \(e^{\eta_0}-1\).  Hence the rooted sum
is
\[
O(z/r+z^3/r+z^4/r^2).
\]
For \(x\ge r^{-\alpha}\), \(\alpha<1/3\), one has
\(z=O_C(x^{-1})=o(\sqrt r)\); substitution yields
 \[
 {\operatorname{Var}X_v\over\mu_v^2}
 \le {1\over\mu_v}+
O_C(a/r+a^3/r+a^4/r^2)
\le {1\over\mu_v}+O_C(1/(rx^3)).
\]
The mean \(\mu_v\) is exponential in this range, proving the final
\(o(1)\).

## 5. Insertion after the duplicate-drift displays in Section 4.6

Insert the following after
\(\mathfrak E(e)/D_M=12+O(1/r)\).

### Proof of the drift identity and its scale

Let \(\Gamma(e)=\{F:F\cap e\ne\varnothing\}\), and let \(d(v)\) be the
current target degree.  At \(p=0\), to first order exactly one edge is
marked, and it is automatically isolated.  Therefore
\[
s_e'(0)=-|\Gamma(e)|,\qquad s_v'(0)=-d(v).
\]
Moreover
\[
\sum_{v\in e}d(v)-|\Gamma(e)|
=\sum_{F:t_F>0}(t_F-1)=\mathfrak E(e).
\]
Taking the logarithmic derivative proves the displayed identity.

For every integer \(t\ge0\),
\[
0\le\binom t2-(t-1)\mathbf1_{t>0}
={ (t-1)(t-2)\over2}\mathbf1_{t\ge3}
\le\binom t3.
\]
Thus
\[
0\le S(e)-\mathfrak E(e)\le M_3(e),
\qquad
M_3(e)=\sum_{T\in\binom e3}\deg(T).
\]
The boundary graph has bounded degree and is triangle-free for all
sufficiently large \(r\).  Its connected three-edge subgraphs number
\(O(r)\) and have at least four vertices; a two-edge component plus an
isolated edge gives \(O(r^2)\) choices and five vertices; and three
isolated edges give \(O(r^3)\) choices and six vertices.  The
boundary-codegree theorem consequently gives
\[
{M_3(e)\over D_M}
\le C^3\{O(r)r^{-2}+O(r^2)r^{-3}+O(r^3)r^{-4}\}
=O(1/r).
\]
The finitely many smaller \(r\) are absorbed into the constant.  Combining
this with the exact pair expansion proves
\(\mathfrak E(e)/D_M=12+O(1/r)\).

## 6. Replacement for the unsupported bite-concentration paragraph in Section 4.6

Replace the paragraph beginning “No lower bound on an individual target
degree...” and ending with the claimed matching leave by the following.

### Isolated-count covariance and one-cap descent

Let \(G_j\) be the conflict graph on the \(Z_j\) surviving
configurations, let \(g_e\) be its degrees, and let
\(\Delta=\max_e g_e\).  For a general graph with \(Z\) vertices, mark
vertices independently with probability \(p\), and let \(A\) count marked
vertices having no marked neighbour.  Put
\[
q_e=p(1-p)^{g_e},\qquad \mu=\mathbb EA.
\]
Adjacent vertices have nonpositive covariance.  If \(e,f\) are
nonadjacent and \(c_{ef}=|N(e)\cap N(f)|\), then exactly
\[
\operatorname{Cov}(I_e,I_f)
=q_eq_f\{(1-p)^{-c_{ef}}-1\}.
\]
When \(p\le1/2\) and \(p\Delta\le B\), the braces are at most
\(2e^{2B}pc_{ef}\).  Finally,
\[
\sum_{e,f}c_{ef}=\sum_h|N(h)|^2\le Z\Delta^2,
\qquad
\mu\ge Zp(1-p)^\Delta\ge Zpe^{-2B}.
\]
Consequently
\[
{\operatorname{Var}A\over\mu^2}
\le C_B\left({1\over Zp}+{p\Delta^2\over Z}\right).
\tag{*}
\]

Under the displayed maximum-degree cap in the handoff and while
\(x_j\ge r^{-\alpha}\), the exact shore relation is
\[
{ |M_j|\over|L_j|}
={\bar d_j^L\over\bar d_j^M}
=1+{2\over rx_j}\le2
\]
for all sufficiently large \(r\).  Hence
\[
\Delta(G_j)\le
2rK\bar d_j^M+2rK\bar d_j^L
\le6Kr\bar d_j^M.
\]
Also
\[
{1\over Z_j}\sum_e g_e
\le{1\over Z_j}\sum_vd_j(v)(d_j(v)-1)
\le2Kr(\bar d_j^M+\bar d_j^L)
\le6Kr\bar d_j^M.
\]
Since \(u\mapsto(1-p_j)^u\) is convex, Jensen gives
\[
{\mathbb E(A_j\mid H_j)\over Z_jp_j}
\ge(1-p_j)^{6Kr\bar d_j^M}.
\]

Now take \(\gamma=1/(96K)\).  Once
\(\bar d_j^M\ge e^{r\log r}\), the last display is at least
\(e^{-12K\gamma}=e^{-1/8}\).  In (*) one has
\(p_j\Delta\le1/16\), and the exact identity
\[
Z_jp_j={\gamma|M_j|\over2r^2}
\]
shows that the relative variance is
\(O_K(r^2/|M_j|)=e^{-\Omega(r)}\).  Chebyshev, together with a binomial
Chernoff bound on the total number of marked configurations, therefore
gives
\[
{1\over2}Z_jp_j\le A_j\le2Z_jp_j
\tag{**}
\]
with conditional failure \(e^{-\Omega(r)}\).

It remains only to justify the degree floor used in this argument.  Start
from
\[
Z_0={|M_0|D_M\over2r}=(2r+1)!,
\qquad \log Z_0=(2+o(1))r\log r.
\]
Every accepted configuration has \(2r\) targets on each shore, so its
closed conflict neighbourhood has size at most
\[
2rK\bar d_j^M+2rK\bar d_j^L\le6Kr\bar d_j^M.
\]
By the upper bound in (**),
\[
Z_j-Z_{j+1}
\le A_j\,6Kr\bar d_j^M
\le12K\gamma Z_j=Z_j/8.
\]
The lower bound in (**) removes at least \(\gamma/(2r)\) of each
residual shore per round.  Thus the lower density reaches
\(r^{-\alpha}\) within
\[
J_*=\left\lceil{2\alpha r\log r\over\gamma}\right\rceil
\]
rounds.  For \(\alpha\le1/(256K)\),
\[
\log Z_j\ge\log Z_0+j\log(7/8)
\ge(2-o(1))r\log r-{J_*\over7},
\qquad
{J_*\over7}\le{3\over28}r\log r+O(1).
\]
Since \(|M_j|\le\binom{2r+1}r=e^{O(r)}\), this implies
\(\bar d_j^M\ge e^{r\log r}\), closing the induction.  The conditional
failure probabilities union-bound over the
\(O_K(r\log r)\) stopped rounds.  Accepted configurations are disjoint
within a round, and deletion of their targets makes different rounds
disjoint.  The one-round overshoot is \(1+O_K(1/r)\), and
\[
{|M_j|\over|M_0|}={rx_j+2\over r+2}=o(1).
\]
Therefore, conditional only on persistence of the displayed
maximum-degree cap, the union of accepted configurations is a matching
leaving \(r^{-\alpha}(1+O_K(1/r))\) of the lower shore and \(o(1)\) of
the middle shore.

## 7. Residual editorial dependencies

Even after inserting the blocks above, file citations must be described as
provenance/reproducibility references rather than sources needed for
validity.  In particular, phrases such as “The reduction is ...” and “See
...” should be changed to “A fuller provenance record/checker is ...”.
The generic common-partial-transversal obstruction in Section 4.3 either
needs its short probabilistic construction inserted or should be removed;
it is not needed to prove any positive direct-route statement.

## 8. Optional insertion proving the generic counterexample in Section 4.3

If the sentence asserting insufficiency of generic local statistics is
retained, append the following proof to that paragraph.

Fix integers \(k,D\) with
\(k\ge64\log(2eDk)\), and let \(L\) tend to infinity.  On a set \(X\) of
size \(LD\), choose \(k\) independent uniform equipartitions into \(L\)
blocks of size \(D\).  With probability \(1-o(1)\), every two blocks from
different partitions meet in at most two points: for a fixed pair the
probability of an intersection of size at least three is at most
\[
{\binom D3^2\over\binom{LD}3},
\]
and a union bound over \(O(k^2L^2)\) pairs tends to zero.

Put \(Q=\log(2eDk)\), \(c=16Q/k\), and
\(s=\lceil cL\rceil\).  For a fixed \(s\)-set \(S\), the probability that
one equipartition puts its points in distinct blocks is
\[
p_s={(L)_sD^s\over(LD)_s}
\le\exp\{-s(s-1)/(4L)\}.
\]
The partitions are independent, and hence the expected number of
\(s\)-sets meeting every block in at most one point is at most
\[
\binom{LD}s p_s^k
\le\left({eLD\over s}\right)^s
   \exp\{-ks(s-1)/(4L)\}
\le e^{-sQ}=o(1).
\]
Thus deterministic partitions exist with both properties.

Make one hypergraph vertex for every block, one part for every partition,
and, for each \(x\in X\), one \(k\)-edge consisting of the \(k\) blocks
containing \(x\).  It is \(D\)-regular, and pair codegrees are at most two.
The squared normalized local kernel is at most
\(2(k-1)/D\), because each of the \(D\) incidences at a vertex supplies
\(k-1\) pair incidences and every positive codegree is at most two.
The labels of pairwise disjoint hyperedges form a common partial
transversal, so every matching has fewer than \(cL\) edges and covers at
most \(c=O(\log(Dk)/k)\) of the vertices.  Replacing each edge by any
common number of labelled parallel copies makes the degree arbitrarily
large without changing normalized codegrees or the matching number.  This
proves the claimed generic no-go without using an external source.

## 9. Insertion proving the boundary theorem in Section 4.4

Insert the following after the boxed boundary-codegree inequality.

### Proof of the punctured-circulant density bound

Before the linear relabelling, a retained middle window starting at \(i\)
has boundary edge \(\{i,i+r\}\), and a retained lower window has boundary
edge \(\{i,i+r-1\}\).  Multiplication by \(-2\) modulo
\(b=2r+1\) sends these differences to \(1\) and \(3\), respectively.
The two dirty starts remove \(\{0,1\}\) and \(\{0,3\}\).

For a proper nonempty \(U\subset\mathbb Z_b\), let
\(\partial_d(U)\) be the number of step-\(d\) edges crossing its cut in
the full circulant.  The number of full-circulant edges induced by \(U\)
is
\[
2|U|-{\partial_1(U)+\partial_3(U)\over2}.
\]
The step-one cycle is connected, so \(\partial_1(U)\ge2\).  If
\(\partial_3(U)>0\), parity gives \(\partial_3(U)\ge2\).  If it is zero,
then \(3\mid b\) and \(U\) is a nontrivial union of complete step-three
cycles; its step-one cut has at least \(2b/3\) edges.  Thus every proper
\(U\) induces at most \(2(|U|-1)\) edges.  Deleting the two dirty edges
cannot increase this number, while the full punctured graph has
\(2b-2=2(b-1)\) edges.  Therefore every subgraph with \(m\) edges and
\(v\) nonisolated vertices satisfies \(m\le2(v-1)\).

### Proof of the boundary-codegree inequality

Fix \(T\subseteq e\), put \(t=|T|\), and list its \(q\) distinct boundary
cuts cyclically.  For target lengths \(k,h\in\{r,r-1\}\), fixing one
cyclic start and the intersection size leaves at most four possible
relative starts: the exact numbers are \(b-k-h+1\) in the disjoint case,
two in a proper overlap, and \(|k-h|+1\) in a containment.  Hence, after
choosing an anchor target, the number \(P(T)\) of retained positional
tuples having the prescribed labelled Venn signature satisfies
\[
                         P(T)\le(b-1)4^{t-1}.          \tag{B1}
\]

Let \(n_\sigma\) be the sizes of the labelled Venn cells and set
\[
V(T)=\prod_\sigma n_\sigma!.
\]
For a fixed positional tuple, labels may be assigned independently inside
corresponding cells in exactly \(V(T)\) ways.  Conversely, a proper
nonempty target has a unique cyclic start in a fixed word, so no word is
counted twice.  Thus
\[
                         \deg(T)=P(T)V(T).             \tag{B2}
\]

The \(q\) cuts divide the circle into positive elementary gaps
\(g_1,\ldots,g_q\), with sum \(b\); put \(G(T)=\prod_i g_i!\).
We claim
\[
                         V(T)\le8^{t-1}G(T).           \tag{B3}
\]
Expose the target arcs one at a time and track \(R=V/G\).  Splitting an
old Venn cell of size \(n\) into sizes \(p,n-p\) multiplies \(V\) by
\(\binom np^{-1}\), while splitting an elementary gap of size \(g\) into
\(a,g-a\) multiplies \(G\) by \(\binom ga^{-1}\).
If the two new cuts lie in distinct old gaps, independently selecting the
prescribed labels from those split gaps injects into the prescribed
subset of the containing Venn cell.  Therefore the product of the gap
binomials is at most the corresponding cell binomial, even when the two
gaps belong to the same cell, and \(R\) does not increase.  With one new
cut the same injection applies.  With two old cuts, \(G\) is unchanged
and every Venn-cell factorial can only decrease, so again \(R\) does not
increase.

If both new cuts lie in one old gap of size \(g\), write the three pieces
as \(x,y,z\), where \(y\) lies between the new cuts.  The gap refinement
factor is
\[
\binom gy\binom{g-y}x.
\]
The middle segment is either the new arc or its complement, so
\(y\in\{k,b-k\}\).  Fix the selected labels outside the old gap.
Adjoining a \(y\)-subset of the gap injects into the prescribed selected
subsets of the old Venn cell; if the middle segment is the complement,
apply the same injection to unselected labels and use binomial symmetry.
Thus the Venn-cell split cancels the first binomial.
After the first target has been exposed, every old gap has size at most
\(r+2\); hence \(g-y\le3\) if \(y=k\), and \(g-y\le1\) if
\(y=b-k\).  The uncancelled factor is at most
\(2^{g-y}\le8\).  This proves (B3) by induction.

Every gap is at most \(r+2\).  Factorial log-convexity says that moving one
unit from a smaller positive gap to a larger nonsaturated gap cannot
decrease the product of factorials.  Repeating this transfer yields
\[
G(T)\le
\begin{cases}
(r+2)!(r-q+1)!,&2\le q\le r,\\
(2r-q+2)!,&r+1\le q\le2r+1.
\end{cases}                                            \tag{B4}
\]
Using \((n)_m\ge(n/e)^m\), the first case gives
\[
{G(T)\over r!(r+1)!}
\le {r+2\over(r)_{q-1}}
\le3e^{q-1}r^{2-q},
\]
and the second gives
\[
{G(T)\over r!(r+1)!}
\le e^{q-1}r^{1-q}\le e^q r^{2-q}.
\]
Thus, uniformly,
\[
{G(T)\over r!(r+1)!}\le(3e)^q r^{2-q}.                \tag{B5}
\]

Finally \(D_M=(b-1)r!(r+1)!\), and \(q\le2t\).
Combining (B1)--(B5) gives
\[
{\deg(T)\over D_M}
\le4^{t-1}8^{t-1}(3e)^q r^{2-q}
\le\{32(3e)^2\}^{t}r^{2-q}.
\]
This proves the displayed theorem with the explicit absolute constant
\(C=32(3e)^2\).

## 10. Insertion proving the configuration claims in Section 4.3

Insert the following after the definition of \(E(w)\), replacing the
unproved summary paragraphs through the first-bite claim.

### Deck reconstruction, degrees, and the fractional optimum

In the unpunctured deck, containment between its \((r-1)\)- and
\(r\)-windows is the alternating cycle.  A cyclic \((r-1)\)-interval is
contained in exactly its two one-point end extensions, so there are no
other containment edges.  Deleting \(L_0,M_0\) leaves the path
\[
L_1,M_1,L_2,M_2,\ldots,L_{2r},M_{2r}.
\]
Its endpoint layers orient it canonically.  The recovered same-start
pairs satisfy
\[
M_i\setminus L_i=\{w_{i+r-1}\},\qquad1\le i\le2r.
\]
These give every word position except \(r-1\); the unique unused label
gives that final position.  Hence \(w\mapsto E(w)\) is injective and there
are \(b!\) configurations.

For a fixed \(k\)-set, prescribing any of its \(b-1\) retained starts
gives \(k!(b-k)!\) words, with no overcount because a proper cyclic
interval has a unique start.  Therefore
\[
D_M=(b-1)r!(r+1)!=2r\,r!(r+1)!,
\]
\[
D_L=(b-1)(r-1)!(r+2)!={r+2\over r}D_M.
\]
Weighting every configuration by \(1/D_L\) loads each lower target by
one and each middle target by \(D_M/D_L=r/(r+2)\).  Its total mass is
\[
{b!\over D_L}={|\mathcal L|\over2r},
\]
using the lower incidence identity
\(b!\,2r=|\mathcal L|D_L\).  No fractional matching can have larger mass:
each edge consumes \(2r\) units of the total lower capacity
\(|\mathcal L|\).  This proves optimality.

### Complete pair calculation

For target sizes \(k,h\in\{r,r-1\}\) and intersection \(a\), set
\[
\Phi_{k,h}(a)=a!(k-a)!(h-a)!(b-k-h+a)!
\]
and
\[
m_{k,h}(a)=
\begin{cases}
b-k-h+1,&a=0,\\
2,&0<a<\min(k,h),\\
|k-h|+1,&a=\min(k,h).
\end{cases}
\]
For distinct layer-tagged targets \(A,B\),
\[
d(A,B)=
\bigl((b-2)m_{k,h}(a)+\mathbf1_{a=\min(k,h)}\bigr)
\Phi_{k,h}(a).                                        \tag{P1}
\]
Indeed, after fixing the first cyclic start, the three cases have exactly
the displayed numbers of relative starts.  A positional pair has
\(\Phi_{k,h}(a)\) labelings of its four Venn cells.  Of the
\(bm_{k,h}(a)\) ordered start pairs, \(2m_{k,h}(a)\) have a dirty start;
\((0,0)\) was removed twice and is restored exactly in the same-start
containment case.  This proves (P1).

Inside one fixed configuration, the complete unordered inventory is
\[
\begin{array}{c|c|c|c}
XY&a&N&d\\ \hline
MM&0\le a\le r-1&2r-1&
(4r-2)a!(r-a)!^2(a+1)!\\
LL&0&4r-2&(8r-4)(r-1)!^2\,3!\\
LL&1\le a\le r-2&2r-1&
(4r-2)a!(r-1-a)!^2(a+3)!\\
ML&0&6r-3&(6r-3)r!(r-1)!\,2!\\
ML&1\le a\le r-2&4r-2&
(4r-2)a!(r-a)!(r-1-a)!(a+2)!\\
ML&r-1&4r-1&(4r-1)(r-1)!(r+1)!.
\end{array}                                            \tag{P2}
\]
The \(N\)-column is the retained ordered-start count from (P1), divided
by two only for equal-layer pairs.  Thus (P2) is an analytic inventory,
not a finite census.

Let \(S_{XY}\) be the pair-codegree mass from the indicated layer pair.
Multiplying the last two columns of (P2) and using factorial cancellation
gives the exact sums
\[
{S_{MM}\over D_M}
={(2r-1)^2\over r}
\sum_{a=0}^{r-1}
{1\over\binom ra\binom{r+1}{a+1}},                    \tag{P3}
\]
\[
{S_{ML}\over D_M}
={1\over2r}\sum_{a=0}^{r-1}
{n_{ML}(a)^2\over\binom ra\binom{r+1}{a+2}},           \tag{P4}
\]
\[
{S_{LL}\over D_M}
={r+2\over4r^2}\sum_{a=0}^{r-2}
{n_{LL}(a)^2\over\binom{r-1}a\binom{r+2}{a+3}},        \tag{P5}
\]
where
\[
n_{ML}(a)=
\begin{cases}
3(2r-1),&a=0,\\
2(2r-1),&1\le a\le r-2,\\
4r-1,&a=r-1,
\end{cases}
\quad
n_{LL}(a)=
\begin{cases}
4(2r-1),&a=0,\\
2(2r-1),&1\le a\le r-2.
\end{cases}
\]
For example, the cancellation behind (P3) is
\[
{a!(r-a)!^2(a+1)!\over r!(r+1)!}
={1\over\binom ra\binom{r+1}{a+1}},
\]
and the other two are identical.

Isolating the endpoint terms in these reciprocal-binomial sums gives
\[
\sum_{a=0}^{r-1}
{1\over\binom ra\binom{r+1}{a+1}}
={1\over r}+{2\over r^3}+O(r^{-4}).
\]
In (P4), the containment, disjoint, and \(a=r-2\) terms are respectively
\[
8-{4\over r}+{1\over2r^2},\qquad
{36\over r}-{72\over r^2}+O(r^{-3}),\qquad
{16\over r^2}+O(r^{-3});
\]
all other terms total \(O(r^{-3})\).  In (P5), the \(a=r-2\) and
\(a=0\) terms are
\[
{4\over r}+O(r^{-3}),\qquad
{96\over r^2}+O(r^{-3}),
\]
and the rest total \(O(r^{-3})\).  Here are uniform remainder bounds.
In (P3), the omitted \(a=2\) and \(a=r-2\) terms are respectively
\(O(r^{-5})\) and \(O(r^{-4})\); for
\(3\le a\le r-3\), both binomial factors are \(\Omega(r^3)\), so all
middle terms total \(O(r^{-5})\).  In (P4), the common proper-overlap
prefactor is \(O(r)\): the \(a=1\) term is \(O(r^{-3})\), and after it
is removed the two binomial factors have product \(\Omega(r^5)\), apart
from the already displayed right endpoint layers, so the remaining
\(O(r)\) terms total \(O(r^{-3})\).  The same argument applies to (P5):
its prefactor is \(O(r)\), its \(a=r-3\) term is \(O(r^{-3})\), and all
other undisplayed terms have binomial product \(\Omega(r^5)\).  The
finitely many small \(r\) are absorbed by the constants.  This proves the
stated remainder bounds.
Substitution proves
\[
{S_{MM}\over D_M}=4-{4\over r}+{9\over r^2}+O(r^{-3}),
\]
\[
{S_{ML}\over D_M}=8+{32\over r}-{111\over2r^2}
+O(r^{-3}),
\qquad
{S_{LL}\over D_M}={4\over r}+{96\over r^2}+O(r^{-3}),
\]
and hence the displayed expansion for \(S(e)\).

### Path localization, maximum codegree, and the first bite

The containment pairs in (P2) form the reconstructed alternating path and
number \(4r-1\).  In the full middle cyclic deck, disjointness joins
successive windows in the odd-graph cyclic order; deleting \(M_0\) leaves
a path of \(2r-1\) edges.  The two skeleton masses, obtained from the
\(ML,a=r-1\) and \(MM,a=0\) rows of (P2), sum to
\[
{(2r-1)^2\over r(r+1)}
+{(4r-1)^2\over2r^2}
=12-{12\over r}+{19\over2r^2}+O(r^{-3}).
\]
Subtracting from (P3)--(P5) leaves
\[
{44\over r}+{40\over r^2}+O(r^{-3})
\]
of normalized off-skeleton mass.  The successive factorial ratios in the
MM, LL, and proper-ML rows are, respectively,
\[
{(a+1)(a+2)\over(r-a)^2},\qquad
{(a+1)(a+4)\over(r-1-a)^2},\qquad
{(a+1)(a+3)\over(r-a)(r-1-a)}.
\]
Each is increasing in \(a\), so every row maximum occurs at an endpoint.
Substitution shows that every off-skeleton pair has codegree
\(O(D_M/r^2)\).  For \(r\ge3\), the largest pair codegree is the
containment value
\[
\Delta_2=(4r-1)(r-1)!(r+1)!,
\qquad
{\Delta_2\over D_L}={4r-1\over2r(r+2)},
\]
so \(4r\Delta_2/D_L\to8\).
For \(r=2\), the disjoint LL pair is the finite exceptional maximum; it
does not affect the asymptotic statement.

For the bite calculation, let \(C(e)\) be the number of other
configurations meeting \(e\), and put
\[
A(e)=\sum_{v\in e}(d(v)-1)=2r(D_M+D_L)-4r.
\]
For \(F\ne e\), \(t_F-1\le\binom{t_F}2\), so
\[
A(e)-\left(S(e)-\binom{4r}2\right)
\le C(e)\le A(e).
\]
Thus
\[
C(e)=4(r+1)D_M(1+O(1/r)).
\]
If configurations are marked independently with
\(p=\gamma/(rD_M)\), a fixed marked configuration is isolated with
probability
\[
(1-p)^{C(e)}=\exp(-4\gamma+o(1)).
\]
Isolated marked configurations form a matching.  Multiplying their
retention probability by \(D_M\) or \(D_L\) gives expected covered
fractions
\[
{\gamma e^{-4\gamma}+o(1)\over r},
\qquad
{r+2\over r}{\gamma e^{-4\gamma}+o(1)\over r},
\]
which proves the claimed calibrated first bite.
