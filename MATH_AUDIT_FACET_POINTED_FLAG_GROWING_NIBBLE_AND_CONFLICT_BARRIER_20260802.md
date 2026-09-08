# Facet pointed flags: the plain growing-rank bite closes, but the named-resource packing does not

Date: 2026-08-02  
Status: proof-audited degree/codegree calculation, unconditional one-bite
application, and theorem-scope obstruction.  No prime-slope frame packing,
primitive inventory packing, or OR-word upper bound is claimed.

## 0. Outcome

Put

\[
 q=d+2,\qquad c=r-q+1,
 \qquad W=\binom{k}{r}.
\]

Assume `q>=5`, as holds throughout the sufficiently-large canonical range
in which the frame-packing question is posed.  The finitely many smaller
parameters require their own degenerate-chain conventions and are not used
below.

For a module `(C,V,sigma)`, where `|C|=c`, `|V|=q`, write

\[
 T_{a,j}=C\cup\{\sigma_a,\ldots,\sigma_{a+j-1}\},
 \qquad 2\le j\le q-2,
\]

and

\[
 O_a=T_{a,q-2}\cup\{\sigma_{a-2}\}
     =C\cup(V-\{\sigma_{a-1}\}).
\]

The pointed flag at start `a` is

\[
 F_a=(T_{a,2}\subset T_{a,3}\subset\cdots
      \subset T_{a,q-2}\subset O_a).
\]

Let `G` be the simple hypergraph whose vertices are pointed flags and whose
edges are

\[
                    E(C,V,\sigma)=\{F_a:a\in\mathbb Z_q\}.
\]

Then `G` is exactly `q`-uniform and regular with

\[
 \boxed{D=(c+2)(c+1)(k-r)},\qquad
 \boxed{\Delta _2=c+1}.
\]

Consequently

\[
 {q^2\Delta _2\over D}
 ={q^2\over(c+2)(k-r)}\longrightarrow0.
\]

This favorable ratio has one valid uniform consequence: the repository's
growing-uniformity isolated-bite lemma applies to `G`, with internal overlap
`O(q^{-4})` in the canonical range.

It does **not** prove the desired primitive packing.  Two different pointed
flags can contain the same named target or owner.  A matching of `G` only
prevents equality of complete flags; it does not prevent these underlying
resource collisions.  In fact the named-resource conflict degree is
`exp(Theta(q log q))`, whereas `D=Theta(q^6)`.

No located published or repository theorem turns the displayed ratio into a
resource-conflict-free matching of `Theta(W/q^2)` modules.  In particular:

* Gould--Kelly Theorems 1.4 and 1.6 have fixed-uniformity hierarchies;
  independently of that quantifier issue, the full-codegree bottleneck for
  `G` is

  \[
             B\le D^{1/(q-1)}=1+o(1),
  \]

  so their quantitative conclusion is vacuous here;
* the explicit growing-uniformity condition from Alon--Bollobas--Kim--Vu
  fails exponentially;
* an ordinary product-like `q`-round iteration loses the polynomial
  completion degree: after `Theta(q)` bites its expected residual degree is
  `q^6 exp(-Theta(q))=o(1)`.

Thus the positive remaining target is a **correlated prime-slope
frame/interval-spread theorem**, not a generic nibble on `G`.

## 1. Exact degree and codegree

### Proposition 1.1 (flag degree)

Every pointed flag has degree

\[
                         D=(c+2)(c+1)(k-r).
\]

#### Proof

A flag records its bottom set `T_2`, of size `c+2`; the successive singleton
differences from `T_2` to `O` record the next `q-3` tags in their cyclic
order.  It does not record which ordered two elements of `T_2` are the first
two tags.  There are

\[
                         (c+2)(c+1)
\]

choices for that ordered pair, after which the core is their complement in
`T_2`.  The owner `O` has rank `r`, and the omitted cyclic predecessor may
be any element of `[k]-O`, giving `k-r` choices.  These data reconstruct the
unique oriented cyclic module modulo rotation.  Multiplication proves the
formula. \(\square\)

