# Compiler column types and the realizable-bundle hypergraph gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

At one fixed signed depth \(q=A\sqrt m+O(1)\), the correct home-bundle
object is a colored \(2^R\)-uniform hypergraph:

* its vertices are literal rank-\((m\mp q)\) targets;
* a color is one dispersed transversal packet \(P\); and
* its color-\(P\) edges are the affine compiler images
  \(I_{P,g,q}^{\epsilon}\), \(g\in\Gamma_R\).

A near-perfect rainbow matching in this hypergraph would partition all
but \(o(W)\) targets into compiler-realizable home bundles.  Repeating
the matching in \(c_q=\lfloor G/N_q\rfloor\) full rounds and one residual
round would give the integer-minimal \(c_q/c_q+1\) floor profile at this
one layer.

The complete coordinate-column invariant classifies the edges exactly.
Write \(K=2^R\).  Index the base compiler faces by their starts
\(x\in Q_R\), and define the column word

\[
 C_i^{q,\epsilon}(x)=
 \begin{cases}
 *,&i\in J_{q,\epsilon}(x),\\
 x_i,&i\notin J_{q,\epsilon}(x).
 \end{cases}                                        \tag{0.1}
\]

An affine conjugate independently complements the \(0/1\) symbols in
each column and permutes the \(R\) columns; it leaves the stars fixed.
Thus a full compiler image is classified by the multiset of the column
words \(C_i\), modulo columnwise complementation.  A partial bundle is
realizable exactly when, after some bijection to a subset of base
compiler rows, its column-type multiset has this form.

This classification gives an exact pair-codegree kernel.  If

\[
 \omega=(a,\delta)
 =\left(|J\cap J'|,
 |\{i\notin J\cup J':\eta_i\ne\eta'_i\}|\right),    \tag{0.2}
\]

put

\[
 M_{R,q}(a,\delta)
 =\binom qa\binom{R-q}{q-a}2^{q-a}
   \binom{R-2q+a}{\delta}.                           \tag{0.3}
\]

This is the number of faces of type \(\omega\) relative to one fixed
face.  Let \(A_{q,\epsilon}(a,\delta)\) be the number of ordered pairs of
distinct base compiler faces of this type.  For two compatible physical
faces of type \(\omega\), the fraction of affine labels containing both
is exactly

\[
 {A_{q,\epsilon}(a,\delta)
  \over V_{R,q}M_{R,q}(a,\delta)},
 \qquad
 V_{R,q}=\binom Rq2^{R-q}.                          \tag{0.4}
\]

