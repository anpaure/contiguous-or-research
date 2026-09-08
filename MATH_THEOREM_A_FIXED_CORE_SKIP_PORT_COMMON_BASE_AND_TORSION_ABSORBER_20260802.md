# Fixed-core skip-port common bases, torsion tickets, and protected circuit rounding

**Date:** 2026-08-02  
**Lane:** A, integral fixed-core chain/state rounding  
**Status:** exact reformulation and conditional rounding theorem.  The
Boolean ticket/circuit supply asserted in the hypotheses is not proved here.
No residence, upper-shadow, connected-topology, source, cap, compiler, or
word claim is made.

## 0. Outcome

The decorated-row/transition master has an exact nonnegative
set-partitioning lift.  This makes the remaining integral issue precise.
After a protected reset plan is fixed, literal fractional feasibility says
that one unit demand is in a rational cone; an orbit quotient certifies the
same fact only when the residual bank retains the quotient symmetry.  A
one-copy factor says that the same demand is in the corresponding affine
semigroup.  Between those two statements lie two genuinely different gates:

1. a **lattice/torsion gate**; and
2. a **unit-normality**, or nonnegative semigroup-hole, gate.

The orbit-symmetric `2x2x2` parity tensor fails the first gate with exact
index two.  Taking its direct sum with any number of private forced dummy
blocks proves abstractly that scalar reserve counts cannot imply an integral
lift.  This direct sum is not asserted to be a literal four-flag reset-bank
embedding.

There are three proof-safe positive routes.

* After its free-span equations are met, a protected ticket bank containing
  independent generators can clear every finite lattice class.  If the
  relevant torsion cokernel is
  `Z/d_1 + ... + Z/d_s`, then `sum_i(d_i-1)` independent binary tickets in
  generator classes suffice for the lattice row.
* After the tickets are fixed, unit-normality of the residual skip-port
  matrix is sufficient.  Total unimodularity, a genuine two-matroid
  common-base representation with network-integral fibres, and a
  payload-transparent rectangular flow are checkable stronger hypotheses.
* Alternatively, literal resource-zero circuits may be used serially.  A
  circuit which stays inside the protected reset face and raises the exact
  transition-matching rank by one gives a finite descent theorem.  An
  elementary load inequality turns a large Boolean circuit bank into a
  protected circuit.

Thus the weakest useful all-k target is not “the orbit LP rounds.”  It is:

> clear the literal cokernel by protected short-reset tickets, then prove
> unit-normality or a DM-augmenting literal circuit supply on the resulting
> fixed-core face.

This composes exactly with `ROTS(k,H)`: ROTS supplies a legal reset plan and
rooted residual Hall; the theorem below supplies the missing joint integral
row.  An orbit-level recoupling identity is not enough unless it has a
literal, resource-disjoint lift.

## 1. The skip-port exact-cover lift

Let `Q` be a finite bank of decorated rows as in
`MATH_THEOREM_A_FIXED_CORE_FLAGGED_CHAIN_STATE_COMMON_BASE_AND_RESET_CUTS_20260802.md`.
For `q in Q`, let

\[
 {cal R}(q)=C(q)\mathbin{\dot\cup}\{T(q)\}             \tag{1.1}
\]

be its named lower targets and owner.  Let `R` be the complete physical
resource shore: every strict-lower target and every owner.  Give every row
two private symbols `q^-` and `q^+`, called its in-port and out-port.  Put

\[
 V={\cal R}\mathbin{\dot\cup}
       \{q^-,q^+:q\in Q\}.                              \tag{1.2}
\]

There are two kinds of zero-one columns on `V`.

* The **skip column**
  \[
                         s_q=\{q^-,q^+\}.              \tag{1.3}
  \]
* For every legal literal transition `p -> q`, the **completed transition
  column**
  \[
              e_{pq}=\{p^+,q^-\}\mathbin{\dot\cup}{\cal R}(q). \tag{1.4}
  \]

Let `A` be their incidence matrix and let `1_V` denote the all-one demand.

### Theorem 1.1 (exact skip-port equivalence)

The binary decorated-row/transition system (1.6) in the fixed-core joint
master is feasible if and only if

\[
                   Az={\bf1}_V,\qquad z\in\{0,1\}^{\cal C}, \tag{1.5}
\]

where `C` is the skip/transition column bank.  Selected transition columns
form exactly the directed cycle cover of the selected decorated rows.

#### Proof

