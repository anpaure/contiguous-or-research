# Realizable Catalan side pairings are not a matroid: the exact four-resource face

Date: 2026-07-31  
Status: exact all-`n` atom-level formulation and exact `n=3` exchange
counterexample.  This rules out a direct ordinary-matroid or delta-matroid
closure on the natural pairing-edge ground; it does not rule out a richer
extended formulation or a Boolean-specific integral theorem.

## 0. Verdict

The corrected two-shore gate cannot be closed by declaring the physically
realizable anchor pairings to be the bases of one more matroid.

On the first valid child fibre (`n=3`), fix one authenticated common basis.
The no-anchor-free pairing families have orders

```text
minus shore: 4 pairings,       plus shore: 2 pairings.
```

Both families fail basis exchange.  Since every feasible pairing has the
same cardinality `Cat_3=5`, they also fail the symmetric-exchange axiom of a
delta-matroid.  Of the eight possible minus/plus combinations, exactly two
give an acyclic contracted attachment graph.  Thus even at the base the
joint topology is a sparse compatibility relation, not the product of two
marginal basis families.

There is nevertheless an exact all-`n` structural formulation.  A side
representative is the intersection of

1. a lower-colour partition-matroid base;
2. an upper-colour partition-matroid base;
3. a pullback graphic-matroid independent set; and
4. an overlapping physical `b`-matching capacity system.

The component pairing is a nonlinear projection of this four-resource
face.  The capacity system is not a matroid in general, and the concrete
`n=3` projection is neither a matroid nor a delta-matroid.  The exact
remaining theorem is therefore a Boolean-specific **rainbow graphic
`b`-matching with two-shore compatibility**, not ordinary two-matroid
intersection.

## 1. Exact atom-level side formulation

Fix one shore of the two-coordinate recursion, a common deletion basis
`Q`, its punctured rank-`n` bank

\[
                         D\subseteq{[2n]\choose n},\qquad |D|=P,
\]

and its seam-anchor bank

\[
                         B\subseteq{[2n]\choose n+1},\qquad |B|=C.
\]

The opposite palette is

\[
                         {\cal U}={[2n]\choose n+2},\qquad |{\cal U}|=P.
\]

Define the atom ground

\[
 {cal A}(D)=\{(L,U):L\in D, U\in{\cal U}, L\subset U\}.       \tag{1.1}
\]

If `U-L={x,y}`, its physical edge is

\[
                     \psi(L,U)=\{L+x,L+y\}             \tag{1.2}
\]

on the rank-`(n+1)` owner bank.  The map `psi` is injective because the
intersection and union recover `(L,U)`.

Let `M_L,M_U` be the partition matroids on `cal A(D)` whose blocks consist
of atoms having the same `L` and the same `U`, respectively, each with
capacity one.  Let `M_G` be the pullback through `psi` of the graphic
matroid on the complete owner graph.  Finally put

\[
 b_v=\begin{cases}1,&v\in B,\\2,&v\notin B,
       \end{cases}                                      \tag{1.3}
\]

and let

\[
 {cal I}_b=\left\{J\subseteq{\cal A}(D):
       \sum_{a:\,v\in\psi(a)}1_{a\in J}\le b_v
       \quad\hbox{for every owner }v\right\}.           \tag{1.4}
\]

### Theorem 1.1 (exact rainbow graphic `b`-matching face)

A set of atoms `J` is a punctured saturating side forest with the required
anchor degree caps if and only if

\[
 \boxed{J\in{\cal B}(M_L)\cap{\cal B}(M_U)
               \cap{\cal I}(M_G)\cap{\cal I}_b.}       \tag{1.5}
\]

The no-anchor-free condition is the additional requirement that every
component of `psi(J)` meet `B`.  When it holds, the components induce the
`Cat_n`-matching of double anchors used in the topology theorem.

#### Proof

Being a base of `M_L` chooses exactly one atom for every `L in D`; being a
base of `M_U` chooses exactly one for every `U in cal U`.  Their common
bases are precisely the containment perfect matchings between the two
palette shores.  Graphic independence is precisely acyclicity of the
physical edges (1.2).  Inequalities (1.4) are exactly maximum degree two at
ordinary owners and maximum degree one at seam anchors.  These are all the
side conditions.  The final sentence is the signed component-charge lemma.
\(\square\)

This explains why the automatic common-basis theorem is not the last
integrality theorem: it closes the existence of common bases for the
**diagonal palettes**, while (1.5) is a common base of two partition
matroids with two further nonredundant physical rows.

### Proposition 1.2 (the capacity row is not a matroid)

Even the unit-capacity specialization of `cal I_b` is not a matroid on
physical edges.  On the three-edge path

```text
                         1-2-3-4
```

the matching sets `{23}` and `{12,34}` are feasible, but neither edge of
the larger set can augment `{23}`.

#### Proof

Both additions give two edges incident with vertex 2 or vertex 3,
respectively.  This violates the matroid augmentation axiom. \(\square\)

With capacities one and two mixed as in (1.3), the same obstruction embeds
whenever the middle owners are anchors.  More importantly, Section 2 gives
a counterexample in the actual Boolean side fibre after all four rows of
(1.5) have been imposed.

## 2. Literal `n=3` exchange failure

Use the authenticated child forest

```text
19-49, 13-28, 37-35-42-14-22-50-56-25-11-7-21-52-44-41,
38, 26
```

and retain child edge `0`, namely `19->49`.  The other fourteen edges form
the common deletion basis `Q`.  Exhausting every `6!` diagonal bijection on
each shore and retaining exactly the physical forests with anchor caps and
no anchor-free component gives the following minus-shore pairing family:

\[
\begin{aligned}
P_0={}&\{13,24,38,57,9\,11\},\\
P_1={}&\{13,26,3\,14,57,9\,11\},\\
P_2={}&\{13,3\,14,46,59,8\,11\},\\
P_3={}&\{15,3\,14,46,79,8\,12\},                 \tag{2.1}
\end{aligned}
\]

where, for example, `13` denotes the anchor pair `{1,13}`, not the integer
thirteen.  Written without this abbreviation, one exchange witness is

\[
\begin{aligned}
X={}&\{(1,5),(3,14),(4,6),(7,9),(8,12)\},\\
Y={}&\{(1,13),(2,4),(3,8),(5,7),(9,11)\}.           \tag{2.2}
\end{aligned}
\]

### Theorem 2.1 (realizable pairings are not matroid bases)

For `e=(3,14) in X-Y`, no `f in Y-X` makes

\[
                             X-e+f                    \tag{2.3}
\]

one of the four realizable pairings.  Hence the minus-shore family is not
the basis family of a matroid on the anchor-pair ground.  The two-member
plus-shore family also fails basis exchange.

Both families fail the delta-matroid symmetric-exchange axiom.

#### Proof

The four minus pairings and two plus pairings are the complete filtered
census, so direct comparison proves (2.3) and its plus-shore analogue.

For the delta-matroid statement, observe generally that if every feasible
set has the same size, symmetric exchange reduces to basis exchange.  Given
`e in X-Y`, toggling `e` alone changes the size by one, and toggling it with
a second member of `X-Y` changes the size by two.  The only size-preserving
choice is to toggle `e` with some `f in Y-X`, which is exactly (2.3).
Therefore the same witness violates symmetric exchange. \(\square\)

The theorem concerns the natural ground whose elements are unordered anchor
pairs.  It does not exclude an extended delta-matroid representation with
auxiliary occurrence or path-state elements.

## 3. The two-shore relation is genuinely correlated

For the same retained child edge, index the four minus pairings and two plus
pairings lexicographically by their edge lists.  The complete contracted
acyclicity relation is

\[
                              \{(0,0),(1,1)\}.          \tag{3.1}
\]

Thus two minus pairings have no compatible plus pairing at all; the other
two each accept exactly one of the plus pairings.

### Corollary 3.1 (no marginal common-basis closure)

Separate nonemptiness of the two physically realizable side-pairing
families does not imply a joint acyclic collar, even for a common basis
whose full collar is positive.  A proof must retain the compatibility
relation (3.1), or prove additional richness/alignment which makes a
graphic completion automatic.

#### Proof

The full source census has four legal minus sides and two legal plus sides,
but only the two pairs in (3.1) make the contracted attachment graph a
forest.  Marginal existence cannot distinguish the six failing products
from the two successes. \(\square\)

The finite relation is small but conceptually exact: the topology theorem
is a graphic constraint **after** nonlinear projection from the atom
choices to component pairings.

## 4. Correct structural target

For a fixed common basis `Q`, the atom-level two-shore problem consists of
two copies of (1.5), coupled by the graphic independence of their component
pairings together with the central partial matching `P_0(Q)`.  Symbolically,

\[
 \begin{split}
 J^-&\in{\cal B}(M_L^- )\cap{\cal B}(M_U^-)
             \cap{\cal I}(M_G^- )\cap{\cal I}_{b^-},\\
 J^+&\in{\cal B}(M_L^+ )\cap{\cal B}(M_U^+)
             \cap{\cal I}(M_G^+ )\cap{\cal I}_{b^+},             \tag{4.1}
 \end{split}
\]

and

\[
          P_0(Q)\cup\Pi(J^-)\cup\Pi(J^+)
          \quad\hbox{is graphic-independent}.          \tag{4.2}

Here `Pi` is the component-pair projection.  It is not a linear map of atom
incidence vectors.

Consequently the most promising positive theorem must use special Boolean
structure beyond generic oracle intersection.  Three exact possibilities
remain.

1. **Aligned catalogue:** construct side atom catalogues on which one of the
   four rows in (1.5) implies another, reducing to ordinary two-matroid
   intersection.
2. **Private path sockets:** arrange that every side component has a fixed
   private anchor attachment, making (4.2) automatic before palette
   matching.
3. **Bounded-interface dynamic state:** preserve the finite component-
   pairing compatibility relation through the two-coordinate induction,
   rather than projecting it to one scalar or one matroid rank.

What is ruled out is the simplest hoped-for route:

```text
automatic common basis + one matroid/delta-matroid pairing oracle.
```

The first Boolean base already violates that abstraction.

## 5. Reproducible audit

The exact audit

```text
scratch/audit_catalan_side_pairing_nonmatroid_n3_20260731.py
```

reuses the frozen literal side enumerator

```text
scratch/audit_h2_catalan_two_coordinate_n3_all_common_bases_physical_20260731.py
```

at its recorded SHA.  It re-enumerates every side incidence bijection for
retained child edge zero, filters physical forest/anchor-cap/no-empty
signatures, checks basis and symmetric exchange exhaustively, and evaluates
all eight contracted minus/plus products.  It writes

```text
scratch/catalan_side_pairing_nonmatroid_n3_20260731.audit.json.
```

This is a complete finite counterexample in one actual Catalan collar, not
an abstract catalogue.  It does not prove hardness, exclude richer extended
formulations, or obstruct the two successful joint pairings in (3.1).
