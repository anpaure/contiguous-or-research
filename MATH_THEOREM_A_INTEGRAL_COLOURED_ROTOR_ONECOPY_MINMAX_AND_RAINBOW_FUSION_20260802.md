# Integral coloured rotors: exact one-copy min--max and rainbow fusion

**Date:** 2026-08-02  
**Lane:** A, integral coloured rotor fusion  
**Status:** unconditional fixed-table one-copy theorem, exact connected
certificate, exact full-depth rainbow normal form and fusion calculus, and a
sharp abstract fractional obstruction.  The canonical all-`k` table-selection
lemma remains open.

## 0. Outcome and corrected input

The only pull-clock input used here is
`MATH_THEOREM_TRIANGULAR_PULL_CLOCK_CORRECTED_20260801.md`, SHA
`7302724eb8b405c2bf1efcc743a1de06809cd1f9b3134e07ba8aa6933b631b21`.
In particular its valid inequalities are

\[
 {A_\delta\over A_{\delta+1}}\geq\rho,
 \qquad {\Delta_{j+1}\over\Delta_j}\leq\rho,
 \qquad \theta={1\over\rho}.                         \tag{0.1}
\]

No argument below uses the reversed ratios from the superseded derivation.
The corrected theorem supplies a rational stationary literal circulation.
It does **not** by itself select one physical trace of every owner colour.

This note proves the following exact separation.

1. Once one exact owner--payload table is fixed and each role has a
   payload-transparent tail/head rectangle, one-copy rounding is integral.
   Feasibility is equivalent to one explicit Hoffman cut family.
2. Connected one-copy rounding is also exact: reserve a distinct-owner
   spanning skeleton and apply the same cuts to the residual rectangles.
   This gives one Euler component and hence zero route sidecar.
3. Before owners are attached to full-depth payload chains, the literal
   problem is a functional three-shore object: a **rainbow directed cycle
   cover**.  Its LP is not integral in general, even when every two-shore
   projection is complete.
4. Colour-neutral `q`-way head permutations are the exact fusion moves.
   Bounded `2x2` rectangles are sufficient on a fusion-tree face but are not
   necessary; from its identity cover an explicit affine family has no
   nontrivial `2x2` move and admits a global `N`-way Hamilton move.
5. If a balanced integral selector has repeated owner colours, a
   hereditarily realizable unit-packet bank contracts the repetitions exactly
   under a max-flow cut system.
6. For odd `k=2r-1`, an integral residual chain table containing the complete
   coatom row always admits a one-copy owner assignment.  Thus on that face
   the owner projection is solved; chainization and chronology-compatible
   fusion remain open.

The theorem therefore replaces denominator clearing by an exact min--max
gate.  It does not yet prove `B(k)+O(1)`: the corrected fractional clock has
not been coupled to one exact table satisfying these cuts.

## 1. The exact fixed-table one-copy cut theorem

Let `V` be a finite literal state set.  Let `I` be the free occurrence roles
after a fixed protected root/path bank `P` has been removed.  Put

\[
 \partial(u\to v)={\bf1}_v-{\bf1}_u,
 \qquad \eta=\partial P,
 \qquad \eta(V)=0.                                   \tag{1.1}
\]

Role `i` has a fixed owner and a fixed named-target payload.  Its legal trace
menu contains a Cartesian rectangle

\[
                         A_i\times H_i\subseteq V\times V,    \tag{1.2}
\]

and every `(a,h)` in that rectangle carries exactly that same owner and
payload.  All further guards which are intended to be preserved must already
be included in the lists `A_i,H_i`; no upper, residence, or compiler guard is
implicit.

The protected bank together with these free roles is assumed to be an exact
table: the role owner labels are pairwise resource-disjoint and use every
required owner once, while the fixed role payloads are pairwise
resource-disjoint and partition the required named residual targets.  The
theorem below rounds the literal state choices; it does not create that
table.

For `X subseteq V`, define

\[
 \ell_A(X)=|\{i:A_i\subseteq X\}|,
 \qquad r_H(X)=|\{i:H_i\cap X\ne\varnothing\}|.       \tag{1.3}
\]

### Theorem 1.1 (Hoffman one-copy criterion)

There is a selector choosing one arc `(a_i,h_i) in A_i times H_i` for every
role and satisfying

\[
                  \sum_{i\in I}\partial(a_i\to h_i)=-\eta       \tag{1.4}
\]

