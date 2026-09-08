# PCPS Row 2: turn factors, transparent pull trees, and a safe rooted opening

**Date:** 2026-08-02  
**Lane:** K, protected Catalan--pivot / `PCS(m,d)` Row 2  
**Status:** exact support-level construction theorem, exact compact turn-table
formulation, and a quantitative private-absorber lemma.  Existence of the
required all-`m` protected upper-covering factor is not proved.

## 0. Result

Put

\[
 \Omega=[2m-1],\qquad
 \mathcal L={\Omega\choose m-1},\quad
 \mathcal V={\Omega\choose m},\quad
 \mathcal U={\Omega\choose m+1},
\]

\[
 W=|\mathcal L|=|\mathcal V|,\qquad
 U=|\mathcal U|,\qquad
 C=W-U=\operatorname {Cat}_m.                         \tag{0.1}
\]

The owner/immediate-upper row of `PCS(m,d)` has the following exact
factor-first sufficient form.

1. Choose a spanning two-factor of the Middle Levels incidence graph
   between `mathcal L` and `mathcal V`.  It must contain the phase-aligned
   `3d`-edge pivot owner collar and have an eligible occurrence of every
   member of the **full** immediate-upper task shore, including the
   distinguished boundary/`D` tasks.
2. Join its factor cycles by a one-phase strict pull incidence tree.  Each
   pull must avoid the protected collar and preserve the complete multiset
   of eligible full-shore task labels.  The result is one Hamilton cycle
   with the same occurrence availability.
3. If `b` of its `W` lower-root turns are ineligible for the full task shore,
   then at least
   \[
                       C-b+1                         \tag{0.2}
   \]
   eligible turn occurrences have a second eligible occurrence of the same
   task.  Therefore, when
   \[
                       C-b+1>3d,                     \tag{0.3}
   \]
   one such redundant occurrence lies outside the pivot.  Delete its
   non-predecessor incidence.  This opens the cycle to a rooted,
   lower-rainbow Hamilton owner path, preserves every full immediate-upper
   task, preserves the pivot successor path, and gives the corrected
   endpoint aperture automatically.

On the resulting rooted path support, every residual full-shore task family
is nonempty.  The contracted graphic-Rado theorem may now be invoked; since
the support is a path, its rank inequalities reduce to this occurrence
availability.  Thus Rado is used only **after** Row 2 has been born.

For the unguarded colour shore `b=0`.  Since `Cat_m>=m` for `m>=3`, the
pivot embedding condition `m>=3d+1` implies (0.3).  With literal boundary/
`D` eligibility, `b` is an exported support statistic and may not be silently
set to zero.

The exact all-parameter missing statement is isolated in Section 7 as the
**protected upper-task factor-and-pull lemma** `PUTP(m,d)`.  It is strictly
smaller than `PCS`: it contains no source antecedent, global address quotient,
residence replay outside the protected collar, deeper upper shadow, compiler,
or regeneration row.

## 1. Exact turn-table normal form

For `L in mathcal L`, its owner star is

\[
                  \mathcal S(L)=\{L+a:a\in\Omega-L\},\qquad
                  |\mathcal S(L)|=m.                  \tag{1.1}
\]

A **turn table** chooses an unordered pair

\[
                  \tau(L)=\{a_L,b_L\}\in{\Omega-L\choose2}.       \tag{1.2}
\]

It supplies the Johnson edge

\[
 e_L=(L+a_L)(L+b_L),\qquad
 \ell(e_L)=L,\qquad u(e_L)=L+a_L+b_L.                \tag{1.3}
\]

Call `tau` balanced when every owner `V in mathcal V` belongs to exactly two
chosen pairs:

\[
   |\{L:V\in\{L+a_L,L+b_L\}\}|=2.                    \tag{1.4}
\]

### Proposition 1.1 (turn tables are exactly Middle Levels two-factors)

Balanced turn tables are in bijection with spanning two-factors of the
Middle Levels incidence graph.  Under this bijection:

