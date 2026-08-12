# Occurrence-exchange repair: an exact Hall gate, an LLL criterion, and the `K17` seven-swap premaster

Date: 2026-07-31  
Status: general conditional repair theorem, an exact finite `K17`
premaster certificate, and a solver-free no-go for its complete radius-one
connector neighbourhood; no marked Hamilton path, `K17` word, or
all-dimension existence theorem is claimed

## 0. Result

The seventh `K17` occurrence exchange is not merely another residence
improvement.  It proves that the two local requirements which had appeared
to compete can coexist:

1. every marked macro component is internally `D2<3` and `D3<4` clean; and
2. every marked component has at least one residence-clean pure-`U`
   connector.

The correct all-odd abstraction is an **occurrence-exchange repair system**.
When repairs have disjoint resources and commute, simultaneous repair is
governed exactly by Hall deficiency.  When they have bounded pairwise
interactions, an independent-transversal local-lemma criterion suffices.
This isolates a concrete dimension-uniform target: prove that every
regenerative parent exports many occurrence repairs but only boundedly many
conflicts per repair.

The result deliberately stops at the premaster gate.  For the new `K17`
forest the clean connector projection has three weak components and far too
many forced leaves for a Hamilton path.  More strongly, the complete
radius-one census contains no connected clean connector graph and no state
satisfying the path endpoint-degree necessary condition.  Thus “no isolated
component” is necessary, but very far from sufficient, for the two-bank
marked Hamilton path.

## 1. Occurrence-choice states

Let \(Z\) be the set of lower colours used by an odd Pascal lift.  For each
\(z\in Z\), let \(F_z\) be the nonempty fibre of physical occurrences of
\(z\) in the parent trace.  An **occurrence transversal** is

\[
                     \tau\in\prod_{z\in Z}F_z.       \tag{1.1}
\]

The deterministic Pascal builder maps \(\tau\) to:

* a macro forest \(P_\tau\);
* a declared set of marked or required macros;
* a literal owner word on every marked forest component; and
* the oriented, labelled clean-connector graph \(\Gamma_\tau\).

Call \(\tau\) **protected** when every forced packet remains in one macro
and every marked component passes all declared internal residence tests.
Call it a **premaster** when it is protected and the underlying marked
component graph of \(\Gamma_\tau\) has no isolated vertex.

An occurrence exchange changes one coordinate \(\tau(z)\) to a different
member of \(F_z\).  It preserves all sector cardinalities, but it may change
macro closure, endpoints, residence, and connector incidence.  Hence these
exchanges are the correct variables for the joint gate; scalar run repair
and connector repair cannot safely be optimized on separate frozen forests.

## 2. Exact Hall criterion in the orthogonal face

Fix a protected state and a finite set \(D\) of declared defects.  A defect
may be a residence-bad protected block or a connector-isolated marked
component.  Let \(R\) be a set of exchange resources, each usable at most
once.  A resource records an occurrence fibre together with a certified
alternative occurrence and its literal repair collar.

Say that the catalogue is **orthogonal** when:

1. an edge \(b\sim\rho\), \(b\in D,\rho\in R\), certifies that applying
   \(\rho\) repairs \(b\);
2. any set of resources with distinct right vertices composes literally;
3. the composite preserves every forced packet and every already-good
   residence block; and
4. every connector witnessing a repaired isolation remains clean and
   incident after the other selected exchanges.

Conditions 2--4 are finite collar/support checks.  In particular, they hold
when the exchange supports and the connector witnesses are resource-disjoint
and separated beyond the residence-transducer radius.

### Theorem 2.1 (occurrence-repair Hall theorem)

In an orthogonal catalogue, all defects can be repaired simultaneously if
and only if

\[
                 |N(S)|\ge |S|\qquad(S\subseteq D). \tag{2.1}
\]

More generally, the maximum number of simultaneously repairable defects is

\[
 \boxed{
   |D|-\max_{S\subseteq D}\bigl(|S|-|N(S)|\bigr)
   =\min_{S\subseteq D}\bigl(|D\setminus S|+|N(S)|\bigr).
 }                                                       \tag{2.2}
\]

