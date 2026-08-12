# Two-scale cover-down, Stage 1: coned alpha-hex packing and the puncture/extension gate

Date: 2026-07-31  
Lane: AD  
Status: exact native constant-support absorber; exact catalogue, degree,
packing, protected-resource, and common-basis survival bounds; exact
conditional Stage-1 composition; sharp scope corrections.  This does
**not** prove a prescribed-leave Delcourt--Postle theorem, an installed
positive-density off bank, a native Stage-2 packet map, or `nu=B`.

## 0. Verdict

The proposed two-scale metric is real, but one must use the correct local
state.  A complete transparent incidence hex is a balanced `3 <-> 3`
switch and preserves the exact host leave.  It cannot cover down.  If one
edge is deleted from one phase, however, the same coned alpha hex becomes a
literal `2 -> 3` absorber for the four resources of that edge.

In the full rank-`n`/rank-`n+2` Boolean side host on `[2n]`:

* every legal geometric diamond lies in exactly `2n(n-2)` such coned alpha
  supports;
* there are

  ```text
  N (n+1) binom(n,3),       N=binom(2n,n-1),
  ```

  canonical supports;
* for `n>=4`, a greedy argument packs at least `ceil(N/72)` pairwise
  outer-resource- and physical-owner-disjoint supports;
* after avoiding a predeclared protected resource set `Z_0`, the lower
  bound is `N/72-|Z_0|/12`; and
* for a subbank of order at most `N/72`, exact common-basis one-point
  marginals choose a synchronized common basis `Q` which punctures at most
  `C/24` raw gadgets.  Here

  ```text
  C=Cat_(n+1),       C/N=2(2n+1)/(n(n+2))<4/n.
  ```

  If six additional possible anchor/port events are charged, the bound is
  `C/8`.  Both are `O(N/n)=O(Cat_n)`.

This is the rigorous Stage-1 scale reduction.  It is not yet a cover-down
theorem.  The first unsupported composition step is:

> extend the surviving common off states to one `P-o(P)` physical side
> matching whose entire leave is the disjoint union of their designated
> target edges.

The arbitrary-`Q` Delcourt--Postle theorem does not prescribe its leave or
force a chosen colour class to contain those off states.  Its protected
reserve theorem tolerates an `o(P)` closed bank, whereas the linear gadget
bank above has `Theta(P)` closed support.  Moreover, a punctured gadget is
not automatically one native gain-one residual token, and the contracted
graphic meaning of a local packet can depend on a long path of `F-Q`.

Thus the two scales meet arithmetically, but the exact missing theorem is a
positive-density, absorber-conditioned matching extension with declared
fallback and graphic signatures.

## 1. Notation and the exact marginal input

Put

\[
 M=\binom{2n}{n},\qquad
 N=\binom{2n}{n-1},\qquad
 P=\binom{2n}{n-2},
\]

\[
 K=\operatorname {Cat}_n={N\over n},\qquad
 C=\operatorname {Cat}_{n+1}.
\]

Let `F` be an oriented parameter-`n` child forest.  The automatic common
basis theorem gives a probability distribution on synchronized common
bases `Q subseteq F`, `|Q|=C`, with the exact marginals

\[
 \Pr(q\in Q)=\alpha:={C\over N}
      ={2(2n+1)\over n(n+2)}<{4\over n}             \tag{1.1}
\]

for every `q in F`.  This is Theorem 4.1 and equations (4.2)--(4.3) of
`THREAD_A_CATALAN_TWO_COORDINATE_COMMON_Q_AND_PUNCTURED_FOREST_NIBBLE_20260731.md`.
No negative dependence is used below.

On the minus side, `Q` deletes the rank-`n` lower resources

\[
                         \{t_q:q\in Q\}.             \tag{1.2}
\]

The tail map is injective.  The dual statement uses the injective head map.
Every physical rank-`n+1` owner has two capacity slots unless it is a seam
anchor, in which case it has one.  We use a canonical first slot, which
exists in both cases.

