# Rank-isolating cyclic-order rectangles: exact lattice and the 0--1 obstruction

Date: 2026-07-25

Pure mathematics only.

## 0. Verdict

Fix a top \(U\) of size \(M=m+H\).  Start with an oriented cyclic order
\(\pi\), and perform two disjoint adjacent swaps at cyclic boundaries whose
separation is \(r\).  The four orders

\[
 \pi_{00},\quad \pi_{10},\quad \pi_{01},\quad \pi_{11}
\]

form an exact signed rectangle.  If \({\cal I}_s(\pi)\) denotes the
incidence vector of all cyclic \(s\)-intervals, then

\[
 {cal I}_s(\pi_{00})+{cal I}_s(\pi_{11})
 -{cal I}_s(\pi_{10})-{cal I}_s(\pi_{01})=0             \tag{0.1}
\]

unless

\[
 s\in\{r,M-r\}.                                         \tag{0.2}
\]

At \(s=r\), the nonzero vector is one elementary octahedral square

\[
 e_{C+yu}+e_{C+xv}-e_{C+xu}-e_{C+yv}.                   \tag{0.3}
\]

The \((M-r)\)-vector is its within-\(U\) complementary square.  Therefore
choosing \(r=m-q\) isolates the lower depth \(q\) from every other
controlled length; its companion length is \(H+q<m-H\).  Choosing
\(r=m+q\) similarly isolates upper depth \(q\), with companion length
\(H-q\).

Moreover, the square vectors (0.3) generate the complete integer lattice of
rank-\(r\) load changes with zero point marginals.  Thus there is no further
linear, parity, or lattice invariant at an isolated rank.

However, the naive physical implementation by putting two *full* diagonal
packets on one top is invalid at coefficient one.  Two cyclic orders which
differ by the two adjacent swaps share at least

\[
 M-4                                                     \tag{0.4}
\]

of their \(M\) middle windows.  Hence two diagonal packets contain at most
\(M+4\), rather than \(2M\), distinct middle owners.  Using two packets on
half of the tops covers at most

\[
 \frac{M+4}{2}N_H=(1/2+o(1))W                           \tag{0.5}
\]

distinct middle owners at the crossing scale.  The rectangle is therefore
an exact signed/multiplicity trade, but not a legal trade inside a 0--1
middle-owner packet matching.

This is a sharp distinction.  Algebraically, the rank loads can be adjusted
independently.  Physically, almost all of the two full-packet occurrences
are duplicate owners.

There is nevertheless a valid truncated repair.  On a controlled band of
lengths \(m-Q,\ldots,m+Q\), one full baseline order plus at most three short
promotion segments can realize the rectangle exactly.  It uses only
\(M+O(Q)\) state occurrences, has at most four paths, and preserves its
complete middle multiset.  This repairs the full-packet overlap objection,
but it does not by itself prove balancing: one elementary rectangle moves
only two units of load, and positivity creates a genuine additional gate.

## 1. The four-order rectangle

Number the cyclic positions \(0,1,\ldots,M-1\).  Put

\[
 x=\pi(0),\qquad y=\pi(1),\qquad
 u=\pi(r),\qquad v=\pi(r+1),                             \tag{1.1}
\]

where

\[
 2\le r\le M-2.                                         \tag{1.2}
\]

Let \(\tau_0\) swap positions \(0,1\), and let \(\tau_r\) swap positions
\(r,r+1\).  They commute.  Define

\[
 \pi_{ab}=\tau_0^a\tau_r^b\pi,
 \qquad a,b\in\{0,1\}.                                  \tag{1.3}
\]

For \(1\le s<M\), let

\[
 {cal I}_s(\pi)=\sum_{j\in\mathbb Z_M}e_{I_\pi(j,s)}.  \tag{1.4}
\]

All the \(s\)-intervals are distinct, so this is a \(0\)--\(1\) vector.

### Lemma 1.1 (one adjacent swap changes only two windows)

At a fixed length \(s\), swapping two adjacent positions changes exactly
the two cyclic windows whose boundary separates those positions.  All other
windows contain both swapped labels or neither and hence are unchanged as
sets.

#### Proof

An interval can change as a set only if it contains exactly one of the two
swapped positions.  For adjacent positions, precisely one length-\(s\)
window ends at the first position and one begins at the second. \(\square\)

### Theorem 1.2 (exact rank isolation)

Put

\[
 \mathscr R_s
 ={cal I}_s(\pi_{00})+{cal I}_s(\pi_{11})
 -{cal I}_s(\pi_{10})-{cal I}_s(\pi_{01}).             \tag{1.5}
\]

Then \(\mathscr R_s=0\) unless \(s=r\) or \(s=M-r\).