#### Proof

By orthogonality, a simultaneous repair in this catalogue is exactly a
matching from repaired defects to distinct exchange resources.  Formula
(2.2) is the bipartite matching deficiency theorem, and (2.1) is Hall's
criterion for a matching saturating \(D\).  The literal composition clauses
then turn the matching into one protected premaster state.  Conversely any
repair in the restricted catalogue assigns a distinct resource to each
repaired defect and therefore gives the matching.  \(\square\)

This theorem is exact only in the stated orthogonal face.  Without the
composition clauses, two individually safe exchanges can merge macro
components, delete one another's last connector, or create a new boundary
run.  Ordinary Hall on the marginal candidate lists would then be unsound.

## 3. Bounded-interaction local lemma

Orthogonality is stronger than necessary.  For each defect \(b\), let
\(L_b\) be a list of individually certified repairs of \(b\).  Put an edge
between two candidate repairs exactly when they cannot coexist: they use the
same occurrence fibre, their support collars interact, they collide in a
connector label, or either one destroys the other's certified repair.
Assume that every conflict-free transversal of the lists composes to a
protected premaster.

### Theorem 3.1 (finite LLL repair criterion)

If every list has size at least \(L\), the candidate-conflict graph has
maximum degree at most \(\Delta\), and

\[
                         L\ge 2e\Delta,               \tag{3.1}
\]

then there is one compatible repair from every list.

#### Proof

Restrict every list to exactly \(L\) candidates and choose one candidate
uniformly and independently from every list.  For each conflict edge whose
ends lie in different lists, let the bad event be that both endpoints are
chosen.  Its probability is \(L^{-2}\).  Such an event shares a random
choice only with conflict edges incident to one of its two lists.  There are
at most \(2L\Delta-1\) of those.  The symmetric Lovasz local lemma applies
because

\[
 eL^{-2}(2L\Delta)\le1.
\]

The resulting transversal is conflict-free, and the composition hypothesis
makes it a simultaneous repair.  \(\square\)

This is the useful asymptotic formulation.  A regenerative proof need not
produce a canonical exchange.  It is enough to export repair-list size
larger than the interaction degree by a constant factor.  Both quantities
are finite, source-relative objects and can be bounded before constructing
the child chronology.

## 4. Exact `K17` specialization

Start from the frozen first-occurrence transversal of the `K15` parent.
The first six exchanges are

```text
 9486: (0,4064) -> (0,5826)
16502: (0,1781) -> (0,6254)
 1675: (0,1997) -> (0,5349)
 2829: (0,2849) -> (0,6201)
22632: (0,1571) -> (0,4923)
26800: (0,2423) -> (0,5775)
```

Their prefix ledger is

```text
swaps                 0    1    2    3    4    5    6
bad marked components 6    5    4    3    2    1    0
D2 bad runs           32   20    8    6    4    2    0
closure macros       190  178  162  160  158  156  154
```

At the six-swap state there is one connector-isolated marked component.
The exact radius-one occurrence census checks all `1430` alternative
exchanges from that state:

```text
residence-clean alternatives                         1411
residence-clean alternatives leaving no isolation     122
```

The lexicographically selected repair is

```text
21006: (0,1121) -> (0,4318).
```

Rebuilding from the parent after all seven exchanges gives

```text
macro edges / forest components              1430 / 5005
marked components / marked closure macros      106 / 153
required / optional marked macros              108 / 45
marked owner tokens                                  3800
strict internal D2 / D3 debt                       0 / 0
geometric / residence-clean directed arcs        422 / 322
distinct pure-U connector labels                       143
connector-isolated marked components                    0
```

The newly enabled clean adjacency joins the old isolated single-macro
component (ports `16638,22835`) to a component exposing port `22838`; its
pure-`U` label is `22839`.  The seventh exchange therefore repairs the
connector gate without spending a residence defect elsewhere.  It also
shrinks the marked closure by one macro and fifteen owner tokens.

The output is an exact instance of the one-defect Hall theorem: the Hall
right neighbourhood is nonempty—in fact it contains `122` safe exchanges.
The first six exchanges exhibit the complementary sequential augmentation
phenomenon for residence defects.  They do **not** prove that the same Hall
or LLL inequalities hold uniformly in the dimension.