The transversal selector theorem controls neither
\(A_{q,\epsilon}\) nor the distribution of the packet-relative types
\(\omega_P(T,T')\) across different product cells.

There is a universal nonrandom atom.  Every component has a
doubled-permutation word, so the start \(x+{\bf1}\), half a cycle later,
has the same support and complementary outside orientation.  Hence every
compiler image is closed under packet antipodes and

\[
 A_{q,\epsilon}(q,R-q)=K,\qquad
 M_{R,q}(q,R-q)=1.                                  \tag{0.5}
\]

Consequently, inside one packet, the pair codegree of a face and its
antipode equals its full single-face degree: every option containing one
contains the other.  Thus the bundle hypergraph is not a low-codegree
random design at the local affine level.  A generic nibble based only on
one-point twirling is invalid.

No \(\Omega(W)\) global target deficit follows from (0.5), because the
packet antipodal involution varies with the physical packet.  Conversely,
the current theorems do not prove the weighted Hall/design inequalities
for the colored hypergraph.  The exact missing finite data are:

1. the full compiler column-type enumerators, beginning with
   \(A_{q,\epsilon}(a,\delta)\);
2. the quenched distribution of the relative types
   \(\omega_P(T,T')\) under the dispersed packet selector; and
3. their common refinement across depths and signs for one affine label.

Accordingly, no realizable-bundle partition or \(\Omega(W)\) type cut is
currently certified.  Sections 5--7 state the precise design theorem
which would settle the fixed window and explain why the all-depth problem
requires a joint column-type, not separate marginal bundle designs.

## 1. Exact full-image column classification

Fix the diverse-order compiler factor \(F\) on \(Q_R\), one orientation,
one sign \(\epsilon\), and one depth \(q\le H\).  For every start
\(x\in Q_R\), let

\[
                         J_{q,\epsilon}(x)\subseteq[R]           \tag{1.1}
\]

be its \(q\)-window direction support.  Literal trace injectivity says
that the faces

\[
 f_{q,\epsilon}(x)
 =\bigl(J_{q,\epsilon}(x),
        x|_{[R]\setminus J_{q,\epsilon}(x)}\bigr)    \tag{1.2}
\]

are all distinct.

Form a \(K\times R\) matrix with rows \(x\) and columns \(i\), whose
entries are (0.1).  A translation \(b\in Q_R\) replaces every fixed
entry in column \(i\) by its complement when \(b_i=1\), while leaving
\(*\) unchanged.  A direction permutation merely permutes columns.
Therefore:

### Theorem 1.1 (full-image affine classification)

Two full signed \(q\)-face images are affine-cube equivalent if and only
if there is a bijection of their face rows under which the multisets of
their \(R\) column words agree, after independently exchanging \(0\) and
\(1\) in each column.

#### Proof

Necessity is the preceding action calculation.  Conversely, match equal
column types, use the resulting coordinate permutation, and complement
exactly the columns whose fixed symbols are exchanged.  The stars give
the varied-coordinate sets and the fixed symbols give every outside
orientation, so the resulting affine map carries every row face to its
matched row.  \(\square\)

The theorem has a simultaneous version.  Stack the rows indexed by
\((q,\epsilon,x)\) for all protected depths and signs.  One option
realizes the entire stacked catalogue precisely when the same column
permutation and the same columnwise complements work in every row block.

For a partial home bundle, one first chooses an injection of its faces
into the appropriate base row block and applies the same column test.
This is equivalent to the nonempty allowed-conjugate intersection in the
home-packet audit.

## 2. Universal one-column census

Although the complete column words depend on the recursive compiler,
their one-column symbol counts are forced.

### Lemma 2.1 (balanced column census)

For every physical direction \(i\),

\[
 \#\{x:i\in J_{q,\epsilon}(x)\}={qK\over R},         \tag{2.1}
\]

and among the remaining starts, the fixed symbols in column \(i\) are
equally split:

\[
 \#\{x:i\notin J(x),x_i=0\}
 =\#\{x:i\notin J(x),x_i=1\}
 ={K\over2}\left(1-{q\over R}\right).               \tag{2.2}
\]

#### Proof

Every compiler component is an isometric \(C_{2R}\) with a
doubled-permutation direction word.  Direction \(i\) occurs twice on a
component, and each occurrence belongs to exactly \(q\) directed
\(q\)-windows.  Hence it occurs in \(2q\) window supports per component.
There are \(K/(2R)\) components, proving (2.1).

Starts half a component apart differ by \({\bf1}\), have the same
window support, and complement every outside orientation.  They pair the
fixed zero and one symbols, proving (2.2).  \(\square\)

In particular every full image is closed under the packet-antipodal map

\[
                         (J,\eta)\longmapsto(J,\eta+{\bf1}_{J^c}).         \tag{2.3}
\]

The one-column census is compatible with the global target-layer
coordinate marginals after dispersed packet averaging.  It gives no
one-coordinate \(\Omega(W)\) deficit.

## 3. Pair types and exact affine codegrees

Fix a physical \(q\)-face \(f=(J,\eta)\).  A second face
\(f'=(J',\eta')\) has pair type

\[
                         \omega(f,f')=(a,\delta)     \tag{3.1}
\]

as in (0.2).  To count its orbit shell:

1. choose \(a\) directions of \(J\) for \(J\cap J'\);
2. choose the remaining \(q-a\) directions of \(J'\) outside \(J\);
3. choose the fixed symbols of \(f'\) on the \(q-a\) coordinates in
   \(J\setminus J'\); and
4. choose the \(\delta\) disagreements on the
   \(R-2q+a\) coordinates fixed in both faces.

This proves (0.3).

Let

\[
 A_{q,\epsilon}(a,\delta)
 =|\{(x,x'):x\ne x',\
       \omega(f_{q,\epsilon}(x),f_{q,\epsilon}(x'))
        =(a,\delta)\}|.                             \tag{3.2}
\]

The affine group acts transitively on faces and on ordered pairs of a
fixed type.  The ordered-pair orbit has size

\[
                         V_{R,q}M_{R,q}(a,\delta).   \tag{3.3}
\]

Double counting affine labels and base ordered pairs proves:

### Lemma 3.1 (pair-label multiplicity)

For fixed physical faces \(f,f'\) of type \((a,\delta)\),

\[
 {|\{g:f,f'\in g{\mathfrak F}_{q,\epsilon}\}|
  \over|\Gamma_R|}
 ={A_{q,\epsilon}(a,\delta)
  \over V_{R,q}M_{R,q}(a,\delta)}.                 \tag{3.4}
\]

For one face the corresponding probability is

\[
                         \theta_{R,q}={K\over V_{R,q}}
                         ={2^q\over\binom Rq}.       \tag{3.5}
\]

Therefore the conditional pair probability is

\[
 {A_{q,\epsilon}(a,\delta)
  \over K\,M_{R,q}(a,\delta)}.                      \tag{3.6}
\]

For the antipodal type \((q,R-q)\), every base face has exactly its
antipodal mate, proving (0.5).  Equation (3.6) then equals one.

The complete \(k\)-face codegree is obtained by replacing the pair type
with the column-type multiset of Theorem 1.1.  Thus the column invariant
is not merely a realizability test; it is the exact higher-codegree
parameter of the option hypergraph.

## 4. The colored realizable-bundle hypergraph

Fix one depth and sign.  Let

\[
                         {\cal V}_q^\epsilon={\cal T}_q^\epsilon          \tag{4.1}
\]

be the literal target layer.  For every dispersed packet \(P\) and
affine label \(g\), define the edge

\[
                         E_{P,g}=I_{P,g,q}^{\epsilon}.            \tag{4.2}
\]

Trace injectivity gives

\[
                         |E_{P,g}|=K.              \tag{4.3}
\]

Color \(E_{P,g}\) by \(P\).  Options of one color are mutually exclusive.
Call the resulting colored hypergraph \({\cal H}_{q,\epsilon}\).

For a target \(T\), let \(d_{\rm cand}(T)\) be the number of dispersed
packets in which \(T\) is a physical \(q\)-face.  Its exact degree is

\[
 d_{\cal H}(T)
 =|\Gamma_R|\theta_{R,q}d_{\rm cand}(T).            \tag{4.4}
\]

For two targets, sum only over packets in which both are compatible.  If
their packet-relative type is \(\omega_P(T,T')\), Lemma 3.1 gives

\[
 d_{\cal H}(T,T')
 =|\Gamma_R|
 \sum_{P:\,T,T'\text{ compatible}}
 {A_{q,\epsilon}(\omega_P(T,T'))
  \over V_{R,q}M_{R,q}(\omega_P(T,T'))}.            \tag{4.5}
\]

Equations (4.4)--(4.5) are the exact degree and codegree ledger requested
by a bundle-design theorem.  The transversal selector gives
anti-localization and safe-profile averages for \(d_{\rm cand}(T)\).
It does not give a quenched lower bound for every weighted target family,
nor does it control the sum in (4.5).

## 5. The fixed-window bundle design theorem which would suffice

Put

\[
                         \lambda_q={G\over N_q}
                         =c_q+\alpha_q.              \tag{5.1}
\]

There are

\[
                         b={G\over K}                \tag{5.2}
\]

packet colors.  A particularly strong sufficient construction is:

1. choose \(c_q\) disjoint color classes of size \(N_q/K+o(W/K)\);
2. in each class choose one edge per color forming a matching which
   covers all but \(o(W)\) target vertices; and
3. from the remaining colors choose
   \(\alpha_qN_q/K+o(W/K)\) edges forming a matching on
   \(\alpha_qN_q+o(W)\) additional targets.

Choose arbitrary options in colors not used by these matchings, subject
to placing their occurrence mass into the same \(c_q/c_q+1\) quotas.
Equivalently, use all colors and require the final degree of every target
to be \(c_q\) or \(c_q+1\), outside \(o(W)\) exceptions.

This is a rainbow near-resolution of
\({\cal H}_{q,\epsilon}\).  It gives compiler-realizable bundles by
construction; no post hoc lifting is needed.

The exact fractional Hall inequality underlying even one covering round
is

\[
 \sum_P\max_{g}
       \sum_{T\in E_{P,g}}y_T
 \ge\sum_Ty_T-o(W)\|y\|_\infty
 \qquad(y\ge0).                                     \tag{5.3}
\]

For floor resolution, arbitrary real weights and the quota hypersimplex
give the stronger configuration dual

\[
 \sum_P\min_g\sum_{T\in E_{P,g}}y_T
 \le c_q\sum_Ty_T+
       \sum_{\text{\(G-c_qN_q\) largest }y_T}y_T.   \tag{5.4}
\]

The current profile Hall theorem proves neither (5.3) nor (5.4) for
arbitrary block-labelled \(y\).

### Missing design hypothesis

A standard low-codegree nibble cannot be invoked from present data.
Already inside one color, antipodal faces have conditional codegree one.
After contracting these pairs one would still need:

\[
 \begin{aligned}
 d_{\cal H}(T)&=(1+o(1))D_q
       &&\text{outside }o(W)\text{ targets},\\
 d_{\cal H}(T,T')&=o(D_q/K)
       &&\text{for every noncontracted pair},        \tag{5.5}
 \end{aligned}
\]

or another quantitative hypothesis strong enough for a
growing-uniformity rainbow matching theorem.  Neither line follows from
axis anti-localization.  In particular, (4.5) shows that it requires the
actual compiler pair enumerator and packet-relative type census.

No proof of (5.5), and no target family violating (5.3) by
\(\Omega(W)\), is currently available from the stated theorems.

## 6. Paired signs and common depths

For one physical occurrence, the lower and upper targets have the same
abstract face \((J,\eta)\): the lower target empties the axes in \(J\),
while the upper target fills them.  Hence one option produces the paired
edge

\[
 E_{P,g,q}^{\rm pair}
 =I_{P,g,q}^-\mathbin{\dot\cup}I_{P,g,q}^+          \tag{6.1}
\]

on the disjoint union of the lower and upper target layers.  Its two
projections both have size \(K\) and share the same column-type
catalogue.

A two-sign home theorem needs a rainbow matching of these paired edges,
disjoint separately on both shores.  Separate lower and upper matchings
cannot be combined after the fact because they may choose different
labels \(g\) in the same packet.

For all depths, define the configuration edge

\[
 {\bf E}_{P,g}
 =\bigdotcup_{\epsilon\in\{-,+\}}
   \bigdotcup_{q=1}^H I_{P,g,q}^{\epsilon}.          \tag{6.2}
\]

One common \(g\) controls every layer.  The complete column invariant is
obtained by stacking all \((q,\epsilon)\) row blocks before comparing
column types.  A separate bundle design at each depth generally chooses
incompatible packet labels and therefore does not diagonalize.

The exact all-depth floor condition is the product-quota dual

\[
 \sum_P\min_g
 \sum_{q,\epsilon}\sum_{T\in I_{P,g,q}^{\epsilon}}
 y_{q,\epsilon,T}
 \le
 \sum_{q,\epsilon}h_{{\cal B}_{q,\epsilon}}
       (y_{q,\epsilon,\cdot})                       \tag{6.3}
\]

for every real target array \(y\).  A common-bundle construction proves
coefficient one only after satisfying (6.3) and rounding one label per
packet.

## 7. Type-count conclusion

The column-type classification is constructive in the following exact
sense:

1. it decides whether any proposed packet bundle is one affine compiler
   image or a subset of one;
2. its \(k\)-column histograms give every local option codegree; and
3. the pair histogram yields the explicit kernel (4.5).

It does not, from the current inputs, yield a partition of the global
target layer.  The dispersed selector controls where supports live but
does not control the compiler type enumerator
\(A_{q,\epsilon}(a,\delta)\) or its alignment between product cells.
The universal antipodal atom (0.5) disproves a naive local
quasirandomness assumption, but because packet antipodes vary, it is not
an \(\Omega(W)\) global Hall cut.

Therefore the exact next finite theorem is:

> Compute the recursive compiler's joint column-type enumerator and prove
> that the dispersed packet-relative type census makes (4.4)--(4.5)
> satisfy a rainbow near-resolution theorem, after contracting the forced
> antipodal atoms, simultaneously for the paired configuration edges
> (6.1).

Absent that enumerator theorem, neither a realizable home-bundle design
nor an \(\Omega(W)\) type-count deficit has been proved.