Let

\[
 C=\{\pi(2),\ldots,\pi(r-1)\},                          \tag{1.6}
\]

and

\[
 D=U-\bigl(C+\{x,y,u,v\}\bigr).                        \tag{1.7}
\]

At the two exceptional lengths,

\[
 \boxed{
 \mathscr R_r
 =e_{C+yu}+e_{C+xv}-e_{C+xu}-e_{C+yv},}                 \tag{1.8}
\]

and

\[
 \boxed{
 \mathscr R_{M-r}
 =e_{D+xv}+e_{D+yu}-e_{D+yv}-e_{D+xu}.}                 \tag{1.9}
\]

#### Proof

The mixed difference in (1.5) can be nonzero only on a window changed by
both adjacent swaps.  Such a window must contain exactly one position from
\(\{0,1\}\) and exactly one from \(\{r,r+1\}\).  The two possible cyclic
arcs are

\[
 1,2,\ldots,r
 \quad\text{and}\quad
 r+1,r+2,\ldots,0,
\]

of lengths \(r\) and \(M-r\), respectively.  This proves the vanishing.
Reading the four label choices on the first arc gives (1.8), and reading
their complements in \(U\) gives (1.9). \(\square\)

### Corollary 1.3 (controlled-band isolation)

Assume \(3H<m\), as holds at the crossing scale for all sufficiently large
\(m\).

* If \(r=m-q\), \(1\le q\le H\), then the companion exceptional length is
  \(M-r=H+q\le2H<m-H\).  Hence among the controlled lengths
  \([m-H,m+H]\), only the lower depth \(q\) changes.
* If \(r=m+q\), \(1\le q<H\), then \(M-r=H-q<m-H\).  Hence only the upper
  depth \(q\) changes.

In both cases the middle length \(m\) is unchanged.

## 2. The exact rank lattice

Let \(V\) be a finite set of size \(n\), and let

\[
 A_r:\mathbb Z^{\binom Vr}\longrightarrow\mathbb Z^V
\]

be the point-incidence map

\[
 (A_rz)(a)=\sum_{S\ni a}z_S.                            \tag{2.1}
\]

Every square

\[
 Q(C;x,y,u,v)
 =e_{C+yu}+e_{C+xv}-e_{C+xu}-e_{C+yv},                 \tag{2.2}
\]

where \(|C|=r-2\) and the four displayed points are distinct and outside
\(C\), lies in \(\ker_{\mathbb Z}A_r\).

### Theorem 2.1 (octahedral generation)

For \(2\le r\le n-2\),

\[
 \boxed{
 \ker_{\mathbb Z}A_r
 =\left\langle Q(C;x,y,u,v)\right\rangle_{\mathbb Z}.}  \tag{2.3}
\]

For \(r=1\) and \(r=n-1\), the kernel is zero.

#### Proof

Let \(z\in\ker_{\mathbb Z}A_r\).  Regard its positive and negative parts
as two multisets \({\cal P},{\cal N}\) of \(r\)-sets.  Their point-degree
vectors agree.  Label the member slots of both multisets.  Their incidence
matrices are bipartite \(0\)--\(1\) matrices with identical row and column
sums.

The symmetric difference of two such matrices decomposes into alternating
even cycles.  Successive \(2\times2\) switches along those cycles transform
one matrix into the other.  On the hyperedge multisets, one switch has the
form

\[
 e_A+e_B-e_{A-a+b}-e_{B-b+a},                           \tag{2.4}
\]

where \(a\in A-B\) and \(b\in B-A\).

It remains to decompose (2.4) into the local squares (2.2).  Induct on

\[
 d=|A-B|=|B-A|.
\]

The case \(d=2\) is exactly (2.2); the case \(d=1\) is zero.  For \(d>2\),
choose

\[
 p\in(A-B)-\{a\},\qquad q\in(B-A)-\{b\}.
\]

The square with common core \(A-\{a,p\}\) is

\[
 e_A+e_{A-a-p+b+q}-e_{A-a+b}-e_{A-p+q}.                \tag{2.5}
\]

After subtracting (2.5) from (2.4), the remainder is the same exchange
relation between \(A-p+q\) and \(B\), now at distance \(d-1\).  Induction
finishes the decomposition.  Hence all of \(\ker_{\mathbb Z}A_r\) is
generated by (2.2).

At ranks \(1\) and \(n-1\), the point-incidence map has trivial integer
kernel. \(\square\)

### Corollary 2.2 (all point-neutral rank changes are formal rectangles)

Fix \(r\le M-2\).  Every integer change of the global rank-\(r\) histogram
which preserves all coordinate point marginals is an integer combination of
cyclic-order rectangles supported inside tops of size \(M\).