Suppose (1.5) holds.  If `q^-` is covered by `s_q`, then `q^+` is covered by
the same column, so no transition enters or leaves `q`.  Otherwise exactly
one transition enters `q`.  The skip is then unavailable, so exactly one
transition must cover `q^+` and leave `q`.  Thus the non-skipped rows have
indegree and outdegree one.  Their incoming transition columns contain
exactly their bundles `R(q)`.  Exact coverage of the physical resource rows
therefore says that the selected chains partition every lower target and
use every owner once.

Conversely, take any integral solution of the joint master.  Select its
transition columns and select `s_q` for every unused decorated row.  The
balance equations cover every private port once, while target and owner
exactness cover every physical resource once.  This is (1.5).  The
transition support has the same directed components in both descriptions.
\(\square\)

One-cycle topology is not encoded by (1.5); it is the further assertion
that this cycle cover has one component.

A fixed protected reset/macro bank is handled by selecting its completed
columns, deleting their covered resources and forbidden conflicting
columns, and applying Theorem 1.1 to the residual matrix `A_P`.  If reset
blocks are still variable, they must be represented by complete literal
ticket columns; three scalar threshold inequalities are not a substitute
for those literal columns.

## 2. Cone, lattice, and semigroup are three different statements

For an integer zero-one matrix `B`, write

\[
\begin{aligned}
 K(B)&=B\mathbb R_{\ge0}^{E},\\
 \Lambda(B)&=B\mathbb Z^{E},\\
 S(B)&=B\mathbb Z_{\ge0}^{E}.                         \tag{2.1}
\end{aligned}
\]

Let `u` be a zero-one residual demand.

### Theorem 2.1 (exact unit-fibre criterion)

For the residual skip-port matrix `A_P`:

1. fractional completion is equivalent to `u in K(A_P)`;
2. one-copy integral completion is equivalent to `u in S(A_P)`;
3. `u in Lambda(A_P)` is a necessary lattice condition; and
4. if
   \[
        K(A_P)\cap\Lambda(A_P)=S(A_P)                 \tag{2.2}
   \]
   (normality), then fractional completion plus the lattice condition is
   sufficient.

Only normality at the one demand `u`, rather than (2.2) for every demand,
is needed.

#### Proof

The first three assertions are definitions combined with Theorem 1.1.  If
(2.2) holds, membership in the cone and lattice implies membership in the
semigroup.  Finally, any nonnegative integral representation of a zero-one
demand by nonzero zero-one columns automatically has coefficients in
`{0,1}` and pairwise resource-disjoint supports: a coefficient at least two,
or two selected columns sharing a row, would place at least two in that
coordinate of `u`.  Hence the semigroup representation is a literal exact
cover. \(\square\)

If `Lambda(A_P)` is saturated in its real span, then every integral point of
`K(A_P)` automatically passes the lattice row, and normality alone rounds
the orbit point.  The parity tensor below shows that saturation is not
formal.  Even after saturation, unit-normality is a separate nonnegative
condition.

### Corollary 2.2 (checkable integral faces)

Each of the following is sufficient for the conclusion of Theorem 2.1.

1. `A_P` is totally unimodular.
2. The residual feasible set has an exact extended formulation as the
   intersection of two matroid base polytopes, and every integral common
   base lifts through a network-integral, payload-transparent fibre.
3. After one residual owner/chain table is fixed, every literal state menu
   is a payload-transparent tail/head rectangle and the rooted fractional
   balance flow is feasible.

In item 2, the protected reset restrictions must be contractions,
deletions, or direct-sum constraints already belonging to the two matroids.
Adding a third partition/laminar matroid is not covered.

#### Proof

Item 1 is standard integral-flow/polyhedral integrality.  The matroid
intersection polytope in item 2 is integral; the assumed fibre then lifts an
integral common base.  Item 3 is precisely the fixed-unit owner-arc network
construction of the hinge-rectangle coloured-flow theorem. \(\square\)

The residual Johnson triangle and determinant-three minors proved in
`MATH_THEOREM_PROTECTED_RESET_RESIDUAL_TORSION_AND_TU_NOGO_20260801.md`
show that item 1 is not the generic Boolean answer.  The other two items
remain genuine possible structured faces.

### Corollary 2.3 (exact common-table Hoffman cylinder)

Fix one integral residual owner/chain table and a protected rooted bank of
boundary `eta` on a rotor-state vertex set `V_rot`, with
`eta(V_rot)=0`.  Suppose free role `i` has a flag-homogeneous,
payload-transparent Cartesian state menu

