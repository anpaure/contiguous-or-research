# The exact opposite-triple defect of the \(0/1\)-lexical Middle-Levels factor

Date: 2026-07-26

Method: pure mathematics only. No finite search or computation is used.

## 0. Statement and consequence

Let

\[
 {\cal X}_r=\binom{[2r+1]}r,\qquad
 {\cal Y}_r=\binom{[2r+1]}{r+1},\qquad
 W_r=|{\cal X}_r|=\binom{2r+1}r .
\]

Let \(F_{01}\) be the spanning \(2\)-factor of the Middle-Levels graph
\(Q_{2r+1}(r,r+1)\) obtained by taking the union of the \(0\)- and
\(1\)-lexical perfect matchings. For \(x\in{\cal X}_r\), let \(y_0(x)\)
and \(y_1(x)\) be its two neighbours in \({\cal Y}_r\), and define its
opposite triple colour by

\[
                         \Phi(x):=y_0(x)\cup y_1(x).
\tag{0.1}
\]

Equivalently, after traversing a component of \(F_{01}\), suppressing its
upper vertices, and writing \(x^-,x,x^+\) for three consecutive lower
vertices, one has

\[
                         \Phi(x)=x^-\cup x\cup x^+.
\tag{0.2}
\]

### Theorem 0.1 (exact lexical opposite-triple defect)

For \(r\ge3\), the number of rank-\((r+2)\) targets omitted by \(\Phi\) is

\[
\boxed{
 M_r
 =\binom{2r-1}{r-3}
   -\frac2{r-1}\binom{2r-2}{r-3}
 =W_r\frac{(r-2)(r-3)}{2(r+2)(2r-1)} .}
\tag{0.3}
\]

Since

\[
 \left|\binom{[2r+1]}{r+2}\right|
 =\frac r{r+2}W_r,
\]

the exact triple-union deficit in the normalization of the GMM fallback is

\[
\boxed{
 W_r-|\Phi({\cal X}_r)|
 =\frac{2W_r}{r+2}+M_r
 =W_r\frac{r+1}{2(2r-1)}.}
\tag{0.3a}
\]

In particular,

\[
                         M_r=\left(\frac14+O(r^{-1})\right)W_r.
\tag{0.4}
\]

Thus the \(0/1\)-lexical factor has a **linear** opposite-triple defect.
It is not a complete-support substitute for the PBBS factor.

Moreover, if \(s\) factor-alternating hexagon flips are applied to
\(F_{01}\), then the resulting factor still omits at least

\[
                         M_r-3s
\tag{0.5}
\]

rank-\((r+2)\) targets, and its domain-normalized deficit is at least

\[
 W_r\frac{r+1}{2(2r-1)}-3s.
\tag{0.5a}
\]

The standard lexical Hamiltonization uses
\(s=p_r-1\le\operatorname {Cat}_r-1=W_r/(2r+1)-1\). Every Hamilton cycle
obtained by that published merge scheme therefore omits

\[
                         \left(\frac14-o(1)\right)W_r
\tag{0.6}
\]

opposite triple targets. This is a construction-specific linear no-go;
it says nothing by itself about a different Mütze--Su Middle-Levels
Hamilton cycle.

## 1. Lattice-path and chain notation

Interpret \(0\) as a down-step and \(1\) as an up-step. Every word has a
unique Greene--Kleitman chain factorization

\[
                         u_0* u_1*\cdots *u_h,
\tag{1.1}
\]

where every \(u_i\) is a Dyck word (never above its initial height) and
the stars are the unmatched bits. The stars are \(1\)'s followed by
\(0\)'s.

A lower middle word \(x\in{\cal X}_r\) has endpoint height \(-1\). Hence,
for a unique \(j\ge0\), its factorization is

\[
 x=u_0\,1\,u_1\,1\cdots 1\,u_j\,0\,u_{j+1}\,0\cdots0\,u_{2j+1}.
\tag{1.2}
\]

