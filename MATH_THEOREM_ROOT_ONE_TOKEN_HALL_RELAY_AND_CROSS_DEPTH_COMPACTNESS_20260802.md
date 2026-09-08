# One-token Hall relays: exact nonaccumulation and the weakest cross-depth linkage

**Date:** 2026-08-02  
**Lane:** ROOT, regenerative pull-cell / screened predecessor completion  
**Status:** unconditional integral min--max theorem on one frozen accepted
slice and an unconditional finite-branching compactness theorem across
depths.  Physical realization of the relay on one global host remains an
explicit hypothesis.  No `B(k)+O(1)` conclusion is claimed.

## 0. Outcome

The screened unsaturated predecessor layer has a sharp deficit-one Hall
obstruction, and disjoint copies can replicate it.  This makes the phrase
“carry one casualty to the next depth” ambiguous: one token can prevent
**temporal** accumulation only after all simultaneous within-slice deficits
have already collapsed to one compatible Hall aperture.

This note gives the exact integral statement.

* On one frozen accepted predecessor table, a carried state token `x`
  repairs all roles iff adding one unit of capacity at `x` satisfies Hall.
  When the baseline deficiency is at most one, this says exactly that `x`
  lies in every deficit-one role neighborhood.
* The augmented matching uses one fewer capacity unit than is available.
  A state `y` can be exported as the next token iff deleting one unit at
  `y` leaves all Hall cuts valid.  This gives an exact directed relay
  relation `x => y`.
* Every repairable input has at least one output, so one token is conserved
  rather than consumed.  At a genuinely deficient slice it cannot be
  exported unchanged: the token must move in complete-state space.
* Across depths, add the literal suspension/quotient relation from an output
  state at depth `m` to an input state at depth `m+1`.  A single carried
  token survives exactly along a path in this layered relay graph.  Because
  every layer is finite, an infinite relay exists iff compatible paths of
  every finite horizon exist.  Left-totality for every state is strictly
  stronger and unnecessary.

This is the weakest matching-level linkage which kills accumulation.  It
also identifies the sharp quantifier boundary.  Separate frozen witnesses
at each depth, or one fractional pull-clock member at each depth, do not
give a layered path.  The token must include every field read by the next
transition, and the same frozen slice must supply the menus, histories,
addresses, upper support and input/output relation.

## 1. One frozen accepted slice

Let `I` be a finite role set and `V` a finite complete-state bank.  Role
`i` has a nonempty accepted predecessor menu `M_i subseteq V`.  “Accepted”
has the strong meaning from the screened protected-completion theorem: for
every `v in M_i`, the physical packet `v -> h_i` has already passed all
owner, named-payload, residence, upper-signature and protected-bank rows
declared in this slice.

Let

\[
                         b:V\longrightarrow\mathbb Z_{\ge0},
                         \qquad b(V)=|I|                         \tag{1.1}
\]

be the baseline tail-capacity vector.  For `J subseteq I`, put

\[
                         N(J)=\bigcup_{i\in J}M_i,
 \qquad
 \delta_b(J)=|J|-b(N(J)),                              \tag{1.2}
\]

and define the exact baseline deficiency

\[
                         \Delta_b=\max_{J\subseteq I}\delta_b(J). \tag{1.3}
\]

Hall's deficient form says that `Delta_b` is the minimum number of roles
left unmatched by the baseline capacities.

A carried **input capacity token** at state `x` changes the capacity vector
to

\[
                              b^x=b+{\bf1}_x.             \tag{1.4}
\]

This convention must be checked against the sign of the physical protected
boundary.  The theorem below applies only when the actual incoming sidecar
changes the predecessor-capacity row by exactly (1.4).

## 2. Exact one-token repair aperture

Let

\[
 \mathcal D_1(b)={J\subseteq I:|J|=b(N(J))+1}.        \tag{2.1}
\]

When this family is empty, interpret its neighborhood intersection as all
of `V`.  Otherwise put

\[
                         C_b=\bigcap_{J\in\mathcal D_1(b)}N(J). \tag{2.2}
\]

### Theorem 2.1 (one-token Hall repair)

The augmented capacities `b^x` match every role if and only if

