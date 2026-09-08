# Moment-coded cores and Kirkman classes pack a constant fraction of rank-two queue source frames

**Date:** 2026-08-07  
**Method:** a two-power-sum constant-weight code and resolvable Steiner
triple systems  
**Status:** unconditional global rank-\(s\)-target packing theorem. It
constructs pairwise source-target-disjoint legal rank-two queue frames with
more than enough endpoint capacity for the PBBS reset. It does not choose
owner-disjoint queue rings inside those frames.

## 0. Statement

Use

\[
n=2m+1,\qquad p=d+1,\qquad c=m-2p,
\qquad s=c+2=m-2d.
\tag{0.1}
\]

A **rank-two source frame** consists of a core

\[
K\in{[n]\choose c}
\tag{0.2}

and \(p\) pairwise disjoint triples

\[
T_1,\ldots,T_p\subseteq[n]\setminus K.
\tag{0.3}

Its rank-\(s\) source inventory is

\[
\Sigma(K;T_1,\ldots,T_p)
=\left\{
K\cup(T_i\setminus\{x\}):1\le i\le p,\ x\in T_i
\right\}.
\tag{0.4}

It contains exactly \(3p\) targets. Every such frame supports a literal
rank-two block-queue ring: order the phases \(T_i\), choose a cyclic
omission order on each triple, and use the permanent core \(K\).

### Theorem 0.1 (constant-density source-frame packing)

There is a family \(\mathscr F\) of rank-two source frames whose inventories
(0.4) are pairwise disjoint and satisfy

\[
\boxed{
\left|\bigcup_{F\in\mathscr F}\Sigma(F)\right|
\ge\left(\frac1{32}-o(1)\right){n\choose s}.}
\tag{0.5}
\]

Equivalently,

\[
\boxed{
|\mathscr F|
\ge\left(\frac1{32}-o(1)\right)\frac1{3p}{n\choose s}.}
\tag{0.6}

At triangular depth,

\[
\frac{{n\choose s}}{{n\choose m}}\longrightarrow e^{-\pi}.
\tag{0.7}

Hence these source-disjoint frames contain

\[
\left(\frac{e^{-\pi}}{32}-o(1)\right)W
\tag{0.8}

endpoint source targets, where \(W={n\choose m}\). Since

\[
\theta=4\sum_{a\ge1}e^{-4\pi a^2}<10^{-4}
<\frac{e^{-\pi}}{32},
\tag{0.9}

the rank-\(s\) target row has a fixed integral safety factor exceeding ten.

## 1. A distance-three family of cores

Choose a prime \(Q\) with

\[
n<Q<2n,
\tag{1.1}

which exists by Bertrand's postulate, and label the coordinates of \([n]\)
by distinct elements of \(\mathbb F_Q\).

Colour every \(c\)-set \(K\) by

\[
\chi(K)=
\left(\sum_{x\in K}x,\ \sum_{x\in K}x^2\right)
\in\mathbb F_Q^2.
\tag{1.2}

Let \(\mathcal K\) be a largest colour class. Then

\[
|\mathcal K|\ge\frac1{Q^2}{n\choose c}.
\tag{1.3}

### Lemma 1.1 (moment colour implies Johnson distance at least three)

Distinct \(K,K'\in\mathcal K\) satisfy

\[
d_J(K,K')\ge3.
\tag{1.4}

#### Proof

At Johnson distance one, write

\[
K'=K-\{a\}+\{b\}.
\]

Equality of the first moments gives \(a=b\), contradicting
\(K\ne K'\).

At distance two, write

\[
K'=K-\{a,b\}+\{u,v\}.
\]

The two moment equations give

\[
a+b=u+v,
\qquad a^2+b^2=u^2+v^2.
\tag{1.5}

Because \(Q>n\ge3\), the field has odd characteristic, and (1.5)
determines the products:

\[
ab=\frac{(a+b)^2-(a^2+b^2)}2=uv.
\]

Thus \(\{a,b\}\) and \(\{u,v\}\) are the roots of the same quadratic
polynomial, so they are equal as unordered pairs. Again \(K=K'\), a
contradiction. \(\square\)

### Corollary 1.2 (disjoint rank-\(s\) upper shadows)

The families

\[
\mathcal U(K)=
\{K\cup e:e\in{[n]\setminus K\choose2}\},
\qquad K\in\mathcal K,
\tag{1.6}

are pairwise disjoint.

#### Proof

If a rank-\(c+2\) set contained both \(K\) and \(K'\), then
\(|K\cup K'|\le c+2\), so \(d_J(K,K')\le2\), contrary to Lemma 1.1.
\(\square\)

## 2. Resolving one upper shadow into queue frames

Fix \(K\in\mathcal K\), and put

\[
U=[n]\setminus K,
\qquad N=|U|=n-c=m+2p+1.
\tag{2.1}

Choose \(N'\le N\) with

\[
N'\equiv3\pmod6,
\qquad N-N'\le5,
\tag{2.2}

and choose a subset \(U'\subseteq U\) of size \(N'\).

By the Kirkman triple-system theorem, the pairs of \(U'\) can be
partitioned into triples, and the triples can be partitioned further into
parallel classes

\[
\mathcal P_1,\ldots,\mathcal P_{(N'-1)/2},
\tag{2.3}

each of which partitions \(U'\) into \(N'/3\) vertex-disjoint triples.

Inside every parallel class, group the triples into batches of exactly
\(p\), discarding fewer than \(p\) triples from that class. Every batch is
a legal source frame over \(K\), because its \(p\) triples are pairwise
disjoint.

### Lemma 2.1 (asymptotically complete packing in one upper shadow)

The frames obtained above have pairwise disjoint inventories and cover

\[
\left(1-o(1)\right){N\choose2}
\tag{2.4}

members of \(\mathcal U(K)\).

#### Proof

In a Steiner triple system, every pair of \(U'\) lies in exactly one
triple. Thus all triangle-edge targets used by different batches are
distinct.

At most \(p-1\) triples are discarded from each of \((N'-1)/2\) parallel
classes, costing \(O(pN)\) pairs. The \(N-N'=O(1)\) unused vertices cost
only \(O(N)\) further pairs. Since \(p=o(N)\), the total loss is
\(o(N^2)\), proving (2.4). \(\square\)

## 3. Global count

Apply Lemma 2.1 independently for every \(K\in\mathcal K\). Corollary 1.2
ensures that inventories from different cores are disjoint. Therefore the
number of covered rank-\(s\) targets is at least

\[
(1-o(1))|\mathcal K|{n-c\choose2}
\ge(1-o(1))\frac1{Q^2}{n\choose c}{n-c\choose2}.
\tag{3.1}

The exact incidence identity

\[
{n\choose c}{n-c\choose2}
={n\choose c+2}{c+2\choose2}
={n\choose s}{s\choose2}
\tag{3.2}

turns (3.1) into

\[
(1-o(1)){n\choose s}\frac{{s\choose2}}{Q^2}.
\tag{3.3}

Now \(s/n\to1/2\), while \(Q<2n\). Hence

\[
\frac{{s\choose2}}{Q^2}
\ge\frac1{32}-o(1).
\tag{3.4}

This proves Theorem 0.1. \(\square\)

## 4. Exact remaining correlation

Theorem 0.1 closes the rank-\(s\) source-target row independently:

- every frame is literal and supports many translated queue rings;
- no two selected frames share a rank-\(s\) source target;
- the integral frame supply exceeds the required PBBS endpoint density by
  a fixed factor.

It does not close owner disjointness. A frame has a full owner fibre of
size \(3^p\), and one must choose one translated \(3p\)-cycle from enough
of these fibres so that the chosen cycles are globally owner-disjoint.
The core distance-three property ensures disjoint rank-\(s\) shadows, but
does not ensure disjoint owner fibres: an \(m\)-set can contain two
distance-three \(c\)-cores.

Combined with
`MATH_THEOREM_RANK2_QUEUE_CANONICAL_TRIPLE_FIBRES_AND_ONE_THIRD_OWNER_PACKING_20260807.md`,
the two hard marginals are now both integral:

\[
\begin{array}{c|c}
\text{resource}&\text{proved integral supply}\\ \hline
\text{rank-}m\text{ owners}&(1/3-o(1))W,\\
\text{rank-}s\text{ source targets}&
(e^{-\pi}/32-o(1))W.
\end{array}
\tag{4.1}
\]

The missing theorem is their common refinement:

> **Owner--source frame recoupling.** From a target-disjoint family of
> legal frames of size \(\Omega(W/p)\), retain
> \((\theta+o(1))W/(3p)\) frames and choose one queue-ring translate in
> each so that all \((\theta+o(1))W\) owners are distinct.

Only after this recoupling do the higher marked depths and physical fusion
enter. No claim of \(B(k)+O(1)\) is made here.

## 5. Exact recoupling configuration hypergraph

For a frame \(F\in\mathscr F\), identify its full owner fibre with
\(G_F=\mathbb F_3^p\), and let

\[
\mathcal A=
\{q\mathbf1+P_j:q\in\mathbb F_3,\ 0\le j<p\}
\tag{5.1}
\]

be the \(3p\)-state queue cycle. Its translation stabilizer is precisely
\(\langle\mathbf1\rangle\), so the frame has

\[
\left|\mathcal R(F)\right|=3^{p-1}
\tag{5.2}

distinct translated queue rings.

Define \(\mathcal G_{\rm rec}(\mathscr F)\) on the disjoint vertex set

\[
{[n]\choose m}\ \mathbin{\dot\cup}\ \mathscr F
\tag{5.3}

by putting in the \((3p+1)\)-edge

\[
\{F\}\cup R
\tag{5.4}

for every \(F\in\mathscr F\) and \(R\in\mathcal R(F)\).

### Proposition 5.1 (exact equivalence)

A matching of size \(H\) in \(\mathcal G_{\rm rec}(\mathscr F)\) is
equivalent to a choice of \(H\) source-target-disjoint frames and one
queue-ring translate in each, with all \(3pH\) owners distinct.

Moreover,

\[
d_{\mathcal G}(F)=3^{p-1},
\qquad
d_{\mathcal G}(X)=p\,d_{\rm fib}(X),
\tag{5.5}

where

\[
d_{\rm fib}(X)=
|\{F\in\mathscr F:X\in G_F\}|.
\tag{5.6}

For a fixed frame \(F\) and owner \(X\in G_F\), exactly \(p\) translated
rings of \(F\) contain \(X\).

#### Proof

The frame vertex in (5.4) enforces at most one ring from each frame, while
the owner vertices enforce owner disjointness. Source-target disjointness
is already built into \(\mathscr F\) by Theorem 0.1. This proves the first
statement.

There are \(3^{p-1}\) distinct translates because
\(\mathcal A+\mathbf1=\mathcal A\). To see that the stabilizer is no
larger, recall that the distance-one graph induced by \(\mathcal A\) is
exactly the cycle \(C_{3p}\). A nonzero translation has order three and,
if it stabilizes \(\mathcal A\), induces a fixed-point-free order-three
automorphism of this cycle. It must therefore rotate the cycle by \(p\) or
\(2p\) steps. Those two rotations are exactly translation by
\(\mathbf1\) and \(2\mathbf1\). Thus the stabilizer is
\(\langle\mathbf1\rangle\).

Translation acts transitively on the \(3^p\) owner states.
Double-counting incidences between the
\(3^{p-1}\) rings and their \(3p\) states shows that every state belongs to

\[
\frac{3^{p-1}\,3p}{3^p}=p
\]

rings. Summing over the frames containing \(X\) gives (5.5). \(\square\)

Thus the remaining rank-\(s\) recoupling theorem has the completely literal
form

\[
\boxed{
\nu\bigl(\mathcal G_{\rm rec}(\mathscr F)\bigr)
\ge(\theta+o(1))\frac{W}{3p}.}
\tag{5.7}
\]

The unequal degree rows in (5.5), rather than any remaining scalar target
shortage, are the precise obstacle to applying a black-box regular
hypergraph matching theorem.
