# Antipodal ears have exact resident external halos, and the remaining gate is port packing

**Date:** 2026-08-06  
**Method:** literal Johnson-geodesic algebra and a quantifier audit; no
computation or search  
**Status:** unconditional asymptotic protected-skeleton theorem.  For the
central antipodal trace band, the first and last `d` swaps can be reserved
entirely in the external coordinates.  This discharges every split
`K`-residence flag, is locally palette-fresh, and leaves an exact uniform
geodesic of linear distance in the middle.  The inherited-port recurrence,
external coarea estimate, and local lemma select all central ears with
private full Ore halos.  Theorem 14.3 co-selects them with the existing
protected reservoir and low rolling-collar cycle and extends the joint bank
to a spanning `q1` two-factor.  The remaining gates are the subexponential
tail splices, arbitrary-width/residual chronology, and terminal cap.

## 1. Set-up

Let

\[
 K\mathbin{\dot\cup}E=[2m-1],\qquad |K|=m-1,\quad |E|=m,
 \tag{1.1}
\]

and let `A,B` be rank-`m` owners.  Write

\[
 T=A\cap E,\qquad T'=B\cap E,
 \tag{1.2}
\]

and

\[
 D=A-B,\qquad I=B-A,\qquad q=|D|=|I|=d_J(A,B).
 \tag{1.3}
\]

The external deletions and insertions are

\[
 D_E=T-T',\qquad I_E=T'-T.
 \tag{1.4}
\]

A monotone Johnson geodesic from `A` to `B` is specified by an ordering of
`D` and an independent ordering of `I`, swapping the two lists
coordinatewise.

Throughout this note `d` is the residence deadline.  The useful aperture
is

\[
             |D_E|\ge2d,\qquad |I_E|\ge2d.           \tag{1.5}
\]

For the antipodal ordering of
`MATH_THEOREM_ANTIPODAL_FOLDED_CUBE_LONG_EAR_REDUCTION_20260806.md`, (1.5)
holds after deleting only `2^{o(m)}` trace pairs: it is enough to retain
Gray representatives `S` with

\[
             2d+1\le |S|\le m-2d-1.                 \tag{1.6}
\]

Indeed, at a complement seam the two directional external differences
have sizes `|S|` and `m-|S|`.  At a seam
`bar S -> S triangle {e}` they have sizes
`|S|,m-|S|-1` or `|S|-1,m-|S|`.  The omitted binomial tails have size

\[
 2\sum_{j\le2d}\binom mj=2^{o(m)}                   \tag{1.7}
\]

at `d=O(sqrt(m))`.

## 2. Exact reserved-halo construction

Choose disjoint ordered sets

\[
 D_E^-,D_E^+\subseteq D_E,\qquad
 I_E^-,I_E^+\subseteq I_E,
 \tag{2.1}
\]

each of size `d`.  In the first `d` transitions, swap the ordered elements
of `D_E^-` for the ordered elements of `I_E^-`.  In the last `d`
transitions, swap the ordered elements of `D_E^+` for the ordered elements
of `I_E^+`.  Join the resulting two halo endpoints by an arbitrary monotone
geodesic on the remaining coordinates.

### Theorem 2.1 (resident external-halo factorization)

Under (1.5), the construction above gives a monotone Johnson geodesic

\[
 A=A_0,A_1,\ldots,A_q=B                              \tag{2.2}
\]

with all of the following properties.

1. No `K`-coordinate changes in the first or last `d` transitions.
2. Every split positive or zero `K`-flag at either endpoint is extended by
   at least `d` further owner positions.
3. If the endpoint witness blocks hold the external traces `T,T'`
   constantly for at least `d+1` positions, every external positive run
   and zero gap meeting the seam has length at least `d+1`.
4. Every owner and immediate lower or upper colour in either open halo is
   fresh relative to the retained internal owner and immediate palettes of
   the adjacent fixed-trace witness, apart from the intended shared
   endpoint owner.
5. After fixing the two halos, the middle segment is a monotone geodesic of
   distance

   \[
                         q_0=q-2d.                  \tag{2.3}
   \]

#### Proof

Condition (1.5) supplies the four disjoint external banks in (2.1).  Each
prescribed transition deletes and inserts one external coordinate, hence
is a Johnson edge and leaves the `K`-projection unchanged.  The unprescribed
coordinates form equal deletion and insertion banks of size `q-2d`, so an
arbitrary ordering of those banks completes a monotone geodesic.  This
proves (1) and (5).

A split endpoint `K`-flag asks only that the endpoint membership bit remain
unchanged for some number at most `d` of subsequent or preceding owner
positions.  Since the `K`-projection is constant throughout each halo,
all such flags are discharged.  This proves (2).

