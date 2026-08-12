# Packing-side repaired promotion rings: exact codegrees and the nibble boundary

Date: 2026-07-26

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q}.
\]

Let \(H\) be the least positive integer for which

\[
 \lambda_H\ge M:=m+H,
\tag{0.1}
\]

and put \(s=m-H\), \(R=N_H\).  Then

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 (M-1)R=W-o(W).
\tag{0.2}
\]

The repaired-ring hypergraph \(\mathcal G\) has

* one tag vertex for every rank-\(M\) top \(U\);
* one owner vertex for every \(X\in\binom{[2m]}m\);
* one formal edge for every oriented cyclic frame on \(U\), modulo
  rotation, and every marked omitted phase.  The edge contains the tag
  \(U\) and the other \(M-1\) cyclic \(m\)-windows.

Thus \(\mathcal G\) is \(M\)-uniform and has \(W+R\) vertices.  A matching
of \(R\) edges is exactly one repaired ring per top with all retained
middle owners distinct; it leaves only

\[
 W-(M-1)R=o(W)
\]

owners uncovered.

This note proves:

1. The two degrees are

   \[
   \boxed{
   D_T=M!,\qquad
   D_O=(M-1){(m!)^2\over s!},\qquad
   {D_O\over D_T}={M-1\over\lambda_H}.}
   \tag{0.3}
   \]

   Moreover

   \[
   1-{2H-1\over M}< {D_O\over D_T}
   \le1-{1\over M}.
   \tag{0.4}
   \]

2. All pair codegrees are exact.  Two tags have codegree zero.  An
   incident tag--owner pair has codegree

   \[
   (M-1)m!H!.
   \tag{0.5}
   \]

   If two owners have Johnson distance \(d\), their codegree is

   \[
   \boxed{
   C_d=
   \begin{cases}
   \displaystyle
   {2(M-2)(d!)^2(m-d)!^2\over s!},&1\le d<H,\\[2mm]
   (M-2)(H!)^2(s+1)!,&d=H,\\
   0,&d>H.
   \end{cases}}
   \tag{0.6}
   \]

   Hence, for large \(m\),

   \[
   \boxed{\Delta_2=C_1,\qquad
   {\Delta_2\over D_T}={2(M-2)\over m^2\lambda_H}
   ={2+o(1)\over m^2}.}
   \tag{0.7}
   \]

3. There is an exact formula for every higher codegree in terms of
   simultaneous cyclic-frame realizations; see Theorem 3.1.  In
   particular, for all sufficiently large \(m\),

   \[
   2\le C_j(\mathcal G)\le\Delta_2\quad(2\le j\le M),
   \qquad
   \boxed{C_M(\mathcal G)=2.}
   \tag{0.8}
   \]

   The terminal value two is the two orientations of the same geometric
   repaired ring.

4. No audited published growing-uniformity nibble or tag-perfect theorem
   applies.

   * Pippenger--Spencer and the modern conflict-free/tag-perfect
     theorems fix the uniformity before taking the degree limit.
   * The explicit Grable--Kostochka--Rödl variable-rank condition fails
     at the sharp constant

     \[
     \boxed{
     {M\Delta_2\log(W+R)\over D_T}
     =4\log2+o(1),}
     \tag{0.9}
     \]

     instead of tending to zero.
   * In the 2025 Gould--Kelly full-codegree theorem, even the best
     possible bottleneck parameter obeys

     \[
     B\le(D_T/C_M)^{1/(M-1)}
       =(1+o(1)){M\over e}.
     \tag{0.10}
     \]

     Its published hierarchy fixes \(M\), and even ignoring that issue
     its error is already bounded below by
     \[
       B^{-1+\gamma}\log^A D_T
       \ge {\log D_T\over B}
       =(e+o(1))\log M,
     \]
     so formal substitution \(M\to\infty\) is vacuous.
   * The Gould--Kelly \(X\)-perfect theorem also needs a degree surplus
     of that polylogarithmic size; the actual tag surplus is only
     \(O(H/m)=o(1)\).

5. An elementary maximal-matching argument gives the unconditional bound

   \[
   \boxed{
   \nu(\mathcal G)\ge
   {R D_T\over D_T+(M-1)(D_O-1)}
   \ge {R\over M-1+1/M}
   =(1+o(1)){R\over M}.}
   \tag{0.11}
   \]

   It selects only a \(1/M\) fraction of the tags and covers only a
   \(1/m+o(1/m)\) fraction of the middle layer.  The exact quantitative
   bottleneck is therefore a factor \(M\): coefficient one needs
   \((1-o(1))R\) repaired rings, while all unconditional degree/codegree
   machinery audited here guarantees only \(\Theta(R/M)\).

