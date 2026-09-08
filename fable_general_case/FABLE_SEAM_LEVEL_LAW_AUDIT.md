# Audit of Fable's failed seam-level proof attempt

## 1. Scope and verdict

This audits the raw Claude trace

`5d106b46-3000-4132-9735-c4e3ac4b59ca.jsonl`

at assistant UUIDs

- `f610e248-9eb5-4486-b8ce-e9ad960c3469`,
- `a936767c-7714-4d67-8c7a-b10e0a6f0e11`,
- `7942ed12-6d26-40db-9a2c-6cb204e13b4e`, and
- failed edit `58953b6f-5af3-40e1-90ba-f720f67bfe90`.

I compared it with the independently audited statements in
`FABLE_RUN_SPECTRUM_AUDIT.md`, `FABLE_INTERVAL_SUPPLY_AUDIT.md`,
`MIXED_PROFILE_CROSSLINE_AUDIT.md`,
`GENERAL_BOUNDARY_RESERVOIR_AUDIT.md`,
`POSITIVE_SEAM_CROSSLINE_COUPLING_AUDIT.md`, and
`THREE_HALVES_TRANSITION_GEOMETRY_AUDIT.md`.

**Verdict:** the trace does not prove a seam-level law and does not exclude
the balanced abstract survivor `mu=2 delta_(4/3)`.  No new unconditional
theorem should be entered in the handoff from this attempt.  The attempted
`Edit` was rejected, and the persisted raw tool input ends after 2048 bytes,
in the middle of the definition of a seam.  Consequently there is no
complete formal proof artifact to audit; the only complete record is the
exploratory thinking trace.

The attempt does, however, isolate a useful conditional skeleton: a regular
`4a/3` plateau has a rising cross-coordinate ending near or above `a/3`, and
there are too few positive high levels to absorb the rising cross of almost
every plateau.  The missing theorem is precisely the quantitative passage
from a nonabsorbing seam to enough cheap, bounded-congestion run service.

## 2. Earliest unsupported inference

The first fatal inference occurs in `a936...`, paragraphs 47--49.  The trace
claims that the tail inequality forces **every** length-`(4a+2)` window to
contain a regular plateau of cost `(4/3+o(1))a`, and therefore

`q_i <= (4/3+o(1))a`

for every index.  It then combines this alleged pointwise upper bound with
the lower sum law to conclude

`q_i=(4/3-o(1))a`

for all but `o(a^2)` indices.

Neither implication follows.  The audited facts are only

\[
q_i\le 2a,
\qquad
\sum_i q_i\ge (4-o(1))a^3,
\]

and, for each **fixed** `delta>0`,

\[
#\{i:q_i>(4/3-\delta)a\}
\ge
\left({3\delta\over 2/3+\delta}-o(1)\right)a^2.
\]

This is a positive-density conclusion, not an almost-everywhere conclusion;
its coefficient tends to zero with `delta`.  As already demonstrated in
`FABLE_RUN_SPECTRUM_AUDIT.md`, even the full abstract capped spectrum is
compatible with `3/5` of the indices having cost `a` and `2/5` having cost
`2a`.  Thus the lower sum law cannot supply the missing pointwise upper
bound or concentration.

The sentence about plateau spacing being “roughly `(3/2)a`” does not repair
the argument.  Atomic convergence determines total plateau count and edge
mass, but it gives no uniform upper bound on individual complement gaps and
does not make every window meet a regular selected plateau.

## 3. Consequences that therefore fail

Everything below depends on the preceding concentration step.

### 3.1 Peak-free gaps and valley normal form

Paragraphs 51--59 assert that almost all desert gaps contain no short peak,
so every coordinate is valley-shaped in almost every seam.  This uses the
unproved assertion that only `o(a^2)` window starts may see a cheap peak.
The audited run spectrum permits a positive density of such starts.
Therefore peak-free gaps and the global valley normal form are not proved.

### 3.2 “Next level or poison”

Paragraphs 107--121 and 153--175 try to show that a rising cross-coordinate
must either become the fixed coordinate of the next selected plateau at a
level at least `a/3`, or create a cheap peak.  There is a plausible local
threshold-component mechanism here, but the trace does not prove the needed
global alternative:

- a superlevel component may pass through gap positions and partial pieces
  of later plateaux;
- its maximum plateau may be an intermediate directed peak of cost up to
  `a`, not the `o(a)`-cost “poison” subsequently budgeted;
- several seams may be discharged by the same later component;
- word-boundary escapes and the multiplicity of the seam-to-run map are not
  bounded; and
- a long threshold component is not automatically a constant-coordinate
  plateau, as emphasized in `FABLE_RUN_SPECTRUM_AUDIT.md`.

The trace repeatedly notices these issues and changes the proposed poison
cost from near `4a/3`, to `a`, to `o(a)`, without supplying one invariant
definition or a complete case proof.

