# Translation packets are generically multidepth-rainbow

Date: 2026-07-25

## 1. Result and relevance

Let \(n\) be prime, identify the coordinate set with \(\mathbb Z_n\), and
let \(\pi\) be an oriented cyclic order.  Write

\[
 I_i^{(r)}(\pi)=\{\pi_i,\pi_{i+1},\ldots,\pi_{i+r-1}\}
 \qquad(i\in\mathbb Z_n).
\]

Call \(\pi\) **translation-rainbow at rank \(r\)** when the \(n\) sets
\(I_i^{(r)}(\pi)\) lie in \(n\) distinct translation orbits of
\(\mathbb Z_n\).  Equivalently,

\[
 I_j^{(r)}(\pi)\ne I_i^{(r)}(\pi)+a
 \quad\text{for every }i\ne j\text{ and }a\in\mathbb Z_n.
\]

The theorem below gives an exact first-moment identity.

### Theorem 1 (exact translation-collision count)

Fix \(1\le r\le (n-1)/2\), and choose \(\pi\) uniformly among oriented
cyclic orders.  The expected number of ordered triples

\[
 (i,j,a),\qquad i\ne j,\quad a\ne0,
\]

for which

\[
 I_j^{(r)}(\pi)=I_i^{(r)}(\pi)+a
\]

is exactly

\[
 \boxed{\frac{n^2(n-1)}{\binom nr}}. \tag{1.1}
\]

Consequently

\[
 \boxed{
 \Pr(\pi\text{ is not translation-rainbow at rank }r)
 \le \frac{n^2(n-1)}{\binom nr}.}                 \tag{1.2}
\]

For a rank set \(R\subseteq\{1,\ldots,(n-1)/2\}\), the probability of a
failure at any rank in \(R\) is at most

\[
 \boxed{n^2(n-1)\sum_{r\in R}\binom nr^{-1}.}    \tag{1.3}
\]

In particular, for every central band

\[
 R=\{m-H,m-H+1,\ldots,m\},\qquad n=2m+1,quad H=o(m),
\]

almost every cyclic order is simultaneously translation-rainbow throughout
\(R\).  The same is then true in the complementary upper band.

This is a genuine simultaneous multidepth statement.  It says that the
within-packet clustering feared in a translation-orbit construction is not
generic: it is exponentially rare in the central band.

## 2. Cyclic run enumeration

Fix \(a\ne0\).  Since \(n\) is prime, the translation \(x\mapsto x+a\)
is one \(n\)-cycle.  For an \(r\)-set \(S\), let \(t_a(S)\) be the number
of runs of ones in its binary word along this cycle.  Equivalently,

\[
 t_a(S)=|S\setminus(S+a)|,
 \qquad |S\cap(S+a)|=r-t_a(S).                    \tag{2.1}
\]

### Lemma 2 (number of cyclic words with \(t\) runs)

For \(1\le t\le\min(r,n-r)\),

\[
 \boxed{
 \#\{S\in\tbinom{\mathbb Z_n}{r}:t_a(S)=t\}
 =\frac nt\binom{r-1}{t-1}\binom{n-r-1}{t-1}.}  \tag{2.2}
\]

#### Proof

Choose a distinguished start of a one-run.  There are \(n\) choices for
that coordinate, \(\binom{r-1}{t-1}\) compositions of the \(r\) ones into
\(t\) positive run lengths, and \(\binom{n-r-1}{t-1}\) compositions of
the zeros into the \(t\) positive intervening gaps.  Every binary cyclic
word with \(t\) runs is counted once for each of its \(t\) run starts.
Dividing by \(t\) proves (2.2).  \(\square\)

## 3. One pair of positional intervals

Fix distinct starts \(i,j\).  Let the two length-\(r\) positional blocks
have intersection size \(r-t\).  Conditional on

\[
 I_i^{(r)}(\pi)=S,
\]

the other interval is uniform among the

\[
 \binom rt\binom{n-r}{t}                          \tag{3.1}
\]

\(r\)-sets having intersection \(r-t\) with \(S\).  Indeed, the labels
on the \(r-t\) shared positions form a uniform \((r-t)\)-subset of \(S\),
and the labels on the \(t\) new positions form a uniform \(t\)-subset of
the complement.

Thus, for fixed \(a\ne0\), equality

\[
 I_j^{(r)}=I_i^{(r)}+a
\]

is possible precisely when \(t_a(S)=t\), and Lemma 2 gives

\[
\begin{aligned}
 \Pr(I_j^{(r)}=I_i^{(r)}+a)
 &={
 \frac nt\binom{r-1}{t-1}\binom{n-r-1}{t-1}
 \over
 \binom nr\binom rt\binom{n-r}{t}}\\[1mm]
 &=\boxed{\frac{nt}{r(n-r)\binom nr}}.            \tag{3.2}
\end{aligned}
\]

The cancellation uses

\[
 \frac{\binom{r-1}{t-1}}{\binom rt}=\frac tr,
 \qquad
 \frac{\binom{n-r-1}{t-1}}{\binom{n-r}{t}}=\frac t{n-r}.
\]

## 4. Summing over positional separations

For a cyclic separation \(d=j-i\), put

\[
 t(d)=r-|[i,i+r-1]\cap[j,j+r-1]|.
\]

Because \(r\le(n-1)/2\),

\[
 t(d)=\min(d,n-d,r),
\]

and the exact sum is

\[
\begin{aligned}
 \sum_{d=1}^{n-1}t(d)
 &=2\sum_{d=1}^{r-1}d+(n-2r+1)r\\
 &=r(n-r).                                        \tag{4.1}
\end{aligned}
\]

Now sum (3.2) over the \(n\) choices of \(i\), all nonzero separations
\(d\), and all \(n-1\) nonzero translations \(a\).  Equation (4.1)
gives

\[
 n(n-1)\frac{n}{r(n-r)\binom nr}
 \sum_{d=1}^{n-1}t(d)
 =\frac{n^2(n-1)}{\binom nr},
\]

which is (1.1).  Markov's inequality and a union bound prove
(1.2)--(1.3).  Complementation transfers the conclusion from rank \(r\)
to rank \(n-r\).  \(\square\)

## 5. Full translation packets

For a cyclic order \(\pi\), define its translation packet

\[
 \mathcal T(\pi)=\{\pi+a:a\in\mathbb Z_n\}.
\]

### Corollary 3 (one packet has no internal band collisions)

If \(\pi\) is translation-rainbow at rank \(r\), then the \(n^2\) sets

\[
 \{I_i^{(r)}(\pi)+a:i,a\in\mathbb Z_n\}
\]

are all distinct.  In particular, \(\mathcal T(\pi)\) consists of \(n\)
distinct cyclic orders modulo rotation, and it covers exactly \(n^2\)
distinct rank-\(r\) masks.

#### Proof

If

\[
 I_i^{(r)}+a=I_j^{(r)}+b,
\]

then \(I_j^{(r)}=I_i^{(r)}+(a-b)\).  Translation-rainbowness forces
\(i=j\), and freeness of the translation action on a nonempty proper
subset of \(\mathbb Z_n\) forces \(a=b\).  If two translated orders were
equal modulo rotation, their interval rows would give such a collision.
\(\square\)

Hence a generic translation packet is a perfect internal packing at every
central depth simultaneously.  Any remaining MWC obstruction in this
architecture is entirely a **cross-packet** selection obstruction.

After quotienting masks by translations, a good packet contains exactly
\(n\) distinct quotient vertices at every controlled rank.  A putative MWC
family made of full packets would choose

\[
 (1+o(1))\frac{W}{n^2}
\]

packets and would need to cover all but \(o(W/n)\) quotient masks across
the band.  The mean quotient load remains \(W/N_q\); packetization removes
the internal collision problem but does not by itself solve the integral
cross-packet near-cover problem.

## 6. Arithmetic-progression orders are the opposite extreme

Let

\[
 \pi_a=(0,a,2a,\ldots,(n-1)a),\qquad a\ne0.
\]

Then

\[
 I_i^{(r)}(\pi_a)=ia+\{0,a,\ldots,(r-1)a\}.
\]

Thus all \(n\) intervals of \(\pi_a\) lie in one translation orbit, and
translating the coordinate labels merely rotates the same cyclic order:

\[
 \pi_a+b=\operatorname{rot}_{b/a}(\pi_a).
\]

So the proposed AP packet is maximally degenerate, not rainbow.  Moreover
\(a\) and \(-a\) give the same interval family up to translation.  The
entire affine family of AP orders therefore covers at most

\[
 \frac{n(n-1)}2
\]

distinct masks at any fixed rank.  This is polynomial and hence
\(o(W)\) in the central band.

Therefore a construction consisting only of AP/AGL images cannot satisfy
MWC.  AP wreaths can at most be a negligible seed inside a completion whose
leading mass consists of non-AP, translation-rainbow packets.

## 7. A symmetric exact multicover with almost all packets good

Let \(F\) be any exact middle wreath factor, with \(|F|=W/n\).  Relabel it
by a uniformly random permutation \(\sigma\in S_n\), while keeping the
translation group on \(\mathbb Z_n\) fixed.  For every fixed row
\(C\in F\), the cyclic order \(\sigma C\) is uniform.  Hence, for a lower
rank band \(R\),

\[
 \mathbb E\#\{C\in F:\sigma C\text{ fails in }R\}
 \le \frac Wn\,n^2(n-1)\sum_{r\in R}\binom nr^{-1}.              \tag{7.1}
\]

For every fixed Gaussian window \(R=\{m-\lceil A\sqrt m\rceil,\ldots,m\}),
the right side is polynomial in \(n\), hence \(o(W/n)\).  Thus some
relabeling makes all but a negligible fraction of the factor rows
simultaneously packet-rainbow.

