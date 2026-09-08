# Small-codegree rounding solves every separate-offset clustered token problem

**Status (2026-08-21).**  Conditional only on the same formal clustered
payload capacities used in the profile-capacity theorem, every upper offset
`1<=q<=H` has an integral token/source/target matching, and the sum of its
target deficits over all offsets is `o(W_b)`.  Thus neither the individual
phase-token rows nor their color capacities are an integral obstruction at
any offset.  The proof lifts the exact fractional containment flow to a
3-uniform hypergraph and applies the quantitative small-codegree
edge-colouring theorem of Molloy and Reed.

This theorem still treats different offsets separately.  It does **not**
make the selected targets at `q=1,...,H` into one nested extension chain, and
it does not make their phase tokens arise from common cyclic orders or from
one tight-cycle factor bank.  Those shared-order constraints remain the
physical gate.

## 1. Parameters and the central-quarter truncation

Let `A,B` be disjoint `b`-sets, where `b` is an odd prime, and put

\[
 W_b={2b\choose b},\qquad
 H=\Theta(\sqrt{b\log b}).                           \tag{1.1}
\]

For definiteness retain only payload splits

\[
 J=\{g,g+1,\ldots,b-g\},\qquad g=\lfloor b/4\rfloor. \tag{1.2}
\]

The source layer at split `r` is

\[
 \mathcal U_r=\{U:|U\cap A|=r,\ |U\cap B|=b-r\},
 \qquad L_r=|\mathcal U_r|={b\choose r}^2.          \tag{1.3}
\]

This stronger truncation costs exponentially little.  Uniformly for
`1<=q<=H`, the total occurrence capacity removed from all `r notin J` is at
most

\[
 \sum_{r\notin J}L_r=e^{-\Omega(b)}W_b,              \tag{1.4}
\]

because the `q+1` phase-type capacities at one source split sum to `L_r`.
Consequently, after summing over `q`, (1.4) is still `o(W_b)`.  In particular
the pooled scalar profile-capacity theorem remains

\[
 \sum_{q=1}^H\left[M_q-F_q\right]
 =O(W_b b^{-1/4})+o(W_b)=o(W_b),                    \tag{1.5}
\]

where `M_q=binom(2b,b+q)` and

\[
 F_q=\sum_s\min(P_{q,s},T_{q,s})                    \tag{1.6}
\]

is the exact fractional containment-flow value after the truncation.

## 2. The token hypergraph and its fractional matching

Fix `q`.  For a source split `r in J` and `0<=z<=q`, put

\[
 D_{r,q,z}={b-r\choose z}{r\choose q-z},            \tag{2.1}
\]

and let `n_(r,q,z)` be the clustered phase multiplicity

\[
 n_{r,q,z}=
 \begin{cases}
 b-r-q+1,&z=0,\\
 2,&1\le z\le q-1,\\
 r-q+1,&z=q.
 \end{cases}                                        \tag{2.2}
\]

The number of occurrence tokens of color `c=(r,z)` is the integer

\[
 Q_c={n_{r,q,z}\over b}L_r.                         \tag{2.3}
\]

Indeed, for prime `b` and `0<r<b`, `b` divides `binom(b,r)`; hence
`b^2` divides `L_r`, which proves the asserted integrality.

For a target profile `s`, write

\[
 P_{q,s}={b\choose s}{b\choose s-q},\qquad
 \rho_{q,s}=\min(1,P_{q,s}/T_{q,s}),                \tag{2.4}
\]

with `rho=0` when `T=0`.  The exact fractional containment flow is

\[
 f_q(U,V)=\rho_{q,s}{n_{r,q,z}\over bD_{r,q,z}},
 \quad r=|U\cap A|,\ s=|V\cap A|,\ z=s-r,           \tag{2.5}
\]

for `U subset V`, and zero otherwise.  Its source loads are at most one,
its target loads are at most one, its color-`c` mass is at most `Q_c`, and
its total mass is `F_q`.

Create the 3-uniform hypergraph `\mathcal H_q` with vertex classes

\[
 \mathcal O_q\ \dot\cup\ \mathcal U\ \dot\cup\ \mathcal V_q, \tag{2.6}
\]