The \(0\)-lexical upward edge flips the first unmatched zero, namely the
displayed zero immediately after \(u_j\).

The lexical scan orders down-steps row by row from top to bottom and from
right to left within a row. Thus the \(1\)-lexical edge flips the second
down-step in this order. The following lemma makes that step explicit.

### Lemma 1.1 (the second lexical down-step)

For \(x\) as in (1.2), exactly one of the following holds.

1. If \(u_j\ne\varepsilon\), write its right factorization as

   \[
                         u_j=v\,0\,w\,1,
   \qquad v,w\in D.
   \tag{1.3}
   \]

   The \(1\)-lexical upward edge flips the displayed \(0\) in (1.3).

2. If \(u_j=\varepsilon\) and \(j\ge1\), the \(1\)-lexical upward edge
   flips the second unmatched zero, the zero immediately after
   \(u_{j+1}\).

3. If \(j=0\) and \(u_0=\varepsilon\), then

   \[
                         x=0u_1,
   \qquad u_1=v\,0\,w\,1,
   \tag{1.4}
   \]

   and the \(1\)-lexical upward edge flips the displayed \(0\) in the
   right factorization of \(u_1\).

#### Proof

The first unmatched zero starts at the maximum row attained by a down-step
of \(x\), and it is the rightmost down-step in that row. This is the
\(0\)-lexical step.

If \(u_j\ne\varepsilon\), the other down-steps in the same maximum row
are precisely the first down-steps of the top-level components of \(u_j\).
The rightmost of them is the \(0\) in the right factorization (1.3), so it
is second in the lexical order.

If \(u_j=\varepsilon\), no second down-step exists in the maximum row.
When \(j\ge1\), the second unmatched zero exists. It lies in the next
row, after the entire valley \(u_{j+1}\), and is therefore the rightmost
down-step in that row.

When \(j=0\), there is only one unmatched zero. All remaining down-steps
belong to the nonempty Dyck word \(u_1\) one row lower. Its rightmost
top-level down-step is exactly the \(0\) in (1.4). This proves all three
cases. \(\square\)

The third case is essential. Omitting it changes the exact answer by a
Catalan-scale boundary term.

## 2. Forward formula for the opposite colour

The two upper neighbours of \(x\) are obtained by flipping the two steps
in Lemma 1.1. Their union therefore flips both steps simultaneously.

### Lemma 2.1 (three forward normal forms)

For \(x\) as in (1.2):

1. if \(u_j=v0w1\ne\varepsilon\), the relevant part changes as

   \[
                         v\,0\,w\,1\,0
              \longmapsto v\,1\,w\,1\,1;
   \tag{2.1}
   \]

2. if \(u_j=\varepsilon\) and \(j\ge1\), it changes as

   \[
                         0\,u_{j+1}\,0
              \longmapsto 1\,u_{j+1}\,1;
   \tag{2.2}
   \]

3. if \(j=0,u_0=\varepsilon\), and \(u_1=v0w1\), it changes as

   \[
                         0\,v\,0\,w\,1
              \longmapsto 1\,v\,1\,w\,1.
   \tag{2.3}
   \]

These are the only possibilities.

#### Proof

This is immediate from the \(0\)-lexical step and Lemma 1.1. To justify
(0.2), an upper neighbour \(y_k(x)=x\cup\{a_k\}\) has another lower
factor neighbour distinct from \(x\), so that other lower neighbour
contains \(a_k\). Hence its union with \(x\) is \(y_k(x)\). Doing this
on the two sides of \(x\) proves
\(x^-\cup x\cup x^+=y_0(x)\cup y_1(x)\). \(\square\)

## 3. Exact inverse and fibre formula

Fix a target \(T\in\binom{[2r+1]}{r+2}\). Its endpoint height is \(+3\).
Let \(b\ge0\) be the number of its unmatched zeros. Then it has \(b+3\)
unmatched ones and a unique factorization

