# Endpoint chains, the Greene--Kleitman forest, and the fixed-`H` q1 planting proof

Date: 2026-08-01  
Status: independent mathematical audit.  The endpoint-chain and
Greene--Kleitman statements pass.  The Ore--Ryser deletion argument passes.
The scalar Kruskal--Katona inequality used by the fixed-`H` theorem now has
a complete self-contained proof as well as the finite replay.

## 0. Verdict

Let

\[
 r=\left\lceil {k\over2}\right\rceil,
 \qquad W={k\choose r},
 \qquad \Lambda=\sum_{s=1}^{r-1}{k\choose s},
\]

and let a universal nonzero contiguous-OR word have length `W+e`.

1. The architecture-free endpoint cap is correct: every lower-rank target
   has a witness of physical length at most `e`, and the selected middle
   witnesses can be chosen with distinct right endpoints and physical length
   at most `e+1`.
2. The exact endpoint-defect inequality below is correct.  It gives a new
   uniform consequence for every hypothetical `B(k)+C` word: apart from
   `O_C(W/sqrt(k))` middle owners, every selected owner has a proper-suffix
   chain of any prescribed fixed positive fraction of the extremal depth.
3. The Greene--Kleitman central-mate graph really is acyclic, has exactly
   `Cat_m` tree components, and has maximum degree exactly `m`.  Acyclicity
   does **not** imply maximum degree two.
4. In
   `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`,
   the edge-minimal Ore--Ryser step is sound.  Deleting a protected edge
   incident with the violating left set raises both sides of the same strict
   cut inequality by exactly one.
5. The coarse middle-shadow inequality used there now has a complete proof.
   The key auxiliary fact is
   `partial_k(t)-t>=k-1` for `1<=t<=binom(2k-2,k)`; the near-full case is
   reduced by complementation to that same auxiliary fact.  The exact replay
   over every `a` for `2<=m<=12` still passes.

## 1. Exact endpoint-chain theorem

Let the nonempty letters be `A_1,...,A_n`, where `n=W+e`, and put

\[
 C_{i,j}=A_i\cup A_{i+1}\cup\cdots\cup A_j.
\]

For a fixed left endpoint `i`, let `f_i` be the number of initial cells
`C_(i,i),C_(i,i+1),...` having rank below `r`, and put

\[
                         F_i=i+f_i.                 \tag{1.1}
\]

If the whole column remains below rank `r`, use `F_i=n+1`.

### Lemma 1.1 (left-endpoint cap)

The sequence `F_i` is nondecreasing.  Values of `F_i<=n` which first expose
different rank-`r` sets are distinct.  Consequently

\[
                         f_i\le e                  \tag{1.2}
\]

for every `i`.

#### Proof

Deleting the first letter from a cell cannot increase its union, so
`f_(i+1)>=f_i-1`; the cases `f_i=0,1` give the same monotonicity directly.
Thus `F_(i+1)>=F_i`.

If `F_i=F_j=b` with `i<j` and both columns first meet rank `r` there, then

\[
                 C_{j,b}\subseteq C_{i,b}.
\]

Equal rank forces equality.  Since all `W` middle masks must occur, at least
`W` distinct finite values of `F` occur.  If `F_i` is the `t`-th such value,
then monotonicity gives `i>=t`, while room for the later values gives
`F_i<=n-(W-t)`.  Hence `f_i=F_i-i<=n-W=e`.  The value `n+1` is handled in
the same way after the `W` finite values.  \(\square\)

It follows immediately that every occurrence of a target below rank `r`
has length at most `e`: it lies before the first rank-`r` cell in its
left-endpoint chain.  For each middle target choose a column in which it
occurs and truncate at that column's first rank-`r` cell.  The resulting
`W` middle witnesses have distinct right endpoints and length at most
`e+1`.

