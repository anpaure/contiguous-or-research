# Stratified point load and weighted-LLL packing of the tail chronology

**Date:** 2026-08-06  
**Method:** exact Boolean-layer coarea, `K`-fibre point probabilities,
an asymmetric local lemma, and direct all-occurrence exposure tails; no
computation or search  
**Status:** draft point-load calculation and conditional tail-packing
argument.  The exact audit
`MATH_AUDIT_TAIL_STRATIFIED_WEIGHTED_LLL_AND_EXPOSURE_GATE_20260806.md`
corrects the global-exposure LLL, isolates the unproved small-fibre
co-selection row, and explains why a tail-only Hamilton completion is not
a completion of the central-plus-tail bank.  Do not cite the unconditional
status or component conclusion from an earlier version of this draft.

## 1. Why singleton low auxiliaries must be omitted

The unique rank-`m` owner whose union can witness `K union {e}` is

\[
                         K\cup\{e\}.                \tag{1.1}
\]

If all `m` singleton auxiliaries were protected, every one of these owners
would contain the same unused lower facet `K`.  The all-occurrence exposure
at `K` would be `m`, not sub-half.

There is a second manifestation of the same obstruction.  The first
external insertion from `K union {e}` has immediate upper colour

\[
                         K\cup\{e,f\},              \tag{1.2}
\]

which is the forced upper colour of the two-owner witness for `{e,f}`.

Therefore the complement-paired construction is used only for

\[
                         2\le |T|\le2d.             \tag{1.3}
\]

There are only `m` co-singleton high targets.  Keep their old monotone
high paths and attach them by the universal seasoning-buffer theorem of
`MATH_THEOREM_UNIVERSAL_SEASONING_BUFFER_TAIL_SPLICE_20260806.md`.
This is a polynomial exceptional bank and introduces no singleton owner
of the form `(1.1)`.

## 2. Exact external coarea for a rank-`q` macro family

For every `q` in `(1.3)`, temporarily construct the tail macro for **every**
`q`-subset `T subseteq E`, using the symmetric laws below:

1. the two low-collar insertion banks and their orders are uniform;
2. the balanced-high core, shores, and orders are uniform subject to their
   sizes;
3. connector interval SDRs are chosen by an equivariant version of the
   three-zone schedule; and
4. all still-free deletion and insertion orders are uniform.

The actual hinge-tail family is a subfamily of this full symmetric family.

### Lemma 2.1 (one-slot external point load)

Fix a labelled role slot in the rank-`q` macro.  Retain the part of its law
having external rank `s`.  If

\[
                         q\le s\le m-q,             \tag{2.1}
\]

then for every fixed `S in binom(E,s)`,

\[
 \sum_{T\in\binom Eq}
   \Pr\bigl(\operatorname{tr}(X_T)=S,
             |\operatorname{tr}(X_T)|=s\bigr)
       \le{\binom mq\over\binom ms}\le1.           \tag{2.2}
\]

#### Proof

The aggregate subprobability law over all rank-`q` starts is invariant
under `Sym(E)`.  Its total mass is at most `binom(m,q)`, so its mass at a
fixed rank-`s` trace is at most the first ratio in `(2.2)`.  If the role
has deterministic external rank `s`, equality holds.  Binomial
unimodality gives the last inequality under `(2.1)`. \(\square\)

All external traces in a low collar and balanced-high path lie between the
low rank `q` and the complementary rank `m-q`.  For a low-to-high
connector this also holds if the bounded residence-forced prefix and suffix
are completed by a rank-monotone type word.  The compatibility of that
type word with every clipped interval constraint is part of the explicit
rank-band row retained in the audit note.  Palette traces shift a displayed
owner rank by at most one;
grouping those two adjacent cases costs only a polynomial factor.  There
are `O(m)` slots and three base role types per macro.  Restricting from all
rank-`q` sets to the actual tail family only decreases the nonnegative sum.

### Corollary 2.2 (polynomial external role load)

