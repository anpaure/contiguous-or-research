# GMM tight two-level enumeration: exact Johnson projection, cheap direct-step quarantine, and the depth-two obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Let

\[
 p=2m+1,\qquad
 W=\binom pm,\qquad
 N=\binom p{m-1}={m\over m+2}W,\qquad
 D=W-N={2W\over m+2}.                              \tag{0.1}
\]

Gregor--Mička--Mütze Corollary 2 supplies a tight enumeration of levels
\(\{m-1,m\}\).  Its exact projection is a Hamilton cycle on all \(W\)
vertices of \(J(p,m)\) with:

1. exactly \(N\) lower-mediated Johnson edges;
2. exactly \(D\) direct middle--middle Johnson edges;
3. every rank-\((m-1)\) set occurring exactly once as the intersection
   label of a mediated edge; and
4. the \(D\) direct edges contributing \(D\) additional, uncontrolled
   lower-intersection occurrences.

The direct edges themselves are asymptotically harmless.  Delete them
from the Hamilton cycle and compile the resulting owner paths with the
standard radius-\(H\) reset interface.  The total direct-step reset toll
is

\[
 \boxed{
                         O(HD)
                         =O\left({H\over m}W\right)
                         =o(W)\qquad(H=o(m)).}       \tag{0.2}
\]

Thus the \(W-N\) direct transitions can be quarantined without assuming
that the Hamilton cycle is a wreath factor.

What remains after that quarantine is not automatically \(H\)-safe.
Every mediated owner path has an exact lower-path normal form

\[
 R_{i+1}=R_i-d_i+a_i,\qquad
 X_i=R_i\cup R_{i+1},                               \tag{0.3}
\]

and its owner exchange is

\[
                         X_{i+1}=X_i-d_i+a_{i+1}.    \tag{0.4}
\]

For two consecutive owner exchanges, all four labels

\[
                         d_i,\ a_{i+1},\ d_{i+1},\ a_{i+2}
\]

are forced distinct except possibly

\[
                         \boxed{d_i=a_{i+2}.}        \tag{0.5}
\]

This delayed return is the exact first obstruction.  The lower
depth-two trace still has rank \(m-2\), but the upper trace has rank only
\(m+1\), rather than \(m+2\):

\[
\begin{aligned}
 |X_i\cap X_{i+1}\cap X_{i+2}|&=m-2,\\
 |X_i\cup X_{i+1}\cup X_{i+2}|
 &=
 \begin{cases}
  m+2,&d_i\ne a_{i+2},\\
  m+1,&d_i=a_{i+2}.
 \end{cases}                                      \tag{0.6}
\end{aligned}
\]

Let \(B_2\) be the number of delayed returns away from the direct-edge
collars.  Every segmentation into two-safe inherited owner paths must cut
at least \(B_2/2\) additional owner edges.  Hence the standard reset
compiler has the lower toll

\[
                         \Omega(HB_2).               \tag{0.7}
\]

Corollary 2 gives no bound on \(B_2\).  The local pattern is compatible
with distinct lower vertices, distinct owners, and exact mediated
adjacency, so it cannot be excluded from tightness or simplicity alone.

There is a second independent depth-two gap.  The mediated edge labels
form a spanning path forest \(\mathcal F_R\) on all \(N\) rank-\((m-1)\)
sets, with at most \(D\) components.  Its edge colours

\[
                         RR'\longmapsto R\cap R'
\]

are exactly the inherited lower depth-two targets.  The forest has enough
raw edges:

\[
 |E(\mathcal F_R)|
 \ge N-D
 =\binom p{m-2}
   +{(2m-6)W\over(m+2)(m+3)}.                      \tag{0.8}
\]

But GMM tightness gives no injectivity or near-surjectivity of these
rank-\((m-2)\) colours.  Thus even after all direct steps are paid for,
depth-two literal coverage is a new saturating/path-colour problem one
rank lower.

The exact conclusion is:

> The \(W-N\) direct middle steps admit an \(o(W)\) quarantine for every
> \(H=o(m)\).  The GMM theorem does not yield an \(H\)-safe owner word,
> because the mediated core has two uncontrolled \(q=2\) invariants:
> delayed returns (0.5) and collisions of the path-forest colours in
> (0.8).

## 1. Tight enumeration contracts to an exact Hamilton Johnson cycle

Let a cyclic tight enumeration of the two levels contain:

* \(a\) cross-rank adjacent pairs;
* \(b\) lower--lower adjacent pairs; and
* \(c\) middle--middle adjacent pairs.

