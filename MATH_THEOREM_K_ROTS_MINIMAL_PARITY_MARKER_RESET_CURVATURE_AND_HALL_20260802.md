# Minimal ROTS parity marker, reset curvature, and rooted Hall

**Date:** 2026-08-02  
**Status:** exact local theorem and sharp abstract obstruction.  This note
does not prove that the K17, K19, or K21 literal catalogues contain the
required bridge.  It does not prove normality of the remaining common
selector, chronology connectivity, residence, upper decks, common-cap, a
compiler, or a word.

## 0. Result

The determinant-two common-selector face carries one missing affine parity
bit.  Its smallest algebraic repair is one odd physical configuration.
Equivalently, an optional absorber uses one binary off/on marker ticket.
Tags, duplicated states, and arbitrarily many private forced columns do not
repair the face unless some selected column changes the physical parity
footprint.

For ROTS this algebraic repair is not enough.  A one-ticket repair is
physical precisely when the odd bridge and its complementary even row:

1. are literal completed configurations and are resource-disjoint;
2. have the required reset-threshold total; and
3. form a protected partial matching satisfying every residual rooted Hall
   cut.

When the odd bridge preserves the reset type of the even configuration it
replaces, one-ticket reset transparency is equivalent to vanishing of one
explicit `2 x 2` reset curvature.  Nonzero curvature cannot be removed by
one such ticket; two parity cells with opposite diagonal choices cancel it.

Finally, disjoint sums of parity cells have independent `Z/2` classes.
Thus the existence of one determinant-two minor does not imply an `O(1)`
marker theorem.  A global result must bound the two-primary cokernel rank or
construct a correlated ticket whose physical support clears the required
classes.

## 1. The local parity face

Let

\[
 A=\{a_0,a_1\},\qquad B=\{b_0,b_1\},\qquad C=\{c_0,c_1\},
\]

and let the four available configurations be

\[
 e_{ij}=\{a_i,b_j,c_{i\oplus j}\},\qquad i,j\in\{0,1\}.       \tag{1.1}
\]

Thus the available triples are `000,011,101,110`.  Let

\[
                         u={\bf1}_{A\dot\cup B\dot\cup C}.     \tag{1.2}
\]

Weighting every `e_ij` by `1/2` gives `u`, but no integral exact cover does.
Indeed exact coverage of `A` and `B` leaves only

\[
 \{e_{00},e_{11}\}\quad\hbox{or}\quad
 \{e_{01},e_{10}\},                                        \tag{1.3}
\]

and the first pair repeats `c_0`, while the second repeats `c_1`.

Define the odd twin

\[
 o_{ij}=\{a_i,b_j,c_{1\oplus i\oplus j}\}.                   \tag{1.4}
\]

Write `bar i=1-i`, `bar j=1-j`.

### Theorem 1.1 (one odd bridge is necessary and sufficient)

For every `i,j`,

\[
                     o_{ij}\mathbin{\dot\cup}e_{\bar i\bar j}=u. \tag{1.5}
\]

Consequently one odd bridge makes the local one-copy selector integral.
Conversely, every exact two-column cover of the six resources contains one
odd configuration.  Hence no extension whose every nonprivate column still
projects to one of the four even configurations can repair the face.

#### Proof

The `A` and `B` entries of `e_(bar i,bar j)` complement those of `o_ij`.
Its `C` entry is

\[
 (1-i)\oplus(1-j)=i\oplus j,
\]

which complements the `C` entry of `o_ij`.  This proves (1.5).

Conversely, two columns covering `A` and `B` once must be bitwise
complementary on their first two coordinates.  If both have even total
parity, their third coordinates agree, so they do not cover `C` once.
Thus one selected column has odd parity.  Projecting any allegedly exact
tagged cover to its physical `A,B,C` footprint would give an exact cover by
even columns, which is impossible. \(\square\)

The class `[u]` is the nonzero element of the local `Z/2` Smith quotient.
Equation (1.5) says that the class of every odd bridge is `[u]`, because
`u-o_ij=e_(bar i,bar j)` lies in the even-column lattice.

### Corollary 1.2 (smallest optional marker ticket)

Add one private marker resource `m`.  Give one ticket the two modes

\[
                         t_{\rm off}=\{m\},\qquad
 t_{\rm on}=\{m\}\mathbin{\dot\cup}o_{ij}.                    \tag{1.6}
\]

The off mode together with weight `1/2` on every even column is the old
fractional state.  The on mode together with `e_(bar i,bar j)` is an exact
integral cover.  Thus an optional local absorber needs exactly one binary
marker bit, or two modes.  A forced odd bridge needs no separate marker row;
the two-mode formulation only records the ability to leave the absorber
inactive.

A one-state private dummy, or any direct sum of private forced columns,
cannot help: after deleting the private rows and projecting the selected
columns, Theorem 1.1 gives the same contradiction.

## 2. The exact reset-curvature condition

Let

