# Uniform coordinate twists stabilize complete PBBS target banks, but not every longitudinal component transport

**Date:** 2026-08-05  
**Method:** target-bank reindexing, PBBS rotation equivariance, and commuting cycle actions; no computation or search  
**Status:** unconditional stabilizer theorem and exact realization gate.  A uniform coordinate rotation enlarges the admissible terminal stabilizer beyond local three-port permutations.  It is canonically realized as an automorphism of the full PBBS factor, but no known theorem realizes one nonzero rotation longitudinally inside every PBBS component.

## 0. Outcome

Let `rho` be cyclic coordinate rotation on `Z_n`, `n=2m+1`.  If a terminal occurrence transport sends every chosen target witness for `S` to a witness for

\[
                         \rho^sS,                         \tag{0.1}
\]

then a complete lower/upper bank remains complete: assign target `U` to the transported old witness for `rho^(-s)U`.  The same reindexing transports an occurrence-capacitated compiler.

Thus the exact admissible terminal stabilizer of a **complete target bank** contains the global coordinate group `C_n`, in addition to whatever local three-port deck stabilizer is available.  In fact the Boolean rank families are invariant under all coordinate permutations; `C_n` is singled out because it is a symmetry of the canonical PBBS chronology.

For the PBBS map `g`,

\[
                         g\rho^s=\rho^sg.                  \tag{0.2}
\]

Hence `rho^s` is an exact occurrence automorphism of the full factor and of every all-depth lower/complementary-upper fan deck.

This does **not** mean that an unmodified directed path inside every PBBS component realizes `rho^s`.  For a component `C`, such a longitudinal realization exists exactly when

\[
                         \rho^sC=C.                        \tag{0.3}

\]

In that case there is a unique factor time `t_C(s)` with

\[
                         \rho^s|_C=g^{t_C(s)}|_C.          \tag{0.4}

\]

The time may depend on `C`.

The known terminal component `J_b=(3,2,1^(b-1))` gives a sharp warning.  In one congruence class spatial rotation cyclically permutes three distinct PBBS cycles, so `rho` is not an in-component transport there; only `rho^3` is.  Therefore no theorem may use a nonzero uniform twist as a **longitudinal** return without first checking the component action.

The corrected aligned-macro target may consequently be weakened from relative identity to

\[
                         \overline H=\rho^s             \tag{0.5}

\]

on the complete transported bank.  But (0.5) is still an open physical planting statement; PBBS equivariance alone supplies an abstract global automorphism, not the required product of aligned site and path maps.

## 1. Complete-bank rotation lemma

Let `\mathcal T` be a target family invariant under `rho`.  Suppose

\[
                         b:\mathcal T\longrightarrow\mathcal O          \tag{1.1}
\]

is an injective chosen occurrence bank with

\[
                         \operatorname {val}(b(S))=S.     \tag{1.2}
\]

### Theorem 1.1 (uniform-twist stabilizer)

Suppose an output occurrence injection `Phi` satisfies, for one fixed `s`,

\[
 \operatorname {val}'(\Phi(b(S)))=\rho^sS
 \qquad(S\in\mathcal T).                              \tag{1.3}
\]

Then

\[
                         b'(U)=\Phi(b(\rho^{-s}U))       \tag{1.4}
\]

is a complete output bank for the original literal target family.

If `Phi` preserves occurrence types and unit capacities, every compiler
matching on `b(\mathcal T)` transports to one on `b'(\mathcal T)`.

#### Proof

Rotation invariance gives `\rho^{-s}U\in\mathcal T`.  Equations
(1.3)--(1.4) give

\[
 \operatorname {val}'(b'(U))
 =\rho^s\rho^{-s}U=U.
\]

Both maps in (1.4) are injective.  Reindexing the left shore of a matching by the bijection `U -> rho^(-s)U` preserves all occurrence capacities. `square`

### Corollary 1.2 (simultaneous Boolean banks)

One uniform twist preserves simultaneously:

1. every strict-lower rank family;
2. the complete middle owner layer;
3. every proper-upper rank family; and
4. a paired lower/upper bank obtained by complementation.

Indeed coordinate rotation preserves rank, inclusion, union, intersection, and complementation.

## 2. Stabilizer scope: coverage versus exact multiplicity current

Theorem 1.1 concerns a chosen complete injection, not an arbitrary overcomplete multiplicity vector.

Let `mu(S)` be the number of old occurrences of target `S`.  A uniformly rotated output bank has