No owner factor is proved.  The positive contribution is the complete
local ledger and an exact identification of why the catalogue lies on,
not inside, the known growing-uniformity nibble boundary.

## 1. Packing-side calibration

The ratio recurrence is

\[
 {\lambda_q\over\lambda_{q-1}}
 ={m+q\over m-q+1}.
\tag{1.1}
\]

Minimality in (0.1) gives

\[
 \lambda_{H-1}<M-1,
\]

and therefore

\[
 1\le{\lambda_H\over M}
 ={\lambda_{H-1}\over m-H+1}
 <{M-1\over m-H+1}
 =1+O(H/m).
\tag{1.2}
\]

The usual expansion

\[
 \log\lambda_q={q^2\over m}
 +O\left({q^2\over m^2}+{q^4\over m^3}\right)
\]

locates \(H\) at \((1+o(1))\sqrt{m\log m}\).  Also

\[
 {(M-1)R\over W}={M-1\over\lambda_H}
 =1-O(H/m),
\tag{1.3}
\]

which proves (0.2).  More precisely, (1.2) and \(\lambda_H\ge M\)
give

\[
 {m-H+1\over M}
 <{M-1\over\lambda_H}
 \le {M-1\over M},
\]

which is (0.4).

## 2. Exact degrees and pair codegrees

We retain oriented cyclic frames as formal columns.  Reversal produces
two copies of each geometric repaired edge.  This is harmless:
the matching theorems considered below allow multihypergraphs, and all
degree ratios are unchanged if one quotients by reversal.

### Proposition 2.1 (degrees)

Equation (0.3) holds.

#### Proof

A top has \((M-1)!\) oriented cyclic frames and \(M\) choices of omitted
phase, giving \(D_T=M!\).

Fix a middle owner \(X\).  There are \(\binom mH\) tops containing it.
Within a fixed containing top, exactly \(m!H!\) oriented cyclic frames
make \(X\) an \(m\)-window.  The omitted phase may be any of the other
\(M-1\) windows.  Thus

\[
 D_O=(M-1)\binom mH m!H!
 =(M-1){(m!)^2\over s!}.
\]

Finally

\[
 {(m!)^2/s!\over M!}={1\over\lambda_H},
\]

proving the ratio in (0.3). \(\square\)

### Proposition 2.2 (tag-pair and tag--owner codegrees)

Two distinct tags have codegree zero.  If \(X\subset U\), then

\[
 \deg(U,X)=(M-1)m!H!,
\tag{2.1}
\]

and otherwise it is zero.

#### Proof

An edge contains one tag.  For \(X\subset U\), there are \(m!H!\)
frames containing \(X\), and \(M-1\) admissible omitted phases.
\(\square\)

### Theorem 2.3 (complete owner-pair profile)

Equation (0.6) holds.

#### Proof

First ignore the omitted phase.  If \(1\le d<H\), a common top contains
\(X\cup Y\), and its remaining \(H-d\) elements may be chosen in
\(\binom{m-d}{H-d}\) ways.  Inside that top, the four Venn cells of the
two \(m\)-windows must be four consecutive blocks.  The oriented frame
count is

\[
 2(d!)^2(H-d)!(m-d)!.
\]

Multiplication and cancellation give

\[
 {2(d!)^2(m-d)!^2\over s!}
\]

full frames.  If \(d=H\), the top is forced and the full-frame count is
\((H!)^2(s+1)!\).  If \(d>H\), the union is larger than a top.

For a repaired edge containing both owners, the omitted phase may be any
of the other \(M-2\) phases.  Multiplication by \(M-2\) proves (0.6).
\(\square\)

### Corollary 2.4 (maximum pair codegree)

For all sufficiently large \(m\), the distance-one owner pair is the
maximum pair codegree and (0.7) holds.

#### Proof

Among owner pairs, the normalized sequence from Theorem 2.3 is maximized
at \(d=1\); the \(d=H\) endpoint is exponentially smaller.  Also

\[
 {\deg(U,X)\over C_1}
 ={M-1\over2(M-2)}
   {m^2\over\binom mH}
 =\exp[-\Theta(H\log(m/H))].
\tag{2.2}
\]

Thus tag--owner pairs are smaller.  Finally

\[
 {C_1\over D_T}
 ={2(M-2)\over m^2}
   {(m!)^2/s!\over M!}
 ={2(M-2)\over m^2\lambda_H}.
\]

Use \(M/\lambda_H=1+O(H/m)\). \(\square\)

## 3. Every higher codegree and the terminal value

The following formula is exact for every vertex set and is useful when a
theorem asks for the entire codegree sequence rather than only
\(\Delta_2\).

For a family \(\mathcal Q\) of owner vertices and a top \(U\), define

