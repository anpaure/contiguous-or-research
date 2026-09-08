# QRE compression: annealed profile symmetry and quenched shifting no-go

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Result

Consider the maximal lower or upper rank-twisted compatibility graph with
independent perfect matchings on every macroblock and every local rank.
There are two sharply different compression statements.

1. **Annealed compression is valid.**  After averaging the matching
   array, the graph is invariant under arbitrary independent coordinate
   permutations in every macroblock half.  The Hall-deficiency functional

   \[
                     h(\mathcal A)=|N(\mathcal A)|-|\mathcal A|
   \tag{0.1}
   \]

   is submodular.  Consequently, if an annealed Hall obstruction exists,
   one of maximum deficiency is a union of the ordered half-profile orbits

   \[
       \bigl(|T\cap A_j|,|T\cap C_j|\bigr)_{j\le b}.     \tag{0.2}
   \]

   The same conclusion holds for any exactly group-invariant weighted
   Hall functional.  This formally justifies profile compression for the
   averaged quotient.

2. **Quenched coordinate shifting is false as a structural theorem.**
   Fix even \(d\ge6\), let \(b=m/d\), and let \(1\le q\le b\).  For every
   standard within-half coordinate compression \(C_{uv}\), there are
   legal rank-matching arrays and lower targets \(T\), of global rank
   \(m-q\), for which

   \[
   \boxed{
     |N^-(C_{uv}T)|-|N^-(T)|
        =2^q\binom{b-1}{q-1}>0.}                       \tag{0.3}
   \]

   There are equally legal arrays for which the difference is the
   negative of (0.3).  Complementation gives the same two conclusions on
   the upper shore at rank \(m+q\).  Thus no fixed direction of ordinary
   coordinate shifting can monotonically reduce all raw Hall
   neighborhoods, even when \(q=A\sqrt m+O(1)\).

3. For an independent quenched array, the common within-half automorphism
   group of all \(2d+1\) rank matchings in one macroblock is trivial with
   probability \(1-o(1)\).  Hence the annealed orbit argument has no
   quenched symmetry group on which to operate.  Likewise, exact
   matching-status orbits for one rank do not survive the independent
   matchings at the other ranks.

These statements refute the proposed **standard compression proof** of
QRE\(_A\).  They do not refute QRE\(_A\) itself, nor do they prove that a
minimum quenched cut cannot accidentally be profile-measurable.  Any such
theorem must be a genuinely probabilistic isoperimetric statement for the
raw realized graph; it cannot follow from the usual edge-preserving
shifts or from automorphism symmetrization.

## 1. The general automorphism-compression lemma

Let \(G=(L,R;E)\) be a finite bipartite graph.  For
\(\mathcal A\subseteq L\), put

\[
                         h(\mathcal A)=|N(\mathcal A)|-|\mathcal A|.
\tag{1.1}
\]

### Lemma 1.1 (submodular minimum cuts)

The function \(h\) is submodular:

\[
 h(\mathcal A\cap\mathcal B)+h(\mathcal A\cup\mathcal B)
 \le h(\mathcal A)+h(\mathcal B).                     \tag{1.2}
\]

If a finite group \(\Gamma\) acts by graph automorphisms, then among the
global minimizers of \(h\) there is a \(\Gamma\)-invariant one.

#### Proof

Neighborhood cardinality is a coverage function and is submodular:

\[
 |N(\mathcal A\cap\mathcal B)|
 +|N(\mathcal A\cup\mathcal B)|
 \le |N(\mathcal A)|+|N(\mathcal B)|.
\]

Cardinality is modular, proving (1.2).  If \(\mathcal A,\mathcal B\) are
global minimizers, the two terms on the left of (1.2) are each at least
the minimum, so both are minimizers.  For every \(g\in\Gamma\),
\(g\mathcal A\) is a minimizer.  Iterating unions over the finite orbit
gives the invariant minimizer

\[
                         \bigcup_{g\in\Gamma}g\mathcal A.
\]

It is a union of \(\Gamma\)-orbits. \(\square\)

The same proof applies to a group-invariant capacitated neighborhood
functional, replacing vertex cardinalities by invariant modular
capacities.

## 2. Application to the annealed rank-matching graph

In macroblock \(B_j=A_j\dot\cup C_j\), average independently over every
perfect matching

\[
                         \pi_{j,k}:A_j\longrightarrow C_j.
\]

For a fixed inclusion \(T\subset X\), put