#### Proof

Theorem 2.1 supplies squares (2.2).  Each uses only the \(r+2\) points
\(C+\{x,y,u,v\}\), which can be extended to a top \(U\) of size \(M\).
Arrange the four special points and \(C\) as in (1.1), (1.6); Theorem 1.2
realizes the square. \(\square\)

Therefore the formal trade lattice has exactly the expected invariant:
the point marginal.  There is no hidden parity class or additional linear
congruence.

### Corollary 2.3 (all full top-packet choices lie in one formal fibre)

Choose one full cyclic packet on every top \(U\in\binom{[2m]}M\).  At
rank \(r<M\), every coordinate occurs in exactly

\[
 r\binom{2m-1}{M-1}=\frac{rMN_H}{2m}                    \tag{2.6}
\]

selected interval occurrences, independently of every cyclic-order choice.
Consequently the difference between the rank-\(r\) load vectors of any two
one-packet-per-top selections is an integer combination of rank-\(r\)
rectangles.

#### Proof

Inside one cyclic order on \(U\), a coordinate of \(U\) belongs to exactly
\(r\) of the \(M\) cyclic \(r\)-intervals.  There are
\(\binom{2m-1}{M-1}\) tops containing a fixed coordinate.  This proves
(2.6), and Theorem 2.1 gives the final assertion. \(\square\)

## 3. Why two diagonal packets are not physical

The preceding section concerns signed incidence vectors.  A physical packet
transversal requires every middle owner to occur at most once.

### Theorem 3.1 (diagonal overlap)

At any length \(s\notin\{r,M-r\}\), and in particular at \(s=m\) for the
rank-isolating choices in Corollary 1.3, the two diagonal orders
\(\pi_{10},\pi_{01}\) have at least \(M-4\) common cyclic \(s\)-intervals.
The same is true of \(\pi_{00},\pi_{11}\).

Consequently either diagonal pair has at most \(M+4\) distinct middle
windows in total.

#### Proof

The orders \(\pi_{10}\) and \(\pi_{01}\) differ by the two disjoint
adjacent swaps.  By Lemma 1.1, each swap can change only two length-\(s\)
windows.  All other \(M-4\) windows are identical in the two orders.
The union bound gives the assertion.  The other diagonal is identical.  A
pair has \(2M\) window occurrences, of which at least \(M-4\) are shared,
so its union has size at most \(M+4\). \(\square\)

### Corollary 3.2 (the half-top allocation has linear middle defect)

At the crossing scale, putting a diagonal pair on \(N_H/2\) tops and no
packet on the remaining tops covers at most

\[
 \frac{M+4}{2}N_H
 =\left(\frac12+o(1)\right)W                             \tag{3.1}
\]

distinct middle owners.

Thus its literal middle repair alone costs \((1/2-o(1))W\).

### Corollary 3.3 (rectangles preserve an existing middle defect)

As a signed identity, the rectangle preserves the complete middle
*multiset*.  Hence it cannot turn a middle multiplicity-two/hole pair into
a 0--1 middle transversal.  Any starting diagonal with repeated owners has
the same middle load vector after the trade.

This rules out using the rectangle first and repairing middle ownership
later at sublinear cost.

## 4. What survives

### 4.1 A legal bounded-segment rectangle

Fix a hard band

\[
 {cal B}_Q=\{m-Q,m-Q+1,\ldots,m+Q\},\qquad 1\le Q\le H,
                                                               \tag{4.1}
\]

and choose the swap separation

\[
 r=m-q_0\quad\text{or}\quad r=m+q_0,qquad1\le q_0\le Q.       \tag{4.2}
\]

For a swap across positions \(a,a+1\), let \(E_a\subseteq\mathbb Z_M\)
be the set of phase starts at which *some* length in \({\cal B}_Q\) is
changed by that swap.  Lemma 1.1 gives the exact formula

\[
 E_a
 =\{a+1\}\cup
 \{a-s+1:s\in{cal B}_Q\}.                              \tag{4.3}
\]

Thus \(E_a\) is the union of one point and one cyclic interval of length
\(2Q+1\).  Put

\[
 O=E_0\cap E_r,qquad K=E_0-E_r.                        \tag{4.4}
\]

Both \(O\) and \(K\) are unions of at most two cyclic intervals, and

\[
 |O|\le2Q+2.                                             \tag{4.5}
\]

Consider the following two phase-restricted configurations:

\[
 \begin{array}{c|c}
 \text{left configuration}&\text{selected starts}\\ \hline
 \pi_{00}&\mathbb Z_M\\
 \pi_{11}&O
 \end{array}                                             \tag{4.6}
\]

