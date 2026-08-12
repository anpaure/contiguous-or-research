# Two separated star selectors close the chain ledger but not the carrier

Date: 2026-08-01  
Lane: D, additive-constant two-star macro  
Status: exact trace/common-cap theorem, exact adjacent `d=2` exception, and
orientation-general sharp no-go for two literal asymmetric selectors when
`d>=3`.  The theorem does not exclude a nonflat bridge, a compensating
deletion collar, or a macro whose two stars are not individually asymmetric
selectors.

## 0. Verdict

Two copies of the asymmetric one-chain selector have an exact useful
composition.  Put a prefix selector and a reflected suffix selector in
opposite phase.  For `d>=3`, their closest compatible outward-facing
placement has star separation `d+1` and total source-support width `3d`.
At `d=2` there is one exceptional adjacent composition of width four, and it
is already a literal two-owner Johnson path.  In phase `epsilon` their active
fans realize

\[
 B_\epsilon+\text{prefix},\qquad
 B_{1-\epsilon}+\text{suffix},                         \tag{0.1}
\]

while the destroyed crossing targets are

\[
 B_{1-\epsilon}+\text{prefix},\qquad
 B_\epsilon+\text{suffix}.                             \tag{0.2}
\]

The prepared two-phase endpoint carve realizes (0.2) literally.  On changing
phase, the fan and endpoint target assignments transpose.  Thus the complete
two-chain target/address ledger returns exactly in each terminal state.

For `d>=3`, this does **not** give a physical coatom packet in any
orientation.  Exactness of two strict asymmetric selectors forces their
separation to be at least `d+1`.  No
depth-`d` owner window then contains both stars.  The star-spanning owners of
the prefix selector are

\[
                 B_0\cup B_1\cup\{f_1,\ldots,f_i\},
                 \qquad 1\le i<d,                       \tag{0.3}
\]

and hence have strictly increasing ranks.  The reflected selector has the
same defect in reverse.  For every `d>=3`, the literal two-selector word is
therefore not an equicardinal `D^d` chronology, regardless of the endpoint
return bank or the compiler matching.

There is also no fixed-address typed socket common to both phases unless the
two phase bases coincide.  There is, however, an exact **two-socket terminal
transposition**: if the named targets are `B_0,B_1`, the two star cells cover
both in each phase and swap their addresses between phases.  Its exact cap
test is stated below.

The raw source-length charge of the two insertions is `+2`; the affected
short-cell count changes by `2d`.  Typing both star cells consumes two scalar
credits, leaving scalar net `2d-2`; in the separated construction this is
realized by distinct opposite-fan addresses.  Those addresses all have the
same plateau value `B_0 union B_1`, so their matching rank is one and
`2d-2` is not a compiler-capacity theorem.  In
the adjacent `d=2` exception the inactive nonsingleton fans coincide at the
central `B_0 union B_1` address, and one further
credit is required to return the old joint span, leaving at most one.  A
zero-length version needs two separately
audited deletion/return operations and is not supplied by this macro.

## 1. The closest compatible pair

Let `d>=2`.  Let `C,{a},{b},{f_1},...,{f_d}` be pairwise disjoint, with
`C` nonempty, and put

\[
 B_0=C\cup\{a\},\qquad B_1=C\cup\{b\},\qquad
 F_i=\{f_1,\ldots,f_i\}.                                \tag{1.1}
\]

Place the first star at `0`.  Its prefix-selector word in phase
`epsilon in {0,1}` is

\[
\begin{aligned}
 A_{-t}^\epsilon&=C\cup\{f_t\}&&(1\le t<d),\\
 A_0^\epsilon&=B_\epsilon,\\
 A_1^\epsilon&=B_{1-\epsilon},\\
 A_t^\epsilon&=C&&(2\le t<d).
\end{aligned}                                            \tag{1.2}
\]

Place a reflected suffix selector at `s=d+1`, in the complementary phase:

\[
\begin{aligned}
 A_s^\epsilon&=B_{1-\epsilon},\\
 A_{s-1}^\epsilon&=B_\epsilon,\\
 A_{s-t}^\epsilon&=C&&(2\le t<d),\\
 A_{s+t}^\epsilon&=C\cup\{f_{d-t+1}\}&&(1\le t<d).
\end{aligned}                                            \tag{1.3}
\]

