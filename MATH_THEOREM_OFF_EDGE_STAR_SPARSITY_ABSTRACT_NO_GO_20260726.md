# Off-edge star sparsity does not imply the annulus fractional colouring bound

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Outcome

The off-edge-star conclusion of
`MATH_THEOREM_LAMINAR_PORT_STAR_SPARSIFICATION_AND_LAYERED_HALL_GATE_20260726.md`
is a real local pseudorandomness statement, but it cannot by itself imply

\[
 \chi_f'(\mathcal H^\#)
 \le (1+o(m^{-1/2}))D_1.                                      \tag{0.1}
\]

In fact there are **simple**, exactly regular hypergraphs at the same
parameter scales which satisfy much more:

* every vertex has degree exactly (D);
* every edge has size at most (K);
* every pair-codegree is (O(\delta D/K));
* for every vertex (v\notin e), at most (\delta D) edges through
  (v) meet (e);

but nevertheless

\[
 \chi_f'(\mathcal G)\ge c\delta KD.                              \tag{0.2}
\]

For the fine-strip scales

\[
 K=\Theta(h\sqrt m)=m^{7/6+o(1)},\qquad
 \delta=\Theta(h/m^{3/2})=m^{-5/6+o(1)},                         \tag{0.3}
\]

this gives

\[
 \Delta_2(\mathcal G)=O(D/m^2),\qquad
 \chi_f'(\mathcal G)\ge m^{1/3-o(1)}D.                           \tag{0.4}
\]

Thus neither maximum codegree, actual edge width, exact target degrees,
nor the summed one-star estimate can establish (0.1).  The obstruction is
a diluted projective plane: a large pairwise-intersecting subfamily has
only a (\delta)-fraction of each vertex star, but it uses (\Theta(K))
vertices per edge, so globally it contains (\Theta(\delta KD)) edges.

This is an **abstract** no-go, not a refutation of the physical strip
hypergraph.  The construction does not have the cyclic interval-flag
kernel of physical strips.  A positive theorem must use that full kernel
(or a global random-port property), not just its off-edge-star corollary.
All vertices in the construction may be regarded as nonmiddle targets;
the separate physical requirement of (2h) middle owners per strip is
deliberately not asserted.  Thus the result rules out an abstract
matching theorem from the numerical hypotheses, while leaving a theorem
from literal strip geometry fully open.

## 1. General construction theorem

### Theorem 1.1 (regular projective-plane blocker)

Let (K,D\to\infty), let (0<\delta<1), and assume

\[
 \delta D/K\longrightarrow\infty,\qquad \delta K\longrightarrow\infty.
                                                                    \tag{1.1}
\]

After harmlessly taking (D) even, there is a finite simple hypergraph
\(\mathcal G\) such that

\[
 d_{\mathcal G}(v)=D\quad\text{for every }v,                       \tag{1.2}
\]

\[
 |e|\le K\quad\text{for every }e,                                 \tag{1.3}
\]

\[
 \Delta_2(\mathcal G)\le C{\delta D\over K},                     \tag{1.4}
\]

and, for every (v\notin e),

\[
 \left|\{f:v\in f,\ f\cap e\ne\varnothing\}\right|
 \le\delta D.                                                      \tag{1.5}
\]

Nevertheless

