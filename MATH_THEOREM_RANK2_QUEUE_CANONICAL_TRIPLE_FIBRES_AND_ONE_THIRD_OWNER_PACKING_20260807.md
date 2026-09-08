# Canonical triple fibres give a deterministic one-third owner packing by rank-two queues

**Date:** 2026-08-07  
**Method:** canonical singleton-triple fibres and a linear quotient code in
\(\mathbb F_3^p\)  
**Status:** unconditional global owner-packing theorem. It closes the
owner-disjoint rank-two queue-ring row at density
\(1/3-o(1)\), far above the PBBS reset density \(\theta\). It does not
select the marked lower targets or fuse the chosen rings into one physical
chronology.

## 0. The theorem

Use

\[
n=2m+1,\qquad p=d+1,\qquad \ell=3p,
\tag{0.1}
\]

and assume only \(p=o(m)\). Let \(\mathcal H_Q\) be the hypergraph on the
rank-\(m\) owner layer

\[
\mathcal V={{[n]}\choose m}
\tag{0.2}
\]

whose edges are the \(\ell\) owners of coordinate-labelled copies of the
rank-two block queue from
`MATH_THEOREM_RANK2_BLOCK_QUEUE_FLAT_OWNER_RESET_20260807.md`.

### Theorem 0.1 (one-third queue owner packing)

There is a matching \(\mathcal M\subseteq\mathcal H_Q\) such that

\[
\boxed{
\left|\bigcup_{E\in\mathcal M}E\right|
\ge\left(\frac13-o(1)\right){n\choose m}.}
\tag{0.3}
\]

Equivalently,

\[
\boxed{
|\mathcal M|\ge
\left(\frac13-o(1)\right)\frac1{3p}{n\choose m}.}
\tag{0.4}
\]

At the triangular deadline, the required reset density is

\[
\theta=4\sum_{a\ge1}e^{-4\pi a^2}<10^{-4}.
\tag{0.5}
\]

Therefore the owner row has more than a factor \(3000\) of asymptotic
integral slack:

\[
\boxed{
\left|\bigcup_{E\in\mathcal M}E\right|
>(\theta+o(1))W,
\qquad W={n\choose m}.}
\tag{0.6}
\]

The proof is deterministic after one fixed partition of \([n]\) into
triples. No nibble or growing-uniformity matching theorem is used.

## 1. Complement form of a queue owner

Partition the queue bank into \(p\) triples

\[
T_1,\ldots,T_p,
\tag{1.1}
\]

and let \(K\) be the permanent owner core of size \(m-2p\). Put

\[
A=[n]\setminus\left(K\cup\bigcup_{i=1}^pT_i\right).
\tag{1.2}
\]

Then

\[
|A|=n-(m-2p)-3p=m+1-p.
\tag{1.3}
\]

Every owner in the ring contains exactly two coordinates of each \(T_i\).
Hence its complement has the form

\[
Y=A\cup\{y_1,\ldots,y_p\},
\qquad y_i\in T_i.
\tag{1.4}
\]

Conversely, the complement of every set in (1.4) is a rank-\(m\) owner
over the core \(K\) and the bank \(T_1\dot\cup\cdots\dot\cup T_p\).
Thus the complete local owner fibre is naturally

\[
\prod_{i=1}^pT_i\cong\mathbb F_3^p.
\tag{1.5}
\]

## 2. Canonical fibres partition almost every owner

Fix once and for all a partition

\[
[n]=T_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}T_q
\mathbin{\dot\cup}R,
\qquad |T_i|=3,\quad |R|\le2,
\tag{2.1}
\]

where the triples are linearly ordered and \(q=\lfloor n/3\rfloor\).

For an \((m+1)\)-set \(Y\), call \(T_i\) a **singleton triple** if

\[
|Y\cap T_i|=1.
\tag{2.2}
\]

Call \(Y\) eligible if it has at least \(p\) singleton triples. For an
eligible \(Y\), let

\[
B(Y)=(T_{i_1},\ldots,T_{i_p})
\tag{2.3}
\]

be its first \(p\) singleton triples, in the fixed global order, and put

\[
A(Y)=Y\setminus\bigcup_{T\in B(Y)}T.
\tag{2.4}
\]

Since each chosen triple contributes one element,

\[
|A(Y)|=m+1-p.
\tag{2.5}
\]

### Lemma 2.1 (exact canonical-fibre partition)

For every eligible \(Y\), all \(3^p\) sets

\[
\mathcal F(Y)=
\left\{
A(Y)\cup\{y_1,\ldots,y_p\}:
y_j\in T_{i_j}
\right\}
\tag{2.6}
\]

