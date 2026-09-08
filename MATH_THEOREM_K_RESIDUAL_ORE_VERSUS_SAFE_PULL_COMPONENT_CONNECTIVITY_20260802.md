# Residual Ore expansion does not force a safe-pull component tree

**Date:** 2026-08-02  
**Lane:** K, prospective direct-new-phase pump/corridor planting  
**Status:** exact separation theorem, exact robust cut criterion, and exact
compatible-hypertree completion lemma.  No ambient Boolean pull-supply
theorem is claimed.

## 0. Outcome

The residual Ore--Ryser theorem closes the owner/lower-`q1` degree row after
the opened pump and the `O(d)` protected bank are fixed.  Its two opposite
Lovasz--Kruskal--Katona branches do **not** imply that any resulting cycle
factor has a connected auxiliary graph of history-/palette-safe pulls or
Boolean hexagons.

There are two independent missing correlations.

1. **Component-cut supply.**  A safe circuit has to use old factor edges on
   opposite sides of every nontrivial component cut.  This information is
   lost under the owner/lower incidence projection used by Ore--Ryser.
2. **Simultaneous or serial compatibility.**  Even if the graph of
   individually safe pulls is connected, two tree edges can use the same old
   factor edge or private resource.  Executing either then destroys the
   other.  Connectivity alone is sufficient only for a support-disjoint
   catalogue, or for a catalogue with a proved hereditary/noninterleaving
   pull property.

The exact positive replacement is a joint object:

> a residual two-factor containing the protected bank, together with a
> resource-compatible spanning `{2,3}`-hypertree of accepted pull/hex
> certificates on its physical components.

For an `h`-resource protected bank, the sharp robust component-cut statistic
is a transversal number.  For every component shore `S`, let the candidate
circuits crossing `S` carry their complete hazard sets.  Every bank of size
at most `h` leaves a crossing circuit if and only if the minimum resource
transversal of those hazard sets is greater than `h`.  The familiar
count/load sufficient condition

\[
       |\mathcal P_F(S)|>h\lambda_S
\tag{0.1}
\]

follows when one protected resource occurs in at most `lambda_S` candidates
across that cut.  Neither this transversal number nor even its positivity is
bounded by the LKK shore estimates.

Thus the proposed factor-first route is viable only with a new correlated
factor-plus-circuit theorem.  LKK supplies marginal factor existence, not
the required spanning pull tree.

## 1. Safe component circuits

Let `F` be a directed residual owner/lower two-factor containing the fixed
protected occurrence bank `Q`.  Write `C(F)` for its directed physical cycle
components.

A **binary pull certificate** `p` consists of an old selected phase
`O(p) subset F`, an accepted new phase `N(p)`, and its complete occurrence,
history, palette, upper-ticket, charge and private-resource ledger.  It is a
component pull if its old phase meets two distinct components and replacing
`O(p)` by `N(p)` merges those components.

A **ternary hex certificate** is defined similarly, with the old phase on
three distinct components and the standard Boolean-hex replacement merging
the three components into one.  Its component footprint has size three.

Let

\[
       \mathcal H_Q(F)
\tag{1.1}
\]

be the `{2,3}`-uniform multihypergraph on `C(F)` whose labelled hyperedges
are all accepted certificates disjoint from `Q`.  Parallel labels are kept:
they can have different hazards and different serial behaviour.

For `S subset C(F)`, let `P_F(S)` be the labelled certificates whose
component footprint meets both `S` and its complement.  A hypergraph is
connected exactly when

\[
   \mathcal P_F(S)\ne\varnothing
   \quad
   (\varnothing\ne S\subsetneq\mathcal C(F)).
\tag{1.2}
\]

This is a component-circuit cut, not an owner/lower Ore shore.

## 2. When a spanning circuit family really merges the factor

For a certificate `p`, let `supp(p)` contain every old/new occurrence and
every private resource whose use can invalidate another certificate.

Call a family `T` **private** if its supports are pairwise disjoint.  Call it
a **loose spanning `{2,3}`-hypertree** if its members can be ordered
`p_1,...,p_t` so that the first footprint starts the tree and every later
footprint meets the union of the earlier footprints in exactly one component
and introduces `|kappa(p_i)|-1` new components.  Equivalently,

