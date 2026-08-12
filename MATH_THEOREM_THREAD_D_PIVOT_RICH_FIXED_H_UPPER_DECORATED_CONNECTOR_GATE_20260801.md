# Pivot-rich fixed-`H` packets reduce exactly to a bounded-hole Catalan connector

Date: 2026-08-01  
Lane: Thread D / additive-constant packet host  
Status: exact reduction and damage ledger.  The uniform connector extension
assertion in Section 6 is a hypothesis, not a proved all-dimension theorem.

## 0. Result

The sharp pivot packet of
`MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`
has **zero local upper damage**: every old interval-OR occurrence survives
the packet replacement, at every width and in every exterior context.  For
fixed `H`, its protected middle-level incidence lift also fits inside a
spanning owner/lower-`q1` two-factor.

Neither statement controls the upper palette or the component count of the
unprotected completion.  Those two global rows have the following weakest
exact certificate.  If `t` named immediate-upper colours may be absent, the
rooted part has `U-t` edges and `C+t` components; a connector forest must
then contribute exactly `C+t-s` edges, after which only an `s`-by-`s`
ordinary Hall completion remains.  The resulting factor has at most `s`
components and at most `t` immediate-upper holes.  Opening its components
outside the protected paths creates at most `s` further immediate-upper
holes.  Thus the exact additive ledger is

\[
                         \boxed{s+t=O(H)}.                 \tag{0.1}
\]

This cleanly separates packet-local zero damage from connector/opening
damage.  It also isolates the missing uniform theorem: a protected
**partial rooted Catalan forest plus connector forest** with (0.1).  Small
protected-factor extension, local OR transparency, and residual Hall do not
imply that correlated object.

Global residence outside the packets, upper targets of width greater than
one, and the common compiler cap are not conclusions of this note.

## 1. Coordinates

Let `ML_m` be the incidence graph between

\[
 {cal L}={{[2m-1]}\choose {m-1}},\qquad
 {cal M}={{[2m-1]}\choose m}.
\]

Both shores have size

\[
 W={2m-1\choose m}.
\]

The immediate-upper colour set is

\[
 {cal U}={{[2m-1]}\choose {m+1}},\qquad
 U=|{cal U}|,
\]

and

\[
 C=W-U={2W\over m+1}=\operatorname {Cat}_m.              \tag{1.1}
\]

Fix a perfect matching `M0` of `ML_m`.  For an incidence edge
`e=LU` outside `M0`, set

\[
 \operatorname {up}(e)=M_0(L)\cup U,
 \qquad
 \lambda(e):L\longrightarrow M_0^{-1}(U).                \tag{1.2}
\]

For a matching `Q` outside `M0`, the labelled links `lambda(Q)` form a
directed partial permutation.  We call them **graphic-independent** when
their underlying labelled undirected edges form a forest; isolated vertices
are retained when components are counted.

Let `P` be a protected incidence path bank.  Properly two-edge-colour it as

\[
                         P=P_0\mathbin{\dot\cup}P_1.       \tag{1.3}
\]

The reference matching will contain `P0`, and the variable matching will
contain `P1`.

## 2. Partial rooted Catalan forests

Fix an allowed exceptional upper-colour set `Z subset cal U`, with
`|Z|=t`.  A matching `Q0 subset ML_m-M0` is a **`Z`-partial rooted Catalan
forest** if

1. `up` maps `Q0` bijectively onto `cal U-Z`; and
2. `lambda(Q0)` is graphic-independent.

Consequently

\[
 |Q_0|=U-t=W-(C+t),                                      \tag{2.1}
\]

so its spanning link forest has exactly `C+t` components.  This identity is
why an allowed upper hole increases, rather than decreases, the initial
connector debt.

## 3. Exact bounded-hole decomposition

### Theorem 3.1 (partial Catalan forest plus connector forest)

Fix integers `t>=0` and `0<=s<=C+t`, a set `Z subset cal U` of size `t`,
and a perfect matching `M0`.  The following are equivalent.

1. There is a matching `Q subset ML_m-M0` such that
   
   \[
   |Q|=W-s,\qquad
   \operatorname {up}(Q)\supseteq{cal U}\setminus Z,      \tag{3.1}
   \]
   
   and `lambda(Q)` is graphic-independent.

2. There are matchings `Q0,Q1 subset ML_m-M0` whose union is a matching,
   such that

   * `Q0` is a `Z`-partial rooted Catalan forest;
   * `|Q1|=C+t-s`; and
   * after contracting every component of `lambda(Q0)`, the labelled links
     of `Q1` form a loopless forest.

Under either condition `Q=Q0 union Q1`.  If the graph induced after deleting
the endpoints of `Q` has a perfect matching `R` outside `M0`, then

\[
                           M_1=Q\mathbin{\dot\cup}R        \tag{3.2}
\]

is a perfect matching, `M0 union M1` has at most `s` components, and every
immediate-upper colour outside `Z` occurs.  Hence its actual immediate-upper
hole set is contained in `Z`.

#### Proof

Assume 1.  For each colour in `cal U-Z`, choose one carrying edge of `Q`;
call the selected set `Q0`.  It has `U-t` edges and inherits both the
matching and graphic-independence properties.  Thus it is a `Z`-partial
rooted Catalan forest.  Put `Q1=Q-Q0`.  Then

\[
 |Q_1|=(W-s)-(U-t)=C+t-s.                                \tag{3.3}
\]

Because `lambda(Q)` is a forest, every link of `Q1` joins two distinct
current components and the contracted links are a forest.

Conversely, a forest of links between distinct components of a forest has
acyclic union.  Thus `Q0 union Q1` satisfies (3.1), and (2.1) plus the
stated size of `Q1` gives `|Q|=W-s`.