\[
             \lambda(q)\in\mathbb Z^3                           \tag{2.1}
\]

be the three-threshold reset signature of a completed configuration `q`.
The theorem also applies if further additive boundary ledgers are appended
to `lambda`.  The fractional even face carries signature

\[
                \bar\lambda={1\over2}
                 \sum_{p,q\in\{0,1\}}\lambda(e_{pq}).          \tag{2.2}
\]

For an odd bridge define its boundary defect

\[
 \Delta_{ij}=\lambda(o_{ij})+\lambda(e_{\bar i\bar j})
                            -\bar\lambda.                       \tag{2.3}
\]

### Theorem 2.1 (one-ticket reset transparency)

Among repairs using one odd bridge, the common selector is integral and
the old reset ledger is unchanged if and only if

\[
                             \boxed{\Delta_{ij}=0}.             \tag{2.4}
\]

#### Proof

Theorem 1.1 proves exact physical coverage.  The selected integral pair has
reset signature `lambda(o_ij)+lambda(e_(bar i,bar j))`; the old fractional
face has signature (2.2).  Equality is exactly (2.4). \(\square\)

The most useful special case is a **vertical parity bridge**: changing the
parity role does not change the address/reset type,

\[
                         \lambda(o_{ij})=\lambda(e_{ij}).       \tag{2.5}
\]

Put

\[
 \kappa=\lambda(e_{00})+\lambda(e_{11})
             -\lambda(e_{01})-\lambda(e_{10}).                 \tag{2.6}
\]

### Corollary 2.2 (rectangle curvature)

Under (2.5), a diagonal bridge `o_00` or `o_11` has defect `kappa/2`, and
an off-diagonal bridge `o_01` or `o_10` has defect `-kappa/2`.  Therefore a
single vertical bridge preserves the old reset ledger if and only if

\[
                              \boxed{\kappa=0}.                 \tag{2.7}
\]

If `kappa` is nonzero, two parity cells with the same curvature and with
both diagonal classes (diagonal and off-diagonal) physically available have
a reset-transparent two-ticket absorber: use a diagonal bridge in one cell
and an off-diagonal bridge in the other.  Their defects cancel.  A single
cell cannot do so.

#### Proof

Substitute (2.5) in (2.3).  The two diagonal choices give

\[
 \lambda(e_{00})+\lambda(e_{11})-\bar\lambda=\kappa/2,
\]

and the two off-diagonal choices give `-kappa/2`.  The remaining assertions
follow immediately. \(\square\)

For four flags at depth three there are ten downward/neutral endpoint types
`(alpha,beta)` with `0<=beta<=alpha<=3`.  Thus a canonical bounded typed
interface retaining both parity and literal reset endpoints is

\[
       (\hbox{parity bit},\hbox{reset endpoint type})
          \in\mathbb Z/2\times\mathcal I_3,\qquad
                        |\mathcal I_3|=10,                      \tag{2.8}
\]

at most twenty states before literal guards are imposed.  A true one-ticket
vertical bridge is an edge between the two parity states over one fixed
member of `I_3`.  Merely attaching the bit as a label creates no such edge.

If the chronology is allowed to change its reset ledger, `Delta_ij=0` is a
sufficient transparency condition rather than a necessary condition for
global feasibility.  In that case the new integer demand must be sent
through the exact interval-transport flow; scalar equality alone is not a
replacement for that flow.

## 3. Rooted Hall is an independent literal condition

Let `G=(L,R;E)` be the rooted residual successor graph before fixing the
bridge pair, with

\[
                         \sigma(X)=|N(X)|-|X|.                  \tag{3.1}
\]

Suppose the literal odd bridge and its complementary even configuration
induce a two-edge partial matching `P`.  Put

\[
 p_P(X)=|V_L(P)\cap X|,
 \qquad q_P(N(X))=|V_R(P)\cap N(X)|.                           \tag{3.2}
\]

### Theorem 3.1 (exact protected bridge criterion)

The bridge pair extends to a matching saturating the residual left shore if
and only if

\[
             \boxed{q_P(N(X))-p_P(X)\le\sigma(X)
                     \quad\hbox{for every }X\subseteq L.}      \tag{3.3}
\]

#### Proof

After selecting `P`, Hall's condition in the residual graph is

\[
 |N(X)\setminus V_R(P)|\ge |X\setminus V_L(P)|.
\]

Expanding both sides gives (3.3). \(\square\)

Thus exact `A/B/C` coverage and zero reset curvature do not imply rooted
extendability.  On every tight old cut, (3.3) requires zero protected cut
charge.  A sufficient stronger certificate is that the two bridge edges
belong to one known left-saturating matching.  More generally, the exact
cut test (3.3), or a literal reserve absorber, is load-bearing.

### Theorem 3.2 (minimal physical ROTS marker)

A one-ticket repair of the isolated parity face which preserves a fixed
reset flow and rooted extension exists if and only if some odd bridge
`o_ij` satisfies all of the following:

1. `o_ij` and `e_(bar i,bar j)` are legal completed literal configurations;
2. their nonprivate physical resources are disjoint and cover the six local
   resources once;
3. `Delta_ij=0`; and
4. their rooted edge pair is a partial matching satisfying (3.3).

Under these conditions replacing the half-integral parity face by the pair
in (1.5) leaves every other demand unchanged.  Conversely every one-bridge
repair has this form and must satisfy conditions 1--4.

#### Proof

Sufficiency combines Theorems 1.1, 2.1, and 3.1.  For necessity, exact
coverage forces the complementary pair by the proof of Theorem 1.1;
preservation of the reset ledger forces (2.4), and rooted extension forces
(3.3). \(\square\)

Condition 1 is the distinction between a physical marker and an abstract
parity tag.  A state label which has no completed odd configuration in the
literal catalogue fails before reset or Hall is tested.

## 4. Why `O(1)` markers do not follow from determinant two

Take the direct sum of `t` disjoint copies of the even parity face.  Its
two-primary lattice quotient contains

\[
                            (\mathbb Z/2)^t.                    \tag{4.1}
\]

The unit demand has nonzero coordinate in every factor.

### Theorem 4.1 (marker-rank and bounded-support lower bounds)

1. A bank of `b` binary marker tickets has residue span of dimension at
   most `b`.  To clear every class in (4.1), necessarily `b>=t`.
2. Even for the fixed all-nonzero unit class, if every ticket mode changes
   at most `h` parity factors, then at least
   
   \[
                                \left\lceil t/h\right\rceil     \tag{4.2}
   \]
   
   activated tickets are necessary.
3. Private forced columns and marker refinements which project to even
   columns have zero residue and cannot improve either bound.

#### Proof

The direct-sum quotient is the direct sum of the `t` local `Z/2` quotients.
Each binary ticket contributes one residue vector, so `b` vectors span a
space of dimension at most `b`.  This proves item 1.  For item 2, the union
of the supports of fewer than `ceil(t/h)` activated residues omits some
coordinate of the unit class.  Item 3 follows by projection to each even
face. \(\square\)

Therefore a bounded-marker all-`k` theorem needs at least one of the
following genuinely global facts:

* the two-primary cokernel rank of the protected common selector is bounded;
* all local parity minors represent one bounded family of homologous global
  classes; or
* a correlated literal ticket of nonlocal support clears the required class
  while remaining reset- and Hall-safe.

The presence of one determinant-two minor proves none of these statements.

## 5. Exact conditional global lemma

Let `A_P` be the protected residual completed-configuration matrix after a
ROTS chronology and reset bank have been fixed.  Suppose:

1. the relevant torsion quotient is an elementary group
   `(Z/2)^s` with `s=O(1)` (or the unit-demand class lies in such a direct
   summand);
2. there are `s` pairwise compatible literal marker tickets whose odd modes
   form a residue basis;
3. one common choice of their modes is reset-transparent, either ticketwise
   by Theorem 2.1 or as a zero-sum bank by Corollary 2.2;
4. the same chosen literal bank satisfies the rooted cut inequalities
   (3.3); and
5. after its lattice class is cleared, the residual matrix is normal at the
   unit demand, or a protected resource-zero circuit theorem rounds that
   unit fibre.

### Theorem 5.1 (bounded-marker ROTS rounding)

Under assumptions 1--5, the common literal selector has an integral
one-copy completion preserving the fixed reset flow and rooted Hall.  The
exported torsion state has `s` bits, hence at most `2^s` mode combinations.

#### Proof

Choose ticket modes which clear the cokernel class.  Assumptions 3 and 4
retain the reset and rooted faces.  Assumption 5 converts cone-plus-lattice
membership into a nonnegative integral representation.  Since the residual
demand is zero-one, the representation is a literal exact cover. \(\square\)

For the isolated determinant-two face, `s=1` and Theorem 1.1 supplies the
integral representation explicitly; no extra normality hypothesis is
needed.  For the full ROTS master, determinant two establishes only
`s>=1`.  Bounded `s`, physical odd-ticket supply, and the final unit-fibre
rounding remain separate lemmas.

## 6. Scope for `1S-ROTS(17)`

The theorem gives an exact diagnostic for the joint master.

* A common short state is useful as a parity marker only if its completed
  long--short--long configuration is an odd bridge in the physical
  three-resource incidence, not merely a new address label.
* Its reset endpoint type is one of the ten types in (2.8); a vertical bridge
  retains the same type, while a nonvertical bridge must be charged through
  the interval flow.
* Its two rooted incidences must pass (3.3) in the same recoupled table.
* One such bridge closes one isolated `Z/2` class.  It does not prove that
  the full K17 common-selector cokernel has rank one or that its unit fibre
  is normal.

Accordingly the exact finite census should report, for every common-state
socket record, its physical parity residue, reset endpoint type, and rooted
cut/DM eligibility.  Counting all three projections separately is
insufficient.
