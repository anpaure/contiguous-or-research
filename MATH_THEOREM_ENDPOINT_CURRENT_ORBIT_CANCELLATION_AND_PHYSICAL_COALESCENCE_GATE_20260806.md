# Finite orbit cancellation of endpoint currents, and the physical coalescence gate

**Date:** 2026-08-06  
**Method:** pure mathematics; finite-group averaging and convexity only  
**Status:** unconditional algebraic cancellation theorem; exact conditional
physical lift with all resource and occurrence premises stated explicitly.

## 0. Verdict

Endpoint leakage of a fixed finite component history has no asymptotic
algebraic obstruction.  Let a finite coordinate group `G` act transitively
on the endpoint types, and let

\[
                         D_1,\ldots,D_t                 \tag{0.1}
\]

be the endpoint currents of the `t` phase transitions.  Each `D_i` has
total sum zero.  A finite multiset of coordinate-conjugate **whole
histories** can be chosen so that

\[
                         \sum_c g_cD_i=0
                         \qquad(1\le i\le t)            \tag{0.2}
\]

simultaneously.  One may take the complete finite group orbit.  More
sharply, if there are `p` endpoint types, at most

\[
                              t(p-1)+1                  \tag{0.3}
\]

distinct conjugate history types are needed, with positive integer
multiplicities.

For the four-switch semilength-four Haar history:

* the unoriented complementary endpoint-pair set has size `35`, so at most
  `4*34+1=137` conjugate history types suffice abstractly;
* the oriented terminal endpoint set has size `70`, so the completely
  orientation-safe bound is `4*69+1=277` types.

All these numbers are absolute constants.

The physical qualification is load-bearing.  If the endpoint-claim images
of the suffix cylinders are pairwise disjoint, their currents cannot cancel:
a zero sum then forces every cylinder current to vanish separately.  Orbit
cancellation requires a common or routed endpoint halo in which a target
removed by one cylinder is installed by another.  The cylinder interiors
may be private, but their endpoint claims must be coalesced.

Under an exact common-halo packing premise, (0.2) makes every phase an exact
factor transition.  Terminal endpoint cancellation automatically cancels the
proper tail-state and tail-edge currents.  For arbitrary-width crossing
chords one must average the finite **complete boundary-current vector**, not
merely the terminal endpoint histogram.  The same orbit theorem applies to
that augmented vector.  Thus the remaining theorem is physical occurrence
routing, not finite current arithmetic.

## 1. Endpoint-current spaces

Let `Omega` be a finite set of endpoint types and let a finite group `G`
act on `Omega`.  Write

\[
                         V=\mathbb Q^\Omega.            \tag{1.1}
\]

For a local component replacement with old and new endpoint histograms
`e^-`,`e^+`, put

\[
                         D=e^+-e^-\in\mathbb Z^\Omega.  \tag{1.2}
\]

The two shores have the same number of rows, so

\[
                         \sum_{x\in\Omega}D(x)=0.       \tag{1.3}
\]

Two choices of `Omega` are useful.

1. **Oriented endpoints:**
   \[
                         \Omega_{\rm or}={ [2a]\choose a}.
                                                               \tag{1.4}
   \]
2. **Complementary endpoint pairs:**
   \[
       \Omega_{\rm pair}
        =\bigl\{\{X,[2a]-X\}:X\in{[2a]\choose a}\bigr\}.      \tag{1.5}
   \]

The symmetric group `S_(2a)` is transitive on both sets.  The pair quotient
may be used when row orientations can be selected coherently; the oriented
space is the proof-safe physical terminal ledger.

## 2. Exact Reynolds formula

### Theorem 2.1 (orbit-sum formula)

Let `O` run over the `G`-orbits of `Omega`.  For every `D in V`,

\[
 \boxed{
 \sum_{g\in G}gD
 =\sum_O { |G|\over |O|}
        \left(\sum_{x\in O}D(x)\right){\bf1}_O.}       \tag{2.1}
\]

Consequently the full group development cancels `D` if and only if

