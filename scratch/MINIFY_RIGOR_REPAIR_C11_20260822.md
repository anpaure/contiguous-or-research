# Master-handoff rigor repair: the mixed external-root lemma in C.11

**Purpose.**  This is standalone replacement text for the proof of
(C.11.3)--(C.11.8).  It defines the exposure tree and proves both the
mixed-root codegree estimate and the two-root polymer sum.  No computation
or external result is a premise.

**Replacement guidance.**  In Appendix C.11, retain (C.11.1)--(C.11.2),
then replace the text from “We first prove the mixed-root estimate” through
the proof of (C.11.8) by the two lemmas and application below.  Define the
falling factorial once in the handoff by

\[
 (n)_a=n(n-1)\cdots(n-a+1),\qquad (n)_0=1.                 \tag{C11-R.0}
\]

The notation is that of C.11: \(b=2r+1\), \(k_q=r-q\),
\(B_q=\binom b{k_q}\), \(D_q=b\,k_q!(b-k_q)!\), and
\(F=E(w)\) is a fixed directed punctured configuration.

## Mixed external-root codegree lemma

Suppose that \(T=I_{k_q}^w(s)\) is a full cyclic window of the row \(w\).
Put a cut between consecutive positions of \(w\), and multiply cut labels
by \(-2\) modulo \(b\).  The boundary pairs of the \(r\)- and
\((r-1)\)-targets of \(F\) become the edges of a subgraph

\[
 \mathcal B_F\subseteq
 \operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\})             \tag{C11-R.1}
\]

obtained by deleting two edges.  The boundary pair \(R_q\) of \(T\) has
cyclic length \(2q+1\).  For
\(\varnothing\ne S\subseteq F\), let \(\partial S\) be the set of
boundary edges representing its tagged targets, and define

\[
 v_q(S)=|V(R_q\cup\partial S)|,                             \tag{C11-R.2}
\]

\[
 d_q(T,S)=|\{u\in\mathfrak S_b:T\text{ is a full window of }u,
                    \ S\subseteq E(u)\}|,                  \tag{C11-R.3}
\]

where \(\mathfrak S_b\) is the set of permutations of the \(b\) ground
labels and \(E(u)\) is the punctured configuration defined by the row
\(u\).

There is an absolute constant \(C\) such that, uniformly for

\[
 2\le q\le\sqrt r/4,
\]

\[
 \boxed{\frac{d_q(T,S)}{D_q}
       \le C^{|S|}r^{\,2-v_q(S)}.}                         \tag{C11-R.4}
\]

The same statement holds for the complementary upper target.

### Proof

Anchor the start of \(T\).  Its two root cells have sizes

\[
                         r-q,\qquad r+1+q.                 \tag{C11-R.5}
\]

Fix the labelled Venn signature of \(T\cup S\).  If
\(n_\sigma\) are its cell sizes and \(V=\prod_\sigma n_\sigma!\), then
\(V\) is the number of label assignments for any one compatible positional
tuple.  Let \(P_q(S)\) be the number of relative positional tuples with
the anchored start and this signature.  It is enough to prove

\[
 P_q(S)V\le
 C^{|S|}(r-q)!(r+1+q)!r^{\,2-v_q(S)}.                     \tag{C11-R.6}
\]

Indeed, there are \(b\) choices for the start of \(T\), so the left side
times \(b\) bounds \(d_q(T,S)\), whereas
\(D_q=b(r-q)!(r+1+q)!\).  The puncture can only reduce the count.

We now prove (C11-R.6), including the positional multiplicity.  Order
\(S=\{S_1,\ldots,S_t\}\).  The exposure tree at level \(i\) has one node
for every relative start tuple of
\(T,S_1,\ldots,S_i\) having the prescribed labelled Venn signature; the
start of \(T\) is fixed.  A node \(\eta\) is weighted by the product
\(V_i(\eta)\) of the factorials of its current Venn cells.  Thus the sum
of the terminal node weights is exactly \(P_q(S)V\).

At any node list the positive elementary cut gaps as
\(g_1,\ldots,g_v\), and put \(G=\prod_hg_h!\).  They satisfy

\[
                  \sum_hg_h=b,\qquad g_h\le r+1+q.         \tag{C11-R.7}
\]

If an old Venn cell \(C\) is the disjoint union of elementary gaps
\(H\), and a child interval takes \(p_H\) labels from gap \(H\), with
\(p_C=\sum_{H\subset C}p_H\), then

\[
 \prod_{H\subset C}\binom{|H|}{p_H}\le\binom{|C|}{p_C},
 \qquad
 \sum_{\sum p_H=p_C}\prod_H\binom{|H|}{p_H}
       =\binom{|C|}{p_C}.                                  \tag{C11-R.8}
\]