where `\mathcal O_q` has `Q_c` distinct token vertices of every color `c`,
and include `(o,U,V)` exactly when `o` has color `(r,z)` and `U subset V`
has that color.  Define

\[
 \theta_q(o,U,V)={f_q(U,V)\over Q_c}.               \tag{2.7}
\]

### Lemma 2.1 (exact fractional lift)

`theta_q` is a fractional matching of `\mathcal H_q` of mass `F_q`.
If

\[
 \alpha(\theta_q)=
 \max_{x\ne y}\sum_{e\supset\{x,y\}}\theta_q(e),  \tag{2.8}
\]

then, uniformly for `1<=q<=H`,

\[
 \alpha(\theta_q)\le
 {1\over {g\choose q}}+e^{-\Omega(b)}.              \tag{2.9}
\]

#### Proof

The load at a source or target is its load under `f_q`; the load at a token
of color `c` is the total color mass divided by `Q_c`, hence at most one.
Summing (2.7) over the `Q_c` tokens recovers (2.5), so the total mass is
`F_q`.

There are three kinds of vertex pairs.  For a compatible source-target pair,

\[
 \sum_o\theta_q(o,U,V)=f_q(U,V)
 \le {1\over D_{r,q,z}}
 \le {1\over {g\choose q}}.                         \tag{2.10}
\]

The last inequality follows from `r,b-r>=g` and
`binom(g,z)binom(g,q-z)>=binom(g,q)`; increasing either ground-set size only
increases the product in (2.1).  For a token-source pair, (2.2)--(2.5) give

\[
 \sum_V\theta_q(o,U,V)
 ={\rho_{q,r+z}\over L_r}\le L_r^{-1}.             \tag{2.11}
\]

For a token-target pair, biregular flag counting gives

\[
 \sum_U\theta_q(o,U,V)
 ={\rho_{q,s}\over P_{q,s}}\le P_{q,s}^{-1}.       \tag{2.12}
\]

All retained `L_r` and `P_(q,s)` are `exp(Omega(b))`, proving (2.9).
\(\square\)

## 3. Quantitative fractional-to-integral rounding

We use the following standard consequence of the Molloy--Reed quantitative
small-codegree edge-colouring theorem.

### Lemma 3.1 (bounded-rank weighted matching rounding)

Let `k` be fixed and let `theta` be a fractional matching in a sequence
of finite `k`-uniform hypergraphs with `alpha(theta)<=alpha=o(1)`.  Suppose
there are scales `D` such that `D max_e theta(e)<=1`,
`D alpha/log |V| -> infinity`, and `D theta(\mathcal H)->infinity`.
Then

\[
 \nu(\mathcal H)\ge
 \left[1-O_k\!\left(
   \alpha^{1/k}\log^4(1/\alpha)\right)\right]\theta(\mathcal H). \tag{3.1}
\]

More precisely, the bracket in (3.1) contains an additional sampling
`-o(1)` term.  In the application below the scale `D` is chosen so that this
term is `o(1/H)`; it is therefore recorded separately in (4.1).

#### Derivation from edge colouring

Independently retain each hyperedge `e` with probability `D theta(e)`.
The scale hypotheses and Chernoff bounds, followed by a union bound over
vertices and vertex pairs, give a simple sampled hypergraph `G` satisfying

\[
 \Delta\le(1+o(1))D,\qquad
 \Delta_2\le(1+o(1))D\alpha,qquad
 |E|\ge(1-o(1))D\theta(\mathcal H).                 \tag{3.2}
\]

Molloy and Reed prove, for fixed `k`,

\[
 \chi'(G)\le \Delta(G)+
 O_k\!\left(\Delta(G)
   (\Delta(G)/\Delta_2(G))^{-1/k}
   \log^4(\Delta(G)/\Delta_2(G))\right).           \tag{3.3}
\]

Here one applies (3.3) with the valid upper parameters
`D_s=(1+epsilon)D` and
`C_s=max(1,(1+epsilon)D alpha)`, where `epsilon=o(1)` is the
concentration error; the theorem does not require the displayed bounds to
equal the actual maximum degree and codegree.

