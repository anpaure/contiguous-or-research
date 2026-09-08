# Independent audit: copy-before-erase still needs a literal private reservoir

**Date:** 2026-08-06  
**Scope:**
`MATH_THEOREM_ODD_COPY_BEFORE_ERASE_NINE_RECORD_COLLAR_20260806.md` and
`MATH_THEOREM_ODD_RESIDUAL_FIRST_CONNECTOR_COPY_BEFORE_ERASE_20260806.md`.
No computation is used.

## Verdict

The information-counting correction is sound: once the exterior source is
still reverse-decodable, it determines (s=a+b), and for fixed (s) there
are at most three ordered collar types.  Hence the three selected unordered
first-clock rows have enough information capacity.  Keeping the eventual
double head at one fixed physical berth also removes the adaptive-berth
collision from the source-internal bootstrap proposal.

The two proposed closure theorems nevertheless do **not** yet pass.  Both
invoke a private bounded reservoir and an occurrence-labelled component
route which have not been constructed.  The proved component-mass router is
a scalar/configuration reachability theorem.  Its own conclusion explicitly
states that it does not provide a pairwise-disjoint labelled path bank.
Invoking that router as the missing labelled setup, teardown, or residual
writer is therefore circular.

The proof-safe status is

\[
 \boxed{
 \text{three-state copy-before-erase record: informationally sufficient;}
 \quad
 \text{literal reservoir and residual handoff: open.}
 }
\]

## 1. What passes

For a collar (C(a)\mid C(b)), the outside central tape determines
(s=a+b) as long as that outside tape remains source-decodable.  The number
of ordered pairs at fixed sum is

\[
                         1,2,3,2,1.
\]

Therefore one can inject the ordered pairs at each fixed sum into the three
selected rows

\[
 \{01,10\},\qquad \{02,11\},\qquad \{12,21\}.
\]

An ordinary tail work edge toggles only the selected endpoint and leaves its
unordered row fixed.  Thus, conditional on a literal setup path and a
source-decodable exterior, this row really can serve as the three-valued
record while the source collar is absent.

The phase table in the proposed theorem is also the correct copy-before-
erase pattern: source collar during record writing, row record during head
creation and retirement, fixed head berth during bulk work, and target
collar during record erasure.  This repairs the earlier use of a moving head
created at a source-dependent berth.

## 2. The reservoir is not supplied by the component router

The setup theorem asks for two disjoint bounded work reservoirs and then
uses them to compensate the two collar increments

\[
                            4-2(a+b).
\]

No literal coordinate sets, initial configurations, terminal
configurations, or paths for these reservoirs are specified.  In particular,
the proof does not establish that:

1. the reservoir cells have one known common initial state for all nine
   sources, or that their old source information has first been copied
   elsewhere;
2. changing the reservoir while the collar is held fixed preserves the
   exterior decoder which is being used to recover (s=a+b);
3. the setup and teardown reservoirs are disjoint from the first clock, the
   fixed head berth, the old linkage, and every still-live source record;
4. the reservoir transition and collar transition compose to a path of
   constant total mass at every microstep; and
5. the nine resulting paths are pairwise vertex-disjoint, including their
   prepayment and restoration segments.

Theorem 6.4 of
`MATH_AUDIT_ODD_COMPLEMENT_ONE_SOCKET_INDEPENDENT_20260806.md` proves that,
with the active clock fixed, feasible mass triples and configurations inside
the two work components are reachable.  Immediately after that proof the
source says:

> Theorem 6.4 removes the only scalar obstruction ... The remaining issue is
> labelled serialization.

That theorem therefore cannot establish the five properties above.  A path
between two configurations need not preserve the unknown information in the
coordinates it overwrites, and simple paths chosen separately for different
sources need not be mutually disjoint.

There is also a chronology issue hidden by the word *prepay*.  If the
reservoir is first changed before the collar conversion, its mass change must
already be balanced somewhere else.  If the reservoir is instead meant to
change simultaneously with the collar, the proof must give the interleaved
literal unit-transfer sequence.  Either convention can be valid, but neither
is specified, and in both conventions the old and target reservoir contents
must remain recoverable.

