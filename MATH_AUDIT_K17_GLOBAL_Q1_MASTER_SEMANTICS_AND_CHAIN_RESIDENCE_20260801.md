# Global-q1 master: clause semantics pass, composed residence fails

## Status and scope

This note independently audits the SAT artifact

```text
/dev/shm/k17_global_q1_master/run3_j4_k32_socket256
```

for the `k=17` global immediate-upper (`q1`) master with optional sockets,
the global cap-32 provider atlas, and macros J1--J4.

The q1 clause semantics are exact and the SAT model satisfies every encoded
clause.  The decoded construction is nevertheless **rejected**: composing
individually resident provider seams produces 143 nonresident complete
chains.  This note is not a `k=17` construction certificate.

The audited CNF has SHA-256

```text
2627e7b2277176474b3c5b7256b4e469c550b7c9eb289de72bc65604c8a4c1a4
```

and the retained SAT output has SHA-256

```text
e07868507317f79ea2bfd23155e1403835f08922089c216da45b12084d77ce32
```

## 1. Fail-closed semantic checklist

| gate | result | exact audit |
|---|---:|---|
| complete SAT assignment | PASS | 1,440,814 variables assigned; zero assignment conflicts |
| all CNF clauses | PASS | 7,015,468 parsed; zero unsatisfied and zero unknown |
| socket target groups accidentally ALO-forced | PASS | zero matching positive group clauses |
| provider target groups accidentally ALO-forced | PASS | zero matching positive group clauses |
| macros accidentally forced | PASS | zero positive macro unit clauses |
| old q1 edge multiplicity | PASS | exactly one old edge for each of 19,448 rank-10 colours |
| exact physical q1 clauses | PASS | all 19,448 reconstructed clauses present exactly once |
| literal socket target | PASS | every one of 49,243 socket rows physically delivers its named target |
| provider seam schema | PASS | 329,738 rows previously replayed; all individually resident |
| J1--J4 literal decks | PASS | zero delivery mismatch; zero individual residence failure |
| J1--J4 cut implications | PASS | all 20 expected conditional clauses present |
| selected-provider indegree/outdegree | PASS | endpoint replay finds no capacity error |
| selected-provider cycles | PASS for this model | zero cycle components |
| complete provider-chain residence | **FAIL** | 143 bad chains, 172 bad internal runs |

The independent full-model replay is
`scratch/k17_global_q1_master_semantic_audit_20260801/independent_model_check.txt`.

## 2. Exact q1-clause reconstruction

For each rank-10 colour `y`, the audit independently reconstructed the
literal delivery clause from physical owners:

\[
 \bigvee_{e:\,c(e)=y}\neg z_e
 \quad\vee\quad
 \bigvee_{s:\,y\in U(s)}x_s
 \quad\vee\quad
 \bigvee_{p:\,y\in U(p)}x_p
 \quad\vee\quad
 \bigvee_{J:\,y\in U(J)}x_J.                \tag{2.1}
\]

The four terms are respectively:

1. every old owner edge of colour `y`, guarded by its noncut literal;
2. every physical adjacency created by a socket row, including both guard
   seams and all consecutive facet owners;
3. every corrected one-facing external provider seam of colour `y`;
4. every hard-coded delivery of J1--J4.

After sorting and deduplicating literals, the 19,448 expected clauses
contain 485,312 literal occurrences.  Scanning the complete 127 MB DIMACS
found every expected clause exactly once, with no missing or duplicate
clause.

The field `child_colours` in a socket row is its cut-casualty ledger, not
its created q1 deck.  The audit therefore reconstructs the latter directly
from literal owner adjacencies; it does not incorrectly equate the two.

There are 1,872 unit cut clauses.  These are legitimate instances of
(2.1) for colours having only their old uncut delivery in the sparsified
master; they are not unconditional macro-cut assertions.

## 3. Optionality and J1--J4 conditioning

In global mode the builder omits both the ALO and AMO target-group loops
used by the staged solver.  Socket and provider occurrences are therefore
optional physical packets selected only when they help satisfy a global
colour clause.  J1--J4 each receive a separate optional variable; none has
a positive unit clause.

Every macro cut is encoded one-way:

\[
 x_J\Longrightarrow z_e
 \qquad\text{or}\qquad
 x_J\Longrightarrow\neg z_e.                \tag{3.1}
\]

The exact 20 expected binary clauses are all present:

* J1: four forced and two forbidden cuts;
* J2: three forced and two forbidden cuts;
* J3: four forced and one forbidden cut;
* J4: three forced and one forbidden cut.

Thus an unselected macro does not impose its cut pattern.  Owner conflicts
with sockets and provider ranges are likewise conditional on the macro
variable through the physical position-capacity buckets.

J4 is the literal path

```text
8152,8090,69530
```

using owner positions `155:0,282:1,282:2`.  Its adjacent unions are exactly
`8154,73626`; it has no short internal positive run.  Its cuts are
`155:1,282:1,282:3` forced and `282:2` forbidden, all conditionally on J4.