The overlap in (1.2)--(1.3) is exactly positions `2,...,d-1`, and both
prescriptions equal `C` there.  The combined support is

\[
                   [-(d-1),2d],                           \tag{1.4}
\]

which has `3d` source positions.

For `1<=i<d`, define the prefix and suffix chains

\[
 P_i^e=B_e\cup F_i,\qquad
 S_i^e=B_e\cup\{f_{i+1},\ldots,f_d\}.                    \tag{1.5}
\]

### Theorem 1.1 (exact two-selector trace)

In phase `epsilon`, the first collar has

\[
 \operatorname{fan}^{P}_i=P_i^\epsilon,\qquad
 \operatorname{lost}^{P}_i=P_i^{1-\epsilon},             \tag{1.6}
\]

and the second collar has

\[
 \operatorname{fan}^{S}_i=S_i^{1-\epsilon},\qquad
 \operatorname{lost}^{S}_i=S_i^\epsilon.                 \tag{1.7}
\]

The unused opposite fan of each collar is constant from depth two onward:
every one of its nonsingleton cells has value `B_0 union B_1`.

#### Proof

For the first collar, every old crossing contains position `+1`, hence the
base `B_(1-epsilon)`, and contains exactly the left filler sources
`f_1,...,f_i`.  Its active left fan contains the star `B_epsilon` and those
same filler sources.  This proves (1.6).  Reflection exchanges left with
right, sends `f_t` to `f_(d-t+1)`, and uses star base
`B_(1-epsilon)`; this gives (1.7).  The first nonstar source on each inactive
flank already contains the opposite base, while all later inactive sources
are subsets of it, proving the plateau assertion.  \(\square\)

### Proposition 1.2 (the adjacent `d=2` exception)

For `d=2`, put the two stars at adjacent positions `0,1` and use

\[
 A_{-1}^\epsilon=C\cup\{f_1\},\quad
 A_0^\epsilon=B_\epsilon,\quad
 A_1^\epsilon=B_{1-\epsilon},\quad
 A_2^\epsilon=C\cup\{f_2\}.                              \tag{1.8}
\]

The first star is the prefix selector and the second is the reflected suffix
selector: each star is the other collar's nearest active-base source.  Their
two depth-two owners are

\[
 T_0=B_0\cup B_1\cup\{f_1\},\qquad
 T_1=B_0\cup B_1\cup\{f_2\}.                             \tag{1.9}
\]

They are equicardinal, meet in codimension one, and are phase independent.
Thus (1.8) is a literal Johnson edge, and the two typed star values `B_0,B_1`
transpose under phase reversal in one common cap.  This is the small-depth
escape exhibited here from the separation/rank argument below; its two
exterior joins remain host conditions.

#### Proof

The four fan/lost values are obtained by the unions
`A_(-1) union A_0`, `A_(-1) union A_1`, `A_1 union A_2`, and
`A_0 union A_2`.  They are respectively
`B_epsilon+f_1`, `B_(1-epsilon)+f_1`,
`B_(1-epsilon)+f_2`, and `B_epsilon+f_2`.  The two length-three
unions are (1.9).  \(\square\)

Deleting the two adjacent stars makes the two flank sources adjacent.  Their
old length-two span has value

\[
                  J=C\cup\{f_1,f_2\}.                    \tag{1.10}
\]

None of the three new length-two cells has value `J`: their values are
`B_epsilon+f_1`, `B_0 union B_1`, and `B_(1-epsilon)+f_2`.
Thus the adjacent macro has one exact joint-span return obligation.  This
obligation is separate from the two opposite-phase chain returns.

### Corollary 1.3 (guarded `d=2` literal phase macro)

Put `D=B_0 union B_1` and place fixed guard letters `D` immediately outside
the four-source word (1.8):

\[
 (A_{-2},\ldots,A_3)
   =(D,C+f_1,B_\epsilon,B_{1-\epsilon},C+f_2,D).          \tag{1.11}
\]

Then the complete ordered depth-two owner segment is

\[
          D+f_1,\quad D+f_1,\quad D+f_2,\quad D+f_2.     \tag{1.12}
\]

