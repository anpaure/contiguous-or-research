# Positive-resident joining of protected PBBS blocks is local; global completion is one one-sided age-Hall and chronology gate

**Date:** 2026-08-13  
**Status:** unconditional reduction.  It corrects the earlier use of
two-sided/biresident ages: the maximal candidate is nonempty already when
`d<R`, and it reconstructs the owner trace exactly when positive owner
runs have length at least `d+1`.  The local scheduling of
declared protected blocks is therefore strictly easier than previously
stated.  The ordinary protected-factor theorem still does not imply a
positive-resident global completion.  For a fixed first matching and a
fixed one-sided age state, the missing completion is exactly a residual
Hall system; one cyclic chronology additionally requires the usual subtour
conditions.  No typed-cap or global untouched-deck claim is made.

## 1. Positive residence is the exact source condition

Put

\[
                         q=d+1.                    \tag{1.1}
\]

Let `(T_i)` be a cyclic rank-`R` Johnson trace and define its maximal
depth-`d` candidate by

\[
 P_p=\bigcap_{a=0}^{d}T_{p-a}.                    \tag{1.2}
\]

Since `d<R`, every set in `(1.2)` is nonempty: along `d` Johnson
transitions at most `d` members of the first owner can be deleted.

### Lemma 1.1 (one-sided maximal-antecedent criterion)

One has

\[
                         \bigcup_{p=i}^{i+d}P_p=T_i
                         \quad\text{for every }i       \tag{1.3}
\]

if and only if every nonconstant cyclic **positive** coordinate run in
`T` has length at least `q`.

No lower bound on zero-gap lengths is required.

#### Proof

Fix a coordinate `x`.  If its positive owner run is the cyclic interval
`[a,b]`, then its support in `P` is exactly

\[
                         [a+d,b].                  \tag{1.4}
\]

This support is nonempty precisely when the run has at least `d+1=q`
owners.  In that case every length-`q` owner window based inside `[a,b]`
meets `(1.4)`, so `(1.3)` contains `x` exactly on its original positive
run.  A coordinate constantly one on the component is present in every
`P_p`, while a coordinate constantly zero is absent from every `P_p`.
Applying this coordinatewise proves both directions. \(\square\)

For every source interval of length at least `q`, `(1.3)` gives the
algebraic rematerialization identity

\[
 \bigcup_{p=a}^{b}P_p
 =\bigcup_{i=a}^{b-d}T_i,
 \qquad b-a+1\ge q.                               \tag{1.5}
\]

Thus positive residence is enough both for exact flat inversion by the
nonempty maximal candidate and for every owner-union witness already
present in the chosen chronology.
It does not assert that a new chronology retains every old PBBS witness.

## 2. Exact positive-only connector scheduling

Let

\[
 V_0=A,V_1,\ldots,V_\ell=B                       \tag{2.1}
\]

be a shortest rank-`R` Johnson path between two fixed exterior traces.
For `x in A`, let `lambda(x)` be its positive age at `A`, including `A`,
truncated at `q`; define the positive right age `rho(y)` at `B`
analogously.

Every `x in A-B` is deleted on one edge `p_x in [ell]`, and every
`y in B-A` is inserted on one edge `s_y in [ell]`.  The deletion and
insertion orders are independent permutations.

### Theorem 2.1 (exact one-sided seam test)

Assume every positive run wholly internal to the two exterior traces is
already of length at least `q`.  The joined trace is positive-`q`-resident
at the connector if and only if

\[
 \lambda(x)+p_x-1\ge q
       \qquad(x\in A-B),                           \tag{2.2}
\]

\[
 \ell-s_y+\rho(y)\ge q
       \qquad(y\in B-A),                           \tag{2.3}
\]

and

\[
 \lambda(z)+\ell-1+\rho(z)\ge q
       \qquad(z\in A\cap B)                       \tag{2.4}
\]

for every nonconstant run crossing the connector.

Equivalently, put

\[
 r_x=q+1-\lambda(x),
 \qquad
 u_y=\ell+\rho(y)-q.                               \tag{2.5}
\]

