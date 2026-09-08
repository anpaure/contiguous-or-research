# Strict Macaulay jumps: exact two-run shielding and protected current

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It identifies the
union of two consecutive constant-aperture Macaulay runs across a strict
aperture jump as one gated two-stage DNF.  The owner fibres and Ore slack
are exact, and the protected loss collapses to four path-boundary currents.
When the upper gate fires, every deletion in the lower run's additional
root is shielded automatically.  The theorem does not yet prove all such
two-run unions safe or compose arbitrarily many strict jumps.

No computation, search, or solver result is used.

## 0. A general gated two-run family

Put

\[
 n=2m-1,
 \qquad \mathcal L=\binom{[n]}{m-1}.
\]

Choose pairwise disjoint sets

\[
 R,G,X,Y\subseteq[n],
\]

and assume

\[
 |R|+|G|+1\le m-2.
\tag{0.1}
\]

Define the upper and lower run DNFs

\[
 \mathcal D_0=\{L\in\mathcal L:R\subseteq L, L\cap Y\ne\varnothing\},
\tag{0.2}
\]

and

\[
 \mathcal D_1
 =\{L\in\mathcal L:R\cup G\subseteq L,
                       \ L\cap X\ne\varnothing\}.
\tag{0.3}
\]

Their union is the gated family

\[
 \boxed{
 \mathcal D
 =\{L:R\subseteq L,
       (L\cap Y\ne\varnothing)
       \ \text{or}\
       (G\subseteq L\ \text{and}\ L\cap X\ne\varnothing)\}.}
\tag{0.4}
\]

## 1. Exact owner fibres

For an owner `U`, put

\[
 y_U=|U\cap Y|,
 \qquad x_U=|U\cap X|,
\]

and let

\[
 e_U=\mathbf1_{\{R\cup G\subseteq U,\ x_U\ge1\}}.
\]

### Theorem 1.1 (gated active-core intersection)

An owner is active exactly when `R subset U` and either `y_U>=1` or
`e_U=1`.  Its active-core intersection `J_U` is

\[
 \boxed{
 J_U=
 \begin{cases}
  R\cup\{y\},&y_U=1,\ e_U=0,\\
  R,&y_U\ge2,\ e_U=0,\\
  R\cup G\cup\{x\},&y_U=0,\ e_U=1,\ x_U=1,\\
  R\cup G,&y_U=0,\ e_U=1,\ x_U\ge2,\\
  R,&y_U\ge1,\ e_U=1.
 \end{cases}}
\tag{1.1}
\]

Here `x` and `y` denote the unique hit in the corresponding row.  The
selected-facet multiplicity is

\[
 \boxed{a_U=m-|J_U|.}
\tag{1.2}
\]

Every nonzero fibre has size at least two under (0.1).

#### Proof

The active upper clauses are `R+y` for `y in U cap Y`; their intersection
is `R+y` at a unique hit and `R` at a multiple hit.  The active lower
clauses are `R union G+x` for `x in U cap X`; their intersection is
`R union G+x` at a unique hit and `R union G` at a multiple hit.  If both
groups are active, an upper core omits `G union X`, while a lower core
omits `Y`; their total intersection is exactly `R`.  This proves (1.1).
For a monotone DNF, accepted deletions are `U-J_U`, giving (1.2).
Condition (0.1) makes even the largest active core have size at most
`m-2`. \(\square\)

The last row is the shielding law: once the upper run is active, all of
the additional lower root `G` disappears from the common active core.

## 2. Exact scalar slack

For a base set `B` and a disjoint hit set `Z`, define

\[
 \Phi_q(B;Z)
 =\binom{n-|B|}{q-|B|}
  -\binom{n-|B|-|Z|}{q-|B|}.
\tag{2.1}
\]

For pairwise disjoint `B,X,Y`, define

\[
\begin{aligned}
 \Phi_q^{(2)}(B;X,Y)
 ={}&\binom{n-|B|}{q-|B|}
 -\binom{n-|B|-|X|}{q-|B|}\\
 &-\binom{n-|B|-|Y|}{q-|B|}
 +\binom{n-|B|-|X|-|Y|}{q-|B|}.
\end{aligned}
\tag{2.2}
\]

Use the convention that an inadmissible binomial coefficient is zero, and
put

\[
 \Delta(B;Z)=\Phi_m(B;Z)-\Phi_{m-1}(B;Z),
\tag{2.3}
\]

\[
 \Delta^{(2)}(B;X,Y)
 =\Phi_m^{(2)}(B;X,Y)-\Phi_{m-1}^{(2)}(B;X,Y).
\tag{2.4}
\]

### Theorem 2.1 (two-run inclusion--exclusion)

The exact truncated-shadow slack is

\[
 \boxed{
 {\sigma(\mathcal D)\over2}
 =\Delta(R;Y)+\Delta(R\cup G;X)
  -\Delta^{(2)}(R\cup G;X,Y).}
\tag{2.5}
\]

#### Proof

Every active owner fibre has size at least two, so

\[
 {\sigma(\mathcal D)\over2}=|N(\mathcal D)|-|\mathcal D|.
\]

