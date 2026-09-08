# Two-bank switches: exact residence, upper-provider, and common-cap calculus

Date: 2026-07-31  
Status: dimension-uniform switch theorems and a conditional integral repair
criterion; positive scalar slack alone is proved insufficient; no `K17` word
or all-dimension construction is claimed

## 0. Result and scope

Let

\[
 P=(P_1,\ldots,P_a),\qquad Q=(Q_1,\ldots,Q_b),\qquad a+b=W,
\]

be the two contiguous banks of a lower-rainbow Johnson cycle, and put

\[
 F_0=P_a\cap Q_1,\quad F_j=Q_j\cap Q_{j+1}\ (1\le j<b),
 \quad F_b=Q_b\cap P_1.
\]

The nonflat depth-two row is

\[
                     Z=P_1\cdots P_aF_0\cdots F_b.       \tag{0.1}
\]

A residual incidence rectangle, or more generally a conformal alternating
circuit, cuts the owner cycle into fragments and reglues a signed
permutation of those fragments.  If it leaves the marked bank `P` fixed and
the result connected, its action on `Z` has three exact and quite different
descriptions.

1. **Residence is a finite-state weighted run monoid.**  Reversing a fragment preserves all
   of its internal coordinate runs.  Only the new seams can change the
   depth-two replay defect.  Capped leading/trailing run lengths compute the
   change exactly.
2. **Upper providers form an interval-union monoid.**  Prefix and suffix
   union chains, truncated at rank twelve, compute the complete signed
   change of every rank-ten, -eleven, and -twelve provider load.  The effect
   is local in *fragment state*, but not in a bounded number of physical
   rows: a long low-rank prefix can cross a seam.
3. **A fixed common cap transports except in a five-row seam halo.**  After
   reflecting the unchanged fragment interiors, only the replaced seam
   facets and their exact envelope/cell collars must be replayed.  The
   residual obstruction clutter still has rank at most three.

These statements yield a genuine monotone potential and an integral
min-cost Hall theorem for an **orthogonal guarded switch bank**.  They do
not yield an automatic repair theorem from scalar slack.  In fact positive
scalar slack, ordinary Hall, legal envelopes, and even a permanent bit at
every position can coexist with no common cap.  Thus the right remaining
all-dimension statement is a guarded switch-expansion theorem, not a
counting inequality.

For calibration only, the authenticated connected `K17` `OPTIMAL28` row has

```text
rank-nine / rank-eight rows                 4108 / 20203
strict internal depth-two short runs                2392
unhosted row-bit obligations / failed rows    3759 / 3568
upper holes at ranks 10 / 11 / 12          1900 / 911 / 128
scalar lower-cell slack                              3293.
```

The fact that `3293 > 1900+911+128` has no formal consequence: upper
providers and lower common-cap cells are different correlated resources.

## 1. A rectangle is a signed fragment exchange

Consider a Hamilton owner cycle with every consecutive intersection of the
required lower rank.  Delete the selected incidences of a conformal
alternating circuit.  The retained cycle is a collection of paths.  If the
new incidences restore one cycle, they order and orient those paths into a
signed cyclic permutation.

### Lemma 1.1 (signed-fragment normal form)

Every Hamilton-safe conformal circuit acts on the owner word by a signed
permutation of the retained path fragments.  If all deleted incidences lie
in the interior of `Q`, the marked word `P` is unchanged and `Q` is replaced
by a signed permutation of its fragments.

A two-incidence rectangle which preserves one cycle has the familiar
two-opt form.  After a cyclic choice of indices,

\[
 Q=A\,B\,C\quad\longmapsto\quad Q'=A\,\overleftarrow B\,C. \tag{1.1}
\]

#### Proof

Deleting the old selected incidences from one cycle leaves paths, each with
two boundary occurrences.  Contracting the paths gives the retained
boundary matching.  The inserted incidences give a second matching.  Their
union is one cycle precisely in the Hamilton-safe case.  Traversing that
cycle orders the contracted paths and chooses an orientation for each.
Expanding them proves the claim.  With two cuts there are two paths, and
the nontrivial one-cycle reconnection reverses one of them.  \(\square\)

The induced operation on the facet rail is equally explicit.  Use sentinels
`Q_0=P_a` and `Q_(b+1)=P_1`.  If `B=Q_i...Q_j`, then the old facet subword
is