\[
       \sum_{p\in T}(|\kappa(p)|-1)=|\mathcal C(F)|-1
\tag{2.1}
\]

and the displayed loose ordering spans all components.  Binary members are
ordinary tree edges; ternary members add two new component vertices.

### Theorem 2.1 (private pull/hex hypertree fusion)

If `T subset H_Q(F)` is a private loose spanning `{2,3}`-hypertree, toggling
its certificates produces one directed physical cycle and preserves every
resource row included in the certificate definition.

The same conclusion holds without support disjointness if the labelled
catalogue has the following hereditary property: after any prefix of the
loose order is toggled, every remaining certificate is still accepted with
the same resource ledger and the component topology obtained by contracting
the already merged components.

#### Proof

For a binary member, the exact pull identity merges its two current
components and lowers the component count by one.  For a ternary member, the
Boolean-hex identity merges its three current components and lowers the
count by two.  In the loose order, the old components of the next member are
distinct after all previous contractions: one lies in the accumulated
component and the others are new.  Hence its topology formula applies.

Private supports make the switches commute and preserve all declared
resource rows.  Under the hereditary alternative, apply them in the loose
order instead.  Equation (2.1) lowers the component count by exactly
`|C(F)|-1`, leaving one cycle.  \(\square\)

### Proposition 2.2 (connected individually-safe graph is insufficient)

There is a connected auxiliary pull graph with no compatible spanning tree.

#### Proof

Take three factor components `C_1,C_2,C_3`.  Let `p_12` and `p_23` be
individually accepted component pulls, but require both old phases to use one
common selected occurrence or one common unit-capacity private resource on
`C_2`.  The auxiliary graph is the path

\[
                       C_1-C_2-C_3.
\]

The two labels cannot be selected simultaneously.  Executing either pull
removes the common old occurrence (or consumes the common private token), so
the other is no longer accepted.  Thus the unique graph-theoretic spanning
tree is not a legal circuit family.  \(\square\)

Canonical GMN pulls avoid this example because their selected catalogue is
edge-disjoint and noninterleaving.  Arbitrary Boolean hexes do not inherit
that property merely from individual safety.

## 3. Sharp projection separation from Ore/LKK

### Theorem 3.1 (component-tag lift)

Projected owner/lower Ore--Ryser feasibility, including every LKK shore
inequality used in the residual extension theorem, does not imply even one
safe circuit across a component cut.

More precisely, let `F` be any projected residual two-factor with at least
two components, and let `Q subset F` be any protected bank, including an
`O(d)` bank.  There is a state/guard lift with exactly the same projected
factor, owner degrees, lower degrees, protected incidences, residual degrees
and same-shore codegrees, but whose accepted safe-circuit hypergraph has no
hyperedge meeting two components of `F`.

#### Proof

Give every selected occurrence of `F` the tag of its physical component.
Retain the same owner/lower incidence and every protected resource.  In the
lifted acceptance relation, admit a circuit certificate only when all of its
old ports, new ports and private return states carry one common component
tag.  All selected factor occurrences remain accepted.

Forgetting the tags recovers `F` literally.  Therefore every projected
degree, codegree, Ore--Ryser inequality and LKK calculation is unchanged.
But a certificate meeting two old components has two different tags and is
rejected.  Hence every hyperedge of `H_Q(F)` is a loop inside one component;
after loops are discarded its component graph is edgeless.  \(\square\)

This is a projection-separation theorem.  It does not assert that the
specific Boolean age/history table realizes arbitrary component tags.  It
proves that no argument using only the projected LKK/Ore conclusions can
establish safe-pull connectivity.  A Boolean-specific history correlation
must be used.

There is also a literal Boolean warning: the hex-free near-factor theorem
constructs an asymptotically complete four-resource body, even with a
protected physical cycle, having no applicable ternary old phase.  That
result is not an exact spanning residual factor and is not needed for
Theorem 3.1, but it rules out substituting generic density or high girth for
the missing correlation.

## 4. Exact protected-bank cut criterion

Fix a projected factor `F` and a pre-guard candidate catalogue.  For each
candidate `p`, let