If `r_(1)<=...<=r_(ell)` and `u_(1)<=...<=u_(ell)` are the sorted
lists, legal orders exist exactly when

\[
                         r_{(i)}\le i\le u_{(i)}
                         \qquad(1\le i\le\ell),    \tag{2.6}
\]

together with `(2.4)`.

#### Proof

Before deletion, `x` occurs in its `lambda(x)` exterior owners and in the
additional connector owners `V_1,...,V_(p_x-1)`, giving `(2.2)`.  After
insertion, `y` occurs in `V_(s_y),...,V_(ell-1)` and then in its
`rho(y)` exterior owners, giving `(2.3)`.  A common coordinate occupies
the `ell-1` internal owners between the two endpoint ages, giving `(2.4)`.
These exhaust the coordinate types.

The deletion problem is a unit-job release schedule `p_x>=r_x`, feasible
exactly when the sorted releases satisfy the left half of `(2.6)`.  The
insertion problem is the dual unit-job deadline schedule, giving the right
half.  The two permutations may be paired independently edge by edge.
\(\square\)

At every Johnson cut the positive ages have the unit clipped-age property:
among present coordinates at most `s` have age at most `s`, because each
such run began at one of the last `s` insertion events.  Therefore the cut
form of `(2.6)` gives:

### Corollary 2.2 (positive aperture)

If both ports are Johnson cuts and

\[
                         \ell\ge q,                \tag{2.7}
\]

then a shortest connector ordering preserving every positive run exists.

#### Proof

Every release lies in `[q]`.  If the `i`-th smallest release satisfied
`r_(i)>i` for some `i<=q`, then at least `ell-i+1` deletion labels would
have left age at most `q-i`.  The unit clipped-age bound permits at most
`q-i` such labels, contradicting `ell>=q`.  For `i>q`, `r_(i)<=q<i` is
automatic.

Dually, deadline feasibility is equivalent to saying that at most `s`
insertion labels have deadline at most `s`, for every `s`.  The inequality
`u_y<=s` implies `rho(y)<=s+q-ell`; the right unit-age bound permits at
most `max(0,s+q-ell)<=s` such labels.  Thus both halves of `(2.6)` hold.
Finally `(2.4)` is automatic because `lambda,rho>=1` and
`ell>=q`. \(\square\)

This is the relevant aperture for the flat compiler.  The stronger
`ell>=2d+1` aperture is needed only when a later interface explicitly asks
to preserve zero gaps as well.

## 3. What the clipped-connector theorem closes for named blocks

Call a protected owner-path block **internally positive-safe** when every
positive run bounded wholly inside it has length at least `q`; shorter
nonconstant flags may meet only its two ports.

### Theorem 3.1 (conditional protected-block chain)

Take any finite ordered list of internally positive-safe protected blocks.
For every proposed joining segment, fix its two endpoints, equivalently its
deletion and insertion banks.  Suppose

1. the endpoint banks of every shortest Johnson-geodesic exit arm and
   entrance arm have size at least `q`; and
2. the endpoint banks of every shortest connector between successive far
   ports have size at least `q`.

Then all arm and connector event orders can be chosen so that their
concatenation is one internally positive-`q`-resident owner path.  Only its
two final exterior ports retain clipped positive flags.  If these scheduled
orders are additionally resource-disjoint from one another and from the
fixed blocks, the same chronology is a protected path.

#### Proof

On each exit arm, choose its deletion order from the release inequalities
exported by the fixed block and choose its insertion order arbitrarily.
No inserted coordinate is deleted again inside a shortest arm, so its run
is open at the far port.  Dually, on each entrance arm choose its insertion
order from the deadline inequalities imported by the fixed block and
choose its deletion order arbitrarily.  No coordinate deleted there was
inserted earlier inside that shortest arm.  Unit clipped ages and arm
length at least `q` make the constrained release/deadline schedules
feasible.

The complete exit trace now determines the positive left ages at its far
port, and the complete entrance trace determines the positive right ages
at its far port.  Apply Corollary 2.2 to the shortest connector between
them.  Coordinates common to its endpoints satisfy `(2.4)` automatically,
because their total crossing run has at least `q+1` owners after the two
endpoint ages are included.  The release condition handles every run
which closes on the connector, and the deadline condition handles every
run which opens there and later closes in the entrance arm or its fixed
block.  Runs wholly inside the fixed blocks are safe by hypothesis.  These
cases exhaust the coordinate types. \(\square\)