### 3.3 Poison accounting

Paragraphs 123--151 and 181--235 require `o(a)` poison seams.  No valid
charging lemma is given.  In particular, the proof needs all three of:

1. a cheap span-bounded run for every nonabsorbing seam;
2. a quantitative cost gap below `4a/3`; and
3. bounded congestion when seam service intervals overlap.

The trace proves none of these jointly.  Theorem I bounds the number of
indices at which a chosen run has cost at most `t`, not the number of seams,
unless a bounded-multiplicity seam-to-index assignment is first constructed.
Moreover, at proportional thresholds its direct exceptional bound is
generally `Theta(a^2)`, not `o(a^2)`.  Formulas such as the claimed
`pi(x)` bound and the `27/8` poison coefficient appear during exploration
without a derivation that survives these overlap and cost issues.

### 3.4 Static ledger versus an ordered word

Several earlier statements are exactified beyond what the audited limiting
ledger says:

- `mu -> 2 delta_(4/3)` gives `(2+o(1))a` selected plateaux, with all but
  `o(a)` regular; it does not give exactly `2a` identical plateaux;
- `Delta=0` gives `|Lambda\V|=o(a^2)`, not literal pointwise tiling;
- hence all but `o(a^2)` complement positions are outside selected lines,
  not every gap position;
- `Gamma=Gamma_0=2/9` is one consistent static choice, not a forced value.
  The atomic inequalities allow larger `Gamma` as well.

Accordingly, arguments that distribute exact desert mass among exact seam
lengths do not follow from the abstract survivor.  This is the same
atom-to-order gap explicitly retained in
`POSITIVE_SEAM_CROSSLINE_COUPLING_AUDIT.md`.

## 4. Salvageable rigorous statements

The following deductions are valid and worth retaining.

### Lemma 4.1: rising-end height

Let `P` be a directed plateau with edge length `lambda`, and let `xi` be its
strictly increasing cross-coordinate.  Since `xi` is integer-valued and
lies in `[-a,a]`,

\[
xi(\operatorname{end}P)-xi(\operatorname{start}P)\ge\lambda,
\]

so

\[
xi(\operatorname{end}P)\ge\lambda-a.
\]

For a regular `4a/3` plateau this is

\[
xi(\operatorname{end}P)\ge(1/3-o(1))a.
\]

This is the rigorous content behind “the rising cross must reach `a/3`.”

### Lemma 4.2: high-level capacity

A plateau of edge length at least `(4/3-epsilon)a` on level `t` obeys

\[
|t|\le 2a-\lambda\le(2/3+\epsilon)a.
\]

If it also has positive high level

\[
t\ge(1/3-\epsilon)a,
\]

then there are at most

\[
(1/3+2\epsilon)a+O(1)
\]

available levels in one direction, hence at most

\[
(1+6\epsilon)a+O(1)
\]

across all three directions.  Two such plateaux cannot reuse one geometric
line for small fixed `epsilon`, because each has more than `a` edges while a
line has at most `2a` edges.

### Corollary 4.3: conditional seam-capacity contradiction

Under `mu -> 2 delta_(4/3)`, there are `(2+o(1))a` regular plateaux.  If one
could prove that all but `o(a)` of them have positive high level as a
consequence of their predecessor seam, Lemma 4.2 would give only
`(1+o(1))a` available slots, a contradiction.

This conditional deduction is correct.  It is not yet an exclusion theorem,
because the hypothesis “all but `o(a)` seams are absorbing/high” is exactly
the unproved poison-accounting step.

## 5. Correct next lemma

The useful research target exposed by the failed attempt is:

> **Quantitative seam alternative.**  For consecutive regular directed
> `4a/3` plateaux, either the predecessor's rising cross is absorbed as a
> positive high level by a controlled nearby selected plateau, or the seam
> can be charged to a span-`(4a+3)` internal run with a fixed positive cost
> deficit below `4a/3`; every run/index may receive only `O(1)` charges.

To kill the atom, its constants must force `o(a)` nonabsorbing seams, not
merely a positive-density set of absorbing seams.  A proof must explicitly
handle partial crossings of later plateaux, intermediate directed peaks of
length at most `a`, overlap of service intervals, and both word boundaries.

Until such a lemma is proved, “the rising cross reaches `a/3` but has nowhere
legal to go” is a useful geometric slogan, not a theorem.

## 6. Ledger

- **New unconditional theorem from this attempt:** none.
- **Valid reusable lemmas:** rising-end height; high-level slot capacity.
- **Valid conditional conclusion:** almost-all high absorption contradicts
  the `2 delta_(4/3)` atom.
- **Still conjectural:** the quantitative seam alternative and exclusion of
  the balanced atomic survivor.
- **Broader claims unsupported:** exclusion of every atom on
  `[4/3,3/2]`, stability for nearby non-atomic profiles, and any general
  three-box contradiction derived from this seam law.