\[
 Q_{i-1}\cap Q_i,
 Q_i\cap Q_{i+1},\ldots,Q_{j-1}\cap Q_j,
 Q_j\cap Q_{j+1},                                  \tag{1.2}
\]

whereas the new subword is

\[
 Q_{i-1}\cap Q_j,
 Q_j\cap Q_{j-1},\ldots,Q_{i+1}\cap Q_i,
 Q_i\cap Q_{j+1}.                                  \tag{1.3}
\]

Thus all internal facet values are merely reversed.  Exactly the two seam
facets are replaced.  Rectangle legality says that both new seams are
Johnson adjacencies, so the displayed intersections have the intended
rank.  A circuit with `t` cuts is the same construction with at most `2t`
new seam facets.

## 2. Exact depth-two replay calculus

For a set word `V=(V_0,...,V_(n-1))` and a coordinate `x`, let `w_x(V)` be
its binary membership word.  A positive run is **strict** if it meets
neither linear endpoint.  Define

\[
 \rho_2(V)=
 \sum_x\sum_{R\text{ strict positive run of }w_x(V)}
 |R|\,\mathbf 1_{|R|<3}.                            \tag{2.1}
\]

Also define the literal replay-defect set

\[
 \operatorname{Def}_2(V)=
 \{(i,x):x\in V_i\setminus(E_i\cup E_{i+1}\cup E_{i+2})\}, \tag{2.2}
\]

where `E` is the maximal three-window envelope of `V`, with the usual
linear truncation.

### Lemma 2.1 (run identity)

\[
                  |\operatorname{Def}_2(V)|=\rho_2(V).          \tag{2.3}
\]

In particular, `V` is replayed exactly by its maximal depth-two inverse if
and only if `rho_2(V)=0` (together with nonemptiness of every envelope
letter).

#### Proof

For one coordinate, taking the maximal envelope is three-window erosion and
replaying is three-window dilation.  An endpoint run survives.  A strict run
of length at least three is recovered exactly.  A strict run of length one
or two has empty erosion and every one of its positions is lost.  Summing
over coordinates gives (2.3).  \(\square\)

For one binary word retain:

* whether it is all one;
* its first and last bit;
* its leading and trailing positive-run lengths, capped at three; and
* its internal short-run defect tokens.

Concatenation joins the two run-length encodings and merges the two boundary
runs exactly when both boundary bits are one.  This is an associative finite
operation on the capped boundary data; the defect count is its additive
weight, and labelled internal defect tokens are transported separately.
Taking the product over the ground-set coordinates gives a finite-state
weighted monoid `R_3(V)`.

### Theorem 2.2 (exact seam locality)

For a signed-fragment switch, every replay defect lying strictly inside a
retained fragment is transported bijectively.  All created or destroyed
defects are determined exactly by composing the `R_3` boundary states at
the new seams.  Reversal swaps leading and trailing states and preserves
the internal defect multiset.

Consequently the exact residence change of a `t`-cut circuit is computable
from its `2t` seam states; it is unnecessary to rescan any fragment
interior.

#### Proof

Reversal preserves run lengths and changes only their order.  Concatenating
the signed fragments can affect only runs meeting a new seam.  The capped
length three records exactly whether such a merged or newly internal run is
short.  Lemma 2.1 converts the resulting run calculation into the replay
calculation.  \(\square\)

This is locality in a finite-state sense.  It does not say that choosing a
geometrically short incidence rectangle gives a small owner fragment.

## 3. Exact rank-10--12 provider calculus

For a nonempty set word `V`, let

* `u(V)` be the union of all its letters;
* `P_h(V)` be the multiset of unions of all nonempty prefixes having rank at
  most `h`;
* `S_h(V)` be the analogous suffix multiset; and
* `I_h(V)` be the multiset of unions of all nonempty intervals having rank
  at most `h`.

Multiplicities record physical provider occurrences.  If `*` denotes union
convolution of multisets, with outputs of rank above `h` discarded, then

\[
\begin{aligned}
 u(UV)&=u(U)\cup u(V),\\
 P_h(UV)&=P_h(U)\uplus\bigl(u(U)*P_h(V)\bigr),\\
 S_h(UV)&=S_h(V)\uplus\bigl(S_h(U)*u(V)\bigr),\\
 I_h(UV)&=I_h(U)\uplus I_h(V)
              \uplus\bigl(S_h(U)*P_h(V)\bigr).       \tag{3.1}
\end{aligned}
\]