if and only if

\[
 \boxed{\ell_A(X)-r_H(X)\leq\eta(X)
                  \quad\hbox{for every }X\subseteq V.}          \tag{1.5}
\]

Whenever (1.5) holds, the selector is integral and uses every fixed owner
and every declared named target exactly once.

#### Proof

Let `p_v` and `q_v` be the selected tail and head counts.  Equation (1.4)
is

\[
                         p-q=\eta.                    \tag{1.6}
\]

Every role whose entire tail list lies in `X` must place its tail in `X`, so
`p(X)>=ell_A(X)`.  At most `r_H(X)` roles can put a head in `X`.  Hence
(1.6) implies (1.5).

For sufficiency, put

\[
 f_A(X)=|\{i:A_i\cap X\ne\varnothing\}|,
 \qquad f_H(X)=|\{i:H_i\cap X\ne\varnothing\}|.       \tag{1.7}
\]

The possible aggregate tail-count vectors form the integral polymatroid
base polytope

\[
 B(f_A)=\sum_{i\in I}\operatorname{conv}\{{\bf1}_v:v\in A_i\}, \tag{1.8}
\]

and analogously the possible head counts form `B(f_H)`.  Thus (1.6) asks
for

\[
                         p\in B(f_A)\cap(B(f_H)+\eta). \tag{1.9}
\]

Polymatroid intersection says that (1.9) is nonempty exactly when

\[
 f_A(Y)+f_H(V\setminus Y)\geq |I|+\eta(Y)
                           \quad(Y\subseteq V).        \tag{1.10}
\]

Replacing `Y` by `V-X` and using

\[
 f_A(V\setminus X)=|I|-\ell_A(X),
 \qquad \eta(V\setminus X)=-\eta(X),                 \tag{1.11}
\]

turns (1.10) into (1.5).  Both rank functions are integral, so their common
base polytope has an integral point `p`.  Two ordinary bipartite
`b`-matchings decompose `p` into one tail choice and `p-eta` into one head
choice for every role.  Pair the two choices belonging to the same role;
Cartesianity in (1.2) makes every pair a literal legal trace.  Owner and
payload exactness were fixed rolewise.  \(\square\)

The same proof can be written as an integral transshipment and (1.5) is
exactly its closed-cut family.  Thus this is a Hoffman theorem, not merely a
necessary Hall bound.

### Corollary 1.2 (fractional implies integral on one common table)

If a rational root-conditioned circulation is supported in the rectangles
of one fixed exact owner--payload table, then (1.5) holds and an integral
one-copy selector exists on that same table.

This is the strongest valid use of stationary fractional flow.  The
corrected pull clock averages over payload tables and owner assignments, so
it does not yet satisfy the premise.

### Theorem 1.3 (exact connected one-copy criterion)

Here a selector is **connected** when the underlying undirected support of
`P` together with all selected free arcs is connected.  Such a selector
exists if and only if there are:

1. a state set `V_*` containing every state used by `P`;
2. legal arcs `R`, from pairwise distinct free roles, with both endpoints in
   `V_*`, such that the
   underlying undirected support of `P union R` contains a spanning tree of
   `V_*`; and
3. after deleting the roles used by `R`, restricting every remaining
   rectangle to `(A_i cap V_*) times (H_i cap V_*)`, and replacing `eta` by

   \[
                              \eta_R=\eta+\partial R,  \tag{1.12}
   \]

   all cuts (1.5) hold for the residual system.

#### Proof

Under the three conditions, Theorem 1.1 supplies an integral residual
selector entirely inside `V_*`.  Its boundary is `-eta_R`, so adjoining
`P` and `R` is balanced.  The reserved support already spans `V_*`, hence
the complete support is connected.

Conversely, take `V_*` to be the used states of a connected selector and
choose any spanning tree of its full underlying support.  Let `R` be the
distinct free-role arcs which occur in that tree.  The fixed bank `P`
together with `R` contains the tree, even when `P` itself contains cycles.
Deleting the roles of `R` leaves the actual residual selector, so the
residual cuts hold by Theorem 1.1.  \(\square\)

A connected balanced support has an Euler circuit.  Therefore Theorem 1.3
is an exact zero-sidecar certificate on the rectangle face.

## 2. Full-depth functional rainbow normal form

The preceding theorem fixes owners before rounding.  The genuinely coloured
gate appears when the target chains are fixed but their owner assignment is
not.