\[
 \boxed{\ \chi_f'(\mathcal G)\ge c\delta KD.\ }                \tag{1.6}
\]

Here (c,C>0) are absolute constants.

#### Proof

Choose a power of two (r) with

\[
 {K\over8}<r\le {K\over4}.                                       \tag{1.7}
\]

There is a projective plane of order (r).  Denote its point set by
\(P\), its line set by (\mathcal L), and put

\[
 b=|P|=|\mathcal L|=r^2+r+1.
\]

Every line has (r+1) points, every point lies on (r+1) lines, and
any two lines intersect.

Set

\[
 t=\left\lfloor{\delta D\over4(r+2)}\right\rfloor.                \tag{1.8}
\]

By (1.1), (t\to\infty).  For each
\((\alpha,L)\in[t]\times\mathcal L\), introduce a new tag
\(z_{\alpha,L}\), and add the special edge

\[
 e_{\alpha,L}=L\cup\{z_{\alpha,L}\}.                            \tag{1.9}
\]

These edges are simple and pairwise intersecting: their underlying
projective lines intersect even when their tags differ.  A point has
special degree

\[
 d_0=t(r+1),                                                       \tag{1.10}
\]

and a tag has special degree one.  Two points have codegree exactly
\(t\); a point--tag pair has codegree at most one; and two tags have
codegree zero.

It remains to regularize degrees without creating large codegrees.  Put
\(X=P\sqcup\{z_{\alpha,L}\}\).  Give each (x\in X) exactly
\(D-d_{\rm sp}(x)\) private stubs, introduce one new vertex for each
stub, and join the stub to its new vertex by a two-edge.  Let (A) be
the set of new vertices.  Thus every member of (A) currently has
degree one.  Finally place a simple ((D-1))-regular graph on (A).

For completeness, the parity can be arranged without changing any
estimate.  Taking (r) even and (D) even, the number of stubs is

\[
 b\bigl[(D-t(r+1))+t(D-1)\bigr],
\]

which is even.  It is much larger than (D), so a simple
\((D-1))-regular graph on (A) exists.  Every old and new vertex now
has degree exactly (D), proving (1.2).  The filler edges have size two,
while (1.7) gives (r+2<K), proving (1.3).

The only pair-codegree larger than one is the codegree (t) of two
projective points.  Hence

\[
 \Delta_2(\mathcal G)=t
 \le {\delta D\over4(r+2)}
 \le C{\delta D\over K},
\]

which is (1.4).

Fix (v\notin e).  Every edge through (v) meeting (e) contains a
pair (v,u) with (u\in e).  Therefore

\[
 \left|\{f:v\in f,\ f\cap e\ne\varnothing\}\right|
 \le\sum_{u\in e}d(v,u)
 \le |e|t
 \le(r+2)t
 \le {\delta D\over4},                                           \tag{1.11}
\]

where filler pairs have codegree at most one and (t\ge1).  This proves
(1.5), with room.

Finally, all (tb) special edges are pairwise intersecting.  A matching
contains at most one of them.  In any fractional edge colouring, summing
the covering inequalities over the special edges therefore shows that
the total colour weight is at least (tb).  For all sufficiently large
parameters, (1.8) and (1.7) give

\[
 tb\ge c\,\delta D r\ge c\,\delta DK.
\]

Thus (\chi_f'(\mathcal G)\ge tb\ge c\delta KD), proving (1.6).
\(\square\)

### Weighted form of the obstruction

Give weight one to the special edges and zero to every filler edge.  Then

\[
 \nu_w(\mathcal G)=1,
 \qquad
 w(E(\mathcal G))=tb\ge c\delta KD.                               \tag{1.12}
\]

Consequently even the much weaker-looking all-weights statement

\[
 \nu_w(\mathcal G)\ge {w(E(\mathcal G))\over(1+o(1))D}             \tag{1.13}
\]

fails by the factor (\Theta(\delta K)).

## 2. Specialization to the fine-strip scales

Take

\[
 h=m^{2/3+o(1)},\qquad
 K=\Theta(h\sqrt m)=m^{7/6+o(1)},\qquad
 \delta=m^{-5/6+o(1)}.                                            \tag{2.1}
\]

The port degree (D_1) is exponential in (h\log m), so
\(\delta D_1/K\to\infty\).  Theorem 1.1 with (D=D_1) gives

\[
 {\Delta_2\over D_1}
 =O(\delta/K)=O(m^{-2+o(1)}),                                     \tag{2.2}
\]

which matches the noncomparable pair scale in the physical strip
catalogue.  It also gives

\[
 {\chi_f'(\mathcal G)\over D_1}
 \ge c\delta K
 =m^{1/3-o(1)}.                                                     \tag{2.3}
\]

Thus the abstract obstruction survives even after strengthening the
input from the off-edge-star estimate to the numerical maximum-codegree
bound (O(D_1/m^2)).

There is also no obstruction at the level of coarse rank counts.  Colour
the projective points independently into (2H) signed layers.  A line
contains (r+1) points, so when (H=m^{1/2+o(1)}), Chernoff's inequality
and a union bound over the (r^2+r+1) lines give a colouring in which
every line contains

\[
 O(r/H)=O(m^{2/3+o(1)})=O(h)                                      \tag{2.4}
\]

points in each layer.  Hence even the coarse facts “(O(h)) ports per
rank” and “(O(h\sqrt m)) ports in total” do not exclude the blocker.

## 3. What remains genuinely physical

Theorem 1.1 does **not** show that the selected physical strip
hypergraph has a large fractional chromatic index.  It shows exactly
which information has been discarded on the way to (3.4) of the laminar
port note.

The projective-plane blocker has a coherent pairwise-intersecting family
\(\mathcal P\) with

\[
 |\mathcal P|=\Theta(\delta KD),\qquad
 d_{\mathcal P}(v)=O(\delta D),                                   \tag{3.1}
\]

and spreads its intersections over (\Theta(K)) vertices per edge.
The one-star estimate sees only the second quantity.  It cannot sum the
small fractions over all vertices of an edge without losing the fatal
factor (K).

Physical strip edges have additional structure absent above:

1. their vertices are Boolean targets in prescribed ranks;
2. the targets of one strip are cyclic interval flags rather than an
   arbitrary (K)-set;
3. every pair-codegree is governed by the full orbit formula (1.5), not
   merely by its maximum; and
4. in the random exact-target port model, the choices at distinct targets
   have extra global randomness not recorded by the deterministic
   off-edge-star event.

The projective plane distributes essentially the same codegree over all
pairs on one line.  A physical strip has a highly nonuniform flag metric:
most pairs are far in the cyclic/Boolean geometry and have vastly smaller
codegree.  Therefore the plausible surviving route is a global theorem
which uses the **entire within-edge pair kernel**, or a typical-random-port
theorem which rules out coherent finite-plane blockers.  The scalar
condition (3.4) is insufficient.

At minimum, any proof of (0.1) must establish

\[
 |\mathcal A|\le(1+o(m^{-1/2}))D_1                               \tag{3.2}
\]

for every pairwise-intersecting family of selected physical strips
\(\mathcal A\).  This clique inequality is necessary but not sufficient:
the exact fractional-colouring statement is the weighted hereditary
capacity inequality

\[
 \nu_w(\mathcal H^\#)
 \ge {w(E(\mathcal H^\#))\over(1+o(m^{-1/2}))D_1}
 \qquad\text{for every }w\ge0.                                   \tag{3.3}
\]

Theorem 1.1 says that a future argument must derive (3.2)--(3.3) from
the literal cyclic flag geometry.  It cannot derive them from exact
degrees, edge width, maximum codegree, and off-edge-star sparsity alone.

## 4. Disposition

The fractional-colouring route is not refuted for physical strips, but
its present local input is complete as far as abstract matching theory is
concerned.  The next admissible theorem must be one of:

* a physical-strip EKR/supersaturation theorem excluding (3.1);
* a weighted matching theorem using the full pair-orbit kernel; or
* a typical-random-port theorem excluding all weighted projective-plane
  analogues.

Without one of these genuinely global inputs, the required
\(o(m^{-1/2})\) fractional-colouring error cannot follow.