The first map sends independently chosen gap subsets to their disjoint
union in \(C\); intersection with the old gaps recovers them.  Summing
over allocations gives the second identity.  Consequently all branches
whose two new cuts lie in distinct old gaps are paid for by the Venn-cell
refinement and do not increase the ratio of total node weight to the gap
factorial product.

If both new cuts lie in one ordinary gap of size \(g\), write its three
pieces as \(u,m,v\).  The middle piece or its complement has size in
\(\{r-1,r,r+1,r+2\}\).  Since an ordinary gap has size at most \(r+2\),
one has \(u+v\le3\), so the information lost when the two outside pieces
are merged costs at most

\[
                         \binom{u+v}{u}\le8.                \tag{C11-R.9}
\]

The only additional case is a gap descended from one of the two root
cells and still having size \(g\ge r-1\).  Put
\(d=u+v=g-m\le q+2\).  There are at most \(d+1\) positional splits, the
Venn merge loses at most \(\binom du\), and the exact change of the gap
factorial is

\[
 \frac{u!m!v!}{g!}
 =\frac1{\binom gd\binom du}.                              \tag{C11-R.10}
\]

Thus the total, over every split of this type, is charged by

\[
 \frac{d+1}{\binom gd}\le
 \begin{cases}
  1,&d=0,\\
  4/r,&d=1,\\
  16/r^2,&2\le d\le q+2.
 \end{cases}                                               \tag{C11-R.11}
\]

For the last line, the ratio of the expression at \(d+1\) to that at
\(d\) is \((d+2)/(g-d)\le1\), since
\(q+2\le\sqrt r/2\) for large \(r\); hence its maximum occurs at
\(d=2\), and \(3/\binom g2\le16/r^2\).  Enlarging the absolute constant
handles the finitely many smaller \(r\).

At the first exposure level, (C11-R.10)--(C11-R.11) sum every possible
root-relative placement.  At later levels retain \(S_1\) as a positional
anchor.  A cyclic interval of either central length and prescribed
intersection with \(S_1\) has at most four starts: disjointness gives at
most \(b-k-h+1\le4\), a proper overlap gives two, and containment gives
at most \(|k-h|+1\le2\).  Therefore (C11-R.8), with one absolute factor
per exposed interval, sums all children rather than following one branch.
Coincident old cuts cost no power of \(r\); one genuinely new reference
cut costs \(O(1/r)\), and two cost \(O(1/r^2)\), by
(C11-R.8)--(C11-R.11).  This remains true if another positional child
makes a reference cut coincident, because that child is already one of the
splits summed in (C11-R.11).

For completeness, the terminal factorial envelope used in this induction
is

\[
 \frac{G}{(r-q)!(r+1+q)!}
 \le C^v r^{\,2-v}.                                      \tag{C11-R.12}
\]

To prove it, factorial log-convexity moves mass from smaller positive gaps
to larger nonsaturated gaps.  If \(v\le r-q+1\), the maximizing product is
at most
\((r+1+q)!(r-q-v+2)!\), and division by the root product leaves
\(1/(r-q)_{v-2}\le(e/r)^{v-2}\), after changing the constant because
\(q\le\sqrt r/4\).  If \(v>r-q+1\), the transfers leave at most one gap
of size \(b-v+1\) and all other gaps of size one, which is smaller still.
The elementary inequality used here is
\((n)_a=a!\binom na\ge(n/e)^a\): compare ordered samples with samples
allowing repetition to obtain \(\binom na\ge(n/a)^a\), and integrate
\(\log x\) to obtain \(a!\ge(a/e)^a\).

Let \(v_i^*\) be the number of reference cuts of
\(T,S_1,\ldots,S_i\).  The preceding child calculation and
(C11-R.12) give, by induction over the exposure tree, the following
bound.  Since \(v_i^*\le2i+2\), its factor \(C^{v_i^*}\) is absorbed by
enlarging the absolute base \(C\):

\[
 \sum_{\eta\text{ at level }i}V_i(\eta)
 \le C^i(r-q)!(r+1+q)!r^{\,2-v_i^*}.                      \tag{C11-R.13}
\]

At level zero this is equality.  The three child cases above prove the
induction step and exhaust all possibilities because an interval has two
boundary cuts.  At level \(t\), \(v_t^*=v_q(S)\), so
(C11-R.13) is (C11-R.6).  This proves (C11-R.4).  Complementation keeps
the same boundary pair and proves the upper-target version. \(\square\)

## Two-root polymer lemma

For a sufficiently small absolute \(c_0>0\), uniformly in the preceding
range and for \(0\le z\le c_0\sqrt r\),