Only J1 is selected in the audited SAT assignment.

## 4. Endpoint capacities are sound but residence is noncompositional

Provider occurrences are grouped by exact physical range.  For each range,
the master enforces:

* at most one selected occurrence using the range as a left endpoint;
* at most one using it as a right endpoint;
* one common orientation if both roles are used;
* one physical range-use token in every occupied owner-position bucket.

This deliberately permits a range to be the right endpoint of one provider
and the left endpoint of a second, thereby forming a longer directed chain.
The decoded model has:

```text
1,815 selected providers
3,148 provider ranges
482 ranges used as shared middle fragments
1,333 path components
0 cycle components
```

Every selected two-range provider passed its individual residence test.
That test is not compositional.  A coordinate run can touch the exposed
boundary in each pairwise test and become a short internal run when a third
fragment is attached.  Literal whole-chain replay finds:

```text
143 bad path components
172 short internal positive runs
```

This is the unique decisive unsoundness in trusting the SAT result as a
resident construction.  It does not invalidate the q1 palette clauses.

## 5. Required correction

There are two proof-safe repairs.

### Conservative isolated-seam mode

For every exact provider range, place **both endpoint roles together** in
one AMO constraint.  Equivalently, forbid a range from being selected once
as a right endpoint and once as a left endpoint.  Every provider component
then has one seam, so the already authenticated pairwise residence audit is
complete.

### Exact chain-state mode

Keep provider chains, but propagate the boundary run-state of all 17
coordinates through the selected successor relation.  Reject a transition
whenever it closes a positive run of length less than four.  A lazy exact
variant decodes each SAT model and adds a blocking clause for every bad
selected provider chain; residence must be replayed after every solve.

The exact lazy blocker bank extracted from this assignment has 152 clauses:

* 151 binary clauses exclude the bad adjacent-provider pairs detected by
  three-fragment replay;
* one ternary clause excludes the sole bad full-chain run not exposed by any
  adjacent pair;
* no quartic or longer clause is needed for this assignment.

This 152-clause bank is the minimal model-specific CEGAR repair found by the
independent replay.  By contrast, blocking each of the 143 bad components as
a whole gives a conservative 143-clause bank.  Neither bank is a static
all-model residence theorem: after every subsequent SAT solution, the
complete selected chains must be reconstructed and replayed, with new exact
blockers added as necessary.  A direct chain-state automaton would make that
closure eager instead.

The first lazy round confirms that warning.  The formula obtained by adding
the original 151 binary pair clauses (but not its one ternary clause) is SAT
and passes full CNF replay.  Its selected provider graph has 1,860 edges and
1,348 path components, but 174 components contain 217 short internal runs.
Its new minimal blocker bank has 192 clauses: 191 binary and one ternary.
Thus model-specific pair blocking merely moves the defect unless blocker
banks are accumulated and full-chain replay is iterated to a fixed point.

Independently, directed cycles remain a required lazy gate in future
models.  This SAT model happened to have none; the base builder does not
make acyclicity automatic.

## 6. Verdict

The global q1 master is **palette-sound**:

* optionality is encoded correctly;
* every old, socket, provider, and J1--J4 delivery appears in the exact
  all-colour clauses;
* macro cuts are conditional;
* the retained SAT assignment literally satisfies the CNF.

It is not yet **construction-sound** because whole-chain provider residence
was omitted.  The run3 SAT result must not be cited as a `k=17` upper bound
or carrier until a corrected no-chain or chain-state model is SAT and its
complete literal paths are replayed.

The audit artifacts are:

```text
semantic q1/CNF audit
75c61a90b1b455c3c7f53055ab27d0982e0b6397eda1a13ad876a8f87428097f

independent SAT model replay
9cfe96dd8d4facdb30f2ffabcbd07a84d689ea0461622cb3c024600c1c3b1b08

provider whole-chain residence replay
87bd155596c580ac2698b3818b240eb36c7c58bb888180bf860faccc07fcd07c

authoritative remote chain-residence audit
1f1f17afa6ed62101dc4fa9f6df10fde00195d2ee6d53d70c092008533198939

minimal 152-clause model-specific blocker bank
928a7690e0b009f52643eb55d07e93529d5cfe67159f39225e521c130aad3b0d

conservative 143-component blocker bank
ec284914fb91d66f53d7495a918d4e21b03faf93a073da79f12156b1261ca1eb

independent chain-residence checker source
4f2e8fdef3ab71f48d7910b2e09dc446a9d11bb7b66b55510e771a4411e23fc1

first lazy-round chain audit
521657000906767c2d23922bf39bb5c787caa4e4da19696f4608e1a03a4e76c3

first lazy-round 192-clause blocker bank
1ae647aba9899b3069e91323dfee53613e4bd909abb8c428e5845e450a312f34
```