### Proposition 1.2 (maximum pair codegree)

Two compatible flags at adjacent cyclic starts have codegree exactly `c+1`.
Two flags at nonadjacent starts have codegree at most one.  Hence

\[
                         \Delta _2(G)=c+1.
\]

#### Proof

For adjacent starts, the two bottom `(c+2)`-sets intersect in the core plus
the tag common to the two consecutive bottom pairs.  Any of the `c+1`
elements of this intersection may be declared to be that common tag.  The
core and the two outside tags are then fixed, and the two nested chains fix
the rest of the cyclic order.  All `c+1` declarations give compatible
completions.

For nonadjacent starts, the two bottom tag pairs are disjoint, so the
intersection of the bottom sets is the core itself.  The successive
singleton differences in either full flag then determine the cyclic tag
order; the second flag fixes the only order ambiguity in the first bottom
pair.  Thus at most one module contains both flags. \(\square\)

In the canonical regime `q=Theta(sqrt(k))` and `c,k-r=Theta(k)=Theta(q^2)`.
Therefore

\[
 D=\Theta(q^6),\qquad \Delta _2=\Theta(q^2),\qquad
 {q^2\Delta _2\over D}=\Theta(q^{-2}).                 \tag{1.1}
\]

## 2. What the ratio really proves: one plain-flag bite

For an edge `e` of `G`, the normalized internal star overlap used by
`MATH_LEMMA_GROWING_UNIFORMITY_REGENERATIVE_NIBBLE_20260726.md` is

