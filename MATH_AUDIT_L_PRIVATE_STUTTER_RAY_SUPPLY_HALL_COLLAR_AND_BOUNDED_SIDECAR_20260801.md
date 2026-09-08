# Audit: private-stutter supply, collar compatibility, and bounded sidecars

Date: 2026-08-01  
Audited theorem:
`MATH_THEOREM_L_PRIVATE_STUTTER_RAY_SUPPLY_HALL_COLLAR_AND_BOUNDED_SIDECAR_20260801.md`  
Status:
`PASS_AFTER_ORIENTED_CENTER_CAP_AND_ONE_WRITER_GUARD_CORRECTIONS`.

This is an independent symbolic audit.  No solver or large finite census is
used.  A tiny depth-one replay was used only to corroborate the explicit
long-path example.

## 1. Native collar row

For adjacent selected states, individual same-neighbour legality certifies
three sides of the state square.  The fourth side is literal exactly when

\[
       X^t_i\triangle\widehat X^t_i
       \subseteq B_{t+1}\cap\widehat B_{t+1}
       \qquad(0\le i<d).
\]

There is no transition shared by nonadjacent selected centers.  Hence these
are all native compatibility rows and every passing phase family is a
Boolean cube.

The OR-ray invariance proof also checks.  A site's write difference is
contained in the next newborn in both phases.  Any later ray interval which
contains the write also contains that masking newborn.  Future writes lie
outside the interval.  Distinct centers have distinct right endpoints, so
their occurrence-labelled ray cells are distinct.

The depth-one `A,X,H` example literally satisfies both individual
retimings, while the joint phase requires the false transition `H\to H`.
It is a valid smallest positive-cell adjacent warning.

## 2. Site-selection rows

On a genuinely opened independent chronology bank, compatible site choice
is an ordinary distinct-representative problem, so the stated Hall
inequalities are iff.  The `3h-2` bound is the exact simple greedy estimate:
each previous center forbids at most itself and its two path neighbours.

For ordered interval menus, the earliest recursion

\[
       \rho_i=\max\{a_i,\rho_{i-1}+2\}
\]

is componentwise no later than any feasible choice.  Its deadline test and
closed maximum formula are therefore exact.

The original guard-DAG wording needed an additional scope row.  The patched
version requires at most one selected writer per guarded resource and
old/new/indifferent unary phase reads, with boundary sentinels.  Each guard
then gives one fixed precedence arc, and acyclicity is necessary and
sufficient.  With multiple writers, the theorem correctly leaves a general
guard-order CSP.

The oriented-candidate master now also uses capacity one per physical center
and pair-specific failed-cross conflicts.  This prevents two alternative
phases at one occurrence from being selected as distinct sites.

## 3. Pin-contracted compiler Hall

For a selected path tuple, remove `Q_1,\ldots,Q_h` from the residual target
shore and remove the complete selected ray union from the residual cell
shore.  Hall matches precisely the remaining targets.  Adding
`Q_i\lambda_i` for `1\le i<h` saturates the intermediate rows and leaves
`\lambda_0` free.

After toggle `i`, the new port has value `Q_{i+1}`.  Relocating the
`Q_{i+1}` edge from `\lambda_{i+1}` frees the next port; the last port
installs `Q_h`.  Conversely, deleting the pins from any serialization of
this stipulated form leaves exactly the residual matching.  This proves the
iff with its declared scope.

For disjoint selected rays,

\[
 |D(P)\cap N(A)|
   =\sum_{i,p}y_{ip}|R_p\cap N(A)|,
\]

so the Benders cut coefficients are literal.  The theorem makes no
fractional-hull claim.  It also correctly fixes one complete cap state
`\theta`; Hall in a union of cap graphs would reverse the existential
quantifiers.

The interval-neighborhood reduction remains valid after arbitrary deleted
cells: a deficient target family has a deficient interval component.
For laminar neighborhoods, its maximal distinct members are disjoint, so a
deficient sum contains one deficient laminar member.

## 4. Bounded-sidecar rows

The common-reserve corollary is sound because one residual matching avoids
the entire declared candidate-ray bank.  Adding the selected intermediate
pins then invokes the contracted Hall theorem directly.

The fixed-matching network is exact on its explicitly background-fixed,
longest-port handoff face.  Integral paths are precisely free-root,
matched-port continuation, and terminal-hole relocation chains.  Site and
target capacities make simultaneous paths disjoint.  A path-length bound
`L` gives at most `HL` stutter occurrences; min-cut alone gives no such
bound.

Rado's criterion is used only after full path macros, compiler state, and
collars have been contracted into a certified laminar matroid.  Merely
laminar physical intervals do not form that matroid.

## 5. Counterexamples and final scope

The two-target, three-cell example proves that individual ray privacy does
not compose.  The packet example `P,Q,R` violates matroid augmentation.
The nested-guard two-cycle proves that laminar supports alone do not order
writes.

The doubled-`X_0` depth-one construction is literal.  It supplies `q_0`
twice, every `q_i` for `1\le i<N` once, and `q_N` zero times.  Relative to
the declared matching, the reachable relocation graph is the unique
`N`-site path.  Thus reachability and min-cut one can require arbitrarily
many consumed stutters.

Verdict:

\[
\boxed{\text{PASS at fixed-cap, occurrence-labelled,
one-writer/background-fixed scope}.}
\]

The audit does not establish a dimension-uniform site reservoir, a
coindependent compiler bank, bounded relocation diameter, or
`B(k)+O(1)`.