\[
 \boxed{
 \sum_{\varnothing\ne S\subseteq F}
 z^{|S|}r^{\,2-v_q(S)}
 =O\!\left(\frac z r+\frac{z^3}r+\frac{z^4}{r^2}\right).}  \tag{C11-R.14}
\]

### Proof

The graph \(\mathcal B_F\) has maximum degree four, is triangle-free for
all sufficiently large \(r\), and every \(m\)-edge subgraph with \(v\)
nonisolated vertices satisfies

\[
                              m\le2(v-1).                   \tag{C11-R.15}
\]

Indeed the full circulant is the union of its step-one and step-three
two-factors.  Every proper nonempty vertex set has at least two step-one
cut edges.  It either cuts a step-three cycle, giving two more, or is a
union of whole step-three cycles; in the latter case its step-one cut is
at least four.  Thus an induced proper subgraph has at most \(2v-2\)
edges.  On all \(b\) vertices, deleting the two punctured edges leaves
\(2b-2\) edges.  This proves (C11-R.15).  Triangle-freeness follows because
three signed steps from \(\{1,3\}\) have odd integer sum of absolute value
at most nine and cannot vanish modulo \(b\ge11\).

Adjoin the fixed chord \(R_q\).  It creates no triangle: a sum of two
signed elements of \(\{1,3\}\) belongs to
\(\{0,\pm2,\pm4,\pm6\}\), whereas the chord length is \(5\) for \(q=2\)
and at least \(7\) for \(q\ge3\), with no modular wrap in the stated
range.

Decompose \(S\) into its connected components in \(\mathcal B_F\).
A maximum-degree-four exploration from a prescribed vertex has at most
\(A_0^m\) connected \(m\)-edge shapes.  Components meeting neither chord
endpoint have total connected activity

\[
 \eta_0=O(z/r+z^4/r^2).                                   \tag{C11-R.16}
\]

The one-, two-, and three-edge cases use respectively at least two, three,
and four vertices; (C11-R.15) gives a geometric tail from four edges on.
A connected component meeting a prescribed chord endpoint has rooted
activity

\[
 O(z/r+z^2/r^2+z^3/r+z^4/r^2).                            \tag{C11-R.17}
\]

The first two terms again use triangle-freeness, while
(C11-R.15) and the bounded-choice exploration give the last two geometric
tails.  The same estimate covers a component meeting both endpoints; the
chord itself supplies the second fixed root, and the smallest such
component has three edges.  There are only two chord endpoints.

Dropping disjointness among all other components only enlarges the sum and
multiplies a rooted contribution by at most \(e^{\eta_0}\).  If no
component meets a chord endpoint, subtract the empty family.  Combining
these alternatives, absorbing \(z^2/r^2\) into \(z/r\), and taking
\(c_0\) small enough proves (C11-R.14). \(\square\)

## Application: product external-degree variance

Let \(I_G\) indicate survival of a catalogue row \(G\in\Omega_q(T)\), so
\(X_{q,T}=\sum_GI_G\) and \(\mathbb EI_G=\rho\).  For distinct rows
\(F,G\), the quotient of their joint survival probability by
\(\rho^2\) is at most \(x^{-|F\cap G|}\).  With
\(a=x^{-1}-1\), expand

\[
 x^{-|F\cap G|}-1
 =\sum_{\varnothing\ne S\subseteq F\cap G}a^{|S|}.
                                                                    \tag{C11-R.18}
\]

Separate the diagonal variance, sum first over \(G\), and apply
the mixed external-root codegree lemma to each \(S\subseteq F\).
Maximizing over the anchored
row \(F\) gives

\[
 \frac{\operatorname {Var}X_{q,T}}{\mu_q^2}
 \le\frac1{\mu_q}+
 \sum_{\varnothing\ne S\subseteq F}
       (Ca)^{|S|}r^{\,2-v_q(S)}.                          \tag{C11-R.19}
\]

If \(x\ge r^{-\alpha}\) with \(\alpha<1/3\), then
\(Ca=o(\sqrt r)\).  The two-root polymer lemma and
\(a\le x^{-1}\) yield

\[
 \frac{\operatorname {Var}X_{q,T}}{\mu_q^2}
 \le\frac1{\mu_q}+O\!\left(
       \frac1{rx}+\frac1{rx^3}+\frac1{r^2x^4}\right)
 \le\frac1{\mu_q}+O\!\left(\frac1{rx^3}\right).          \tag{C11-R.20}
\]

The mean is exponential uniformly in this range:
\(D_q=\exp((2+o(1))r\log r)\), while
\(\rho\ge x^{4r}\), so
\(\mu_q\ge\exp((2-4\alpha+o(1))r\log r)\).  Hence the right side is
\(o(1)\).  This is exactly (C.11.8), now with its mixed-root combinatorial
input fully stated and proved.