\[
                         \sum_{x\in O}D(x)=0           \tag{2.2}
\]

for every `G`-orbit `O`.  In particular, if `G` is transitive, every
zero-total endpoint current cancels.

#### Proof

Fix `y in O`.  For each `x in O`, exactly `|G|/|O|` group elements send
`x` to `y`.  Therefore the coefficient of `e_y` in the left side of (2.1)
is

\[
                 { |G|\over|O|}\sum_{x\in O}D(x),      \tag{2.3}
\]

independent of `y`.  This proves (2.1), and (2.2) follows.  \(\square\)

### Corollary 2.2 (distinct conjugates suffice)

Let `Stab_G(D)` be the stabilizer of `D`.  If (2.2) holds, then

\[
             \sum_{g\in G/\operatorname{Stab}_G(D)}gD=0.      \tag{2.4}

\]

Thus every distinct vector in the conjugacy orbit may be used once; repeated
group elements are unnecessary.

#### Proof

Every distinct orbit vector occurs `|Stab_G(D)|` times in (2.1).  Divide
the zero identity by that number.  \(\square\)

## 3. Coherent cancellation of a whole phase history

Let

\[
                         \mathbf D=(D_1,\ldots,D_t)\in V^t    \tag{3.1}
\]

be the endpoint-current vector of an entire fixed history.  The group acts
diagonally, so Theorem 2.1 applies to every coordinate simultaneously.

### Theorem 3.1 (finite coherent orbit cancellation)

Assume `G` is transitive on `Omega` and every `D_i` has total zero.  Then:

1. the complete diagonal orbit cancels every phase:
   \[
             \sum_{g\in G/\operatorname{Stab}_G(\mathbf D)}gD_i=0
             \qquad(1\le i\le t);                    \tag{3.2}
   \]
2. there are conjugates `g_1,...,g_q` and positive integers
   `n_1,...,n_q`, with
   \[
                            q\le t(|\Omega|-1)+1,       \tag{3.3}
   \]
   such that
   \[
                            \sum_{j=1}^q n_jg_jD_i=0
                            \qquad(1\le i\le t).       \tag{3.4}
   \]

The same conjugate and multiplicity are used at every phase; (3.4) is not
a separate phasewise selection.

#### Proof

Equation (3.2) is Corollary 2.2 applied in `V^t`.

For the sharper support bound, every `D_i` lies in the zero-sum subspace of
`V`, of dimension `|Omega|-1`.  Hence the orbit of `mathbf D` lies in a
space of dimension at most

\[
                              t(|\Omega|-1).            \tag{3.5}

\]

The uniform Reynolds average says that zero lies in the convex hull of that
finite orbit.  Caratheodory's theorem expresses zero as a convex combination
of at most (3.3) orbit points.  The orbit points are integral, so the
feasible convex polytope is rational; choose rational coefficients and
clear denominators.  The positive numerators are the `n_j` in (3.4).
\(\square\)

### Corollary 3.2 (the four-switch constants)

For `a=4,t=4`,

\[
                         |\Omega_{\rm pair}|={1\over2}{8\choose4}=35,
 \qquad                 |\Omega_{\rm or}|={8\choose4}=70.     \tag{3.6}
\]

Therefore (3.3) gives respectively `137` and `277` distinct conjugate
history types.  After clearing denominators, the total number of copies is
some absolute finite constant independent of the lifted dimension.

There is also a completely explicit multiplicity-free bound.  The alternating
group `A_8` is transitive on four-subsets, and hence on both ledgers in (3.6).
Using every element of `A_8` once cancels the whole history with at most

\[
                              |A_8|=20160                         \tag{3.7}
\]

copies.  This is not intended as an efficient physical constant; it removes
any dependence on unspecified Caratheodory denominators.

Indeed, start with any permutation carrying one four-set to another.  If it
is odd, compose it with a transposition inside the target four-set; this
does not change the target set and makes the transporter even.  The same
argument descends to complementary pairs.

