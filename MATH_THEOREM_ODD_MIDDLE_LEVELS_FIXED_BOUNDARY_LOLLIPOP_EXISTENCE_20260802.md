# Fixed-boundary augmented-incidence lollipops exist in every odd Middle Levels graph

**Date:** 2026-08-02  
**Status:** unconditional theorem.  This closes the central feasibility row
left open in `MATH_THEOREM_K17_H1_INCIDENCE_EULER_REDUCTION_20260802.md`.
It does **not** prove residence, the full upper deck, the lower compiler, or
`nu(17)=24313`.

## 0. Statement

For `n>=3`, let `ML(2n-1)` be the bipartite containment graph with shores

\[
 \mathcal Q={{[2n-1]}\choose {n-1}},\qquad
 \mathcal T={{[2n-1]}\choose n}.
\]

Fix distinct Johnson-adjacent vertices `M,D in Q`, and put

\[
                         B=M\cup D.                 \tag{0.1}
\]

Thus `B` is the unique owner containing both `M` and `D`.

### Theorem 0.1 (fixed-boundary lollipop existence)

There is a connected spanning simple incidence subgraph `G^+` of
`ML(2n-1)` satisfying

\[
\begin{aligned}
 \deg_{G^+}(T)&=2 &&(T\in\mathcal T),\\
 \deg_{G^+}(M)&=1,\qquad &N_{G^+}(M)&=\{B\},\\
 \deg_{G^+}(D)&=3,\\
 \deg_{G^+}(Q)&=2 &&(Q\in\mathcal Q\setminus\{M,D\}).
                                                        \tag{0.2}
\end{aligned}
\]

Consequently `G^+` is one alternating tail from `M` to `D` together with
one alternating cycle through `D`.  In particular, the `h=1` augmented
incidence selector is feasible for `K17` (`n=9`) for every fixed boundary
pair `(M,D)`.

The proof for `n>=4` is a protected, three-edge refinement of the cycle
factor and pull-tree proof used by Gregor--Merino--Mütze to prove that the
Middle Levels graph is Hamilton-laceable.  The only external ingredients
used below are their canonical cycle factor and its spanning tree of
incidence-hexagon gluings.

## 1. A Hamilton-path sufficient form

The desired graph follows from a slightly stronger rooted path statement.

### Lemma 1.1

Suppose `C in T` contains `D`, `C!=B`, and `H` is a Hamilton path of
`ML(2n-1)` from `M` to `C` such that

1. the first edge of `H` is `MB`; and
2. `CD` is not an edge of `H`.

Then

\[
                             G^+=H+CD               \tag{1.1}
\]

satisfies (0.2).

#### Proof

The endpoints `M,C` have degree one in `H`, and every other vertex has
degree two.  The vertex `D` is internal because the two path endpoints lie
on opposite shores and are `M,C`; it therefore has degree two in `H`.
Adding the absent edge `CD` raises the degrees of `C,D` by one.  Thus `C`
becomes degree two, `D` becomes degree three, `M` remains the leaf with
unique edge `MB`, and every other degree remains two.  The graph remains
simple, spanning, and connected.  \(\square\)

The rest of the proof constructs exactly this `H`.

## 2. Canonical factor notation

Write vertices as binary strings of length `2n-1`.  Recall the canonical
Middle Levels cycle factor `C_n` from the Hamilton-laceability proof.

For a lower string `x=t0`, where `t` is a Dyck word of length `2n-2`, write

\[
                   t=1u0v\qquad(u,v\text{ Dyck}).
\]

The two factor neighbours are

\[
 f(x)=1u1v0,\qquad g(x)=1u0v1.                    \tag{2.1}
\]

The maps are extended equivariantly under cyclic rotation.  The edges
`xf(x)` and `xg(x)` form two disjoint perfect matchings, and their union is
the spanning cycle factor `C_n`.

The same construction has a family `S_n` of incidence `C_6` gluings whose
auxiliary graph on the components of `C_n` is a tree.  We use two precise
features of that family.

* Each gluing is alternating with respect to `C_n`, so toggling any forest
  of auxiliary-tree edges leaves a spanning two-factor with the
  corresponding component forest.
* After the automorphism used in the Hamilton-laceability proof, every
  vertex of every gluing `C_6` has one distinguished coordinate equal to
  one.  Since `C_n` is invariant under cyclic coordinate rotation, the
  distinguished coordinate can be chosen arbitrarily.

These are Lemmas 25, 27, and 28 and the last paragraph of the proof of
Theorem 8 in:

> P. Gregor, A. Merino, and T. Mütze, *Star transposition Gray codes for
> multiset permutations*, J. Graph Theory 103 (2023), 212--270,
> arXiv:2108.07465.

## 3. The protected local alternating path

Assume `n>=4`.  In one-based bit positions define

\[
\begin{aligned}
 M&=(10)^{n-1}0,\\
 F&=M+\{2\},\\
 Q&=M-\{3\}+\{2\}=1100(10)^{n-3}0,\\
 C&=Q+\{2n-1\}=1100(10)^{n-3}1,\\
 B&=M+\{2n-1\},\\
 D&=M-\{3\}+\{2n-1\}.                           \tag{3.1}
\end{aligned}
\]

Here `+` and `-` mean insertion and deletion of coordinates.  The strings
`M,Q,D` have rank `n-1`, and `F,C,B` have rank `n`.  Moreover,

\[
        B=M\cup D,\qquad C=D\cup\{2\}.             \tag{3.2}
\]

The prefix `(10)^(n-1)` is a Dyck word, so (2.1) gives

\[
                       f(M)=F,\qquad g(M)=B.        \tag{3.3}
\]

Likewise `1100(10)^(n-3)` is a Dyck word, and therefore