* every lower root occurs exactly once as a projected Johnson intersection;
* the projected owner graph is a spanning Johnson cycle cover;
* its upper-turn occurrence at `L` is exactly `L+a_L+b_L`; and
* the table is connected exactly when the Middle Levels factor is one
  Hamilton cycle.

#### Proof

Given `tau`, join `L` to the two owners `L+a_L,L+b_L`.  Every lower vertex
has degree two by construction and every owner has degree two by (1.4), so
the incidence graph is a spanning two-factor.  Conversely, the two owners
adjacent to a lower vertex `L` are distinct members of its star and hence
uniquely determine (1.2).  Suppressing `L` produces (1.3).  Distinct roots
give distinct lower colours, and suppression preserves components.  \(\square\)

Every factor component is even and therefore has two alternating perfect-
matching phases.  On a component containing the protected pivot, choose the
phase `M_0` containing its predecessor incidences; its other phase contains
the pivot successor incidences.  This phase choice is load-bearing.  A turn
table without it does not yet define the rooted support used by Rado.

### Full-shore eligibility

For ordinary Row 2, every turn `e_L` is eligible for the task `u(e_L)`.
To include literal boundary/`D` restrictions, attach an eligibility bit

\[
                  \epsilon(L,\tau(L))\in\{0,1\}.       \tag{1.5}
\]

An eligible occurrence still serves its unique value `u(e_L)`.  Define

\[
 \lambda_\tau(R)=
 |\{L:u(e_L)=R,\ \epsilon(L,\tau(L))=1\}|,
 \qquad
 b_\tau=|\{L:\epsilon(L,\tau(L))=0\}|.               \tag{1.6}
\]

The factor is **full-shore upper-covering** when

\[
                         \lambda_\tau(R)\ge1
                 \qquad(R\in\mathcal U).              \tag{1.7}
\]

Thus any distinguished boundary/`D` subset of `mathcal U` is included in
(1.7), with its literal provider restriction encoded by (1.5).  If a
boundary obligation is an occurrence-labelled task not determined by one
rank-`m+1` value, it must be added as a separate task label; the counting
and safe-opening conclusion below then require the corresponding task
alphabet and eligible-occurrence total to be restated.  Colour coverage
alone does not certify such an extra named row.

## 2. The unconditional fractional state and the exact defect ledger

Introduce a variable `y_(L,{a,b})` for every turn option.  The exact cycle-
cover relaxation is

\[
 \sum_{\{a,b\}}y_{L,\{a,b\}}=1,                       \tag{2.1}
\]

\[
 \sum_{L,\{a,b\}:V\in\{L+a,L+b\}}y_{L,\{a,b\}}=2.   \tag{2.2}
\]

The unguarded upper-cover rows are

\[
 \sum_{L,\{a,b\}:L+a+b=R}y_{L,\{a,b\}}\ge1
                 \qquad(R\in\mathcal U).             \tag{2.3}
\]

### Proposition 2.1 (uniform fractional turn factor)

The point

\[
                  y_{L,\{a,b\}}={1\over {m\choose2}}             \tag{2.4}
\]

satisfies (2.1)--(2.3).  Every owner has load exactly two and every upper
colour has load

\[
                   {{m+1\choose2}\over {m\choose2}}
                  ={m+1\over m-1}=1+{2\over m-1}.      \tag{2.5}
\]

#### Proof

There are `binom(m,2)` pairs at each root.  A fixed owner has `m` lower
facets; at each facet, `m-1` pairs contain that owner.  Its load is therefore
`m(m-1)/binom(m,2)=2`.  A fixed `R in mathcal U` contains
`binom(m+1,2)` roots of rank `m-1`, and exactly one option at each root has
union `R`, giving (2.5).  \(\square\)

This proves marginal fractional feasibility, not integral cycle-cover
existence with a pivot, guards, or connectivity.  The margin `2/(m-1)`
tends to zero; independent rounding has no constant reserve.

For an integral table, put `h(tau)=|{R:lambda_tau(R)=0}|` in the unguarded
case.  Since there are `W` occurrences and `U` colours,