The theorem closes the **chronological scheduling of fixed endpoint
banks**.  A previously selected literal geodesic already fixes its event
order; changing that order can change its intermediate owners and facets.
Therefore mere existence of resource-disjoint unscheduled paths does not
by itself imply that the scheduled paths are resource-disjoint.  Avoidance
and residence must be co-selected, unless private signatures make resource
separation invariant under all permitted orderings.  The theorem does not
perform that co-selection for an arbitrarily large protected forest.  In
the present PBBS application:

* the compound low-spine path has no internally trapped short positive
  flag; its long bridges can absorb the exported flags;
* every clean paired backup halo is monotone and exports its nonconstant
  flags to its far ports; and
* the theorem removes the unnecessary zero-gap premise from joining these
  named blocks.

The remaining named-bank graph problem is to co-select the required event
orders with owner/lower disjointness and acceptable exposure.  Distinct
one-tag and pair-tag signatures make most cross-segment separation
automatic, and the existing one-tag theorem selects a clean system for
`O(sqrt R)` components.  It does not state the required positive-schedule
co-selection theorem for the full `O(d^3)` casualty bank and must not be
silently extrapolated to it.

## 4. Exact global positive-age Hall gate

Now fix a perfect first incidence matching `M_0` which contains the
declared first-phase incidences of every protected path.  On the rank-`R`
owner shore

\[
                         X={ [2R-1]\choose R},      \tag{4.1}
\]

write

\[
                         M_0(T)=T\setminus\{x_T\}. \tag{4.2}
\]

Its possible nontrivial successors are

\[
 T_y=T\setminus\{x_T\}\cup\{y\},
 \qquad y\notin T.                                \tag{4.3}
\]

A one-sided capped age state assigns to every `z in T` a value

\[
                         a_T(z)\in[q],             \tag{4.4}
\]

where `q` means "at least `q`".  Absent coordinates carry no age.

Define `D^+_(M_0,a)` on split tail and head copies of `X` by retaining
`T -> T_y` exactly when

\[
 a_T(x_T)=q,
 \qquad a_{T_y}(y)=1,                              \tag{4.5}
\]

and for every persistent coordinate `z in T\cap T_y`,

\[
                         a_{T_y}(z)=\min\{q,a_T(z)+1\}.  \tag{4.6}
\]

There is no condition on how long `y` was absent before its insertion.

Let `Q` be the forced successor matching induced by all already oriented
protected paths, and let `Z_Q,H_Q` be its tail and head sets.  Assume

\[
                         Q\subseteq D^+_{M_0,a}.     \tag{4.7}
\]

### Theorem 4.1 (positive-resident completion iff one Hall system)

For the fixed pair `(M_0,a)`, there is a simple spanning owner/lower
two-factor whose first phase is `M_0`, whose owner-age state is exactly
`a`, which contains `Q`, and in which every positive coordinate run has
length at least `q` if and only if

\[
 \boxed{
 |N_{D^+_{M_0,a}}(S)\setminus H_Q|\ge |S|
 \quad(S\subseteq X\setminus Z_Q).}               \tag{4.8}
\]

When `(4.8)` holds, the completion is integral.

#### Proof

Delete the forced tails and heads.  Extending `Q` is exactly a perfect
matching of the residual bipartite graph induced by `D^+_(M_0,a)`, and
Hall is `(4.8)`.  The matched successor of `T` uses the same lower facet
`M_0(T)`, so lifting the successor matching gives a second perfect
incidence matching disjoint from `M_0`.

On every successor cycle, a coordinate is born with age one, its age
increments on every persistent occurrence, and it can be deleted only at
age `q`.  Hence every finite positive run has at least `q` owners.  A
coordinate constant on a cycle may have age `q` throughout.  Conversely,
recording the capped ages of any positive-resident oriented factor with
age state `a` puts every successor arc in `D^+_(M_0,a)` and proves
`(4.8)`. \(\square\)

