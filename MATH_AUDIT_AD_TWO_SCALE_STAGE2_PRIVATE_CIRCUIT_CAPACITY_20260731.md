# Stage-two private-circuit capacity in the proposed two-scale cover-down

Date: 2026-07-31  
Status: exact conditional composition theorem, exact constants, and a sharp
quantifier/capacity audit.  No Boolean private-circuit packing theorem is
claimed.

## 0. Verdict

The two proposed scales are numerically compatible only after four genuinely
global hypotheses are supplied: installed common off states, cross-token
resource privacy, a contracted graphic/root transversal, and literal cap
guards.  Under those hypotheses the final circuit step is exact and is just
graphic Rado.

What is currently called the generic `Theta(n)` circuit *capacity* is only a
necessary upper bound, not a proved lower-bound packing theorem.  In the two
punctured shores there are `2P` old matching atoms.  Pairwise-private circuits
whose old parts have order at least `a n` can service at most

```text
floor(2P/(a n))
 = floor(2(n-1) Cat_n/(a(n+2)))                         (0.1)
```

tokens in total, with the analogous one-shore bound half as large.  The
independent-boundary theorem constructs one full-graph alternating path.  A
matching-preserving circuit needs two internally and physically cross-disjoint
such paths, and a Catalan-scale bank needs them in the `Q`-punctured side
graphs with their old states already present in the bulk matching.  None of
those packing/installability statements is presently proved.

There is also a quantifier obstruction.  A Catalan-size bank of
`Theta(n)`-old-edge circuits occupies `Theta(P)` old matching atoms.  It is not
an `o(P)` protected reserve, so the protected Delcourt--Postle theorem cannot
be applied outside it without losing a linear number of edges.  Conversely,
if the long corridors are fixed before `Q`, Theorem 4.2 has risk length
`Theta(n)` and gives only a constant-fraction survival estimate.  Thus the
long bank has to be chosen jointly with or after `Q` and simultaneously
installed in the side matching.  That conditional matching theorem is the
first missing stage-two condition.

## 1. Exact scales

Use the notation of
`MATH_THEOREM_K_COMMON_BASIS_PRIVATE_CIRCUIT_ALTERATION_20260731.md`:

```text
K = Cat_n,
N = binom(2n,n-1) = nK,
P = binom(2n,n-2) = n(n-1)K/(n+2),
C = Cat_(n+1),
alpha = C/N = 2(2n+1)/(n(n+2)).                       (1.1)
```

Each of the two punctured side representatives is a matching of order `P`.
The two current matchings therefore contain exactly `2P` old atoms.

Suppose stage one starts with a prepacked family indexed by `I`.  For token
`i`, let `ell_i` be the average number of child atoms whose membership in
`Q` punctures a candidate gadget.  If a token is declared unresolved only
when every member of its candidate list is punctured, its unresolved
indicator is at most the punctured fraction `b_i`.  The common-basis marginal
theorem and Theorem 4.2 therefore give a common basis with

```text
|J| <= sum_i b_i <= alpha sum_i ell_i.                 (1.2)
```

In particular, if `|I|<=cN` and every `ell_i<=L`, then

```text
|J| <= c L C
     = [2cL(2n+1)/(n+2)] K.                            (1.3)
```

If the prepacked risk sets are disjoint subsets of the `N` child atoms,
then `sum_i ell_i<=N`, so the sharper direct statement is

```text
|J| <= C = [2(2n+1)/(n+2)]K.                           (1.4)
```

The coefficient in (1.4) tends to four, not one.  This is not an artefact
of the proof: in the abstract risk system consisting of one singleton risk
set per child atom, every common basis punctures exactly `|Q|=C` tokens.
Whether a particular Boolean transparent-gadget packing realizes that sharp
risk system is a separate question.

## 2. Exact private-capacity theorem

### Theorem 2.1 (private old-state budget)

Let `M_-` and `M_+` be the two fixed side matchings, each of order `P`.  Let
`R_i subseteq M_- union M_+`, `i in J`, be nonempty, pairwise-disjoint old
parts of matching-alternating circuits.  If

```text
|R_i| >= a n                                                   (2.1)
```