\[
 T=u_0\,1\cdots1\,u_{b+2}\,1\,u_{b+3}\,0\cdots0\,u_{2b+3}.
\tag{3.1}
\]

There are \(2b+4\) Dyck valleys, and their total semilength is

\[
                         \sum_i |u_i|/2=r-b-1.
\tag{3.2}
\]

### Theorem 3.1 (exact fibre multiplicity)

If \(b\ge1\), then

\[
 |\Phi^{-1}(T)|
 =\mathbf 1_{\{u_{b+1}=\varepsilon\}}
  +\mathbf 1_{\{u_{b+2}=\varepsilon\}}.
\tag{3.3}
\]

If \(b=0\), then

\[
 |\Phi^{-1}(T)|
 =\mathbf 1_{\{u_1=\varepsilon\}}
  +\mathbf 1_{\{u_2=\varepsilon\}}
  +\mathbf 1_{\{u_0=u_3=\varepsilon\}}.
\tag{3.4}
\]

#### Proof

Every lower preimage belongs to exactly one of the three forward cases of
Lemma 2.1.

For (2.2), the target retains the same \(2j+1\) chain stars, but the first
two unmatched zeros have become ones. Thus \(b=j-1\), and the empty
central valley of the source is \(u_j=u_{b+1}\). Conversely, whenever
\(u_{b+1}=\varepsilon\), changing the last two unmatched ones of \(T\) to
zeros reconstructs a unique source of form (2.2). This case requires
\(j=b+1\ge1\), so it works also for \(b=0\).

For (2.1), breaking the last top-level Dyck pair creates two new unmatched
ones, and flipping the first unmatched zero creates a third. Thus \(b=j\).
In the target factorization, the three displayed ones in (2.1) are
separated by valleys \(v,w,\varepsilon\). Therefore
\(u_{b+2}=\varepsilon\). Conversely, if that valley is empty, replace

\[
                         v\,1\,w\,1\,1
                 \quad\hbox{by}\quad
                         v\,0\,w\,1\,0
\]

to reconstruct the unique source with central Dyck word \(v0w1\).

Finally, (2.3) necessarily has \(b=0\), and its target factorization is

\[
                         \varepsilon\,1\,v\,1\,w\,1\,\varepsilon.
\]

It therefore gives exactly the additional indicator
\(u_0=u_3=\varepsilon\). Conversely those two empty outer valleys recover
the unique source \(0v0w1\). No source remains outside the exhaustive
three cases of Lemma 2.1, proving (3.3)--(3.4). \(\square\)

Thus, for \(b\ge1\), a target is missing exactly when both displayed
central valleys \(u_{b+1},u_{b+2}\) are nonempty. For \(b=0\), the same
criterion holds except that the special \(h=1\) matching rescues the
targets whose two outer valleys are both empty.

## 4. Ballot enumeration of the missing targets

Let

\[
                         C(z)=\sum_{k\ge0}\operatorname {Cat}_k z^k
\]

be the Catalan generating function. Recall

\[
                         C(z)-1=zC(z)^2
\tag{4.1}
\]

and, for positive integer \(p\),

\[
 [z^k]C(z)^p=\frac{p}{2k+p}\binom{2k+p}{k}.
\tag{4.2}
\]

If the \(h=1\) rescue in (3.4) is temporarily ignored, the number of
targets having both specified valleys nonempty is

\[
\begin{aligned}
 M_r^{\rm raw}
 &=\sum_{b=0}^{r-3}
   [z^{r-b-1}](C-1)^2C^{2b+2}\\
 &=\sum_{b=0}^{r-3}[z^{r-b-3}]C^{2b+6}\\
 &=\sum_{b=0}^{r-3}\frac{b+3}{r}\binom{2r}{r-b-3}.
\end{aligned}
\tag{4.3}
\]

Put \(t=r-b-3\). Since

\[
 \frac{r-t}{r}\binom{2r}{t}
 =\binom{2r-1}{t}-\binom{2r-1}{t-1},
\tag{4.4}
\]

