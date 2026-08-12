# Rooted upper bases and the lower quotient-graphic gate

Date: 2026-07-31  
Status: exact reduction, cap-safe exchange theorem, and independently replayed
finite obstruction/positive fixtures; no all-parameter side-selection theorem

## 0. Result

Fix an oriented Catalan path forest $F$, an automatically supplied common
basis $Q$, and $Z=F-Q$. Suppose the upper punctured shore has no
anchor-free component. After adjoining a root $\rho$, its $P$ selected side
edges together with exactly $C-K=N-P$ root-to-anchor edges form a spanning
tree.

Once this upper tree is fixed, the remaining topology is ordinary graphic
independence. If $\mu_-$ and $\mu_+$ are the upper and lower anchor-pair
matchings on $V=\operatorname{comp}(Z)$, then

\[
 \beta(\Gamma_Q)=\beta(\mu_-\cup\mu_+)
               =\beta(\overline{\mu_+}\text{ on }V/\mu_-). \tag{0.1}
\]

Loops and parallel edges are retained after contraction. Equivalently, for
the two fixed-point-free partial involutions $\alpha$ and $\delta$ defined by the
matchings, the physical complement is acyclic exactly when $\delta\alpha$ has
no periodic orbit on its iterated domain.

This gives an exact packet rule: a palette- and degree-preserving lower
exchange repairs all topology cycles iff, after deleting its old links, its
new contracted links are independent over the residual graphic forest.

The reduction does not make lower completion automatic. On the frozen
strict $n=3$ face the upper shore has $c_0^-=0$, but the unique lower
shore repeats four upper anchor pairs. They become four quotient loops, so
the contracted cycle rank is four. The known non-strict $n=3$ lift escapes
this obstruction.

## 1. Setup and rooted upper base

Use

\[
 M={2n\choose n},\quad N={2n\choose n-1},\quad
 P={2n\choose n-2},\quad C=M-P,\quad K=\operatorname{Cat}_n. \tag{1.1}
\]

The punctured forest $Z$ has $K+C$ components. For $q=t_qh_q\in Q$,
put $a(q)=[t_q]_Z$ and $b(q)=[h_q]_Z$. Both maps are injective.
A double-anchor upper component produces a link between two $a$-images;
a double-anchor lower component produces a link between two $b$-images.
The link sets $\mu_-$ and $\mu_+$ are matchings and the side charge gives

\[
 |\mu_-|=K+c_0^-,\qquad |\mu_+|=K+c_0^+.             \tag{1.2}
\]

### Theorem 1.1 (rooted graphic base)

Let $S^-$ be an anchor-capped $P$-edge linear forest on the $N$ upper
side vertices, and let $A^-$ be its $C$ anchors. Adjoin a root $\rho$ and
the star $E_\rho=\{\rho a:a\in A^-\}$. Then $c_0^-=0$ iff there is
$R_\rho\subseteq E_\rho$, of order

\[
 |R_\rho|=C-K=N-P,                                    \tag{1.3}
\]

such that $S^-\cup R_\rho$ is a spanning tree.

#### Proof

If every component contains an anchor, choose one anchor in each component
and join it to $\rho$. A $P$-edge forest on $N$ vertices has $N-P=C-K$
components, and the result is a tree. Conversely, deleting the root edges
from such a tree leaves every component incident with its unique former
root edge, hence with an anchor. Two root edges into one component would
have formed a cycle through $\rho$. QED.

For the direct-edgewise occurrence bank, the upper row is therefore
exactly: one occurrence in each of the two outer-colour partitions, the
physical degree/anchor caps, and one rooted graphic base. This is a
formulation, not an integrality theorem for their intersection.

## 2. Exact lower quotient and alternating permutation

### Theorem 2.1 (lower quotient identity)

Fix anchor-capped upper and lower side forests. Contract all upper links,
retaining loops and parallel lower images. Then (0.1) holds.

#### Proof

Star-contracting each side component preserves cycle rank and converts the
physical attachment graph into $H=\mu_-\cup\mu_+$ on $V$. The upper
links form a matching and hence a forest. Contracting a forest preserves
cycle rank. A lower link inside one upper block becomes a loop, and lower
links with the same two upper blocks remain parallel. QED.

### Corollary 2.2 (partial-involution criterion)

Let $\alpha$ and $\delta$ be the partial involutions defined by the two matchings.
Then $\Gamma_Q$ is a forest iff $\delta\alpha$ has no periodic orbit.

#### Proof