Consequently Lemma 2.1 may provide the abstract row reachability needed for
the record, but Section 3 does not yet provide the labelled reservoir route
needed to turn that record into a fixed double head.

## 3. Deterministic simple routes do not imply bank injectivity

Both proposed files use the following inference:

\[
 \text{component connectivity}
 +\text{ one deterministic simple route per decoded source}
 \Longrightarrow
 \text{pairwise-disjoint occurrence-labelled routes}.
\]

This implication is false without an additional state decoder.  Simplicity
only prevents one selected route from visiting the same vertex twice.  It
does not prevent routes chosen for two different sources, or two different
stages, from meeting at an intermediate vertex.

This is exactly the issue already exposed by the literal collision

\[
  ACB\longrightarrow HHB,
  \qquad
  BAC\longrightarrow BHH,
\]

when the first head is allowed to move through (B): the first route can
reach (BHH), the bootstrap state of the second route.  A fixed physical
head berth prevents this particular collision during bulk work, but it does
not automatically label the reservoir-writing or arbitrary component-route
microsteps.

A proof must give either an explicit reversible transducer whose current
state recovers source and stage, or a separately proved tagged time-expansion
whose hypotheses include every reservoir and clock transition.  Saying that
the current state determines the microstep is the desired conclusion, not a
consequence of choosing the route deterministically.

## 4. The residual schedule is not exhaustive as written

Let

\[
 q=\epsilon(a_1)+\epsilon(a)+\epsilon(b),
 \qquad \epsilon(c)=c-1.
\]

After removing the first connector and the fixed collar, the work tape has
imbalance (-q).  The cancellation stack therefore leaves (|q|) unmatched
extremes, where

\[
                         |q|\in\{0,1,2,3\}.
\]

Section 2 of the residual theorem asks to locate “the unique unmatched work
connector” whenever (a_1) is extreme.  That connector need not be unique
and need not exist.  For example,

\[
 (a_1,a,b)=(2,2,2)
 \quad\Longrightarrow\quad |q|=3,
\]

whereas

\[
 (a_1,a,b)=(2,0,1)
 \quad\Longrightarrow\quad |q|=0.
\]

The bounded-bank observation remains correct, but the proposed four-stage
schedule must be split into the zero-, one-, two-, and three-residual cases.
In the zero-residual extreme case, the claimed remote target used to record
the orientation of (a_1\) is absent, so another persistent literal record is
needed through first-clock retirement.

Even after this case split, the residual file inherits the unconstructed
private reservoir from Section 2 and the unproved labelled serialization of
an arbitrary component route.

## 5. Smallest proof-safe completion

It is enough to prove one finite interface.

### Private-reservoir visible-cart lemma

For every collar type ((a,b)), every residual type
((a_1,|q|,\operatorname{sign}q)), and every required setup or teardown mass
change, give explicit bounded coordinate sets and directed paths such that:

1. reservoir initial and terminal states are prescribed and their overwritten
   source information is either common or retained elsewhere;
2. every unit transfer has constant global mass and a directed shadow-clock
   lift;
3. the first-row record, fixed head berth, root/boundary register, and old
   linkage are protected exactly where claimed;
4. the literal current state recovers source type, phase, and microstep;
5. paths for all source and residual types are pairwise vertex-disjoint; and
6. every reservoir is restored before its final source label is erased.

This is a bounded theorem: there are only nine collar types and finitely many
residual cases.  Proving it would validate the copy-before-erase strategy and
would close the odd collar.  The current component-mass theorem proves its
scalar feasibility but not this literal interface.

## 6. Exact frontier

The newest proposal is real progress because it reduces the persistent
record from nine states to three and fixes the head berth.  It does not yet
finish the odd package.  The remaining burden is not asymptotic packing; it
is one explicit finite occurrence-labelled reservoir/cart theorem, including
the four residual multiplicity cases.