for every `i`, where `a>0`, then

```text
|J| <= floor(2P/(a n))
     = floor(2(n-1)K/(a(n+2))).                         (2.2)
```

If `J_epsilon` is the set of tokens whose circuits lie in shore
`epsilon`, then separately

```text
|J_epsilon| <= floor(P/(a n))
             = floor((n-1)K/(a(n+2))).                 (2.3)
```

#### Proof

Pairwise privacy implies that the `R_i` are disjoint subsets of a set of
order `2P`, or of a set of order `P` after fixing one shore.  Summing (2.1)
and substituting (1.1) proves (2.2)--(2.3).  `square`

Thus `O(K)` is the exact order of the largest possible private bank, but
Theorem 2.1 is an upper bound.  It does not select one circuit.

Combining (1.3) with (2.2) gives the exact constant compatibility condition

```text
                  a c L <= (n-1)/(2n+1).               (2.4)
```

If all unresolved tokens land on one shore, (2.3) instead requires

```text
                  a c L <= (n-1)/(2(2n+1)).             (2.5)
```

Big-Oh notation suppresses precisely these load-bearing constants.

### Corollary 2.2 (distance cost for the known paired-path circuit)

Take two independent-boundary absorbers with the same outer endpoint pair
`(L,U)` and put `s=|L-U|`.  If they are internally and physically
cross-disjoint, their union gives the matching-preserving circuit of Lemma
1.2 in the cited private-circuit note.  Its old matching part has at least

```text
                         2s+1                            (2.6)
```

atoms.  Consequently a private bank of such circuits at distance at least
`s` has total capacity at most

```text
                         floor(2P/(2s+1)).               (2.7)
```

#### Proof

In the independent-boundary construction the internal geodesic parameter
`d` satisfies `d>=s-1`.  Its off and on states have orders `d+1` and
`d+2`.  Combining the on state of one path with the off state of the other
therefore gives old-state order

```text
(d_1+2)+(d_2+1) >= 2(s-1)+3 = 2s+1.
```

Apply Theorem 2.1 without rounding `2s+1` to `an`.  `square`

For comparison with the sharp disjoint-risk estimate (1.4), capacity alone
can cover all `C` residual tokens only if

```text
                 2s+1 <= n(n-1)/(2n+1).                (2.8)
```

The right side is `(1/2+o(1))n`.  Thus a proof using only one-point
marginals plus fully private paired-path circuits cannot close the worst
sharp risk system when all required endpoint distances exceed about `n/4`.
This is a limitation of that two-black-box proof, not a no-go for correlated
Boolean constructions.

### Theorem 2.3 (gain-one cover-down budget)

Fix one punctured shore whose final matching must have order `P`.  Suppose
the current matching has deficiency `t`, and all `t` missing units are to be
filled by pairwise-private gain-one ears.  Let `R_i` be the off packet of ear
`i`; toggling it replaces `|R_i|` old atoms by `|R_i|+1` new atoms.  If
`|R_i|>=an` for every `i`, then

```text
                         t <= floor(P/(an+1)).          (2.9)
```

Across two shores the sum of their separately serviced deficiencies is at
most `floor(2P/(an+1))`; if one cover-down token requires one ear on **each**
shore, the relevant bound remains the one-shore bound (2.9).

For the known independent-boundary ear joining outer endpoints at distance
`s`, `|R_i|>=s`, and hence

```text
                         t <= floor(P/(s+1)).           (2.10)
```

#### Proof

Before the toggles the matching has `P-t` atoms.  Its pairwise-disjoint off
packets therefore satisfy

```text
sum_i |R_i| <= P-t.
```

The lower bound `sum_i|R_i|>=tan` gives `t(an+1)<=P`.  For the explicit
ear, the construction parameter satisfies `d>=s-1` and the off state has
`d+1>=s` atoms.  `square`

In the sharp disjoint-risk case (1.4), servicing `C` outer-leave units on
one shore by these ears is numerically possible only if

```text
2(2n+1)(an+1) <= n(n-1),                              (2.11)
```

or, for the explicit distance-`s` ear,

```text
                         s+1 <= n(n-1)/(2(2n+1)).       (2.12)
```

