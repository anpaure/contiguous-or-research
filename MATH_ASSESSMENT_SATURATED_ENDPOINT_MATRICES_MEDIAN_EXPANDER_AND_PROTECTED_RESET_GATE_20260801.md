# Saturated endpoint matrices and median-expander fusion at the protected reset gate

Date: 2026-08-01

Status: exact applicability assessment and conditional synthesis theorem.
This note does not import an external construction of the required Boolean
matrices or expanders.  It identifies precisely what the two techniques
would close if their hypotheses were realized by literal turn atoms, and
why their abstract forms do not by themselves close the protected-host or
rolling-reset three-return gates.

## 0. Verdict

Two techniques are potentially complementary.

1. A saturated endpoint matrix with two-sided coordinate coverage and
   separated palettes can provide **universal typed chronology returns**, if
   its entries are complete occurrence-labelled tail--head--owner paths.
2. A median split followed by a robust Hall matching can fuse a family of
   path components by a factor of two per round, if every matched edge is a
   literal transparent connector and the same port invariant regenerates
   after contraction.

Together they give a clean sufficient theorem for the topological part of a
protected host.  They do **not** automatically give either

* simultaneous compiler safety of the three returns, or
* one common exterior for the two reset phases.

The first failure already occurs in the strict-gammoid circuit

\[
                             U_{2,3},                         \tag{0.1}
\]

even when all endpoint and chronology palettes are completely separated.
The second has the three-label Borromean contraction obstruction.  Thus the
external techniques strengthen the gate only after private compiler sinks
and phase-paired contraction are included in every matrix entry.

There is also a scope restriction on the expander.  A fixed root-local
Cartesian circuit host cannot have growing portal degree: the affine
weight-two theorem gives degree and edge-connectivity at most three.  The
expander/matching must therefore be a **prospectively selected residual
free-port graph**, not a static family of simultaneously toggleable root
circuits.

## 1. Literal typed endpoint matrices

Let the three return types be

\[
                         \mathsf A,\mathsf P_0,\mathsf P_1.   \tag{1.1}
\]

For type `i`, let `S_i` and `T_i` be its possible source and sink endpoint
states.  A matrix entry

\[
                         e\in\mathcal R_i(s,t)                \tag{1.2}
\]

must mean a complete literal return path, not merely a path in one
projection.  In particular it records compatible tail, head and owner
turns, every palette/provider ticket, its phase data, and its compiler
hazard set `D(e)`.

Call the three matrices **resource separated** when there are disjoint
resource grounds `E_i` and every member of `R_i` uses only `E_i`, apart from
its prescribed endpoint.  Within one matrix, selections made at distinct
rows and columns must also have disjoint internal resources; a mere
set-theoretic row/column cover does not imply this.

The following distinction is essential.

* Two-sided coordinate cover means every row and every column has at least
  one available entry.
* Universal endpoint compatibility means

  \[
                 \mathcal R_i(s,t)\ne\varnothing
                 \qquad((s,t)\in S_i\times T_i).             \tag{1.3}
  \]

The first condition does not imply the second.  If a saturated-matrix
theorem supplies (1.3), separated palettes make the three chronology
choices independent.  If it supplies only nonempty row and column margins,
a prescribed reset endpoint pair can still be a structural zero.

## 2. Endpoint separation does not imply compiler separation

Suppose (1.3) holds for all three types and their chronology resources are
disjoint.  Choose one entry of each type, with distinct compiler hazard
cells

\[
                              c_{\mathsf A},c_0,c_1.          \tag{2.1}
\]

Let one compiler target be adjacent to precisely these three cells.  Its
transversal matroid is `U_(1,3)`, so the safe-deletion dual is `U_(2,3)`.
Every one- or two-return subfamily is safe, while the triple is not.

Thus even a complete endpoint matrix with fully separated chronology
palettes does not imply a protected three-return lift.  The missing row is

\[
 D(e_{\mathsf A})\cup D(e_0)\cup D(e_1)
                         \in I(M_\theta^*),                   \tag{2.2}
\]

in one fixed compiler cap.

Likewise, separate forward- and reverse-phase endpoint matrices do not
produce one common exterior.  After the phase banks are contracted, the
residual upper/task matroids may have incompatible parallel pairs; the
three-label Borromean example shows that both phasewise Rado systems can
pass while their common task transversal is empty.

### Theorem 2.1 (separated-corridor three-return lemma)

Assume for each type `i` that:

1. every prescribed endpoint pair has a nonempty literal matrix cell
   `R_i(s_i,t_i)`;
2. the three matrices use disjoint chronology resource palettes;
3. their compiler hazards lie in a direct sum

   \[
                  K_{\mathsf A}\oplus K_0\oplus K_1
                     \subseteq M_\theta^*,                   \tag{2.3}
   \]

   and every candidate hazard set is independent in its summand; and
4. every entry is bi-contractible: its two phase banks leave the same
   represented residual exterior at both host stages.

Then every prescribed reset endpoint triple has a compatible protected
three-return lift.

#### Proof

