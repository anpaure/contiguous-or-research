# Context-phased logarithmic blind spectrum and the exact one-sided parent-projection gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is used.

## 0. Outcome

For the context-phased compiler, let a protected window visit \(d\)
bottom \(Q_4\)-leaves, and let

\[
                         C_1,\ldots,C_b
\]

be its dyadic frontier cells, with coarse-coordinate sizes
\(s_j=|C_j|\).  Its residual blind subgroup is

\[
                         \mathcal B_A=\bigoplus_{j=1}^bE(C_j).
\]

This note computes its complete weight spectrum and the exact spectrum of
the higher disjoint-pair atoms.  The two generating functions are

\[
 \boxed{
 W_A(z)=\prod_{j=1}^b
 { (1+z)^{s_j}+(1-z)^{s_j}\over2}}                 \tag{0.1}
\]

and

\[
 \boxed{
 M_A(z)=\prod_{j=1}^b
 \sum_{r=0}^{\lfloor s_j/2\rfloor}
 { (s_j)_{2r}\over2^r r!}z^r.}                    \tag{0.2}
\]

Here \([z^{2t}]W_A\) counts weight-\(2t\) blind shifts, while
\(t![z^t]M_A\) counts ordered collections of \(t\) disjoint
weight-two shifts, the precise local objects used in the old
\((t+1)\)-face atom.

If \(q=o(R)\) and \(t\le c\log m\), then uniformly

\[
 \boxed{
 { [z^{2t}]W_A(z)\over\binom{R-q}{2t}}
 \le\left({C t\over d}\right)^t,}                 \tag{0.3}
\]

and

\[
 \boxed{
 {t![z^t]M_A(z)\over (R-q)_{2t}/2^t}
 \le\left({C\over d}\right)^t.}                  \tag{0.4}
\]

At a Gaussian window \(q=A\sqrt m\), \(d=\Theta(\sqrt m)\).
For \(t=c\log m\), both bounds are

\[
                         \exp[-\Omega((\log m)^2)].             \tag{0.5}
\]

Thus the entire blind hierarchy through logarithmic strength is
negligible.  The residual flat is still exponential because its mass is
concentrated at macroscopic Hamming weights, not at bounded or logarithmic
strength.

There is also a decisive one-sided structural conclusion.  The residual
blind-cell spectrum does **not by itself** force \(\Omega(W)\) holes.  For every
fixed rank-twisted parent cell and every choice of compiler labels, packet
face recovery makes the complete cell resolutions of its packets
pairwise literal-target disjoint.  Hence all frontier cells align into an
exact home resolution of the parent's emitted literal targets.

Globally, attach the parent label to every emitted target.  The selected
frontier cells then form an exact partition of all \(G\) tagged
occurrences.  Literal holes and repeats arise only after applying the
projection

\[
                         (\text{parent},T)\longmapsto T.        \tag{0.6}
\]

Consequently no lower bound based only on the residual blind spectrum can
prove \(\Omega(W)\) holes for every correlated resolution.  Such a lower
bound must be a cross-parent projection/Hall obstruction.  Conversely,
the logarithmic spectrum does not construct a near-complete literal
projection: it removes the local higher-atom obstruction but leaves the
exact cross-parent maximum-union problem.

## 1. Exact full blind weight enumerator

For a finite set \(C\) of size \(s\), the even-parity subspace has weight
enumerator

\[
 \sum_{\alpha\in E(C)}z^{|\alpha|}
 =\sum_{r\text{ even}}\binom srz^r
 ={(1+z)^s+(1-z)^s\over2}.                         \tag{1.1}
\]

The frontier cells are disjoint and

\[
                         \mathcal B_A=\bigoplus_jE(C_j).
\]

Weights add across a direct sum, so their enumerators multiply.  This
proves (0.1).  In particular,

\[
                         W_A(1)=2^{\sum_js_j-b}
 =2^{n-4d-b},                                      \tag{1.2}
\]

recovering the exact exponential flat size.

Formula (0.1) controls every strength, including the macroscopic range.
For example, a uniform element of \(\mathcal B_A\) is a product of
uniform even-parity words on the cells.  In every cell of size at least
two, each coordinate is balanced.  Hence its expected weight is

\[
                         {1\over2}\sum_{j:s_j\ge2}s_j,          \tag{1.3}
\]

which is \(\Theta(n)\) whenever the nontrivial frontier contains a
positive fraction of the unvisited coordinates.  Exponential flat size
is therefore compatible with a vanishing logarithmic-strength spectrum.

## 2. Exact higher disjoint-pair enumerator

In one cell of size \(s\), the number of ways to choose an unordered
collection of \(r\) disjoint unordered coordinate pairs is

