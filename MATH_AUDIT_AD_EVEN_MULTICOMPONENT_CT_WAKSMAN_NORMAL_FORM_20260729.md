# Adversarial audit of the even multi-component `(c,t)` / Waksman theorem

Date: 2026-07-29  
Audited file:
`MATH_THEOREM_AD_EVEN_MULTICOMPONENT_CT_WAKSMAN_NORMAL_FORM_20260729.md`  
Method: solver-free algebraic and encoding-scope audit.

## 1. Verdict

After the owner-transversal patch, the principal theorems are correct:

1. the slot/successor/phase datum is equivalent to every
   rotation-equivariant spanning simple middle factor;
2. a quotient cycle of length `ell` and voltage `v` has the exact
   `g=gcd(n,v)`-track form stated in Section 3;
3. the physical lift has `g` cycles of length `n ell/g`, including `n`
   cycles of length `ell` at voltage zero;
4. the Waksman successor network is an **additional** topology layer, not a
   replacement for the middle owner-transversal network;
5. the validity bits in (5.6) select exactly the cyclic windows that do not
   repeat a physical vertex before their last included position;
6. the partial-permutation coverage network is exact for those actual
   occurrences and has no occurrence-by-target selector product; and
7. the constant-trace residence exception and the component-voltage
   annotation are exact.

No existence result, simultaneous opening theorem, or current-code
implementation claim follows, and the theorem now says so.

Three narrow wording/implementation qualifications arose during the audit.
All three are now stated explicitly in the theorem note; Section 8 retains
them as warnings for downstream reuse.  None invalidates the normal form or
its asymptotic selector-free conclusion.

## 2. Slot-voltage equivalence

Let the quotient dart out of owner slot `i` be

\[
 U_i\longrightarrow \rho^{p_i}U_{\sigma(i)}.
\]

At the physical representative `U_i`, its outgoing neighbour is

\[
                         \rho^{p_i}U_{\sigma(i)},
\]

while, writing `h=sigma^{-1}(i)`, its incoming neighbour is

\[
                         \rho^{-p_h}U_h.
\]

Thus (2.2) is exactly the condition that the two incident physical edges
are distinct.  The local Johnson tests make both edges legal.

There is no untested duplicate edge orbit.  Two distinct quotient darts can
generate the same undirected edge orbit only if their unordered endpoint
owner pairs agree.  The only nontrivial possibility is a quotient 2-cycle,
where the reverse darts agree precisely when their two neighbours at either
endpoint agree; (2.2) excludes it.  A quotient loop can double an undirected
edge orbit only when `2p=0 mod n`.  Since `n=2r-1` is odd, this forces
`p=0`, which already fails the Johnson test `U_i~U_i` under the free owner
action.

Conversely, the quotient of an invariant degree-two factor is a degree-two
multigraph with loops counted twice.  Orienting each quotient circuit gives
one outgoing dart and one incoming dart at each owner.  Freeness gives a
unique phase on each outgoing dart.  Hence Theorem 2.1 is surjective as well
as injective at the physical-edge-set level, modulo the stated independent
orientation choices.

In the closing-voltage gauge for a quotient 2-cycle, the first dart has
phase zero and the return dart has phase `v`.  The two physical neighbours
coincide exactly at `v=0`, confirming the special sentence after Theorem
2.1.

## 3. Multi-track indexing and twisted boundary

Put `g=gcd(n,v)` and `m=n/g`.  Addition by `v` has the `g` coordinate
orbits

\[
 x_{h,q}=h+qv,qquad 0\le h<g,\quad q\in\mathbb Z_m.
\]

For each fixed `h`, the map

\[
 (j,q)\longmapsto j-q\ell\pmod {m\ell}
\]

is a bijection from `Z_ell x Z_m` to `Z_(m ell)`: reducing the image modulo
`ell` recovers `j`, after which division by `ell` recovers `q modulo m`.
Therefore (3.5) neither identifies nor omits a membership bit.

At the integer boundary `j=ell`,

\[
 c_h(\ell-q\ell)=c_h(-(q-1)\ell).
\]