It is equicardinal and phase independent.  Every interval of length at
least three which meets a phase-active source has the same literal union
in both phases: it either contains both active bases or one of the guards
`D`.  At length one the target multiset is unchanged.  At length two the
entire signed change is the coefficient-one square

\[
 [B_1+f_1]+[B_0+f_2]-[B_0+f_1]-[B_1+f_2].                \tag{1.13}
\]

The common caps may be chosen as `P_0=P_1=D`, with every fixed flank and
guard cap equal to its displayed source value.  Thus both terminal words
are literal in one cap family.  The phase transition itself changes no
physical length; planting the two star positions costs two.  After typing
both stars and paying the joint return (1.10), the scalar short-cell
surplus is at most one.

#### Proof

The four length-three unions give (1.12).  An interval containing exactly
one active source and having length at least three must cross the adjacent
guard on that side; an interval containing both active sources contains
`D` already.  This proves upper literal invariance.  Direct enumeration of
the three length-two intervals gives (1.13), and the cap claim is witnessed
by (1.11).  The final count is `2d-2-1=1` at `d=2`. \(\square\)

## 2. Endpoint return and terminal address transposition

The prepared endpoint-carving theorem gives, in phase `epsilon`, literal
boundary cells with values

\[
 P_i^{1-\epsilon}\quad\text{on the left},\qquad
 S_i^\epsilon\quad\text{on the right}.                   \tag{2.1}
\]

At the selected-row incidence level, assume its source supports, the two
star-collar support, and all named cell addresses are pairwise disjoint.
Then (1.6)--(1.7) and (2.1) coexist in the product of those row systems.  A
physical terminal word additionally requires all carrier and protected rows;
Theorem 4.2 shows that the raw selector word fails that stronger test.  For
every `i`, phase reversal performs the address
transpositions

\[
 \operatorname{fan}^{P}_i\longleftrightarrow
 \operatorname{boundary}^{P}_i,\qquad
 \operatorname{fan}^{S}_i\longleftrightarrow
 \operatorname{boundary}^{S}_i.                          \tag{2.2}
\]

Thus the complete prefix/suffix chain bank has the same target set and the
same address set in both phases.  This is an exact target-ledger statement,
and becomes a physical matching only after the full common-cap test passes.
The matching is terminal-state dependent; (2.2) is not one edgewise matching
common to both phases.

This is the strongest unconditional positive statement for the literal
two-selector trace.  In particular, the inactive fan plateaux cannot replace
the endpoint bank: despite furnishing `2(d-1)` distinct addresses, they
furnish at most two literal target values, and here in fact the two values
coincide.

## 3. Exact common-cap criterion for two stars

The architecture-independent criterion is useful because long protected
rows may meet both collars.  Let `p,q` be the star positions, let `P_x` be
the common source cap at position `x`, and, in phase `epsilon`, let a selected
row `J` have target `T_J^epsilon` and fixed exterior OR contribution
`E_J^epsilon`.  Define

\[
 K_x^\epsilon=P_x\cap
    \bigcap_{J\ni x}T_J^\epsilon.                         \tag{3.1}
\]

### Theorem 3.1 (two-star maximal-word test)

Both terminal phases have nonzero words inside the same cap family `P` if
and only if, for each `epsilon`,

\[
 E_J^\epsilon\subseteq T_J^\epsilon,\qquad
 K_x^\epsilon\ne\varnothing,                             \tag{3.2}
\]

and

\[
 T_J^\epsilon=E_J^\epsilon\cup
                 \bigcup_{x\in J}K_x^\epsilon            \tag{3.3}
\]

for every selected row and every source position.  The maximal terminal
words are `A_x^epsilon=K_x^epsilon`.

If every selected row has source-span at most `d+1`, then stars separated by
`d+1` occur together in no row, and (3.1)--(3.3) factor into two one-star
tests.  For longer protected rows this factorization is invalid; their fixed
exterior contribution must remain in (3.3).

#### Proof

Every feasible source at `x` is contained in its cap and in every target row
containing `x`, hence in `K_x^epsilon`.  Exact row replay gives one inclusion
in (3.3), while the definition of `K` gives the other.  Conversely the
maximal letters `K` replay all rows by (3.3).  The separation assertion is
the elementary fact that a source interval of at most `d+1` positions has
coordinate span at most `d`.  \(\square\)