For a fixed external trace and physical rank, the total expected base-role
load of the complete random tail bank is `m^{O(1)}`.  The same statement
holds for every fixed-radius Ore role after multiplying by a polynomial.

As in the central antipodal proof, bounded-variable Bernstein concentration
and a union bound over `2^m` traces select the external schedules with
polynomial **maximum** load.  The random variables belonging to distinct
rank-`q` macros are independent; the two connectors incident with one
macro form only a bounded dependency neighbourhood.

## 3. The small external layers have a sharper point bound

The polynomial maximum bound is deliberately crude near the bottom.  A
direct collar count is sharper.

At collar depth `a>=0`, a low macro based at `T` has external trace

\[
                         S=T\cup J_a,qquad |J_a|=a. \tag{3.1}
\]

For fixed `S` of size `s=q+a`, the sum over all rank-`q` bases is exactly

\[
 {\binom sq\over\binom{m-q}a}
       ={\binom mq\over\binom ms}\le1.             \tag{3.2}
\]

There are two collars.  Thus, after conditioning on the external trace,
the aggregate point mass at a fixed physical role is bounded by

\[
 \begin{array}{c|c}
 \text{role rank}&\text{worst `K`-fibre denominator}\ \hline
 m-1&\binom{m-1}s,\\
 m&\binom{m-1}{s-1},\\
 m+1&\binom{m-1}{s-2}.
 \end{array}                                       \tag{3.3}
\]

The only zero-dimensional entry is the upper role at `s=2`.  By Section 1
it occurs only as the unique protected upper target of a rank-two witness;
no singleton collar is present, so it has no nonlocal competitor.

For every remaining random role `s>=3`.  Summing over the at most `s`
possible starting ranks and the two collar sides gives

\[
 \Lambda_s
 \le {C s\over\binom{m-1}{s-2}}                 \tag{3.4}
\]

for a fixed rank-`m+1` physical role, and stronger bounds in the other two
ranks.  In particular

\[
 \sum_{s=3}^{3d} \Lambda_s=O(m^{-1}).              \tag{3.5}
\]

The balanced-high and connector roles begin in layers at distance at
least `d-O(1)` from either end.  Their total point load is