Counting the two incidences at every listed vertex gives

\[
                         2N=a+2b,\qquad
                         2W=a+2c.                  \tag{1.1}
\]

Every cross-rank pair has Hamming distance at least one, and every
distinct equal-rank pair has Hamming distance at least two.  Hence the
total Hamming length is at least

\[
                         a+2b+2c=2W+2b.             \tag{1.2}
\]

The defining tight length is

\[
                         (W+N)+(W-N)=2W.            \tag{1.3}
\]

Equality in (1.2)--(1.3) forces

\[
                         b=0,\qquad a=2N,\qquad c=D,             \tag{1.4}
\]

and forces equality in every local distance bound.

### Theorem 1.1 (exact projected structure)

Delete every lower vertex from the tight cyclic enumeration.  The
remaining cyclic order

\[
                         X_0,X_1,\ldots,X_{W-1},X_0             \tag{1.5}
\]

is a Hamilton cycle of \(J(p,m)\).  Exactly \(N\) of its edges arise from
a unique intervening lower vertex, and exactly \(D\) arise from a direct
middle--middle pair.  The \(N\) mediated intersection labels are all
rank-\((m-1)\) sets, exactly once.

#### Proof

Because \(b=0\), every lower vertex is flanked by two middle vertices.
Equality in the cross-rank distance bound says it is incident with both.
Contracting it therefore creates the Johnson edge between two distinct
facets containing it.

Equality at every direct middle--middle pair says its Hamming distance is
two, so it too is a Johnson edge.  All \(W\) middle vertices occur once,
giving a Hamilton cycle.  Every lower vertex occurs once and labels its
contracted edge by the intersection of the two flanking owners.
Equation (1.4) gives the counts. \(\square\)

### Corollary 1.2 (exact depth-one lower ledger)

Every lower rank-\((m-1)\) target has load at least one.  The total excess
above load one is exactly \(D\), contributed by the direct edges:

\[
 \sum_R\bigl(L_1(R)-1\bigr)=D.                     \tag{1.6}
\]

No floor/ceiling distribution of this excess, and no upper-union
statement, follows from tightness.

## 2. The direct-step quarantine theorem

Mark the \(D\) direct edges in (1.5) and delete them.  A cycle with \(D\)
deleted edges becomes at most \(D\) vertex-disjoint owner paths (exactly
\(D\) components when isolated vertices are retained in the usual way).
All \(W\) owners remain present.

### Theorem 2.1 (direct steps cost only \(o(W)\))

Assume every resulting mediated path is \(H\)-safe.  Then the Hamilton
owner set compiles as a literal path word with total length

\[
                         W+O(HD).                   \tag{2.1}
\]

In particular, for every \(H=o(m)\), this is \(W+o(W)\).

#### Proof

Use one ordinary radius-\(H\) reset at every path boundary.  Its length
is \(O(H)\), and there are at most \(D\) paths.  Equation (0.1) gives

\[
 {HD\over W}={2H\over m+2}=o(1).
\]

No property of a wreath factor is used: only the Hamilton owner order and
the standard path-reset interface are invoked. \(\square\)

Equivalently, one may quarantine the \(H\)-neighbourhood of every direct
edge.  Its total owner mass is at most \(O(HD)=o(W)\).  Every surviving
window then lies wholly in one lower-mediated path.

The hypothesis in Theorem 2.1 is the real issue.  Neither the uniqueness
of the lower labels nor Hamiltonicity makes those paths \(H\)-safe.

## 3. Exact lower-path normal form

Consider one run of consecutive mediated owner edges.  List their lower
intersection labels in order as

\[
                         R_0,R_1,\ldots,R_\ell,
\]

so the intervening middle owners are

\[
                         X_i=R_i\cup R_{i+1}
                         \qquad(0\le i<\ell).        \tag{3.1}
\]

The \(R_i\)'s are distinct rank-\((m-1)\) sets.  Consecutive labels are
distinct facets of \(X_i\), hence adjacent in \(J(p,m-1)\).  There are
unique labels \(d_i\in R_i\) and \(a_i\notin R_i\) such that

\[
                         R_{i+1}=R_i-d_i+a_i.        \tag{3.2}
\]

Since

\[
                         X_i=R_{i+1}+d_i
                         =R_i+a_i,                  \tag{3.3}
\]

the next owner is

\[
                         X_{i+1}=R_{i+1}+a_{i+1}.
\]

This proves the owner exchange identity

\[
                         X_{i+1}=X_i-d_i+a_{i+1}.    \tag{3.4}
\]