Thus the cover-down threshold is asymptotically `a<=1/4`, respectively
`s<=n/4`, rather than the `a<=1/2` aggregate zero-boundary threshold.  Again
this is the exact constant required by the two-black-box route, not a
universal obstruction to correlated/multi-token ears.

### Corollary 2.4 (calibrated C6-to-long-ear arithmetic)

Suppose stage one supplies at most `N/72` prepacked constant gadgets.  With raw
child-puncture risk three, (1.2) leaves at most

```text
                         B <= C/24,                    (2.13)
```

and after charging six further anchor/port events, total risk nine leaves
at most

```text
                         B <= C/8.                     (2.14)
```

Here `B` counts **uncertified gadgets**, not automatically native gain-one
tokens.  If every uncertified gadget has a certified fallback state whose
residual decomposes into at most `g` native gain-one tokens, the stage-two
token count is at most `gB`.

The off-centre independent-boundary construction at side parameter `n` has
old state of order at most `n+1` and on state of order at most `n+2`.
Therefore the **raw scalar** storage check for `B` gain-one ears is

```text
                         B(n+2) <= P.                  (2.15)
```

For the guarded value `B=C/8`, the one-token-per-gadget left/right ratio is
exactly

```text
(n+2)C/(8P) = (n+2)(2n+1)/(4n(n-1)),                  (2.16)
```

which tends to `1/2` and is at most one for every `n>=5`.  For `B=C/24`
the corresponding ratio is

```text
                         (n+2)(2n+1)/(12n(n-1)),       (2.17)
```

which tends to `1/6`.

With fallback multiplicity `g`, multiply (2.16)--(2.17) by `g`.  In
particular the guarded risk-nine estimate plus the worst-case ear length is
automatically within scalar capacity only when

```text
g(n+2)(2n+1) <= 4n(n-1).                               (2.18)
```

For integral `g>=1`, (2.18) permits `g=1` for `n>=5`, but no `g>=2` at
any `n`: the `g=2` row would require
`(n+2)(2n+1)<=2n(n-1)`, whose two sides differ by `7n+2` in the wrong
direction.  Risk three has three times the room.

#### Proof

Equations (2.13)--(2.14) are (1.2) with respectively
`|I|<=N/72,L=3` and `|I|<=N/72,L=9`.  A final matching after `B` gain-one
toggles starts with only `P-B` atoms.  The total old-state demand is at most
`B(n+1)`, so (2.15) is precisely
`B(n+1)<=P-B`.  Substitute `P/C=n(n-1)/(2(2n+1))` to obtain
(2.16)--(2.17); the first inequality reduces to
`2n^2-9n-2>=0`, true for integral `n>=5`.  `square`

Thus the calibrated two-scale proposal genuinely clears the scalar metric
barrier with constant slack **provided that every punctured gadget becomes
one native gain-one token**.  Equations (2.15)--(2.18) do **not** prove that
fallback semantics, pack the ears, place their off states in one matching,
pair their endpoints, or pass the graphic/root/cap rows.

## 3. Exact conditional two-scale completion

The following is the correct composition statement.

There are two different token types.  A matching-alternating **circuit** has
equal old and new cardinalities and preserves the complete outer-coverage
vector.  It can repair degree, anchor, topology, or representative-choice
defects, but it cannot reduce the outer deficiency of a `P-o(P)` DP
matching.  If the stage-one residual tokens are uncovered lower/upper outer
colours, stage two instead needs gain-one ears: an off packet of order `r`
and an on packet of order `r+1` which additionally covers one prescribed
lower and one prescribed upper endpoint.  Before the graphic test, the two
leave shores must be paired by an endpoint template whose induced graph has
a perfect matching.  This is exactly the coupled-leave Hall row, and it is
not implied by private-circuit capacity.

Theorem 3.1 below is stated for zero-boundary physical-defect tokens.  Its
gain-one version is valid after adding the hypotheses that the selected ears
pair and cover the two outer leaves exactly once.  The local
independent-boundary absorber supplies one full-graph ear for a prescribed
pair at distance at least three; it does not supply the required
`Q`-punctured, mutually private ear bank or the endpoint Hall matching.