\[
                         \mu'(U)=\mu(\rho^{-s}U).         \tag{2.1}

\]

Therefore:

* support completeness is always preserved;
* one chosen occurrence per target and its compiler matching are always preserved by reindexing;
* pointwise signed multiplicity current is zero only when `mu` is invariant under `rho^s`.

The full all-start PBBS occurrence deck has this invariance by equivariance.  A deterministic gap section with a non-equivariant tie rule need not have an invariant overcomplete histogram.  Its chosen one-per-target subbank is nevertheless safe under Theorem 1.1 whenever the occurrence transport (1.3) is literal.

This is why uniform target reindexing is a genuine enlargement of the proof interface but not a license to equate arbitrary local current vectors.

## 3. Enlargement beyond the local three-port stabilizer

Let `G_loc<=S_3` be the stabilizer of the local triangular port deck.  A local role permutation acts on the port address `i`; a ground rotation acts on every literal set value.  On the abstract complete bank the two actions commute:

\[
                         (\pi,\rho^s):(i,S)\longmapsto(\pi i,\rho^sS). \tag{3.1}

\]

### Theorem 3.1 (product stabilizer)

The admissible complete-bank stabilizer contains

\[
                         G_{loc}\times C_n.               \tag{3.2}

\]

If all coordinate permutations are admitted abstractly, `C_n` may be replaced by `Sym(n)`.  For canonical PBBS transport, the proved orientation-preserving symmetry is `C_n`; coordinate reflection conjugates `g` to `g^(-1)` and is not a positive longitudinal symmetry.

#### Proof

The local action changes only occurrence roles.  The ground action changes every coordinate in every target and owner.  Hence they commute.  Local deck stabilization and Theorem 1.1 may be applied in either order. `square`

For `s\ne0`, this is normally a strict enlargement.  No rank-`m` PBBS
owner is fixed by a nonidentity rotation, because a rotation orbit size
would divide both `m` and `2m+1`.  Thus ground rotation is not merely a
hidden local port permutation.

## 4. PBBS realizes rotation globally

### Theorem 4.1 (all-depth occurrence equivariance)

For every cyclic PBBS occurrence

\[
                         I=(X,gX,\ldots,g^qX),            \tag{4.1}
\]

the rotated sequence

\[
                         \rho^sI=(\rho^sX,g\rho^sX,\ldots,g^q\rho^sX) \tag{4.2}

\]

is another literal PBBS occurrence.  Its lower intersection and upper complementary union are respectively the `rho^s` rotations of those of `I`.

Consequently `rho^s` is an exact automorphism of the complete all-depth PBBS occurrence deck.

#### Proof

Cyclic parenthesis matching has no distinguished origin, so `g rho^s=rho^s g`.  Apply this identity at every state in (4.1).  Rotation commutes with intersection, union, and complementation. `square`

This is a global factor automorphism: it may send one PBBS component to another.

## 5. Exact longitudinal realization criterion

Let `C` be one directed `g`-component.

### Theorem 5.1 (component return criterion)

The following are equivalent.

1. Some unmodified directed path in `C` transports one state `X` to `rho^sX`.
2. `rho^sX` belongs to `C` for one `X\in C`.
3. `rho^sC=C`.

When these conditions hold, there is one residue `t_C(s) mod |C|` such that

\[
                         \rho^sX=g^{t_C(s)}X             \tag{5.1}
\]

for every `X\in C`.  The complete past/future fan state is transported by
the same identity.

#### Proof

The implications `1=>2=>3` use membership and the commutation (0.2).  If
`rho^sC=C`, choose `X_0\in C`.  Transitivity of `g` on its directed cycle
gives a unique `t` with `rho^sX_0=g^tX_0`.  For `X=g^uX_0`,

\[
 \rho^sX=\rho^sg^uX_0=g^u\rho^sX_0=g^{u+t}X_0=g^tX.
\]

This proves (5.1) and every implication.  Applying the equality to all neighboring times transports the complete history state. `square`

### Corollary 5.2 (global in-place twist gate)

One nonzero rotation is realized longitudinally on every component in a
family `\mathcal C` exactly when

\[
                         s\in\bigcap_{C\in\mathcal C}
                         \{a:\rho^aC=C\}.                \tag{5.2}

\]

The path times `t_C(s)` may vary with `C`; uniform coordinate voltage does not mean uniform factor time.

## 6. Known canonical transports and the no-go boundary

Several special PBBS components do realize nonzero twists internally.