If `R` exists, then (3.2) is a perfect matching disjoint from `M0`.  The
permutation `M0^{-1}M1` has as many cycles as the factor has components.
The `W-s` independent links already have graphic rank `W-s`; adding links
from `R` cannot lower rank.  Hence

\[
 c(M_0\cup M_1)
   =W-r_{\rm gr}(\lambda(M_1))
   \le s.                                                 \tag{3.4}
\]

Finally `Q0` already witnesses every colour outside `Z`.  This proves the
palette assertion.  \(\square\)

### Corollary 3.2 (protected version)

Theorem 3.1 preserves the protected bank `P` provided

\[
 P_0\subseteq M_0,\qquad
 P_1\subseteq Q_0\cup Q_1,                               \tag{3.5}
\]

and `R` is selected in the residual graph after all chosen endpoints and
the forbidden matching `M0` are removed.  Conditions (3.1), graphic
independence, and residual Hall are literal and separately checkable.  In
particular this corollary does not assume the factor whose existence it is
meant to prove.

## 4. Local packet damage versus connector damage

Let `P` be the union of `H` resource-disjoint sharp pivot-rich collared
paths.  One packet contributes `6h` protected incidence edges, so

\[
                            |E(P)|=6Hh.                   \tag{4.1}
\]

If `6Hh<=m-2`, the small protected-factor theorem supplies some spanning
owner/lower-`q1` factor containing `P`.  More strongly, inside every planted
packet the explicit source replacement transports every old interval-OR
witness at every width.  This is the exact statement

\[
                   \text{packet-local upper damage}=0.    \tag{4.2}
\]

Equation (4.2) does **not** say that an arbitrary completion covers the
global upper palette.  It says only that the packet edit itself does not
destroy an old occurrence.  The global completion may still omit `t`
immediate-upper colours, and the small protected-factor theorem gives no
useful bound on its number of components.

Now suppose the protected certificate of Corollary 3.2 exists.  Its factor
has `c<=s` cycles and at most `t` immediate-upper holes.  Since `P` is a
forest, no factor cycle is wholly contained in `P`; choose one incidence
edge outside `P` on every cycle and open there.  Each opening removes one
projected Johnson adjacency and therefore can destroy at most one further
immediate-upper colour.  The resulting path forest still contains `P` and
has

\[
 \begin{aligned}
   \text{path components} &\le s,\\
   \text{immediate-upper holes} &\le t+c\le t+s.          \tag{4.3}
 \end{aligned}
\]

Thus exact upper-transparent cuts are unnecessary for an additive result.
They would improve `t+c` to `t`, but the weakest sufficient ledger is
`s+t=O(H)`.

This seam bound concerns the immediate-upper row only.  New cross-seam
intervals may add witnesses, but no such unverified addition is credited.
Conversely, arbitrary-width upper witnesses, clipped residence flags, and
compiler cells crossing a seam require their own guards.

## 5. The fixed-`H` implication

### Theorem 5.1 (conditional fixed-`H` upper-decorated host)

Fix `H>=1`.  Suppose that for every sufficiently large `m` and every
resource-disjoint bank `P` of `H` sharp pivot-rich collared paths satisfying
(4.1), there is a protected certificate of Corollary 3.2 with

\[
                           s+|Z|\le \kappa H              \tag{5.1}
\]

for an absolute constant `kappa`.  Then `P` lies in a spanning
owner/lower-`q1` path forest with at most `kappa H` components and at most
`kappa H` immediate-upper holes.

#### Proof

Apply Theorem 3.1 and then open the factor as in Section 4.  Both bounds are
immediate from (4.3) and (5.1).  \(\square\)

For a formulation uniform also at `H=0`, replace the right side of (5.1) by
`kappa(H+1)`.

## 6. The exact missing extension hypothesis

The smallest noncircular missing assertion exposed by this reduction is:

> **Protected bounded-hole Catalan connector.**  For every fixed protected
> pivot path bank `P`, one can choose `M0`, a named set `Z`, a `Z`-partial
> rooted Catalan forest `Q0`, a contracted connector forest `Q1`, and the
> residual matching `R`, satisfying (3.3), (3.5), and `s+|Z|=O(H)`.

The four ingredients are genuinely coupled:

* upper occurrences choose `Q0`;
* matching capacities constrain `Q0 union Q1`;
* graphic independence constrains the connector links; and
* the unused endpoints must satisfy residual Hall.

The uniform fractional point, an unrestricted protected factor, or a local
zero-damage packet proves none of these integral correlations.  Requiring a
Hamilton factor or upper-transparent opening would be stronger than needed.

Even this missing assertion closes only the owner, lower-`q1`,
immediate-upper, and component/opening ledgers.  A regenerative theorem must
still add:

1. residence on the unprotected bulk and at all opened endpoints;
2. arbitrary-width upper witness preservation; and
3. one literal common compiler cap with its boundary cells.

Accordingly, Theorem 5.1 is the precise global upper-decorated connector
interface furnished by the pivot-rich packet theorem, not a proof of the
full additive-constant conjecture.

## 7. Dependency audit

The proof uses only:

1. the local packet and fixed-`H` planting statements in
   `MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`;
2. the small protected-factor and bounded-opening ledgers in
   `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`;
3. the rooted-link rank identity from
   `MATH_THEOREM_UPPER_DECORATED_NEAR_FACTOR_CATALAN_CONNECTOR_DECOMPOSITION_20260801.md`.

No Hamiltonicity, transparent-cut, all-width, common-cap, or regenerative
extension theorem is imported.