\[
                         {(s)_{2r}\over2^r r!}.     \tag{2.1}
\]

Selections in different cells are independent, proving (0.2).  The
coefficient \([z^t]M_A\) counts an unordered collection of \(t\)
disjoint pairs in the union of the cells.  Ordering those pairs gives

\[
                         D_t(A):=t![z^t]M_A(z).     \tag{2.2}
\]

Starting from one compiler face, toggling the two context coordinates of
each selected pair gives \(t\) further faces.  All \(t+1\) faces share
the same direction support and have the old labelled disjoint-pair column
type.  Thus (2.2), not merely a moment bound, is the exact blind-kernel
contribution to that higher affine type.

For a fixed first ambient face, the number of ordered disjoint-pair
tuples of the same type is

\[
                         {(R-q)_{2t}\over2^t}.      \tag{2.3}

Division of (2.2) by (2.3) gives the exact conditional affine atom
contributed by the frontier blind kernel.

## 3. Uniform logarithmic-strength estimates

Put

\[
                         S_2=\sum_j\binom{s_j}{2}.  \tag{3.1}
\]

The recursively balanced visit law gives

\[
                         \sum_js_j^2\le {2n^2\over d},
 \qquad
                         S_2\le {n^2\over d}.       \tag{3.2}
\]

Every weight-\(2t\) member of \(\mathcal B_A\) has even intersection
with every cell.  Sort the selected coordinates inside each cell and
pair consecutive coordinates.  This is a canonical collection of \(t\)
distinct pairs from the set of \(S_2\) available within-cell pairs, and
its union recovers the original set.  Therefore

\[
                         [z^{2t}]W_A(z)
 \le\binom{S_2}{t}
 \le {S_2^t\over t!}.                              \tag{3.3}
\]

Also, forgetting the disjointness restriction in (2.2) gives

\[
                         D_t(A)\le S_2^t.           \tag{3.4}
\]

Let \(N=R-q\).  When \(2t=o(N)\),

\[
 \binom N{2t}\ge{(N-2t)^{2t}\over(2t)!},
 \qquad
 { (N)_{2t}\over2^t}
      \ge{(N-2t)^{2t}\over2^t}.                   \tag{3.5}
\]

Using

\[
                         {(2t)!\over t!}\le(2t)^t, \tag{3.6}
\]

equations (3.2)--(3.6), and \(R=2n\), proves

\[
 { [z^{2t}]W_A(z)\over\binom N{2t}}
 \le
 \left({2tS_2\over(N-2t)^2}\right)^t
 \le\left({Ct\over d}\right)^t,                 \tag{3.7}
\]

and

\[
 {D_t(A)\over (N)_{2t}/2^t}
 \le
 \left({2S_2\over(N-2t)^2}\right)^t
 \le\left({C\over d}\right)^t.                  \tag{3.8}
\]

These bounds are uniform for \(t\le c\log m\), since
\(\log m=o(R)\).  At \(d=\Theta(\sqrt m)\), taking logarithms gives

\[
 t\log(Ct/d)=-\Omega((\log m)^2)
\]

at \(t=c\log m\), and the disjoint-pair bound is at least as strong.

The sum of all nontrivial normalized blind coefficients through this
range is also negligible:

\[
 \sum_{t=1}^{\lfloor c\log m\rfloor}
 { [z^{2t}]W_A(z)\over\binom{R-q}{2t}}
 =O(1/d)=o(1).                                      \tag{3.9}
\]

Indeed the first term is \(O(1/d)\), and subsequent ratios are bounded by
the supergeometric majorant in (3.7).

## 4. Exact home utilization at the shallow one-sided gate

Fix one typed layer and deterministic options \(g_P\).  Order the packets
arbitrarily and put

\[
 H_P=I_{P,g_P}\setminus\bigcup_{P'<P}I_{P',g_{P'}}.             \tag{4.1}
\]

Then the \(H_P\)'s are disjoint, each is a realizable home subset of one
selected compiler option, and

\[
                         \bigdotcup_P H_P=\bigcup_P I_{P,g_P}. \tag{4.2}
\]

Let

\[
                         \ell_P=|I_{P,g_P}|-|H_P|.              \tag{4.3}
\]

Since every packet image has size \(K\),

\[
                         \sum_P\ell_P
 =G-\left|\bigcup_PI_{P,g_P}\right|.              \tag{4.4}
\]

Consequently

\[
 \boxed{
 M_q^\epsilon
 =N_q-G+\sum_P\ell_P.}                             \tag{4.5}
\]

At shallow depths \(G-N_q=o(W)\).  Therefore a one-sided near-cover is
equivalent to

\[
                         \sum_P\ell_P=o(W).         \tag{4.6}
\]

In words, all but \(o(W)\) emitted rows must become distinct homes.  This
is the deterministic form of home polarization.

Now partition every \(I_{P,g_P}\) into its frontier blind cells
\(F_{P,\lambda}\).  Put

\[
                         H_{P,\lambda}=H_P\cap F_{P,\lambda}.  \tag{4.7}
\]

These are simultaneously realizable home bundles under the same packet
label, and

\[
 \sum_{P,\lambda}
   (|F_{P,\lambda}|-|H_{P,\lambda}|)
                         =\sum_P\ell_P.             \tag{4.8}
\]

Thus the residual cells create no extra loss term.  They can always be
trimmed into exact home bundles; near-cover is equivalent to using all but
\(o(W)\) of their total row mass.  Selecting only a sparse set of whole
cells still fails by the earlier capacity cut, but using the complete
resolution is lossless.

## 5. Complete parent-tagged alignment

Let \(C\) be one retained rank-twisted product parent.  The dispersed
selector partitions it into packets.  The exact packet-face recovery
lemma says that a literal face emitted by this parent determines its
unique packet.  Hence, for arbitrary selected compiler labels,

\[
                         I_{P,g_P,q}^{\epsilon}
 \cap I_{P',g_{P'},q}^{\epsilon}=\varnothing
 \qquad(P\ne P',\ P,P'\subset C).                 \tag{5.1}
\]

Partitioning each image into its frontier cells gives:

### Theorem 5.1 (complete tagged frontier resolution)

For every choice of one context-phased compiler label in every packet,
the bundles

\[
 \widetilde F_{P,\lambda}^{q,\epsilon}
 :=\{(C,T):T\in F_{P,\lambda}^{q,\epsilon}\}       \tag{5.2}
\]

are pairwise disjoint over all retained packets and parents, and their
union has exactly \(G\) members at each typed layer.

#### Proof

Within one packet, the frontier cells partition its injective image.
Equation (5.1) separates different packets of one parent.  The explicit
parent tag separates different parents.  Summing the packet image sizes
gives \(G\). \(\square\)

Thus the residual exponential cells admit an exact complete home
assignment on the parent-tagged literal occurrence set.  They do not
force holes before parent tags are erased.

Let

\[
                         \pi(C,T)=T                \tag{5.3}
\]

be the projection to the actual target layer.  All literal repeats are
exactly collisions of \(\pi\), and

\[
 \left|\pi\left(\bigdotcup_{P,\lambda}
       \widetilde F_{P,\lambda}^{q,\epsilon}\right)\right|
 =\left|\bigcup_PI_{P,g_P,q}^{\epsilon}\right|.    \tag{5.4}
\]

Combining (5.4) with the missing/repeat identity gives

\[
 \boxed{
 M_q^\epsilon
 =N_q-G+
 \sum_T\bigl(|\pi^{-1}(T)|-1\bigr)_+.}             \tag{5.5}
\]

The fibre in (5.5) is taken inside the selected tagged resolution.
Equation (5.5) contains no separate blind-cell term.

## 6. What is decided and what remains

The residual exponential blind cells do not impose an intrinsic
\(\Omega(W)\) hole count:

* their complete spectrum through logarithmic strength is negligible;
* their whole resolutions partition every packet image exactly;
* they align into an exact literal home resolution inside every parent;
  and
* after parent tagging they resolve all \(G\) occurrences with no repeat.

Therefore any proof that every globally correlated legal state has
\(\Omega(W)\) holes must exhibit a cross-parent family of physical targets
on which the projection (5.3) has unavoidable excess fibres.  The local
blind spectrum, even at all strengths, cannot be that witness by itself.

What is not decided is whether legal affine labels and cross-parent slab
trades can make the projection in (5.3) almost injective at every
protected typed layer.  The exact remaining one-sided theorem is

\[
 \min_{\text{one common legal label per packet}}
 \sum_{q\le H,\epsilon}
 \sum_T\bigl(|\pi^{-1}_{q,\epsilon}(T)|-1\bigr)_+
 =\sum_{q\le H,\epsilon}(G-N_q)+o(W).              \tag{6.1}
\]

Equivalently, the projected union must miss only \(o(W)\) targets.  This
is a cross-parent projection/resolution theorem, not a blind-flat or
finite-moment theorem.

The rigorous decision supplied here is therefore negative on the proposed
**blind-spectrum obstruction**: residual exponential cells can be aligned
into complete target bundles at the parent-tagged level, and the local
spectrum contributes no compulsory loss term.  This does not decide the
stronger literal assertion that some legal global projection has
\(o(W)\) holes; nor does it prove that every such projection has
\(\Omega(W)\) holes.  Those two alternatives are now exactly the
cross-parent projection problem (6.1), with the blind-cell issue removed.