No claim is made that the Caratheodory multiplicities are small.  Their
finiteness is enough for an additive-constant architecture if a physical
host realizes the copies without adding one new word position per copy.

### Corollary 3.3 (two-copy inverse criterion)

If one group element `g` satisfies

\[
                              gD_i=-D_i
                              \qquad(1\le i\le t),       \tag{3.8}
\]

then the two histories `mathbf D` and `gmathbf D` cancel.  More generally,
one forward occurrence and one resource-disjoint reverse occurrence of the
same entire history have opposite endpoint currents.

This is the smallest possible orbit absorber, but a common `g` satisfying
(3.8) need not exist for a multistep history.

## 4. Endpoint images and the augmented all-width theorem

Fix one suffix path `S`.  At a proper tail state the physical current of a
component is

\[
                         T_jD,
 \qquad T_j(e_X)=e_{X+S_j}.                            \tag{4.1}
\]

At a tail adjacent union it is

\[
                         U_jD,
 \qquad U_j(e_X)=e_{X+(S_{j-1}\cup S_j)}.             \tag{4.2}
\]

If the coordinate action is confined to the base ground, these maps are
equivariant:

\[
                              L(gD)=gL(D).              \tag{4.3}
\]

Consequently endpoint-current cancellation alone cancels every proper tail
state and tail adjacent-union current.

It does **not** follow in general that terminal endpoint current determines
every wider chord crossing the base/tail cut.  Such a chord may remember an
earlier base state.  In the tensored Tamari trade, for example, the complete
interface consists of six endpoint union/intersection currents and four
finite internal currents, as computed in
`MATH_THEOREM_TAMARI_TENSOR_COMPLETE_CHORD_RAIL_CURRENT_20260806.md`.

The correct general formulation is still finite.  Let `A` index every
finite boundary-current type needed by a fixed base history, let

\[
                 C_{i,\alpha}\in \mathbb Q^{\Omega_\alpha}
                 \qquad(1\le i\le t,\ \alpha\in A),             \tag{4.4}
\]

and let `G` act on each `Omega_alpha`.  This list may include terminal
endpoint current, internal base-chord currents, and the endpoint union and
intersection currents transported along the tail rails.

### Theorem 4.1 (finite complete-current orbit cancellation)

Assume that, for every `i`, `alpha`, and every `G`-orbit `O` in
`Omega_alpha`,

\[
                  \sum_{x\in O}C_{i,\alpha}(x)=0.               \tag{4.5}
\]

Then the complete diagonal `G`-orbit of the whole history cancels every
current `C_(i,alpha)` simultaneously.  Moreover a positive integral
relation exists using at most

\[
             1+\sum_{i=1}^t\sum_{\alpha\in A}
               \sum_{O\in\Omega_\alpha/G}(|O|-1)                \tag{4.6}
\]

distinct conjugate history types.

Every equivariant linear rail transport of these currents is cancelled by
the same relation.

#### Proof

Apply Theorem 2.1 in the direct sum of all the displayed current spaces.
Condition (4.5) says that the Reynolds projection is zero.  Apply
Caratheodory in the direct sum of the orbitwise zero-sum subspaces to obtain
(4.6), then clear rational denominators.  Finally, for every equivariant
linear transport `L`, linearity gives

\[
       \sum_j n_j L(g_j C_{i,\alpha})
       =L\!\left(\sum_j n_j g_j C_{i,\alpha}\right)=0.           \tag{4.7}
\]

\(\square\)

### Corollary 4.2 (proof-safe all-width scope)

For the tensored four-row Tamari trade, take the six endpoint currents and
four internal currents of the complete chord-rail theorem as the augmented
vector in Theorem 4.1.  Their full symmetric coordinate orbit cancels the
complete contiguous union/intersection ledger at every width.  More
generally, any orbit identity for that entire ten-current vector does so.

If only the terminal endpoint vector `D_i` is averaged, the unconditional
conclusion is limited to the tail-state and tail-edge maps (4.1)--(4.2),
unless the wider boundary currents are separately proved to factor linearly
through `D_i`.