One elementary endpoint Hall row is nevertheless automatic once the leave
itself is much larger than a polynomial exceptional neighbourhood.

### Lemma 3.0 (far-pair Hall)

Let

```text
S subseteq binom([2r],r),       T subseteq binom([2r],r+2),
|S|=|T|=B.
```

Join `L in S` to `U in T` when `|L-U|>=3`.  Put

```text
Delta_r = max(
  sum_(s=0)^2 binom(r,s)binom(r,s+2),
  sum_(s=0)^2 binom(r-2,s)binom(r+2,s+2)).              (3.0)
```

If `B>=2 Delta_r`, this far-pair graph has a perfect matching.  Every
matched pair is therefore in the local scope of the off-centre
independent-boundary theorem.

#### Proof

For fixed `L`, the number of rank-`r+2` sets `U` with `|L-U|=s` is
`binom(r,s)binom(r,s+2)`: delete `s` elements of `L` and add `s+2` from its
complement.  For fixed `U`, the dual count is
`binom(r-2,s)binom(r+2,s+2)`.  Hence the complement of the far-pair graph
has maximum degree at most `Delta_r`, and the far graph has minimum degree
at least `B-Delta_r>=B/2`.

A balanced bipartite graph of order `B+B` and minimum degree at least
`B/2` has a perfect matching.  Indeed Hall is immediate for sets of order
at most `B/2`; if a larger set `X` had `|N(X)|<|X|`, a vertex outside
`N(X)` would have degree at most `B-|X|<B/2`.  `square`

Here `Delta_r=Theta(r^6)`, while a Catalan-scale `B` is exponential.  Thus
distance at least three is not an obstruction for a sufficiently large
residual bank.  The lemma is deliberately not universal: a small leave may
consist only of close pairs.  It also does not allocate distinct boundary
diamonds or private interiors; those remain separate Hall/packing rows.

### Theorem 3.1 (two-scale private-circuit closure)

Fix a common basis `Q`, the two side representative matchings, and the fixed
physical scaffold.  Suppose stage one leaves a token set `J` satisfying
(1.2).  Assume the following stage-two data.

1. **Installed common off states.**  For every `i in J` there is a nonempty
   option set `S_i`.  Every option in `S_i` is a matching-alternating
   circuit with exactly the same old matching part `R_i`, and
   `R_i` is contained in the current representative matching.  The sets
   `R_i` are pairwise disjoint and avoid every fixed protected scaffold
   edge.
2. **Incidence and physical privacy.**  Options for distinct tokens use
   disjoint outer resources and disjoint physical internal resources.  They
   may meet the fixed graph only at declared attachment ports, and the port
   vertices allocated to distinct tokens are distinct.  Hence any one
   option per token preserves both representative matchings and has no
   cross-token cap conflict.
3. **Cap and defect guards.**  Delete all `R_i` and call the remaining
   physical graph `F_0`.  It is a forest.  Every option is internally a
   forest, repairs its declared token, creates no stage-one token, and at
   each option locally obeys

   ```text
   d_(F_0)(v)+d_(its new edges)(v) <= b(v),              (3.1)
   ```

   where `b(v)=1` at a protected seam anchor and `b(v)=2` otherwise.
   The distinct-port clause in row 2 makes (3.1) a local option test also at
   the ports.
4. **Graphic links.**  Suppress every private internal vertex of an option.
   Its only nonlocal effect is one link `ell(C)` between components of
   `F_0`.  Put `L_i={ell(C):C in S_i}`.  For every `X subseteq J`,

   ```text
   r_gr(union_(i in X)L_i) >= |X|.                     (3.2)
   ```

Then one can choose one circuit for every token, simultaneously preserving
the two representative matchings, all physical caps, physical acyclicity,
and every protected anchor.  Every token in `J` is repaired.

If in addition final components must contain exactly one designated root,
then (3.2) must be supplemented by the exact rooted row: in the selected
link forest on the components of `F_0`, every connected component has total
root weight exactly one.  Equivalently, assume first that every component
of `F_0` contains at most one root.  Add a new vertex `star` and a fixed edge
`star C` for every root-bearing component `C`.  The final exactly-one-root
condition is equivalent to