\[
 \boxed{
   \sum_{R\in\mathcal U}(\lambda_\tau(R)-1)_+=C+h(\tau).
 }                                                       \tag{2.6}
\]

Indeed the number of represented colours is `U-h`, so the excess over one
on represented classes is `W-(U-h)`.  Hence upper coverage is exactly the
minimum possible repeat excess `C`.  A transparent pull cannot repair a
missing colour: it preserves both sides of (2.6).

## 3. Protected upper-transparent pull trees

Let `F=M_0 dotunion M_1` be an oriented spanning Middle Levels two-factor.
A **one-phase pull** is an alternating even incidence circuit which replaces
some edges of `M_1` by the other circuit phase and leaves `M_0` fixed.  It is
strict on a component set `H_z` when its deleted `M_1` edges lie in distinct
current factor cycles and its new phase joins those cycles into one.

It is **full-task transparent** when the multiset of eligible task labels at
all affected lower roots agrees before and after the pull.  This includes
the eligibility bit in (1.5), not merely the underlying set union.

Fix a family `mathcal Z` of pairwise incidence-vertex-disjoint one-phase
pulls, all disjoint from the protected pivot vertices.  Make the bipartite
incidence graph

\[
 \mathcal I(F,\mathcal Z)
   \quad\hbox{on}\quad
 \operatorname {Comp}(F)\mathbin{\dot\cup}\mathcal Z,             \tag{3.1}
\]

where an old factor component is adjacent to `z` when it contains a deleted
edge of `z`.

### Theorem 3.1 (transparent pull-tree Hamiltonization)

Suppose

1. `F` is full-shore upper-covering and contains the phase-aligned pivot,
   with every pivot successor turn eligible for its own full-shore task;
2. every member of `mathcal Z` is a strict full-task-transparent pull;
3. `mathcal I(F,mathcal Z)` is a tree; and
4. each pull has exactly one deleted edge in each incident old component.

Then the pulls can be ordered so their simultaneous symmetric difference is
one Hamilton cycle `H`.  The cycle contains the pivot with the same matching
phase and has exactly the same eligible full-task multiplicity vector as
`F`.

#### Proof

Root the incidence tree at an old factor component.  Process pull nodes
away from the root.  When a pull is processed, its parent-side deleted edge
lies in the unique component already accumulated toward the root, whereas
every other incident old component is in a fresh, disjoint subtree.  Thus
its deleted edges lie in distinct current cycles and strictness merges all
of them into one.  Pairwise incidence-vertex-disjointness keeps every later
circuit literal.  Induction over the tree leaves one cycle.

Each pull avoids the pivot and changes only `M_1`, so the protected phase is
unchanged.  Full-task transparency preserves the complete task multiplicity
vector at every step.  \(\square\)

The tree hypothesis may be replaced by the equivalent loose-hypertree
rank inequalities together with hereditary strictness.  Connectivity of
the two-section alone is insufficient.  The all-dimensional coherent-ECO
supply theorem proves that the coherent atom two-section is connected; it
does **not** prove a pairwise-disjoint strict incidence tree, so it does not
close Theorem 3.1.

## 4. The safe rooted opening and exact redundancy count

Let `H=M_0 dotunion M_1` be the Hamilton cycle from Theorem 3.1.  Let
`E=W-b` be the number of eligible turn occurrences.  Under (1.7), let `s`
be the number of task labels having multiplicity at least two.  The number
of eligible occurrences belonging to repeated task classes is

\[
                         E-U+s.                       \tag{4.1}
\]

If `E>U`, then `s>=1`, and therefore (4.1) is at least

\[
                         E-U+1=C-b+1.                 \tag{4.2}
\]

### Theorem 4.1 (protected redundant-provider opening)

Assume `H` contains the `3d` protected pivot turns and satisfies

\[
                         C-b+1>3d.                    \tag{4.3}
\]

Then there is a lower root `o` outside the protected pivot such that