## 5. Why literally disjoint cylinders cannot absorb one another

Let cylinder `c` have physical endpoint-claim embedding

\[
                         \phi_c:\Omega\longrightarrow\Xi.     \tag{5.1}
\]

Its physical endpoint current is `(phi_c)_*D_c`.

### Theorem 5.1 (disjoint-image no-cancellation)

If the sets `phi_c(Omega)` are pairwise disjoint, then

\[
                         \sum_c(\phi_c)_*D_c=0          \tag{5.2}
\]

if and only if

\[
                              D_c=0                    \tag{5.3}
\]

for every `c` for which `phi_c` is injective.

#### Proof

Restrict (5.2) to the coordinate block `phi_c(Omega)`.  Every other summand
vanishes there, leaving `(phi_c)_*D_c=0`.  Injectivity gives `D_c=0`.
\(\square\)

Therefore independent disjoint suffix sectors do not implement the Reynolds
identity.  Cancellation requires at least one of:

1. a common endpoint halo;
2. an occurrence router identifying claims from different sectors;
3. a cross-sector component whose old/new rows transfer ownership of the
   same physical endpoint targets; or
4. a jointly reselected outside completion which supplies the missing
   incidences.

The interiors can remain resource-disjoint.  The endpoint claims cannot.

### Corollary 5.2 (overlap-component localization)

Form the graph on cylinders in which `c` and `c'` are adjacent when their
physical claim images intersect.  If the aggregate physical current is zero,
then the aggregate current of the cylinders in **each connected component**
of this graph is zero separately.  In particular, every isolated cylinder
must already be sealed.

#### Proof

The unions of the claim images belonging to distinct graph components are
disjoint.  Restrict the zero-current identity to the union associated with
one component.  \(\square\)

Thus a nontrivial absorber needs not merely some accidental overlap: its
claim-overlap graph must connect every leaking subcollection which is meant
to cancel jointly.

## 6. Conditional physical exact-factor theorem

First isolate the exact incidence statement.  For phase `i`, let `R_i` be
the disjoint union of every capacity-one physical resource class whose exact
coverage defines the factor.  Let `a_(i,c)^-` and `a_(i,c)^+` be the
nonnegative integral incidence vectors of the old and new rows of cylinder
`c`, and let `o_i` be the retained outside incidence vector.

### Lemma 6.1 (complete-resource replacement criterion)

Assume the old shore is exact:

\[
                 o_i+\sum_c a_{i,c}^-={\bf1}_{R_i}.             \tag{6.1}
\]

Then the simultaneous replacement is an exact factor if and only if

\[
                 \sum_c(a_{i,c}^+-a_{i,c}^-)=0
                 \quad\hbox{in }\mathbb Z^{R_i}.                \tag{6.2}
\]

#### Proof

Add the left side of (6.2) to (6.1).  Equality gives the new all-one
incidence vector.  Conversely, subtract the two exact-factor identities.
\(\square\)

In particular, once (6.2) is proved in the **complete** physical resource
lattice, no separate new-row collision check is needed: its nonnegative
integral sum equals the old zero-one vector.  The difficulty is proving
(6.2), rather than proving only its projection to abstract endpoint names.

The following premise separates the solved orbit arithmetic from that live
physical problem.

### Definition 6.2 (capacity-faithful coherent cylinder development)

For conjugate histories `g_jmathbf D` with multiplicities `n_j`, such a
development consists of physical packet occurrences satisfying:

1. **Whole-history realization.**  Copy `(j,l)` carries one literal
   conjugate phase sequence
   \[
              g_jF_0\longrightarrow g_jF_1\longrightarrow\cdots
              \longrightarrow g_jF_t,                 \tag{6.3}
   \]
   with one consistent opening and suffix state through all phases.
2. **Private interiors.**  At the start of every phase transition, all
   non-halo states and colours of the selected old packets are pairwise
   disjoint and disjoint from the retained outside factor.