\[
 \alpha_j=|X\cap A_j|,\qquad \gamma_j=|X\cap C_j|,
 \qquad
 \ell_A=|(X\setminus T)\cap A_j|,\quad
 \ell_C=|(X\setminus T)\cap C_j|.
\]

Its averaged retention probability depends only on

\[
 \alpha_j,\quad\gamma_j,\quad\ell_A,\quad\ell_C.       \tag{2.1}
\]

Indeed it is the product of the exact falling-factorial probabilities

\[
 { (d-\gamma_j)_{\underline{\ell_A}}
   \over d_{\underline{\ell_A}}}
 { (d-\alpha_j)_{\underline{\ell_C}}
   \over(d-\ell_A)_{\underline{\ell_C}}}               \tag{2.2}
\]

on the lower shore, with the corresponding occupied-coordinate formula
above the middle.  Therefore the averaged weighted graph is invariant
under

\[
 \Gamma=\prod_{j=1}^b
   \bigl(S(A_j)\times S(C_j)\bigr).                    \tag{2.3}
\]

The target orbits of \(\Gamma\) are exactly the ordered half profiles
(0.2).  Lemma 1.1 proves the annealed assertion in Section 0.  If the
minimum of \(h\) is negative, the invariant minimizer produced there is
nonempty and is a genuine Hall obstruction.  If no obstruction exists,
the empty set is of course the trivial invariant minimizer.

This is an existence statement for a minimum profile cut.  It is stronger
than merely averaging a chosen cut's indicator, but it uses exact graph
symmetry.  That hypothesis is lost after the matchings are sampled.

## 3. Exact failure of a lower coordinate shift

We now construct (0.3).  It suffices to take no residual coordinates,
so \(m=bd\).  In exactly \(q\) macroblocks give the lower target local
rank \(d-1\), and in the other \(b-q\) blocks give it rank \(d\).  Its
global rank is then \(m-q\).

For one local target \(R\) of rank \(t\in\{d-1,d\}\), its contribution
to the exact maximal lower-degree polynomial is

\[
 P_R(z)=\sum_{a=0}^d
    2^a\binom{e_{t+a}(R)}a z^a,                       \tag{3.1}
\]

where \(e_k(R)\) is the number of matching edges of \(\pi_k\) disjoint
from \(R\).  Perfect matchings at different ranks are independent pieces
of data, so they may be prescribed separately.

Choose the local half sizes as follows:

\[
 (|R\cap A|,|R\cap C|)=
 \begin{cases}
 (d/2,d/2),&t=d,\\
 (d/2,d/2-1),&t=d-1.
 \end{cases}                                           \tag{3.2}
\]

For every relevant rank matching one can arrange

\[
                         e_{t+a}(R)=1.                 \tag{3.3}
\]

For \(t=d\), use one empty edge, one full edge, and \(d-2\) split
edges.  For \(t=d-1\), use one empty edge and \(d-1\) split edges.
The half sizes in (3.2) make both status patterns feasible.  Thus

\[
                         P_R(z)=1+2z.                  \tag{3.4}
\]

Do this in every ordinary block.

In one distinguished block choose \(u,v\in A\) with
\(v\in R\) and \(u\notin R\), and put

\[
                         R'=R-v+u.                    \tag{3.5}
\]

At the rank-\((t+1)\) matching, prescribe

\[
 \pi_{t+1}(u)\in R\cap C,
 \qquad
 \pi_{t+1}(v)\in C\setminus R.                       \tag{3.6}
\]

Complete the matching so that \(R\) has the status pattern (3.3).
After (3.5), the first displayed edge changes from split to full and the
second from split to empty.  Therefore