For phase-swapped typed sockets, prescribe

\[
 Z_p^\epsilon=S_\epsilon,\qquad
 Z_q^\epsilon=S_{1-\epsilon}.                             \tag{3.4}
\]

With nonstar letters frozen, let `U_(x,J)^epsilon` be the union of the
nonstar sources in a row `J` containing star `x`, and set

\[
 M_x^\epsilon=\bigcup_{J\ni x}
       (T_J^\epsilon-U_{x,J}^\epsilon),\qquad
 Q_x^\epsilon=P_x\cap\bigcap_{J\ni x}T_J^\epsilon.        \tag{3.5}
\]

Assume first that every `U_(x,J)^epsilon` is contained in its target; this
is necessary and cannot be repaired at the star.  Then (3.4) is legal exactly
when every affected row replays after these substitutions.  In the separated
bounded-span case this is equivalently the two one-star forced-mask tests

\[
 M_p^\epsilon\subseteq S_\epsilon\subseteq Q_p^\epsilon,
 \qquad
 M_q^\epsilon\subseteq S_{1-\epsilon}\subseteq Q_q^\epsilon.             \tag{3.6}
\]

together with containment of every fixed nonstar union in its target.  If a
row contains both stars, only the joint replay equation in (3.3) is exact;
two separate interval tests are insufficient.

For the selector (1.2)--(1.3), `(S_0,S_1)=(B_0,B_1)` gives two terminal
typed sockets whose addresses swap.  A fixed target at a fixed star address
in both phases would require `B_0=B_1`, which erases the phase selector.

## 4. Sharp separation and carrier obstruction

### Theorem 4.1 (minimum separation)

Let an exact prefix selector at `0` have lost crossing targets
`P_i^(1-epsilon)`, and let an exact reflected suffix selector at `s>0` have
star base `B_(1-epsilon)` and the lost suffix targets of (1.7).  If
`B_0-B_1` and `B_1-B_0` are both nonempty, then for `d>=3`

\[
                              s\ge d+1.                    \tag{4.1}
\]

Equality is attained by (1.2)--(1.3).

#### Proof

If `s=1`, the two stars supply each other's active bases.  For `d>=3`, however,
the prefix selector forces `f_1` at position `-1`, while that position is at
distance two on the suffix selector's inactive flank and its exact targets
exclude `f_1`.  Thus `s=1` is impossible.  (When `d=2` that inactive-flank
position does not exist, giving Proposition 1.2.)

Now let `s>=2`.  The suffix selector must put the phase-`epsilon` exclusive active coordinate
at its nearest left source, position `s-1`.  If `s<=d`, that position lies
on the positive flank of the prefix collar at distance at most `d-1` and is
contained in at least one prefix crossing.  But every prefix crossing target
is `B_(1-epsilon) union F_i` and excludes that active coordinate.  Exact OR
replay is impossible.  Hence `s>=d+1`.  The overlap check following (1.3)
proves attainability.  \(\square\)

### Theorem 4.2 (equicardinal-carrier no-go)

For `d>=3`, no outward-facing prefix/suffix pair satisfying Theorem 4.1 can
be a literal equicardinal depth-`d` carrier while retaining the exact
asymmetric selector targets.

#### Proof

At separation at least `d+1`, no source window of length `d+1` contains both
stars.  For the prefix star, the owner window with `i` old positions on the
left and `d-i` on the right has value

\[
 Z^\epsilon\cup\operatorname{lost}^{P}_i
   =B_0\cup B_1\cup F_i.                                 \tag{4.2}
\]

Its rank increases by one from `i` to `i+1`.  Since `d>=3`, at least two such
owners occur.  They cannot belong to one equicardinal chronology.  The
suffix collar has the reversed defect.  The argument uses only the target
values and the star identity, so changing hidden source copies or enlarging
the common caps cannot repair it.  \(\square\)

### Theorem 4.3 (orientation-general separation and no-go)