Let `I` index `N` strict depth-`d` payload chains

\[
 \varnothing=S_{i,0}\subsetneq S_{i,1}\subsetneq\cdots
             \subsetneq S_{i,d}.                     \tag{2.1}
\]

Assume their named targets partition the required residual target bank.  Put

\[
 A_{i,d-q+1}=S_{i,q}\setminus S_{i,q-1},
 \qquad h_i=(A_{i,1},\ldots,A_{i,d}),                 \tag{2.2}
\]

and assume the states `h_i` are distinct.  Let `Omega` be the rank-`r`
owner bank, with `|Omega|=N`.

### Theorem 2.1 (functional coloured-rotor equivalence)

A literal predecessor arc **from bank state `h_j` to bank state `h_i`**
exists precisely when

\[
 (A_{j,2},\ldots,A_{j,d})
       =(A_{i,1},\ldots,A_{i,d-1})                   \tag{2.3}
\]

and

\[
 \kappa(j,i):=S_{i,d}\cup A_{j,1}\in\Omega.          \tag{2.4}
\]

Its trace is uniquely

\[
                (A_{j,1},A_{i,1},\ldots,A_{i,d}),    \tag{2.5}
\]

and its owner colour is `kappa(j,i)`.

Consequently exact target use, state balance, and one-copy owner use are
equivalent to binary variables `x_(j,i)` satisfying

\[
 \begin{aligned}
  \sum_jx_{j,i}&=1 &&(i\in I),\\
  \sum_ix_{j,i}&=1 &&(j\in I),\\
  \sum_{\kappa(j,i)=T}x_{j,i}&=1 &&(T\in\Omega).
 \end{aligned}                                        \tag{2.6}
\]

Thus an integral selector is exactly a rainbow directed cycle cover.  Its
Euler components are the permutation cycles, and zero-sidecar connected
balance is exactly a rainbow Hamilton cycle.

#### Proof

The overlap equation for the tail state `h_j` and head state `h_i` is
exactly (2.3).  The last `q` letters of (2.5) have union `S_(i,q)`, so the
trace carries payload `i`.  Its total union is (2.4), proving the functional
owner formula.

The first row of (2.6) selects every payload/head once.  Hence the multiset
of selected heads is exactly the `N` distinct bank states `{h_i}`.  On the
zero-boundary face, balance forces the tail multiset to be the same bank;
therefore every selected tail is a unique `h_j`, so no tail outside the bank
is relevant to a balanced selector.  The second row records this exact tail
use.  The third selects every owner colour once.  The first two rows make a
permutation; its cycles are precisely the directed Euler components.
\(\square\)

If owner `T_i` has already been attached to payload chain `i`, retain only
arcs with `kappa(j,i)=T_i`.  The colour row then becomes automatic and
(2.6) collapses to ordinary predecessor Hall.  Conflating this attached
face with the unattached three-shore face is the source of the false generic
rounding inference.

## 3. Exact colour-neutral fusion moves

Let `F` be a rainbow cycle cover from Theorem 2.1.

### Theorem 3.1 (`q`-way rainbow fusion)

Choose one selected arc `j_t->i_t` on each of `q` distinct cycles of `F`.
Let `sigma` be a `q`-cycle.  Replace those arcs by

\[
                         j_t\longrightarrow i_{\sigma(t)}.   \tag{3.1}
\]

With every complementary arc fixed, (3.1) is a resource-exact fusion if and
only if

1. every new arc exists, and
2. the owner-colour multisets agree:

   \[
    \{\!\{\kappa(j_t,i_{\sigma(t)}):1\le t\le q\}\!\}
      =\{\!\{\kappa(j_t,i_t):1\le t\le q\}\!\}.       \tag{3.2}
   \]

When these conditions hold, all `q` old cycles fuse into one cycle while
every owner and payload remains exact.

#### Proof

The tails and heads in (3.1) are merely permuted, so the first two rows of
(2.6) remain exact.  The fixed complement leaves the owner row unchanged if
and only if (3.2) holds.  Cutting one edge from each old cycle gives `q`
directed paths; reconnecting their heads by one `q`-cycle concatenates all
paths into one directed cycle.  \(\square\)

For `q=2`, selected arcs `j->i` and `l->m` may be crossed precisely when

\[
 \{\!\{\kappa(j,m),\kappa(l,i)\}\!\}
       =\{\!\{\kappa(j,i),\kappa(l,m)\}\!\}.          \tag{3.3}
\]