The general correlation-free survival statement used below is Theorem 4.2
of
`MATH_THEOREM_K_COMMON_BASIS_PRIVATE_CIRCUIT_ALTERATION_20260731.md`:
for precomputed candidates with child-risk sets `R(A)`, some common basis
has total punctured-candidate fraction at most

\[
                    \alpha\sum_A |R(A)|              \tag{1.3}
\]

after the appropriate averaging within each candidate list.

## 2. The coned alpha hex

Let `Omega=[2n]`.  Choose

\[
 H\in\binom\Omega{n-1},\qquad
 z\in\Omega\setminus H,\qquad
 A=\{a,b,c\}\subseteq\Omega\setminus(H\cup\{z\}). \tag{2.1}
\]

Define the three lower resources

\[
 D_a=H+a,\qquad D_b=H+b,\qquad D_c=H+c,              \tag{2.2}
\]

and the three upper resources

\[
 V_a=H+b+c+z,\quad V_b=H+c+a+z,\quad
 V_c=H+a+b+z.                                       \tag{2.3}
\]

There are two alternating incidence phases

\[
 {\cal P}=\{(D_a,V_c),(D_b,V_a),(D_c,V_b)\},          \tag{2.4}
\]

\[
 {\cal N}=\{(D_a,V_b),(D_b,V_c),(D_c,V_a)\}.          \tag{2.5}
\]

Every displayed pair is a containment with rank difference two.  Put

\[
 X_{ab}=H+a+b,\quad X_{bc}=H+b+c,\quad X_{ca}=H+c+a,
\]

\[
 Z_a=H+a+z,\quad Z_b=H+b+z,\quad Z_c=H+c+z.          \tag{2.6}
\]

Use the canonical first capacity slot at each of these six physical owners.

### Theorem 2.1 (exact two-state identity)

Both `P` and `N` are three-atom matchings on exactly the same twelve host
resources:

* the three resources in (2.2);
* the three resources in (2.3); and
* the six canonical owner slots in (2.6).

Their physical projections are respectively

\[
 \{X_{ab}Z_a,X_{bc}Z_b,X_{ca}Z_c\},                 \tag{2.7}
\]

\[
 \{X_{ca}Z_a,X_{ab}Z_b,X_{bc}Z_c\}.                 \tag{2.8}
\]

Thus each phase is a three-edge physical matching, and their union is the
alternating six-cycle

\[
 Z_aX_{ab}Z_bX_{bc}Z_cX_{ca}Z_a.                    \tag{2.9}
\]

In particular both phases have the same physical-owner degree vector.
Changing phase preserves every outer palette, every used capacity slot,
and every cap-one anchor guard.

#### Proof

For example, `V_c-D_a={b,z}`, so the physical edge of `(D_a,V_c)`
is `X_ab Z_a`.  The other five calculations give (2.7)--(2.8).
All six sets in (2.6) are distinct because `a,b,c,z` are distinct.  Each
phase therefore covers every displayed resource exactly once.  Equation
(2.9) is the literal union. `square`

### Corollary 2.2 (constant-support edge absorber)

Fix any `e in P`.  The off state

\[
                         {\cal P}\setminus\{e\}       \tag{2.10}
\]

matches the eight resources outside `e`, while the on state `N` matches all
twelve resources.  Hence (2.10) `-> N` is a literal `2 -> 3` absorber for
the four-resource legal side atom `e`.

The analogous statement holds after exchanging the two phases.  The
complete `3 <-> 3` toggle alone is zero-boundary and cannot alter any host
leave.

#### Proof

The atoms of `P` are mutually disjoint and Theorem 2.1 says that `N` covers
their complete resource union. `square`

### Proposition 2.3 (all geometric candidates occur)

Every legal geometric side diamond `e=(D,V)`, with
`|D|=n`, `|V|=n+2`, `D subset V`, lies in exactly