Choose one nonempty matrix entry for each type.  Resource separation makes
their chronology paths mutually disjoint and their literal turn records
make the three projections consistent.  Direct-sum independence in (2.3)
gives (2.2).  Bi-contraction identifies the two residual phase exteriors,
so the fixed-cap and phase-paired Rado interfaces survive. \(\square\)

This is a genuine positive use of the saturated/separated-palette method.
Its extra hypotheses are exactly the rows absent from an ordinary
coordinate-cover matrix.

## 3. Median-halving component fusion

Let `C` be a family of directed path components.  Each component has a free
left port and a free right port, in addition to any protected reset ports.
Split the components into two classes `L,R` with

\[
              |L|=\lfloor|\mathcal C|/2\rfloor,
              \qquad |R|=\lceil|\mathcal C|/2\rceil.         \tag{3.1}
\]

The split may be chosen by a median of any scalar component weight.  Let
`G_C` be the bipartite graph whose edge `CD`, with `C in L,D in R`, is a
literal connector from the right port of `C` to the left port of `D`.

### Theorem 3.1 (protected median-halving lemma)

Suppose at every stage:

1. after deleting every protected port, `G_C` satisfies

   \[
                         |N(X)|\ge|X|\qquad(X\subseteq L);    \tag{3.2}
   \]
2. connectors selected on a matching have disjoint physical resources and
   preserve the declared owner, palette, residence, upper and compiler
   payloads;
3. a connector concatenates its two directed paths and leaves their two
   outer ports as a new legal component state; and
4. the same hypotheses regenerate for the contracted component family.

Then all components can be fused into one directed path by at most
`ceil(log_2 |C|)` matching rounds.

#### Proof

Hall's theorem applied to (3.2) gives a matching saturating `L`.  Every
matched edge joins two different paths and the matching has no shared
endpoint, so all joins may be installed simultaneously and produce

\[
                    |\mathcal C'|
                    =|\mathcal C|-|L|
                    =\lceil|\mathcal C|/2\rceil              \tag{3.3}
\]

new path components.  Their outer endpoints give the regenerated ports.
Iterate (3.3). \(\square\)

An expander estimate is useful only as a sufficient way to prove the robust
Hall row (3.2).  For example, if at most `p` sink ports are protected, the
surplus condition

\[
                         |N(X)|\ge|X|+p                       \tag{3.4}
\]

before protection implies (3.2) afterward.  Median normalization balances
the two shores; it does not prove (3.2), literal connector safety, or the
regeneration row.

The union of the round matchings is not an arbitrary connector tree.  The
induction keeps every component a path, so every original component uses at
most its two exposed outer ports.  This is the useful topological advantage
of median halving.

## 4. Why the expander must be prospective

Theorem 3.1 cannot be instantiated by one fixed root-local factor together
with a Cartesian family of `C6/C10` toggles.  At one raw SCD root, every
local two-factor state is a weight-two vector.  Hereditary legality of all
star subsets makes these states an affine constant-weight-two space, which
has at most four members.  After the base state, at most three nontrivial
portal states remain.

Consequently the static root-faithful portal graph has

\[
                         \Delta\le3,\qquad\lambda\le3.        \tag{4.1}
\]

It cannot be the growing robust expander imagined in the median-fusion
argument.

The live interpretation is instead:

1. choose the owner/upper forest prospectively;
2. expose alternative free-port connector columns;
3. select only one matching of those alternatives in the current round;
4. contract the matched paths and rebuild the next residual graph.

No claim is made that all alternative edges can be toggled together.

## 5. Combined protected-host lemma

The two techniques combine in the following exact sufficient statement.

> **Separated-palette protected reset-host lemma.**  A prospectively chosen
> two-phase host has four disjoint resource palettes: three return palettes
> for `A,P0,P1` and one fusion palette.  The return palettes satisfy
> Theorem 2.1, including private/direct-sum compiler sinks and
> bi-contraction.  After contracting the chosen return triple, the fusion
> palette satisfies Theorem 3.1 at every median-halving stage.  Every atom is
> a full literal turn path and is transparent to the declared upper,
> residence and compiler payloads.

Under these hypotheses one first reserves the three returns, then repeatedly
applies the median-halving matching.  The final result is one protected path
host containing a switch-ready rolling reset and one common exterior for
both phases.

The proof is just Theorems 2.1 and 3.1, with palette separation ensuring
that the two selections commute.

## 6. Exact assessment

The saturated-matrix technique can materially strengthen the **endpoint
chronology** row if it yields universal cells of full literal paths and not
only row/column marginals.  The expander-matching technique can materially
strengthen **component fusion** if applied to the prospective residual
free-port graph; median halving then gives a particularly clean regenerating
path invariant.

Neither technique alone proves the current gate.  The remaining Boolean
content is precisely to construct entries which simultaneously carry

* a full tail--head--owner lift;
* phase-paired residual minors;
* direct-sum/private compiler relocation sinks;
* protected upper and residence tickets; and
* a residual free-port Hall surplus that regenerates after contraction.

Accordingly, the best concrete target imported from the two techniques is
the Separated-palette protected reset-host lemma above.  It is strictly
stronger than ordinary endpoint cover and strictly weaker than asking for a
static Cartesian connector expander, which is impossible by (4.1).