The unconditional event-label obstruction inherited from one residual
tail is therefore

\[
                         a_T(x_T)<q.               \tag{4.9}
\]

Such a residual tail has zero outdegree.  Even when `(4.9)` fails,
incompatibility with every prescribed target age vector can also give zero
outdegree.  Having only young **absent** coordinates is not by itself an
obstruction, because positive residence imposes no zero-gap waiting time
before an insertion.

The ordinary protected matching/factor theorem chooses `M_0` and an
unfiltered second matching.  It does not co-select a global age state and
does not prove `(4.8)`.  The exact completion problem is:

\[
 \boxed{
 \text{co-select }M_0\text{ and }a\text{ extending the protected profiles
 so that }(4.7)\text{ and }(4.8)\text{ hold}.}      \tag{4.10}
\]

## 5. One global chronology is a separate exact cut condition

Hall gives a successor permutation, not necessarily one cycle.  With
binary successor variables `z_(TT')`, one cyclic chronology is equivalent
to the matching equations, the forced equations for `Q`, and

\[
 \boxed{
 \sum_{T\in S,\ T'\notin S}z_{TT'}\ge1
 \quad(\varnothing\ne S\subsetneq X).}            \tag{5.1}
\]

Indeed `(5.1)` excludes every proper union of successor cycles.  Thus the
strongest exact global gate is the age-filtered matching-plus-subtour
system, not ordinary Hall alone.

Alternatively one may first obtain a positive-resident two-factor from
`(4.8)` and then fuse its cycles.  Such a fusion must preserve the full
owner/lower signature and pass the local connector inequalities of Section
2 at every new seam.  Degree restoration or an uncoloured component switch
does not imply this.

Even a one-cycle positive-resident completion does not automatically
retain the PBBS all-depth occurrence tower: the clean-halo theorem repairs
the named crossing casualties, while an arbitrary completion may discard
uncut old occurrences.  Their preservation or replacement is a further
chronology/deck condition on the same selected object.

## 6. The tight-wreath relative-graft alternative

Every clean paired package, including its two central paths and four halo
arms, is two collared arcs of one tight wreath row.  Consequently a
protected-row extension or a support-feasible exact row trade would make
that package automatically resident inside a full-aperture MSW row.

There is, however, no hereditary protected-row theorem.  At `m=3`, two
window-disjoint prescribed rows already have a residual exact-cover system
which is infeasible over the nonnegative rationals; see
`MATH_OBSTRUCTION_PROTECTED_TIGHT_WREATH_ROWS_NOT_HEREDITARILY_EXTENDABLE_20260813.md`.

Hence the relative MSW escape has the following exact form:

1. realize the tailored clean rows as positive supports of exact wreath
   trades whose negative supports are available in one resident factor;
2. choose those trades conformally, so their negative rows and positive
   rows are each pairwise disjoint; and
3. Hamiltonize/fuse the resulting row factor through positive-safe seams
   while preserving the protected arcs.

Item 1 is not implied by pairwise resource disjointness.  Item 3 is not
implied by endpoint-preserving MNW Hamiltonization: that theorem preserves
one MSW half but does not certify positive residence at every new seam or
the full PBBS upper/deep deck.

## 7. Exact frontier

The corrected order of proof is therefore

\[
 \boxed{
 \begin{gathered}
 \text{local positive scheduling}\quad\text{(Sections 2--3)},\\
 \text{co-selection with resource-disjoint joining of the named bank},\\
 \text{one-sided age-Hall completion }(4.8),\\
 \text{connected successor chronology }(5.1),\\
 \text{untouched/deep occurrence replacement and typed cap.}
 \end{gathered}}                                  \tag{7.1}
\]

The first row is closed at the endpoint-bank level.  The second row must
ensure that the schedule-compatible literal paths, not merely some paths
with the same endpoints, avoid every protected resource.
The first unresolved global carrier assertion is `(4.10)`, strengthened
by `(5.1)` when one source cycle is required.  Zero-gap residence should
not be reintroduced unless a separately named complement-dual interface
actually needs it.