An external coordinate is constant on each adjacent witness block.  Along
the monotone ear it changes at most once: a coordinate in `T-T'` is deleted
once, one in `T'-T` is inserted once, and a coordinate in `T cap T'` or
outside `T union T'` never changes.  Hence every run or gap meeting an ear
endpoint contains a complete adjacent witness block unless it is the bit
which changes immediately there; in that case the run or gap on the other
side contains the other complete witness block.  Either way its length is
at least `d+1`.  This proves (3).

Within a fixed-trace witness, every owner and both immediate colours have
external trace exactly `T` (or exactly `T'` at the other end).  At a halo
edge with current external trace `S`, deleting `x in E` and inserting
`y in E` gives external traces

\[
             S-\{x\},\qquad S+\{y\}                 \tag{2.4}
\]

for its lower and upper colours.  Neither is the current owner trace.
Monotonicity also prevents a proper intermediate trace from returning to
`T` or reaching `T'` early.  Thus no open-halo owner or palette role can
equal a retained role of the adjacent fixed-trace witness.  The owners and
palettes inside one monotone geodesic are themselves distinct: the numbers
of completed deletions and insertions strictly increase.  This proves (4).
\(\square\)

The theorem is stronger than a qualitative residence assertion.  It
factors every central seam into

\[
 \boxed{\text{deterministic resident halo of length }d}
 \;\cdot\;
 \boxed{\text{free geodesic of distance }q-2d}
 \;\cdot\;
 \boxed{\text{deterministic resident halo of length }d}.
 \tag{2.5}
\]

For the endpoint pairs in the antipodal theorem, `q>=m-2`; hence

\[
                         q_0\ge m-2-2d.             \tag{2.6}
\]

## 3. The exact aperture survives halo conditioning

Fix the two ordered halos.  Choose the orders of the remaining deletion
and insertion banks independently and uniformly.

### Theorem 3.1 (conditioned middle aperture)

At distance `s` into the free middle segment, every compatible owner has
probability

\[
                         {1\over\binom{q_0}s^2}.      \tag{3.1}
\]

Every compatible immediate lower or upper colour at its transition from
level `s` to `s+1` has probability

\[
              {1\over\binom{q_0}s\binom{q_0}{s+1}}. \tag{3.2}
\]

#### Proof

After the halos have been removed, the remaining deletion and insertion
orders are independent uniform permutations of two `q_0`-sets.  An owner
at level `s` specifies their two unordered prefix `s`-sets.  A lower or
upper colour specifies prefix sets of sizes `s,s+1` in the two possible
orders.  The same counting as the unconditioned random-geodesic aperture
gives (3.1)--(3.2).  \(\square\)

Thus residence costs exactly `2d` swaps and no exponential factor in the
central random aperture.  Since `d=o(m)`, every middle layer at linear
distance from its ends still has `2^{2m-o(m)}` effective owner and palette
choices.

## 4. Arbitrary inherited ports eliminate the two-port quantifier

Lemma 2.1 of the antipodal folded-cube theorem chooses minimum-intersection
ports separately for each seam.  That formulation creates an unnecessary
quantifier: the independently requested incoming and outgoing owners need
not be the two ports of the same retained witness.

The minimum-intersection condition is much stronger than needed.  Linear
Johnson distance already leaves exponential middle aperture.

### Theorem 4.1 (inherited-port dwell recurrence)

Let `T_0,...,T_(N-1)` be the cyclic almost-antipodal trace order.  Given an
arbitrary incoming `K`-port

\[
 P_i\in\binom K{m-|T_i|},                            \tag{4.1}
\]

there is a cyclic order of `K` whose first window of that size is `P_i`.
Open its full cyclic-window dwell at an edge incident with `P_i`.  The
other endpoint `P_i'` is an adjacent window.  Use

\[
 A_i=T_i\cup P_i',\qquad B_i=T_{i+1}\cup P_{i+1}     \tag{4.2}
\]

as the endpoints of ear `i`.  Then every two ports are physical ports of
one dwell, and

\[
                         d_J(A_i,B_i)\ge {m\over2}-2. \tag{4.3}
\]

Consequently, after the two external residence halos, every free middle
distance satisfies

\[
                         q_{0,i}\ge {m\over2}-2-2d
                                  =\Omega(m).        \tag{4.4}
\]

This recurrence closes cyclically after choosing all `P_i`, including
`P_0`, in advance.

#### Proof