\[
 \Phi_U(\mathcal Q)=
 |\{\pi:\pi\text{ is an oriented cyclic frame on }U,\ 
          \mathcal Q\subseteq I_m(\pi)\}|.
\tag{3.1}
\]

It is zero unless every owner in \(\mathcal Q\) is contained in \(U\).

### Theorem 3.1 (full structural codegree formula)

Let \(Q\) be a set of \(j\) vertices of \(\mathcal G\), containing
\(t\) owner vertices.

* If \(Q\) contains at least two tags, then \(\deg(Q)=0\).
* If \(Q\) contains the single tag \(U\), then

  \[
  \boxed{\deg(Q)=(M-t)\Phi_U(Q\cap\mathcal X).}
  \tag{3.2}
  \]

* If \(Q\) contains no tag, then

  \[
  \boxed{
  \deg(Q)=(M-t)
  \sum_{\substack{U\in\binom{[2m]}M\\
                  U\supseteq\bigcup(Q\cap\mathcal X)}}
       \Phi_U(Q\cap\mathcal X).}
  \tag{3.3}
  \]

These formulas, together with (3.1), give the exact \(j\)-codegree of
every \(j\)-set for all \(1\le j\le M\).

#### Proof

After fixing a frame containing the \(t\) prescribed owner windows, the
omitted phase can be any of the remaining \(M-t\) phases.  If a tag is
present its top is fixed; without a tag, sum over all compatible tops.
\(\square\)

### Proposition 3.2 (terminal reconstruction)

For all sufficiently large \(m\) and \(2\le j\le M\),

\[
 2\le C_j(\mathcal G)\le C_2(\mathcal G),
\]

and \(C_M(\mathcal G)=2\).

#### Proof

The upper bound follows because every \(j\)-set contains a pair.  Every
geometric repaired edge has its two oriented representations, giving the
lower bound.

For the terminal assertion, fix the tag and all \(M-1\) retained owner
windows.  Complementing the owners inside the top gives \(M-1\) cyclic
\(H\)-windows.  Since \(2H<M\), two such windows meet in \(H-1\) elements
exactly when their starts differ by one.  Their intersection-\((H-1)\)
graph is therefore a path.  Traversing the path recovers each successive
leaving and entering symbol.  These differences recover the entire
cyclic frame and the unique missing window, up to reversing the path.
Hence exactly the two orientations represent the terminal vertex set.
\(\square\)

Remark: (3.2)--(3.3) are an exact full sequence, but maximizing
\(\Phi_U\) in closed factorial form for every intermediate \(j\) is a
separate circular-arc extremal problem.  It is unnecessary for the
black-box audit: the exact pair value and exact terminal value already
force the two decisive bottlenecks below.

### 3.3 Complete small-case verification

As an independent check, a complete enumeration at \(m=4\) gives
\(H=3,M=7,s=1\) and \(40320\) formal edges.  Every geometric edge has
formal multiplicity two, and the enumerated ledgers are

\[
 D_T=5040,\qquad D_O=3456,\qquad D_{T,O}=864,
\]

\[
 C_1=360,\qquad C_2=160,\qquad C_3=360,\qquad C_7=2.
\]

These are exactly the values from (0.3), (0.5), (0.6), and Proposition
3.2.  The tie \(C_1=C_H\) at this small value also explains why the
qualification “for sufficiently large \(m\)” is needed in Corollary
2.4.

## 4. Published theorem audit

### 4.1 Classical Pippenger--Spencer

Pippenger and Spencer state their theorem for hypergraphs of fixed
uniformity \(k\), with asymptotically equal degrees and negligible
codegrees.  Here \(k=M\to\infty\), so the theorem does not diagonalize.
This is explicit in the authors' published abstract: “every edge contains
exactly \(k\) vertices, for some fixed \(k\).”