Let the prefix and suffix selectors independently choose their active fan
on the left or on the right, while retaining their strict filler orders and
opposite phase bases.  For `d>=3`, every source-compatible pair has star
separation at least `d+1`.  The exact minimum is `d+1` for the outward and
inward pairs and `2d-1` for either same-direction pair.  Consequently every
such pair contains the
varying-rank owner chain (4.2), possibly reversed, and no orientation is an
equicardinal depth-`d` carrier.

#### Proof

There are four side choices.  If the active fans point outward, the
exclusive active-label argument of Theorem 4.1 applies.  If they point
inward, the case `s=1` prescribes an active filler at the other star and
already conflicts with its base.  For `2<=s<=d`, choose a shared gap
source at distances `t,u>=1`, with `t+u=s`.  The prefix fan forces `f_t`
there, while the suffix fan through distance `u` permits only
`f_(d-u+1),...,f_d`.  Since `t<=d-u`, it excludes `f_t`, a contradiction.

If both active fans point left, then for `s<=d-1` the prefix star lies in
the suffix active fan and introduces the prefix-exclusive base coordinate,
which that fan target omits.  At `s=d`, the suffix far increment `f_2`
occurs at the prefix selector's nearest inactive source and enters its
first crossing target `B_(1-epsilon)+f_1`, which forbids `f_2`.
For `d+1<=s<=2d-2`, that far increment occurs at position
`s-d+1 in {2,...,d-1}`, still on the prefix inactive flank and still in its
first crossing.  Thus `s>=2d-1`; the both-right case is its reflection.
The bounds are attained: the outward construction is (1.2)--(1.3), the
inward pair agrees on every shared source `C+f_t`, and same-direction
supports are disjoint and adjacent at `2d-1`.  Once the global bound
`s>=d+1` holds, no length-`d+1` owner window contains both stars.  Each selector's
own mixed owners are exactly (4.2), in increasing or decreasing order,
and have at least two distinct ranks when `d>=3`. \(\square\)

For `d=2` there is only one internal mixed owner per collar, so this
argument is vacuous.  Proposition 1.2 is the sharp adjacent exception;
its two external joins and the joint-span return (1.10) still require
literal replay.

Consequently the minimal live extension is not a third marginal target
assignment.  It must change the physical owner equations: for example a
nonflat bridge spanning the collars, a compensating deletion/facet collar,
or a macro in which at least one star is not an exact asymmetric selector.

## 5. Length and address ledger

Relative to the word with the two star positions deleted:

* the literal support (1.4) has length `3d` instead of `3d-2`, so source
  length charge is exactly `+2`;
* each insertion replaces `d-1` old crossing cells by `2d-1` fan cells, a
  net short-cell change of `d`;
* the pair therefore has scalar net `2d`;
* typing both singleton stars consumes two, leaving scalar net `2d-2`;
* in the adjacent `d=2` exception, returning the joint old span consumes
  one more unit, leaving at most one scalar address;
* in the separated construction, the `2d-2` unused nonsingleton
  opposite-fan addresses realize only the plateau `B_0 union B_1`, so their
  useful matching rank is at most one; in the adjacent `d=2` exception the
  two inactive plateau addresses coincide physically.

Deleting `r` other source cells changes the gross source-length charge to
`2-r`, but each deletion changes its own interval rows.  A zero-length macro
therefore requires two explicit, common-cap, basis-neutral deletion returns;
they cannot be inferred from this scalar ledger.

## 6. Audit

The lightweight exact replay

```text
scratch/audit_threadD_two_star_selector_commonq_20260801.py
```

checks (1.6)--(1.7), overlap compatibility at the sharp separation, the
separation conflicts below `d+1`, terminal typed-socket transposition, owner
rank drift, and every count above for `2<=d<=32` and both phases.

The companion replay

```text
scratch/audit_threadD_two_star_orientation_adjacent_gate_20260801.py
```

checks the exact orientation minima through `d=24`, while

```text
scratch/audit_threadD_two_star_orientation_redundant_copy_exhaustive_20260801.py
```

independently enumerates every coordinatewise source pattern satisfying the
fan and crossing equations, including arbitrary legal redundant copies, for
`2<=d<=6`, both phases, and all four orientations.  It rejects all 196
smaller-separation cases and constructs nonempty witnesses for all 40 exact
minima.  The analytic proof above supplies the all-`d` conclusion.
