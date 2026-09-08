# The logarithmic residual: outer Hall is tractable, four-resource Hall is not local

Date: 2026-07-31  
Status: deterministic outer-perfect-matching theorem and sharp sparse
four-partite space-barrier counterexample; no exact Boolean residual theorem

## 0. Verdict

At survival `p=m^(-1/3)`, the Boolean ordered-diamond residual has the
promising scales

```text
D=Theta(m)=Theta(log N),       Delta_2=Theta(m^(1/3))=Theta(D^(1/3)).
```

These statistics are enough to reduce the **outer** matching problem to one
large-rectangle mixing condition.  If the outer projection has minimum
degree `delta`, same-shore codegree `lambda`, and no empty rectangle above
size `Theta(delta^2/lambda)`, then it has a perfect matching.  At the target
scales this means checking rectangles only above `Theta(D^(5/3))`.

They do **not** imply an outer-perfect four-resource matching.  There are
sparse four-partite hypergraphs with:

* all degrees `(1+-epsilon)Theta(log n)`;
* maximum pair codegree at most two;
* a random-like outer projection with a perfect matching and no Hall holes;
* middle shores of size `n+k`, where `k=o(n)`; but
* no matching covering the outer shore.

The obstruction is a hidden middle-resource space barrier of only one
vertex.  Thus the missing residual hypothesis is a genuinely four-resource
capacity/expansion condition, at least a robust fractional Hall condition,
followed by a lattice/transferral condition.  Ordinary degree, codegree and
outer mixing cannot prove the desired theorem.

## 1. Residual scaling

Let the full ordered-diamond hypergraph have outer degree `Theta(m^2)` and
maximum pair codegree `Theta(m)`.  If every resource survives with density
`p`, then, conditional on one surviving resource, an incident atom survives
when its other three resources survive.  Therefore

```text
D_res=Theta(m^2 p^3).
```

A fixed resource pair has two further resources to survive, so

```text
Delta_2,res=Theta(m p^2).
```

At `p=m^(-1/3)` these become

```text
D_res=Theta(m),             Delta_2,res=Theta(m^(1/3)).     (1.1)
```

If `n=Np` outer resources remain, each middle role has `n+K` unused
resources, where `K=Cat_m=N/m`, and hence

```text
K/n=m^(-2/3).                                             (1.2)
```

## 2. A deterministic Hall theorem for the outer projection

For a balanced bipartite graph `G=(A,B)` write `codeg(x,x')` for the
number of common neighbours of two vertices on the same shore.

### Theorem 2.1 (small-codegree plus large-hole exclusion)

Let `|A|=|B|=n`.  Suppose:

1. every vertex has degree at least `delta`;
2. every same-shore pair has codegree at most `lambda`;
3. an integer `s_0>=1` satisfies

   ```text
   lambda(s_0-1) <= delta(delta-1);                       (2.1)
   ```

4. there are no anticomplete sets `X subset A`, `Y subset B` with
   `|X|>s_0` and `|Y|>s_0`.

Then `G` has a perfect matching.

### Proof

First let `S` lie on either shore and put `t=|S|<=s_0`.  Suppose for a
contradiction that `Y=N(S)` has `y<=t-1` vertices.  If `d_Y(v)` denotes the
number of neighbours of `v in Y` in `S`, then

```text
sum_(v in Y) binom(d_Y(v),2) <= lambda binom(t,2).         (2.2)
```

On the other hand `e(S,Y)>=delta t`.  Cauchy--Schwarz gives

```text
sum_(v in Y) binom(d_Y(v),2)
 >= 1/2 ((delta t)^2/(t-1)-delta t).
```

After division by `t/2`, the lower side is

```text
delta^2 t/(t-1)-delta
 > delta(delta-1)
 >= lambda(t-1),
```

contradicting (2.2).  Hence Hall holds for every set of order at most
`s_0` on either shore.

Now suppose `S subset A` is a Hall obstruction of order greater than
`s_0`, and put `Y=B-N(S)`.  Then

```text
|Y|=n-|N(S)| >= n-|S|+1.
```

If `|Y|<=s_0`, then `N(Y) subset A-S` has order at most `n-|S|<|Y|`,
contradicting the small-set result on the other shore.  If `|Y|>s_0`, then
`S,Y` are an excluded anticomplete pair.  Thus no Hall obstruction exists,
and Hall's theorem supplies a perfect matching.  `square`

At `delta=Theta(D)` and `lambda=O(D^(1/3))`, one may take

```text
s_0=Theta(D^(5/3)).                                      (2.3)
```

So outer matching is not the hard part of the logarithmic residual: local
codegree controls all polynomially small Hall rows, and one mixing estimate
controls the rest.

## 3. A sparse space barrier invisible to the outer projection

The next theorem shows why Theorem 2.1 cannot be lifted using only local
four-graph statistics.