\[
                              g(Q)=C.               \tag{3.4}
\]

It follows that

\[
                              P_0=M,F,Q,C            \tag{3.5}

\]

is a three-edge path which starts and ends with factor edges `MF,QC`, while
its middle edge `FQ` is outside the factor.

The two factor cycles opened by (3.5) are distinct.  Indeed, under the
plane-tree interpretation of the factor, `(10)^(n-1)` is the star on `n`
vertices, whereas `1100(10)^(n-3)` has maximum degree `n-2` and a nonleaf
vertex of degree two.  For `n>=4` these are nonisomorphic plane trees.

Consequently

\[
                     \mathcal C_n\mathbin\triangle E(P_0)   \tag{3.6}
\]

opens those two cycles and joins them into one simple path from `M` to `C`;
all other factor cycles remain unchanged.  Notice especially that the
factor edge `MB` survives (3.6).

## 4. A pull tree that cannot touch the local path

Every vertex in (3.5), and also both vertices of `MB` and `CD`, has bit
four equal to zero.  Take the transformed family `h(C(T_n))` from
the last paragraph of the proof of GMM Theorem 8, and cyclically rotate it
so that its protected last coordinate becomes coordinate four.  Thus every
vertex of every gluing hexagon has bit four equal to one, while the rotation
still preserves the canonical factor.  Call its auxiliary spanning tree
`R`.

Let `K_M,K_Q` be the two factor-cycle vertices of `R` containing `M,Q`.
Delete any one auxiliary edge on the unique `K_M`--`K_Q` path of `R`.
After adjoining the local merger (3.5), the resulting auxiliary graph is
again a spanning tree: it is exactly `R` plus the edge `K_MK_Q`, with one
edge removed from the unique resulting cycle.

Toggle all retained gluing hexagons together with `P_0`.  The toggles are
edge-disjoint from `P_0`, because their bit-four coordinate is one while
all vertices of `P_0` have bit four zero.  Every internal degree remains
two; only `M,C` have degree one.  The auxiliary graph is connected and
acyclic, so the result is one Hamilton path `H` from `M` to `C`.

The edge `MB` is untouched by both kinds of toggles, hence it is the first
edge of `H` at `M`.

It remains only to check that `CD` is absent.  It is not one of the three
edges in (3.5).  Since `g(Q)=C`, the inverse identity gives `f(C)=Q`, while
the other factor neighbour satisfies

\[
       g(C)=1100(10)^{n-4}001\ne
       1000(10)^{n-3}1=D.                          \tag{4.1}

Thus `CD` is not a factor edge.  No gluing hexagon can create it, because
both endpoints of `CD` have bit four zero whereas every gluing vertex has
bit four one.  Therefore `CD` is absent from `H`.

Lemma 1.1 now gives a lollipop for this particular ordered pair `(M,D)`.
The symmetric group on `[2n-1]` is transitive on ordered pairs of adjacent
rank-`(n-1)` sets, so relabelling proves the result for every fixed
`(M,D)`.

## 5. The remaining small case `n=3`

On `[5]`, take

\[
 M=\{1,2\},\qquad D=\{1,3\},\qquad B=\{1,2,3\}.
\]

The following is a Hamilton path from `M` to `C={1,3,5}`:

\[
\begin{array}{rcl}
12,&123,&13,134,14,124,24,245,25,125,\\
15,&145,&45,345,34,234,23,235,35,135.
\end{array}                                       \tag{5.1}
\]

Every juxtaposition denotes a set, and consecutive sets are incident.
The path starts with `MB`; the edge `DC=13--135` is not a path edge.
Adding it gives (0.2).  Symmetry again handles every fixed adjacent pair.

For `n=2` the statement is impossible because every Middle Levels vertex
has ambient degree two while (0.2) asks for `deg(D)=3`; this is the only
small exception.

## 6. Consequences and exact scope

For `K17`, take `n=9`.  Theorem 0.1 proves that the base incidence rows

\[
 \deg(M)=1,\quad \deg(D)=3,\quad
 \deg(Q)=2\ (Q\ne M,D),\quad \deg(T)=2
\]

together with connectedness and the fixed boundary edge `MB` are always
feasible.  The 218,790-variable lollipop master is therefore not deciding
central existence; it is selecting among a nonempty family for the
additional gates.

What remains attached to the same Euler chronology is exactly:

1. internal depth-three residence after opening;
2. rank-ten and deeper upper coverage;
3. a named age/refresh spelling and the two-row lower compiler.

The theorem supplies none of those three rows.  In particular it must not
be cited as a `24313` word or as evidence that a generic lollipop passes the
residence or compiler gates.

## 7. Deterministic local audit

The bounded audit

```text
scratch/audit_odd_ml_fixed_boundary_lollipop_20260802.cpp
```

checks the complete `n=3` Hamilton path, replays the canonical `f,g` factor
maps, and checks every displayed local identity for `4<=n<=100`.  It was
compiled and run with `g++ -O3` on the H100 CPU under

```text
/home/amodo/or15/work/root_odd_ml_lollipop_audit_20260802/
```

and returned

```text
PASS_ODD_ML_FIXED_BOUNDARY_LOLLIPOP_LOCAL_IDENTITIES n=3,4..100
```

with hashes

```text
audit source  f50c223e54414eaf5f69349773a35660e3f004503bf35489a3174d768dc1ed88
audit binary  29bcf7d029239d8cb1b8011cebfbbc494d9937fecfda55b835cc9284edcb89dc
stdout        2371774b4eb0041615bb9b1767ed9a398d24fafdebd542a4671229219481f239
```

The audit checks the new local algebra.  The all-`n` pull-tree existence is
the cited published theorem, not a finite computation.
