# Audit of the K17 joint recoupled-parent selector and first smoke CNFs

Date: 2026-08-03

Status: PASS for the Boolean pinned-parent smoke layer.  The emitted V1
generator is a proof-safe branch--Benders master only; it is not an exhaustive
common-basis/root-open selector.  The current bundles are synthetic fixtures,
not the real strict-`bf5b` role/state/incidence bundle.

This was a read-only/static audit.  No solver was launched in this lane.  The
already-emitted artifacts and their manifests were read and their checksums
were replayed.

## 1. Frozen provenance

The final bound files are:

```text
a584381ebb6a22e33580aca518be9539cd3a4c4e758c82e17b299a64125eadf2  generator source
d01f85bbeb3c9291d8c45133afca4e996f3f2faf7ea8c6ff9d4fc136e65705db  smoke driver
e85f2005f154790e94bfd64cedb283fc8da539013841c891b991b6e11f0533ea  PROOF_SAFE_MANIFEST.sha256
81ff2292095c57eef27e17c34dee1560de23aeeaa343c405e1d383bc17dcc124  frozen_tests/FROZEN_MANIFEST.sha256
```

The proof-safe manifest binds the source, test driver, README, synthetic
fixtures, cut witness/certificate/transcript, binaries, CNFs, DRAT artifacts,
and decoded candidates.  Its complete checksum replay passes.

The first positive smoke is:

```text
d4b49aba1a1cce2ab69cb4dde753ebd88337dfa9a1b6ef496239a1bf6f4d13b7  positive master.cnf
a886c92bcded3816f02e61d93a05de2dbd0df82bd9d9d04bee9896055395abc5  positive varmap
9081722f586691455a6197990039e9cc72bf430095830a00fb047839c285bfbc  positive build audit
db3d864d1958ebe71f9f8a59933fb2da7774737267dae8ac0130911a31e9fe01  positive assignment
```

The CNF declares 170 variables and 548 clauses; the emitted census agrees.

## 2. Boolean activation semantics

The positive varmap names, among others,

```text
MODE 0                 variable 1
ROLE_SUPPORT 0 phase0 variable 3
ROLE_SUPPORT 0 phase1 variable 4
ROLE_COMMON 0          variable 23
STATE_GROUP 0 phase0   variable 28
STATE_GROUP 0 phase1   variable 29
STATE_GROUP 5 phase0   variable 38
STATE_GROUP 5 phase1   variable 39
OCCURRENCE 0 phase0    variable 46
```

The literal clauses include:

```text
-1  23                 MODE0 -> ROLE_COMMON0
-23 1                  ROLE_COMMON0 -> MODE0
-28 3, -38 3           a phase-0 group -> phase-0 support
-28 -38                at most one phase-0 group
-3 28 38               support -> some phase-0 group
-46 3, -46 28          occurrence -> support and its declared group
-3 46                  complete-menu support -> its occurrence
```

The phase-1 clauses are analogous.  The common-group gates are exact ANDs of
the phase-0 and phase-1 group bits, and `ROLE_COMMON` is their exact OR.
Consequently, for a selected donor mode,

\[
 \boxed{
 \mathrm{MODE}_e
 \iff \mathrm{ROLE\_COMMON}_e
 \iff \text{one identical declared }(q,\alpha,\beta)
       \text{ is selected in both phases}.}
\]

The predecessor/successor physical occurrence rows may differ between
phases.  Complete menus make each supported role select exactly one literal
occurrence per phase.  Incomplete menus are an active-set relaxation and do
not produce a fully priced witness.

The separate phase, marginal-both, either, and common-state aggregates are
not collapsed.  The asymmetric fixture has `p0=1`, `p1=0`, `both=0`,
`either=1`, and `common=0`, as required.

Dynamic row prerequisites are also in the correct direction:

- a `BASE_LMR` occurrence requires that no selected mode consume its donor
  row; and
- a `SELECTED_LLR` occurrence requires its creating mode.

Protected rows are rejected as mode endpoints, short roles, occurrence long
rows, and root-action rows.

## 3. Pinned-face and cross-disjoint scope

The master uses one unit capacity per `(phase, physical long row)` across
both predecessor and successor uses.  Thus two different sockets cannot use
the same long row on opposite sides in one phase.  It represents the
cross-disjoint `c=0` occurrence face (apart from a single occurrence whose
predecessor and successor are literally the same row, which is counted once),
not the general cross-reused aperture.

This restriction is exact for that face but must be stated on every UNSAT or
support bound.  A global model allowing a role to be a predecessor of one
socket and successor of another needs separate in/out capacities plus their
cycle-cover coupling.