the sum telescopes to

\[
                         M_r^{\rm raw}=\binom{2r-1}{r-3}.
\tag{4.5}
\]

The rescued targets have \(b=0\), \(u_0=u_3=\varepsilon\), and
\(u_1,u_2\ne\varepsilon\). Their number is

\[
\begin{aligned}
 E_r
 &=[z^{r-1}](C-1)^2\\
 &=[z^{r-3}]C^4
 =\frac2{r-1}\binom{2r-2}{r-3}.
\end{aligned}
\tag{4.6}
\]

Subtracting (4.6) from (4.5) proves the first expression in (0.3).
Dividing by \(W_r\) gives

\[
 \frac{M_r}{W_r}
 =\frac{(r-1)(r-2)}{2(2r+1)(r+2)}
  -\frac{r-2}{(2r+1)(2r-1)}
 =\frac{(r-2)(r-3)}{2(r+2)(2r-1)},
\tag{4.7}
\]

which proves the second expression and (0.4).

## 5. Stability under lexical hexagon Hamiltonization

An alternating \(6\)-cycle in the bipartite Middle-Levels graph contains
three lower vertices. Taking symmetric difference with it changes one
factor edge at each of those three lower vertices and changes no factor
edge elsewhere. Consequently at most three values of \(\Phi\) change.
One map-value edit can enlarge the image by at most one, so after \(s\)
such switches at most \(3s\) formerly missing targets can be gained. This
proves (0.5).

The standard \(0/1\)-lexical factor has \(p_r\) components, indexed by
plane trees with \(r\) edges, and the published compatible merge tree uses
\(p_r-1\) hexagons. Forgetting the root maps the
\(\operatorname {Cat}_r\) rooted ordered trees onto those plane trees, so

\[
                         p_r-1\le\operatorname {Cat}_r-1
                         =\frac{W_r}{2r+1}-1.
\tag{5.1}
\]

Equations (0.3), (0.5), and (5.1) yield (0.6).

## 6. Adversarial audit and exact scope

1. **The \(h=1\) boundary is not optional.** For
   \(x=0(v0w1)\), the two matching neighbours flip the first displayed
   zero and the zero inside \(v0w1\), giving target \(1v1w1\). These are
   exactly the \(b=0\) targets with empty outer valleys. Omitting this
   branch gives the incorrect raw count \(\binom{2r-1}{r-3}\); (4.6) is
   the necessary correction.

2. **The triple colour really is the union of the two upper neighbours.**
   This uses edge-disjointness of the two perfect matchings. Without it,
   the other lower endpoint of an upper neighbour might equal \(x\), and
   (0.2) would fail. In the \(0/1\)-lexical factor the matchings are
   edge-disjoint by their distinct scan indices.

3. **No hidden inverse cases remain.** Lemma 1.1 partitions lower words
   according to \(u_j\ne\varepsilon\), \(u_j=\varepsilon,j\ge1\), and
   \(u_j=\varepsilon,j=0\). The reconstructions in Theorem 3.1 reverse
   these three cases uniquely.

4. **This does not refute every Middle-Levels Hamilton cycle.** It proves
   a linear obstruction for the \(0/1\)-lexical factor and for any factor
   within \(o(W_r)\) lower-slot edits of it. The published
   \(O(\operatorname {Cat}_r)\)-hexagon Hamiltonization is in that class.
   A construction with a linear number of different lower slots, including
   a separately defined Mütze--Su cycle unless an overlap theorem is
   supplied, is outside the conclusion.

5. **Quantitative implication for the recursive GMM fallback.** If the
   chosen Middle-Levels base routine is exactly the standard lexical
   Hamiltonization, its base opposite defect is
   \((1/4-o(1))W_r\), not \(O(\operatorname {Cat}_r)\). Therefore that
   base cannot satisfy the Catalan-scale hypothesis needed by the Pascal
   recursion. Identifying a different routine with the lexical one must
   be done at the edge-set level, not by theorem attribution alone.