\[
                 A_i\times H_i\subseteq V_{\rm rot}\times V_{\rm rot}. \tag{2.3}
\]

Put

\[
 \ell_A(X)=|\{i:A_i\subseteq X\}|,
 \qquad r_H(X)=|\{i:H_i\cap X\ne\varnothing\}|.     \tag{2.4}
\]

Then that table has an integral one-copy state completion if and only if

\[
                \boxed{\ell_A(X)-r_H(X)\le\eta(X)
                       \quad(X\subseteq V_{\rm rot}).} \tag{2.5}
\]

If the rectangle modes have fixed flag/reset types, the rounding preserves
the declared reset ledger.

#### Proof

Possible aggregate tail counts and head counts are integral polymatroid
base polytopes.  The balance equation is `p-q=eta`.  Polymatroid
intersection is nonempty exactly under (2.5), and its integral point
decomposes into one tail and one head choice per role.  Cartesianity pairs
those choices without changing the owner, payload, flag, or reset type.
\(\square\)

This is necessary and sufficient only after one common table and its
rectangles have been chosen.  An orbit average mixing several tables does
not meet the premise.  It is the most concrete current positive route for
ROTS: concentrate the fractional orbit point on one literal table, then
verify (2.5).

### Corollary 2.4 (central complementary bi-packing insertion)

Suppose a pair of literal central interval packings has complementary lower
and upper palettes, and orient its maximum-degree-two union as in
`MATH_THEOREM_CENTRAL_TWO_INTERVAL_BANK_REDUCTION_AND_ENGEL_RANGE_GATE_20260802.md`.
This gives an integral central subtable satisfying the lower and upper
exact rows and the Johnson tail/head capacity rows.  Assume, additionally,
that these oriented roles together with every protected and noncentral role
embed in **one exact residual owner--named-payload table**.  Let `P` be its
fixed rooted bank, put `eta=\partial P` with `eta(V_rot)=0`, and suppose every
free role has a nonempty Cartesian rotor-state menu which is constant on all
four central labels and every guard intended to survive.  If this common
table passes (2.5), it has an integral one-copy rotor-state completion.

If the fixed Johnson tail/head labels are themselves coordinates of the
variable rotor state, their injectivity is not automatic under Corollary
2.3; it must be enforced by singleton menus or by additional matching rows.
If the interval-bank union is acyclic, the static table also satisfies the
central graphic row.  With `c` alternating cycle components, deleting one
edge per cycle gives defect exactly `c` in each outer palette, but the
reduced table, boundary, and Hoffman cuts must then be rebuilt and rechecked.

#### Proof

The two-bank theorem supplies the integral central four-resource subtable.
The extra hypothesis makes it one legal exact table of the kind required by
Corollary 2.3, which rounds its Cartesian rotor-state cylinder without
changing any fixed payload resource.  Acyclicity belongs to the static union
graph.  Deleting one edge from each cycle proves the outer defect count, but
role deletion need not preserve (2.5), which is why the reduced instance is
explicitly retested.
\(\square\)

This is only an insertion interface.  Dong--Mao's proved range does not
contain the central parameters and supplies neither of the two banks.
Moreover the central graphic forest and the later transition-cycle topology
are different rows and must not be conflated.

## 3. Exact torsion-ticket algebra

Let `A_0` be the bulk residual matrix before choosing the modes of
`b_reset` protected reset tickets.  Use the full cokernel

\[
 \overline G={\mathbb Z^V\over\Lambda(A_0)}
       \cong\mathbb Z^f\oplus G_{\rm tor}.           \tag{3.1}
\]

Ticket `j` has a default mode and finitely many alternative complete literal
modes.  After contracting all default modes, let `u` be the bulk demand and
define `g_(j,mu)` so that choosing mode `mu` changes the bulk demand from
`u` to `u-g_(j,mu)`.  Every integer delta has a class in the full quotient
`Gbar`; no individual delta is assumed to lie in the real span of `A_0`.

Here the bulk catalogue `A_0` is required to be the same in every ticket
mode.  If changing a ticket also deletes or creates bulk columns, one must
use the mode-dependent matrix `A_(0,mu)` and the single quotient (3.1) is no
longer an exact test.  Likewise, “independent tickets” below means that their
complete literal supports are pairwise disjoint and all chosen modes are
simultaneously realizable without changing `A_0`.

### Theorem 3.1 (exact ticket congruence)

The ticket modes clear the complete lattice obstruction if and only if one
can choose a **jointly realizable** tuple containing one mode per ticket so
that