\[
                              2n(n-2)                 \tag{2.11}
\]

supports of the form (2.1)--(2.5).  The same holds for any legal
capacity-slot lift after retaining its two prescribed target slots and
using canonical slots at the four auxiliary owners.

#### Proof

Write `V-D={p,q}`.  To realize `e=(D_a,V_c)`, choose

* `a in D` (`n` choices), and put `H=D-a`;
* an ordering `(b,z)` of `{p,q}` (two choices); and
* `c in Omega-V` (`n-2` choices).

The construction is then forced, and these choices are recovered from the
support.  This proves (2.11).  Slot relabelling at the two target owners
retains any prescribed legal target slots. `square`

This is the side-host analogue of the alpha-trade edge absorber.  It must
not be identified with an AGCF edge: an AGCF edge is an entire
`(3n+1)`-resource complement geodesic.  A native map between the two packet
languages remains an additional interface.

## 3. Exact catalogue degrees and a linear disjoint bank

Let `Z_n` be the family of canonical supports (2.1).  The support determines
`H` as the intersection of its three lower resources, determines
`{a,b,c}` from their union, and determines `z` from the common extra point
in the three upper resources.  Thus `Z_n` is a simple twelve-uniform support
hypergraph when its resources are typed as lower, upper, and physical owner.

Its order is

\[
 |Z_n|=N(n+1)\binom n3.                              \tag{3.1}
\]

By coordinate transitivity, the three resource degrees are

\[
 d_D={3|Z_n|\over M}
     ={n^2(n-1)(n-2)\over2},                         \tag{3.2}
\]

\[
 d_V={3|Z_n|\over P}
     ={n(n-2)(n+1)(n+2)\over2},                     \tag{3.3}
\]

\[
 d_X={6|Z_n|\over N}
     =n(n-1)(n-2)(n+1).                              \tag{3.4}
\]

For `n>=4`,

\[
                         \Delta(Z_n)=d_X,             \tag{3.5}
\]

since `d_X/d_V=2(n-1)/(n+2)>=1`, and plainly `d_X>d_D`.

### Theorem 3.1 (linear full-support packing)

For every `n>=4`, `Z_n` contains at least

\[
                         \left\lceil {N\over72}\right\rceil       \tag{3.6}
\]

pairwise lower-resource-, upper-resource-, and physical-owner-disjoint
supports.

More generally, after forbidding any predeclared typed resource set `Z_0`,
there is such a packing of order at least

\[
                         {N\over72}-{|Z_0|\over12}.    \tag{3.7}
\]

The integer conclusion is obtained by taking the ceiling of the positive
right side.

#### Proof

Let `B` be a maximal disjoint family of `t` supports.  Every member of
`Z_n` meets one of the `12t` resources covered by `B`.  Each such resource
lies in at most `Delta(Z_n)` supports, so

\[
 |Z_n|\le12t\Delta(Z_n).
\]

But (3.1) and (3.4) give `|Z_n|=Nd_X/6`.  Hence
`t>=N/72`, proving (3.6).

Deleting `Z_0` removes at most `Delta(Z_n)|Z_0|` supports.  Repeat the same
maximality argument in the remainder:

\[
 t\ge {|Z_n|-\Delta|Z_0|\over12\Delta}
   ={N\over72}-{|Z_0|\over12}.
\]

`square`

For each support choose one target atom `e in P`.  Full-support
disjointness makes all target atoms disjoint, makes the union of all off
states `P-{e}` a common host matching, and makes either complete phase
choice locally cap-safe.  The off physical graph is itself a matching.
This is an installed **local** off bank; extending it by the bulk is a
separate statement.

## 4. Exact common-basis survival

Fix a packed minus-shore subbank `B` of order

\[
                         t\le\left\lfloor{N\over72}\right\rfloor. \tag{4.1}
\]

For a support `A in B`, let

\[
 R(A)=\{q\in F:t_q\in\{D_a,D_b,D_c\}\}.             \tag{4.2}
\]