Taking the union of all translations of this relabelled factor gives an
exact \(n\)-fold middle cover resolved into full translation packets; all
but a negligible fraction of its packets have zero internal collision at
every rank in the fixed Gaussian window.  This does not choose the needed
one-fold subcover, but it removes within-packet algebraic clustering from
that remaining integrality problem.

## 8. Exact frontier left by the lemma

The translation-packet route is neither proved nor ruled out.  What is now
proved is sharper:

1. a generic packet is simultaneously perfect internally through the whole
   central band;
2. AP packets are maximally bad and contribute only a negligible number of
   masks;
3. the unresolved theorem is a quotient packet-selection theorem producing
   near-balanced cross-packet loads.

Thus any further algebraic attack should use AP orders only as boundary
data, and should put its main effort into a correlated selection or trade
system among generic translation-rainbow packets.

## 9. Odd-graph quotient and the zero-voltage cycle gate

There is a useful exact graph interpretation of the remaining middle-layer
packet selection.

Let

\[
 G=KG(n,m),\qquad n=2m+1,
\]

and let \(T=\mathbb Z_n\) act on its vertices by coordinate translation.
For prime \(n\), this action is free on every nonempty proper subset, so the
quotient multigraph

\[
 \overline G=G/T
\]

has

\[
 |V(\overline G)|=\frac1n\binom nm=\operatorname{Cat}_m              \tag{9.1}
\]

vertices.  Give quotient edges their natural \(T\)-voltage: after choosing
one representative of each vertex orbit, a lifted edge ends at a translate
of the chosen representative, and that translate is its voltage.

### Theorem 4 (good packets are zero-voltage quotient \(n\)-cycles)

There is a bijection, up to translation of the lifted packet, between:

1. translation packets of wreaths which are translation-rainbow at the
   middle rank; and
2. simple \(n\)-cycles in \(\overline G\) having total voltage zero.

Under this correspondence, disjoint quotient cycles lift to vertex-disjoint
translation packets in \(G\).

#### Proof

The middle intervals of a cyclic order form an \(n\)-cycle in the odd graph:
successive length-\(m\) windows are disjoint after taking the standard odd
step indexing, and every shortest odd cycle of \(KG(2m+1,m)\) is a wreath.

Take a translation-rainbow wreath \(C\).  Its \(n\) translated copies are
vertex-disjoint, because equality between a vertex of \(C+a\) and a vertex
of \(C+b\) would be a translation collision between two middle intervals
of \(C\).  Their quotient image is therefore a simple \(n\)-cycle.  One
lift is the closed cycle \(C\), so its total voltage is zero.

Conversely, let \(\overline C\) be a simple quotient \(n\)-cycle of total
voltage zero.  Its lift starting at any chosen representative closes after
\(n\) edges.  Translating that lift gives \(n\) closed \(n\)-cycles.  They
are pairwise vertex-disjoint because \(\overline C\) is simple and the
action on vertices is free.  Every lifted \(n\)-cycle is a shortest odd
cycle of \(G\), hence is the middle-window cycle of a cyclic coordinate
order.  The \(n\) lifts are exactly one full translation packet.  \(\square\)

### Corollary 5 (middle packet factorization gate)

A family of full translation packets covers every middle set at most once
if and only if the corresponding zero-voltage simple \(n\)-cycles are
vertex-disjoint in \(\overline G\).  It covers all but \(o(W)\) middle sets
if and only if those quotient cycles cover all but

\[
 o(W/n)=o(\operatorname{Cat}_m)
\]

quotient vertices.

There is a small unavoidable divisibility warning.  A quotient \(n\)-cycle
uses \(n\) vertices, while

\[
 |V(\overline G)|=\operatorname{Cat}_m
\]

need not be divisible by \(n\) (for prime \(n\), it is in fact nonzero
modulo \(n\)).  Thus an exact all-packet factor is arithmetically impossible
in those dimensions.  The remainder is fewer than \(n\) quotient vertices,
hence fewer than \(n^2=o(W)\) actual middle sets, and is irrelevant for MWC.

The algebraic middle-layer problem is therefore the following precise
near-decomposition:

> Pack zero-voltage simple \(n\)-cycles in
> \(KG(n,m)/\mathbb Z_n\) so that they miss only
> \(o(\operatorname{Cat}_m)\) quotient vertices.

For the full MWC gate, attach to every such quotient cycle its \(n\) lower
interval-orbit vertices at each controlled depth.  Theorem 1 shows that
almost every available quotient cycle has no repeated attached vertex at
any central depth.  What remains is to choose the quotient cycles so that
their attached vertices have near-complete **cross-cycle** coverage.

This separates three phenomena cleanly:

* AP wreaths project to degenerate one-vertex behavior and are negligible;
* generic wreath packets give simple zero-voltage cycles and perfect
  within-cycle shadow packing;
* the unresolved constant-one content is a multidepth near-factor theorem
  for these zero-voltage cycles in the quotient.

## 10. Explicit coordinates for the quotient odd graph

The quotient in Section 9 has a particularly simple algebraic model.  It
may be useful for constructing the required zero-voltage cycles.

Because \(n=2m+1\),

\[
 m^{-1}=-2\pmod n.                                 \tag{10.1}
\]

Every translation orbit of \(m\)-sets has a unique representative of
coordinate sum zero.  Indeed, translating an \(m\)-set by \(t\) changes
its sum by \(mt\), and \(m\) is invertible.  Put

\[
 \mathcal Z_m=\{A\in\tbinom{\mathbb Z_n}{m}:\sum_{x\in A}x=0\}.
\]

Then \(\mathcal Z_m\) is the vertex set of \(\overline G\).

For \(A\in\mathcal Z_m\) and \(y\notin A\), define

\[
 \boxed{
 T_y(A)=\bigl(\mathbb Z_n\setminus(A\cup\{y\})\bigr)-2y.}         \tag{10.2}
\]

### Proposition 6 (normalized-neighbor formula)

The \(m+1\) quotient neighbors of \(A\) are exactly the sets \(T_y(A)\),
for \(y\notin A\).  The directed quotient edge

\[
 A\longrightarrow T_y(A)
\]

has translation voltage \(2y\) under the convention that the lifted
neighbor is \(T_y(A)+2y\).  Its reverse is labelled \(-y\):

\[
 \boxed{T_{-y}(T_y(A))=A.}                         \tag{10.3}
\]

#### Proof

Every odd-graph neighbor of \(A\) is

\[
 D_y=\mathbb Z_n\setminus(A\cup\{y\}),\qquad y\notin A.
\]

Its coordinate sum is \(-y\).  Translating it by \(-2y\) changes its sum
by \(m(-2y)=y\), so its unique zero-sum representative is (10.2).
Equivalently, the actual lifted neighbor is \(T_y(A)+2y=D_y\), giving the
voltage.  Also

\[
 \mathbb Z_n\setminus T_y(A)
 =(A\cup\{y\})-2y=(A-2y)\cup\{-y\}.
\]

Thus \(-y\notin T_y(A)\), and deleting \(-y\) from this complement and
then translating by \(2y\) returns \(A\).  This is (10.3).  \(\square\)

Consequently a quotient walk is described by a sequence

\[
 A_{i+1}=T_{y_i}(A_i),\qquad y_i\notin A_i,         \tag{10.4}
\]

and its total voltage is

\[
 2\sum_i y_i\pmod n.                               \tag{10.5}
\]

The zero-voltage condition in Theorem 4 is therefore simply

\[
 \boxed{\sum_{i=0}^{n-1}y_i=0\pmod n.}             \tag{10.6}
\]

This converts the packet-factor problem into an explicit cycle-packing
problem on zero-sum subsets, with one omitted-coordinate label per step.

### Proposition 7 (the AP vertices are precisely the nonzero-voltage loops)

A quotient loop \(T_y(A)=A\), with \(y\ne0\), lifts to a
translation-stable AP wreath.  Conversely every translation-stable AP
wreath gives such a loop.  The labels \(y\) and \(-y\) give the two
orientations of the same loop, so there are \((n-1)/2\) underlying AP loop
vertices.

#### Proof

The loop equation is

\[
 \mathbb Z_n=A\ \dot\cup\ \{y\}\ \dot\cup\ (A+2y).              \tag{10.7}
\]

Along the cyclic order with step \(2y\), membership in \(A\) alternates
away from the unique omitted point \(y\).  Since the cycle length is odd,
there is a unique such \(m\)-set; it consists of every other point in that
step order.  Its translates are exactly the length-\(m\) intervals of an
arithmetic-progression cyclic order.  Reversing the loop replaces \(y\) by
\(-y\), producing the same interval family.  The converse follows by
reading the same alternating partition for an AP wreath.  \(\square\)

The quotient gate is now fully explicit: apart from the negligible AP
loops, one seeks disjoint simple trajectories of (10.4), each of length
\(n\), satisfying (10.6), and having near-complete attached lower-shadow
orbits at every controlled depth.

## 11. Two quotient odd steps are one normalized Johnson exchange

The maps (10.2) also expose a useful bridge back to Johnson geometry.

Suppose

\[
 B=T_y(A),\qquad C=T_z(B),
\]

and the second step is not the reversal of the first, so \(z\ne-y\).
The condition \(z\notin B\) is then equivalent to

\[
 p:=2y+z\in A.                                     \tag{11.1}
\]

A direct complement calculation gives

\[
\begin{aligned}
 C
 &=\left((A-2y)\cup\{-y\}\right)\setminus\{z\}-2z\\
 &=\boxed{
 \bigl(A-2(y+z)\bigr)\setminus\{-z\}
 \ \cup\ \{-y-2z\}.}                             \tag{11.2}
\end{aligned}
\]

Here \(-z\in A-2(y+z)\) is exactly (11.1).  Thus a nonbacktracking
two-step walk in the quotient odd graph is a one-element exchange after a
normalizing translation.  The backtracking case \(z=-y\) gives
\(T_{-y}T_y(A)=A\).