Here a full union is regarded as a singleton multiset in the two middle
lines.  Formula (3.1) defines an associative **truncated interval-union
monoid** `U_h`.  Reversal satisfies

\[
 P_h(\overleftarrow V)=S_h(V),\quad
 S_h(\overleftarrow V)=P_h(V),\quad
 I_h(\overleftarrow V)=I_h(V).                       \tag{3.2}
\]

### Theorem 3.1 (exact upper-shadow derivative)

Let `Z'` be obtained from `Z` by any Hamilton-safe signed-fragment switch.
The signed provider derivative through rank `h` is

\[
             \Delta_h=I_h(Z')-I_h(Z),                \tag{3.3}
\]

and it is computed exactly by (3.1)--(3.2) from the fragment prefix/suffix
states and the new seam facets.  In particular, for every target `R` of
rank `10`, `11`, or `12`,

\[
             \mu' (R)=\mu(R)+\Delta_{12}(R).         \tag{3.4}
\]

No provider wholly internal to one retained fragment is lost; its
occurrence is merely reflected or translated.

#### Proof

Every interval of a concatenation lies wholly in the left word, wholly in
the right word, or uniquely crosses the seam as a nonempty suffix followed
by a nonempty prefix.  This proves (3.1), and associativity follows from
actual word concatenation.  Reversal bijects intervals and exchanges
prefixes with suffixes, proving (3.2).  Cancelling the internal-fragment
terms leaves exactly (3.3).  The deep-interval identity for `D^2` says that
these are precisely the providers arising from physical intervals of
length at least three.  \(\square\)

Write `o_K(R)=max(0,-Delta_K(R))` and
`a_K(R)=max(0,Delta_K(R))` only after cancelling additions and removals of
the same label.  A switch is provider-safe through rank twelve exactly when

\[
              o_K(R)-a_K(R)\le \mu(R)-1             \tag{3.5}
\]

for every currently covered target `R` of ranks ten through twelve.  It
strictly repairs the upper palette when (3.5) holds and some current hole
has positive final delta.  This is necessary and sufficient, not a first-
moment surrogate.

The prefix/suffix state need not have bounded physical width.  Although its
union can increase at most four times between ranks eight and twelve, a
plateau may contain many provider occurrences.  Replacing `U_12` by a
constant row collar would therefore be unsound.

## 4. Exact common-cap transport

Fix an exact maximal common-cap compiler `M` for `Z`.  Signed-permute the
fragment interiors and transport every selected singleton or adjacent-pair
cell wholly contained in one fragment, reflecting its position and keeping
its target label.  At each new seam leave the crossing pair cell and all
cells meeting the seam envelope halo temporarily unassigned.

Let `I` be the set of genuinely replaced seam-row positions after this
transport.  In a two-opt move `I` consists of the two new facets in (1.3).
Put

\[
 J=I+\{0,1,2\},\qquad H=I+\{-2,-1,0,1,2\}.           \tag{4.1}
\]

Indices outside the word are discarded.

### Theorem 4.1 (five-row cap-transport lemma)

Outside `J`, the maximal-envelope letters transport exactly.  Outside the
row halo `H`, every depth-two replay equation transports exactly.  Every
old selected short cell disjoint from `J` remains exact after transport.
Hence the switched row admits an exact common cap extending the transported
interior assignment if and only if the residual target/cell choices meeting
`J` satisfy the maximal-cap equations on `J` and the protected rows in `H`.

The inclusion-minimal new conflict clutter has rank at most three.  A
sufficient certificate is the restriction to this halo of the permanent
position bits, protected-row hosts, and co-selectable selected-target hosts
from the guarded-Hall theorem.

#### Proof

An envelope position is the intersection of the at most three row letters
whose windows contain it.  After fragment transport it can change only if
one of those rows is in `I`, which gives `J`.  A replay equation uses three
consecutive envelope positions and therefore only rows in the five-row halo
`H`.  A singleton or adjacent-pair cell disjoint from `J` sees exactly the
same transported cap and label.

It remains to apply the exact common-cap criterion to the halo.  At most
three available short cells meet one position (its singleton and the two
adjacent pairs), while a protected depth-two row has three hosts and a
selected short target has at most two.  Thus every minimal obstruction has
size at most three.  Permanent bits and the two host families rule out all
such obstructions exactly as in the guarded-Hall proof.  \(\square\)

The theorem is deliberately conditional on transporting a previously exact
compiler.  If no exact compiler is fixed, or if a switch changes target
assignments far from its seams, one must solve the full rank-three common-
cap system.  Scalar envelope nonemptiness is not enough.

## 5. Positive scalar slack is not a repair theorem

### Theorem 5.1 (arbitrary-slack retained-bank no-go)

For every `s>=1` there is a chain-aligned, individually feasible retained
target--cell bank with ordinary Hall, nonempty legal envelopes, and scalar
cell surplus at least `s`, but with no bank-supported integral common cap.

#### Proof

Use the two-position `K_(2,2)` core with common envelope
`{o,a,x}` and lower labels `{o}` and `{o,x}`.  Both marginal perfect
matchings cap both positions by labels omitting `a`, so the protected middle
row loses `a`.  The marginal graph is convex, Hall holds, and `o` is a
permanent bit.  Adjoin any number of unused short cells (or disjoint
already-solved target/cell pairs plus additional unused cells).  This
increases scalar surplus of the retained bank without changing the
unsatisfiable core.  \(\square\)

The carrier-level three-position example in
`MATH_THEOREM_GUARDED_CONVEX_LAMINAR_COMMON_CAP_COMPILER_20260731.md`
already has positive surplus and a unique marginal matching, so the failure
is not an artefact of two symmetric matchings.

Therefore no implication of the form

\[
 \text{positive scalar slack}+\text{marginal switch/Hall feasibility}
 \Longrightarrow\text{simultaneous repair}            \tag{5.1}
\]

can be valid without a trace-guard or exact conflict hypothesis.

## 5A. Host-first component-split potential

There is a still earlier ordering which the scalar ledger must respect.
For a proposed row `Z`, define the exact host set of a required row bit by

\[
 \mathcal H_{i,x}(Z)=
 \{p\in\{i,i+1,i+2\}:x\in E_p(Z)\}.                 \tag{5.2}
\]

Thus `(i,x)` is a replay obstruction precisely when
`H_(i,x)(Z)` is empty.  Put

\[
 u(Z)=|\{(i,x):x\in Z_i,\ \mathcal H_{i,x}(Z)=\varnothing\}|. \tag{5.3}
\]

The lower compiler and its nominal scalar slack are not instantiated until
`u(Z)=0`.

Suppose the complementary shore is partitioned into physical components
`C`, and each component is offered a finite option set `Theta_C`.  An option
records:

```text
its literal facet or owner block,
the row-bit obligations it hosts,
its added owner-bank token cost,
its seam run state and socket resources,
its U12 provider derivative,
and its five-row cap guard state.
```

For option variables `y_(C,theta)`, the exact host premaster contains

\[
 \sum_{\theta\in\Theta_C}y_{C,\theta}=1,             \tag{5.4}
\]

and, for every internal obligation `o`,

\[
 \sum_{C,\theta:o\text{ is hosted by }(C,\theta)}
 y_{C,\theta}\ge1.                                  \tag{5.5}
\]

Seam obligations are added after the component order is chosen.  Equations
(5.4)--(5.5) are a covering system, not a matching system: one physical
host may serve up to three neighbouring row-bit obligations.

The correct lexicographic physicalization potential is

\[
 \boxed{
 \Pi(Z)=\left(
 u(Z),
 [a(Z)+|H^+(Z)|+s_{\rm aux}-7401]_+,
 \kappa_{\rm cap}(Z)
 \right),}                                          \tag{5.6}
\]

where `H^+` is the upper family with no long provider and
`kappa_cap` is zero exactly when the matching-plus-rank-three common-cap
system is feasible.  The coordinates must be read in order.  In particular,
the second coordinate is merely hypothetical while the first is nonzero.

### Theorem 5A.1 (whole-migration versus true-split floor)

Let `B` be a set of complementary components containing internally trapped
host obligations.  Assume that, in a stated relaxation, each component
`C in B` has only two ways to discharge all of its trapped obligations:

1. migrate the whole component into the owner bank, at token cost `c_C`; or
2. use a genuine split/nonflat variant of that component.

Let `s` be the owner-token budget available for whole migrations.  Every
feasible repair has a split set `S subset B` satisfying

\[
             \sum_{C\in S}c_C
             \ge \sum_{C\in B}c_C-s.                \tag{5.7}
\]

Consequently, if `c_(1)>=c_(2)>=...` are the migration costs, the number of
true splits is at least the least `q` for which

\[
             \sum_{j=1}^{q}c_{(j)}
             \ge \sum_{C\in B}c_C-s.                \tag{5.8}
\]

#### Proof

Every component outside `S` must be migrated, so its total cost
`sum_(C in B\\S)c_C` is at most `s`.  Rearranging gives (5.7).  Among all
sets of a fixed cardinality, the sum is maximized by the largest costs,
which gives (5.8).  \(\square\)

This theorem is scoped to its migration/split dichotomy.  A compound
actuator spanning components or a partial-macro migration is a third option
and must be entered explicitly in (5.4)--(5.5) with its actual resource
vector.

The frozen `K17` calibration has `3759` unhosted obligations, all on the
facet shore.  At the atomic level, `141` bad macro interiors carry `227`
immutable facet-run defects.  In the broader component-local/whole-migration
relaxation, `257` complementary components are bad and Theorem 5A.1 gives
the independently frozen floor of `106` genuine component variants.  This
is a host/cap lower bound, not a construction and not a global `K17` no-go.
Partial-macro and compound actuators remain outside that floor.

## 6. The correct positive theorem: guarded repair Hall

Let the atomic obligations of a state `(Z,M)` be grouped into packets
`O_1,...,O_m`.  A packet may contain depth-two replay-defect tokens and
rank-ten/-eleven/-twelve holes.  Let `S` be a finite bank of Hamilton-safe
signed-fragment switches.  A switch `e` is **protected for packet `O_i`**
when:

1. its run-monoid derivative removes every replay defect in `O_i` and
   creates no replay defect;
2. its `U_12` derivative fills every upper hole in `O_i` and satisfies
   (3.5) for every currently covered upper target;
3. its five-row cap transition passes Theorem 4.1 (or preserves one common
   global guarded-Hall bank); and
4. it exports an integer short-cell cost `c(e)>=0`, counting auxiliary
   singleton/pair cells consumed without discharging a distinct residual
   lower target.

Call a collection of candidate switches **orthogonal** when any subfamily
of distinct candidates:

* has disjoint changed incidence support and disjoint seam cap halos;
* uses preallocated, disjoint provider-withdrawal tickets, never exceeding
  `mu(R)-1` for any protected target `R`; and
* has additive short-cell cost and commuting signed-fragment actions.

This is a checkable structural hypothesis, not a consequence of pairwise
geometric disjointness alone.

Make a bipartite graph `G` from obligation packets to switches, joining
`O_i` to `e` precisely when `e` is protected for `O_i`.  Give edge
`(O_i,e)` cost `c(e)`.

### Theorem 6.1 (orthogonal guarded repair Hall)

Suppose the switch bank is orthogonal and the current exact compiler has
unused scalar reserve `s`.  A simultaneous protected repair choosing one
distinct switch for every obligation packet exists whenever

\[
             |N_G(X)|\ge |X|\qquad(X\subseteq\{O_1,\ldots,O_m\}) \tag{6.1}
\]

and the minimum-cost packet-saturating matching of `G` has cost at most
`s`.  The resulting switched row has no obligation in any `O_i`, loses no
previously covered upper target through rank twelve, remains depth-two
replay exact outside the deliberately repaired defects, and admits one
exact common cap.

If every edge has cost at most one, the simpler hypotheses (6.1) and
`s>=m` suffice.

#### Proof

Hall gives a packet-saturating matching, and the usual source--packet--
switch--sink network with edge costs computes an integral minimum-cost one.
Orthogonality makes the selected incidence changes commute.  The run
derivatives create no new defects and remove every packet defect.  The
preallocated provider tickets and (3.5) retain every old upper target, while
the matched service rows fill every packet hole.  Disjoint cap halos and
Theorem 4.1 transport the old exact compiler across every switch.  Finally
the additive cost bound leaves the scalar cell ledger nonnegative.  \(\square\)

Define

\[
 \Phi(Z)=|\operatorname{Def}_2(Z)|+
          |H_{10}(Z)|+|H_{11}(Z)|+|H_{12}(Z)|.       \tag{6.2}
\]

Every nonempty protected matched batch strictly decreases `Phi` and never
increases any of its four summands.  Thus an iterative construction
terminates if (6.1) and the reserve bound persist after each batch.

The missing theorem is now precise: prove a dimension-uniform supply of
orthogonal guarded switches with the required Hall expansion.  The existing
rectangle and alternating-circuit abundance proves only the unguarded
projection of that statement.

## 7. `K17` calibration and the next exact audit

For the connected `OPTIMAL28` owner cycle, the forced row (0.1) has:

\[
 \Phi=3759+1900+911+128=6698.                        \tag{7.1}
\]

The first term is the exact number of bit-labelled host obligations; they
occupy `3568` distinct replay-mismatching rows.  There are `2392` strict
short runs.  The lower-only scalar reserve is `3293`; if all `2939` upper
holes were charged to short cells instead of repaired by long providers,
the combined reserve would be only `354`.

These aggregate figures alone support neither a positive nor a negative
conclusion.  They
show exactly what should be exported for each residual rectangle or longer
circuit:

```text
port-pairing / Hamilton signature,
R3 seam derivative and repaired defect tokens,
U12 signed provider derivative,
five-row common-cap guard transition,
short-cell cost.
```

For the **fixed** OPTIMAL28 macro/packet skeleton, two later exact censuses
already decide the first Hall preflight.

* `141` unselected macro interiors contain `227` strict owner runs of length
  three.  Facetization makes them internal runs of length two.  A residual
  incidence rectangle cuts only at exposed ports, so its signed-fragment
  action transports these defects and cannot repair them.
* Even after relaxing all owner/port degree, topology, residence and cap
  coupling, the union of every locally possible residual-pair provider
  omits `218` rank-ten targets.  The rank-ten adjacent-pair reduction makes
  these genuine all-width upper holes on this skeleton.

Hence the guarded-repair graph of Theorem 6.1 has isolated obligation
packets on the fixed skeleton: its Hall condition fails before costs are
considered.  A catalogue of residual rectangles alone would therefore be
the wrong next computation.  At least one macro/packet interior,
occurrence choice, or genuinely nonflat component option must change.

After such an atlas is supplied, each option should export the five-field
signature above and the correct next computation is its min-cost guarded
Hall test.  Running independent residence, upper-hole, and common-cap
optimizers would discard the correlation that the theorem requires.

## 8. Proven/conditional boundary

Proved here:

* signed-fragment normal form for Hamilton-safe circuit switches;
* exact run-monoid calculation of depth-two replay changes;
* exact associative provider calculus through rank twelve;
* exact five-row transport of an already fixed common cap;
* arbitrary positive scalar slack does not imply common-cap feasibility;
* an integral min-cost Hall theorem for an orthogonal guarded switch bank.

Also proved for the authenticated fixed skeleton by the cited exact
censuses: residual incidence rectangles alone cannot repair either all
residence obligations or all rank-ten holes.

Not proved here:

* that the authenticated `K17` connected flow has enough protected
  rectangles or circuits;
* that its current non-replaying row can first be equipped with a common cap;
* that the orthogonality/Hall hypotheses hold in every dimension; or
* a `K17` word, a new upper bound, or `nu(k)=B(k)`.

## 9. Lightweight audit and source boundary

The dimension-free identities in Sections 2--3 are exhaustively checked by

```text
scratch/audit_k17_two_bank_switch_monoids_20260731.py
SHA-256 481397b176e2d1325733d26f4323465a4c86db684dbce57d8c1f9ad5014a2dea

scratch/k17_two_bank_switch_monoids_20260731.audit.json
SHA-256 6a1cea7d4de6b615545373c9eb0634bb8ab6b4decb5ca3106dbda846c14cda45
payload d16ddf425ce56a84f08896953a5561eacc69e287645057fd5af8cb92b8390be4
```

It checks all binary words through length nine and all nonempty three-bit
set words through length four, including every concatenation split and
reversal.  It is a formula audit, not switch-supply evidence.

The fixed-skeleton `218`-hole obstruction is independently frozen in

```text
MATH_AUDIT_AD_K17_OPT28_FIXED_SKELETON_STATIC_PROVIDER_NOGO_20260731.md
SHA-256 45dca08cf71d394266d382846bd30b43d6792806cdd2ee59fb667cd776b36414
```

The broader immutable-component and component-local migration/variant floor
is frozen in

```text
MATH_THEOREM_THREAD_D_K17_OPT28_COMPONENT_CAP_PHYSICALIZATION_GATE_20260731.md
SHA-256 e1f56cd564304452a40beaaa669ab0ae1dd4724232639254f9c5792a4955980e
```

That frozen theorem gives the broad-component floor of `106` variants in
its stated component-local/wholesale dichotomy.  No narrower live ledger is
used as theorem evidence here.