\[
                         e_{t+1}(R')=2.                \tag{3.7}
\]

At every rank \(t+a\), \(a\ge2\), pair \(u,v\) to two unoccupied
\(C\)-coordinates.  The swap (3.5) then interchanges one empty and one
split edge, leaving the empty count equal to one for both \(R,R'\).
All other edges can be completed with the status patterns above.  Hence

\[
                         P_{R'}(z)=1+4z.               \tag{3.8}
\]

The global target degrees, which equal their singleton-neighborhood
cardinalities, are coefficient products.  Equations (3.4) and (3.8) give

\[
\begin{aligned}
 |N^-(T)|
   &=[z^q](1+2z)^b=2^q\binom bq,\\
 |N^-(C_{uv}T)|
   &=[z^q](1+4z)(1+2z)^{b-1}.
\end{aligned}                                           \tag{3.9}
\]

Subtracting and using Pascal's identity proves

\[
 |N^-(C_{uv}T)|-|N^-(T)|
 =2^q\binom{b-1}{q-1},                                 \tag{3.10}
\]

as claimed.

For the reverse example, prescribe the special rank-\((t+1)\) matching so
that the two local polynomials differ in the opposite direction by exactly
\(2z\).  When \(t=d\), one may start with one empty and one full edge and
let compression turn both into split edges, giving \(1+2z\) versus \(1\).
When \(t=d-1\), start with two empty and one full edge and let compression
remove one of each, giving \(1+4z\) versus \(1+2z\).  At all ranks
\(t+a\), \(a\ge2\), use the unchanged one-empty patterns above.  In both
cases the coefficient difference is
\(-2^q\binom{b-1}{q-1}\).  Thus neither orientation of a fixed coordinate
order is universally neighborhood-decreasing.

The construction applies whenever \(q\le b\).  In particular, with
\(d=\Theta(\log m)\) and \(q=A\sqrt m+O(1)\), one has \(q<b=m/d\) for
all sufficiently large \(m\).

## 4. Upper-shore version

For an upper target \(U\) of local rank \(u\), its local polynomial is

\[
 P_U^+(z)=\sum_{a=0}^d
       2^a\binom{f_{u-a}(U)}a z^a,                    \tag{4.1}
\]

where \(f_k(U)\) counts full matching edges.  Use local ranks \(d+1\)
in exactly \(q\) blocks and rank \(d\) elsewhere, giving global rank
\(m+q\).  Prescribe one full edge at every relevant source rank, except
that the distinguished compressed target has two full edges at the
one-promotion rank.  The same feasible status patterns as in Section 3,
with empty and full interchanged, give

\[
 P_U^+(z)=1+2z,
 \qquad
 P_{C_{uv}U}^+(z)=1+4z.                               \tag{4.2}
\]

The coefficient calculation (3.9)--(3.10) is unchanged.  Reversing the
special matching reverses the sign.  Equivalently, this construction is
obtained from Section 3 by complementation, with the direction of the
coordinate shift reversed.

Thus the shifting failure is genuinely two-sided.

## 5. Quenched arrays have no profile automorphism group

Fix one macroblock and let

\[
                         \pi_0,\ldots,\pi_{2d}
\]

be independent uniform bijections \(A\to C\).  A within-half coordinate
automorphism is a pair \((g,h)\in S(A)\times S(C)\) satisfying

\[
                         h\pi_k=\pi_kg                 \tag{5.1}
\]

for every \(k\).  Once \(g\) and \(\pi_0\) are fixed, (5.1) forces

\[
                         h=\pi_0g\pi_0^{-1}.           \tag{5.2}
\]

For nonidentity \(g\), a fresh uniform \(\pi_k\) satisfies (5.1) with
probability

\[
 {|C_{S_d}(g)|\over d!}
 ={1\over|\operatorname{Cl}(g)|}
 \le {2\over d(d-1)},                                 \tag{5.3}
\]

because the transposition class is a smallest nontrivial conjugacy class
of \(S_d\) for \(d\ge5\).  Union bounding over at most \(d!\) choices of
\(g\) and the remaining \(2d\) independent matchings gives

\[
 \Pr\{\text{a nontrivial common automorphism exists}\}
 \le d!\left({2\over d(d-1)}\right)^{2d}=o(1).         \tag{5.4}
\]

Therefore the full quenched rank array almost surely has no nontrivial
within-half automorphism.  The stabilizer of one matching, which supports
its zero/single/full status compression, is destroyed by the independent
matchings at the other ranks.

## 6. Exact conclusion boundary

The following are proved.

1. An annealed minimum Hall cut may be taken to be an ordered half-profile
   union.
2. Ordinary coordinate shifts are not neighborhood-monotone in the raw
   rank-twisted graph, at every scale \(q\le m/d\), on either sign.
3. Matching-status threshold symmetries do not survive a quenched
   independent rank array.

The following are not proved.

1. Failure of QRE\(_A\).
2. Existence of a nonprofile minimum cut with high probability.
3. A quenched compression obtained by a new nonlocal operation rather than
   ordinary shifts or automorphisms.

Thus compression closes the annealed/profile quotient exactly but does
not lift it to raw QRE.  The remaining route must prove a quenched
cut-norm, normalized-matching, or product-permutation isoperimetric theorem
directly.
