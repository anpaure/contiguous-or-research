# Arbitrarily named PBBS bodies cannot be reached by an `O(d)` relative graft

**Date:** 2026-08-05  
**Method:** the PBBS soliton-height invariant, cyclic prefix amplitudes, and
component contraction; no computation or search  
**Status:** unconditional obstruction to the universally quantified named
relative-graft lemma.  There are literal sharp-shield/residence-collar banks
whose PBBS height is `O(d)` and prescribed PBBS body components of height
`m-1`.  Any factor rethread which attaches such a bank to such a body while
leaving the PBBS factor unchanged elsewhere uses `Omega(m)` new incidence
edges.  Since `d=Theta(sqrt(m))`, no uniform `O(d)` relative graft can work
for arbitrary prescribed PBBS bodies.  This does not obstruct choosing the
body components in correlation with the collar placement.

## 1. PBBS height and a Lipschitz lemma

Work in the Middle-Levels incidence graph on

\[
                         n=2m-1
\]

coordinates, with owner shore `binom([n],m)` and facet shore
`binom([n],m-1)`.  For an owner `T`, write

\[
                         A(T)=[n]\setminus T.                \tag{1.1}
\]

Thus `A(T)` is a deficit-one PBBS state of rank `m-1`.

For a cyclic zero-one word `A` with one more zero than one, give a member
weight `+1` and a nonmember weight `-1`.  Let `H(A)` be the height of the
Dyck word obtained by cutting immediately after the cyclic unmatched zero
and deleting that zero.  Equivalently, by the cycle lemma,

\[
       H(A)=\max\left\{\sum_{i\in J}\omega_i:
              J\text{ a cyclic interval}\right\}.          \tag{1.2}
\]

of its cyclic prefix-sum walk.  The peak-pruning/PBBS action-angle theorem
identifies this number with the largest soliton part `lambda_1`; in
particular it is constant on every PBBS factor component.

### Lemma 1.1 (one Johnson move changes height by at most two)

If `T,T'` are equal or adjacent in `J(n,m)`, then

