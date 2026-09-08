# Independent proof audit: Boolean interval blocker LLL and the literal
# six-cycle occurrence obstruction

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_BOOLEAN_INTERVAL_BLOCKER_LLL_AND_SIX_CYCLE_SECTION_OBSTRUCTION_20260804.md`  
**Method:** independent symbolic proof replay.  No computation, solver,
enumeration, or random experiment.

## 0. Verdict

**PASS, with the scope stated in the theorem.**

The positive theorem is unconditional once its explicit factor premises
hold.  It proves an upper occurrence selector and rooted all-width forest.
Its nonvacuous form separates deterministic-safe targets from a vulnerable
leave; only vulnerable targets require logarithmically many witnesses.  It
does not prove that a protected all-dimensional Boolean factor has the
bounded multiplicities, deterministic-safe low rows, logarithmic vulnerable
menus, constant random-colour load, breaker banks, or private reserves.

The literal six-cycle calculation also passes.  Its only repeated q1
colour is `C+abc`.  The two targets `C+abcd` and `C+abce` have unique
admissible witnesses, even after longer intervals are allowed, and they
force the two different occurrences.  This is a Boolean component-level
obstruction, not a spanning-factor obstruction.

## 1. Interval incidence replay

On a directed cycle, a proper `q`-edge interval containing a fixed edge
places that edge in one of positions `1,...,q`; the position fixes the
start.  Hence there are exactly `q` such intervals.  A path can only delete
starts, so it has at most `q`.

For a fixed occurrence `e` of q1 colour `R`, a geodesic witness for a
rank-`(m+q)` target is a `q`-edge interval.  Each interval has one owner
union and therefore names at most one target.  Summing gives

\[
 \sum_{q=2}^{m-1}q
 ={m(m-1)\over2}-1=S_m.                              \tag{1.1}
\]

There are `mu_R` occurrences, so at most `mu_R S_m` target bad events can
mention variable `R`.  Counting the same target through several witnesses
or occurrences only overcounts and is harmless.  The polynomial load
bound is correct.

## 2. Target failure probability

For an admissible witness `I`, every deterministic colour is already fixed
to the required occurrence.  Its random q1 colours are distinct.  Under
independent uniform occurrence choices,

\[
 \Pr(I\text{ survives})
 =\prod_{R\in S^+(I)}|\Omega_R^P|^{-1}.              \tag{2.1}
\]

The multiplicity bound gives `|Omega_R^P|<=mu_R<=M`; if at most `A`
random colours occur, (2.1) is at least `M^{-A}`.  The declared `t`
witnesses have pairwise disjoint **random** scopes.  Shared deterministic
colours do not create dependence.  Therefore their survival events are
independent and

\[
 \Pr(B_X)
 =\prod_{I\in\mathcal L_X}(1-\Pr(I\text{ survives}))
 \le(1-M^{-A})^t.                                    \tag{2.2}
\]

This correctly strengthens the earlier full-colour-disjoint statement to
random-colour disjointness.  A deterministic-safe witness has empty random
scope and survives with probability one, so removing its zero-probability
failure event can only lower all variable loads and dependency degrees.
The hybrid corollary is valid.

## 3. Component events and dependency degree

If one component contains two occurrences of the same q1 colour, a section
selecting one occurrence globally cannot contain both component edges.  It
is therefore automatically broken.

Otherwise the component is q1-rainbow.  Its declared breaker edges have
distinct random colours.  Selecting all `s` has probability

\[
 \prod_{e\in Z_K}|\Omega_{u(e)}^P|^{-1}\le2^{-s}.    \tag{3.1}
\]

Avoidance omits at least one breaker edge, hence breaks the component.

A random colour occurs in at most `mu_R S_m` target scopes.  A physical
occurrence belongs to one component, so it occurs in at most `mu_R`
component-breaker scopes.  Thus its total bad-event load is at most

\[
                         \mu_R(S_m+1)\le M(S_m+1).   \tag{3.2}
\]

Every target scope has size at most `At`; every component scope has size
`s`.  With `B=max(At,s)`, an event has at most

\[
                         BM(S_m+1)-1                 \tag{3.3}
\]

neighbours.  Multiple shared colours only reduce this number.  Therefore

\[
 e\max\{(1-M^{-A})^t,2^{-s}\}BM(S_m+1)\le1          \tag{3.4}
\]

is a valid symmetric LLL condition.  Avoiding all bad events gives exactly
the four conclusions claimed in Theorem 3.1.

For fixed `A,M`, the proposed choices satisfy

\[
 (1-M^{-A})^{\lceil6M^A\log m\rceil}\le m^{-6},
 \qquad
 2^{-\lceil6\log m/\log2\rceil}\le m^{-6}.          \tag{3.5}
\]

The remaining factor in (3.4) is `O_(A,M)(m^2 log m)`, so (3.4) holds
eventually.  The asymptotic corollary is correct.

### Fixed-width resource check

A directed cycle cover on `W` edges has at most `W` proper directed
`q`-edge intervals at any fixed width.  Since one interval has one union,
if every rank-`(m+q)` target receives one witness and `V_q` targets receive
`t` witnesses, necessarily

\[
 {2m-1\choose m+q}+(t-1)V_q\le W.                  \tag{3.6}
\]

At q2,

\[
 {W\over{2m-1\choose m+2}}
 ={(m+1)(m+2)\over(m-1)(m-2)},                      \tag{3.7}
\]

which is below two for every integer `m>=9`.  Also

\[
 {V_2\over{2m-1\choose m+2}}
 \le {6m\over(m-1)(m-2)(t-1)}.                     \tag{3.8}
\]

Thus a uniform logarithmic menu is impossible at low width; the theorem's
hybrid formulation is essential.  With `t=Theta(log m)`, only an
`O(1/(m log m))` q2 fraction can be vulnerable.

## 4. Private reserve replay

For a component subset `Y`, the designated edges `d_K`, `K in Y`, are
`|Y|` distinct physical occurrences outside the full menu envelope.  Group
them by q1 colour.  A used colour `R` is available as a reserve in a member
of `Y`, and its group has size at most `b_R`.  Therefore

\[
 |Y|\le
 \sum_{R:N_R^{\rm res}(A_{\mathcal L})\cap Y\ne\varnothing}b_R.   \tag{4.1}
\]

This is exactly immutable reserve Hall.  With component events removed, a
random colour has target-event load at most `M S_m`; event size is at most
`At`.  The target-only condition

\[
 e(1-M^{-A})^t At M S_m\le1                         \tag{4.2}
\]

is therefore correct.  The LLL produces a rainbow witness bank; reserve
Hall may then produce a different occurrence section containing that bank
and breaking every component.  No quantifier is exchanged improperly.

## 5. Literal six-cycle replay

Let `|C|=m-2` and use five coordinates `a,b,c,d,e` outside `C`.  The six
owners are

\[
 C+ad, C+ab, C+ac, C+bc, C+ce, C+de.            \tag{5.1}
\]

Consecutive intersections, including the wrap, all have size `m-1`, so
this is a Johnson six-cycle.  Consecutive unions are

\[
 C+abd, C+abc, C+abc, C+bce, C+cde, C+ade.       \tag{5.2}
\]

Thus `R=C+abc` is the only repeated q1 colour, and its two occurrences are
adjacent.

The six two-edge owner-window unions are

\[
 C+abcd, C+abc, C+abce, C+bcde, C+acde, C+abde. \tag{5.3}
\]

The five rank-`(m+2)` entries are distinct.  Hence

\[
 X=C+abcd
 \quad\text{uses edges }(C+abd,R_1),                \tag{5.4}
\]

and

\[
 Y=C+abce
 \quad\text{uses edges }(R_2,C+bce).                \tag{5.5}
\]

For `X`, the complete consecutive block of owners lying in `X` is

\[
 C+ad, C+ab, C+ac, C+bc.                          \tag{5.6}
\]

The only longer `X`-valued extension of (5.4) inside that block uses both
`R` edges and is inadmissible.  Extending across either external boundary
introduces `e`.  For `Y`, the analogous compatible block is

\[
 C+ab, C+ac, C+bc, C+ce,                          \tag{5.7}
\]

and its only longer `Y`-valued extension again uses both `R` edges;
external extension introduces `d`.  Thus (5.4)--(5.5) are unique among all
admissible cyclic intervals, not only among minimum-width witnesses.

One occurrence section chooses one of `R_1,R_2`.  It therefore cannot keep
both witnesses.  Either singleton target is feasible, because all four
other colours in (5.2) are unique.  Every section omits the unchosen `R`
edge and breaks the cycle.  The claimed Boolean obstruction is exact.

## 6. Four-cycle impossibility replay

If opposite edges of a Johnson four-cycle have common union `R`, every one
of the four owner vertices is an `m`-facet of `R`.  The two intervening
adjacent unions are rank-`(m+1)` subsets of the rank-`(m+1)` set `R`, hence
equal `R`.  Thus the abstract colour word `R,A,R,B` with `A,B` different
from `R` cannot be literal Boolean.  This is consistent with, and explains
the need for, the six-cycle construction.

## 7. Scope boundary

The audited theorem proves the upper selector unconditionally **inside its
stated factor class**.  It leaves open all of the following existence rows:

1. a protected resident upper-surjective factor with `mu_R<=M=O(1)`;
2. deterministic-safe witnesses for almost every low-width target;
3. `Theta(log m)` geodesic witnesses for every remaining vulnerable target
   with pairwise-disjoint random scopes;
4. `O(1)` repeated colours in each vulnerable witness;
5. logarithmic component breaker banks or a capacity-faithful private
   reserve map; and
6. co-instantiation with the lower source, seam, and common-cap router.

The six-cycle shows that these hypotheses cannot be replaced by individual
target feasibility plus Boolean interval geometry.