Tail injectivity gives `|R(A)|<=3`.  If `Q cap R(A)=emptyset`, all three
lower resources survive in the punctured side host; all three upper
resources remain present; and the canonical first slot at every physical
owner exists even when that owner becomes an anchor.  Thus both states in
Section 2 remain legal.

### Theorem 4.1 (raw Stage-1 survival)

Some synchronized common basis `Q` punctures at most

\[
                       3\alpha t\le {C\over24}        \tag{4.3}
\]

members of `B`.  In particular

\[
 {C\over24}
 = {2n+1\over12(n+2)}{N\over n}
 < {1\over6}{N\over n}.                              \tag{4.4}
\]

For simultaneous banks of order at most `N/72` on both shores, the total
number punctured is at most `C/12`.

#### Proof

For random `Q` under the common-basis marginal law,

\[
 \mathbf E\,|\{A:Q\cap R(A)\ne\varnothing\}|
 \le\sum_A\sum_{q\in R(A)}\Pr(q\in Q)
 \le3\alpha t.
\]

Choose an outcome no larger than its expectation and use (1.1), (4.1).
The dual head-bank proof is identical, and the same additive cost chooses
one `Q` for both shores. `square`

### Corollary 4.2 (locally guard-closed survival)

Suppose a packet's declared external use additionally requires that none of
its six physical owners become a seam anchor.  Since the anchor map
`q -> U_q` is injective on the child forest, charge those at most six events
to the risk set.  Then `|R(A)|<=9`, and some common basis punctures at most

\[
                         9\alpha t\le {C\over8}       \tag{4.5}
\]

packets in one bank.  Moreover

\[
 {C\over8}
 ={2n+1\over4(n+2)}{N\over n}
 <{1\over2}{N\over n}.                               \tag{4.6}
\]

This six-event closure is needed only when the packet requires a second
side incidence or a declared component port at those owners.  The isolated
packet itself respects a cap-one anchor in both states.

The bounds (4.3)--(4.6) are an exact use of one-point marginals.  They do
not choose one surviving option from overlapping lists, install the common
off states in a bulk matching, or control a contracted graphic link.

## 5. Exact conditional Stage-1 composition

The following states precisely what the calculation would prove if the
missing extension were supplied.

### Theorem 5.1 (conditional constant-packet cover-down)

Fix precomputed unit defect tokens `I`.  For each token `i`, let `A_i` be a
finite list of coned alpha edge absorbers.  Assume:

1. **Constant closed risk.**  Every candidate has a child-risk set of order
   at most `r`, and avoiding it preserves its outer resources, its required
   cap status, and its declared local port semantics.
2. **Surviving private selection.**  After `Q` is chosen, all but `J` of the
   tokens admit one selected surviving candidate; their complete two-state
   supports are pairwise host-resource-private.
3. **Common off-state extension and target leave.**  The selected off states
   are contained in one current side matching.  Together with the bulk,
   that matching leaves exactly the disjoint four-resource target edges of
   the selected absorbers, and no other Stage-1 target resource.
4. **Cap and anchor guards.**  Every on state respects residual degree one at
   seam anchors and degree two elsewhere, jointly with the bulk.
5. **Graphic row.**  After deleting the selected off states and contracting
   the remaining physical forest, all on-state physical edges are loopless
   and form a forest.  If exact roots are required, the corresponding fixed
   root-star edges together with the selected links form a spanning tree.
6. **Bad-token semantics.**  Every token in `J` has a declared current
   fallback state which decomposes into at most `g` native Stage-2
   gain-one tokens.  No invalid off state of a punctured gadget is silently
   retained.

Then all selected surviving absorbers may be switched on simultaneously.
They cover their target edges exactly, preserve the two outer injections,
all physical caps and protected anchors, and preserve physical acyclicity
(and the declared rooted row).  The residual Stage-2 token count is at most

\[
                         g|J|.                       \tag{5.1}
\]

