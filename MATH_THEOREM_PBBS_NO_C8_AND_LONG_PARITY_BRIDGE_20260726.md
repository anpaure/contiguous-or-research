# The natural PBBS factor has no \(C_8\), but has an explicit linear-size parity bridge

Date: 2026-07-26

Method: pure mathematics only.

## 0. Statement and relevance

Put

\[
 n=2r+1,\qquad {\cal X}=\binom{[n]}r,\qquad
 B_r=\operatorname {Cat}_r={1\over n}\binom nr,\qquad r\ge2.
\]

Let \(f:{\cal X}\to{\cal X}\) be the cyclic-parenthesis, or PBBS,
permutation. If \(U_Z=[n]\setminus Z\), consider the natural pair of
perfect matchings in the Middle Levels graph

\[
 M_0(U_Z)=f^{-1}(Z),\qquad M_1(U_Z)=f(Z).                 \tag{0.1}
\]

### Theorem A (exact \(C_8\) obstruction)

There is no \(M_1\)-alternating \(C_8\) in the Middle Levels graph.
Equivalently, the natural PBBS exchange digraph has no directed
\(4\)-cycle. This remains true before imposing the additional requirement
that a new \(M_1\)-edge avoid \(M_0\).

Consequently the physically disjoint “PBBS \(C_6\)-forest plus one
initial \(C_8\)” atlas cannot exist. Any \(C_8\) used after PBBS
hexagon switches must have been created by the earlier switches and must
meet their physical vertex support (it need not share an edge).

### Theorem B (explicit parity bridge)

The same exchange digraph contains an explicit directed cycle of length

\[
                         2n=4r+2.                           \tag{0.2}
\]

Thus the Middle Levels factor has an \(M_1\)-alternating circuit of length
\(4n=8r+4\). Switching on it changes exactly \(2n=O(r)\) matching slots,
preserves the perfect upper-colour ledger, changes at most \(2n\)
lower/opposite-colour occurrences, and reverses the parity of the number
of factor components.

More precisely, if \(c\) is the number of cycles of the PBBS monodromy
\(f^{-2}\), then the switched state has

\[
 c'-c=
 \begin{cases}
 -1,&3\nmid n,\\
 +1,&3\mid n,
 \end{cases}                                               \tag{0.3}
\]