\[
                         |H(A(T))-H(A(T'))|\le2.             \tag{1.3}
\]

#### Proof

In the nontrivial case, `A(T')` is obtained from `A(T)` by changing one
zero to one and one one to zero.  The weight of every cyclic interval
therefore changes by `0`, `2`, or `-2`.  Taking the maximum in (1.2) in
both directions proves (1.3).  `square`

Let `F_PBBS` be the natural bipartite PBBS two-factor.  If an incidence
edge `IT`, with `I subset T`, joins vertices which lie on PBBS components
`C_I,C_T`, respectively, then the old PBBS owner paired through `I` and
the owner `T` are equal or Johnson adjacent.  Hence Lemma 1.1 gives

\[
                         |H(C_I)-H(C_T)|\le2.                \tag{1.4}
\]

Here `H(C)` denotes the common value of `H` on the owners of `C`.

## 2. A sharp shield entirely in bounded height

Put `h=m-1` and cyclically order the ground coordinates as

\[
             \kappa,x_1,y_1,x_2,y_2,\ldots,x_h,y_h.         \tag{2.1}
\]

Define the sharp full-union Johnson shield

\[
 T_j=\{\kappa\}\cup\{y_1,\ldots,y_j\}
             \cup\{x_{j+1},\ldots,x_h\},
             \qquad0\le j\le h.                            \tag{2.2}
\]

It has `m` owners, every step is the exchange `x_(j+1)->y_(j+1)`, and
its owner union is the full ground set.  This is the sharp shield from the
full-union localization theorem.

Its complementary PBBS state is

\[
 A(T_j)=\{x_1,\ldots,x_j\}
             \cup\{y_{j+1},\ldots,y_h\}.                    \tag{2.3}
\]

On every coordinate pair `(x_i,y_i)`, the membership word of (2.3) is
either `10` or `01`; at pair boundaries the prefix walk returns to the
same level.  The extra coordinate `kappa` is the unique deficit zero.
Consequently

\[
                             H(A(T_j))\le2                  \tag{2.4}
\]

for every shield owner.

Now attach any fixed number of literal screen paths and sharp residence
collars whose total distance from the shield endpoints in the Johnson
graph is at most `K_0 d`, where `K_0` is an absolute constant.  This
includes the two opened common-history `C8` paths and their depth-`d`
incoming/outgoing collars.  Lemma 1.1 gives

\[
                         H\le Kd,
             \qquad K:=2+2K_0,                              \tag{2.5}
\]

on every owner of this protected shield--collar bank.  A facet incident
with one of these owners lies on a PBBS component of height at most
`Kd+2`, by (1.4).

Thus the sharp full-ground shield does **not** force the protected bank to
visit high PBBS soliton sectors.  The pair ordering (2.1) realizes the
entire bank at height `O(d)`.

## 3. Component-contraction lower bound

Let `P` be a protected incidence-path bank and let `F_0` be a partial or
spanning factor which agrees with `F_PBBS` away from `P`.  Assume every
PBBS component meeting `P` has height at most `H_0`.

Let `F'` be another spanning factor which retains every protected edge of
`P`.  Write

\[
 q=|F'\setminus(F_0\cup P)|                                 \tag{3.1}
\]

for the number of genuinely new incidence edges outside the protected
bank.  Edges deleted from the old factor do not help the estimate.

### Theorem 3.1 (height-distance support bound)

If one component of `F'` meets both `P` and a PBBS component `C`, then

\[
                         q\ge {H(C)-H_0\over2}.              \tag{3.2}
\]

The right side is understood as zero when it is negative.

#### Proof

Contract every component of `F_PBBS`.  Also contract into one root all
PBBS components which meet `P`; retaining the protected bank may join
those root components for free.  Every old PBBS edge becomes a loop.
Every genuinely new incidence edge gives one edge between two contracted
PBBS components, and (1.4) says that the heights at its endpoints differ
by at most two.

An `F'` component meeting both `P` and `C` projects to a walk from the
root set to `C`.  It uses at most `q` genuinely new edges.  Starting at
height at most `H_0` and changing height by at most two per edge gives

\[
                         H(C)\le H_0+2q,
\]

which is (3.2).  `square`

The statement allows arbitrarily long unchanged excursions inside any
PBBS component and arbitrarily many deleted edges.  Such excursions cost
nothing but also cannot change the soliton height.  Thus helper components
and two-colour alternating returns do not evade the bound.

If support is counted in contracted matching-pair units rather than new
incidence edges, one switched unit creates at most two new coloured
incidences.  Hence (3.2) still gives a matching-pair lower bound

\[
                         s\ge {H(C)-H_0\over4}.              \tag{3.3}
\]

## 4. A prescribed body at linear distance

The fully nested deficit-one state has Dyck part

\[
                         1^{m-1}0^{m-1}                     \tag{4.1}
\]

and therefore lies on a PBBS component `C_star` with

\[
                         H(C_star)=m-1.                     \tag{4.2}
\]

Use the low-height sharp-shield/collar realization of Section 2.  Then
`H_0<=Kd+2`.  Theorem 3.1 gives

\[
 q\ge {m-1-Kd-2\over2}=\Omega(m),                          \tag{4.3}
\]

and, in contracted matching-pair units,

\[
 s\ge {m-1-Kd-2\over4}=\Omega(m).                          \tag{4.4}
\]

In the optimal OR-word regime

\[
                         d=\Theta(\sqrt m),                  \tag{4.5}
\]

so (4.3)--(4.4) are not `O(d)`.

It is enough to prescribe `C_star` as one of the two requested PBBS body
components; failure of that one attachment already prevents the demanded
two-body graft.

## 5. Typed endpoints and the localized upper bank

The obstruction is earlier than either of the two extra interfaces.

1. Requiring the outer collar socket to retain its nested positive/zero
   endpoint state only removes possible rethreads and cannot weaken
   (3.2).
2. Requiring the rank-stratified upper-backup paths to remain fixed and
   disjoint also only removes possible rethreads.  If those paths are
   included in the protected root bank, the same theorem applies with
   `H_0` equal to the maximum PBBS height of the root bank.  No low-height
   realization of an arbitrary prescribed backup bank is asserted here.

No claim that arbitrary stabilizer copies automatically have low height is
needed for the owner/q1 negative result: (4.3) already holds before any
upper constraint is imposed.  In the intended interface the backup bank is
protected pointwise, not offered as an additional attachment router; under
that scope it cannot cure the owner/q1 distance obstruction.

## 6. Correct quantifier and remaining positive target

The following universally quantified lemma is false:

> for every pair of prescribed PBBS body components, two opened
> sharp-shield/collar paths admit an `O(d)`-support relative alternating
> graft to those bodies.

The counterexample is the low-height protected bank (2.1)--(2.5) together
with the prescribed maximally nested body (4.1).

The proof-safe replacement must correlate body selection with collar
placement.  An exact positive target is:

> **Height-local named-graft lemma.**  Choose the PBBS body components
> together with the protected shield/collar bank so that every requested
> body lies within `O(d)` edges of the bank in the PBBS component-contact
> graph, and then construct edge-compatible alternating returns realizing
> those short contact paths while preserving the typed socket and upper
> backups.

The height condition

\[
                         |H(C)-H(P)|=O(d)                   \tag{6.1}
\]

is necessary but not sufficient.  The remaining incidence, two-colour,
and endpoint-state rows still have to be proved on that correlated face.
Alternatively one may allow `Theta(m)` relative support; the explicit
long PBBS parity bridge shows that linear support is a natural scale in
the unconditioned factor.

## 7. Dependencies

The PBBS height invariant is the largest peak-pruning/soliton part used in
`MATH_THEOREM_PBBS_SOLITON_GAP_FORCES_EXPONENTIALLY_MANY_SELECTED_CYCLES_20260805.md`.

The sharp shield and the quadratic exterior localization theorem are in
`MATH_THEOREM_FULL_UNION_SHIELDS_LOCALIZE_ALL_EXTERIOR_SPLICE_DAMAGE_20260805.md`.

The sharp residence collars are in
`MATH_THEOREM_ROOTED_ROTOR_OPENING_RESIDENCE_COLLAR_AND_C8_GRAFT_GATE_20260805.md`.

The exact two-colour alternating-return normal form is in
`MATH_THEOREM_C8_RELATIVE_PBBS_ALTERNATING_GRAFT_AND_UPPER_BACKUP_20260805.md`.