are eligible and have the same ordered triple list \(B(Y)\) and the same
base \(A(Y)\). Consequently the distinct sets \(\mathcal F(Y)\) form a
partition of all eligible \((m+1)\)-sets into full
\(\mathbb F_3^p\)-fibres.

#### Proof

Changing the selected element inside one of the triples in \(B(Y)\)
preserves the fact that this triple has intersection size one. Every other
global triple is disjoint from the selected bank and its intersection with
the set is unchanged. Therefore the first \(p\) singleton triples remain
exactly \(B(Y)\), and removing their singleton elements again gives
\(A(Y)\).

Thus every set in (2.6) has the same canonical data. Conversely, equal
canonical data give exactly the family (2.6), so two such fibres are equal
or disjoint. \(\square\)

### Lemma 2.2 (almost every owner is eligible)

If \(Y\) is uniform in \({[n]\choose m+1}\), then

\[
\Pr(Y\text{ is not eligible})=e^{-\Omega(m)}.
\tag{2.7}
\]

#### Proof

Let

\[
Z(Y)=\bigl|\{i:|Y\cap T_i|=1\}\bigr|.
\tag{2.8}
\]

For each fixed triple,

\[
\Pr(|Y\cap T_i|=1)
=3\frac{{n-3\choose m}}{{n\choose m+1}}
=\frac38+O(m^{-1}).
\tag{2.9}
\]

Since \(q=2m/3+O(1)\),

\[
\mathbb EZ=\frac m4+O(1).
\tag{2.10}
\]

Expose \(Y\) as the first \(m+1\) values of a uniform random permutation
of \([n]\). A transposition exchanging one selected and one unselected
coordinate changes \(Z\) in at most two global triples. The bounded-
difference inequality on the uniform slice therefore gives

\[
\Pr\bigl(Z\le\mathbb EZ-t\bigr)
\le\exp(-\Omega(t^2/m)).
\tag{2.11}
\]

Because \(p=o(m)\), take \(t=\mathbb EZ-p=\Theta(m)\). This proves
(2.7). \(\square\)

By complementation, the eligible complements account for

\[
(1-e^{-\Omega(m)})W
\tag{2.12}
\]

rank-\(m\) owners.

## 3. A one-third packing inside one ternary fibre

Identify a canonical fibre with

\[
G=\mathbb F_3^p
\tag{3.1}
\]

by labelling the three choices in each ordered triple by
\(0,1,2\). Let \(e_1,\ldots,e_p\) be the standard basis, put

\[
P_0=0,\qquad P_j=e_1+\cdots+e_j\quad(1\le j<p),
\qquad \mathbf1=e_1+\cdots+e_p,
\tag{3.2}
\]

and define

\[
\mathcal A=
\{q\mathbf1+P_j:q\in\mathbb F_3,\ 0\le j<p\}.
\tag{3.3}
\]

The \(3p\) states in \(\mathcal A\), read in cyclic order, increment
coordinates \(1,2,\ldots,p\) once in each of three rounds. Thus
\(\mathcal A\) is exactly one rank-two queue owner ring in complement
coordinates. Every translate \(g+\mathcal A\) is another valid queue ring,
obtained by changing the initial omission in each phase.

### Lemma 3.1 (linear quotient injective on the queue cycle)

Let

\[
h=1+\lceil\log_3p\rceil.
\tag{3.4}
\]

There is a linear map

\[
F:G\longrightarrow\mathbb F_3^h
\tag{3.5}
\]

whose restriction to \(\mathcal A\) is injective.

#### Proof

Choose a nonzero vector \(s\in\mathbb F_3^h\). The quotient by the line
\(\langle s\rangle\) has

\[
3^{h-1}\ge p
\tag{3.6}
\]

cosets. Choose representatives

\[
R_0=0,R_1,\ldots,R_{p-1}
\tag{3.7}
\]

from \(p\) distinct cosets of \(\langle s\rangle\). Define

\[
\begin{aligned}
F(e_j)&=R_j-R_{j-1} &&(1\le j<p),\\
F(e_p)&=s-R_{p-1}.
\end{aligned}
\tag{3.8}
\]

Then

\[
F(P_j)=R_j\quad(0\le j<p),
\qquad F(\mathbf1)=s.
\tag{3.9}
\]

Consequently

\[
F(q\mathbf1+P_j)=qs+R_j.
\tag{3.10}
\]

Different values of \(j\) lie in different cosets of
\(\langle s\rangle\), and for fixed \(j\) the three values of \(q\) are
distinct. Hence the \(3p\) images in (3.10) are distinct. \(\square\)

### Lemma 3.2 (kernel-translate packing)

The family