\[
       |J|\le b(N(J))+{\bf1}_{x\in N(J)}
                         \qquad(J\subseteq I).          \tag{2.3}

Consequently:

1. if `Delta_b>=2`, no one-token repair exists;
2. if `Delta_b<=1`, a one-token repair exists at `x` exactly when

   \[
                              x\in C_b.                 \tag{2.4}
   \]

Thus, on the only repairable deficiency range `Delta_b<=1`, `C_b` is the
exact integral repair aperture of the frozen slice.

#### Proof

Clone each state `v` into `b(v)+1_(v=x)` capacity copies.  A matching of all
roles into those copies exists exactly under Hall's inequalities, which are
(2.3).

One added copy raises the capacity of any neighborhood by at most one, so a
cut of deficit at least two cannot be repaired.  Suppose `Delta_b<=1`.
Every baseline-valid cut stays valid.  A deficit-one cut becomes valid
exactly when its neighborhood contains `x`.  Requiring this simultaneously
for all members of `D_1(b)` is precisely (2.4).  \(\square\)

### Corollary 2.2 (replication is a within-slice obstruction)

Suppose `J_1,...,J_p` have pairwise disjoint neighborhoods and
`delta_b(J_t)=1` for every `t`.  Then

\[
                  \delta_b(J_1\cup\cdots\cup J_p)=p,    \tag{2.5}
\]

so at least `p` input capacity tokens are necessary.  In particular, one
token cannot repair disjoint copies of the screened-collar deficit-one
example.

#### Proof

Disjoint neighborhoods make `b(N(union_t J_t))` the sum of their
capacities, so the deficiencies add.  Apply Theorem 2.1.  \(\square\)

This is the first quantifier barrier.  A theorem saying “each primitive
collar has deficit at most one” does not imply `Delta_b<=1` for the complete
table.  One must prevent replicated deficient shores or prove that their
neighborhoods share one common repair state.

For later formulas, write

\[
 \mathcal R_b=\{x\in V:b+{\bf1}_x\text{ matches every role}\}. \tag{2.6}
\]

Theorem 2.1 says `R_b` is empty when `Delta_b>=2` and `R_b=C_b` when
`Delta_b<=1`.

## 3. Exact output aperture and relay relation

Fix `x in R_b`, so `b^x` matches all roles.  An output state must
correspond to an available capacity copy; put

\[
                         A_x=\{y\in V:b(y)+{\bf1}_{y=x}>0\}. \tag{3.1}
\]

Define

\[
 x\Rightarrow_b y
 \quad\Longleftrightarrow\quad
 b+{\bf1}_x-{\bf1}_y\ge0
 \text{ and all roles match into }b+{\bf1}_x-{\bf1}_y. \tag{3.2}
\]

Thus the input token is installed at `x`, the roles are matched, and the
unused capacity unit at `y` is exported.

### Theorem 3.1 (one-in/one-out relay min--max)

For `x in R_b` and `y in A_x`, the following are equivalent.

1. `x =>_b y`.
2. For every role set `J`,

   \[
   |J|\le b(N(J))+{\bf1}_{x\in N(J)}
                         -{\bf1}_{y\in N(J)}.           \tag{3.3}
   \]
3. No `b^x`-tight role set has a neighborhood containing `y`; explicitly,

   \[
   y\notin
      \bigcup_{J:\ |J|=b^x(N(J))}N(J).                \tag{3.4}
   \]

Consequently the exact output aperture is

\[
 O_b(x)=A_x-
      \bigcup_{J:\ |J|=b^x(N(J))}N(J).                \tag{3.5}
\]

It is nonempty for every repairable input `x`.

#### Proof

The equivalence of items 1 and 2 is Hall's theorem for the capacity vector
in (3.2).  Since `b^x` already satisfies Hall, subtracting one copy at `y`
can fail only on a set whose neighborhood contains `y`; it fails there
exactly when the augmented Hall slack was zero.  This proves items 2--3 and
(3.5).

Finally, `b^x(V)=|I|+1`.  Take any matching of all `|I|` roles.  It leaves
one capacity copy unused, say at `y`.  The same matching is feasible after
that copy is deleted, so `y in O_b(x)`.  \(\square\)

### Corollary 3.2 (a genuine deficit forces token motion)

If `Delta_b=1`, then

\[
                              x\not\Rightarrow_b x      \tag{3.6}
\]

for every repairable input `x`.

#### Proof

Deleting the same copy that was added returns the baseline vector `b`, which
does not match all roles when `Delta_b=1`.  \(\square\)

Thus “reuse the same aperture token” may mean reuse one protected physical
occurrence, but its complete Hall state must change.  Rank suspension of a
state without an actual output-to-input transition is not a regenerative
proof.

### Example 3.3 (the minimal forced relay)

Let two roles both have the singleton menu `{a}`, and let the baseline
capacities be `b(a)=b(c)=1`.  Then `Delta_b=1`,

\[
                         C_b=\{a\},\qquad O_b(a)=\{c\}. \tag{3.7}
\]

The input token at `a` supplies the second required copy of `a`; the unused
baseline copy at `c` is the forced output.  Repeating this same deficient
slice at every depth has a one-token infinite relay exactly when the literal
suspension contains `c_m -> a_(m+1)`.  The identity suspension
`c_m -> c_(m+1)` fails immediately because `c_(m+1)` is outside the next
repair aperture.  Taking disjoint copies of this two-role system gives
Corollary 2.2 and requires one simultaneous token per copy.

## 4. Physical interpretation and its limit

Suppose the fixed protected bank and the incoming sidecar have been oriented
so that their exact boundary changes the free-tail demand from `b` to
`b+1_x`.  Choose a physical packet for every role according to a matching
certifying `x=>_b y`.  Then the packet bank together with the protected bank
has the same boundary as the baseline system plus one outgoing capacity
token at `y`.  Every rolewise resource and guard compiled into the accepted
menus is preserved.

Indeed, if `m` is the fixed-head count and the protected-bank boundary is
`eta`, so that `b=m+eta`, the selected tail count is

\[
                         p=b+{\bf1}_x-{\bf1}_y.
\]

Hence the free packets plus the protected bank have boundary

\[
                         (m-p)+\eta={\bf1}_y-{\bf1}_x.  \tag{4.1}
\]

They have exactly the boundary of one directed complete-state relay from
`x` to `y` at the contracted predecessor interface.  They may still contain
additional balanced components; connectedness requires the separate
protected skeleton row.

This is a complete statement only at the frozen predecessor layer.  It does
not manufacture a physical source occurrence for the incoming copy, a
literal output port for the unused copy, or a suspension into the next
dimension.  Those are the cross-depth data below.  In particular, a state
which exists only as a marginal pull-clock type is not automatically a
capacity copy in (1.4).

## 5. Cross-depth relay graph

For every depth index `m>=m_0`, fix one finite accepted slice

\[
                    \mathfrak S_m=(I_m,V_m,(M_i^m),b_m). \tag{5.1}
\]

All data in a slice are frozen before its Hall relation is evaluated.  Let

\[
                    \Sigma_m\subseteq V_m\times V_{m+1}  \tag{5.2}
\]

be the **literal suspension relation**: `(y,x') in Sigma_m` means that the
outgoing physical token at state `y` is a legal incoming capacity token at
state `x'` in the next slice.  It includes every rail, root/aperture,
history, address, cap, upper-witness and sidecar field which the next slice
reads.  A rank or mask map alone is not `Sigma_m`.

Define a layered directed graph by

\[
x\longrightarrow_m x'
\quad\Longleftrightarrow\quad
x\in\mathcal R_{b_m},\quad
\exists y\in O_{b_m}(x): (y,x')\in\Sigma_m,\quad
x'\in\mathcal R_{b_{m+1}}.                            \tag{5.3}
\]

### Theorem 5.1 (weakest one-token nonaccumulation linkage)

Fix an initial input `x_(m_0)`.  A compatible relay through slices
`m_0,...,n` exists if and only if the layered graph (5.3) has a directed
path

\[
                         x_{m_0}\to x_{m_0+1}\to\cdots\to x_n. \tag{5.4}
\]

Along such a path exactly one capacity token enters and exactly one leaves
every slice.  Hence the predecessor Hall correction has cardinality one at
every depth and does not accumulate with `n`.

An infinite compatible relay from `x_(m_0)` exists if and only if paths
(5.4) exist for every finite terminal index `n`.  It is not necessary that
every state in every repair aperture have a successor.

#### Proof

For one edge of (5.3), choose `y in O_(b_m)(x)` and a matching certifying
`x=>_(b_m)y`; then apply its literal suspension `(y,x') in Sigma_m`.
Concatenating these choices proves the forward construction and conserves
one token slice by slice.  Conversely, read the input, unused output and
suspension from any claimed relay; Theorems 2.1 and 3.1 force exactly one
edge of (5.3) at every layer.

For the infinite assertion, form the rooted tree of all finite compatible
paths from `x_(m_0)`.  Every level is nonempty by hypothesis, and every node
has finite degree because `V_m,V_(m+1)` are finite.  Koenig's infinity lemma
gives an infinite branch.  The reverse implication is immediate by taking
prefixes.  \(\square\)

The word *compatible* is load-bearing.  Existence of some repaired slice at
each `m` does not imply nonempty levels in this path tree.  Likewise, if two
slice certificates with the same displayed mask have different hidden
addresses or histories, they are different vertices unless those fields are
proved irrelevant to the next transition.

### Corollary 5.2 (finite-horizon formulation)

For a proof of nonaccumulation it is sufficient, and under the Markov-
complete token convention necessary, to construct compatible frozen
certificates for every finite depth horizon with one common initial token.
This is weaker than a left-total induction theorem and equivalent to one
infinite regenerative spine.

## 6. Terminal repairs are paid once, not carried

Suppose the auxiliary relay of Theorem 5.1 closes every field exported to
the next depth.  At depth `m`, let a terminal physicalization have a repair
family `H_m` of word cost at most `c`, but do not include any `H_m`-defect in
the exported token state.  Then the terminal length bound at depth `m` pays
that repair once.  It is not summed over the preceding relay path.

This conclusion is false if an `H_m`-defect remains in a field read by
`Sigma_m`: it must then be added to the outgoing state, and the one-token
model no longer describes the recursion.  This is exactly the distinction
between terminal eviction and carried repair in the regenerative pull-cell
theorem.

## 7. Rebase on the newest inputs

### 7.1 Fractional pull-clock membership

The corrected pull-clock theorem now closes stationary literal trace
membership and every optimal rank marginal.  It does not bound `Delta_b`,
construct `C_b`, choose an integral relay edge, or identify an unused
complete-state capacity copy.  Theorem 2.1 shows the first genuinely
integral separator after fractional membership: the intersection of all
deficit-one occurrence neighborhoods.

### 7.2 Screened-collar predecessor obstruction

The screened hinge theorem makes owner chronology, arbitrary-width
owner-derived upper signatures and the local residence collar invariant
across a Boolean tail menu.  Its integral predecessor layer nevertheless
has a deficit-one Hall example at every depth, and disjoint copies replicate
it.  Corollary 2.2 is therefore sharp for the actual route: before asking for
cross-depth linkage, the chosen global table must prevent simultaneous
replication or make all deficient neighborhoods share one literal token.

The shielded two-cell macro theorem supplies nontrivial rectangles on a
root-distinct Middle-Levels owner path with at most one nonrectangular owner.
That is an owner/support projection theorem; it does not imply
`Delta_b<=1` for the complete-state table.

### 7.3 K17 calibration

The authenticated K17 work now contains a connected guard-valid full
immediate-upper circulation covering all `19,448/19,448` rank-ten colours.
Independent residence/deep-upper circuit descents also lower the positive
short-run debt substantially while preserving the scoped owner/q1 rows.
These are strong nonemptiness and mobility calibrations.

They are not a relay edge in (5.3).  The full-q1 certificate and a
residence-improved certificate may be different frozen slices; neither yet
exports one complete unused predecessor state, proves that its suspension
lies in the next repair aperture, or closes source/common-cap/compiler and
regeneration.  Combining their best scalar scores would reverse the
quantifiers in Theorem 5.1.

## 8. Exact remaining physical hypothesis

At the predecessor layer the accumulation problem is now completely
resolved by Theorems 2.1, 3.1 and 5.1.  A physical `B(k)+O(1)` theorem still
requires genuine existence of one layered path whose vertices satisfy, on
the **same frozen slice**:

1. at most one global predecessor deficiency and a nonempty repair aperture
   `C_b`;
2. one output `y in O_b(x)` physically realized by the selected packets;
3. a literal, Markov-complete suspension `(y,x') in Sigma_m` into the next
   repair aperture;
4. the global source/address/history, rooted upper, compiler and protected
   spanning-skeleton rows; and
5. bounded terminal repair fields which are not exported.

It is enough to prove these rows for every finite compatible horizon; no
uniform left-total statement is needed.  None of the five existence rows is
proved here.  In particular, this note proves exact nonaccumulation of one
integral Hall token, not an unconditional bound for `nu(k)`.

## 9. Independent audit target

The companion verifier

`scratch/audit_root_one_token_hall_relay_20260802.py`

independently enumerates small menu/capacity systems, compares the repair
aperture (2.2) and output aperture (3.5) with brute-force capacitated
matchings, checks output nonemptiness and forced token motion at genuine
deficiency one, and replays replicated disjoint deficient shores.  Its
result and hashes are recorded in the companion audit note after execution.