If a cycle cover's components admit a tree of pairwise arc-disjoint
`2x2` witnesses, processing the tree edges gives a rainbow Hamilton cycle.
Absence of such a rectangle is only an obstruction to this move class;
Theorem 3.1 permits larger circuits.

## 4. Why fractional stationarity does not round generically

### Theorem 4.1 (smallest three-shore parity hole by shore size)

Let tails, heads, and owner colours all be `{0,1}`.  Allow all four arcs and
set

\[
                         \kappa(p,h)=p\mathbin\oplus h.       \tag{4.1}
\]

Giving every arc weight `1/2` satisfies every tail, head, and owner row with
load one, and every two-shore projection is `K_(2,2)`.  There is no integral
rainbow cover.

#### Proof

The only tail--head perfect matchings are the identity, whose two colours
are both zero, and the transposition, whose two colours are both one.  The
four triples are equivalently

\[
                         000,\quad011,\quad101,\quad110.      \tag{4.2}
\]

Any two of them share a coordinate.  The constraint minor using rows
`tail0,tail1,head0,colour0` and the four columns has determinant two.  Hence
the LP point is genuinely nonintegral.  A common shore of size one has only
one possible triple and is integral, so common shore cardinality two is
minimal.  \(\square\)

This is an abstract rotor obstruction.  It is not a Boolean-chain
counterexample.

### Lemma 4.2 (the Boolean union colouring excludes the intercalate)

Suppose `kappa(j,i)=C_j union S_i`.  If

\[
 C_1\cup S_1=C_2\cup S_2=X,
 \qquad C_1\cup S_2=C_2\cup S_1=Y,                   \tag{4.3}
\]

then `X=Y`.

#### Proof

If `x in X-Y`, the first equality and `x notin C_1 union S_2` force
`x in S_1-C_1-S_2`.  The second diagonal then forces `x in C_2`, contrary
to `x notin C_2 union S_1=Y`.  Hence `X subseteq Y`; symmetry gives the
reverse inclusion.  \(\square\)

Thus the smallest abstract determinant-two hole does not embed in the
functional Boolean union-colour face.  This does not prove that the Boolean
face is normal; authenticated physical odd-cycle minors remain possible.

### Theorem 4.3 (affine odd/even calibration)

On `Z_N`, allow every arc and put

\[
                         \kappa(j,i)=j+i\pmod N.       \tag{4.4}
\]

The uniform weight `1/N` is an exact fractional point.  If `N` is odd,
`i=j+b` with `gcd(b,N)=1` is a rainbow Hamilton cycle.  If `N` is even, no
rainbow cycle cover exists.

#### Proof

For odd `N`, translation by `b` is one permutation cycle and the colours
`2j+b` are a permutation of `Z_N`.  For even `N`, every permutation `pi`
satisfies

\[
 \sum_j\kappa(j,\pi(j))=2\sum_jj=0\pmod N,            \tag{4.5}
\]

whereas using every colour once has sum `N/2 mod N`.  \(\square\)

For odd `N`, the rainbow identity cover has `N` loops and no nontrivial
colour-neutral `2x2` switch.  Indeed, crossing the loops `a->a,b->b`
replaces colours `{2a,2b}` by `{a+b,a+b}`; multiset equality forces
`2a=2b`, hence `a=b`.  Nevertheless the global translation fuses the cover.
Thus a bounded rectangle basis cannot be assumed without proof even in a
complete, maximally regular positive atlas.

## 5. Exact owner-overload absorption

Suppose an integral role/payload/state-balanced selector has owner
multiplicities `m_T`, with

\[
                         \sum_Tm_T=|\Omega|.           \tag{5.1}
\]

A directed packet `U->V` is a literal boundary-zero replacement preserving
all roles, payloads, and guards while changing the owner count by
`-e_U+e_V`.  Let `kappa_(UV)` be the number of independently available
copies.  Call the packet bank **hereditarily realizable** if every integral
flow within these capacities can be executed serially without invalidating
the remaining declared packets.

### Theorem 5.1 (owner contraction cuts)

Under hereditary realizability, the owner multiplicities can be changed to
the all-one vector if and only if

\[
 \boxed{m(X)-|X|\leq\kappa(\delta^+X)
                  \quad\hbox{for every }X\subseteq\Omega.}   \tag{5.2}
\]