### Theorem 3.1 (logarithmic-degree four-resource counterexample)

For every fixed `epsilon>0` and every sequence `k=o(n)`, there exist, for
all sufficiently large even `n`, four-partite four-uniform hypergraphs with
parts

```text
|A|=|B|=n,              |C|=|D|=n+k,
```

such that:

1. every nonzero vertex degree is `(1+-epsilon)d`, where
   `d=Theta_epsilon(log n)`;
2. maximum pair codegree is at most two;
3. the `A-B` projection has minimum degree `Theta_epsilon(log n)`, maximum
   same-shore codegree at most two, and a perfect matching;
4. no hypergraph matching covers `A`.

### Proof

Split `A=A_0 union A_1` and `B=B_0 union B_1` into equal halves.  Split
the two middle parts as

```text
|C_0|=|D_0|=n/2-1,
|C_1|=|D_1|=n/2+k+1.
```

Start with the complete four-partite hypergraph whose atoms `(a,b,c,d)`
satisfy

```text
a in A_i iff c in C_i,       b in B_j iff d in D_j.       (3.1)
```

Sample every allowed atom independently with probability

```text
rho=c_epsilon log n/n^3,
```

where `c_epsilon` is a sufficiently large constant.

Every vertex has `Theta(n^3)` allowed incident atoms.  The ratios between
the largest and smallest such counts are `1+O(k/n)+O(1/n)=1+o(1)`.
Chernoff bounds and a union bound therefore give (1) with positive
probability.

Every pair of vertices lies in at most `O(n^2)` allowed atoms, so its
sampled codegree has mean `O(log n/n)`.  The probability that a fixed pair
has codegree at least three is `O((log n/n)^3)`; summing over `O(n^2)`
pairs shows that (2) holds with probability tending to one.

For a fixed pair `(a,b)`, the candidate atoms use
`|C_i||D_j|=(1+o(1))n^2/4` independent choices, where `i,j` are its labels.
Candidate sets belonging to different `(a,b)` pairs are disjoint.
Consequently the outer projection is an inhomogeneous binomial bipartite
graph with independent edge probabilities

```text
(1+o(1)) c_epsilon log n/(4n).
```

Standard Chernoff and Hall-cut union bounds, with `c_epsilon` large, give
minimum degree `Theta_epsilon(log n)`, same-shore codegree at most two, and
no Hall obstruction.  This proves (3) with probability tending to one.

Finally every atom containing a vertex of `A_0` also contains a vertex of
`C_0`.  A matching covering all `|A_0|=n/2` such vertices would therefore
need `n/2` distinct vertices of `C_0`, but `|C_0|=n/2-1`.  This is
impossible, proving (4).  Since all asserted high-probability events occur
simultaneously, a deterministic realization exists.  `square`

The middle surplus `k` may have exactly the residual order in (1.2); it
does not cure the one-vertex capacity defect.

## 4. The corrected pseudorandom target

Theorem 3.1 proves that the following data are insufficient, even together:

* almost regular logarithmic degree;
* pair codegree `o(D)` (indeed at most two);
* a perfect, expanding outer projection; and
* the correct lower-order middle surplus.

At minimum, an exact residual theorem needs a robust four-resource
fractional Hall condition.  One convenient formulation is: for every
weight vector on any three resource shores, every sufficiently large set
on the fourth shore has enough incident atom mass to dominate the requested
capacities, with positive slack except in the global all-ones direction.
This excludes the `A_0-C_0` space barrier.

Fractional feasibility alone may still leave lattice/divisibility barriers.
Accordingly the honest deterministic target has three layers.

1. **Robust capacity:** a fractional outer-perfect matching lying a
   controlled distance inside every non-global resource inequality.
2. **Transferrals:** bounded alternating absorbers whose incidence
   differences generate the full zero-sum lattice of residual defects.
   The independent-boundary absorber supplies the local candidates, but
   their resource-disjoint packing is not yet proved.
3. **Topology:** after integrality, a switch system that removes every
   directed physical cycle without changing the four resource counts.

The residual scaling remains promising because the local absorber has
superpolynomial schedule room there.  The new obstruction says exactly
what a proof must preserve during the first nibble: not merely degrees and
codegrees, but the robust four-resource capacity polytope and its local
transferral bank.

## 5. Exact remaining theorem

> **Logarithmic Boolean residual theorem.**  Show that the actual residual
> produced from the ordered-diamond Boolean hypergraph at survival
> `m^(-1/3)` satisfies robust four-resource capacity and full transferral,
> and then round it to an outer-perfect matching whose directed Johnson lift
> is acyclic.

Theorem 2.1 proves the outer-projection portion.  Theorem 3.1 shows that the
four-resource capacity clause cannot be deleted or replaced by local
degree/codegree hypotheses.  Establishing robust capacity for the
*actual correlated Boolean residual* is now the sharp next step.