Consequently, if a quotient \(n=2m+1\) cycle is cut at one edge and its
remaining \(2m\) edges are paired, its even-indexed vertices form a
length-\(m\) path in this normalized quotient-Johnson graph; the two path
endpoints are joined by the unpaired odd-graph edge.  Conversely such a
path, together with compatible intermediate labels and a closing odd edge,
recovers the quotient cycle.

This suggests a concrete constructive line which is different from iid
packet selection: build a near-spanning system of long normalized-Johnson
paths, insist on the zero-voltage sum (10.6), and use their intermediate odd
vertices to form the packet cycles.  The exact shadow colors along these
paths are inherited from a single cyclic order, so this formulation keeps
the multidepth correlation rather than discarding it.

## 12. Every attached depth is an every-second intersection shadow

The multidepth data of a quotient cycle can be read directly from its lifted
middle vertices; the underlying coordinate order need not be reconstructed.

Let \(C\) be a lifted wreath, and index its odd-graph cycle as

\[
 M_i=I_{im}^{(m)}(\pi),\qquad i\in\mathbb Z_n.      \tag{12.1}
\]

Successive \(M_i\)'s are disjoint because their interval starts differ by
\(m\).  Since

\[
 -2m=1\pmod n,                                     \tag{12.2}
\]

we have

\[
 M_{i-2h}=I_{im+h}^{(m)}(\pi).                     \tag{12.3}
\]

### Proposition 8 (exact intersection/union shadow formula)

For every \(0\le q\le m-1\), the \(n\) lower intervals of length
\(m-q\) are exactly

\[
 \boxed{
 L_{i,q}:=\bigcap_{h=0}^{q}M_{i-2h}
 =I_{im+q}^{(m-q)}(\pi),\qquad i\in\mathbb Z_n,}   \tag{12.4}
\]

and the \(n\) upper intervals of length \(m+q\) are exactly

\[
 \boxed{
 U_{i,q}:=\bigcup_{h=0}^{q}M_{i-2h}
 =I_{im}^{(m+q)}(\pi),\qquad i\in\mathbb Z_n.}     \tag{12.5}
\]

#### Proof

By (12.3), the sets in the intersection or union are the \(q+1\)
length-\(m\) intervals with consecutive starts

\[
 im,im+1,\ldots,im+q.
\]

Their common intersection starts at \(im+q\) and has length \(m-q\);
their union starts at \(im\) and has length \(m+q\).  Multiplication by
\(m\) permutes \(\mathbb Z_n\), so varying \(i\) gives all cyclic starts.
\(\square\)

Now let

\[
 A_0\xrightarrow{y_0}A_1\xrightarrow{y_1}\cdots
 \xrightarrow{y_{n-1}}A_0
\]

be a zero-voltage quotient cycle from Section 10.  Choose \(s_0=0\) and

\[
 s_{i+1}=s_i+2y_i.                                 \tag{12.6}
\]

Then \(\widetilde A_i=A_i+s_i\) is a closed lifted wreath, and its attached
rank-\((m-q)\) quotient shadow is

\[
 \boxed{
 \left[
 \bigcap_{h=0}^{q}(A_{i-2h}+s_{i-2h})
 \right]_T,qquad i\in\mathbb Z_n.}                \tag{12.7}
\]

The global choice of \(s_0\) only translates every set and hence disappears
in the quotient.  Formula (12.7) is therefore intrinsic to the labelled
quotient cycle.

Accordingly, the surviving algebraic MWC theorem can be stated without any
cyclic-order language:

> Find almost disjoint zero-voltage \(n\)-cycles in the normalized odd
> quotient (10.2) such that, for every
> \(q\le\sqrt m\,\omega(m)\), the quotient intersection shadows (12.7)
> cover all but \(o(W/n)\) rank-\((m-q)\) translation orbits in total.

This is exactly the desired simultaneous complete-consecutive-intersection
condition, now attached to explicit algebraic trajectories rather than to
independent rankwise choices.

## 13. Why restricting the algebraic construction to prime dimensions is enough

The prime hypothesis in Theorem 1 is not an asymptotic loss if one succeeds
in proving the constant-one OR bound along odd primes.

### Proposition 9 (prime-subsequence transfer)

Assume

\[
 \nu(p)\le(1+o(1))W(p)                              \tag{13.1}
\]

as \(p\to\infty\) through odd primes.  Then

\[
 \nu(k)\le(1+o(1))W(k)                              \tag{13.2}
\]

for all integers \(k\).

#### Proof

Let \(p\le k\) be the largest prime below \(k\).  The prime number theorem
implies \(p/k\to1\).  Iterating the trimmed one-bit lift gives

\[
 \nu(k)\le2^{k-p}\nu(p).                            \tag{13.3}
\]

The central-binomial asymptotic gives

\[
 \frac{2^{k-p}W(p)}{W(k)}
 =(1+o(1))\sqrt{\frac{k}{p}}=1+o(1).                \tag{13.4}
\]

Combining (13.1)--(13.4) proves (13.2).  \(\square\)

Thus it is legitimate for the translation/finite-field line to solve MWC
only for prime \(n=2m+1\).  The ordinary lift then fills the gaps between
prime dimensions without changing the leading constant.

## 14. Exact equivariance is impossible for half the prime dimensions

One tempting strengthening of the packet route is to ask for an exact
middle wreath factor invariant under all coordinate translations.  There is
a sharp congruence obstruction.

### Theorem 10 (translation-invariant factor obstruction)

Let \(n=2m+1\ge7\) be prime.  If an exact middle wreath factor \(F\) is
invariant under \(\mathbb Z_n\)-translation, then \(m\) is even.  More
precisely:

* if \(m\) is even, \(F\) must contain exactly two translation-fixed AP
  wreaths;
* if \(m\) is odd, no translation-invariant exact factor exists.

#### Proof

Translation acts on the wreath rows of \(F\).  Since \(n\) is prime, every
row orbit has size \(1\) or \(n\).  A fixed wreath is necessarily an AP
wreath.  Indeed, if translating its cyclic order by \(1\) equals rotation
by \(j\), then

\[
 \pi_{k+j}=\pi_k+1.
\]

The nonzero step \(j\) generates \(\mathbb Z_n\), so \(\pi\) is an
arithmetic-progression order.  Reversal identifies slopes \(a\) and
\(-a\), and hence there are only

\[
 \frac{n-1}{2}=m                                      \tag{14.1}
\]

fixed AP wreaths available.

Let \(f\) be the number of fixed rows.  Since

\[
 |F|=\operatorname{Cat}_m,
\]

orbit counting gives

\[
 f\equiv\operatorname{Cat}_m\pmod n.                 \tag{14.2}
\]

Modulo the prime \(n\),

\[
\begin{aligned}
 \operatorname{Cat}_m
 &=\frac1{m+1}\binom{n-1}{m}\\
 &\equiv 2(-1)^m\pmod n,                              \tag{14.3}
\end{aligned}
\]

because \(\binom{n-1}{m}\equiv(-1)^m\) and
\(2(m+1)=n+1\equiv1\pmod n\).

If \(m\) is even, (14.2)--(14.3), together with \(0\le f\le m<n\), forces
\(f=2\).  If \(m\) is odd, it forces \(f=n-2>m\), contradicting (14.1).
\(\square\)

This rules out an exact equivariant factor for every prime
\(n\equiv3\pmod4\).  It does **not** rule out MWC packetization: one may
leave fewer than \(n\) unpacketized rows, which is polynomial and therefore
asymptotically negligible.  It does show that any successful packet proof
must be formulated as a near-equivariant factor with a small residue, not as
an exact invariant factor in all dimensions.

## 15. Iid packet selection still has the full \(\sqrt m\) barrier

Theorem 1 removes internal packet collisions, but it does not make random
selection viable.  There is a distribution-free lower bound.

Fix a rank \(r\), and let

\[
 M_r=\frac1n\binom nr
\]

be the number of translation orbits of rank-\(r\) masks.  Let a random full
translation packet be drawn from **any** distribution on cyclic orders.  For
a quotient target \(v\), let \(p_v\) be the probability that the packet
hits \(v\).  One packet has at most \(n\) distinct quotient interval targets,
so

\[
 \sum_{v=1}^{M_r}p_v\le n.                         \tag{15.1}
\]

### Theorem 11 (distribution-free iid packet barrier)

Choose \(b\) packets independently from this same distribution.  The
expected number of missed quotient targets is at least

\[
 \boxed{
 M_r\left(1-\frac n{M_r}\right)^b.}                \tag{15.2}
\]

Consequently, if

\[
 b=(1+o(1))\frac{W}{n^2},                          \tag{15.3}
\]

then the expected number of missed actual rank-\(r\) masks is at least

\[
 \boxed{
 N_r\exp\left(-(1+o(1))\frac W{N_r}\right).}       \tag{15.4}
\]

#### Proof

A quotient target \(v\) is missed by all \(b\) iid packets with probability
\((1-p_v)^b\).  The function \(p\mapsto(1-p)^b\) is convex for \(b\ge2\).
Jensen's inequality and (15.1) give