The largest color class in a proper edge coloring is a matching.  Dividing
the edge count in (3.2) by (3.3) proves (3.1).

In the present application this sampling is legitimate uniformly.
Indeed `|V(\mathcal H_q)|=exp(O(b))`, every nonzero token class has
`Q_c=exp(Omega(b))`, while

\[
 {g\choose q}^{-1}=\exp(-o(b))\qquad(q\le H=o(b/\log b)). \tag{3.4}
\]

Thus one may take `D=exp(c b)` for a sufficiently small absolute `c>0`:
all sampling probabilities are below one and `D alpha` dominates every
union-bound logarithm.  This proves the claimed uniform use of (3.1).

## 4. Aggregate all-offset theorem

### Theorem 4.1 (all separate tokenwise offsets round with `o(W_b)` loss)

In applying Lemma 3.1 below one may use
`alpha=(1+o(1)) beta_q` uniformly: by (1.1),
`beta_q=binom(g,q)^(-1)=exp(-o(b))`, whereas the second term in (2.9) is
`exp(-Omega(b))`.

For every `1<=q<=H`, the token/source/target hypergraph has a matching
`\mathcal M_q` such that

\[
 F_q-|\mathcal M_q|
 \le O\!\left(F_q\beta_q^{1/3}
                    \log^4(1/\beta_q)\right)+o(W_b/H),
 \qquad \beta_q={g\choose q}^{-1}.                  \tag{4.1}
\]

Consequently

\[
 \sum_{q=1}^H\left[M_q-|\mathcal M_q|\right]=o(W_b). \tag{4.2}
\]

The same conclusion holds for the lower offsets by complementation.

#### Proof

Apply Lemmas 2.1 and 3.1 with `k=3`; the exponentially accurate sampling in
the proof of Lemma 3.1 makes its auxiliary error `o(W_b/H)`.  Since
`F_q<=W_b`, the `q=1` rounding loss is

\[
 O(W_b b^{-1/3}\log^4 b)=o(W_b).                   \tag{4.3}
\]

For `2<=q<=H<g/2`, `binom(g,q)>=binom(g,2)`.  The function
`x^(1/3)log^4(1/x)` is increasing for all sufficiently small `x`, so the
sum of the remaining rounding losses is at most

\[
 O\!\left(HW_b b^{-2/3}\log^4 b\right)
 =O\!\left(W_b b^{-1/6}\log^{9/2}b\right)=o(W_b),  \tag{4.4}
\]

for the canonical `H=Theta(sqrt(b log b))`; the same calculation holds
whenever `H=o(b^(2/3)/log^4 b)`.  Add the scalar deficit (1.5) to obtain
(4.2).  Complementation interchanges upper and lower offsets without
changing any estimate.  \(\square\)

## 5. Exact consequence and surviving gate

Theorem 4.1 closes the full **separate-offset tokenwise color-capacity
relaxation**, including every interior phase type and every growing offset
`q<=H`.  In particular, neither the determinant-two faces of the natural
matrix nor generic bounded-color matching gaps cause a linear loss in this
dense orbit model: the lifted fractional solution has vanishing pair load,
and bounded-rank small-codegree rounding absorbs the integrality.

What remains is not another fixed-`q` matching problem.  The matchings
`\mathcal M_q` may use different middle-source subsets, different base-phase
tokens, and mutually nonnested upper targets.  A physical product atom must
choose one base phase and one pair of cyclic orders and thereby realize one
common chain

\[
 U=V_0\subset V_1\subset\cdots\subset V_H.         \tag{5.1}
\]

Moreover, many atoms share each tight-cycle order.  The remaining theorem is
therefore a simultaneous-chain/factor-order coinstantiation theorem.  This
note proves no growing-rank tight-cycle decomposition and no coefficient-one
construction by itself.

## Reference for the rounding input

M. Molloy and B. Reed, *Near-optimal list colorings*, Random Structures &
Algorithms **17** (2000), 376--402.  Their quantitative chromatic-index
bound is also stated in D. Y. Kang, D. Kuehn, A. Methuku and D. Osthus,
*New bounds on the size of nearly perfect matchings in almost regular
hypergraphs*, J. London Math. Soc. **108** (2023), 1701--1746.
