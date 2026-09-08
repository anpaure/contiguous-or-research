# Cyclic-star multidepth links: exact charging, a sufficient suffix theorem, and a realizable spike

**Date:** 2026-08-06  
**Method:** modular-sum completion counting, link double counting, greedy
suffix extension, and an explicit restricted-sum construction  
**Status:** unconditional. Exact average \(t\)-link bounds hold at every
depth, and a uniform nested-link bound would construct a long legal linear
star chart. However, the packet geometry itself can realize maximally
concentrated forbidden links while all participating cores remain
bottom-disjoint in one modular-sum class. Hence the existing scalar
averages do not imply the required multidepth expansion.

## 1. Setup

Let cores have size \(s-1\) in \(\mathbb Z_n\), put

\[
                         v=n-s+1,
\]

and fix one modular-sum class

\[
 \mathcal Q_c=
 \left\{Q\in{\mathbb Z_n\choose s-1}:\sum Q=c\pmod n\right\},
 \qquad M=|\mathcal Q_c|.
\]

Suppose \(T\) distinct-core star packets have already been selected, each
with private cyclic length at most \(L\). For an unused core
\(Q\in\mathcal Q_c\), let

\[
 \mathcal F_{Q,j}\subseteq{\mathbb Z_n\setminus Q\choose j}
\]

be the family of private \(j\)-sets which would reproduce a previously
selected depth-\(j\) target.

For \(J\subseteq\mathbb Z_n\setminus Q\), \(|J|=t<j\), write

\[
 d_{Q,j}(J)=
 \left|\{I'\in\mathcal F_{Q,j}:J\subseteq I'\}\right|.                 \tag{1.1}
\]

## 2. Exact one-target \(t\)-link charge

Fix one previous depth-\(j\) target \(X\), so

\[
                         |X|=s+j-1.
\]

A future equal-colour core \(Q\subset X\) has forbidden private port

\[
                         I'=X\setminus Q,
\]

and the colour equation is

\[
                         \sum I'=\sum X-c\pmod n.                      \tag{2.1}
\]

### Lemma 2.1 (one-target \(t\)-link bound)