1. On the rectangular all-unit and single-soliton components, the audited rooted evolution fixes the unrooted shape and moves the physical root.  Their rotation copies therefore occur on the same component.
2. For the terminal action shape `J_b=(3,2,1^(b-1))`, the exact action-angle theorem gives

   \[
                            \delta=\gcd(3,b),
   \]

   up to the equivalent `r=b-1` indexing, and proves that powers of `rho^delta` stabilize one component with factor-time gap at most `21`.

The same theorem supplies an exact obstruction.  In the congruence class `delta=3`, spatial rotation `rho` cyclically permutes three distinct PBBS components.  Therefore `rho` is **not** a longitudinal transport on those components.

### Corollary 6.1 (no universal one-step longitudinal rotation)

For infinitely many terminal parameters, no family of unmodified paths, one inside each PBBS component, can realize the uniform twist `rho` on the complete factor.  The terminal `J_b` sector already violates (5.2).

The power `rho^3` closes that particular sector, but no theorem in the present record proves that one fixed nonzero `s` stabilizes every PBBS component.  The intersection in (5.2) may be trivial when all action sectors are included.

Thus the known status is:

* **global occurrence automorphism:** proved for every `rho^s`;
* **special-component longitudinal transport:** proved on the components above;
* **one nontrivial longitudinal twist on every component:** open, and false for `s=1` on the terminal three-cycle sector;
* **realization by a product of aligned positive C6 sites:** open.

## 7. A bounded local macro cannot usually close a nontrivial twist

Let the order of `rho^s` on coordinates be

\[
                         h={n\over\gcd(n,s)}.             \tag{7.1}

\]

The rotation action on rank-`m` owners is free: a stabilized owner would
be a union of coordinate orbits of size dividing both `m` and `n`, while
`gcd(m,n)=1`.

### Theorem 7.1 (support-orbit divisibility)

If a nonempty finite set `A` of rank-`m` owner occurrences is invariant
under `rho^s`, then

\[
                         h\mid |A|.                       \tag{7.2}

\]

In particular, if `n` is prime and `s\ne0`, every nonempty invariant owner
support has at least `n` members.

#### Proof

Every `rho^s` orbit on rank-`m` owners has size exactly `h`, by freeness.
An invariant set is a disjoint union of such orbits. `square`

### Corollary 7.2 (constant-site local-twist obstruction)

On infinitely many prime values `n=2m+1`, a fixed number of resident C6
sites has owner support `O(d)=O(sqrt(n))<n`.  Such a self-contained macro
cannot have its complete owner support return under a nonidentity uniform
rotation.

Therefore a coordinate twist can help a bounded aligned macro only through
a **global handoff** to rotated occurrences outside the local support, or
through a full rotation-orbit packet family.  It is not a hidden local
two-site or four-site return mechanism.

This does not obstruct the global complete-bank lemma: that bank already
contains every rotated target and every middle owner.  It separates the
global stabilizer gain from the local physical realization problem.

## 8. Corrected aligned-macro criterion

Let `widehat tau^k` be the unavoidable physical strand-tag transport of an aligned `k`-site macro, and put

\[
                         \overline H=\widehat\tau^{-k}H. \tag{8.1}

\]

For a complete target bank, the sufficient terminal condition may be weakened from `bar H=I` to

\[
                         \boxed{\overline H=\rho^s}      \tag{8.2}

\]

under one literal occurrence transport, or more generally

\[
                         \overline H\in
                         (G_{loc}\times C_n)             \tag{8.3}

\]

with the relevant local deck stabilizer and compiler types retained.

Equation (8.2) genuinely enlarges the algebraic target.  It does not solve
the physical macro: one must still show that the chronological product of
its site and intersite maps is the same uniform `rho^s` on every protected
lower and upper occurrence.  Componentwise phase shifts, unrelated
coordinate permutations, or rank-histogram equality do not suffice.

## 9. Scope

Proved:

1. exact complete-bank and compiler transport under one coordinate twist;
2. the product enlargement by the cyclic ground symmetry;
3. exact all-depth PBBS rotation equivariance;
4. the necessary-and-sufficient component return criterion; and
5. failure of uniform one-step longitudinal rotation on the known terminal
   three-component sector;
6. the support-orbit obstruction to a bounded self-contained twist macro.

Not proved:

1. one nonzero twist stabilizing every PBBS component;
2. a globally aligned C6 macro realizing (8.2);
3. compatibility with a fixed non-rotation-invariant typed common cap or opening sidecar; or
4. an all-dimensional upper bound.