* its eligible task has another eligible occurrence;
* deleting the `M_1` incidence at `o` preserves every full-shore task;
* `M_0` remains a perfect predecessor matching;
* `M_1-e_o` contracts relative to `M_0` to one rooted Hamilton path;
* the owner sequence is lower-rainbow, omitting only `o`; and
* `o` is contained in the intended owner endpoint, so the corrected
  endpoint aperture holds.

The complete pivot successor phase remains a contiguous protected subpath.

#### Proof

Equations (4.1)--(4.2) give at least `C-b+1` redundant eligible root
occurrences.  Since only `3d` roots are protected, (4.3) supplies one such
root `o` outside the pivot.

At `o`, the cycle has the two incidences `oM_0(o)` and `oM_1(o)`.  Delete
the latter.  The turn task at `o` disappears, but another eligible
occurrence of the same task survives; every other root turn is unchanged.
The deleted incidence is outside the pivot.

The remaining alternating incidence graph is one path whose endpoints are
the lower root `o` and the owner `M_1(o)`.  Suppressing the lower vertices
gives all `W` owners in order and all lower roots except `o` as their
pairwise-distinct consecutive intersections.  Relative to the retained
perfect matching `M_0`, the incidences of `M_1-e_o` are one directed rooted
path.  Finally `o subset M_0(o)` (and also `o subset M_1(o)` in the closed
cycle), so the omitted root is incident with an owner endpoint.  This is
the corrected aperture, not an arbitrary endpoint assumption.  \(\square\)

For ordinary unguarded upper colours, `b=0`.  The elementary inequality
`Cat_m>=m` for `m>=3`, together with `m>=3d+1`, gives
`C+1>3d`; hence the safe opening is automatic once the protected
upper-covering Hamilton cycle exists.

A cycle certificate and its opened path certificate are different objects.
The cycle has `W` lower turns; the path has `W-1`.  The theorem identifies
the exact redundant occurrence whose loss makes this difference harmless.
An arbitrary cut need not preserve the full shore.

## 5. Rado only after availability

Let `S=M_1-e_o` and let `P_1 subset S` be the pivot successor incidences.
Under the rooted map

\[
       \lambda(LV):L\longrightarrow M_0^{-1}(V),\qquad
       \operatorname {up}(LV)=M_0(L)\cup V,            \tag{5.1}
\]

`lambda(S)` is one directed path.  Every full upper task has an eligible
occurrence in `S`, by Theorem 4.1.  The protected pivot colours are distinct,
and their prescribed occurrences are eligible by Theorem 3.1's first
hypothesis.

Consequently the residual occurrence families used in the contracted
graphic-Rado theorem are all nonempty, while every subset of `S` is graphic-
independent.  Choosing the prescribed pivot occurrence for its colours and
one eligible occurrence for every residual colour gives an upper-exact
rooted forest directly; equivalently, all contracted Rado inequalities
hold.  This is the promised logical order:

\[
 \boxed{
 \text{upper occurrence availability on the whole path}
 \quad\Longrightarrow\quad
 \text{path-support Rado selection}.
 }                                                       \tag{5.2}
\]

No graphic rank theorem creates a missing boundary/`D` occurrence.

## 6. A quantitative private repair absorber

The transparent pull tree preserves an already complete task multiset; it
cannot repair the holes of its input factor.  The following exact lemma
isolates one sufficient repair bank before Theorem 3.1.

Let `F` be a protected two-factor and let `mathcal H` be its missing full-
shore tasks, `h=|mathcal H|`.  For each `R in mathcal H`, let `mathcal A_R`
be a family of protected-disjoint alternating circuits such that toggling
any `z in mathcal A_R`

* keeps a spanning two-factor;
* creates an eligible occurrence of `R`; and
* does not touch one fixed reserve occurrence chosen for every task already
  present in `F`.

Call two atoms conflicting when their incidence-vertex supports meet.

### Theorem 6.1 (private absorber by bounded conflict)

Assume every `mathcal A_R` has at least `q` atoms and every atom conflicts
with at most `Delta` atoms in each other family.  If