Since `x_(h,q-1)=x_(h,q)-v`, this says

\[
 x_{h,q}\in M_\ell
 \quad\Longleftrightarrow\quad
 x_{h,q}-v\in M_0,
\]

which is exactly `M_ell=rho^v M_0`, with the sign in the theorem correct.
Consequently (3.7)--(3.8) count the actual insertions and deletions even on
the twisted closing seam.  Combining them with the top-bit change gives
the four Johnson cases in (3.10).

The bit census is also exact:

\[
 g(m\ell)=n\ell,
 \qquad
 \sum_C n\ell_C=nN=W.
\]

## 4. Trace orientation and residence

Start a lifted cycle at physical phase `a`.  If
`x-a=x_(h,q_0)`, then at physical time `q ell+j`,

\[
\begin{aligned}
 x\in\rho^{a+qv}M_j
 &\Longleftrightarrow x_{h,q_0-q}\in M_j\\
 &\Longleftrightarrow
 c_h(q\ell+j-q_0\ell)=1.
\end{aligned}
\]

Thus the sign of the shift in Corollary 3.3 is correct: every old-coordinate
trace is a cyclic shift of one exact track.  The top coordinate is fixed by
`rho`, so its trace is `t` repeated `m` times.

Under the explicitly stated finite physical-cycle convention, an all-one
trace on a physical cycle of length `L` is one positive run of length `L`,
not an infinite run.  Hence the additional test `L>=D` is necessary and
sufficient for an all-one component.  The complementary all-zero test is
likewise necessary for dual residence.  Corollary 3.4 is exact.

For a nonconstant cyclic trace, every positive run has zero boundaries, so
the cyclic motifs `0 1^s 0` enumerate the runs.  On a very short cycle the
two displayed boundary zeros may be the same physical position; this is an
implementation caveat recorded in Section 8, not a defect in the
mathematical motif statement.

## 5. Owner-transversal enforcement

The successor permutation by itself does not prevent two variable slots
from carrying the same middle-owner orbit.  The pre-patch formulation
therefore lacked a necessary global condition.

The current Theorem 5.1 repairs this exactly.  It is conditional on the
existing width-`N` middle-orbit partial-permutation network, and calls the
width-`N` successor network **additional**.  The two layers do different
jobs:

* the middle network makes `([M_i],t_i)` the complete owner transversal;
* the successor network chooses `sigma` and supplies predecessor/successor
  payloads for the local factor law.

Together they match the final condition of Theorem 3.1 and all hypotheses
of Theorem 2.1.  Alternatively one could fix a canonical representative of
each owner orbit as a constant, but then the `W+N` state bits would not be
free variables.  The current variable-slot interpretation correctly keeps
the separate owner network.

## 6. Successor Waksman exactness and size

A width-`N` rearrangeable Waksman setting implements an arbitrary
permutation `sigma`.  Forward traversal sends input `h` to output
`sigma(h)`, so output `i` receives its predecessor `h=sigma^{-1}(i)`.
Backward traversal of the same physical switches sends the payload at output
`sigma(i)` to input `i`, supplying the successor.  Therefore the same
controls correctly expose both

\[
               \rho^{-p_h}U_h,qquad
               \rho^{p_i}U_{\sigma(i)}
\]

at slot `i`.  No inverse-permutation error occurs.

The recurrence

\[
 S(M)=2\lfloor M/2\rfloor+S(\lceil M/2\rceil)+S(\lfloor M/2\rfloor)
\]

gives exactly

\[
                         S(858)=8078,qquad S(5148)=61680.
\]

Thus the retained coverage-control count

\[
 3S(858)+S(5148)=85914
\]

and the topology-extended count

\[
 85914+S(858)=93992
\]

are arithmetically correct.  They count permutation controls, not all CNF
variables or clauses, as the theorem now emphasizes.

The conservative successor auxiliary count is also arithmetically correct:

\[
 8078+2(16)(12)(8078)+858(4)+15(4)(858)(12)
 =3{,}731{,}222.
\]