Any prescribed subset of a finite set occurs as a consecutive window in
some cyclic order: list its members first and its complement second.  Thus
the dwell beginning at `P_i` exists, and opening the incident cyclic edge
gives an adjacent physical outgoing port `P_i'`.  This proves physical
two-port realization for every trace, with no compatibility condition on
the incoming port selected by the previous ear.

For consecutive almost-antipodal traces, their external intersection has
size at most one.  Their two trace sizes sum to `m`, `m-1`, or `m+1`.
Therefore their two `K`-port sizes also sum to `m`, `m+1`, or `m-1`, and

\[
 |P_i'\cap P_{i+1}|
 \le\min(|P_i'|,|P_{i+1}|)\le {m+1\over2}.          \tag{4.5}
\]

It follows that

\[
 |A_i\cap B_i|\le1+{m+1\over2}\le {m\over2}+2.
\]

Since both owners have rank `m`, this is (4.3).  Subtracting the `2d`
reserved transitions gives (4.4).  The construction is cyclic because
the last ear is simply prescribed to end at the already chosen `P_0`.
\(\square\)

Thus the earlier seamwise minimum-intersection ports may be discarded.
The price is only a change from distance `m-O(1)` to distance
`m/2-O(1)`, which leaves `2^{\Omega(m)}` owner and palette aperture at
every linear middle layer.

## 5. Why ambient cardinality alone cannot pack the endpoints

The comparison

\[
 O(m2^m)\quad\hbox{used roles}\qquad\hbox{versus}\qquad
 2^{2m-o(m)}\quad\hbox{ambient roles}                \tag{5.1}
\]

is not an endpoint-halo proof.

### Proposition 5.1 (linear-size endpoint-facet blocker)

Fix any bank of `N` oriented owner pairs `(A_i,B_i)` with
`q_i=d_J(A_i,B_i)`.  There is a forbidden lower-palette bank of size at
most

\[
                         \sum_i q_i                 \tag{5.2}

which blocks every monotone Johnson geodesic from every `A_i` to `B_i` at
its first transition.

In particular, for `N=Theta(2^m)` and `q_i=Theta(m)`, only
`O(m2^m)` forbidden roles suffice.

#### Proof

For every `i`, put into the forbidden bank all lower facets

\[
                         A_i-\{x\},\qquad x\in A_i-B_i.       \tag{5.3}

The first transition of any monotone geodesic must delete one
`x in A_i-B_i`; its lower colour is precisely the corresponding member of
(5.3), independently of which insertion is paired with that deletion.
Thus every first transition is blocked.  The union has size at most
`sum_i q_i`.  \(\square\)

This is not a counterexample to the inherited-port recurrence of Theorem
4.1: changing `P_i` changes the endpoint `A_i` and its facet bank.  It is a
sharp counterexample to any proof which freezes the recurrence and then
invokes only the global density comparison (5.1).  Incoming ports and
their first palette tickets must be selected before, or together with, the
protected background.

## 6. Interim sharpened ear gate

The forced noncyclic `K`-profile problem has therefore split into two
precise statements.

1. **Closed here:** on the central antipodal band, all positive/zero
   endpoint residence flags and all local fixed-trace palette collisions
   are discharged by two explicit external halos.  The remaining random
   core has distance `Omega(m)` and exact aperture (3.1)--(3.2).
2. **Closed here:** arbitrary inherited incoming ports extend to physical
   two-port dwells, and all free middle distances remain `Omega(m)`.
3. **Open at this point of the proof:** choose the inherited ports and two external halos so
   that their owner, lower, and upper roles are private relative to one
   another and the protected reservoir; then pack the free middle
   geodesics.

The `2^{o(m)}` traces outside (1.6) may be left to the existing rolling
collar/bridge reserve.  They do not affect the exponential central packing
scale.

The essential gain at this stage is that residence is no longer entangled
with the random middle-ear selection.  Proposition 5.1 shows why a bare
universe-size comparison cannot finish the private-port problem.  Sections
8--14 subsequently solve it by external fork separation, coarea spread,
and the local lemma.

## 7. Interim scope (superseded by Sections 11--15)

Proved:

1. an exact external-halo schedule for every retained antipodal seam;
2. simultaneous positive- and zero-residence extension at both ports;
3. local owner/lower/upper palette freshness relative to the adjacent
   fixed-trace witnesses;
4. exact post-conditioning random-geodesic probabilities; and
5. a sharp `O(m2^m)` endpoint blocker showing why ports must be selected
   jointly; and
6. a first random draw with only polynomially many colliding macros.

Not yet proved at this point:

1. reinsertion of the polynomial collision leave with fresh ports;
2. compatibility with the PBBS whole-fan bank or terminal cap; or
3. `nu(k)<=B(k)+O(1)`.

## 8. Adjacent ears have a deterministic external fork separator

There is one local dependence in the inherited-port recurrence: the two
ears incident with the same dwell use adjacent `K`-ports.  It can be
removed at the external-trace level.

Away from the `2^{o(m)}` deleted-tail splice positions, the antipodal word
has the exact fork identity

\[
             |T_{i-1}\mathbin\triangle T_{i+1}|=1.  \tag{8.1}
\]

Indeed, at `T_i=R_i` its two neighbours are
`bar R_(i-1),bar R_i`, and at `T_i=bar R_i` they are
`R_i,R_(i+1)`.

### Lemma 8.1 (two-coordinate fork tag)

At a central fork (8.1), the two incident external halos may be chosen so
that, except for their intended common dwell endpoint, no owner, lower
colour, or upper colour of one incident ear equals a role of the other.

#### Proof

Let `e` be the unique coordinate on which `T_(i-1),T_(i+1)` differ.  One
of those two traces agrees with `T_i` at `e`, and the other does not.  Call
the corresponding branches the agreeing and disagreeing branches.

On the disagreeing branch, flip `e` in its first external swap.  Pair it
with a coordinate `f` of the opposite swap direction.  Such an `f` exists
because both directional external difference banks have size at least
`2d`.  Since the two far traces differ only at `e`, the agreeing branch
must eventually flip `f` in the same direction.  Delay that flip until its
last external swap, and never flip `e` on that branch.

Relabel the two bits so their values at `T_i` are `(1,0)`.  The first edge
on the disagreeing branch has

\[
 \begin{array}{c|ccc}
 &\text{new owner}&\text{lower}&\text{upper}\\ \hline
 (e,f)&(0,1)&(0,0)&(1,1).
 \end{array}                                          \tag{8.2}
\]

Every later owner and internal palette role on that branch has `e=0`.
Every role on the agreeing branch has `e=1`.  Hence only the first upper
role in (8.2) could meet the agreeing branch.  But that branch has `f=0`
until its last external swap.  Once it has `f=1`, its external trace is
within one swap of `T_(i-1)` or `T_(i+1)`, whereas the exceptional upper
trace in (8.2) is within one insertion of `T_i`.  Those traces have Hamming
distance at least `m-O(d)>0`.  They cannot be equal.  If the flip of `e`
is an insertion rather than a deletion, complement the two displayed bits;
the same argument applies with lower and upper interchanged.  \(\square\)

Thus local endpoint saturation does not create an exponential family of
bad adjacent ears.  All remaining collision pairs involve macros whose
port variables are disjoint.

## 9. A polynomial external-load law

Choose every incoming port `P_i` uniformly from its `K` layer, choose the
incident outgoing dwell edge uniformly, and choose a cyclic order of `K`
uniformly subject to those two windows.  At every ear use the fork tags and
the two reserved halos above.

In the free middle, prescribe only the **type word** of swaps.  Pair as
many external deletions with external insertions as possible, pair the
unbalanced external changes with opposite `K` changes, and pair the
remaining `K` changes together.  Order the unbalanced changes so that the
external rank stays between its two endpoint ranks.  Within every type,
choose the coordinate orders uniformly.

For a physical role `X`, write `tr_E(X)=X cap E`.

### Lemma 9.1 (rank-monotone almost-complement load)

For each of the three role ranks `m-1,m,m+1` and every external trace
`S`, the total expected number of roles in the complete random dwell-and-ear
bank having external trace `S` is at most `m^C` for one absolute constant
`C`.

Conditional on `tr_E(X)=S`, the `K`-projection of any one role is uniform
on the layer of the required size.

#### Proof

First consider exact complementary endpoints on a free external ground set
of size `M`.  Fix a start rank `u` and a transition profile which has
deleted `alpha` old coordinates and inserted `beta` new coordinates.  For
a fixed resulting trace `S` of size

\[
                         s=u-\alpha+\beta,
\]

sum its occurrence probability over all rank-`u` starts.  There are

\[
 \binom s\beta\binom{M-s}\alpha
\]

compatible starts, and each contributes

\[
 {1\over\binom u\alpha\binom{M-u}\beta}.
\]

Cancellation gives the exact identity

\[
 {\binom s\beta\binom{M-s}\alpha
  \over\binom u\alpha\binom{M-u}\beta}
 = {\binom M u\over\binom M s}.                    \tag{9.1}
\]

The type word keeps `s` between `u` and `M-u`.  Binomial unimodality and
symmetry therefore make (9.1) at most one.

An almost-complement pair has at most two common or commonly absent
coordinates.  Group by those named coordinates, by start rank, by
`(alpha,beta)`, and by whether the role is an owner, lower colour, or upper
colour.  After deleting the named exceptional coordinates, (9.1) applies
verbatim to owners.  A lower or upper trace differs from its incident owner
trace by at most one coordinate, so the adjacent binomial ratio costs at
most another polynomial factor.  There are only polynomially many groups
and at most `O(m)` positions per macro.  Restricting from all possible
starts to the actual trace order can only decrease every nonnegative sum.
This proves the polynomial external-load bound.  A dwell contributes only
`O(m)` roles to its unique external trace and is absorbed by the same
bound.

Finally, the port/cyclic-order/geodesic law is invariant under every
permutation of `K`.  The symmetric group is transitive on every fixed-size
`K` layer.  Conditioning on the external trace and hence on the required
`K` size therefore gives the asserted uniform law.  \(\square\)

The content of (9.1) is the cancellation missing from the raw birthday
heuristic: although there are exponentially many ears, only polynomial
expected load reaches one named external trace.

## 10. Birthday alteration leaves only polynomially many bad macros

Call a pair of nonintended equal owner, lower, or upper roles a collision.
The adjacent pairs handled by Lemma 8.1 and the intended shared chronology
endpoints are not collisions.

### Theorem 10.1 (polynomial collision alteration)

There is a realization of the random inherited-port/dwell/ear bank with at
most `m^C'` collision pairs, for an absolute constant `C'`.  Deleting every
trace macro incident with a collision removes only `m^C'` macros and leaves
all remaining owners and both immediate palettes globally distinct.

#### Proof

Nonlocal role pairs use disjoint incoming-port, cyclic-order, and
middle-geodesic variables, hence their laws are independent.  Among role
pairs whose variables overlap, the only possible nonintended cases are:
the two ears incident with one dwell, handled by Lemma 8.1, and one ear
against its adjacent fixed-trace dwell, handled by Theorem 2.1.  Consecutive
dwells have different external traces.  All other role pairs are included
in the independent calculation below (even if their macro indices happen
to be adjacent).

Let `Lambda_0(S)` be the total expected owner load at external trace `S`.
Conditional `K`-uniformity gives

\[
 \mathbb E C_0
 \le {1\over2}\sum_{S\subseteq E}
       {\Lambda_0(S)^2\over
        \binom{m-1}{m-|S|}}.                       \tag{10.1}
\]

By Lemma 9.1, `Lambda_0(S)<=m^C`.  The exact layer ratio is

\[
 \sum_{s=1}^m {\binom ms\over\binom{m-1}{s-1}}
 =m\sum_{s=1}^m{1\over s}=O(m\log m).              \tag{10.2}
\]

Thus (10.1) is polynomial.

For lower colours the relevant `K` layer has size
`binom(m-1,s)`, and

\[
 \sum_{s=0}^{m-1}{\binom ms\over\binom{m-1}s}
 =m\sum_{j=1}^m{1\over j}=O(m\log m).              \tag{10.3}
\]

For upper colours it has size `binom(m-1,s-2)`, and

\[
 {\binom ms\over\binom{m-1}{s-2}}
 ={m(m+1-s)\over s(s-1)}
\qquad(2\le s\le m),                               \tag{10.4}
\]

whose sum is `O(m^2)`.  The same argument therefore bounds expected lower
and upper collision pairs by a polynomial.  Summing the three bounds gives

\[
                         \mathbb E C_{\rm all}=m^{O(1)}.       \tag{10.5}
\]

Some realization has at most twice this expectation.  Removing both
macros incident with every collision removes at most twice the number of
collision pairs and leaves a collision-free retained bank.  \(\square\)

This theorem replaces an exponential simultaneous-packing problem by a
polynomial alteration problem.  It does **not** yet reinsert the deleted
macros.  The exact remaining statement is:

> **Polynomial repair lemma.**  Against the fixed collision-free good bank,
> reprepare and insert `m^{O(1)}` deleted dwell-and-ear macros, preserving
> the two external halos, the PBBS protected bank, and the cyclic
> chronology.

The good bank has only `2^{m+o(m)}` roles, while each repaired free middle
has linear distance and exponential aperture.  Proposition 5.1 still
forces the repair to choose its new incoming port and first facet jointly;
one may not freeze a blocked old port and appeal only to middle randomness.

The polynomial repair clause is lineage only: Theorem 11.2 below
supersedes it by selecting a collision-free internal bank directly.

## 11. In fact the internal collision leave can be removed by the local lemma

The polynomial alteration theorem is useful as a robust fallback, but its
repair lemma is unnecessary for collisions internal to the antipodal bank.
The pointwise load, rather than merely total expected collisions, satisfies
the local-lemma criterion.

Let

\[
 N_*:=\binom{m-1}{2d-1}.                            \tag{11.1}
\]

Every owner, lower, and upper role in the retained central band has a
`K`-projection lying in a layer of size at least `N_*`.  At
`d=Theta(sqrt(m))`,

\[
                         N_*=m^{\Omega(d)}.          \tag{11.2}
\]

### Lemma 11.1 (uniform point load)

For every fixed physical owner, lower colour, or upper colour `X`, the sum
over all random nonlocal roles `Y` of

\[
                         \Pr(Y=X)
\]

is at most `m^C/N_*`.

#### Proof

Fix `S=tr_E(X)`.  Lemma 9.1 bounds the total expected number of roles with
external trace `S` by `m^C`.  Conditional on that trace, every compatible
`K`-projection is uniform on a layer of size at least `N_*`.  Summing the
point probabilities gives the claim.  \(\square\)

### Theorem 11.2 (collision-free internal antipodal ear bank)

For all sufficiently large `m`, the inherited-port antipodal dwell-and-ear
bank has a realization in which every owner and both immediate palettes
are globally distinct, apart from intended shared consecutive endpoints.
All endpoint residence flags remain discharged.

#### Proof

Use independent base variables for every incoming port and cyclic dwell
order, and for every free middle deletion/insertion order.  Consider a bad
event for each nonintended equality of roles belonging to two different
objects.

No bad event is needed for two dwells: their exact external traces are
different.  An ear and either incident dwell are locally fresh by Theorem
2.1.  The two ears incident with one dwell are disjoint by Lemma 8.1.
Every remaining compared object pair uses disjoint base variables and is
independent.

One dwell or ear contains `O(m)` roles.  Therefore, after fixing an
arbitrary realization of one object, Lemma 11.1 and a union bound give

\[
 \sum_{Y\ne X}\Pr(\text{the fixed object collides with object }Y)
 \le \varepsilon_m,
 \qquad
 \varepsilon_m:={m^{C+1}\over N_*}=o(1).            \tag{11.3}
\]

Let `B_e` range over the object-pair collision events and put
`p_e=Pr(B_e)`.  Two events are independent unless their two object pairs
use base variables at cyclic distance at most one.  Consequently the sum
of `p_f` over the dependency neighbourhood of any `B_e` is at most
`C_0 epsilon_m` for an absolute constant `C_0`: there are only constantly
many endpoint-variable incidences, and (11.3) applies at each one.

Set `x_e=2p_e`.  For all sufficiently large `m`,

\[
 \sum_{f\sim e}x_f\le2C_0\varepsilon_m<\frac12.
\]

Hence

\[
 x_e\prod_{f\sim e}(1-x_f)
 \ge2p_e\left(1-\sum_{f\sim e}x_f\right)
 \ge p_e.
\]

The asymmetric Lovasz local lemma selects all base variables with no bad
event.  The deterministic halo and fork constraints were built into every
sample, so residence survives.  \(\square\)

Theorem 11.2 closes the owner/lower-`q1`/upper-`q1` packing **inside** the
antipodal common-core bank.  It does not by itself prove disjointness from
an arbitrary externally frozen protected bank.  For composition, it is
enough that the external bank obey the same polynomial trace-load bound,
or that it be co-selected under the existing full-halo separation theorem.

## 12. The complete low rolling-collar cycle can be avoided simultaneously

The externally protected low-target cycle is small enough that no
trace-spread hypothesis is needed.  Let `J` be the one-cycle rolling-collar
bank for all targets of rank at most `d`.  Its full owner/lower/upper role
set has size

\[
 |R(J)|\le m^{O(1)}\sum_{j=1}^d\binom{2m-1}j
 \le m^{O(1)}\left({2em\over d}\right)^d.           \tag{12.1}
\]

### Theorem 12.1 (low-cycle relative avoidance)

The collision-free realization in Theorem 11.2 may be chosen with every
owner and both immediate palettes disjoint from `J`.

#### Proof

For one random central macro and one fixed resource of `J`, every possible
equality has probability at most `1/N_*`: after its external trace is
specified, the random `K`-projection is uniform on a layer of size at least
`N_*`.  A macro has `O(m)` roles.  Therefore the unary bad event that one
macro meets `J` has probability at most

\[
 \delta_m\le {m^{O(1)}|R(J)|\over N_*}.             \tag{12.2}
\]

Use the elementary lower bound

\[
 \binom{m-1}{2d-1}\ge
 \left({m-1\over2d-1}\right)^{2d-1}.                \tag{12.3}
\]

At `d=Theta(sqrt(m))`, (12.1)--(12.3) give

\[
 \log\delta_m
 \le-d\log(m/d)+O(d)\longrightarrow-\infty.       \tag{12.4}
\]

Thus `delta_m=o(1)`.  Add the unary avoidance events to the local-lemma
system of Theorem 11.2.  One unary event shares base variables with only a
constant number of object rows; its dependency-neighbourhood sum is
`O(epsilon_m+delta_m)=o(1)`.  The same `x=2p` proof applies and avoids all
unary and pair-collision events simultaneously.  \(\square\)

This composes the complete low source bank with the central antipodal
common-core chronology at owner and immediate-palette level.  It still
does not install the arbitrary-width PBBS occurrence bank or terminal cap.

## 13. The local lemma survives the full protected-Ore halo

For a protected path bank `H`, let its **Ore halo** contain

1. every protected owner and lower colour;
2. every lower facet of a protected owner;
3. every owner containing a protected lower colour;
4. every protected immediate-upper colour; and
5. the bounded endpoint-neighbour tags used to distinguish private from
   exceptional endpoints.

One central dwell-and-ear macro has `O(m)` incidences, so its Ore halo has
size `O(m^2)`.

### Lemma 13.1 (halo trace spread)

The external schedules and `K` variables in Theorem 11.2 may be selected
so that all nonlocal Ore halos of the central bank are disjoint.  The
conditional `K` fibre in the halo local-lemma instance has size at least

\[
                         B_m=\binom{m-1}{2d-2}.      \tag{13.1}
\]

#### Proof

Every added halo role is obtained from a base owner, lower colour, or upper
colour by adding or deleting at most one coordinate and by choosing one of
at most `m` such coordinates.  Therefore its external trace differs from a
base trace in at most one coordinate.  Lemma 9.1, summed over the at most
`m+1` adjacent external traces and the at most `m` local choices, still
gives polynomial maximum external load.

Its `K` size differs by at most one from a base role.  On the central band
all such sizes lie between `2d-2` and `(m-1)-(2d-2)`, proving (13.1).
Conditional `K`-uniformity is unchanged by marking which local facet or
cofacet is used, because the marked law remains `Sym(K)`-equivariant.

One macro now affects `O(m^2)` formal roles instead of `O(m)`.  This only
multiplies the numerator in (11.3) and the dependency degree by a
polynomial.  Since `B_m=m^{Omega(d)}`, the local-lemma parameter remains
`o(1)`.  Exclude the intended overlaps between consecutive chronology
objects; every other halo equality is a bad event.  The proof of Theorem
11.2 then applies verbatim.  \(\square\)

## 14. Co-selection with the existing protected bank

Write the protected bank from the rolling-collar/reservoir theorem as

\[
                         P=P_{\rm bulk}\cup P_{\rm hi},       \tag{14.1}
\]

where `P_bulk` consists of the deterministic top and low common-core paths
together with the complete low rolling-collar cycle, and `P_hi` is the
probabilistically packed high-trace tail.

### Lemma 14.1 (bulk obstacle load)

The enlarged halo of the deterministic top/low common-core part has
polynomial load in every fixed external trace and physical rank.  The full
halo of the rolling low-collar cycle has size at most

\[
                         m^{O(1)}(2em/d)^d.          \tag{14.2}
\]

Consequently the central halo in Lemma 13.1 can be selected disjoint from
the full halo of `P_bulk`.

#### Proof

One low common-core path has one exact external trace and `O(m)` roles.
Passing to its Ore halo changes the trace in at most one coordinate and
costs a polynomial factor.  Hence a named external trace receives roles
from only polynomially many neighbouring path traces and has polynomial
load.  The deterministic top bank itself has only polynomially many paths
and is absorbed by the same estimate.

The rolling-collar estimate is (12.1), with another polynomial factor for
its enlarged halo.  The trace-spread part may be put into the fixed-obstacle
version of the halo LLL.  The raw collar part has unary probability at most
its size times `m^{O(1)}/B_m`, which is

\[
 \exp\{-d\log(m/d)+O(d)\}=o(1).                    \tag{14.3}
\]

Adding these unary events leaves every dependency-neighbourhood sum
`o(1)`.  \(\square\)

### Lemma 14.2 (high-tail halo can be selected afterward)

After fixing the central halo and `P_bulk`, the random high-trace paths of
the hybrid reservoir can be chosen with their full Ore halos disjoint from
both fixed banks and from one another.

#### Proof

The central bank has `O(m2^m)` incidences and hence
`m^{O(1)}2^m` halo roles.  A high-tail candidate path has `O(m^2)` halo
roles.  Every one-role marginal in the symmetric high-tail construction
lies in a layer of size `2^{2m-o(m)}`; marking a facet, cofacet, or endpoint
neighbour changes this only by a polynomial factor.  Thus the probability
that one candidate halo meets the fixed central halo is at most

\[
 {m^{O(1)}2^m\over2^{2m-o(m)}}=2^{-m+o(m)}.         \tag{14.4}
\]

The same estimate applies to `P_bulk`.  There are only `2^{o(m)}` high
targets, so the union of all earlier high-tail halos remains
`2^{o(m)}` and contributes `2^{-2m+o(m)}`.  The total forbidden probability
is less than one at every greedy step.  \(\square\)

### Theorem 14.3 (joint protected bank and exact `q1` factor)

For all sufficiently large `m`, the complete protected bank `P` and the
central antipodal dwell-and-ear bank `A` have a simultaneous realization
such that

1. `P union A` has maximum incidence degree two;
2. all nonlocal Ore halos are disjoint;
3. every protected owner, lower colour, and immediate-upper colour is
   private except for intended consecutive incidences;
4. the joint exposure bounds satisfy

   \[
    \ell_{P\cup A}(x)\le10,\qquad
    e_{P\cup A}^{\rm priv}(x)\le10,
    \qquad z_U(P\cup A)\le9;                       \tag{14.5}
   \]

5. `P union A` extends to a spanning two-factor of the middle-levels
   incidence graph.

#### Proof

Lemmas 13.1--14.2 give the simultaneous halo separation.  It remains only
to audit the local contribution of `A` to (14.5).

Along a monotone Johnson ear, a fixed lower vertex can be contained in at
most two consecutive owners.  Otherwise two owners containing it would be
Johnson adjacent while their positions on a geodesic differ by at least
two.  The same statement holds in a cyclic-window dwell: two length-`h`
windows containing one fixed length-`h-1` subset must be adjacent.
Likewise a fixed owner can contain at most two consecutive protected lower
colours of either object.  At a chronology seam only the two incident
objects can contribute.  Therefore the central local bounds are at most

\[
               \ell_A(x)\le4,\qquad
               e_A^{\rm priv}(x)\le2,
               \qquad z_U(A)\le4.                 \tag{14.6}
\]

All other central contributions have disjoint Ore halos.  The old bank has
bounds `10,10,9`; hence the joint bounds are the **maximum**, not the sum,
of the old bounds and (14.6), proving (14.5).

The joint bank still has only `O(m2^m)` incidences.  The protected-factor
proof uses precisely this size scale, the three bounds in (14.5), and the
same at most `2m` exceptional deterministic top endpoints.  Every new
central endpoint is private: its unique protected lower neighbour belongs
to its protected path palette.  Thus the small-shore, optional co-small,
and near-shadow arguments apply without alteration and extend `P union A`
to a spanning two-factor.  \(\square\)

## 15. Exact decoration interface after coextension

Theorem 14.3 makes the following rows automatic.

1. **Immediate ownership and palettes.**  Every central owner and both
   `q1` palettes are literal and private in one exact spanning factor.
2. **Common-core target witnesses.**  Each intact dwell has contiguous
   owner union `K union T`; inserting ears between dwells does not alter
   that internal interval.
3. **Central residence.**  Cyclic dwell interiors are biresident, the two
   external halos discharge every seam flag, and the fork construction
   creates no short external run or gap.
4. **Low literal tickets.**  The rolling-collar cycle is halo-disjoint and
   retains every rank-at-most-`d` source interval.
5. **Known hinge-damage backup.**  Every old witness in `P` remains intact.

It does **not** make the following rows automatic.

1. The `2^{o(m)}` deleted trace tails and their splice ears still have to be
   inserted into the central chronology.
2. A spanning two-factor completion is not a bounded-component or one-cycle
   completion; its unprotected residual edges need not be resident.
3. The common-core damage family is not the complete arbitrary-width PBBS
   occurrence bank.  Upper targets outside the retained hinge/fan witnesses
   still require one occurrence-complete chronology.
4. No theorem here transports the terminal common-cap/compiler state through
   the new ears or the residual factor completion.

Thus the forced noncyclic ear and exact `q1` coextension gates are closed.
The remaining decorated theorem is a tail-splice plus all-width/residual
chronology plus terminal-cap statement.