\[
                         H(p)\subseteq\mathcal R
\tag{4.1}
\]

be the set of atomic protected resources which would block `p`.  History or
palette rejection which is not representable by a resource intersection is
incorporated first by deleting that candidate.

For a component shore `S`, define

\[
 \tau_F(S)=min\{|Z|: Z\subseteq\mathcal R,
                    Z\cap H(p)\ne\varnothing
                    \text{ for every }p\in\mathcal P_F(S)\}.
\tag{4.2}
\]

Use `tau_F(S)=infinity` if some crossing certificate has empty hazard set.

### Theorem 4.1 (sharp robust component-cut criterion)

Every protected bank `Q` of at most `h` atomic resources leaves the safe
component hypergraph connected if and only if

\[
                   \tau_F(S)>h
       \quad
       (\varnothing\ne S\subsetneq\mathcal C(F)).
\tag{4.3}

For one fixed bank `Q`, the exact condition is simply

\[
 \exists p\in\mathcal P_F(S): H(p)\cap Q=\varnothing
       \quad
       (\varnothing\ne S\subsetneq\mathcal C(F)).
\tag{4.4}
\]

#### Proof

The surviving hypergraph is disconnected exactly when some nontrivial
component shore has no surviving crossing certificate.  A bank blocks every
candidate across `S` exactly when it is a transversal of the hazard family
`{H(p):p in P_F(S)}`.  This proves both statements.  \(\square\)

### Corollary 4.2 (count/load sufficient condition)

Suppose, for a fixed shore `S`, every atomic resource belongs to the hazard
set of at most `lambda_S` crossing candidates.  Then

\[
                      |\mathcal P_F(S)|>h\lambda_S
\tag{4.5}
\]

implies `tau_F(S)>h`.  If (4.5) holds for every component shore, every
`h`-resource protected bank leaves the safe component hypergraph connected.

#### Proof

An `h`-set of resources can meet at most `h lambda_S` candidates.  \(\square\)

Condition (4.3) is sharp for connectivity.  To obtain one legal fusion it
must be combined with a private or hereditary spanning-hypertree condition
as in Theorem 2.1.

The word `sharp` here is scoped to the **fixed prepared catalogue**.  An
internal preparatory switch can create a new certificate crossing a cut
which was empty initially.  Thus an empty fixed-catalogue cut is a complete
no-go only for the static atlas, or for a move class proved closed under
within-shore toggles.  For a dynamic catalogue the exact termination row is:

> at every reachable accepted factor with more than one component, there is
> a safe switch which strictly coarsens its current component partition.

The nonnegative integer component count then proves termination.  A private
or hereditary spanning hypertree is the cleaner one-shot certificate and
does not require such dynamic regeneration.

## 5. The minimal strengthened residual theorem

The exact factor-first statement sufficient for the prospective pump route
is the following.

> **Protected residual factor with a compatible circuit basis.**  After the
> direct-new-phase three edges, opened pump and `O(d)` corridor bank are
> fixed, there exists a residual owner/lower two-factor `F` and a family `T`
> of accepted Boolean pulls/hexes such that:
>
> 1. `F` contains the protected bank and satisfies the exact residual
>    demands;
> 2. every old phase of `T` is contained in `F`;
> 3. `T` is private, or has a proved serial-hereditary acceptance order;
> 4. its component footprints form a loose spanning `{2,3}`-hypertree; and
> 5. the marked direct-new-phase contractions lie in the unique final
>    component with their endpoint/history state unchanged.

Theorem 2.1 then gives one marked physical cycle.  The existing residual
Ore theorem proves item 1 only.  Its protected-edge extension can force any
already chosen two-bounded `O(d)` incidence bank, but it neither chooses the
components containing those incidences nor proves items 2--4 after the
completion.  In particular, planting `O(d)` old pull edges does not by
itself plant a component tree: the completion may put several intended
ports on one component or may close a component cut without any accepted
certificate.

Thus the smallest genuinely new row is not another owner/lower shore.  It is
the joint factor--circuit-basis condition above, or quantitatively the
cutwise transversal condition (4.3) together with private/hereditary
certificate selection.  Upper shadows, residence outside the encoded
history state, integer background charge and the terminal compiler remain
separate.