\[
\{c+\mathcal A:c\in\ker F\}
\tag{3.11}
\]

consists of pairwise disjoint queue rings and covers at least one third of
\(G\).

#### Proof

Suppose

\[
c+a=c'+a',
\qquad c,c'\in\ker F,\quad a,a'\in\mathcal A.
\tag{3.12}
\]

Applying \(F\) gives \(F(a)=F(a')\). Lemma 3.1 gives \(a=a'\), and then
\(c=c'\). Thus all translates in (3.11) are disjoint.

Since \(|\operatorname{im}F|\le3^h\), their covered fraction is

\[
\frac{3p|\ker F|}{3^p}
=\frac{3p}{|\operatorname{im}F|}
\ge\frac{3p}{3^h}.
\tag{3.13}
\]

The definition of \(h\) gives

\[
3^h=3^{1+\lceil\log_3p\rceil}\le9p,
\tag{3.14}
\]

so (3.13) is at least \(1/3\). \(\square\)

The construction is allowed to use all elements of \(\ker F\): although
the translate parameter may change every phase origin independently, that
is exactly a relabelling of the cyclic omission order inside each triple.

## 4. Global assembly

Apply Lemma 3.2 independently inside every canonical fibre from Lemma 2.1.
Rings in one fibre are disjoint by Lemma 3.2, while rings in distinct
fibres are disjoint because the fibres themselves partition the eligible
owner complements.

Therefore the selected rings form a matching in the rank-\(m\) owner
hypergraph. By (2.12), the number of covered owners is at least

\[
\frac13(1-e^{-\Omega(m)})W
=\left(\frac13-o(1)\right)W.
\tag{4.1}
\]

This proves Theorem 0.1. \(\square\)

## 5. Sharp obstruction inside one fixed canonical fibre system

For a frame \((K;T_1,\ldots,T_p)\), the rank-\(s\) source inventory of
every translated queue ring is

\[
\Sigma(K;T_1,\ldots,T_p)
=\left\{
K\cup(T_i\setminus\{x\}):1\le i\le p,\ x\in T_i
\right\},
\qquad s=m-2d.
\tag{5.1}
\]

It has \(3p\) targets and is independent of the translation
\(c\in\mathbb F_3^p\): over one period every phase visits all three
omission states.

### Theorem 5.1 (fixed-fibre named-target no-go)

Any collection of queue rings which is both owner-disjoint and
rank-\(s\)-target-disjoint contains at most one ring from each canonical
fibre of Section 2. Consequently, if all rings are required to come from
that one fixed canonical fibre partition, they cover at most

\[
\boxed{
\frac{3p}{3^p}W=o(W)}
\tag{5.2}
\]

owner vertices.

#### Proof

All translates in one fibre have the same frame and hence the identical
inventory (5.1). Two of them collide in all \(3p\) rank-\(s\) targets, so
at most one may be selected.

The canonical partition has at most \(W/3^p\) fibres, including the
negligible ineligible remainder optimistically. One ring covers \(3p\)
owners. Multiplication gives (5.2), which is \(o(W)\) because
\(p\to\infty\). \(\square\)

Thus Theorem 0.1 cannot be made target-disjoint by thinning its
kernel-translate family. A successful construction must vary the phase
triple frame between rings, or decorate the source inventory while keeping
the owner queue valid.

## 6. Scope and the next gate

This theorem closes the exact owner-disjointness row for the rank-two
queue reset:

- every selected object is a literal \(3p\)-owner queue ring;
- different selected rings share no rank-\(m\) owner;
- the covered owner density is a fixed constant exceeding the required
  \(\theta\) by more than three orders of magnitude;
- the construction is explicit and uses no asymptotic hypergraph-matching
  theorem.

It does **not** yet close the rank-two rolling block-factor theorem. Two
correlated rows remain:

1. **Named-target selection.** The \(d\) proper suffix chains carried by
   different selected rings need not be disjoint in their target layers.
   The canonical owner fibres were defined using owner complements, not
   the residual PBBS target chart.
2. **Physical fusion and residual chart.** The selected queue rings are
   separate components. They must be fused into the merged owner
   chronology while preserving the upper deck, residence, and terminal
   compiler, and the unselected lower targets must still admit the
   complementary PBBS chain factor.

Thus the global problem has moved from

\[
\text{fractional owner capacity}\Longrightarrow
\text{integral owner packing}
\]

to the strictly later correlation

\[
\boxed{
\text{one-third owner packing}\ +\
\text{named-target-disjoint subpacking}\ +\
\text{fusion/residual factor}.}
\tag{6.1}
\]

No claim about \(\nu(k)\le B(k)+O(1)\) is made until those later rows are
proved.