with \(c'-c=-1\) also in the exceptional small case \(r=2\).

Thus the parity part of the PBBS connector problem is solved at cost
\(O(r)=o(B_r)\): use the bridge when the initial component count is even,
and omit it when that count is odd. What remains is the
component-transversal \(C_6\) fusion atlas. Conditional on a compatible
loose \(C_6\)-tree in the resulting odd-component state, the final
Hamilton cycle has triple-union defect \(O(B_r)\).

## 1. The exact PBBS exchange dictionary

Write \(p_+(A)\) and \(p_-(A)\) for the forward- and reverse-unmatched
zeros of the deficit-one cyclic word \(A\in{\cal X}\). Then

\[
 f(A)=A^c\setminus\{p_+(A)\},\qquad
 f^{-1}(A)=A^c\setminus\{p_-(A)\}.                         \tag{1.1}
\]

The old \(M_1\)-edge whose lower endpoint is \(A\) has upper endpoint

\[
 (f^{-1}A)^c=A\cup\{p_-(A)\}.                              \tag{1.2}
\]

In the upper-centre parametrization \(U_Z=Z^c\), the exchange-digraph
criterion is

\[
 Z\longrightarrow X
 \quad\Longleftrightarrow\quad
 f(Z)\cap X=\varnothing,\qquad X\notin\{Z,f^2(Z)\}.         \tag{1.3}
\]

Since \(f(Z)^c=Z\cup\{p_+(Z)\}\), every nontrivial candidate has the
form

\[
 X=Z\setminus\{x\}\cup\{p_+(Z)\},\qquad x\in Z.             \tag{1.4}
\]

Only the unique choice giving \(X=f^2(Z)\) is forbidden by collision
with \(M_0\).

## 2. A clean-label lemma

We use reverse matching, in which a zero is an opening parenthesis and a
one a closing parenthesis.

### Lemma 2.1 (survivors only disappear)

Let \(C\) have \(2t+1\) more zeros than ones, and let \(U_-(C)\) be its
\(2t+1\) reverse-unmatched zeros. Change any \(j\le t\) zeros of \(C\)
to ones. Every reverse-unmatched zero of the resulting word belongs to
\(U_-(C)\).

#### Proof

It suffices to change one zero at a time. Decompose the original cyclic
word at its reverse-unmatched zeros:

\[
 0_{z_0}D_0\,0_{z_1}D_1\cdots0_{z_{d-1}}D_{d-1},
 \qquad d>1,                                                \tag{2.1}
\]

where every \(D_i\) is a reverse-Dyck word. If a displayed \(z_i\) is
changed, the unchanged Dyck blocks cancel and the new closing parenthesis
consumes one other displayed zero. If an internal zero of a \(D_i\) is
changed, retain the old noncrossing matching except for the pair incident
with that zero. The changed zero and its old partner are two unmatched
closing parentheses; after the unchanged pairs are contracted, they
consume two displayed zeros. In both cases every surviving opening is
one of the displayed \(z_i\)'s. The new deficit is \(d-2\), so the claim
can be iterated. \(\square\)

For five cyclic zeros labelled \(0,1,2,3,4\), change a pair to ones and
let \(s(P)\) be the unique reverse-unmatched zero. Direct cancellation
gives

\[
\begin{array}{c|cccccccccc}
P&01&12&23&34&40&02&13&24&30&41\\ \hline
s(P)&2&3&4&0&1&3&4&0&1&2.
\end{array}                                                 \tag{2.2}
\]

Equivalently, the selected positions divide the three unselected positions
into two cyclic gaps, and \(s(P)\) is the first zero in the longer gap.

## 3. Proof that no natural PBBS \(C_8\) exists

Suppose an \(M_1\)-alternating \(C_8\) existed. List its four old lower
endpoints cyclically as \(A_0,A_1,A_2,A_3\). By (1.2), the old upper
endpoint at \(A_i\) is

\[
 U_i=A_i\cup\{p_-(A_i)\}=A_{i-1}\cup A_i,                  \tag{3.1}
\]

where indices are modulo four. Hence

\[
 p_-(A_i)=A_{i-1}\setminus A_i.                            \tag{3.2}
\]

The \(A_i\)'s form a simple \(4\)-cycle in the Johnson graph, and the
four unions \(U_i\) are distinct.

### Lemma 3.1 (the only two Johnson shapes)

Under these hypotheses, the \(A_i\)'s have one of the following forms.

* **Star:** for a common \((r-1)\)-set \(S\) and four distinct labels,

  \[
  A_i=S\cup\{x_i\}.                                         \tag{3.3}
  \]

* **Rectangle:** for a common \((r-2)\)-set \(C\) and four distinct
  labels \(a,b,c,d\), after reversing or rotating the cycle,

  \[
  \begin{aligned}
  A_0&=C\cup\{a,c\},& A_1&=C\cup\{b,c\},\\
  A_2&=C\cup\{b,d\},& A_3&=C\cup\{a,d\}.
  \end{aligned}                                             \tag{3.4}
  \]

#### Proof

The Johnson distance between \(A_0\) and \(A_2\) is one or two. If it is
one, their common neighbours are of star type over \(A_0\cap A_2\), or
are facets of the common \((r+1)\)-set \(A_0\cup A_2\). A neighbour of
the latter type gives the same union on its two incident cycle edges,
contrary to distinctness of the \(U_i\)'s. Thus both \(A_1,A_3\) are
of star type, giving (3.3).

If the distance is two, put \(C=A_0\cap A_2\). Every common neighbour
of \(A_0,A_2\) contains \(C\) and chooses one point from each of the two
two-point differences. If \(A_1,A_3\) agree in either choice, two
consecutive unions coincide. They must therefore be opposite corners,
giving (3.4). \(\square\)

The star is impossible. The core \(S\) has three more zeros than ones,
and (3.2) says

\[
                         p_-(S\cup\{x_i\})=x_{i-1}.         \tag{3.5}
\]

Every one of the four \(x_i\)'s is a reverse survivor after changing one
zero of \(S\). Lemma 2.1 puts all four in the three-point set \(U_-(S)\),
a contradiction.

For the rectangle, (3.2) gives

\[
\begin{array}{ll}
p_-(C\cup\{a,c\})=d,&p_-(C\cup\{b,c\})=a,\\
p_-(C\cup\{b,d\})=c,&p_-(C\cup\{a,d\})=b.
\end{array}                                                 \tag{3.6}
\]

The core \(C\) has five more zeros than ones. Since each of
\(a,b,c,d\) occurs as a survivor in (3.6), Lemma 2.1 puts all four among
the five reverse-unmatched zeros of \(C\). Contract the reverse-matched
pairs of \(C\). Equations (3.6) become

\[
 s(ac)=d,\qquad s(bc)=a,\qquad s(bd)=c,\qquad s(ad)=b       \tag{3.7}
\]

on the cyclic five-set in (2.2).

Rotate so that \(a=0\). The equation \(s(bc)=0\) and (2.2) leave only

\[
 \{b,c\}=\{3,4\}\quad\hbox{or}\quad\{b,c\}=\{2,4\}.          \tag{3.8}
\]

There are four ordered cases:

\[
\begin{array}{c|c|c}
(b,c)&d=s(0c)&\text{failed equation}\\ \hline
(3,4)&1&s(0,1)=2\ne b,\\
(4,3)&1&s(4,1)=2\ne c,\\
(2,4)&1&s(2,1)=3\ne c,\\
(4,2)&3&s(4,3)=0\ne c.
\end{array}                                                 \tag{3.9}
\]

This contradiction proves Theorem A. The forbidden-\(M_0\) condition in
(1.3) was never used.

## 4. Construction of the long even bridge

All subscripts are modulo \(n\). Define

\[
 A_b=\{b-2,b-4,\ldots,b-2r\},                               \tag{4.1}
\]

\[
 T_b=A_b\setminus\{b-2\}\cup\{b\}.                         \tag{4.2}
\]

### Lemma 4.1 (matching identities)

For every \(b\),

\[
 p_+(A_b)=b,\qquad f(A_b)=A_{b+1},                          \tag{4.3}
\]

\[
 p_+(T_b)=b-1,\qquad f^3(T_b)=T_{b+1},                     \tag{4.4}
\]

\[
 f^2(A_b)=A_b\setminus\{b+1\}\cup\{b\},                    \tag{4.5}
\]

\[
 f^2(T_b)=T_b\setminus\{b+1\}\cup\{b-1\}.                  \tag{4.6}
\]

#### Proof

By rotation covariance take \(b=0\). Then \(A_0\) is the alternating word
\(0101\cdots010\). Its \(10\)-pairs leave coordinate \(0\), and flipping
the pairs gives \(A_1\). This proves (4.3), and (4.5) follows by applying
it twice.

The word \(T_0\) is

\[
                         11(01)^{r-2}000.                   \tag{4.7}
\]

Its forward reduction leaves \(2r=-1\). The successive words
\(f(T_0)\) and \(f^2(T_0)\) have forward survivors \(1\) and
\(2r-1=-2\), respectively: cancel the evident internal \(10\)-pairs,
then pair the unique remaining one cyclically with the first available
zero. Their one-sets are explicitly

\[
\begin{aligned}
 f(T_0)&=\{2,4,\ldots,2r-2,2r-1\},\\
 f^2(T_0)&=\{0,3,5,\ldots,2r-3,2r\}.
\end{aligned}                                               \tag{4.8}
\]

In particular,

\[
 f^2(T_0)=T_0\setminus\{1\}\cup\{2r\},                     \tag{4.9}
\]

and its complement, after deleting survivor \(2r-1\), is \(T_1\).
This proves (4.4), (4.6), and the lemma. \(\square\)

### Theorem 4.2 (a legal directed \(C_{2n}\))

For every \(b\), both arrows

\[
                         A_b\longrightarrow T_b
                         \longrightarrow A_{b-2}            \tag{4.9}
\]

are legal in the PBBS exchange digraph.

#### Proof

The first arrow replaces \(b-2\in A_b\) by \(p_+(A_b)=b\). By (4.5),
the forbidden successor \(f^2(A_b)\) instead replaces \(b+1\), so the
two are different for \(n\ge5\).

The second arrow replaces \(b\in T_b\) by \(p_+(T_b)=b-1\), producing

\[
 A_{b-2}=T_b\setminus\{b\}\cup\{b-1\}.
\]

By (4.6), the forbidden successor instead removes \(b+1\). Hence this
arrow is legal. \(\square\)

Because \(2\) is invertible modulo odd \(n\), iterating (4.9) visits all
\(A_b\)'s and all \(T_b\)'s. The two families are disjoint: equality
\(A_b=T_c\) would force \(b=c-1\) by their forward survivors, whereas
\(b-2\in A_b\) but \(b-2\notin T_{b+1}\). Thus (4.9) is a simple
directed \(C_{2n}\).

## 5. Exact monodromy effect

Let

\[
 \sigma=f_1^{-1}f_0,\qquad \sigma(U_Z)=U_{f^{-2}(Z)}.       \tag{5.1}
\]

Fix \(b_0\), put \(b_j=b_0-2j\), and abbreviate

\[
 a_j=U_{A_{b_j}},\qquad t_j=U_{T_{b_j}}.
\]

The switch left-multiplies \(\sigma\) by

\[
 \tau=(a_0\,t_0\,a_1\,t_1\,\cdots\,a_{n-1}\,t_{n-1}).      \tag{5.2}
\]

The \(a_j\)'s form one complete \(\sigma\)-cycle, in the order

\[
                         \sigma(a_j)=a_{j+1}.               \tag{5.3}
\]

For \(r\ge3\), the \(T_b\)'s and their first two \(f\)-images are three
disjoint rotation families. Here is the exact check. Equality
\(f(T_b)=T_c\) forces \(c=b+2\) by their forward survivors; after rotating
to \(b=0\), the label \(3\) belongs to \(T_2\) but not to
\(f(T_0)=\{2,4,\ldots,2r-2,2r-1\}\). Equality
\(f^2(T_b)=T_c\) similarly forces \(c=b-1\); after rotating to \(b=0\),
the label \(3\) belongs to \(f^2(T_0)\) but not to \(T_{-1}\). Finally
\(f(T_b)=f^2(T_c)\) would imply \(T_b=f(T_c)\), already excluded.
All rotations within each family are distinct because their forward
survivors are distinct. Thus the \(T_b\)'s lie in one \(f\)-cycle of
length \(3n\),
hence one \(\sigma=f^{-2}\)-cycle, and

\[
                         \sigma^3(t_j)=t_{j+1}.              \tag{5.4}
\]

There are no other marked vertices between \(t_j\) and \(t_{j+1}\) on
this \(\sigma\)-cycle.

This \(T\)-cycle is disjoint from the \(A\)-cycle. We already proved that
no \(T_b\) equals an \(A_c\). If \(f^k(T_b)=A_c\) for \(k=1\) or \(2\),
then applying \(f^{3-k}\) and using (4.3)--(4.4) would give an equality
between another \(T\)-state and an \(A\)-state, again impossible.

Cut the incoming \(\sigma\)-arcs at all \(a_j,t_j\). In
\(\tau\sigma\), a trace starting at \(t_j\) follows its old
\(\sigma\)-segment to the predecessor of \(t_{j+1}\), passes through
\(a_{j+2}\), and enters \(t_{j+3}\). The induced return permutation on
the \(n\) cut \(T\)-segments is

\[
                         j\longmapsto j+3.                  \tag{5.5}
\]

The two old touched components are replaced by \(\gcd(n,3)\) components.
Consequently

\[
 c(\tau\sigma)-c(\sigma)=\gcd(n,3)-2,                       \tag{5.6}
\]

which is (0.3).

For \(r=2\), one instead has \(f(T_b)=T_{b+2}\). The \(T_b\)'s are still
one \(\sigma\)-cycle; tracing the same cut arcs gives the return shift
\(j\mapsto j+4\pmod 5\). This is a five-cycle, so the two touched
components merge and \(c'-c=-1\).

Since \(2n\) is even, the multiplier (5.2) is odd. The exact calculation
also directly confirms that component parity reverses.

## 6. The hexagon atlas survives the bridge

Let

\[
 {\cal S}=\{A_b,T_b:b\in\mathbb Z/n\mathbb Z\}
\]

be the \(2n\)-vertex support of the directed bridge. A natural PBBS
star hexagon whose three centre vertices avoid \({\cal S}\) is physically
disjoint from the bridge: its upper vertices are indexed by those three
centres, and its lower vertices are their three distinct \(f\)-images.
The bridge therefore changes none of its six incidences. Every such
hexagon remains alternating and legal after the bridge.

The complete PBBS triangle atlas has \(N-n\) legal cores, where
\(N=\binom n{r-1}\), and every centre belongs to at most \(r\) atlas
triangles. Deleting \({\cal S}\) consequently destroys at most \(2nr\)
triangles. The post-bridge state retains at least

\[
                         N-n-2nr                            \tag{6.1}
\]

natural legal hexagons. Since the atlas is linear with maximum degree
\(r\), greedy packing still gives a physically disjoint family of size

\[
 {N-n-2nr\over3r-2}
   =\left({2\over3}+o(1)\right)B_r.                         \tag{6.2}
\]

Thus the parity repair does not consume a positive fraction of the
available \(C_6\) supply. It leaves only the quotient-topology question,
not a local or scalar connector shortage.

## 7. Triple-union cost and the remaining connector theorem

An alternating circuit with \(k\) old \(M_1\)-edges changes exactly \(k\)
matching slots and at most \(k\) opposite triple-union occurrences. The
bridge has \(k=2n\). Since the initial PBBS defect is

\[
 \beta_r^{\rm PBBS}={2\over r+2}\binom nr,                  \tag{7.1}
\]

after the bridge

\[
 \beta_r\le {2\over r+2}\binom nr+2n=O(B_r).                \tag{7.2}
\]

If a subsequent compatible component-transversal \(C_6\)-forest uses
\(s=O(B_r)\) switches, it changes at most \(3s\) more occurrences and
still gives

\[
 \beta_r=O(B_r)=o\!\left(\binom nr\right).                  \tag{7.3}
\]

When the initial component count is even, the bridge makes it odd at cost
\(O(r)\), so a \(C_6\)-forest may end in one component. When it is
already odd, omit the bridge. The only remaining hypothesis is:

> **PBBS component-transversal hexagon-tree lemma (unproved).** After the
> explicit bridge, the factor components admit an ordered loose spanning
> tree of legal \(M_1\)-alternating \(C_6\)'s, with every switch meeting
> three current components.

Theorem A also gives a lower boundary for any alternative net parity
change. The symmetric difference of the initial and final perfect
matchings decomposes into initial alternating circuits. A parity change
forces at least one circuit with an even number of old matching edges.
The adjacent-rank graph has no alternating \(C_4\), and Theorem A rules
out \(C_8\). Hence such a net bridge contains an alternating circuit of
length at least \(12\). The explicit bridge has length \(8r+4\);
optimizing it is quantitatively irrelevant to the Catalan edit budget.

## 8. Audited boundary

Proved here:

1. no natural PBBS \(M_1\)-alternating \(C_8\) exists;
2. the earlier disjoint-\(C_8\) connector-atlas hypothesis is false;
3. an explicit legal parity bridge exists with \(4r+2\) changed slots;
4. its component effect is exactly \(-1\) or \(+1\) as in (0.3); and
5. its triple-union cost is \(O(r)=o(B_r)\).

Still unproved:

1. a component-transversal spanning \(C_6\)-tree after the bridge;
2. an unconditional PBBS Hamiltonization; and
3. the resulting constant-one contiguous-OR theorem.