3. **Capacity-faithful common-halo router.**  Expand the aggregate signed
   abstract current into unit positive and negative claim tokens.  At each
   phase there is a type-preserving bijection
   \[
                         \rho_i:\mathcal P_i^+longrightarrow
                                  \mathcal P_i^-                 \tag{6.4}
   \]
   and an injective physical placement
   `eta_i: P_i^- -> H_i subset R_i` of the old negative tokens.  The literal
   new claim token `p` is realized at the exact physical occurrence
   `eta_i(rho_i(p))`.  Thus different copies may use different occurrence
   slots of the same abstract type, but positive claims are routed onto the
   old capacity-one bank rather than into disjointly tagged replicas.  If
   all-width preservation is claimed, these token sets are formed from the
   complete augmented boundary-current vector of Section 4.
4. **Complete-resource closure.**  Every signed resource not carried by the
   common halo cancels inside its private packet, and there are no omitted
   structural-zero, orientation, tail-history, or compiler-resource
   coordinates.  Equivalently, the full physical difference is
   After applying the router in item 3, the sum of the literal packet
   differences is exactly the routed orbit current, with no further
   coordinates.  In particular it is zero in the complete resource lattice:
   \[
             \sum_{j,l}
             (a_{i,(j,l)}^+-a_{i,(j,l)}^-)=0.           \tag{6.5}
   \]
5. **Common outside completion.**  At phase zero, the outside rows together
   with the old packet bank form an exact factor.  All outside rows are
   identical on the two shores of each simultaneous phase switch.

Items 3--4 are stronger than equality of abstract endpoint labels: they are
literal occurrence-level capacity statements.

The orbit identity guarantees equality of the numbers of positive and
negative tokens of each abstract type, hence an abstract type-preserving
bijection.  It does **not** guarantee that the positive literal rows can be
realized at the physical occurrences selected by `eta_i`; that realization
is exactly the router premise.

### Theorem 6.3 (orbit cancellation lifts to exact factors)

Assume (3.4) and a capacity-faithful coherent cylinder development.  Switch
all copies of phase `i` simultaneously, for `i=1,...,t`.  Then every
intermediate state is an exact shortest-wreath factor, the outside
completion is untouched, and all included equivariant current ledgers are
zero.  In particular, all widths are preserved when the development carries
the complete boundary-current vector of Section 4.

#### Proof

Induct on the phase.  At phase `i`, the old selected rows are a partial exact
factor by items 2--3.  Their base central current is zero because each local
component is an exact support trade.  Their complete halo current is zero by
(3.4).  Every included transported boundary current is zero by Theorem 4.1.
By (6.5), this is exactly the complete-resource identity (6.2).  Lemma 6.1
therefore preserves an exact factor and leaves the outside rows unchanged.
Item 1 supplies the correct old packets for the next phase.  Induction proves
the claim.
\(\square\)

## 7. Sharpened frontier

For every fixed finite base history, including the four-switch Haar circuit,
the endpoint-current vector admits an absolute-size coherent orbit absorber.
Thus neither endpoint counts nor finite-group representation theory can be
the remaining obstruction.

The unresolved theorem is:

> **Physical endpoint-halo coalescence.**  Realize one of the finite orbit
> absorbers inside a common exact factor so that the conjugate cylinder
> interiors are private, the endpoint claims share a capacity-one routed
> halo, and the same routing remains valid through every phase of the
> history.

Literal disjoint suffix cylinders are insufficient by Theorem 5.1.  The
needed construction must be a cross-sector ownership router or a joint
completion theorem.

The connected native companion graphs in the anchored `D_3` pentagon close
the **time-zero abstract generator-supply** row, but they do not imply this
router.  A suffix-suspended companion edge still has to be realized as a
reusable guarded excursion whose positive claims are installed on the old
common-halo occurrences.  Thus a positive `D_3` companion audit and the
orbit theorem are complementary: the former supplies connected generators;
the latter removes their finite current arithmetic; physical guarded reuse
and terminal common-cap compatibility remain.