V1 now accepts only
`PINNED_PARENT_STATE_RELAXATION`.  An attempted manifest switch to
`EXHAUSTIVE_AUTHENTICATED_ROOT_STATE_COLUMNS` is rejected.  This closes a
previous over-scoping hole: no DRAT proof can acquire a global root-open label
from an unauthenticated manifest string.

`ROOT_ACTION` remains only an intent bit.  It conflicts with incident modes
and with a `BASE_LMR` occurrence pinning its row, but there are no
`a_lm/a_lr/a_mr/delta_m` presentation variables and no common-basis matching
inside the CNF.  Every SAT candidate therefore correctly returns
`NEEDS_ROOT_COMMON_BASIS_SEPARATION`.

## 4. Cut encoding and the 50-head contract

The generic cut circuit has the intended semantics:

- atoms in one disjunct are conjoined exactly;
- disjuncts of one term are ORed exactly; and
- a binary exact counter enforces the term threshold.

For an actual 50-head Hall row, however, syntactic exactness is not enough.
The production separator must have exactly one semantic term for every
`INACTIVE_HEAD(h)` and exactly one term for every distinct
`NEIGHBOR_SUPPLIER(u)`.  Alternative supports for the same supplier are
disjuncts of that one term.  The current generic term schema does not carry
those semantic keys, so uniqueness and supplier-OR coalescing must be proved
by its external verifier or added as a canonical credit ledger.

Cut authentication is now substantially fail-closed.  A witness binds the
parent, the semantic bundle digest, the cut-summary digest, the entire term
file, modes, roles, state groups, both phase incidence files, role summary,
root actions, oracle certificate, and verifier transcript.  Tampering with
the term file is rejected.

The remaining production-proof caveat is semantic replay: the loader checks
that a hash-bound key/value transcript says `VERIFIED`, but it does not itself
execute or verify the oracle certificate.  A real 50-head cut needs a bound
verifier source/executable and invocation, or a mechanically checkable
certificate consumed directly.  The synthetic `rho0 OR rho1` cut tests the
CNF and authentication plumbing; it is not an audit of the real 50-head
credit ledger.

Binding every witness to the whole term file is safe but makes incremental
Benders awkward: appending a cut requires reissuing all prior witnesses.  A
canonical per-cut slice digest is the clean future interface.

## 5. Negative smoke scope

The emitted negative regressions are:

```text
b04713d45482eaab6b33c0aa857f4275d4307251eb01389d2ee0a6b52975e02e  q-mismatch CNF
c71c1b0684f746ccb48b189d18cf403b2bcc699478d76fd7c2413cf27a626ffb  q-mismatch DRAT
cc1c299a022e3fd6e65f344b19ebb6932849b544af9988df924cc1b1f0e3bd83  root-cut CNF
8b8e0d7c8c8a465d814b74498ff91ec4f1b42b2dc2612a48cea28e6a01aaf896  root-cut DRAT
```

Their existing transcripts contain exactly one `s VERIFIED`, and the audits
correctly label both results
`STATIC_PINNED_PARENT_RELAXATION_UNSAT_DRAT_VERIFIED`.  They are not global
common-basis/root-open cores.  Additive accounting, term-file tampering, and
an exhaustive-root-scope spoof are rejected.

## 6. Singleton-root interface

The fully priced singleton request now binds the corrected singleton theorem
SHA, semantic bundle, parent, mode and phase catalogues, protected ledger,
root-action catalogue, complete assignment, selected modes/roles/groups/
occurrences, and selected actions.  It records the corrected predicate

```text
edge is in the chosen perfect matching
OR endpoints share an alternating SCC.
```

If active-set pricing is incomplete, the source emits a blocked marker rather
than an SCC request.  This correctly enforces recomputation after final phase
pins.  The incomplete-menu fixture exists, but this blocked path is not yet
exercised by the frozen regression script; adding that regression is advised.

No phase-pinned SCC implementation is included yet.  The request is an
external-oracle handoff, not a survivor certificate.  Singleton survivors do
not compose, and their supplier credits depend on the chosen low child and
literal completion.

## 7. Exact conclusion

The first smoke CNFs correctly implement the declared Boolean pinned-parent,
common-state, cross-disjoint occurrence layer.  They do not supply a
polynomial separator over common-basis elements alone, because neither the
representing matchings nor the residual root/occurrence completions are in the
master.

The proof-safe architecture is therefore unchanged:

1. branch on/lift a literal mode and phase-state assignment;
2. complete or reject it with the augmented common-basis/root matching oracle;
3. materialize the supplier graph;
4. separate it by maximum matching/min-cut; and
5. add only a canonical Hall cut proved valid for every residual completion
   represented by that branch.

A real strict-`bf5b` role/state/incidence bundle, the phase-pinned singleton
oracle, the production 50-head semantic credit ledger, and the full augmented
common-basis representation remain open.