\[
                         m^{O(1)}/\binom{m-1}{d-O(1)}=m^{-\omega(1)}.
 \tag{3.6}

## 4. Local tags remove shared-variable equalities

At a low outer port the external trace has size at most `3d`.  Choose the
first connector insertion `a` outside that trace and never delete it.
Every later connector role contains `a`, whereas every role of the low
macro omits it.  The first lower/upper pair is distinguished by a second
external label exactly as in the two-coordinate fork lemma.

At a balanced-high port choose two labels from its fixed external core
`C`; this is possible because `|C|=q+1>=3`.  Hold the first label fixed on
the high macro and flip it only on the final connector transition; delay
the paired label on the other incident connector.  The same two-bit table
as the central fork separates both connectors from the high macro and from
one another, apart from intended endpoints.

Call these the **local fork tags**.  They use only a bounded number of the
`Theta(m)` available directional changes.  To invoke them one must exhibit
their four boundary swaps inside the three-zone interval schedule and show
that the two neighbours reserve the required inserted labels.  Once this
literal table is supplied, every remaining possible equality uses disjoint
macro variables.  The first draft did not include that table, so this is a
hypothesis of Conditional Theorem 5.1 rather than a closed row.

## 5. Weighted local lemma for exact base privacy

For every nonintended equality of two tail base roles of the same physical
rank, make one bad event.  Intended consecutive endpoints and the unique
rank-two upper targets are omitted.  Unary avoidance of an already fixed
central/rolling/hinge bank is valid only after proving the weighted
small-fibre obstacle bound in the audit note; polynomial trace load alone
does not imply it at external rank three.

Fix an arbitrary realization of one macro.  Equations `(3.4)`--`(3.6)`,
summed over its `O(m)` roles, show that the sum of the probabilities of all
collision events involving that macro is

\[
                         \varepsilon_m=O(m^{-1})+m^{-\omega(1)}=o(1).
 \tag{5.1}
\]

This is a point-mass statement; it does not multiply the weakest boundary
probability by all `O(m)` slots.

Two bad events are independent unless their macro pairs meet or are
consecutive in the cyclic tail order.  Hence the sum of event
probabilities in the dependency neighbourhood of any event is at most
`C epsilon_m`.  Put `x_e=2Pr(B_e)`.  For large `m`,

\[
 x_e\prod_{f\sim e}(1-x_f)
 \ge2\Pr(B_e)\left(1-2C\varepsilon_m\right)
 \ge\Pr(B_e).                                      \tag{5.2}
\]

The asymmetric Lovasz local lemma therefore gives a realization with no
owner, immediate-lower, or immediate-upper collision.

### Conditional Theorem 5.1 (tail-internal base-role packing)

The low collars, balanced-high paths, and all resident connectors for
`2<=q<=2d` have a simultaneous realization in which the protected owner
paths are simple and both immediate palettes are private, provided the
external-rank band and literal local-fork schedules asserted in Sections 2
and 4 are supplied.  This conclusion is internal to the random tail bank.
Avoidance of the fixed central/rolling bank at the smallest fibres, and the
polynomial co-singleton seasoning bank, require the separate
boundary/co-selection lemma in the audit note.

## 6. Direct all-occurrence exposure: corrected event system

Full pairwise Ore-halo disjointness is stronger than needed at the bottom
layers and would reintroduce the singleton obstruction.  Let `F_0,F_1` be
the two alternating edge classes after opening one nonpayload connector
transition, and put

\[
 \widehat\alpha(F_i)=\max_x|N(x)\cap Y_i|,
 \qquad
 \widehat\beta(F_i)=\max_U|N(U)\cap Z_i|.          \tag{6.1}
\]

A fixed lower vertex is contained in at most two owners of one monotone
piece, and a fixed owner contains at most two lower colours of one piece.
The point-load calculation with one extra marked facet or cofacet therefore
gives bounded expected exposure, and one macro contributes only a bounded
amount.

One must **not** add the global events
`{widehat alpha_x>m/3}` directly to the collision LLL: such an event sees
the accumulated local-event charge of every macro which can hit `x`.
Instead use the minimal `t=Theta(m)` macro-witness events from Theorem 3.1
of
`MATH_AUDIT_TAIL_STRATIFIED_WEIGHTED_LLL_AND_EXPOSURE_GATE_20260806.md`.
Their rooted factorial-moment sum is `exp(-Omega(m log m))`; a witness sees
only `t O(1/m)=O(1)` local charge.  Hence, under the same external-rank,
fork, and boundary/co-selection hypotheses as Conditional Theorem 5.1,
the tail forest may simultaneously satisfy

\[
                         \widehat\alpha(F_i),
                         \widehat\beta(F_i)\le m/3. \tag{6.2}
\]

This does not by itself give a low-component completion of the combined
central-plus-tail bank.  Applied to the tail forest alone, the
Hamilton-anchored theorem forgets the central protected edges.  Applied
to the combined bank, the sharp matching-scale theorem still gives an
exact spanning `q1` factor, but its Hamilton-damage estimate is not
subexponential because the central bank has `2^{m+o(m)}` edges.

## 7. Exact scope

Established or reduced here:

1. the rank-two/singleton zero-fibre obstruction;
2. external trace spread for the complete tail chronology;
3. an `O(1/m)` tail-internal base-collision charge away from intended
   rank-two roles; and
4. a correct witness-event LLL reduction for fixed sub-half exposure.

Still open:

1. prove the literal rank-band/fork and small-fibre boundary co-selection
   lemma, including the co-singleton seasoning bank;
2. obtain a bounded- or subexponential-component completion which retains
   the central and tail banks simultaneously and preserves residence;
3. install the PBBS arbitrary-width occurrence bank on the same chronology;
4. transport the terminal common-cap/compiler state; and
5. deduce `nu(k)<=B(k)+O(1)`.