\[
             [u]=\sum_{j=1}^{b_{\rm reset}}[g_{j,\mu(j)}]
                     \quad\hbox{in }\overline G.     \tag{3.2}
\]

The free coordinates of (3.2) are exact real-span equations.  After they
have been cleared, suppose the remaining torsion group is

\[
                 G_{\rm tor}\cong
                    \bigoplus_{i=1}^s\mathbb Z/d_i\mathbb Z, \tag{3.3}
\]

and the bank contains `d_i-1` independent binary tickets with alternatives
of residue `0` and one fixed generator `gamma_i` of the `i`th cyclic factor,
then every class is clearable using at most

\[
                              \sum_{i=1}^s(d_i-1)      \tag{3.4}
\]

tickets.

#### Proof

After modes are fixed, lattice feasibility is exactly
`u-sum_j g_(j,mu(j)) in Lambda(A_0)`, which is (3.2).  In (3.3), write each
torsion coordinate of the residual class as `a_i gamma_i` with
`0<=a_i<d_i` and activate `a_i` of its tickets.  This proves (3.4) after the
free coordinates have been cleared. \(\square\)

The theorem is only the lattice row.  Once (3.2) is met, the residual demand
may still lie outside the cone.  If it is in the cone, it may still be a hole
of `S(A_0)`.  Unit-normality, a network/matroid face, or the circuit theorem
below must still be proved.

### Proposition 3.2 (cone and lattice must use the same ticket mode)

There is a two-mode ticket instance whose bulk semigroup is normal, for
which one mode is fractionally feasible but not lattice-feasible and the
other is lattice-feasible but not fractionally feasible.  Hence separate
existential choices for cone feasibility and (3.2) do not imply a common
integral completion.

#### Proof

On five resource rows take the four independent bulk columns

\[
 c_1=00010,\quad c_2=01100,\quad
 c_3=10100,\quad c_4=11010,                           \tag{3.5}
\]

and full demand `11111`.  The default ticket is `t_0=00001`, leaving

\[
 u_0=11110={1\over2}(c_1+c_2+c_3+c_4).               \tag{3.6}
\]

Independence makes these coefficients unique, so `u_0` is in the cone but
not in the column lattice.  The alternative ticket `t_1=00111` leaves

\[
                         u_1=11000=-c_1+c_4.          \tag{3.7}
\]

Thus `u_1` is in the lattice, but its unique bulk coefficient vector has a
negative entry and it is outside the cone.  Independence also proves
`K(A_0) cap Lambda(A_0)=S(A_0)`: a lattice point has a unique integral
coefficient vector, and cone membership makes it nonnegative.  Neither
ticket mode has an integral completion. \(\square\)

Accordingly every positive theorem below quantifies one common mode
`mu` before testing its cone, lattice, and normality rows.

For a protected flag chronology, a ticket is admissible only if its literal
mode is a certified short block or macro and the selected modes satisfy

\[
       \rho(D)=\max(D_0,D_1,D_2,D_0+D_2-D_1)\le b.   \tag{3.8}
\]

Thus (3.4) is useful only when its tickets fit among the **actual** `b`
maximal short blocks.  The K19 and K21 ledgers

\[
\begin{array}{c|c}
 k&N_{\rm short}\\ \hline
19&14976\ldots14991\\
21& 8736\ldots 9573
\end{array}                                           \tag{3.9}
\]

show that raw short-role capacity is not scarce.  They do not prove that
these rows form that many separated literal tickets, nor that their residue
classes clear the required element of the full cokernel `Gbar` in (3.1).

### Corollary 3.3 (conservative short-row footprint test)

Suppose a ticket/reset bank has already been constructed, and let
`R_short` be the number of distinct short **rows** in its complete literal
footprint.  Then the short-row count creates no further scalar obstruction
whenever

\[
 R_{\rm short}\le14976\quad(K19),\qquad
 R_{\rm short}\le8736\quad(K21).                    \tag{3.10}
\]

In the special case where every one of the `rho(D)` reset blocks and every
one of `a` absorber tickets is a pairwise-disjoint single-short-row socket,
`R_short=rho(D)+a`.

#### Proof

The right sides are the minimum possible `N_short` values in (3.9), so the
displayed number of distinct rows fits every profile in the calibrated
range. \(\square\)

This is intentionally one-way.  The premise already contains the hard
literal assertion that the rows are separated, simultaneously realizable,
and have the required ticket/reset modes.  Without it, (3.10) is only
arithmetic.