Let `S` be this set of selected right endpoints.  For `b in S`, let `x_b`
be the number of **distinct nonempty proper suffix unions** inside its
selected middle witness.  Equivalently, `x_b` is one less than its
last-occurrence-block depth.  Then

\[
                  0\le x_b\le e.                   \tag{1.3}
\]

Use one witness for each of the `Lambda` lower masks, and let `q_b` be the
number ending at `b`.  At a selected endpoint every lower witness is a
proper suffix of the selected middle witness: starting weakly before the
middle witness would contain a rank-`r` union.  Hence `q_b<=x_b`.  At an
unselected endpoint there are at most

\[
                         c_b=\min\{e,b\}             \tag{1.4}
\]

eligible physical suffix lengths (endpoints are numbered from `1`).  Since

\[
 \sum_{b=1}^{W+e}c_b=eW+{e+1\choose2},              \tag{1.5}
\]

we obtain the exact architecture-free inequality

\[
 \boxed{
 \sum_{b\in S}(c_b-x_b)
 \le
 \sigma_e:=eW+{e+1\choose2}-\Lambda .
 }                                                    \tag{1.6}
\]

Every summand is nonnegative.  For an equality-length word `e=d(k)`, a
summand is zero exactly when `b>=d+1`, the selected interval is
`[b-d,b]`, and its `d+1` letters create `d+1` distinct last-occurrence
blocks.  Thus the endpoint interval assertion and its equality case are
both valid; the one-based convention in (1.4) is essential.

## 2. Strong architecture-free consequence of `B(k)+O(1)`

Define

\[
 d=d(k)=\min\left\{j:jW+{j+1\choose2}\ge\Lambda\right\},
 \qquad
 \sigma=dW+{d+1\choose2}-\Lambda .                  \tag{2.1}
\]

Minimality gives the useful exact bound

\[
                         0\le\sigma<W+d.             \tag{2.2}
\]

Suppose now that the word has length

\[
                         W+d+C                       \tag{2.3}
\]

for a fixed nonnegative integer `C`; put `e=d+C`.  From (1.6), and from the
fact that at most the first `e` endpoints have `c_b<e`,

\[
 \sum_{b\in S}(e-x_b)
 \le \sigma_e+{e\choose2}.                           \tag{2.4}
\]

The exact change in scalar slack is

\[
 \sigma_e=CW+\sigma+Cd+{C+1\choose2}.                \tag{2.5}
\]

Subtracting `CW` from (2.4) gives the signed-depth estimate

\[
 \sum_{b\in S}(d-x_b)
 \le
 A_{k,C}:=sigma+Cd+{C+1\choose2}+{d+C\choose2}.      \tag{2.6}
\]

Since `x_b<=d+C`, the total positive deficit below depth `d` obeys

\[
 \boxed{
 \sum_{b\in S}(d-x_b)^+
 \le CW+A_{k,C}.
 }                                                    \tag{2.7}
\]

In particular, for every integer `1<=t<=d`,

\[
 \boxed{
 \#\{b\in S:x_b\le d-t\}
 \le {CW+A_{k,C}\over t}.
 }                                                    \tag{2.8}
\]

This is independent of a flat carrier, Johnson adjacency, PBBS, wreaths,
or a compiler normal form.  It is forced by universality and physical
length alone.

Uniformly on both parities,

\[
 d(k)=\sqrt{\pi k\over8}+O(1),                       \tag{2.9}
\]

while `A_(k,C)<=W+O_C(k)`.  Hence for fixed `C` and fixed `eta in (0,1)`,

\[
 {1\over W}
 \#\{b:x_b\le(1-\eta)d\}
 \le
 \left({C+1\over\eta}\sqrt{8\over\pi}+o(1)\right)
 {1\over\sqrt{k}}.                                  \tag{2.10}
\]

Thus a hypothetical `B(k)+O(1)` construction necessarily contains
`W-O_C(W/sqrt(k))` middle owners with recency depth at least any fixed
fraction of the extremal `Theta(sqrt(k))` depth.  The average signed depth
is even tighter:

\[
 {1\over W}\sum_{b\in S}x_b
 \ge d-{sigma\over W}-o(1)>d-1-o(1).                \tag{2.11}
\]

What is **not** forced for `C>0` is one common flat delay or a contiguous
`(0,d)` core.  Up to `C` units of over-depth per owner can compensate
under-depth elsewhere.  Equation (2.7), rather than flatness, is the honest
architecture-free rigidity statement.

## 3. Greene--Kleitman Catalan forest audit

In the Greene--Kleitman SCD of `B_(2m)`, every nonsingleton chain has one
central triple

\[
                      L\lessdot T\lessdot U.
\]

Let `H` be the other middle point in `[L,U]` and orient the induced Johnson
edge `T->H`.

* The `L` and `U` entries run once through ranks `m-1` and `m+1`, so both
  outer palettes are exact.
* In standard bracketing, if `a<b` are the two relevant free-zero
  positions, `T=L+a` and `H=L+b`.  Therefore
  `omega(H)-omega(T)=b-a>0` for `omega(X)=sum_(i in X)i`.  Directed cycles
  are impossible.
* Every middle vertex has outdegree at most one.  If an undirected cycle
  existed, its equal numbers of vertices and edges would force every cycle
  vertex to orient one cycle edge, producing a directed cycle.  Hence the
  underlying graph is a forest.
* It has `binom(2m,m-1)` edges on `binom(2m,m)` vertices, so it has exactly
  `Cat_m` components.

The degree claim is also exact, but does not follow merely from the displayed
example.  If `q(X)` is the number of alternate-head preimages, then

\[
 \deg(X)={\bf1}_{X\text{ is on a nonsingleton GK chain}}+q(X). \tag{3.1}
\]

The minimum-return fibre law gives `q(X)<=m`, with equality only for
`X=(01)^m`; that word is a singleton chain.  Every nonsingleton has
`q(X)<=m-1`.  Thus

\[
                         \Delta=m.                  \tag{3.2}
\]

The forest theorem is therefore correct, including acyclicity and exact
maximum degree, but it supplies a branching forest rather than a Catalan
linear forest when `m>=3`.

## 4. Fixed-`H` Ore--Ryser audit

Let `P` be a 2-bounded protected subgraph of the middle-level incidence
graph, with `|E(P)|<=m-2`, and suppose an inclusion-minimal
`H subseteq P` has no two-factor completion.  In the residual graph put
`b(v)=2-d_H(v)`.  Ore--Ryser supplies `A` on the left with

\[
 b(A)>\sum_U\min\{b(U),d_{G-H}(U,A)\}.               \tag{4.1}
\]

If `xU in H` with `x in A`, delete that protected edge.  Then `b(x)` rises
by one, so the left side rises by one.  On the right, both `b(U)` and the
available degree from `A` rise by one, and therefore

\[
 \min\{b(U)+1,d(U,A)+1\}=\min\{b(U),d(U,A)\}+1.      \tag{4.2}
\]

The same strict violation survives, contradicting minimality.  Thus no
edge of `H` meets `A`.  The rest of Theorem 2.1 follows exactly as written
from the truncated two-shadow inequality.  There is no gap in the
edge-minimal deletion step.

The upstream scalar KK estimate

\[
 K_m(a)-a\ge\min\{m-1,{2m-1\choose m}-a\}            \tag{4.3}
\]

is now proved self-containedly in the fixed-`H` note.  The proof first shows
`partial_k(t)-t>=k-1` below `binom(2k-2,k)` by the canonical first binomial
term and equal-rank incidence counting.  Above that breakpoint, the missing
lower shadow is complemented and the same auxiliary estimate bounds its
upper shadow.  The independent replay verifies every `a` for `2<=m<=12`.
Thus Theorem 2.1 has no remaining logical dependency on an unstated
Kruskal--Katona corollary.