Every cycle in a union of two matchings alternates. Following one upper and
one lower link walks by $\delta\alpha$ around one parity class. Conversely, a
periodic orbit expands to an alternating cycle. A common upper/lower link is
the two-edge cycle and becomes a fixed point. QED.

The periodic-orbit statement is a zero/nonzero test; one alternating cycle
has two oriented periodic orbits. Exact cycle rank is read from the quotient
multigraph in (0.1).

### Corollary 2.3 (strong universal-safe face)

Let $B=b(Q)$. If every upper link has an endpoint outside $B$, then the
topology is acyclic for every legal lower shore.

#### Proof

Every upper edge on an alternating cycle must have both endpoints incident
with lower links and therefore in $B$. QED.

This is sufficient but not necessary. The positive direct chain has 2, 9,
and 31 cycle-capable upper links at $n=3,4,5$, respectively.

## 3. Cap-safe augmenting packets

Fix the upper shore. Suppose a lower physical packet replaces old link set
$X$ by a same-cardinality link set $Y$, and independently preserves both
palettes, the literal lower side forest, and every physical degree/anchor
cap. Bars denote images in $V/\mu_-$.
All link collections in this section are labelled multisets, so parallel
images remain distinguishable.

### Theorem 3.1 (necessary and sufficient packet test)

The exchanged attachment graph is a forest iff

\[
 (\overline{\mu_+}\setminus\overline X)\cup\overline Y \tag{3.1}
\]

is loopless and graphic-independent. Equivalently, after removing the old
packet, the new quotient links may be inserted in any order and every one
joins two different current union-find components.

If $X$ contains one lower edge from every old alternating cycle, the
residual is a forest. Hence any cap-safe $Y$ independent over that residual
eliminates all topology debt.

#### Proof

The first statement is Theorem 2.1 after the exchange. Inserting an edge
into a forest preserves acyclicity exactly when its endpoints are in
different components. Alternating cycles in a union of two matchings are
vertex-disjoint, so deleting one lower edge from each destroys all old
cycles. QED.

In particular, every topology-closing packet must remove at least one lower
link from each old alternating cycle. Since those cycles are vertex-disjoint,

\[
 |X|\ge \beta(\Gamma_Q).                              \tag{3.2}
\]

This bound is sharp at the abstract link level: remove one lower edge per
cycle and reinsert the same number of quotient edges as a forest extension.
Physical palette and cap constraints may force a larger packet.

This is an exact augmenting theorem, but it is conditional on a physical
palette- and cap-preserving packet. Abstract quotient rewiring alone is not
a side actuator.

## 4. Sharp frozen-face obstruction

In the complete strict-extremal $n=3$ face both shores are individually
unique and have $(c_0,c_1,c_2)=(0,4,5)$. Their link sets are

```text
upper: (7,56) (13,52) (14,25) (22,42) (35,44)
lower: (7,56) (14,25) (21,28) (22,42) (35,44).
```

The four common links

```text
(7,56) (14,25) (22,42) (35,44)
```

become four literal quotient loops. Thus $\beta(\Gamma_Q)=4$, despite the
upper rooted-tree certificate. Since the strict lower catalogue has one
element, no strict cap-safe packet exists in this face.

Therefore a rooted upper base plus an independently feasible lower shore is
not sufficient. The shores must be selected jointly, or a physical exchange
must leave this strict face. The authenticated non-strict $n=3$ lift has
quotient cycle rank zero.

## 5. Positive chained fixtures

Independent replay of the direct-edgewise chain gives:

| child n | central components | upper links | lower links | root edges | cycle-capable upper links | quotient loops | quotient cycle rank |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 19 | 5 | 5 | 9 | 2 | 0 | 0 |
| 4 | 56 | 14 | 15 | 28 | 9 | 0 | 0 |
| 5 | 174 | 42 | 44 | 90 | 31 | 0 | 0 |

In every row the upper $P$ side edges plus the root edges form a literal
spanning tree. These are finite positive fixtures, not induction.

## 6. Audit and scope

The deterministic audit is

```text
scratch/audit_h2_catalan_rooted_upper_alternating_lower_20260731.py
scratch/h2_catalan_rooted_upper_alternating_lower_20260731.audit.json
```

It authenticates and rebuilds the direct $n=3,4,5$ chain, constructs the
root trees, contracts the upper matchings, reconstructs the unique strict
$n=3$ side pair and its four loops, and exhausts all $76^2=5776$ pairs
of partial matchings on six labelled vertices to check contraction and the
periodic-orbit criterion.

No all-parameter occurrence supply, side representative theorem, cap-safe
packet supply, residence, shadow, compiler, or global equality conclusion
is claimed.