## 4. Sharp direct-sum obstruction

Let the three two-element resource shores be

\[
 A=\{a_0,a_1\},\quad B=\{b_0,b_1\},\quad C=\{c_0,c_1\}. \tag{4.1}
\]

Take the four even-parity columns

\[
 000,\quad011,\quad101,\quad110,                     \tag{4.2}
\]

where `ijk` consumes `a_i,b_j,c_k`.

### Proposition 4.1 (disjoint dummy capacity does not remove parity torsion)

Weighting every column in (4.2) by `1/2` covers every resource exactly
once.  There is no integral exact cover.  The column lattice has index two
in its saturated real-span lattice.  Adding any number `b` of disjoint
private resources with forced singleton columns preserves all three facts
and leaves the same index-two obstruction.  These identity summands model
arbitrarily much algebraically independent reserve capacity; they are not
claimed to be physical short/reset fragments of the Boolean master.

#### Proof

The fractional assertion is immediate.  Exact coverage of the `A` and `B`
shores leaves only the two candidate pairs

\[
             \{000,110\},\qquad\{011,101\};          \tag{4.3}
\]

the first repeats `c_0` and the second repeats `c_1`.  Thus neither is an
exact cover.

Every nonzero full-rank minor of the six-by-four incidence matrix has
absolute determinant two, so the lattice index is two.  Equivalently the
six exact-cover equations force `2x_000=1`.  A direct sum with identity
columns and private rows does not change this Smith factor or the
infeasibility of the original component. \(\square\)

One odd-parity bridge column, for example `001`, changes the gcd of the
full-rank minors from two to one and gives the exact cover

\[
                         \{001,110\}.                 \tag{4.4}
\]

This is the smallest algebraic model of a symmetry-breaking reset ticket.
It does not assert that the K19/K21 Boolean bank contains the corresponding
literal ticket.

Proposition 4.1 is stronger than saying that a particular K17 table is bad,
but only at the abstract exact-cover level.  It proves that an arbitrarily
large **disjoint neutral** reserve and exact orbit marginals do not imply
one-copy rounding.  To transfer the statement to four-flag reset blocks one
would still need a literal embedding.  The missing algebraic invariant is
the cokernel class, followed by unit-normality.

There is, separately, a literal Boolean illustration in
`MATH_THEOREM_A_BOOLEAN_C10_NESTED_STATE_SMITH2_ORBIT_LIFT_OBSTRUCTION_20260802.md`:
five K11 length-two rows form an exact nested-state `C10`, have integral
orbit totals and `rho(D)=0`, but their restricted submaster has Smith
quotient `Z/2`.  That result confirms that Smith residue and short/reset
count are orthogonal inside a Boolean catalogue.  It is not a full K11,
K19, or K21 obstruction and is not a direct-sum embedding of Proposition
4.1.

## 5. A protected alternating-circuit descent theorem

Let `B` be an integral decorated owner/chain table satisfying a fixed
protected reset plan.  Because every owner occurs once, identify the
selected rows by their owners.  Let `F_P` be the forced transition matching
inside the protected bank.  From the bipartite compatibility graph delete
the endpoints of `F_P` and every conflicting edge; call the residual graph
`G_B^P`, and put

\[
             \nu_P(B)=|F_P|+\text{maximum matching size of }G_B^P. \tag{5.1}
\]

A **protected resource-zero circuit exchange** is a replacement

\[
                B'=(B\setminus C^-)\mathbin{\dot\cup}C^+              \tag{5.2}
\]

such that the two sides use identical lower-target and owner resources,
all protected columns survive, and the new table still has a certified
reset plan with (3.8).  This is a literal signed circuit, not merely an
orbit-count identity.

### Theorem 5.1 (protected DM circuit descent)

Assume there is one protected static table `B_0`.  Suppose that for every
reachable table `B` with `nu_P(B)<W`, there is a protected resource-zero
circuit exchange `B -> B'` satisfying