\[
                         q>(h-1)\Delta,                \tag{6.1}
\]

then one can choose pairwise support-disjoint atoms `z_R in mathcal A_R`.
Toggling all of them yields a protected full-shore upper-covering two-factor.

#### Proof

Order the missing tasks arbitrarily.  After fewer than `h` atoms have been
chosen, at most `(h-1)Delta` members of the next family conflict with an
earlier choice.  Equation (6.1) leaves a legal atom.  The selected circuits
are vertex-disjoint, so their toggles commute and retain degree two.  The
fixed reserve witnesses keep every old task present, and `z_R` supplies each
formerly missing task.  \(\square\)

This is a quantitative absorber lemma, not a Boolean supply theorem.  The
unproved Boolean row is to construct such banks (or a sharper correlated
matching) with the literal boundary/`D` eligibility and with a subsequent
transparent pull tree.  Mere menu size does not imply (6.1).

## 7. The exact smaller all-parameter lemma

Call `PUTP(m,d)` the following assertion.

> There is a phase-oriented spanning Middle Levels two-factor `F` which
> contains the sharp `3d`-turn pivot collar, whose successor turns are
> eligible for their own tasks, covers every full immediate-
> upper task (including every boundary/`D` task in its eligible phase), and
> admits a protected-disjoint, full-task-transparent strict pull incidence
> tree.  Its ineligible-turn count `b` satisfies `C-b+1>3d`.

### Corollary 7.1

`PUTP(m,d)` implies `PCS(m,d)` Row 2: a rooted lower-rainbow Johnson
Hamilton path containing the protected pivot, with an eligible occurrence
of every full immediate-upper task and with the corrected endpoint aperture.
It also supplies the upper-exact rooted Catalan forest after the path-support
Rado step.

This implication is Theorems 3.1, 4.1 and Section 5.

`PUTP` is strictly smaller than `PCS`.  It does not mention:

* the source word or maximal-erosion envelopes;
* global physical address/history replay;
* residence outside the already proved local pivot collar;
* upper witnesses of width greater than one turn;
* the terminal common-cap/lower compiler; or
* regeneration of the next Pascal aperture.

There are two unconditional pieces toward its hypotheses.

1. For `6d<=m-2`, the small protected-factor theorem embeds the complete
   pivot incidence path in some spanning two-factor.  That completion need
   not cover the upper task shore.
2. The full coherent-ECO catalogue has connected component two-section in
   every dimension.  It does not supply the disjoint strict transparent
   incidence tree required above.

The obvious canonical shortcut is impossible.  The lexical GMN base factor
misses

\[
 M_r=W_r{(r-2)(r-3)\over2(r+2)(2r-1)},\qquad r=m-1,    \tag{7.1}
\]

upper colours, while a canonical pull tree changes at most
`3(C_r-1)` turn values.  The audited inequality

\[
                         M_r>3(C_r-1)                  \tag{7.2}
\]

holds for `r>=11`, i.e. `m>=12`.  Therefore no choice of the unmodified
canonical lexical pull spanning tree can be upper-covering in the eventual
range, even without a pivot.  Transparent pulls preserve rather than repair
this deficit.  An all-`m` proof must use a nonlexical upper-covering factor,
a preliminary nontransparent repair/absorber, or a broader packet family.

## 8. Scope

Proved here:

* exact turn-table equivalence for the owner/lower cycle-cover row;
* the uniform fractional upper-cover state and exact hole/repeat identity;
* protected upper-task preservation under a strict transparent pull tree;
* the sharp redundant-provider count `C-b+1` and safe rooted opening;
* the corrected endpoint aperture and path-support Rado implication; and
* the quantitative private-absorber lemma.

Not proved:

* `PUTP(m,d)` for all sufficiently large `m`;
* a protected upper-covering factor or a Boolean private absorber bank;
* a disjoint strict transparent ECO pull tree for that factor;
* any source/address, residence, deeper-shadow, compiler, or regeneration
  row; or
* `PCS`, `B+1`, or an all-`k` bound.

No finite search was used.