\[
\begin{aligned}
 \mathbb E[\#\text{ missed quotient targets}]
 &=\sum_v(1-p_v)^b\\
 &\ge M_r\left(1-\frac{\sum_vp_v}{M_r}\right)^b\\
 &\ge M_r\left(1-\frac n{M_r}\right)^b.
\end{aligned}
\]

Every missed quotient target represents \(n\) missed actual masks.  Under
(15.3),

\[
 \frac{bn}{M_r}=(1+o(1))\frac W{N_r},
\]

and \(n/M_r\) is exponentially small in the central band, proving (15.4).
\(\square\)

For \(r=m-q\) with \(0\le q\le A\sqrt m\), both \(N_r/W\) and
\(W/N_r\) stay between positive constants depending only on \(A\).
Therefore (15.4) is \(\Omega_A(W)\) at each of \(\Theta(\sqrt m)\)
depths.  Iid packet sampling consequently misses

\[
 \Omega_A(W\sqrt m)
\]

band masks in expectation, even if every sampled packet is internally
translation-rainbow at every depth.

Thus the packet route needs a resolvable/correlated quotient design.  Merely
replacing individual random wreaths by perfect internal translation packets
does not improve the global occupancy barrier at all.

## 16. A positive first-shadow near-2-factor

There is an exact integral construction satisfying the complete first-lower
shadow and common middle-degree requirements.  It does not yet impose the
tight-cycle/zero-voltage packaging.

### Theorem 12 (lower-rainbow Johnson near-2-factor)

Let \(n=2m+1\),

\[
 W=\binom nm,\qquad N_1=\binom n{m-1}=\frac{m}{m+2}W.
\]

There is a simple graph \(J^*\) on the vertex set
\(\binom{[n]}m\) such that:

1. every edge is a Johnson edge;
2. every \((m-1)\)-set occurs as the intersection color of exactly one
   edge;
3. every middle vertex has degree at most two; and
4. the total missing degree from two-regularity is exactly

\[
 \boxed{
 \sum_{X\in\binom{[n]}m}(2-d_{J^*}(X))
 =2(W-N_1)=\frac{4W}{m+2}=o(W).}                   \tag{16.1}
\]

In particular, all but at most \(4W/(m+2)\) middle vertices have degree
two.

#### Proof

Construct a flow network with a source, one node for each
\((m-1)\)-set \(S\), one node for each \(m\)-set \(X\), and a sink.  Give
the source-to-\(S\) arc fixed flow two.  For every inclusion \(S\subset X\),
put an arc of capacity one from \(S\) to \(X\).  Give every
\(X\)-to-sink arc capacity two.

There is a fractional flow of the required value: send

\[
 \frac{2}{m+2}                                      \tag{16.2}
\]

along every inclusion \(S\subset X\).  Each lower set has \(m+2\)
middle supersets, so it sends two units.  Each middle set has \(m\) facets,
so it receives

\[
 \frac{2m}{m+2}<2.                                 \tag{16.3}
\]

All capacities are integral.  The integral max-flow theorem therefore
supplies a full integral flow.  Each lower set \(S\) sends its two units to
two distinct middle supersets \(X_S,Y_S\), because the inclusion arcs have
capacity one.  Join \(X_S\) and \(Y_S\).  They are distinct Johnson-adjacent
\(m\)-sets and

\[
 X_S\cap Y_S=S.
\]

Different lower sets give different edges, since a Johnson edge has a
unique intersection.  The sink capacity makes every middle degree at most
two.  Finally \(J^*\) has exactly \(N_1\) edges, so its degree sum is
\(2N_1\), proving (16.1).  \(\square\)

Thus the complete first shadow admits, integrally and with common middle
ownership, a lower-rainbow graph which is two-regular outside only
\(O(W/m)\) degree slots.  Its components are paths, cycles, and isolated
vertices.

What remains for the positive packet program is sharply identifiable:

* modify only \(o(W)\) selected Johnson edges so that the components become
  length-\(n\) **tight** cycles (successive vertices are consecutive
  length-\(m\) windows of one coordinate order);
* arrange those cycles into the zero-voltage translation packets of
  Sections 9--12; and
* retain the analogous every-second intersection coverage at all fixed
  Gaussian depths.

Theorem 12 proves that at depth one there is no marginal, divisibility, or
middle-degree obstruction.  The remaining obstruction is genuinely the
ordered tight-cycle packaging, not first-shadow supply.

## 17. The first-shadow near-2-factor descends to the translation quotient

For prime \(n\), Theorem 12 has a quotient version which interfaces directly
with Sections 9--12.

Let \(\mathcal L\) be the translation orbits of \((m-1)\)-sets and
\(\mathcal M\) the translation orbits of \(m\)-sets.  Both actions are free,
so

\[
 |\mathcal L|=N_1/n,qquad |\mathcal M|=W/n.         \tag{17.1}
\]

Form the quotient inclusion **multigraph**.  Its edges are translation
orbits of flags \(S\subset X\).  Every lower vertex has degree \(m+2\) and
every middle vertex degree \(m\), counting parallel flag orbits.

Parallel flags at a lower vertex are extremely exceptional.

### Lemma 13 (only AP lower orbits have parallel quotient supersets)

If two distinct supersets \(X=S\cup\{x\}\) and \(Y=S\cup\{y\}\) belong to
the same translation orbit, then \(X\) is one cyclic interval in some
nonzero translation step \(a\), and \(S=X\cap(X+a)\) is an AP interval of
length \(m-1\).  Consequently at most

\[
 \frac{n-1}{2}=m                                      \tag{17.2}
\]

lower translation orbits have parallel quotient supersets.

#### Proof

Write \(Y=X+a\), with \(a\ne0\).  Since \(|X\cap Y|=m-1\),

\[
 |X\setminus(X+a)|=1.
\]

Along the \(a\)-cycle, this is the number of one-runs of the binary word of
\(X\).  Hence \(X\) has one run and is a cyclic AP interval.  Its
intersection with its one-step translate is the AP interval obtained by
deleting the two endpoints.  Slopes \(a\) and \(-a\) define the same
translation orbit, giving at most \((n-1)/2\) exceptional orbits.  \(\square\)

### Theorem 14 (quotient lower-rainbow near-2-factor)

After discarding at most \(m\) exceptional AP lower vertices, there is a
loopless quotient-Johnson multigraph \(\overline J^*\) on \(\mathcal M\)
such that:

1. every retained lower orbit is the intersection color of exactly one
   quotient Johnson edge;
2. every quotient middle vertex has degree at most two; and
3. its total degree defect is at most

\[
 \boxed{
 \frac{4W}{n(m+2)}+2m.}                            \tag{17.3}
\]

Thus it covers every first-lower translation orbit except \(O(n)\), and is
two-regular outside \(o(W/n)\) quotient degree slots.

#### Proof

Delete the exceptional lower vertices from the quotient inclusion
multigraph.  On the remaining graph there are no parallel flags.  Give each
remaining lower vertex demand two, each flag capacity one, and each middle
vertex capacity two.  Sending \(2/(m+2)\) along every remaining flag is a
feasible fractional flow; deletion of lower vertices only decreases the
middle loads from the bound \(2m/(m+2)<2\).  Integral max flow selects two
distinct quotient middle neighbors for every retained lower vertex.

Join those two neighbors.  Absence of parallel flags makes the two endpoints
distinct, and their representatives can be chosen as two actual supersets
of the same lower set, so this is a quotient Johnson edge with the prescribed
intersection orbit.  Different lower orbits can in principle give parallel
quotient Johnson edges; these are retained as distinct colored edges.
Middle capacity gives maximum degree two.  If \(d\le
m\) lower vertices were deleted, the degree defect equals

\[
 2\frac Wn-2\left(\frac{N_1}{n}-d\right)
 =\frac{4W}{n(m+2)}+2d,
\]

which proves (17.3).  \(\square\)

Every edge of \(\overline J^*\) has a canonical two-step realization in the
quotient odd graph: if representatives \(X,Y\) meet in \(S\), then

\[
 X\;--\;\bigl(\mathbb Z_n\setminus(X\cup Y)\bigr)\;--\;Y.          \tag{17.4}
\]

The possible collision of the intermediate vertices in (17.4) is exactly
the complementary-upper color collision: two selected lower colors may
produce the same union \(X\cup Y\).  Thus the next positive lemma needed for
the quotient cycle construction is now narrower still:

> Choose the integral flow in Theorem 14 so that all but \(o(W/n)\) of the
> intermediate vertices (equivalently, upper union colors) are distinct,
> and then splice the resulting quotient-Johnson path/cycle components into
> zero-voltage length-\(n\) cycles.

Theorem 14 supplies the exact lower shadow and near-two-regular middle
ledger; only the simultaneous upper-rainbow and ordered-cycle conditions
remain at depth one.

## 18. Fixed-uniformity matching gives both first shadows simultaneously

The upper-rainbow part of the preceding gate can be achieved up to \(o(W)\)
without any growing-uniformity theorem.

### Theorem 15 (two-sided-rainbow Johnson pseudofactor)

For \(n=2m+1\), there is a set \(E^*\) of \(W-o(W)\) Johnson edges on the
middle layer such that:

1. all lower intersection colors of \(E^*\) are distinct;
2. all upper union colors of \(E^*\) are distinct; and
3. every middle vertex is incident with at most two edges of \(E^*\).

Consequently all but \(o(W)\) lower colors, upper colors, and middle degree
slots are covered.

#### Proof

Create a four-uniform hypergraph \(\mathcal H\) with vertex parts

\[
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal U=\binom{[n]}{m+1},\qquad
 \mathcal M=\binom{[n]}m\times\{0,1\}.
\]

For every interval \(S\subset U\), where \(|S|=m-1\) and \(|U|=m+1\),
there are exactly two intermediate middle sets \(X,Y\).  For every clone
choice \(a,b\in\{0,1\}\), put in the hyperedge

\[
 \{S,U,(X,a),(Y,b)\}.                              \tag{18.1}
\]

A matching in \(\mathcal H\) is precisely a family of Johnson edges with
distinct lower colors, distinct upper colors, and middle degree at most two.

Put

\[
 D=2m(m+1).
\]

The vertex degrees are

\[
\begin{array}{c|c}
\text{part}&\text{degree}\\ \hline
\mathcal L&4\binom{m+2}{2}=2(m+2)(m+1)=(1+2/m)D,\\
\mathcal U&4\binom{m+1}{2}=D,\\
\mathcal M&2m(m+1)=D.
\end{array}                                        \tag{18.2}
\]

The maximum pair codegree is at most \(2(m+1)\).  Indeed, a lower color
and one middle clone have at most \(2(m+1)\) common edges; an upper color
and one middle clone have at most \(2m\); a lower-upper pair has at most
four; and two distinct middle clones have codegree at most one.  Hence

\[
 \Delta_2(\mathcal H)/D=O(1/m)=o(1).               \tag{18.3}
\]

The standard fixed-uniformity Pippenger--Spencer nibble theorem now applies:
a fixed-uniformity hypergraph whose vertex degrees are \((1+o(1))D\), with
\(D\to\infty\) and maximum pair codegree \(o(D)\), has a matching covering
all but \(o(|V|)\) vertices.  Thus \(\mathcal H\) has a matching of size
\(W-o(W)\).  Reading it through (18.1) proves all three assertions.
\(\square\)

This use of a matching theorem is at uniformity four, independent of \(m\).
It therefore avoids the growing-edge-size degeneration which invalidates
the economical-cover approaches to the full band.

## 19. Exact complement-folding criterion for a tight packet factor

Theorem 15 still produces an abstract degree-two Johnson pseudofactor.  The
remaining cyclic packaging can be stated as one local involutive condition.

For a Johnson edge \(e=XY\), put

\[
 d(e)=\mathbb Z_n\setminus(X\cup Y).                \tag{19.1}
\]

This is the middle vertex complementary to its upper color.  Given a
Johnson graph \(J\), replace every edge \(e=XY\) by the two odd-graph edges

\[
 Xd(e),\qquad Yd(e),                                \tag{19.2}
\]

and call the resulting odd-edge multigraph \(\mathcal O(J)\).

### Lemma 16 (complement folding)

Suppose \(J\) is two-regular and its upper colors are all distinct, so
\(e\mapsto d(e)\) is a bijection from \(E(J)\) to the middle vertices.
Then every edge of \(\mathcal O(J)\) has multiplicity two, and the doubled
edges form an odd-graph two-factor, if and only if for every
\(e=XY\), with \(d=d(e)\), the two \(J\)-edges incident with \(d\) have
complement values \(X\) and \(Y\):

\[
 \boxed{
 \{d(f):f\in E(J),\ d\in f\}=\{X,Y\}.}            \tag{19.3}
\]

#### Proof

The occurrence of the odd edge \(Xd\) contributed by \(e\) is doubled
precisely when an edge \(f\) incident with \(d\) has \(d(f)=X\).  The same
statement with \(Y\) handles the other half of (19.2).  Since \(d\) has
exactly two incident \(J\)-edges and the complement map is bijective,
these two requirements are exactly (19.3).  Applying this at every edge
shows that every odd edge occurs twice.  Conversely, double occurrence of
the two edges in (19.2) forces the two values in (19.3).  Dividing all
multiplicities by two leaves degree two at every vertex, hence an odd-graph
two-factor.  \(\square\)

For a genuine wreath with standard consecutive middle windows \(J_j\),

\[
 d(J_jJ_{j+1})=J_{j+m+1},                           \tag{19.4}
\]

and (19.3) holds identically.  Moreover the resulting odd two-factor has
all components of length \(n\).

Thus a positive depth-one packet theorem has been reduced to a familiar
design shape:

1. find a near-spanning two-sided-rainbow degree-two Johnson graph as in
   Theorem 15;
2. enforce the local complement-folding equations (19.3) on all but
   \(o(W)\) vertices; and
3. enforce that the folded odd two-factor has cycles of length \(n\) and,
   in the translation quotient, zero voltage.

The first item is now proved with fixed-uniformity machinery.  Items 2--3
are the genuinely ordered/resolvable part, and are concrete local-cycle
conditions rather than an undifferentiated shadow-balancing demand.

## 20. Equivalent rainbow-transition formulation in the odd graph

There is an even cleaner formulation of the remaining depth-one condition.
Let \(F\) be a two-factor of the odd graph, written as a successor
permutation \(f\).  At a middle vertex \(X\), its two cycle neighbors

\[
 P=f^{-1}(X),\qquad Q=f(X)
\]

are distinct \(m\)-subsets of the \((m+1)\)-set \(\mathbb Z_n\setminus X\).
Hence

\[
 \tau_F(X):=P\cap Q                                  \tag{20.1}
\]

has size \(m-1\), while

\[
 P\cup Q=\mathbb Z_n\setminus X.                    \tag{20.2}
\]

Thus the upper turn colors of **every** odd-graph two-factor are already
perfectly rainbow: they are simply the complements of the centers.  Only
the lower transition map (20.1) needs balancing.

At a fixed center \(X\), unordered pairs of incident odd-graph edges are in
bijection with \((m-1)\)-sets disjoint from \(X\).  Explicitly, if

\[
 S\subseteq\mathbb Z_n\setminus X,qquad |S|=m-1,
\]

and \((\mathbb Z_n\setminus X)\setminus S=\{a,b\}\), the corresponding
two neighbors are

\[
 S\cup\{a\},\qquad S\cup\{b\}.                     \tag{20.3}
\]

Therefore the exact depth-one packet problem is:

> Find a \(C_n\)-factor of \(KG(n,m)\) whose chosen transition at each
> vertex has labels (20.1) covering all but \(o(W)\) lower targets.

In the translation quotient, require in addition that the projected
\(n\)-cycles have zero voltage.  Theorem 15 proves that the transition
labels, centers, and endpoint degree slots admit an almost-perfect
fixed-uniformity matching.  Complement folding (19.3) is exactly the
condition that these independently selected local transitions are
reciprocal and hence form an actual two-factor.

This is a standard-looking **rainbow transition-system factor** problem:
the unresolved q=1 theorem is no longer a shadow-count statement, but an
integral cycle-factor theorem with one locally bounded transition color at
each vertex.

## 21. Every first-lower color fits in one near-spanning rainbow forest

There is also an exact acyclic selection, obtained from the matroidal Hall
condition.

### Theorem 17 (complete lower-rainbow Johnson forest)

The Johnson graph on \(\binom{[2m+1]}m\) contains a forest with exactly
one edge of every lower intersection color.  It has

\[
 N_1=\binom{2m+1}{m-1}=W-\frac{2W}{m+2}             \tag{21.1}
\]

edges and therefore exactly

\[
 \boxed{W-N_1=\frac{2W}{m+2}=o(W)}                 \tag{21.2}
\]

components, counting isolated vertices.

#### Proof

For every lower set \(S\), let \(E_S\) be the clique of Johnson edges
among its \(m+2\) middle supersets.  We seek one representative from every
\(E_S\), with all representatives independent in the graphic matroid.

By Rado's matroidal transversal theorem, this is possible if and only if,
for every family \(\mathcal A\) of lower colors,

\[
 r_{\rm gr}\left(\bigcup_{S\in\mathcal A}E_S\right)
 \ge |\mathcal A|.                                  \tag{21.3}
\]

Let the nonempty connected components of the union graph have vertex sets
\(V_1,\ldots,V_t\), and let \(\mathcal A_j\) consist of the colors whose
cliques lie in component \(j\).  A color clique is connected, so the
\(\mathcal A_j\)'s partition \(\mathcal A\).

Count inclusion flags between \(\mathcal A_j\) and \(V_j\).  Every lower
set has \(m+2\) middle supersets, while a middle set contains only \(m\)
lower facets.  Hence

\[
 (m+2)|\mathcal A_j|\le m|V_j|.                    \tag{21.4}
\]

Since \(\mathcal A_j\ne\varnothing\), integrality strengthens this to

\[
 |V_j|\ge|\mathcal A_j|+1.                         \tag{21.5}
\]

The graphic rank of component \(j\) is \(|V_j|-1\), and so

\[
 r_{\rm gr}\left(\bigcup_{S\in\mathcal A}E_S\right)
 =\sum_j(|V_j|-1)
 \ge\sum_j|\mathcal A_j|=|\mathcal A|.
\]

Rado's theorem supplies the desired forest.  Its component count follows
from \(|V|-|E|=W-N_1\).  \(\square\)

This is stronger than a mere near-cover at the first lower rank: every
lower target is used exactly once and the selected graph is already acyclic,
with only \(O(W/m)\) components.  What it does not control is vertex degree.
A high-degree tree is not a tight cyclic-order path, so the remaining
ordered theorem can equivalently be phrased as a **bounded-degree Rado
refinement**:

> choose the representatives in Theorem 17 so that deleting \(o(W)\) edges
> leaves paths which can be bundled into the normalized zero-voltage
> length-\(n\) trajectories of Sections 10--12.

Theorems 12, 15, and 17 now solve three different projections of the q=1
gate—degree, two-sided colors, and acyclicity.  The missing result is their
simultaneous resolvable intersection.

## 22. The saturating-cycle theorem merges degree two and connectivity

For the lower side alone, a published saturating-cycle theorem gives a much
stronger object than Theorems 12 and 17 separately.

Recall the theorem of Gregor--Mička--Mütze: the subgraph of a Boolean cube
induced by any consecutive interval of levels has a cycle saturating its
smaller bipartition class.  Apply it in \(B_{2m+1}\) to levels \(m-1,m\).

### Theorem 18 (one complete lower-rainbow Johnson cycle)

There is a simple Johnson cycle

\[
 X_0X_1\cdots X_{N_1-1}X_0                       \tag{22.1}
\]

on \(N_1\) distinct middle sets such that

\[
 \{X_i\cap X_{i+1}:i\in\mathbb Z_{N_1}\}
 =\binom{[2m+1]}{m-1}.                              \tag{22.2}
\]

Thus every first-lower color occurs exactly once, every used middle vertex
has degree two, and only

\[
 W-N_1=\frac{2W}{m+2}=o(W)                         \tag{22.3}
\]

middle vertices are omitted.

#### Proof

The saturating Boolean cycle has the form

\[
 S_0,X_0,S_1,X_1,\ldots,S_{N_1-1},X_{N_1-1},S_0,
\]

where the \(S_i\)'s are all \((m-1)\)-sets, the \(X_i\)'s are distinct
\(m\)-sets, and

\[
 S_i\subset X_i\supset S_{i+1}.
\]

Consequently \(X_i\) and \(X_{i+1}\) are distinct middle supersets of
\(S_{i+1}\), hence are Johnson adjacent and have intersection exactly
\(S_{i+1}\).  Projecting away the lower vertices gives (22.1)--(22.2).
\(\square\)

The omitted middle vertices can even be inserted into the color blocks if
one only wants a Hamilton Johnson cycle with complete lower support.  Assign
each omitted middle set \(Z\) to any facet \(S\subset Z\).  In the edge of
(22.1) colored \(S\), list all assigned supersets \(Z\) between its two old
endpoints.  Any two distinct \(m\)-supersets of \(S\) are Johnson adjacent
with intersection \(S\).  This yields a Hamilton cycle on all \(W\) middle
sets in which the edges of each lower color form one nonempty contiguous
block.  Only \(W-N_1=O(W/m)\) lower occurrences are repeats.

In fact the insertion can be made exactly floor-balanced.

### Proposition 18A (exact balanced first-lower Hamilton cycle)

For every \(m\ge6\), there is a Hamilton cycle on
\(\binom{[2m+1]}m\) whose rank-\((m-1)\) intersection multiplicities all
belong to \(\{1,2\}\).  Exactly

\[
 W-N_1=\frac{2W}{m+2}                              \tag{22.4}
\]

colors have multiplicity two.  Thus its first-lower load vector has balanced
overload zero.

#### Proof

Let \(\mathcal E\) be the family of middle sets omitted from (22.1), so
\(|\mathcal E|=d=2W/(m+2)\).  We claim that \(\mathcal E\) has a system of
distinct rank-\((m-1)\) facet representatives.  By Hall, it suffices to
show \(|\partial\mathcal A|\ge|\mathcal A|\) for every
\(\mathcal A\subseteq\mathcal E\).

Write \(|\mathcal A|=\binom{x}{m}\) in the generalized-binomial notation
used in the Lovasz form of Kruskal--Katona.  Since

\[
 d\le\binom{2m-1}{m}\qquad(m\ge6),                \tag{22.5}
\]

we have \(x\le2m-1\).  Kruskal--Katona gives

\[
 |\partial\mathcal A|\ge\binom{x}{m-1}
 =\binom{x}{m}\frac{m}{x-m+1}
 \ge\binom{x}{m}=|\mathcal A|.                    \tag{22.6}
\]

For completeness, (22.5) is equivalent to

\[
 \frac{2}{m+2}\frac{\binom{2m+1}{m}}
                         {\binom{2m-1}{m}}
 =\frac{4(2m+1)}{(m+1)(m+2)}\le1,                 \tag{22.7}
\]

which holds from \(m=6\) onward.  Hall therefore supplies distinct facets
\(S_Z\subset Z\), one for every \(Z\in\mathcal E\).

In the unique edge of (22.1) colored \(S_Z\), insert \(Z\) between its two
old endpoints.  Distinct representatives mean that no block receives more
than one inserted vertex.  The old single edge of color \(S_Z\) is replaced
by two edges of that same color, while every unchosen color remains on one
edge.  All omitted vertices are inserted exactly once, so the result is a
Hamilton cycle and has precisely the asserted multiplicities.  \(\square\)

This removes every marginal, divisibility, and overload defect at the first
lower shadow while retaining one global Johnson cycle.  What it still does
not impose is the FIFO/tight-window law required to split that Hamilton cycle
into zero-voltage length-\(n\) wreath packets.

The SDR argument applies at lower ranks as well.  Write

\[
 N_q=\binom{n}{m-q},\qquad r=m-q.                  \tag{22.8}
\]

### Proposition 18B (an exact one-sided balanced Hamilton tower)

If

\[
 N_q-N_{q+1}\le\binom{2r-1}{r},                    \tag{22.9}
\]

then \(J(n,r)\) has a Hamilton cycle whose rank-\((r-1)\) edge-color
multiplicities belong to \(\{1,2\}\), with exactly
\(N_q-N_{q+1}\) colors doubled.  In particular, for every fixed
\(\varepsilon>0\), (22.9) holds simultaneously for

\[
 0\le q\le\left(\frac12-\varepsilon\right)\log_2 m 
                                                               \tag{22.10}
\]

once \(m\) is sufficiently large.

#### Proof

Apply the saturating-cycle theorem to ranks \(r-1,r\).  Its projection uses
all \(N_{q+1}\) lower colors exactly once and omits a family
\(\mathcal E_q\) of \(N_q-N_{q+1}\) rank-\(r\) vertices.  Under (22.9), the
same Lovasz--Kruskal--Katona calculation as (22.6), with \(m\) replaced by
\(r\), proves Hall's condition for the facet graph of \(\mathcal E_q\).
Insert the omitted vertices into their distinct representative-color edges.
This gives the asserted Hamilton cycle and exact \(1/2\) histogram.

It remains to verify the uniform range.  Put \(a=2q+2\), so
\(2r-1=n-a\).  Uniformly for \(q=O(\log m)\),

\[
 \frac{\binom{2r-1}{r}}{N_q}
 =\prod_{j=0}^{a-1}\frac{n-r-j}{n-j}
 =4^{-(q+1)}(1+o(1)),                             \tag{22.11}
\]

whereas

\[
 \frac{N_q-N_{q+1}}{N_q}
 =\frac{2q+2}{m+q+2}.                              \tag{22.12}
\]

If (22.10) holds, the ratio of (22.12) to (22.11) is
\(O(\log m\,m^{-2\varepsilon})=o(1)\), proving (22.9).  \(\square\)

Proposition 18B gives an exact balanced Hamilton cycle separately at every
rank in a logarithmic tower.  It does **not** make those cycles compatible:
to braid adjacent ranks, the rank-\(r\) cycle must occur as the upper-color
order of the chosen rank-\((r-1)\) cycle.  That common-order constraint is
the substantive tower problem left open below.

There is an exact reason why upgrading the SDR insertion to a two-sided
insertion is tight rather than a routine Hall argument.  Suppose, in
addition, that the projected partial rank-\(r\) cycle already has distinct
upper colors.  For an omitted \(Z\), choosing the facet
\(S=Z\setminus\{z\}\) selects the base edge

\[
 X=S\cup\{x\},\qquad Y=S\cup\{y\}.                 \tag{22.13}
\]

Insertion deletes the old upper color \(S\cup\{x,y\}\) and creates the
pair

\[
 Z\cup\{x\},\qquad Z\cup\{y\}.                    \tag{22.14}
\]

At \(q=0\), there are \(d=W-N_1\) insertions.  The unchanged base edges
occupy \(N_1-d\) upper colors, leaving exactly

\[
 W-(N_1-d)=2d.                                    \tag{22.15}
\]

This is exactly the number of colors created in (22.14).  Hence an
upper-safe SDR must cover the available upper-color family **perfectly** by
the coupled pairs (22.14), while also using distinct facets \(S\).  After
complementing the upper colors, each pair consists of two odd-graph
neighbours of its center \(Z\).  Thus the two-sided insertion is a perfect
paired-transversal problem with no slack; ordinary facet Hall proves only
its first projection.

The same saturating cycle has an exact two-level interpretation.  Its lower
vertices form the Hamilton Johnson cycle

\[
 S_0S_1\cdots S_{N_1-1}S_0,                         \tag{22.16}
\]

because consecutive \(S_i,S_{i+1}\) are distinct facets of \(X_i\).  The
middle sets \(X_i=S_i\cup S_{i+1}\) are precisely its upper edge colors and
are all distinct.  Consequently

\[
 X_i\cap X_{i+1}=S_{i+1},qquad
 X_i\cap X_{i+1}\cap X_{i+2}=S_{i+1}\cap S_{i+2}.  \tag{22.17}
\]

Thus a saturating cycle whose lower Hamilton cycle (22.16) is also
lower-rainbow would solve the first two lower depths at once; equivalently,
the missing exact tower object at depth two is a two-sided-rainbow Hamilton
cycle on rank \(m-1\).  Proposition 18A is compatible with an approximate
version: inserting one omitted middle vertex changes only a bounded number
of triple windows, so all \(d=O(W/m)=o(W)\) SDR insertions change the
depth-two defect by at most \(O(d)=o(W)\).  Hence any saturating cycle whose
lower cycle has \(o(W)\) repeated/missing lower colors upgrades to a full
middle Hamilton cycle with exact balanced depth one and \(o(W)\) depth-two
defect.

For the packet programme, the unexpanded cycle (22.1) is the cleaner object:
it is already a single path/cycle design with exact first-lower rainbowness
and \(o(W)\) middle loss.  The remaining failure is now unmistakable.  A
general Johnson cycle is not a tight-window cycle, and cutting (22.1) into
length-\(n\) pieces does not make those pieces zero-voltage quotient wreaths.
The missing q=1 theorem is precisely a **tight saturating-cycle theorem**:

> obtain the saturation in (22.2) using a disjoint union of length-\(n\)
> tight Johnson cycles whose associated quotient odd cycles have zero
> voltage, up to \(o(W)\) omitted vertices/colors.

This is a substantially narrower positive gate than arbitrary balanced
shadow selection.

## 23. A verified depth-two lower braid

The first genuinely new consecutive-intersection identity can be obtained
by moving the rainbow forest down one rank.

### Lemma 19 (one-rank braid lift)

Let

\[
 S_0,S_1,\ldots,S_\ell
\]

be a path in \(J(n,r)\).  Put

\[
 C_i=S_{i-1}\cap S_i\quad(1\le i\le\ell),
 \qquad
 U_i=S_{i-1}\cup S_i.                              \tag{23.1}
\]

If consecutive lower colors are distinct and all upper colors are distinct,
then the upper-color path

\[
 U_1,U_2,\ldots,U_\ell                               \tag{23.2}
\]

satisfies

\[
 U_i\cap U_{i+1}=S_i,                               \tag{23.3}
\]

and

\[
 U_i\cap U_{i+1}\cap U_{i+2}=C_{i+1}.              \tag{23.4}
\]

#### Proof

Both \(U_i\) and \(U_{i+1}\) are \((r+1)\)-sets containing \(S_i\).
Distinctness of the upper colors makes them distinct facets over \(S_i\),
so their intersection is exactly \(S_i\).  Applying this twice gives

\[
 U_i\cap U_{i+1}\cap U_{i+2}
 =S_i\cap S_{i+1}=C_{i+1}.
\]

\(\square\)

There is a corresponding literal word: emit the lower edge colors
\(C_1,\ldots,C_\ell\), with one suitable endpoint facet at each end.  Adjacent
entries give the \(S_i\)'s and triple windows give the \(U_i\)'s, exactly as
in the facet-braid literalization.

### Theorem 20 (near-complete depth-two lower path system)

For \(n=2m+1\), there is a two-sided-rainbow linear forest in
\(J(n,m-1)\) with \(W-o(W)\) edges.  Its upper-color paths form a middle-layer
path system whose one-fold and two-fold consecutive intersections cover all
but \(o(W)\) sets in ranks \(m-1\) and \(m-2\), respectively.

#### Proof

We spell out the matching theorem application, because the ambient Boolean
layers have exponential size and therefore one must use the small-codegree
Delcourt--Postle corollary, rather than a version carrying an ambient-size
hypothesis.

Put \(r=m-1\) and \(k=n=2m+1\).  Form a four-partite four-graph \(G_m\)
with parts

\[
 \binom{[n]}{r-1},\qquad \binom{[n]}{r+1},\qquad
 \binom{[n]}r^{(0)},\qquad \binom{[n]}r^{(1)}.       \tag{23.5}
\]

For every \(A\in\binom{[n]}{r-1}\),
\(B\in\binom{[n]}{r+1}\) with \(A\subset B\), the interval
\([A,B]\) has two rank-\(r\) members \(X,Y\).  Insert the four hyperedges

\[
 \{A,B,X^{(a)},Y^{(b)}\},\qquad a,b\in\{0,1\}.       \tag{23.6}
\]

A matching in \(G_m\) projects to distinct Johnson edges, has maximum
projected degree two, and is rainbow in both its lower and upper colors.
The four vertex degrees are, respectively,

\[
 2(m+3)(m+2),\qquad 2m(m-1),\qquad
 2(m-1)(m+2),\qquad 2(m-1)(m+2).                    \tag{23.7}
\]

Indeed, a lower color chooses two elements from a complement of size
\(m+3\), an upper color chooses two of its \(m\) elements to delete, and a
fixed clone has \((m-1)(m+2)\) Johnson neighbours and two choices of the
other endpoint clone.  Hence, with

\[
 D=2(m+3)(m+2),                                    \tag{23.8}
\]

all degrees are \((1+O(1/m))D\).  The nonzero pair codegrees are at most

\[
 4,\quad 2(m+2),\quad 2(m-1),\quad 1               \tag{23.9}
\]

for a lower--upper pair, lower--clone pair, upper--clone pair, and adjacent
clone pair, respectively.  Thus \(\Delta_2(G_m)=O(m)=o(D)\).  Moreover,
counting through the lower part gives

\[
 |E(G_m)|=D\binom{n}{m-2}.                          \tag{23.10}
\]

Fix \(L\ge3\).  On the hyperedge set of \(G_m\), declare a size-\(i\)
conflict, \(3\le i\le L\), when those hyperedges are pairwise disjoint and
their projected Johnson edges form a simple \(i\)-cycle.  Let

\[
 Q=r(n-r)=(m-1)(m+2)                                \tag{23.11}
\]

be the Johnson degree.  A fixed lifted edge lies in at most
\(O_L(Q^{i-2})=O_L(D^{i-2})\) size-\(i\) conflicts: after orienting the
cycle, choose the first \(i-2\) free continuation edges, and then account
for only \(O_L(1)\) clone choices.  More generally, any prescribed
\(j\)-edge submatching extends to at most

\[
 O_L(Q^{i-j-1})=O_L(D^{i-j-1})                     \tag{23.12}
\]

size-\(i\) conflicts.  To see the exponent, its projected edges form a
bounded number \(s\ge1\) of paths; the \(i-j\) new edges fill \(s\)
nonempty gaps, and a gap of length \(t\) between fixed endpoints has at
most \(Q^{t-1}\) choices.  There are no size-two conflicts, so the two
additional conflict 2-codegrees vanish.

These estimates verify the fixed-uniformity Delcourt--Postle
small-codegree hypotheses, for example with \(\beta=1/3\):

\[
 \Delta_2(G_m)\le D^{1-\beta},\qquad
 \Delta_i=O_L(D^{i-2}),\qquad
 \Delta_{i,j}=O_L(D^{i-j-1})                       \tag{23.13}
\]

are stronger than the required bounds once \(m\) is large.  The theorem
therefore gives, for every fixed \(L\), a conflict-free matching of size

\[
 \frac{|E(G_m)|}{D}(1-o_L(1))
 =\binom{n}{m-2}-o_L(W)=W-o_L(W).                  \tag{23.14}
\]

Its projection has maximum degree two, both color maps are injective, and
every projected cycle has length greater than \(L\).  Delete one edge from
each projected cycle.  The cycles are vertex-disjoint, so this deletes at
most \(\binom{n}{m-1}/(L+1)\) edges.  First take \(m\to\infty\) for fixed
\(L\), and then choose \(L=L(m)\to\infty\) by the usual diagonal argument.
Adding unused rank-\((m-1)\) vertices as isolated vertices gives a spanning
two-sided-rainbow linear forest \(F_m\) with

\[
 e(F_m)=W-o(W),\qquad
 c(F_m)=\binom{n}{m-1}-e(F_m)=o(W).                \tag{23.15}
\]

Now orient every nontrivial path component
\(S_0,S_1,\ldots,S_\ell\), and list its upper colors
\(U_i=S_{i-1}\cup S_i\).  Lemma 19 says that adjacent intersections in
this upper-color path are the internal vertices \(S_i\), while triple
intersections are the internal lower edge colors \(C_{i+1}\).  Globally the
upper colors, lower colors, and forest vertices are all distinct.  Passing
from the forest to these windows loses at most one rank-\((m-1)\) target and
at most two rank-\((m-2)\) targets per nontrivial component.  By (23.15)
this is \(o(W)\), and the original matching already omitted only \(o(W)\)
colors at either rank.  Hence both claimed shadows have defect \(o(W)\).
\(\square\)

This proves a genuine depth-two lower braid with literal factorization.
It does not prove MWC: the construction is a family of linear paths rather
than zero-voltage tight \(n\)-cycles, and it does not simultaneously supply
the complementary upper half of a growing band at the same cost.  It does
show that the first nontrivial intersection depth itself has no fixed-depth
rainbow obstruction; the obstruction is the common cyclic packet resolution.

## 24. Every fixed central band has a literal tight-segment packing

The preceding depth-two forest can be extended, at every fixed depth, by
packing short **genuine tight segments** rather than individual Johnson
edges.  This does not reach a Gaussian-width band, because the matching
uniformity below depends on the depth.  It does prove that no fixed depth is
an obstruction, including literal factorability.

Fix integers \(h\ge0\) and \(b\ge1\).  They remain fixed while
\(m\to\infty\).  Put

\[
 n=2m+1,\qquad L=m+b+h.                           \tag{24.1}
\]

For an injective word

\[
 x=(x_0,x_1,\ldots,x_{L-1})\in[n]_{\ne}^{L},       \tag{24.2}
\]

and \(0\le i<b\), \(0\le s\le2h+1\), define

\[
 A_{i,s}(x)=\{x_i,x_{i+1},\ldots,
                 x_{i+m-h+s-1}\}.                 \tag{24.3}
\]

Thus \(|A_{i,s}|=m-h+s\).  Let \(\mathcal H_{m;b,h}\) be the
\(b(2h+2)\)-uniform, \((2h+2)\)-partite simple hypergraph whose vertices are

\[
 \mathcal R_s=\binom{[n]}{m-h+s}\quad(0\le s\le2h+1), 
                                                               \tag{24.4}
\]

and whose edges are the distinct set systems

\[
 e(x)=\{A_{i,s}(x):0\le i<b,\ 0\le s\le2h+1\}.     \tag{24.5}
\]

For fixed \(s\), the \(b\) sets in (24.5) are distinct: shifting the
position interval by one removes \(x_i\) and introduces a different
coordinate.  Hence every edge really has the asserted uniformity.

### Lemma 21 (the tight-segment hypergraph is pseudorandom)

For every fixed \(b,h\), the vertex degrees of
\(\mathcal H_{m;b,h}\) are \((1+O_{b,h}(1/m))D_m\), for some
\(D_m\to\infty\), and

\[
 \Delta_2(\mathcal H_{m;b,h})=O_{b,h}(D_m/m)=o(D_m). 
                                                               \tag{24.6}
\]

#### Proof

The symmetric group on \([n]\) acts transitively on every part
\(\mathcal R_s\) and preserves the atom family.  If \(E_m\) is the number
of simple atom edges, every vertex in part \(s\) therefore has degree

\[
 d_s=\frac{bE_m}{\binom{n}{m-h+s}}.                \tag{24.7}
\]

For fixed \(h\), all denominators in (24.7) are
\((1+O_h(1/m))W\).  Thus the degrees are asymptotically equal; they tend to
infinity because, even after fixing a target in one slot, an adjacent
entering boundary coordinate has \(m-O_{b,h}(1)\) choices producing distinct
atoms.

It remains to audit codegrees despite the fact that many ordered words can
describe the same simple atom.  First count labelled injective words.  A
slot \((i,s)\) corresponds to the position interval

\[
 P_{i,s}=[i,i+m-h+s-1].                            \tag{24.8}
\]

Condition on the event that the set of coordinates in a first position
interval \(P\), of size \(r\), is a prescribed set \(A\).  For a second
position interval \(Q\), of size \(t\), put \(u=|P\cap Q|\).  A prescribed
set \(B\) can occur in \(Q\) only when \(|A\cap B|=u\), and in that case
the exact conditional probability is

\[
 \frac{1}{\binom r u\binom{n-r}{t-u}}.             \tag{24.9}
\]

If the two slots are distinct, either their position intervals differ or
their ranks differ.  For distinct target vertices the identical-interval
case contributes zero.  In every nonzero remaining case, at least one
nontrivial choice in (24.9) has a ground set of size \(m-O_h(1)\).  Hence

\[
 \binom r u\binom{n-r}{t-u}\ge m-O_h(1).           \tag{24.10}
\]

There are only \(b^2(2h+2)^2\) choices of the two labelled slots, so the
labelled-word pair codegree is \(O_{b,h}(1/m)\) times a labelled-word
vertex degree.

Finally collapse to simple atoms.  The common position core of all intervals
in (24.5) is

\[
 [b-1,m-h-1],                                      \tag{24.11}
\]

whose size is \(m-h-b+1\).  Permuting the coordinates inside this core does
not change the atom.  Quotient the labelled words by these core
permutations.  After the quotient there are only
\(2b+2h-1\) boundary positions.  Given a simple atom, assigning its
\(b(2h+2)\) set vertices to the labelled slots and ordering those boundary
positions gives at most a constant \(K_{b,h}\) possible quotient words.
Thus collapsing the remaining parallel copies decreases a vertex degree by
at most \(K_{b,h}\), while it cannot increase a pair codegree.  The
labelled estimate consequently implies (24.6).  \(\square\)

### Theorem 22 (fixed-band literal theorem)

For every fixed \(h\), there is a nonzero contiguous-OR word of length

\[
 W+o(W)                                             \tag{24.12}
\]

covering every set in all ranks

\[
 m-h,m-h+1,\ldots,m+h+1.                           \tag{24.13}
\]

#### Proof

For fixed \(b,h\), Lemma 21 and the classical fixed-uniformity
Pippenger--Frankl--Rödl almost-perfect matching theorem give a matching
\(\mathcal M_{m;b,h}\) covering all but \(o_{b,h}(W)\) vertices of
\(\mathcal H_{m;b,h}\).  Since

\[
 \sum_{s=0}^{2h+1}|\mathcal R_s|
  =(2h+2)W(1+O_h(1/m)),                            \tag{24.14}
\]

and every atom contains \(b\) vertices from each part,

\[
 |\mathcal M_{m;b,h}|=\frac{W}{b}+o_{b,h}(W).       \tag{24.15}
\]

For each selected atom choose one representing word \(x\), and emit the
\(b+2h+1\) nonempty base windows

\[
 E_j(x)=\{x_j,x_{j+1},\ldots,x_{j+m-h-1}\},
 \qquad 0\le j<b+2h+1.                             \tag{24.16}
\]

For every matched vertex (24.3), the exact contiguous-union identity is

\[
 E_i(x)\cup E_{i+1}(x)\cup\cdots\cup E_{i+s}(x)
   =A_{i,s}(x).                                    \tag{24.17}
\]

Thus concatenating the atom words covers all but \(o_{b,h}(W)\) targets in
every rank in (24.13).  Append every missing target literally.  The total
length is at most

\[
 (b+2h+1)|\mathcal M_{m;b,h}|+o_{b,h}(W)
 =\left(1+\frac{2h+1}{b}+o_{b,h}(1)\right)W.        \tag{24.18}
\]

Now let \(b\to\infty\) by diagonalization.  At the stage using a fixed
value of \(b\), take \(m\) far enough that the total matching and repair
error, after multiplication by the block length \(b+2h+1\), is at most
\(W/b\).  Then increase \(b=b(m)\) arbitrarily slowly.  Both \((2h+1)/b\) and
the full error term tend to zero, proving (24.12).  \(\square\)

The same two-parameter diagonalization permits a depth
\(h=h(m)\to\infty\) growing arbitrarily slowly: at stage \(j\), use the
fixed theorem with \(h=j\) and, say, \(b=j^3\), after increasing the next
dimension threshold enough to make the total emitted matching and repair
error at most \(W/j\).
This gives a literal \(W+o(W)\) word for some unbounded central band.  It
does not give the Gaussian scale \(h\asymp\sqrt m\): reaching that scale
requires a uniform growing-uniformity matching theorem or the common
zero-voltage packet resolution targeted in Sections 10--12.

## 25. The complement-paired packet hypergraph has vanishing local codegree

The short atoms in Section 24 can be extended to full cyclic orders, but a
full order has growing edge size.  The following calculation shows that no
new *local* overlap obstruction appears.  The only deterministic large
codegree comes from complements, and disappears after pairing them.

For \(0\le q\le H\), let \(\mathcal P_q\) have one vertex

\[
 [A]=\{A,A^c\}                                      \tag{25.1}
\]

for every \(A\in\binom{[n]}{m-q}\).  Thus
\(|\mathcal P_q|=N_q=\binom{n}{m-q}\).  Define the packet hypergraph
\(\mathcal P_{m,H}\) by taking one edge for every oriented cyclic order
modulo rotation.  Its vertices in part \(q\) are the \(n\) complementary
pairs whose lower member is a cyclic interval of length \(m-q\).  Hence
every packet edge contains exactly \(n\) vertices from every part.

### Lemma 23 (exact degrees and pair-codegree bound)

Assume \(H\le m/3\).  Every vertex of part \(q\) has degree

\[
 d_q=(m-q)!(m+q+1)!=\frac{n!}{N_q}.                \tag{25.2}
\]

For two distinct packet vertices \(v,w\), with \(v\in\mathcal P_q\),

\[
 \operatorname{codeg}(v,w)
 \le \frac{2+o(1)}{m-H}\,d_q.                      \tag{25.3}
\]

In particular, uniformly for \(q,q'\le A\sqrt m\),

\[
 \frac{\operatorname{codeg}(v,w)}
      {\min(d_q,d_{q'})}=O_A(1/m),                 \tag{25.4}
\]

while

\[
 \frac{d_q}{d_0}
 =\frac{W}{N_q}
 =\exp\left(\frac{q(q+1)}m+O_A(m^{-1/2})\right).   \tag{25.5}
\]

#### Proof

There are \((n-1)!\) oriented cyclic orders modulo rotation.  A fixed
\(r\)-set is an interval in exactly

\[
 r!(n-r)!=\frac{n!}{\binom nr}                     \tag{25.6}
\]

of them: treat the set as one circular block and order its elements
internally.  This proves (25.2); a set is an interval if and only if its
complement is, so pairing does not change the count.

Condition on a fixed lower representative \(A\), \(|A|=r\), being an
interval.  Its internal linear order and the internal linear order of its
complement are uniform.  Let \(B\), \(|B|=s\), be the lower representative
of a distinct packet vertex.  Both \(r,s\) lie in \([m-H,m]\).

If \(B\subsetneq A\), put \(d=r-s\).  Then \(B\) must be one consecutive
subblock of the random internal order of \(A\), and

\[
 \Pr(B\text{ is an interval}\mid A\text{ is})
 =\frac{d+1}{\binom r d}\le\frac2{m-H}.             \tag{25.7}
\]

The same estimate applies when \(A\subsetneq B\), by describing the
complement of \(B\) as a consecutive subblock of \(A^c\).  If
\(A\cap B=\varnothing\), then \(B\) is a proper consecutive subblock of
\(A^c\), and the identical estimate applies there.  (The equality
\(B=A^c\) cannot occur for two lower representatives, since both have size
at most \(m<n/2\).)

It remains to consider proper overlap.  Put

\[
 a=|A\cap B|,\qquad c=|B\setminus A|.               \tag{25.8}
\]

Here \(1\le a\le r-1\) and \(1\le c\le n-r-1\).  For \(B\) to be a
cyclic interval, \(A\cap B\) must occupy one end of the internal order of
\(A\), while \(B\setminus A\) must occupy the adjacent end of the internal
order of \(A^c\).  There are at most two choices of side, so

\[
 \Pr(B\text{ is an interval}\mid A\text{ is})
 \le\frac{2}{\binom r a\binom{n-r}c}
 \le\frac{2}{r(n-r)}.                             \tag{25.9}
\]

Equations (25.7)--(25.9) prove (25.3).  Applying the same inequality with
the two vertices reversed gives (25.4), because all relevant sizes are
\(m+O_A(\sqrt m)\).  Finally (25.5) is the standard product expansion for
\(W/N_q\).  \(\square\)

For fixed \(H\), Lemma 23 is compatible with the short-atom matching proof
of Section 24.  For \(H=A\sqrt m\), the natural balanced-clone version has
bounded capacities \(c_q\le e^{A^2+o(1)}\), and still has relative local
codegree \(O_A(1/m)\); however, one full packet edge contains
\(n(H+1)=\Theta_A(m^{3/2})\) paired slots.  A near-perfect integral matching
or absorber at that growing uniformity is precisely the bounded-capacity
cyclic-alignment gate.  Lemma 23 does not supply that global selection, but
it rules out local packet overlap as the source of the missing Gaussian
theorem.