\[
                        \nu_P(B')\ge\nu_P(B)+1.      \tag{5.3}
\]

Then after at most `W-nu_P(B_0)` exchanges there is a table whose literal
transition graph has a perfect matching extending every forced transition
in `F_P`.  The resulting object is an integral solution of the fixed-core
joint master.

#### Proof

Every exchange preserves the physical exact cover and the protected reset
face.  The integer potential `W-nu_P(B)` decreases by at least one and is
nonnegative.  At zero, choose a perfect transition matching.  It gives one
incoming and outgoing transition at every owner-labelled row, hence the
joint master by Theorem 1.1. \(\square\)

Condition (5.3) has a proof-safe local certificate.  Take a maximum matching
`M` of `G_B^P`; require **every** edge of `M` to remain present in
`G_(B')^P`, and exhibit an `M`-augmenting path there.  Merely retaining the
edges of `M` outside the circuit support is insufficient: lost matched edges
inside the support can cancel the nominal augmentation.  No comparison of
raw degrees is sufficient.

### Lemma 5.2 (protected supply by load)

Fix `B,M` and let `C(B,M)` be a bank of circuits, each of which satisfies
the augmenting-path certificate above and the reset bound.  Let `F` be the
set of resources forbidden by the protected collar or earlier locked
choices.  If every `f in F` lies in at most `Delta` circuits and

\[
                          |C(B,M)|>\Delta |F|,        \tag{5.4}
\]

then one circuit is disjoint from `F` and is legal for Theorem 5.1.

#### Proof

At most `Delta|F|` circuits meet `F`, by the union bound over their first
forbidden resource. \(\square\)

This is the exact place where Boolean abundance can enter.  It is not
enough to count orbit circuits: (5.4) concerns literal circuits after all
resource, address, and reset guards.  The parity tensor has no augmenting
even-parity circuit; the odd bridge (4.4) supplies the missing class.

## 6. The resulting conditional fixed-core theorem

### Theorem 6.1 (protected fixed-core common-base absorber)

Fix `k,H` and a fixed-core invariant decorated-row bank.  A balanced
one-copy factor exists if all of the following hold.

1. There is **one common choice** `mu` of all ticket modes, defining a
   literal protected short/macro bank `P_mu`, such that `P_mu` satisfies
   ROTS product-order legality, rooted residual Hall, endpoint/address rows,
   and the sharp reset bound `rho(D)<=b<=N_short`.
2. For this same `mu`, residual literal matrix `A_(P,mu)`, and demand `u_mu`,
   \[
        u_\mu\in K(A_{P,\mu})\cap\Lambda(A_{P,\mu}). \tag{6.1}
   \]
   Fractional fixed-core orbit feasibility may certify the cone membership
   only when the residual bank is invariant under the subgroup used for the
   quotient; otherwise literal fractional feasibility is required.
3. On this same mode and residual face, either
   * the residual skip-port demand is unit-normal; or
   * one of the integral faces in Corollary 2.2 applies; or
   * `P_mu` is embedded in one integral **decorated** owner/chain table `B_0`
     and the protected DM-circuit supply of Theorem 5.1 applies from `B_0`.

#### Proof

Contract `P_mu`.  Item 2 puts the same residual unit
demand in the cone and lattice of the same matrix.  Unit-normality gives a
semigroup representation by Theorem 2.1;
Corollary 2.2 gives the same conclusion on either structured integral face.
Alternatively the third branch supplies the starting decorated table
required by Theorem 5.1, which constructs the integral transition matching
directly.  Reinsert `P_mu` and apply Theorem 1.1. \(\square\)

This theorem is deliberately conditional, but its hypotheses are strictly
stronger and more informative than orbit feasibility:

* equation (6.1) contains the exact invariant missed by the parity tensor;
* item 3 separates nonnegative holes from lattice torsion;
* ROTS handles protected static extension and literal reset capacity; and
* circuit exchanges must be literal and resource-zero, which is the exact
  recoupling qualification.

For K19/K21, the next finite or structural audit is therefore:

1. form the protected skip-port matrix on the joint fixed-core bank;
2. compute the Smith class of its unit demand after a candidate reset plan;
3. catalogue literal short-ticket residues and test (3.2); and
4. either prove unit-normality on that face or verify the DM circuit supply
   (5.3), preferably through the load inequality (5.4).

The K19/K21 short-row ranges make Step 3 numerically plausible.  They do not
settle any of Steps 1--4.

## 7. Scope

The results above close no Boolean supply theorem.  In particular they do
not assert:

* that the K19 or K21 skip-port cokernel has bounded invariant factors;
* that their short rows realize generator tickets;
* that the residual semigroup is normal;
* that an orbit circuit has a literal disjoint lift;
* that a perfect transition matching is one directed cycle; or
* residence, deep upper support, source factorability, common-cap, compiler,
  or an equality word.

What is proved is the exact common algebra in which those questions must be
answered and a sharp counterexample to every argument using only fractional
orbit counts and scalar reset abundance.