Thus GMM tightness fixes the owner word only through the shifted lower
exchange labels \((d_i,a_{i+1})\).  It imposes no FIFO or residence rule
on them.

## 4. The exact depth-two delayed-return obstruction

### Theorem 4.1 (complete equality classification for two exchanges)

For two consecutive owner exchanges in a mediated path, the labels

\[
                         d_i,\ a_{i+1},\ d_{i+1},\ a_{i+2}
                                                               \tag{4.1}
\]

are pairwise distinct except possibly for \(d_i=a_{i+2}\).

#### Proof

The membership relations give

\[
\begin{array}{c|cc}
 &\text{inside}&\text{outside}\\ \hline
 R_{i+1}&d_{i+1}&d_i,\ a_{i+1}\\
 R_{i+2}&a_{i+1}&d_{i+1},\ a_{i+2}.
\end{array}
\]

Thus \(d_i\ne d_{i+1}\), \(a_{i+1}\ne d_{i+1}\), and
\(a_{i+1}\ne a_{i+2}\).  If \(d_i=a_{i+1}\), then (3.3) gives
\(X_i=X_{i+1}\), contrary to Hamiltonicity.  If
\(d_{i+1}=a_{i+2}\), the same argument gives
\(X_{i+1}=X_{i+2}\).  The only unexcluded equality is
\(d_i=a_{i+2}\). \(\square\)

### Theorem 4.2 (exact depth-two ranks)

For every such triple of owners,

\[
 X_i\cap X_{i+1}\cap X_{i+2}
                         =R_{i+1}\setminus\{d_{i+1}\},          \tag{4.2}
\]

while

\[
 X_i\cup X_{i+1}\cup X_{i+2}
 =R_{i+1}\cup\{d_i,a_{i+1},a_{i+2}\}.              \tag{4.3}
\]

Consequently (0.6) holds.

#### Proof

Use

\[
\begin{aligned}
 X_i&=R_{i+1}+d_i,\\
 X_{i+1}&=R_{i+1}+a_{i+1},\\
 X_{i+2}
   &=(R_{i+1}-d_{i+1}+a_{i+1})+a_{i+2}.
\end{aligned}
\]

The intersection is (4.2).  The equality classification in Theorem 4.1
shows that the three displayed exterior labels in (4.3) are distinct
except precisely when \(d_i=a_{i+2}\).  Since
\(|R_{i+1}|=m-1\), the rank statement follows. \(\square\)

Thus the lower depth-two rank is automatically correct on every
mediated triple, but the upper rank is correct exactly when the delayed
return is absent.  Full two-sided \(2\)-safety is therefore equivalent to
excluding (0.5).

### A literal compatible bad block

Let \(S\) be any set of size \(m-3\), disjoint from
\(\{1,2,3,4\}\), and put

\[
\begin{aligned}
 R_0&=S\cup\{1,2\},&
 R_1&=S\cup\{2,3\},\\
 R_2&=S\cup\{3,4\},&
 R_3&=S\cup\{4,1\}.
\end{aligned}                                      \tag{4.4}
\]

Then

\[
\begin{aligned}
 X_0&=S\cup\{1,2,3\},\\
 X_1&=S\cup\{2,3,4\},\\
 X_2&=S\cup\{1,3,4\}
\end{aligned}
\]

are distinct owners, all four displayed lower vertices are distinct, and
the two owner exchanges are

\[
                         1\to4,\qquad2\to1.          \tag{4.5}
\]

The repeated label \(1\) gives

\[
                         |X_0\cup X_1\cup X_2|=m+1.
\]

Hence the local axioms certified by tightness do not prohibit the first
depth-two defect.

## 5. Quantitative path-cut obstruction

Let \(B_2\) count indices satisfying \(d_i=a_{i+2}\) inside the mediated
paths after the direct-edge quarantine.

### Proposition 5.1 (delayed-return cut bound)

Any owner-edge deletion which partitions the mediated core into
two-safe inherited paths deletes at least \(B_2/2\) edges.

#### Proof

Each bad depth-two window contains two consecutive owner edges.  At least
one must be deleted, or the same unsafe triple survives in one component.
One owner edge lies in at most two consecutive two-edge windows.  Double
counting incidences between bad windows and deleted edges proves the
bound. \(\square\)

Under the ordinary radius-\(H\) reset interface, every added path
component costs \(O(H)\).  Therefore (0.7) follows.  In particular, this
interface can have \(o(W)\) total reset toll only if