```text
{star C:C root-bearing} union {selected links}
```

being a spanning tree on `star` and all components of `F_0`.  Thus the
selected links must be a **base**, not merely an independent set, of the
graphic matroid after contracting the fixed root-star.  In particular their
number is forced to be

```text
(number of F_0 components) - (number of roots).          (3.3)
```

Ordinary graphic independence supplies at most one root only when the root
edges are included in the matroid test; it does not supply the at-least-one
part.

#### Proof

Rows 1--3 reduce every simultaneous choice to choosing one contracted link
from each list without a graphic cycle.  Rado's independent-transversal
theorem says this is possible exactly under (3.2).  Expanding the selected
links restores the private option forests; (3.1) gives the caps and privacy
prevents all unlisted interactions.  For roots, adjoining the root-star
makes a cycle exactly when one physical component contains two roots, and
spanning means that no physical component is rootless.  Edge count (3.3)
then makes the augmented graph a tree.  `square`

The theorem is sufficient and exact at the declared interface.  None of its
four hypotheses follows from the scalar estimate (2.2).

If port vertices are not private, then (3.2) is no longer sufficient: the
choice must also satisfy the partition-capacity inequalities at shared
ports.  This is a simultaneous colour-list/graphic/partition problem, not
the one-matroid Rado instance above.  Thus “private” cannot mean only
internally vertex-disjoint corridors; it must include endpoint-slot privacy
or an explicit additional cap-selection theorem.

### Corollary 3.2 (calibrated conditional two-scale absorber)

Let `n>=5`.  Assume the following complete installed-bank data.

1. Stage one has at most `N/72` pairwise-private constant gadgets, one per
   intended unit token, with total `Q`-risk at most nine per gadget.  For a
   surviving gadget its common off state is already contained in the bulk
   matching and its on state is cap-safe and transparent relative to the
   fixed physical scaffold.  For a punctured gadget there is an explicitly
   declared fallback current state in `G_Q`; relative to the bulk, that
   fallback leaves exactly one native lower/upper gain-one endpoint pair and
   the corresponding two slot resources, with no additional deficit.
   The bulk together with all surviving off states and all bad fallback
   states has outer leave exactly the disjoint union of these declared
   endpoint pairs.
2. For the common basis chosen by (1.2), let `J` be the uncertified gadget
   set.  Every token of `J` is assigned a private gain-one ear in the
   `Q`-punctured host, with old state of order at most `n+1`.  The ears pair
   the lower and upper leave shores exactly, have installed pairwise-
   disjoint common off states, and are cross-disjoint from all retained
   stage-one gadgets and the fixed scaffold.
3. After all selected old states are deleted, the on options pass the local
   cap guards and their contracted links, together with the mandatory
   root-star, form the required spanning tree (or satisfy the unrooted
   graphic-Rado row when roots are not required).

Then all stage-one tokens can be repaired simultaneously without changing
`Q`, while preserving both outer palettes, physical acyclicity, protected
anchors, and the declared rooted condition.

#### Proof

Equation (1.2) gives `|J|<=C/8`.  By (2.16) and `n>=5`, the gain-ear old
states plus their `|J|` net new atoms fit the scalar shore budget `P`.
Hypothesis 2 asserts the stronger fact that this scalar packing is actually
installed and resource-disjoint.  Toggle every unpunctured stage-one gadget
and the ears assigned to `J`.  Outer coverage is exact by the gain-one
endpoint pairing.  The local rows and the root-star graphic base in
hypothesis 3 give caps, acyclicity, anchor protection, and roots exactly as
in Theorem 3.1.  `square`

This corollary is the exact two-scale implication suggested by the metric
calculation.  Its hypotheses 2--3, and the positive-density off-state clause
and one-unit native-fallback clause in hypothesis 1, are supply theorems
rather than consequences of existing local gadgets or Delcourt--Postle.  In
particular, if `Q` hits an off-phase atom of a transparent hex, simply
abandoning that atom can expose its old outer vertex and both owner slots in
addition to the designated boundary.  One-point risk counting does not turn
that multi-resource residual into the single endpoint pair required here.