It deliberately excludes the listed rank/Johnson, coverage, and validity
comparators.  One realization within this bound routes phase-aligned state
payloads: at each layer the successor payload is rotated by the local dart
phase before the next aligned state is stored.  Hence separate accumulated
phase payloads are not required merely to generate the windows.  Exact
return validity may equivalently compare the aligned state with its initial
state, using owner freeness; its equality gates are among the explicit
exclusions.

## 7. Eligibility, coverage, and voltage annotation

For start slot `i`, the lifted successor returns to its initial physical
vertex precisely when

\[
                    (\sigma^q(i),P_{i,q})=(i,0).
\]

The owner action is free, so no nonzero phase can fix the owner.  The first
return time is therefore

\[
                  \ell_C\frac n{\gcd(n,v_C)}.
\]

An interval containing `w` successive states is one-pass exactly when no
return occurs at a time `1<=q<w`, which is (5.6).  Equality at `q=w` is
allowed: `w` equal to the physical cycle length uses every vertex exactly
once.  This verifies both the strict inequality in (5.6) and the non-strict
eligibility bound in (5.3).

At fixed width, one quotient slot represents all `n` phase starts across
the lifted physical cycles.  These starts form one global rotation orbit,
even when `g>1`; global rotation permutes the `g` physical lifts.  Hence an
eligible quotient component contributes exactly `ell_C` occurrence-orbit
inputs, proving (5.4).

For distinct required target orbits, one actual occurrence cannot serve two
targets.  Thus exact coverage is equivalent to assigning distinct actual
inputs to the required outputs, choosing one rotation phase on each, and
routing that injection through a Waksman permutation.  Routing the validity
bit with the word and fixing it to one at each required output makes padded
inactive inputs harmless.  This proves the partial-permutation assertion
without `M D` selectors.

The new warning that these are cyclic one-pass windows rather than the
windows surviving one simultaneous set of cuts is essential and correct.
Opening and joining remain outside the theorem.

Finally, Proposition 5.5 has no hidden rootless-cycle solution.  The label
`a` is constant around each `sigma`-cycle.  If no slot were its root, the
integer order `h` would increase strictly around a closed loop, an
impossibility.  Once a root exists, `R_i iff a_i=i` and `a_i<=i` make it the
unique minimum-index slot.  The `q` recurrence telescopes from zero at that
root, and the sole entering dart records exactly the circuit-voltage sum.
The claimed `O(N log N+N log n)` stored arithmetic and shared-control mux
scale is therefore exact up to the explicitly stated gate-encoding choice.

## 8. Patched qualifications and downstream reuse warnings

### 8.1 “One-word” should be read componentwise

The verdict now correctly says: one quotient component with unit voltage
has one cyclic `c` track.  If several components all have unit voltage, each
has one track, but there are several separately cyclic words and their
relative voltages remain.  The earlier potentially ambiguous global
“one-word” reading has been removed.

### 8.2 Local Johnson rows alone give a twisted walk

Equations (3.9)--(3.10) alone give legal rank-`r` Johnson seams around a
twisted closed walk.  The theorem now uses exactly that term.  To obtain a
spanning simple factor component, one must additionally use distinct
quotient-owner slots and (2.2), as its following sentence states.  These
conditions must not be dropped when the local track equations are reused;
the length-two, zero-voltage backtrack is the sharp counterexample.

### 8.3 A short cyclic motif may repeat its boundary position

An implementation of Corollary 3.4 must enumerate cyclic runs rather than
only simple quotient paths.  For example, on the length-two trace `01`, the
short positive run has cyclic witness `0,1,0`, whose first and last zero are
the same physical position.  The constant-cycle row alone does not cover
this nonconstant case.  The theorem now states the repeated-boundary
convention explicitly; a future clause generator must preserve it.

## 9. Final proved boundary

The audited note proves an exact arbitrary-voltage, arbitrary-component
factor normal form and a polynomial compact fixed-catalogue projection.  It
does not prove that all component voltages may be normalized to one, that a
fixed upper catalogue is width-complete, that cyclic windows survive common
cuts, that components can be joined residence-safely, or that the common
compiler is feasible.  Those exclusions are stated accurately in its final
scope section.