For a fixed \(t\)-set \(J\subset X\), the target \(X\) charges ports
\(I'\supseteq J\) at at most

\[
 \boxed{
 {1\over j-t}{s+j-1-t\choose j-t-1}}                                  \tag{2.2}
\]

future equal-colour cores.

#### Proof

Choose \(j-t-1\) further elements of \(I'\setminus J\). Equation (2.1)
determines the last residue. Every successful \(I'\) is generated exactly
\(j-t\) times, according to which member of \(I'\setminus J\) is chosen
last. Distinct \(I'\)'s give distinct cores \(Q=X\setminus I'\).
\(\square\)

The case \(t=0\) recovers the exact candidate bound

\[
                         {1\over j}{s+j-1\choose j-1}.                  \tag{2.3}
\]

At the opposite end, \(t=j-1\), a fixed target charges a fixed
\((j-1)\)-link at most once.

## 3. Sequential average link bounds

### Theorem 3.1 (all-\(t\) averaged charge)

For every \(0\le t<j\le d\),

\[
 \boxed{
 \sum_{Q\ {\rm unused}}
 \sum_{J\in{\mathbb Z_n\setminus Q\choose t}}
 d_{Q,j}(J)
 \le
 TL\,{1\over j}{s+j-1\choose j-1}{j\choose t}.}                       \tag{3.1}
\]

If \(T<\rho M\), the average raw \(t\)-link degree is therefore at most

\[
 {\rho\over1-\rho}\,
 {L\over j}\,
 {{s+j-1\choose j-1}{j\choose t}\over {v\choose t}}.                  \tag{3.2}
\]

After division by the number \({v-t\choose j-t}\) of possible extensions
of a \(t\)-link, the normalized average is

\[
 \boxed{
 {\rho\over1-\rho}\,
 {L\over j}\,
 {{s+j-1\choose j-1}\over {v\choose j}}.}                             \tag{3.3}
\]

It is independent of \(t\).

#### Proof

Every previous packet has at most \(L\) targets at depth \(j\). By (2.3),
one such target charges at most
\({s+j-1\choose j-1}/j\) future ports. Every charged \(j\)-port contains
exactly \({j\choose t}\) \(t\)-links. This proves (3.1), with
multiplicity; deleting duplicate charges can only decrease the left side.

There are at least \((1-\rho)M\) unused cores, each with
\({v\choose t}\) links, giving (3.2). Finally use

\[
 {v\choose t}{v-t\choose j-t}={v\choose j}{j\choose t}
\]

to obtain (3.3). \(\square\)

When \(L\le v\), equation (3.3) is at most

\[
 {\rho\over1-\rho}
 \prod_{a=1}^{j-1}{s+a\over v-j+a},                                   \tag{3.4}
\]

and hence at most \(\rho/(1-\rho)\) whenever \(s+j\le v\). Thus every
link order has good **average normalized density** in the top PBBS slab.

## 4. What uniform nested-link control would prove

The cyclic closure is not needed for a protected linear star chart. Let
\(V\) be a \(v\)-set and let

\[
                         \mathcal F_j\subseteq{V\choose j},
                         \qquad2\le j\le d.
\]

For an ordered sequence of distinct vertices
\(\mathbf x=(x_1,\ldots,x_r)\), define its forbidden extension set

\[
 B(\mathbf x)=
 \bigcup_{2\le j\le\min(d,r+1)}
 \left\{y\in V:\{x_{r-j+2},\ldots,x_r,y\}\in\mathcal F_j\right\}.
                                                                            \tag{4.1}
\]

### Theorem 4.1 (nested-suffix avoidance)

Suppose

\[
                         |B(\mathbf x)|\le b                             \tag{4.2}
\]

for every ordered distinct sequence \(\mathbf x\) of length at most
\(d-1\). Then there is a linear ordering of at least

\[
                         v-b                                             \tag{4.3}
\]

distinct vertices in which no consecutive \(j\)-set belongs to
\(\mathcal F_j\), simultaneously for every \(2\le j\le d\).

Consequently it gives at least

\[
                         v-b-d+1                                        \tag{4.4}
\]

full rank-\(s\) star endpoints.

#### Proof

Build the ordering greedily. After \(r<v-b\) vertices have been used,
apply (4.2) to the suffix formed by the last \(\min(r,d-1)\) vertices.
At most \(r\) choices are old and at most \(b\) choices create a forbidden
terminal window. Since \(r+b<v\), a new legal vertex exists. Continue to
length \(v-b\). Each forbidden consecutive set would have been created at
the step when its last vertex was appended, so none occurs.

The last \(v-b-d+1\) positions have complete suffix chains of depths
one through \(d\), proving (4.4). \(\square\)

In particular, the stronger collection of maximum-link estimates

\[
 \max_{J\in{V\choose j-1}}d_{\mathcal F_j}(J)\le\varepsilon_jv,
 \qquad
 \sum_{j=2}^d\varepsilon_j\le\alpha<1,                                \tag{4.5}
\]

implies \(b\le\alpha v\) and a linear chart of length at least
\((1-\alpha)v\).

This is the precise positive answer to the link-expansion question:
**uniform bounded nested-link concentration is sufficient.** The problem
is obtaining it from the current packet selection.

## 5. A packet-generated link spike

The average bounds in Section 3 cannot be promoted to (4.2) by a formal
averaging argument. The cyclic-star geometry itself can realize the sharp
link obstruction.

Let

\[
                         Q=\{0,1,\ldots,q-1\}\subset\mathbb Z_n,
                         \qquad q=s-1,
\]

and let \(V=\mathbb Z_n\setminus Q\). The sums of \(j\) distinct elements
of \(Q\) contain every integer in the interval

\[
 \left[{j(j-1)\over2},
       j(q-1)-{j(j-1)\over2}\right].                                  \tag{5.1}
\]

This interval contains

\[
                         j(q-j)+1                                      \tag{5.2}
\]

consecutive integers. To see that there are no gaps, write
\(a_i=(i-1)+b_i\) for an increasing \(j\)-tuple. The \(b_i\)'s are
nondecreasing in \([0,q-j]\). For every
\(0\le T\le j(q-j)\), write \(T=jr+t\), \(0\le t<j\), and take
\(j-t\) of the \(b_i\)'s equal to \(r\) and \(t\) equal to \(r+1\).
This realizes total increment \(T\); at the maximum endpoint \(t=0\).
Hence, whenever

\[
                         j(q-j)+1\ge n,                                \tag{5.3}
\]

every residue modulo \(n\) is the sum of \(j\) distinct elements of \(Q\).

### Theorem 5.1 (realizable complete and one-link spikes)

Assume (5.3). For every family

\[
                         \mathcal A\subseteq{V\choose j},              \tag{5.4}
\]

there is a family of distinct maximal star packets, whose cores all have
the same modular sum as \(Q\), such that every \(I'\in\mathcal A\) is a
forbidden depth-\(j\) port at \(Q\).

All these prior cores, together with \(Q\), have pairwise disjoint complete
bottom stars.

#### Proof

For each \(I'\in\mathcal A\), use (5.3) to choose

\[
 B_{I'}\in{Q\choose j},\qquad
                         \sum B_{I'}=\sum I'\pmod n.
\]

Put

\[
                         P_{I'}=Q-B_{I'}+I'.                            \tag{5.5}
\]

Then \(P_{I'}\) is an \((s-1)\)-core with the same modular sum as \(Q\).
Moreover \(P_{I'}\setminus Q=I'\), so different \(I'\)'s give different
cores.

The set \(B_{I'}\) lies in the complement of \(P_{I'}\). Choose any
maximal complement cycle in which its \(j\) labels are consecutive. That
packet contains the target

\[
                         P_{I'}\cup B_{I'}=Q\cup I'.                    \tag{5.6}
\]

Thus \(I'\) is forbidden at \(Q\). Distinct cores of one modular-sum class
cannot be Johnson adjacent, so their complete bottom stars are pairwise
disjoint. \(\square\)

Two specializations are exact:

1. If \(\mathcal A={V\choose j}\), then
   \(\mathcal F_{Q,j}={V\choose j}\): the future core is completely
   blocked at depth \(j\).
2. If \(x\in V\) and
   \(\mathcal A=\{I'\in{V\choose j}:x\in I'\}\), then the forbidden family
   has global density exactly \(j/v=o(1)\), but its link at \(x\) is
   saturated:

   \[
   d_{Q,j}(\{x\})={v-1\choose j-1}.                                   \tag{5.7}
   \]

For the top PBBS slab

\[
 n=2m+1,\qquad s=m-2d,\qquad q=m-2d-1,
\]

condition (5.3) holds for every \(3\le j\le d\) once \(m\) is sufficiently
large. Indeed \(j(q-j)\) is increasing on this range, and at \(j=3\) the
condition reduces to \(m\ge6d+12\).

## 6. Exact boundary left open

Theorem 5.1 is a star-specific obstruction, not merely an arbitrary
forbidden-hypergraph example. It proves that

* common modular colour;
* pairwise bottom-star disjointness; and
* small global forbidden density

do not force the uniform nested-link bound (4.2).

Its prior packets are **not** asserted to be mutually target-disjoint at
depths two through \(d\). Therefore it does not refute a carefully
maintained multidepth packing such as the desired extension of the audited
depth-two Dirac construction.

The exact remaining invariant is now clear. A successful sequential
selection must preserve, for enough unused candidate cores \(Q\), bounded
**suffix-union load**

\[
 \max_{\mathbf x}
 \left|
 \bigcup_{j=2}^d
 \{y:\operatorname{suffix}_{j-1}(\mathbf x)+y
                         \in\mathcal F_{Q,j}\}
 \right|\le(1-\lambda)v                                  \tag{6.1}
\]

for one absolute \(\lambda>0\). The average \(t\)-link identities
(3.1)--(3.4) do not supply this maximum. Proving that depth-two-safe packet
selection also controls (6.1), or adding a multiscale pruning rule which
enforces it, is the specialized all-depth star-factor gate.