and

\[
 \begin{array}{c|c}
 \text{right configuration}&\text{selected starts}\\ \hline
 \pi_{01}&E_0=K\cup O\\
 \pi_{10}&\mathbb Z_M-K.
 \end{array}                                             \tag{4.7}
\]

Every cyclic interval of selected starts is emitted as one promotion path.
Consequently each side of (4.6)--(4.7) uses at most four paths.  Both sides
have exactly

\[
 M+|O|=M+O(Q)                                             \tag{4.8}
\]

state occurrences.

### Theorem 4.1 (bounded-segment rank isolation)

For every \(s\in{cal B}_Q\), the difference between the rank-\(s\)
incidence vectors of (4.6) and (4.7) is exactly \(\mathscr R_s\) from
Theorem 1.2.  In particular it vanishes at every controlled length except
\(s=r\), where it is the square (1.8).

At middle length \(m\), the two configurations have exactly the same
middle multiset.  Replacing one by the other therefore preserves every
middle multiplicity and every middle hole.

#### Proof

Fix a phase start \(j\).

* If \(j\notin E_0\), the left side uses \(\pi_{00}\) and the right side
  uses \(\pi_{10}\).  The swap at \(0,1\) changes no controlled window
  starting at \(j\), so their rank-\(s\) intervals agree.
* If \(j\in E_0-E_r=K\), the left side uses \(\pi_{00}\) and the right
  side uses \(\pi_{01}\).  The swap at \(r,r+1\) changes no controlled
  window starting at \(j\), so they agree.
* If \(j\in O\), both diagonal orders are used on each side.  Their local
  difference is the full rectangle contribution at phase \(j\).

Summing over phases gives precisely the full rectangle mixed difference.
Theorem 1.2 now proves the assertion.  Since \(m\notin\{r,M-r\}\), the
middle difference is zero. \(\square\)

### Corollary 4.2 (the segment toll is asymptotically legal)

At the crossing scale of
`TOP_FIBRE_CROSSING_PACKET_REDUCTION_20260725.md`, put one bounded-segment
gadget on every top.  Its extra state-occurrence cost is at most

\[
 O(QN_H)=O(WQ/m)=o(W)                                   \tag{4.9}
\]

whenever \(Q=o(m)\).  Its path count is \(O(N_H)\), so its total
initialization toll is

\[
 O(HN_H)=O(WH/m)=o(W).                                  \tag{4.10}
\]

Thus truncation completely repairs the *cost* objection to local
rectangles.  It does not repair the generation/positivity objection below.

### 4.2 Formal generation is not positive generation

Theorem 2.1 is an integer-lattice statement.  It does not say that every
two nonnegative load vectors with equal point marginals are connected by a
sequence of elementary squares which stays nonnegative.

### Proposition 4.3 (a smallest positivity obstruction)

On six points at rank three, put

\[
 \mu=e_{123}+e_{456},\qquad
 \nu=e_{234}+e_{156}.                                   \tag{4.11}
\]

Then \(A_3\mu=A_3\nu=\mathbf1\), so \(\mu-\nu\) lies in the square
lattice of Theorem 2.1.  Nevertheless no nonzero elementary square can be
applied to \(\mu\) while keeping all coordinates nonnegative.

#### Proof

The negative side of an applicable elementary rank-three square consists
of two present triples sharing its one-point core.  The only two triples in
the support of \(\mu\) are disjoint.  Hence no square is applicable.
The point-degree identity is immediate. \(\square\)

So the octahedral rectangles are not, by themselves, a positive Markov
basis for the load fibre.  A higher-order circuit or a sufficiently dense
reservoir is required.

### 4.3 Remaining uses

The rectangle remains potentially useful in either of two settings.

1. **A nonlocal 0--1 trade.**  Embed many local rectangles into a larger
   circuit whose positive and negative packet families are separately
   middle-disjoint.  Theorem 2.1 says such a circuit would have complete
   rank-control once it exists; Theorem 3.1 says it cannot be one local
   rectangle.
2. **A small absorber after a near-solution.**  Use rectangles on only
   \(o(N_H)\) duplicated top fibres.  Their middle duplication costs
   \(o(MN_H)=o(W)\).  This can repair at most the load moved by those
   absorbers; it cannot correct a linear initial shadow defect.

The exact remaining algebraic-combinatorial gate is therefore:

> construct a family of rank-isolating rectangle combinations whose two
> packet sides are separately 0--1 on the middle layer and whose support is
> large enough to span the required shadow correction.

The point-marginal lattice is no longer an issue.  Separate 0--1
realizability of the two packet sides is the issue.
