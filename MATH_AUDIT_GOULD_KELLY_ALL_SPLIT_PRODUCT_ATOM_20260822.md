# Gould--Kelly does not yield an all-split product-atom near-factor

**Date:** 2026-08-22

## 0. Verdict

Let \(b=2h+1\ge 5\), let

\[
  \mathcal V={\Omega\choose b},\qquad |\Omega|=2b,
\]

and let \(\mathcal H_b\) be the labelled all-split product-atom
multihypergraph of Appendix F.  Thus every edge has

\[
  r=b^2
\]

vertices and every vertex has degree

\[
  D=(b!)^2.
\]

Theorem 1.4 of Gould--Kelly, *Advancing the R\"odl Nibble: New bounds on
matchings and the list chromatic index of hypergraphs*,
[arXiv:2511.11375](https://arxiv.org/abs/2511.11375), does **not** imply a
matching covering \((1-o(1))|\mathcal V|\) in \(\mathcal H_b\).

There are three independent issues.

1. The theorem is quantified for fixed uniformity:

   \[
      1/D\ll 1/A\ll\gamma\ll 1/k,
      \qquad k+1=r=b^2.
   \]

   It states no uniform threshold for \(k\to\infty\).

2. Even if one grants a uniform-in-\(k\) version and ignores all higher
   codegrees, the exact pair row gives

   \[
      B\le\sqrt{D/C_2}=b/2,
   \]

   while \(\log D=2b\log b+O(b)\).  Hence, already for the formally best
   possible \(A=1\), the published relative leave

   \[
      B^{-1+\gamma}\log^A D
   \]

   is \(\Omega(b^\gamma\log b)\), not \(o(1)\).

3. The full codegree sequence gives a much sharper obstruction.  The
   codegree of a complete \(r\)-edge is exactly four, so Theorem 1.4
   forces

   \[
      \boxed{
      B\le \left({(b!)^2\over4}\right)^{1/(b^2-1)}
       =1+O\left({\log b\over b}\right).}
   \]

   Thus the theorem's numerical conclusion is vacuous even before the
   fixed-uniformity quantifier is considered.

The reserve and bipartite variants retain the same hierarchy, the same
full-sequence bottleneck, and the same \(B^{-1+\gamma}\log^A D\) overhead.
They do not repair the conclusion.  Uniform parallel-multiplicity
amplification leaves every relevant ratio unchanged and increases the
logarithmic loss.

This is a black-box obstruction only.  It is not an integral-packing
impossibility for \(\mathcal H_b\).

## 1. The exact Gould--Kelly constraint

Gould--Kelly use \((k+1)\)-uniformity.  Their Theorem 1.4 says, in the
notation relevant here, that if

\[
   1/D\ll1/A\ll\gamma\ll1/k\le1,
\]

\(H\) is \((n,D,\varepsilon)\)-regular and \((k+1)\)-uniform, and

\[
   C_j(H)\le D_j\quad(2\le j\le k+1),
   \qquad D_2\ge D_3\ge\cdots\ge D_{k+1},
\]

then every

\[
  1\le B\le
  \min\left\{
    \sqrt{D/D_2},
    \min_{4\le j\le k+1}(D/D_j)^{1/(j-1)},
    1/\varepsilon
  \right\}                                                \tag{1.1}
\]

gives a matching leaving at most

\[
                      nB^{-1+\gamma}\log^A D              \tag{1.2}
\]

vertices uncovered.  Multihypergraphs are explicitly permitted, and all
degrees and codegrees count edge copies.

For \(\mathcal H_b\), the correct substitution is

\[
                         k=b^2-1.                          \tag{1.3}
\]

Exact regularity causes no \(\varepsilon\)-problem: one may describe an
exactly \(D\)-regular hypergraph as \((n,D,\varepsilon)\)-regular for any
chosen positive \(\varepsilon\), so the last term of (1.1) can be made
nonbinding.

## 2. The two exact codegree rows that settle the question

Appendix F proves

\[
  {\lambda_d\over D}
   ={4\min(d,b-d)\over\binom bd^2}\quad(1\le d<b),
  \qquad \lambda_b=0.
\]

Consequently

\[
  \boxed{C_2=\lambda_1=4((b-1)!)^2,\qquad {C_2\over D}={4\over b^2}.}
                                                                  \tag{2.1}
\]

It remains to record the other endpoint of the codegree sequence.

### Lemma 2.1 (exact labelled edge multiplicity)

Every unlabelled product-atom edge has exactly four labels
\((A,\alpha,\beta)\).  In particular,

\[
                             \boxed{C_{b^2}=4.}            \tag{2.2}
\]

#### Proof

Fix

\[
 E=E(A,\alpha,\beta)
  =\{I_\alpha(i,h)\cup I_\beta(j,h+1):(i,j)\in\mathbb Z_b^2\}.
\]

For a ground element \(x\in\Omega\), count the members of \(E\) that
contain \(x\).  If \(x\in A\), it belongs to \(h\) of the \(b\)
length-\(h\) intervals of \(\alpha\), and hence to exactly \(hb\) members
of \(E\).  If \(x\in\Omega\setminus A\), it belongs to exactly
\((h+1)b\) members.  Since these two frequencies differ, the set \(A\)
is recoverable from the unlabelled edge \(E\).

Projecting \(E\) to \(A\) recovers the deck of all length-\(h\) intervals
of \(\alpha\).  That deck determines the underlying unoriented cycle:
for two points at cyclic distance \(t\le h\), the number of deck members
containing both is \(h-t\), so the pairs attaining the maximum \(h-1\)
are precisely the adjacent pairs.  Thus \(\alpha\) is determined up to
reversal.  On \(\Omega\setminus A\), complementing every recovered
length-\((h+1)\) interval gives the length-\(h\) deck, so \(\beta\) is
also determined up to reversal.  The two reversals are independent and
all four choices give the same set \(E\).  Hence the multiplicity is
exactly four. \(\square\)

For completeness, an explicit upper sequence valid at every order is

\[
 \overline D_j=
 \begin{cases}
   4((b-1)!)^2,&2\le j<b^2,\\
   4,&j=b^2.
 \end{cases}                                               \tag{2.3}
\]

Indeed \(C_j\le C_2\) for all \(j\ge2\).  This deliberately loose
intermediate envelope is not used below.  Taking the exact maxima
\(D_j=C_j\) can only optimize (1.1), and the exact endpoint (2.2) still
applies.  Therefore no calculation of the intermediate \(C_j\)'s can
change the negative verdict.

## 3. Substitution: the endpoint beats the pair bottleneck

The pair term in (1.1) gives exactly

\[
                         B\le {b\over2}.                  \tag{3.1}
\]

The \(j=b^2\) term and (2.2) give

\[
 B\le B_{\rm end}
  \coloneqq\left({(b!)^2\over4}\right)^{1/(b^2-1)}.       \tag{3.2}
\]

Stirling's formula yields

\[
 \begin{aligned}
  \log B_{\rm end}
   &={2\log(b!)-\log4\over b^2-1}\\
   &={2\log b-2\over b}
      +O\left({\log b\over b^2}\right),                 \tag{3.3}
 \end{aligned}
\]

and hence

\[
 B_{\rm end}
  =1+{2\log b-2\over b}
     +O\left({(\log b)^2\over b^2}\right)=1+o(1).        \tag{3.4}
\]

Thus the full-edge row, not (3.1), is the actual Gould--Kelly
bottleneck.  This is the universal endpoint phenomenon behind the
calculation: every nonempty \(r\)-uniform hypergraph has \(C_r\ge1\), so
the Gould--Kelly parameter is at most \(D^{1/(r-1)}\); here
\(\log D=o(r)\).  For every \(0<\gamma<1\),

\[
                  B_{\rm end}^{-1+\gamma}=1-o(1),        \tag{3.5}
\]

whereas

\[
                  \log D=2\log(b!)=2b\log b+O(b).        \tag{3.6}
\]

Since the hierarchy takes \(A\) sufficiently large (in particular
\(A\ge1\)), the right side of (1.2) eventually exceeds \(n\).  The bound
therefore gives no nontrivial matching size.

Even if one incorrectly deleted the \(j=b^2\) condition and used the
optimistic pair ceiling \(B=b/2\), equations (3.1) and (3.6) give

\[
 B^{-1+\gamma}\log^A D
 \ge B^{-1+\gamma}\log D
 =\Omega(b^\gamma\log b)\longrightarrow\infty.           \tag{3.7}
\]

Thus the \(\log^A D\) loss is independently fatal at the pair scale.

## 4. Fixed uniformity and multiplicity amplification

The hierarchy in Theorem 1.4 has its standard order-of-quantifiers
meaning: first fix \(k\), then choose \(\gamma\), then \(A\), and only
then take \(D\) large.  It does not state that the theorem holds along

\[
             k=b^2-1,\qquad D=(b!)^2.                    \tag{4.1}
\]

This is material in the proof.  For example, one hierarchy consequence
used in the codegree-family estimate is

\[
                   \log^5D\ge 2^k(k+1)^{2k+2}.            \tag{4.2}
\]

For (4.1), the logarithm of the left side of (4.2) is \(O(\log b)\),
while the logarithm of its right side is \(\Theta(b^2\log b)\).  Hence
the published proof does not diagonalize to the present parameters.

Uniform multiplicity amplification does not help.  If every labelled
atom is replaced by \(R\) parallel copies, then

\[
 D^{(R)}=RD,\qquad C_j^{(R)}=RC_j\quad(2\le j\le b^2).    \tag{4.3}
\]

In particular,

\[
 {D^{(R)}\over C_2^{(R)}}={D\over C_2},\qquad
 {D^{(R)}\over C_{b^2}^{(R)}}={D\over4}.                 \tag{4.4}
\]

So amplification can make \(D\) exceed an unspecified fixed-\(k\)
threshold, but it leaves every admissible value of \(B\) unchanged and
replaces \(\log^A D\) by the larger \(\log^A(RD)\).  It strictly worsens
the numerical leave bound.

Deleting the four parallel labels is equally ineffective.  The simple
atom hypergraph has degree \(D/4\), pair codegree \(C_2/4\), and
full-edge codegree one.  Both ratios in (4.4), and therefore both
bottlenecks, are unchanged.

More generally, sparsifying to any nonempty regular subhypergraph of the
available product atoms cannot improve the endpoint.  If its degree is
\(d\), then its complete-edge codegree is at least one and \(d\le D\), so

\[
                         B\le d^{1/(b^2-1)}
                           \le D^{1/(b^2-1)}=1+o(1).       \tag{4.5}
\]

Thus thinning may reduce \(\log d\), but it makes the endpoint constraint
at least as restrictive.

The phase refinement in Appendix F has the same behavior: it multiplies
degrees and all full-atom codegrees by the same factor \(b\), so it does
not alter the relevant ratios.

## 5. The reserve and bipartite variants do not bypass the scale

The Gould--Kelly reserve theorem and Bipartite Matching Theorem have the
same fixed-rank hierarchy and the same constraint

\[
 B\le\min\left\{\sqrt{D/D_2},
       \min_{4\le j\le k+1}(D/D_j)^{1/(j-1)}\right\}.     \tag{5.1}
\]

Their reserve/surplus requirement contains the same factor

\[
                       q=B^{-1+\gamma}\log^A D.          \tag{5.2}
\]

The list-edge-colouring corollary does not provide an indirect escape.
It has the additional constraint \(B\le D^{1/b^2}=1+o(1)\).  Colouring
all atoms and taking the largest colour class gives only the guaranteed
covered fraction \(1/(1+q)\), and here \(q\) is not \(o(1)\).

The canonical bipartite encoding makes the obstruction explicit.  Put
\(N=|\mathcal V|\), introduce \(m\) slot vertices \(X=[m]\), retain
\(Y=\mathcal V\), and for each slot \(x\) and atom \(E\) use the
auxiliary edge \(\{x\}\cup E\).  An \(X\)-perfect matching is precisely
a choice of \(m\) pairwise disjoint atoms.

There are \(ND/b^2\) labelled atoms.  Thus

\[
 \deg(x)={ND\over b^2}\quad(x\in X),
 \qquad
 \deg(y)=mD\quad(y\in Y).                               \tag{5.3}
\]

Taking the best possible degree scale \(\mathscr D=mD\), the bipartite
theorem's hypothesis \(\deg(x)\ge(1+q)\mathscr D\) forces

\[
                  m\le {N\over b^2(1+q)}.                \tag{5.4}
\]

Hence a \((1-o(1))\)-cover through this encoding requires \(q=o(1)\).
But the auxiliary edges have size \(b^2+1\), their complete-edge
codegree is again four, and for \(m\le N/b^2\),

\[
 \log\mathscr D=\Theta(b\log b),\qquad
 B\le(\mathscr D/4)^{1/b^2}
   =1+O\left({\log b\over b}\right).                    \tag{5.5}
\]

Thus (5.2) is not \(o(1)\); in fact it diverges.  The reserve theorem is
a conditional way to mop up a leave when a sufficiently dense, bounded
reserve has already been supplied.  It does not construct a reserve for
the product atoms, and its required factor (5.2) is at the same unusable
scale here.

## 6. Fragments do not make this Gould--Kelly application work

For the phase-refined length-\(L\) fragment hypergraph of Appendix F,

\[
                         D_L=Lb(b!)^2,                    \tag{6.1}
\]

and the uniformity is \(L\).  Since every nonempty \(L\)-uniform
hypergraph has \(C_L\ge1\), Theorem 1.4 necessarily imposes

\[
                         B\le D_L^{1/(L-1)}.              \tag{6.2}
\]

In the seam-compatible range at
\(H=\lceil\sqrt{b\log b}\rceil\), Appendix F requires

\[
                         L\gg bH\gg b\log b.             \tag{6.3}
\]

But \(\log D_L=\Theta(b\log b)\), so (6.2)--(6.3) imply

\[
                         \log B=o(1).                    \tag{6.4}
\]

Thus the full-codegree endpoint also blocks the seam-compatible fragment
range.  Shorter fragments do not solve the original problem: they fail
the seam budget and a fragment matching does not by itself reassemble
into a matching of full product atoms with common nearby-rank control.

## 7. What “clustering” and elementary quotients can and cannot do

The “clustering” tolerated by Gould--Kelly is clustering among the
numbers \(D_2,D_3,\ldots,D_{k+1}\).  It does not remove the explicit
\(\sqrt{D/D_2}\) term or the full-edge terms in (1.1).

There are two immediate quotient ideas, and both fail rigorously.

1. **Quotient parallel atom labels.**  Section 4 shows that this divides
   \(D,C_2,C_{b^2}\) by four and changes neither relevant ratio.

2. **Collapse every maximum-codegree vertex pair.**  The distance-one
   pairs already form the Johnson graph \(J(2b,b)\), which is connected:
   any \(b\)-set can be transformed into any other by successive
   one-element exchanges.  Therefore any equivalence relation identifying
   both endpoints of every distance-one pair has a single class.  Its
   quotient carries no near-factor information.

Splitting target vertices into incidence or position copies removes the
pair codegree only by allowing two selected atoms to use different copies
of the same original target.  That lifted matching no longer projects to
an atom matching.  Adding an original-target resource to restore the
projection also restores the original \(b^2\) conflict resources and the
same endpoint obstruction.

These observations do **not** rule out every asymmetric restriction,
conflict-system theorem, or object-specific quotient.  They show that no
parallel-edge quotient, phase refinement, all-high-pair clustering, or
standard bipartite lift turns the desired result into a consequence of
Gould--Kelly.  A genuine replacement would have to compress the
\(b^2\) target conflicts to much smaller effective rank while still
ensuring that quotient matchings project to disjoint full atoms; no such
construction is presently proved in Appendix F.

## 8. Precise conclusion

The exact logical status is:

* Theorem 1.4 is not uniform in \(b^2\)-uniformity.
* Granting uniformity does not help: the complete-edge codegree gives
  \(B=1+o(1)\).
* Even granting the fictitious pair-optimal value \(B=b/2\), the
  \(\log^A D\) factor makes the claimed leave larger than the vertex set.
* Uniform multiplicity amplification preserves the pair and endpoint
  ratios and worsens the logarithmic term.
* The reserve, bipartite, simple-edge, phase-refined, and seam-compatible
  fragment versions retain one or more of the same decisive bottlenecks.
* Collapsing all maximum-codegree pairs is the trivial quotient because
  the Johnson distance-one graph is connected.

Therefore Gould--Kelly arXiv:2511.11375 supplies no rigorous
\(o(1)\)-leave matching for the all-split product-atom hypergraph.  The
near-factor hypothesis in Appendix F remains an object-specific
growing-uniformity packing gate.