## 5. The next obstruction is genuinely stronger

On the displayed seven-swap premaster, the exact clean connector projection
has weak-component sizes

```text
102, 2, 2
```

and `22` component vertices of undirected degree one.  It therefore cannot
contain a Hamilton path even before orientations or repeated pure-`U` labels
are considered.  The corresponding exact labelled model chooses one
orientation of each of the `106` marked components, one incoming and one
outgoing clean arc except at the two path ends, and uses every pure-`U` label
at most once.  Consistently, it is UNSAT before any subtour cut is added:

```text
oriented clean arcs       322
distinct labels           143
variables / clauses       958 / 48925
subtour rounds              0
verdict                   UNSAT
```

The complete radius-one census makes this a theorem about the whole local
face rather than one unlucky witness:

```text
radius-one states checked                         1430
residence-clean states                            1411
states with no isolated marked component           122
states with connected clean connector graph           0
states satisfying the path degree condition           0
minimum number of degree-one component vertices      21
best weak-component shapes                102+2+2 or 103+2+2
```

Thus the seven-swap theorem removes the **degree-zero** obstruction only,
and no single additional occurrence exchange can reach the path gate from
the six-swap state.  It does not imply a labelled path cover, much less a
Hamilton path, residual facet flow, connected complementary completion,
deep-shadow coverage, a common cap, or a `K17` word.  The next exact search
space begins at radius two from the twelve three-component frontier states.
The next all-dimension min--max target is a stronger labelled
path/connector condition, not another scalar isolation count.

## 6. Dimension-uniform target

For every odd Pascal step, prove one of the following.

1. **Hall form:** the residence blocks and connector-isolated components
   admit an orthogonal occurrence-repair catalogue satisfying (2.1).
2. **LLL form:** their repair lists and conflict graph satisfy (3.1).

After this repair, one must still prove a labelled marked-path theorem and
the residual pair-column/common-cap gates.  The occurrence theorem is
therefore a regenerative sublemma, not the full shadow--braid theorem.

The `K17` data support the LLL direction particularly strongly at the last
local gate: `1411/1430` alternatives preserve residence and `122` also
remove the only isolation.  What is missing for an all-odd proof is a
dimension-uniform lower bound on repair-list size and an upper bound on the
support-conflict degree.

## 7. Provenance and scope

The exact finite data are in:

```text
scratch/census_k17_two_bank_single_occurrence_swaps_20260731.py
scratch/k17_two_bank_single_occurrence_swaps_20260731.census.json
scratch/build_k17_sixswap_macro_forest_20260731.py
scratch/k17_sevenswap_premaster_macro_forest_20260731.flow.json
scratch/search_k17_sevenswap_marked_component_path_20260731.py
scratch/k17_sevenswap_marked_component_path_20260731.json
```

Current rebuilt hashes:

```text
k17_two_bank_single_occurrence_swaps_20260731.census.json
SHA-256 e9797343a3d6e841195b01b3541814562f8af8c6645f0d8e4795e2f0a9fa1d83
payload f005edf2557ea5d4b489b765c8b34f3d509c0bdced5c5e8c203df7e04e8e8a7d

k17_sevenswap_premaster_macro_forest_20260731.flow.json
SHA-256 56f6701224913c1b3c09cedd1483595ef627d1bc946a87af43a8e73098dda0dc
payload 153644883597d6bd2f37f9f6271f7423f4db5302c304a83801bf66116566c5d7

k17_sevenswap_marked_component_path_20260731.json
SHA-256 70313f26d046ab24af053dbebeb775f8d516d1faf3666e9f85bd7d13acb343dd
payload bb21e3a05a00a0a5fbb811a0d9557b5647ec6bcf416d4b868aa6a38f6ae1c4fc
```

The finite witness establishes simultaneous residence cleanliness and
non-isolation for this fixed parent and occurrence catalogue.  The Hall and
LLL theorems are general conditional statements.  Neither supplies their
hypotheses in every dimension.
