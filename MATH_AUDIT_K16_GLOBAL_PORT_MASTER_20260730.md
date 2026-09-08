# Independent audit: K16 separated global-port master

Date: 2026-07-30

## Verdict

**GO**, within the model's explicit scope: direction-coherent global port
permutations of the frozen length-eight source, with cuts at cyclic distance
at least four, positive-residence-safe Johnson seams, and exact signed fixed
shadow rows through `q=3`.

The audited corrected driver is
`scratch/solve_k16_len8_physical_93_multicut_cegar_20260730.py`, SHA-256
`9150ea422129bc667f74b8f52e82b26749729cf5dfc13ad9ae26ed0646a30944`.

An UNSAT result from this master is **not** an unrestricted K16 no-go.  It is
only a no-go for this separated, direction-coherent, source-relative port
permutation class.  A capped or UNKNOWN solve is no mathematical verdict.

## Rejected draft and exact counterexample semantics

The earlier draft, preserved on the H100 with SHA-256
`d8b5e39042234a8c7246139942e35891ae4db489a65bd3e26280c32615025dc0`,
combined:

1. additive rows containing upper windows of width five; with
2. only four-position cut exclusion, so cuts at source positions `p` and
   `p+4` were simultaneously legal.

That combination was unsound.  One width-five source occurrence can contain
both cuts.  The two one-seam gain/loss deltas are each computed against the
unchanged source context, so their sum need not equal the occurrence ledger
after both seams are installed.  This is an interaction term, not numerical
slack.

Either five-separation or removal of width-five additive rows fixes it.  The
corrected driver takes the latter route: all additive rows have width at most
four, and every four consecutive source transitions contain at most one cut.

## Complete independent ledger comparison

The checker
`scratch/audit_k16_global_port_master_binary_crosscheck_20260730.py` rebuilt
the Python catalogue and compared it with the independently emitted C++
binary catalogue
`scratch/k16_len8_source_seam_ledger_20260730.bin`.

It checked, without a solver:

- all 12,870 source transition records;
- every baseline load at all 65,536 masks in each of six families;
- every source occurrence-loss multiset in lower/upper q1, q2, and q3;
- every occurrence-gain multiset of all 211,604 directed seams in those six
  families; and
- the two frozen physical hole banks (45 lower-q2 and 48 upper-q3 masks).

Result:

```text
PASS_FULL_211604_SEAM_CROSSCHECK
transition_ledger_sha256 = dd88ddc704cb9a69ccf8302129cbf7badd015c437639f97c103a38e0212a2a92
seam_ledger_sha256       = c649c9e67b0bfe2559466f5461fb4a12bc484cc3edb2a125c799fea6eb223840
```

Audit artifact:

```text
scratch/k16_global_port_master_binary_crosscheck_20260730.audit.json
SHA-256 5608c32fa349ca78d3ccf5a956d6077bc13350be6d4e1f9b6125c9fb125b1d54
```

## Physical directed two-cycles

The corrected model explicitly forbids:

- a selected new edge whose reverse remains as an uncut old edge; and
- a pair of selected new edges that are mutual reverses.

The independent edge census found:

```text
old/new reverse rows = 0
new/new reverse rows = 26,233
total                 = 26,233
```

This exactly matches the built CP-SAT model.  Same-direction duplicate new
edges do not exist: the seam's left port fixes its tail and its right port
fixes its head.

## Frozen length-eight regression

The corrected driver solver-freely replayed the known fifteen length-eight
port cycles (120 selected seams) from the triangle source.  It verified:

- distinct cut rows and columns (a port permutation);
- cyclic cut distance strictly greater than three;
- admissibility of all 120 seams;
- absence of every physical directed two-cycle;
- equality of the signed additive ledgers and literal physical replay;
- positive residence and a simple spanning two-factor; and
- exact equality with the frozen repaired successor factor.

The signed and physical hole profile is intentionally

```text
lower q1 = 0, upper q1 = 0,
lower q2 = 45, upper q2 = 0,
lower q3 = 0, upper q3 = 48.
```

This regression validates the encoding and known descent; it is not a witness
for filling all 93 remaining holes.

Artifact:

```text
scratch/k16_global_port_master_length8_regression_20260730.audit.json
SHA-256 76d0118257a907d663124dd2a8fac37f6098eb00a56130c0f2cf2ecbc2be0878
```

## Built target model

The audited H100 build has:

```text
valid directed seams = 211,604
variables            = 224,475
constraints          = 112,477
reverse-edge rows    = 26,233
model text bytes     = 54,791,764
```

All six signed target/preservation row families are literal physical-mask
rows, not orbit totals.  Every incumbent is additionally materialized and
audited against all fixed lower shadows and arbitrary upper intervals.  An
incumbent that fails the physical audit is excluded by an exact assignment
no-good, so the CEGAR loop is sound although potentially weak.