\[
                         B_2=o(W/H).                 \tag{5.1}
\]

This is a necessary condition for the reset construction, not a universal
no-go against a new seam decoder which repairs delayed returns without
opening a radius-\(H\) boundary.

For the full protected window, let \(\tau_H\) be the minimum number of
owner edges meeting every mediated interval whose exchange-label word has
a repeated coordinate among at most \(H\) consecutive exchanges.  Then
the exact standard-interface gate is

\[
 \boxed{
 \text{compiled length }
 =W+O\bigl(H(D+\tau_H)\bigr),\qquad
 \tau_H=o(W/H).}                                   \tag{5.2}
\]

The direct contribution \(HD\) is already \(o(W)\); only \(\tau_H\)
remains.

## 6. The independent lower depth-two colour problem

Let the \(N\) mediated edge labels be vertices of a graph
\(\mathcal F_R\).  Join two labels when their mediated owner edges are
consecutive in the Hamilton cycle.  Deleting the \(D\) direct owner edges
turns the mediated labels into cyclic runs, so \(\mathcal F_R\) is a
spanning path forest on all rank-\((m-1)\) sets.  It has at most \(D\)
components and therefore

\[
                         |E(\mathcal F_R)|\ge N-D.   \tag{6.1}
\]

For an edge \(RR'\) of this forest, the corresponding three-owner lower
trace is exactly

\[
                         R\cap R'.                  \tag{6.2}
\]

Thus the inherited lower depth-two image is the edge-colour image

\[
 \mathcal L_2^{\rm med}
 =\{R\cap R':RR'\in E(\mathcal F_R)\}.              \tag{6.3}
\]

Put

\[
                         N_2=\binom p{m-2}
                         ={m-1\over m+3}N.           \tag{6.4}
\]

Using (0.1),

\[
\begin{aligned}
 N-D-N_2
 &= {4N\over m+3}-{2W\over m+2}\\
 &= {2m-6\over(m+2)(m+3)}W.                        \tag{6.5}
\end{aligned}
\]

This proves (0.8) for \(m\ge3\).

The positive surplus in (6.5) is only an occurrence count.  The exact
lower depth-two core hole count is

\[
                         N_2-|\mathcal L_2^{\rm med}|,          \tag{6.6}
\]

up to the \(O(D)\) windows meeting a quarantined direct edge.  Corollary 2
contains no assertion that the colours (6.2) are injective, dispersed, or
near-surjective.  This is already a \(q=2\) shadow gate even when
\(B_2=0\).

## 7. General protected depth

On one mediated path, the exact owner exchange word is

\[
                         (d_i\to a_{i+1})_i.         \tag{7.1}
\]

A length-\(q\) inherited window is two-sided safe precisely when its
\(2q\) displayed labels are pairwise distinct.  In that case

\[
\begin{aligned}
 \bigcap_{j=0}^{q}X_{i+j}
   &=X_i\setminus\{d_i,\ldots,d_{i+q-1}\},\\
 \bigcup_{j=0}^{q}X_{i+j}
   &=X_i\cup\{a_{i+1},\ldots,a_{i+q}\}.             \tag{7.2}
\end{aligned}
\]

For \(q\ge2\), neither pairwise label separation nor the image
cardinalities in (7.2) are consequences of:

* Hamiltonicity of the projected owner cycle;
* uniqueness of the \(N\) mediated lower labels;
* the exact count \(D=W-N\) of direct steps; or
* tightness of the original two-level enumeration.

Thus no all-depth conclusion may be transferred from GMM Corollary 2
without a new chronology theorem.

## 8. Certified boundary

Proved:

1. the exact Hamilton Johnson projection and the \(N/D\) edge split;
2. exact lower depth-one coverage with surplus \(D\);
3. an \(O(HD)=o(W)\) quarantine of all direct middle steps;
4. the mediated lower-path normal form (0.3)--(0.4);
5. the complete depth-two delayed-return classification;
6. the path-cut lower bound \(B_2/2\);
7. the spanning lower path-forest reduction; and
8. the exact depth-two occurrence surplus (0.8).

Not proved:

1. \(B_2=o(W/H)\) for a GMM tight enumeration;
2. \(\tau_H=o(W/H)\);
3. near-surjectivity of the lower path colours (6.3);
4. near-surjectivity of the upper depth-two targets;
5. an \(H\)-safe Hamilton owner word; or
6. coefficient one.

The direct \(W-N\) edges are therefore not the obstruction.  The exact
remaining difficulty begins inside the lower-mediated core at \(q=2\).