If `|I|<=kappa N` and every list has average risk at most `r`, Theorem 4.2
gives a common basis with

\[
 |J|\le\alpha r|I|
 \le {2\kappa r(2n+1)\over n+2}\operatorname {Cat}_n
 <4\kappa r\operatorname {Cat}_n.                   \tag{5.2}
\]

#### Proof

Theorem 4.2 gives (5.2).  Rows 2--3 make the simultaneous switches a
matching operation and make their resource gain exactly the declared
target leave.  Row 4 proves cap and anchor legality.  The standard
delete--contract--add graphic criterion proves acyclicity from row 5; the
root-star version is the exact one-root-per-component criterion.  Row 6
gives (5.1). `square`

For a singleton packed bank, (4.3) gives `|J|<=C/24` with raw risk three,
and (4.5) gives `|J|<=C/8` with the six local port guards charged.  These
are only gadget counts until row 6 supplies the native fallback map.

## 6. The first unsupported and false conditions

### 6.1 A full transparent hex has zero boundary

By Theorem 2.1, the complete phases `P,N` have identical host-resource
incidence.  Therefore any sequence of complete transparent hex toggles
preserves the exact lower, upper, and slot leave of the DP matching.
It may rethread physical topology, but it cannot reduce an outer deficiency
or align a non-edge leave.  Cover-down uses the delete-one-edge state of
Corollary 2.2, not the balanced toggle by itself.

