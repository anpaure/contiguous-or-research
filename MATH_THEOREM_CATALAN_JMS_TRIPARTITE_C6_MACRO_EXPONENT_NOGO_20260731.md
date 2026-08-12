# Joos--Mubayi--Smith does not exactify the Catalan side forest

Date: 2026-07-31  
Status: primary-source applicability audit and exact exponent obstruction.
The conclusion is uniform over every admissible fixed common basis `Q`.
It does **not** rule out a future application on genuinely small,
resource-disjoint residual blocks.

Primary source: Felix Joos, Dhruv Mubayi and Zak Smith,
*Conflict-free Hypergraph Matchings and Coverings*,
[arXiv:2407.18144v2](https://arxiv.org/abs/2407.18144), revised
24 June 2026.  The theorem and condition labels below are those of v2.

## 0. Verdict

The natural tripartite encoding is formally of the right fixed type:

* `P` is the punctured lower outer palette;
* an edge of `H_1` is one ordinary diamond atom, hence has profile
  `(p,q)=(1,3)` on `P,Q`;
* an edge of `H_2` is one contracted, already-planted suspended-hex
  gain-one macro, hence has profile `(1,r)=(1,3)` on `P,R` after the
  three non-`P` resources are duplicated into `R`;
* fixed mixed conflicts can forbid collisions between an `R`-duplicate and
  the actual upper/slot resource which it represents.

Nevertheless Theorem 3.1 of Joos--Mubayi--Smith cannot be applied.  In the
fixed-`Q` ordinary host,

\[
 d=\Theta(n^2),\qquad |P\cup Q|=\exp(\Theta(n)),\qquad
 \Delta_2(H_1)=\Theta(n).                                      \tag{0.1}
\]

Condition (S2) would force

\[
                         \varepsilon\ge2^{-1/3}-o(1),           \tag{0.2}
\]

whereas (H2) would force

\[
                         \varepsilon\le\frac12+o(1).           \tag{0.3}
\]

These are incompatible.  This is not an artefact of a bad common basis:
the lower bound on `Delta_2` below follows from the uniform fixed-`Q` edge
ledger.  The v2 proof is even farther from this regime: in the proof of
Theorem 4.2, source lines 652--655, the authors explicitly take
`epsilon_0<1/(2(k-1))` for a `k`-uniform first-stage host.  Here `k=4`, so
their proved range has `epsilon<1/6`.

There is a second, independent mismatch.  The unpunctured resource-private
packet bank of order greater than `P/54` is a **global** supply statement.
The completion theorem requires a **local** supply of at least
`d^epsilon` sufficiently spread `H_2` choices at every vertex of its
designated `P`-side.  One planted packet per target has completion degree
one and violates (H4) immediately.  The owner-transversal and frozen-cap
blockers show that the missing local spread does not follow from the formal
quadratic catalogue.

Thus the arbitrary-`Q`, `P-o(P)` Delcourt--Postle side forest plus the
planted suspended hexes is **not** exactified by the Joos--Mubayi--Smith
black box.

## 1. The precise theorem being audited

The relevant result is Theorem 3.1 (the formal version of Theorem 1.1), not
the covering corollary Theorem 2.1.  For fixed `p,q,r,ell`, it chooses

\[
        0<\varepsilon<\varepsilon_0(p,q,r,\ell),qquad d\ge d_0,
\]

and assumes disjoint vertex sets `P,Q,R` satisfying (S2)

\[
 d^\varepsilon\le |P|\le |P\cup Q|
                       \le\exp(d^{\varepsilon^3}).               \tag{1.1}
\]

Every `H_1` edge has `p` vertices in `P` and `q` in `Q`; every `H_2`
edge has one vertex in `P` and `r` in `R`.  The host conditions on pages
4--5 are

\[
 (1-d^{-\varepsilon})d\le\delta_P(H_1)
       \le\Delta(H_1)\le d,                                    \tag{1.2}
\]
\[
 \Delta_2(H_1)\le d^{1-\varepsilon},                           \tag{1.3}
\]
\[
 \Delta_R(H_2)\le d^{\varepsilon^4}\delta_P(H_2),\qquad
 d_{H_2}(x,v)\le d^{-\varepsilon}\delta_P(H_2).                \tag{1.4}
\]

Subject also to the bounded conflict conditions (C1)--(C5) and
(D1)--(D4), Theorem 3.1 returns a `P`-perfect conflict-free matching
`M subset H_1 union H_2`; at most

\[
                         d^{-\varepsilon^4}|P|                   \tag{1.5}
\]

vertices of `P` use `H_2` edges.  It makes no coverage assertion about
`Q` or `R`.

Conflicts containing exactly one `H_2` edge are excluded by (D1).  They
must instead be checked using the weighted general conditions (E1)--(E6)
on pages 8--9, with

\[
 A(E)=\prod_{x\in V_P(E)}d_{H_2}(x)^{-1}.                        \tag{1.6}
\]

This is the relevant version for one ordinary atom conflicting with one
contracted macro.

Theorem 2.1 is not a substitute.  It produces a conflict-free **covering**
of all vertices of a uniform host, with all but `d^{-epsilon^5}N` vertices
covered once and no vertex covered more than twice.  It is not a perfect
matching and has the same size/codegree hypotheses.

## 2. Natural fixed-four encoding

Use the side-host notation

\[
 \Pi=\binom{2n}{n-2},\qquad N=\binom{2n}{n-1},\qquad
 C=\operatorname{Cat}_{n+1}.                                   \tag{2.1}
\]

For an admissible common basis `Q`, the capacity-slot host `G_Q` has one
vertex for each retained lower colour, one for each upper colour, and one
or two literal vertices at each physical owner.  One ordinary atom is

\[
                         \{D,V,(x,i),(y,j)\}.                    \tag{2.2}
\]

Consequently set

\[
 \mathsf P=\{D\},\qquad
 \mathsf Q=\{V\}\mathbin{\dot\cup}\{\text{literal owner slots}\},
 \qquad H_1=G_Q.                                                 \tag{2.3}
\]

This gives `(p,q)=(1,3)`.  For a suspended hex planted in its two-atom off
state, switching on adds exactly the four resources of its designated atom.
Duplicate that atom's upper and two slot resources into a disjoint set
`mathsf R`; the contracted choice is an `H_2` edge with profile `(1,3)`.
With one `R`-copy per actual resource, equality inside `R` forbids two
macros from sharing that resource, while mixed conflicts must forbid an
`R`-copy from meeting its original `Q` resource.  If option-specific
`R`-copies are used instead, both kinds of actual collision must be inserted
as conflicts and checked after projection.

This contraction is valid only after the corresponding off state has been
planted.  A conflict hypergraph can forbid selections; it cannot impose the
positive implication that selecting a macro also selects its two off atoms.
Thus alternative unplanted formal hexes are not automatically legal `H_2`
choices.

More precisely, let `O_a` and `N_a` be the off and on phases of a packet
whose target atom is `t_a`.  The identity

\[
          \operatorname {inc}(N_a)
          =\operatorname {inc}(O_a)\mathbin{\dot\cup}
             \operatorname {inc}(t_a)                         \tag{2.4}
\]

justifies replacing `O_a` by `N_a` after a contracted macro for `t_a` is
chosen.  It does not justify adding `N_a` when `O_a` is absent.  Therefore a
sound contracted model must install all offered `O_a` first, delete their
resources from the ordinary host, and decode a selected macro by the literal
replacement `O_a -> N_a`.  Conflict-freeness alone cannot enforce this
positive prerequisite.

## 3. Uniform exponent contradiction

The exact fixed-`Q` ledger is

\[
 |E(G_Q)|\ge4\Pi\binom n2-2C(n^2-1),\qquad
 \Delta(G_Q)\le2(n+1)(n+2),                                    \tag{3.1}
\]

and

\[
 {C\over\Pi}={2(2n+1)\over n(n-1)},\qquad
 {N\over\Pi}={n+2\over n-1}.                                  \tag{3.2}
\]

It follows that

\[
 |E(G_Q)|=(2n^2-O(n))\Pi,qquad
 |V(G_Q)|=(4+O(n^{-1}))\Pi.                                    \tag{3.3}
\]

If (1.2) held, average degree and the maximum lower-colour degree would give

\[
              c n^2\le d\le4n^2                               \tag{3.4}
\]

for an absolute `c>0` and all sufficiently large `n`.

The codegree lower bound is also uniform in `Q`.  There are at most
`2(n+2)Pi` compatible pairs `(V,(x,i))` consisting of an upper colour and
an extant slot at an owner `x subset V`.  Every host edge contributes
exactly two such pair incidences.  Hence

\[
 \Delta_2(G_Q)\ge {|E(G_Q)|\over(n+2)\Pi}=2n-O(1).               \tag{3.5}
\]

Now Stirling gives

\[
                  \log\Pi=(2\log2+o(1))n.                       \tag{3.6}
\]

Combining (1.1), (3.4), and (3.6) requires

\[
 n^{1-o(1)}\le O(n^{2\varepsilon^3}),
 \qquad\text{so}\qquad \varepsilon\ge2^{-1/3}-o(1).           \tag{3.7}
\]

Combining (1.3), (3.4), and (3.5) requires

\[
 n^{1-o(1)}\le O(n^{2(1-\varepsilon)}),
 \qquad\text{so}\qquad \varepsilon\le\frac12+o(1).           \tag{3.8}
\]

Equations (3.7)--(3.8) contradict each other.  The proof uses only the
fixed-`Q` ledger and therefore applies to every common basis.  It also
survives any reserve deletion that leaves a constant-density ordinary host:
the vertex count remains `Theta(Pi)`, edge count `Theta(Pi n^2)`, and the
same compatible-pair averaging gives `Delta_2=Omega(n)`.

## 4. Why the `Pi/54` packet supply is not the required reserve

The suspended-hex theorem gives a pairwise-resource-private unpunctured bank
of more than `Pi/54` packets.  This proves linear **total** supply.  It does
not verify (1.4).

Indeed, (1.4) itself forces

\[
                         \delta_P(H_2)\ge d^\varepsilon.         \tag{4.1}
\]

To see this, take an `H_2` edge through `x` and one of its `R` vertices
`v`; then `1<=d_H2(x,v)<=d^{-epsilon}delta_P(H_2)`.  The weighted
conditions (H3')--(H4') used with (E1)--(E6) give the same conclusion.

A resource-private prepacking has one planted off state and therefore one
contracted completion macro at each of its packet targets.  On the whole
palette most targets have degree zero; even after restricting to packet
targets the minimum degree is one.  Both violate (4.1).  Merely duplicating
one physical macro does not create physical alternatives: the mixed
conflicts recording their common actual resources inherit the same
concentration.

The formal `2n(n-2)` catalogue through a target has the right numerical
order, but it is not simultaneously planted.  Moreover all formal choices
meet an `n`-owner transversal, so protecting those owners can reduce the
available degree to zero; and every choice changes the pointwise common-cap
map.  Hence neither local spread nor protected/common-cap compatibility
follows from the catalogue count.

## 5. The exact `j_2=1` collision row

There is one useful positive calculation.  It shows that ordinary
cross-copy resource collisions are not the source of the no-go.

Let

\[
                 \pi:\mathsf R\longrightarrow\mathsf Q       \tag{5.1}
\]

be the projection taking an `R`-duplicate to the actual upper/slot resource
which it represents.  First assume that there is exactly one `R`-copy of
each actual resource, so `\(\pi\)` is injective.  For
`\(x\in\mathsf P\)` and `\(v\in\mathsf Q\)`, put

\[
 \kappa(x,v)=|\{e\in H_2:x\in e,\ v\in\pi(e\cap\mathsf R)\}|,
 \qquad d_x=d_{H_2}(x).                                      \tag{5.2}
\]

Let `D_col` contain the pairs `{f,e}` with `f in H_1`, `e in H_2`
which are disjoint in the abstract tripartite host but satisfy

\[
          (f\cap\mathsf Q)\cap\pi(e\cap\mathsf R)\ne\varnothing.
                                                                    \tag{5.3}
\]

### Lemma 5.1 (literal mixed-collision bounds)

Assume `Delta(H_1)<=d`.  The family `D_col` has type `(j_1,j_2)=(1,1)`
and satisfies the following exact bounds.

1. For every `e in H_2`,

   \[
       |\{f:\{f,e\}\in\mathcal D_{\rm col}\}|\le3d.          \tag{5.4}
   \]

   Hence (E5) holds whenever `ell>=3`; (E6) is vacuous because its
   index set is `j' in [j_1-1]=[0]`.
2. For every `x in mathsf P`, using the paper's unavoidability
   `A({f,e})=d_x^{-1}`,

   \[
               A((\mathcal D_{\rm col})_x^{(1,1)})\le3d.       \tag{5.5}
   \]

   Thus (E2) holds for every fixed positive `delta` and all sufficiently
   large `d`.
3. For a fixed `f in H_1`,

   \[
   A(((\mathcal D_{\rm col})_x^{(1,1)})_{[\{f\},\varnothing]})
       \le {1\over d_x}\sum_{v\in f\cap\mathsf Q}\kappa(x,v).
                                                                    \tag{5.6}
   \]

   Consequently (E3) is exactly an **aggregate projected codegree** row.
   For example, if for some `gamma>epsilon`

   \[
               \max_{x,v}{\kappa(x,v)\over d_x}\le d^{-\gamma},
                                                                    \tag{5.7}
   \]

   then (E3) follows for large `d`, since an `H_1` edge has three
   `mathsf Q` resources and `3d^{-gamma}<=d^{-epsilon}`.

#### Proof

An `H_2` macro has three `R` resources.  For each projected resource there
are at most `d` incident `H_1` edges, proving (5.4).  Sum (5.4) over the
`d_x` macros through `x` and multiply by `d_x^{-1}` to obtain (5.5).
For (5.6), charge every macro conflicting with the fixed `f` to one of the
at most three projected resources in `f cap mathsf Q`; overcounting only
increases the right side.  The claims about (E2), (E3), (E5), and (E6) are
their literal definitions in Section 4.3 of the paper. `square`

The exponent slack in (5.7) is load-bearing only for the harmless constant
three.  In the Boolean host the natural local ratios are powers of `n`, so
one would choose the theorem's `epsilon` strictly below the available
projection exponent if the global exponent obstruction of Section 3 were
absent.

For this bijective projection the remaining weighted host rows also have a
literal interpretation.  Condition (H3') is the global projected load

\[
               \max_v\sum_x{\kappa(x,v)\over d_x}
                         \le d^{\varepsilon^4},                 \tag{5.10}
\]

whereas (H4') is the pointwise version of (5.7) at exponent `epsilon`.
Neither row follows from the total size of a prepacked packet bank.

### Proposition 5.2 (option-specific duplication does not create spread)

Suppose all `d_x` alleged alternatives through a target `x` use the same
actual upper/slot resource `v`.

* If they use one honest common vertex `r_v in mathsf R`, then

  \[
                    d_{H_2}(x,r_v)=d_x,                         \tag{5.11}
  \]

  contradicting (H4') for every `epsilon>0`.
* If `r_v` is replaced by private option-specific copies, fix an ordinary
  `H_1` edge `f` using `v` whose `mathsf P` vertex is different from `x`.
  Thus `f` is abstractly disjoint from every alternative through `x`.
  Every alleged alternative forms a collision conflict with `f`, and the
  left side of (5.6) is exactly

  \[
                         d_x^{-1}d_x=1,                          \tag{5.12}
  \]

  contradicting the (E3) bound `d^{-epsilon}`.

For every upper or slot resource of an ordinary target atom in the
**unpunctured** Boolean host, such an `f` exists when `n>=3`.  For an upper
resource, choose a different rank-`n` lower subset of the same rank-`n+2`
upper set.  For a slot at an owner `X`, use a Johnson neighbour which
deletes a different element of `X`; the other owner has at least its first
slot.  The same conclusion holds in a fixed-`Q` residual block whenever
the target bank explicitly requires residual degree at least two at each
projected resource.  An arbitrary puncture can delete every such
abstractly disjoint edge; in that case the private-copy conclusion is not
asserted for that resource and its local availability must be audited
instead.

Thus the projection fibres, not the formal labels, must be dispersed.
Duplicating a fixed physical target triple cannot supply the required
`H_2` degree.  A one-to-one `Q`/`R` copy is sound only together with all
conflicts (5.3); private copies require the stronger aggregate row (5.6),
which detects the attempted evasion.

## 6. What remains plausible and what is not closed

Some local conflict estimates have the right scale, but they cannot repair
Section 3.

* For ordinary atoms, conflicts saying that `j<=L` selected physical edges
  form a simple `j`-cycle have degree `O_L(d^{j-2})` and higher codegree
  `O_L(d^{j-j'-1})`.  For fixed `L` and any `epsilon<1`, these fit
  (C1)--(C5); there are no size-two cycle conflicts.
* The size condition (E1) is automatic for `mathcal D_col`: every member
  has size two and contains one `H_2` edge.  Condition (E4) is irrelevant
  because it applies only when `j_2>=2`.
* An ordinary atom colliding in an actual upper/slot resource with one
  contracted macro is a conflict with exactly one `H_2` edge.  Lemma 5.1
  verifies (E2), (E3), (E5), and (E6) exactly under the aggregate dispersion
  row (5.7).  The complete mixed catalogue including protected resources
  and macro-expanded cycles has not been proved (E1)--(E6)-bounded.
* Illegal protected-anchor choices should be deleted from `H_2`, not hidden
  as conflicts.  The owner-transversal blocker shows that this deletion can
  destroy (4.1).
* A frozen pointwise common cap is not a bounded collision condition.  It
  can block every orientation of a target catalogue.  Regenerating a common
  cap is a downstream global matching condition.
* Since `ell` is fixed before `d`, bounded conflicts can forbid physical
  cycles only up to a fixed length.  The theorem does not give a linear
  forest or one-reset-per-component topology.  Letting the forbidden length
  grow with `n` is outside Theorem 3.1.

## 7. Exact counterfactual conclusion and actual residue

If one had a different host satisfying every JMS hypothesis and if the mixed
conflicts faithfully encoded all duplicate collisions, then Theorem 3.1
would give:

1. every lower outer colour in `P` exactly once;
2. at most `d^{-epsilon^4}|P|` contracted macro choices;
3. actual upper/slot disjointness only to the extent encoded by verified
   mixed conflicts; and
4. avoidance of any declared fixed-size physical cycle conflicts.

If the lower and upper banks have equal order and every expanded selected
object contributes one new lower and one new upper colour, verified upper
injectivity would then imply upper saturation by counting.  Likewise,
literal collision conflicts would imply cap two and anchor cap one.  These
are consequences of the **encoding plus boundedness**, not conclusions of
JMS alone.

It would still not give:

* extension of the already chosen Delcourt--Postle near forest;
* a long-cycle-free physical forest;
* a compatible endpoint bank or common basis `Q`;
* preservation or regeneration of the common cap; or
* residence, all-width upper witnesses, or the final compiler.

The only plausible remaining JMS use is block-local: partition a declared
reserve into polynomial or sufficiently subexponential, resource-disjoint
blocks, and within every block construct `d^epsilon` genuinely different
planted completion choices per target with (E1)--(E6)-bounded cross-conflicts.
No such block decomposition follows from the current `P-o(P)` forest or the
`Pi/54` bank.  Cross-block physical collisions and the common cap would
still need a separate theorem.

## 8. Relation to the current exact target

The arbitrary-common-basis theorem remains useful: it supplies the
`Pi-o(Pi)` physical body for every chosen `Q`.  The suspended hex remains
useful: it supplies an exact planted `2 -> 3` gain-one identity and a linear
raw bank.  What is missing is still the correlated theorem which builds the
body and the planted off bank together so that the leave is packet-aligned,
then switches while preserving topology and regenerating the common cap.

Joos--Mubayi--Smith does not perform that correlation.  Its `H_2` stage is a
random completion reservoir for the leave produced by its own pseudorandom
`H_1` matching, under hypotheses which the global Catalan host fails.

## 9. Independent arithmetic audit

Run

```text
python3 scratch/audit_catalan_jms_tripartite_c6_macro_exponent_nogo_20260731.py
```

The dependency-free audit checks the exact Catalan/binomial ratios, the
compatible `(V,slot)` pair-incidence lower bound for `Delta_2`, the empty
epsilon interval, the sharp `3d` rows (5.4)--(5.5), the vacuity of (E6) at
`j_1=1`, the normalized-one private-copy obstruction (5.12), and the
explicit abstractly-disjoint `H_1` witnesses for every canonical
unpunctured target resource at `3<=n<=16`.  It writes

```text
scratch/catalan_jms_tripartite_c6_macro_exponent_nogo_20260731.audit.json
```

with status `PASS`.  Its scope is arithmetic and the pure `(1,1)`
cross-projection collision family only.  It does not audit or assert a
robust target bank, protected root/graphic completion, or compiler cap.