The two individual DNF counts are `Phi_q(R;Y)` and
`Phi_q(R union G;X)`.  Their intersection consists of the `q`-sets
containing `R union G` and hitting both `X` and `Y`, whose count is
`Phi_q^(2)(R union G;X,Y)`.  Inclusion--exclusion at ranks `m` and `m-1`
proves (2.5). \(\square\)

## 3. Exact four-current protected loss

For a protected incidence `UL`, write `del(U,L)` for the unique coordinate
in `U-L`.  Define:

* `xi_R`: active-owner incidences with deletion in `R`;
* `eta_Y`: upper-only unique-hit incidences deleting that unique point of
  `Y`;
* `xi_G`: lower-only incidences with deletion in `G`; and
* `eta_X`: lower-only unique-hit incidences deleting that unique point of
  `X`.

### Theorem 3.1 (strict-jump shielding current)

For every protected bank of maximum degree at most two,

\[
 \boxed{
 \lambda_P(\mathcal D)
 =\xi_R+\eta_Y+\xi_G+\eta_X.}
\tag{3.1}
\]

In particular, no deletion in `G`, `X`, or `Y` is charged at an owner where
both run gates are active.

#### Proof

All active fibres have size at least two, so protected loss consists of
protected deletions in `J_U`.  Read the five disjoint rows of (1.1): `R`
is always charged; `Y` is charged only at an upper-only unique hit; `G` is
charged only when the lower gate is active alone; and `X` is then charged
only at a unique hit.  This is exactly (3.1). \(\square\)

Now assume `P` is a union of resident simple owner paths, and let
`mathscr P(B)` denote the paths containing an owner above `B`.

### Corollary 3.2 (four boundary bounds)

\[
 \boxed{
 \xi_R\le2|\mathscr P(R)|,
 \qquad
 \eta_Y\le2|Y|\,|\mathscr P(R)|,}
\tag{3.2}
\]

and

\[
 \boxed{
 \xi_G\le2|\mathscr P(R\cup G)|,
 \qquad
 \eta_X\le2|X|\,|\mathscr P(R\cup G)|.}
\tag{3.3}
\]

Consequently

\[
 \boxed{
 \lambda_P(\mathcal D)
 \le2(|Y|+1)|\mathscr P(R)|
    +2(|X|+1)|\mathscr P(R\cup G)|.}
\tag{3.4}
\]

#### Proof

On one path, the owners containing a fixed base form one interval; an
incidence deleting a base coordinate lies on one of its two boundary
edges.  Each individual hit coordinate also has one occurrence interval
and at most two boundary incidences deleting it.  The upper-only and
lower-only restrictions can only remove contributions.  Summing proves
(3.2)--(3.4). \(\square\)

## 4. Exact realization of a strict Macaulay jump

Take two consecutive maximal constant-aperture runs.  Let the lower-index
run occupy `a,...,b` with aperture `rho_-`, and the upper-index run occupy
`b+1,...,c` with aperture

\[
 \rho_+>\rho_-.
\]

Let `R_- ,X` and `R_+,Y` be their respective common roots and pivot sets
from the common-root run theorem.

### Theorem 4.1 (jump-root relation)

There is a coordinate interval `G`, disjoint from `R_+,X,Y`, such that

\[
 \boxed{
 R_-=R_+\mathbin{\dot\cup}G,
 \qquad |G|=\rho_+-\rho_-.}
\tag{4.1}
\]

Hence the union of the two run DNFs is exactly the gated family (0.4)
with `R=R_+`.

#### Proof

On the lower run, the final pivot is `p_b=rho_-+b`.  On the upper run, the
first pivot is `p_(b+1)=rho_++b+1`.  Comparing the two root formulas shows
that the lower root retains exactly the intervening coordinates

\[
 G=\{\rho_-+b+1,\ldots,\rho_++b\},
\]

in addition to the upper root.  This interval has size
`rho_+-rho_-` and is disjoint from both pivot sets.  The clause identities
then give the gated union directly. \(\square\)

Thus a strict aperture jump does not create an arbitrary cross-run
interaction.  It creates one lower gate `G`; whenever the upper run is
active, that entire gate is shielded from the protected loss.

## 5. Exact frontier

The theorem replaces strict-jump gluing by one explicit two-run object:

\[
 \text{root current}
 +\text{upper unique-hit current}
 +\text{unshielded gate current}
 +\text{lower unique-hit current}.
\]

It does not prove that the scalar expression (2.5) pays these four currents
for every parameter choice.  It also does not yet compose three or more
strict jumps; in that setting successive upper gates can shield multiple
lower roots, and that cancellation must be tracked jointly.

## 6. Dependencies

| role | file | SHA-256 |
|---|---|---|
| Macaulay interval/DNF erosion theorem | `MATH_THEOREM_MACAULAY_INTERVAL_DNF_EROSION_AND_TRIANGULAR_CROSSING_20260804.md` | `c2b7156bb810306738086392238c5fb047b083b4885083a93827bb6ef16df23c` |
| common-root run theorem | `MATH_THEOREM_COMMON_ROOT_MACAULAY_RUN_EXACT_CURRENT_20260804.md` | `00bd9db3dbfd987c039af4bf796a43b7a4598388a5e8f91a88fde34e6b353bb1` |