The six transparent `ML(7)` rows in Table (4.4) of
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`
are even more scoped: transparency is relative to a supplied global
decoration and retained-fragment boundary types.  Suspending that finite
fixture does not automatically make it a fixed-`Q` side absorber.

### 6.2 DP does not install or align the linear bank

`MATH_THEOREM_CATALAN_ARBITRARY_COMMON_BASIS_PHYSICAL_FOREST_20260731.md`
gives, for every fixed common basis, some physical side forest of order
`P-o(P)`.  It neither:

* contains a prescribed collection of off atoms; nor
* leaves prescribed target edges; nor
* supplies a lower bound for one predesignated colour class.

The protected-reserve theorem of item `2301AD` loses `O(|Z|)` selected
atoms when a host-resource set `Z` is closed.  A bank of `Theta(N)` constant
absorbers has `Theta(N)=Theta(P)` closed support.  Hence that theorem cannot
be run outside the bank while retaining a `P-o(P)` conclusion.  The bank
and bulk must instead be chosen jointly, or one needs a DP theorem
conditioned on a positive-density partial matching.

This is the first unsupported condition in the proposed composition.
It is the same edge-aligned cover-down gate in a sharper two-scale normal
form, not another local-absorber existence question.

### 6.3 Punctured gadget count is not native token count

If `Q` deletes the lower resource of an off-state atom, that atom is no
longer in the punctured host.  Abandoning it can expose its upper resource
and its two owner slots in addition to the designated target boundary.
Those exposed resources need not be one legal side edge.  Consequently

\[
      \#\{\text{punctured gadgets}\}
 \ne  \#\{\text{native gain-one residual units}\}              \tag{6.1}
\]

without the fallback hypothesis in Theorem 5.1.  A factor `g` must be
proved; it may not be set to one by notation.

### 6.4 Constant local support need not mean constant graphic risk

The contracted component link of a packet is defined only after the core
forest is fixed.  If two ports are connected by a path of `s` child edges,
membership of any one of those edges in `Q` can change whether the packet
is a loop or a component link.  A risk set which preserves the declared
graphic signature must then contain the whole path and may have order `s`.

Thus the raw coned hex has risk three, and its local anchor closure has risk
at most nine, but its **graphic closure** can have growing or even
macroscopic risk.  Theorem 4.2 yields a Catalan residual only after a
node-private/laminar port theorem keeps this closed risk bounded.  Treating
the component tree of `F-Q` as precomputed is invalid.

### 6.5 Outer privacy is too weak

The literal fixed-`Q`, `n=3` fixture in
`MATH_THEOREM_CATALAN_DP_COLORING_EXCHANGE_CALCULUS_AND_LOCKED_C6_OBSTRUCTION_20260731.md`
has two outer `C6` components with cross slot-dependency arcs in both
directions.  Neither individual phase may switch; only the joint phase
change is legal.  Therefore packet privacy must include capacity slots and
declared physical ports, not only the two outer palettes.  The full-support
packing in Theorem 3.1 was chosen precisely to avoid this error.

## 7. Relation to Stage 2

The off-centre independent-boundary ear has off order at most `n+1` and on
order at most `n+2`.  Therefore `B` pairwise-private gain-one ears on one
shore pass the **scalar** final-size check when

\[
                         B(n+2)\le P.                \tag{7.1}
\]

For the guarded Stage-1 bound `B=C/8`,

\[
 {B(n+2)\over P}
 \le{(n+2)C\over8P}
 ={(n+2)(2n+1)\over4n(n-1)},                         \tag{7.2}
\]

which is at most one for integral `n>=5` and tends to `1/2`.  For the raw
bound `C/24`, the ratio tends to `1/6`.

This verifies the metric interface only.  It does not pack the long ears,
install their common off states, pair their two outer leave shores, or pass
the contracted graphic/root rows.  Moreover a bad Stage-1 gadget may cost
`g>1` native tokens, in which case the left side of (7.1) is multiplied by
`g`.

## 8. Exact proved/conditional boundary

Proved here:

1. the native coned alpha `3 <-> 3` identity and its delete-one-edge
   `2 -> 3` absorber state;
2. exact all-candidate multiplicity `2n(n-2)`;
3. exact catalogue degrees and the `N/72` disjoint-support bank;
4. protected-resource loss `|Z_0|/12`;
5. common-basis survival bounds `C/24` and `C/8`; and
6. the exact conditional privacy/off-state/cap/graphic/fallback interface.

Not proved:

1. extension of a positive-density common off bank to a `P-o(P)` or exact
   fixed-`Q` physical side matching;
2. forcing the bulk leave to be the bank's designated legal target edges;
3. a constant-size native fallback for every punctured gadget;
4. bounded graphic-closure risk for a linear packet bank; or
5. the Catalan-size installed private long-ear theorem.

These are genuine correlations.  Local alpha-hex abundance, exact
one-point common-basis marginals, and the arbitrary-`Q` DP near-forest
theorem do not imply them separately.

## 9. Source audit

The inputs and their exact scopes are:

* `THREAD_A_CATALAN_TWO_COORDINATE_COMMON_Q_AND_PUNCTURED_FOREST_NIBBLE_20260731.md`,
  Theorem 4.1 and (4.2)--(4.3): exact common-basis marginal law;
* `MATH_THEOREM_K_COMMON_BASIS_PRIVATE_CIRCUIT_ALTERATION_20260731.md`,
  Theorem 4.2 and Corollary 4.3: additive puncture survival and its
  explicitly conditional private-tree composition;
* `DIAMOND_PERFECT_MATCHING_ABSORPTION_ROUTE_20260727.md`, Lemma 5.1 and
  Corollary 5.2: the alpha trade and delete-one-edge absorber principle;
* `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`,
  Theorem 2.1 and Table (4.4): fixed-decoration transparent `ML(7)` scope;
* `MATH_THEOREM_CATALAN_ARBITRARY_COMMON_BASIS_PHYSICAL_FOREST_20260731.md`:
  arbitrary-`Q` `P-o(P)` physical forests without prescribed leave; and
* `MATH_THEOREM_CATALAN_DP_COLORING_EXCHANGE_CALCULUS_AND_LOCKED_C6_OBSTRUCTION_20260731.md`,
  Section 4: exact slot-dependency obstruction to outer-only C6 privacy.

All new counts in Sections 2--4 are proved symbolically above; no finite or
probabilistic independence assumption is hidden in them.