Primary source:
[Pippenger--Spencer, *Asymptotic Behavior of the Chromatic Index for
Hypergraphs*](https://doi.org/10.1016/0097-3165(89)90074-5).

### 4.2 Grable--Kostochka--Rödl quantitative condition

The quantitative variable-rank extension requires

\[
 {kC\log |V|\over D}=o(1).
\tag{4.1}
\]

For \(\mathcal G\), take \(k=M\), \(C=\Delta_2\), \(D=D_T\), and
\(|V|=W+R\).  Since

\[
 \log(W+R)=(2\log2+o(1))m,
\]

Corollary 2.4 gives

\[
 {M\Delta_2\log(W+R)\over D_T}
 =(1+o(1))m\,{2\over m^2}\,(2m\log2)
 =4\log2+o(1).
\]

Thus the hypothesis fails by a fixed constant, not by an untracked
little-\(o\).

Primary source for the stated quantitative condition:
[Kostochka--Rödl, *Partial Steiner systems and matchings in
hypergraphs*](https://doi.org/10.1002/(SICI)1098-2418(199810/12)13:3/4%3C335::AID-RSA8%3E3.0.CO;2-W).

### 4.3 Kang--Kühn--Methuku--Osthus

Their nearly-perfect matching theorem again places \(1/k\) above the
asymptotic degree parameter in its hierarchy.  Formally substituting
\(k=M\) into its principal leftover scale does not help:

\[
 \left({D_T\over\Delta_2}\right)^{-1/M+o(1/M)}
 =\exp\left[-{2\log m+O(1)\over m}\right]
 =1-o(1).
\]

It would leave almost all vertices rather than \(o(W)\).

Primary source:
[Kang--Kühn--Methuku--Osthus, *New bounds on the size of Nearly Perfect
Matchings in almost regular hypergraphs*](https://arxiv.org/abs/2010.04183).

### 4.4 Gould--Kelly full-codegree and tag-perfect theorems

Gould--Kelly Theorem 1.4 assumes

\[
 1/D\ll1/A\ll\gamma\ll1/k,
\]

so \(k\) is fixed.  Even under formal substitution, its bottleneck
parameter satisfies, by Proposition 3.2,

\[
 B\le(D_T/2)^{1/(M-1)}
 =(1+o(1)){M\over e}.
\]

The conclusion leaves a fraction
\(B^{-1+\gamma}\log^A D_T\).  Since \(A\ge1,\gamma>0\) and

\[
 \log D_T=(1+o(1))M\log M,
\]

the terminal bound on \(B\) gives

\[
 B^{-1+\gamma}\log^A D_T
 \ge {\log D_T\over B}
 =(e+o(1))\log M.
\]

Thus the bound is vacuous even before imposing the theorem's fixed-rank
parameter hierarchy.

Their Theorem 1.6 seeks an \(X\)-perfect matching, exactly the desired
tag-perfect form, but requires tag degree at least

\[
 (1+B^{-1+\gamma}\log^A D_T)D
\]

over the non-tag degree bound \(D\).  Our actual relative tag surplus is

\[
 {D_T\over D_O}-1
 ={\lambda_H\over M-1}-1
 =O(H/m)=o(1),
\]

so this hypothesis also fails, even before the fixed-\(k\) issue.

Primary source:
[Gould--Kelly, *Advancing the Rödl Nibble*,
Theorems 1.4 and 1.6](https://arxiv.org/abs/2511.11375).

### 4.5 Conflict-free and \(P\)-perfect theorems

The available \(P\)-perfect theorem fixes the edge parameters
\(p,q,r,\ell\) before the degree threshold and requires relative
regularity \(d^{-\varepsilon}\) for a fixed \(\varepsilon>0\).  Here
\(q=M-1\to\infty\), and our relative degree discrepancy is at least
\(1/M\), whereas

\[
 D_T^{-\varepsilon}=\exp[-\Theta_\varepsilon(m\log m)].
\]

Thus its hypotheses fail in two independent ways.

Primary source:
[*Conflict-free hypergraph matchings and coverings*, Theorem
1.1](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/conflictfree-hypergraph-matchings-and-coverings/40E8318628BA6C937FD4AA46CC8A7595).

## 5. Strongest unconditional elementary matching bound

### Theorem 5.1 (greedy repaired-ring bite)

Equation (0.11) holds.

#### Proof

The formal edge count is

\[
 |E(\mathcal G)|=R D_T.
\]

Fix an edge.  Other edges meeting it through its tag number at most
\(D_T-1\).  For each of its \(M-1\) owner vertices, at most \(D_O-1\)
other edges meet it there.  Therefore its closed neighbourhood in the
line graph has size at most

\[
 D_T+(M-1)(D_O-1).
\tag{5.1}
\]

A greedy independent set in the line graph, equivalently a greedy
hypergraph matching, has size at least the number of line-graph vertices
divided by the maximum closed-neighbourhood size.  This gives the first
inequality in (0.11).

Using \(D_O/D_T=(M-1)/\lambda_H\) and \(\lambda_H\ge M\),

\[
\begin{aligned}
 1+(M-1){D_O-1\over D_T}
 &\le1+{(M-1)^2\over\lambda_H}\\
 &\le1+{(M-1)^2\over M}
 =M-1+{1\over M}.
\end{aligned}
\]

This proves the second inequality. \(\square\)

The matching in Theorem 5.1 covers \(\Theta(R)\) middle owners, while an
owner factor must cover \(W-o(W)=\Theta(MR)\).  Closing the factor-\(M\)
gap requires a genuinely regenerative, group-respecting nibble or an
absorber; it is not supplied by any theorem whose hypotheses have been
verified above.