Exactly

\[
                         E=\sum_T(m_T-1)_+             \tag{5.3}
\]

source-to-sink unit paths suffice.  A path is one transported owner unit but
may fire several packet arcs; the total number of packet firings can exceed
`E`.

#### Proof

Put surplus `s_T=(m_T-1)_+` and demand `d_T=(1-m_T)_+`.  Equation (5.1)
gives equal total surplus and demand.  Add a source joined to `T` with
capacity `s_T`, packet arcs with capacities `kappa`, and arcs from `T` to a
sink of capacity `d_T`.  The max-flow cut condition is

\[
 s(X)\leq d(X)+\kappa(\delta^+X),                     \tag{5.4}
\]

which is (5.2) because `s(X)-d(X)=m(X)-|X|`.  Integral max flow decomposes
into `E` unit paths from surplus to missing owners.  Hereditary realization
executes those paths, each lowering total surplus by one.  Necessity follows
by counting how many surplus units must leave `X`.  \(\square\)

Without unit packet saturation and hereditary realization, (5.2) is not
sufficient: the desired correction must also lie in the packet lattice and
interacting physical packets may fail to compose.

## 6. The odd-central owner projection is already integral

The independently audited theorem
`MATH_THEOREM_ROTOR_ODD_COATOM_ONECOPY_AND_PROTECTED_OWNER_CIRCUITS_20260802.md`,
SHA
`6b8626ee4955cfdad41af4916c7afd4980a1bea66126e0633ebd9e8b77824932`,
gives the following consequence.

### Corollary 6.1 (odd coatom owner rounding)

Let `k=2r-1`.  Suppose the residual strict-lower bank is integrally
partitioned into `W=binom(k,r)` target chains and contains every
rank-`(r-1)` target.  Then every role has exactly one coatom maximum, and
the `r`-regular balanced middle-levels incidence graph assigns these maxima
bijectionally to all rank-`r` owners.  Hence the table has an exact one-copy
owner attachment with no added roles.

Every one protected coatom--owner incidence extends; a protected matching
extends exactly under its residual Hall-damage inequalities.  All owner
attachments are connected by protected alternating incidence circuits.
A circuit is chronology-safe exactly when its replacement traces have the
same total state boundary as the traces removed.

Thus, after integral chainization, owner repetition is not a separate
odd-central marginal obstruction.  The chronology boundary and component
rows remain genuinely joint.

## 7. Exact remaining gate and `B(k)+O(1)` scope

The corrected pull clock proves a rational point in an average over chain
tables, owners, and literal states.  The fixed-table theorem requires one
literal choice satisfying all of them simultaneously.  The exact remaining
lower gate can therefore be written as follows.

> Choose an integral triangular chain table, a compatible owner attachment,
> and a protected root `P` so that the Hoffman deficit
>
> \[
>  \Delta=\max_{X\subseteq V}
>       \bigl(\ell_A(X)-r_H(X)-\eta(X)\bigr)           \tag{7.1}
> \]
>
> is nonpositive.  For zero sidecar, choose in addition a distinct-owner
> spanning skeleton whose residual deficit is nonpositive as in Theorem 1.3.

On the saturated unattached face, the same statement is the existence of a
rainbow cycle cover followed by a colour-neutral fusion to one cycle.

The known quotient/type obstructions do not refute this canonical target.
The independent scope audit
`MATH_AUDIT_A_TRIANGULAR_ONECOPY_ROTOR_OBSTRUCTION_SCOPE_20260802.md`
proves that for `k>=31` the canonical aggregate age vector already lies in
the integral rotor semigroup, and that the rigid rotation holes freeze data
not forced by the triangular target.  The smallest actual central literal
obstruction is `k=4`, where one route edge is both necessary and sufficient.

Finally, `O(1)` Euler components alone is not an `O(1)` sidecar theorem.  If
components are opened at states `u,v`, their exact de Bruijn reset cost is

\[
                         d-\operatorname{ov}(u,v).     \tag{7.2}
\]

Thus `B(k)+O(1)` requires either one connected selector or total overlap
deficit `O(1)`.  Residence, arbitrary upper shadows, exterior chronology,
and the terminal common-cap compiler remain downstream unless encoded in
the legal rectangle lists from the start.

The present result is therefore a rigorous integral-rotor min--max and
fusion theorem, not a proof of `B(k)+O(1)` or `B(k)`.