## 4. Why the existing DP reserve theorem does not install stage two

### Proposition 4.1 (positive-density off-state barrier)

Suppose `|J|>=cK` and every private old part has at least `an` atoms, for
fixed `a,c>0`.  Then the installed off-state bank contains at least

```text
                         acN = Theta(P)                 (4.1)
```

matching atoms.  In particular its outer-resource closure has order
`Theta(P)`.

#### Proof

The bank contains at least `acnK=acN` atoms.  Since it is a matching bank,
its old atoms use distinct outer resources in the appropriate host shores,
so closing those resources cannot reduce the order below a positive
constant multiple of `N`.  Finally `P/N=(n-1)/(n+2)`.  `square`

The protected DP theorem loses an additive `O(|Z|)` term for protected host
resources.  Proposition 4.1 therefore makes that loss `Theta(P)`, whereas
its conclusion is useful here only with `o(P)` loss.  The off states do
count as final matching edges, so this is not a resource impossibility; it
shows that one must prove a **DP theorem conditioned on a positive-density
partial matching**, or choose the bulk and circuit bank jointly.  Running
the current theorem on the complement of the bank is not enough.

The same warning applies one scale earlier.  A bank of `Theta(N)`
constant-support stage-one gadgets has `Theta(N)=Theta(P)` common off-state
atoms.  Theorem 4.2 certifies survival of their precomputed corridors under
the later choice of `Q`; it does not force the chosen DP colour to contain
their off states.  Therefore the phrase “embed/pack the constant gadgets”
must itself include a positive-density matching-extension theorem.  If it
means only resource-disjoint prospective supports, the proposed chain
already breaks before the puncture-survival estimate is used.

There is no escape by fixing the long bank before `Q`.  A length-`Theta(n)`
corridor has `Theta(n)` child atoms at risk.  In Theorem 4.2 this means
`alpha L=Theta(1)`, so one-point marginals give only a constant-fraction
list-survival bound, not `1-o(1)` survival.  More exactly, if
`L=lambda n`, then

```text
alpha L = 2 lambda(2n+1)/(n+2) -> 4 lambda.             (4.2)
```

For `lambda >= (n+2)/(2(2n+1))`, the bound for the number of wholly
punctured lists is already at least `|I|` and is completely vacuous.
Stage two must therefore be
chosen after or jointly with `Q`; but the independent-boundary theorem is
for the full off-centre incidence graph, and explicitly does not prove
internal avoidance of the `Q` puncture.

## 5. First false condition and exact remaining theorem

The first unsupported statement in the proposed stage two is:

> “The existing generic `Theta(n)` private-circuit theorem supplies a
> Catalan-size installed bank after `Q`.”

No such theorem currently exists.  What is proved is:

* one prescribed alternating path in the full off-centre graph;
* conditionally, two cross-disjoint paths give one circuit;
* conditionally, a private circuit atlas closes by graphic Rado; and
* necessarily, a private length-`Theta(n)` atlas has only Catalan-order
  capacity.

The exact next theorem is consequently the following positive-density,
fixed-`Q` statement.

> **Stage-two installed-bank theorem.**  For the common basis selected in
> stage one and every residual token set satisfying the explicit bound
> (1.2), first export its exact native boundary.  For actual outer-leave
> tokens, choose the two side representative matchings together with
> pairwise-private common-off-state **gain-one ear** menus in the
> `Q`-punctured host; enforce the endpoint Hall pairing, the one-shore
> budget (2.9) (or the calibrated sufficient budget (2.15)), cap guards,
> and the rooted graphic-base row.  For zero-boundary physical tokens use
> matching-alternating circuit menus instead, with the shore-split capacity
> bounds (2.2)--(2.3) and graphic Rado.  In either case the installed old
> states and the bulk matching must be chosen jointly.

This is strictly stronger than local absorber existence and strictly
different from reserving an `o(P)` protected bank.  A proof could come from
a conditional/reservoir colour theorem, a many-token circuit that amortizes
old support, or a structured shorter-distance pairing reducing the constant
`a`.  Without one of these, the two scales meet only in order notation.