\[
 \sigma(e)={1\over qD}
      \sum_{\{F,F'\}\subset e}d_G(F,F').
\]

There are `q` adjacent pairs in the cyclic edge.  Proposition 1.2 bounds
each of their codegrees by `c+1` and every other pair by one.  Hence

\[
 \sigma(e)
 \le {q(c+1)+\binom q2-q\over qD}
 ={c+1+(q-3)/2\over D}
 =O(q^{-4}).                                           \tag{2.1}
\]

The isolated-bite lemma therefore applies uniformly: marking each module
edge with probability `1/(qD)` and retaining isolated marked edges gives
some matching covering

\[
             {e^{-1}+o(1)\over q}|V(G)|               \tag{2.2}
\]

flag vertices, or `(e^{-1}+o(1))|V(G)|/q^2` module edges.

This is a theorem about equality of whole flags only.  It has no
named-resource conclusion.

Indeed, even the cardinality of a plain flag matching is not the difficult
row.  The number of module edges is

\[
 \begin{aligned}
 E
 &=\binom{k}{c}\binom{k-c}{q}(q-1)!\\
 &=\binom{k}{r+1}{(r+1)_q\over q},                    \tag{2.3}
 \end{aligned}
\]

and a greedy matching in `G` has size at least

\[
                         {E\over1+q(D-1)}.             \tag{2.4}
\]

Relative to `W/q^2`, the main ratio is

\[
 {E/(qD)\over W/q^2}
 ={Eq\over DW}
 ={(r)_{q-1}\over(c+2)(c+1)}\longrightarrow\infty.    \tag{2.5}
\]

Thus the desired number of **flag-disjoint** modules exists by elementary
greedy selection with an enormous margin.  What is missing is the stronger
resource-disjointness.

## 3. The named-resource conflict degree is superpolynomial

Let `P` be a fixed target of a high rank `s=c+j`, `2<=j<=q-2`.  Symmetry and
double counting give the exact number of module edges containing `P`:

\[
                         d_s(P)={Eq\over K_s},
 \qquad K_s=\binom{k}{s}.                              \tag{3.1}
\]

Uniformly in the canonical central band, `K_s=Theta(W)`.  From (2.3),

\[
 {E\over W}={k-r\over q}(r)_{q-1},
\]

and consequently

\[
                         d_s(P)=\exp(\Theta(q\log q)). \tag{3.2}
\]

By contrast, a complete pointed flag has only

\[
                         D=\Theta(q^6)                 \tag{3.3}

module completions.  Therefore the pair-conflict degree on module edges
coming from equality of just one named target is already superpolynomial in
the base degree `D`.

This also gives a direct logical counterexample to contraction: two distinct
flags may have the same `T_{a,j}` but different later singleton extensions.
They are different vertices of `G`, so a `G`-matching may use both, although
their modules collide on that named target.

The conflict-free matching theorems in the current repository fix the base
uniformity before taking the degree limit and require bounded conflict
degrees relative to a power of the base degree.  Equations (3.2)--(3.3)
provide neither condition.  Uniform random sparsification cannot repair the
ratio: it multiplies flag degree and named-target conflict degree by the same
factor.  A structured subcatalogue is required.

## 4. Gould--Kelly does not diagonalize

Theorem 1.4 of Gould and Kelly, *Advancing the Roedl Nibble*,
arXiv:2511.11375, assumes

\[
                         1/D\ll1/A\ll\gamma\ll1/k_0,   \tag{4.1}
\]

where its hypergraph is `(k_0+1)`-uniform.  Here `k_0=q-1`, so this is a
fixed-`q` hierarchy, not a statement uniform along `q->infinity`.
There is no independently growing ambient parameter at fixed `q` in the
canonical relation `q=d(k)+2`; one cannot infer that the polynomial degree
`D=Theta(q^6)` exceeds the hidden threshold.

There is a second, quantitative obstruction which is independent of hidden
thresholds.  The pointed-flag hypergraph is simple, so its full codegree is

\[
                         C_q(G)=1.
\]

The bottleneck parameter in Gould--Kelly Theorem 1.4 therefore satisfies

\[
 B\le\left({D\over C_q(G)}\right)^{1/(q-1)}
   =D^{1/(q-1)}
   =\exp\left(O\left({\log q\over q}\right)\right)
   =1+o(1).                                             \tag{4.2}
\]

Its uncovered-vertex bound

\[
                         nB^{-1+\gamma}(\log D)^A       \tag{4.3}

is consequently larger than the trivial bound `n` for all sufficiently
large `q` and every `A>=1`.  Even suppressing the polylogarithmic factor,
`B=1+o(1)` would cover only an `o(1)` fraction.

Theorem 1.6 of the same paper is an `X`-perfect theorem with the identical
fixed-uniformity hierarchy and the same `B` bottlenecks.  A natural slot
lift, with one `X` vertex for each requested module and edges `{x} union e`,
still enforces only complete-flag disjointness.  It does not encode the
conflict in Section 3.  If all named resources are added as vertices, the
edge size returns to `Theta(q^2)` and one is back at the original growing-
uniformity resource hypergraph.

Thus neither theorem supplies the desired conclusion.

## 5. Other growing-uniformity black boxes

The explicit growing-uniformity criterion audited from Alon--Bollobas--Kim--
Vu requires, in the present notation, at least

\[
                         e^{2q}\Delta _2=o(D/\log D).
\]

Here

\[
 {e^{2q}\Delta _2\log D\over D}
 =\Theta\left({e^{2q}\log q\over q^4}\right)
 \longrightarrow\infty.                               \tag{5.1}
\]

It therefore fails exponentially.  Pippenger--Spencer,
Ehard--Glock--Joos, Delcourt--Postle and the other matching/conflict-free
statements audited in the repository have fixed base uniformity or fixed
power hierarchies and do not provide a uniform diagonal theorem at
`D=Theta(q^6)`.  The repository's unconditional growing-rank result is the
single isolated bite in Section 2; its multiround theorem explicitly assumes
hereditary residual regeneration.

## 6. Why an ordinary `q`-round product nibble loses the degree

One module's pointed deck contains

\[
 q\text{ owners}+q(q-3)\text{ high targets}=q(q-2)    \tag{6.1}

named resources, partitioned among its `q` flags.  One flag contains `q-2`
of these resources.

A bite of `Theta(W/q^3)` resource-disjoint modules uses
`Theta(W/q^2)` resources in each high-rank palette and in the owner palette,
that is, a `Theta(q^{-2})` fraction of each palette.  After `s` such
product-like bites, the marginal survival density is

\[
                         \rho_s=1-\Theta(s/q^2).        \tag{6.2}

Condition on one flag surviving.  Its completion needs the other `q-1`
flags, containing

\[
                         (q-1)(q-2)                    \tag{6.3}

further distinct pointed resources.  Under independent thinning at density
`rho_s`, its expected residual completion degree is exactly

\[
                         D\rho_s^{(q-1)(q-2)}.          \tag{6.4}

For `s=alpha q`, with fixed `alpha>0`, equations (6.2)--(6.4) give

\[
 D\rho_s^{(q-1)(q-2)}
 =q^{6+o(1)}\exp(-\Theta(q))=o(1).                     \tag{6.5}

Thus independent or product-like residuals cannot furnish the hereditary
degree condition needed for `Theta(q)` bites.  They lose typical flag
completions after only `O(log q)` bites.  This is not a no-go theorem for a
correlated construction: a carefully chosen frame may preserve a highly
non-product reservoir.  It is an exact reason why time-zero
`q^2 Delta_2/D=o(1)` cannot be iterated as a generic nibble theorem.

The existing weighted joint-greedy theorem displays the same boundary.  If
each bite has `t_0=alpha W/q^3` modules, after `s` bites its preused-bank
weight has order

\[
                         \Psi_s=\Theta(\alpha s),       \tag{6.6}

because there are `Theta(q)` high palettes and a new candidate has `q`
targets in each.  The sufficient row `Psi+(t_0-1)Gamma<1` therefore supports
only `O(1)` such bites, not `Theta(q)`.

## 7. Exact remaining theorem

The pointed contraction solves neither the labeling collision nor its
global packing.  The proof-safe positive target is:

> **Correlated frame/interval-spread theorem.**  Construct
> `Omega(W/q^3)` mutually resource-disjoint prime-slope frames, or an
> equivalent correlated residual law, so that each frame supplies
> `Theta(q)` mutually compatible facet modules while preserving the low
> labels and protected bank.

Such a theorem yields `Omega(W/q^2)` primitive modules by the proved local
prime-slope amplifier.  No generic matching theorem audited above supplies
it from the pointed-flag degree and pair-codegree alone.

## 8. Sources and scope

The pointed-flag definition and prime-slope local amplifier are in
`MATH_THEOREM_FACET_PRIME_SLOPE_FRAME_Q_AMPLIFIER_20260802.md`.  The
corrected inventory and exact weighted greedy theorem are in
`MATH_THEOREM_FACET_MODULE_LEDGER_AND_WEIGHTED_JOINT_GREEDY_SPREAD_20260802.md`.
The isolated-bite and conditional hereditary-regeneration statements are in
`MATH_LEMMA_GROWING_UNIFORMITY_REGENERATIVE_NIBBLE_20260726.md`.

Primary external references used only for theorem-scope auditing are:

* S. Gould and T. Kelly, *Advancing the Roedl Nibble: New bounds on
  matchings and the list chromatic index of hypergraphs*,
  arXiv:2511.11375, Theorems 1.4 and 1.6;
* N. Alon, B. Bollobas, J. H. Kim and V. H. Vu, *Economical covers with
  geometric applications*, for the explicit growing-uniformity criterion
  quoted in the repository's prior audit.

The present note proves a plain-flag bite and proves that the located black
boxes do not imply the stronger named-resource conclusion.  It neither
proves that a correlated frame packing is impossible nor supplies one.
