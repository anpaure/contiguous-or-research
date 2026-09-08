# Audit of Claude's `opusproblem/work` update

Date: 2026-07-29

Scope: the newest local delta in
`/Users/amir.nuriyev/Downloads/opusproblem/work`, together with the live
H100-CPU runs launched from that copy.  This is a soundness and provenance
audit, not a claim that every older exploratory file in the directory has
been certified.

## 1. Authoritative new files

At audit time the only substantive source/document updates after the prior
snapshot were:

| file | local modification time | SHA-256 |
|---|---:|---|
| `cword.py` | 2026-07-29 13:03:53 | `006fe8ef2600491518b82a075a5d9c27e751f73b0bc30af1c0c1dd611256b452` |
| `LEDGER.md` | 2026-07-29 13:05:05 | `a548ed88f5249296a3a7e46483951cb76f9a33c7b93ce874c8bbc54d46282a84` |
| `GENERAL_CONSTRUCTION.md` | 2026-07-29 07:40:22 | `c904137c6b0d07407f9df768e59eb02109215b825ec8ddd6fd5a84712af12890` |

No new `k=15` word or decorated-carrier `PASS` artifact was present.  The
rigorous bound remains

\[
                 6438\leq \nu(15)\leq 6458.
\]

Both markdown files still quote the obsolete upper bound `6459`.

## 2. Genuine mathematical advance

The single-trace reduction is real.  For a normalized strict unit-voltage
spiral, one cyclic binary word `c` of length `W=kN` determines the carrier:

\[
 T_i=\{x\in\mathbb Z_k:c_{i-xN}=1\}.
\]

Class sums, minimum positive-run length, and one positive-run start and end
in every residue class modulo `N` give an exact Johnson/residence normal
form.  The physically correct version is recorded in

* `MATH_THEOREM_STRICT_SPIRAL_EVENT_STREAM_LIFETIME_AND_DUAL_RESIDENCE_20260729.md`;
* `MATH_DESIGN_K15_ALPHA_BETA_LIFETIME_BENDERS_20260729.md`.

In particular, if

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\},
\]

then every fixed-width lower intersection is obtained by deleting the
corresponding `alpha` prefix, and every upper union by adding the
corresponding `beta` prefix.  At `k=15` the smallest exact schedule master
has only 429 positive lifetimes and 429 following zero gaps, fixed sums, and
two `AllDifferent(429)` residue constraints.  The authoritative resident
seed is reproduced exactly in this representation.

This is the useful content of the update: it replaces a large circuit model
by an exact run/event schedule and makes complement duality literal (positive
lifetimes control lower rank exactness; zero gaps control upper rank
exactness).

One notational correction is essential.  The quotient deletion and
insertion labels are maps `Z_N -> Z_k`; they are not permutations when
`N != k`.  The two permutations are the residue classes modulo `N` of the
lifted run starts and run ends.

## 3. What `cword.py` proves

Positive output is sound for its printed strict sufficient class:

* the eager class-sum, cyclic-residence, and run-start/end transversal
  constraints are literal;
* the physical audit checks middle and first-shadow orbit collisions,
  depth-two misses, and all upper masks;
* a reported `PASS` can therefore be exported and independently checked.

Its negative conclusions are deliberately limited:

* every cover retains only the 150 cheapest selectors;
* upper cover clauses inspect only three near-minimal widths, although the
  final physical audit correctly checks arbitrary widths;
* zero depth-two misses are required, even though the exact linear compiler
  can absorb a small number of boundary exceptions;
* cyclic residence is stronger than cut-dependent linear residence.

Consequently, an `UNSAT` containing capped cover clauses is inconclusive.
The code now drops such clauses.  An eventual `UNSAT` using only accumulated
relational middle/first-shadow collision cuts is sound only for the strict
binary-c-space class.  It is not a lower bound on `nu(15)`.

The earlier unseeded warm-start crash has been fixed: when `anchor_c` is
`None`, the current source disables drift minimization and radius before it
dereferences the anchor.  The already-terminated `k=13` process was not
restarted after this fix, so there is still no new `k=13` result.

Two further scope qualifications are now explicit.  `extract_cw()` cannot
gauge literally *any* voltage to one: this requires `gcd(v,k)=1`.  This does
not make a positive `PASS` unsound, because the reconstructed physical trace
is audited, but it makes the docstring too broad.  Also, start/end
transversality gives rank plus Johnson adjacency, not first-shadow rainbow;
the latter remains a separate lazy collision/coverage condition.

## 4. Compiler/readiness overclaims in the notes

`sandwich2.py` produces sound positive words, but it is not a universal
exact compiler.  For derivative rows above row zero it enumerates only an
envelope and masks obtained by deleting at most two elements.  Therefore a
`SAT` word is valid, while `UNSAT` does not exclude all possible compilers.

`ready15.py` is a sufficient forced-port/core screen, not an exact readiness
criterion.  In particular it requires literal terminal-envelope
surjectivity, whereas a general exact compiler may host such a target in a
higher derivative row.  Its weighted quotient Hall test can be exact inside
the selected forced core without being exact over all compiler choices.

`rowledger.py` also disables its strongest central-layer assertion with
`assert ... or True`; its printed statistics must not be treated as a
certificate without an independent verifier.

The statements in `GENERAL_CONSTRUCTION.md` that the compiler is both
universal and deterministic/polynomial conflate two different objects: the
restricted one-core/Hall pipeline is deterministic after its carrier is
fixed, while `sandwich2.py` is a restricted CP-SAT search.

## 5. Rechecked positive artifacts

Every word currently stored in Claude's folder for `k=9..13` was replayed
with the repository's independent literal verifier.  The following all
cover every nonzero mask at the claimed optimal length:

* `k09_equi_new.word` (128);
* `k10_flat.word` (254);
* all six stored `k=11` words (465);
* `k12_flat.word` (926);
* `k13_flat.word` (1719).

These positive certificates are genuine even where the generating solver's
negative semantics are incomplete.

## 6. Live-search status at audit time

The latest H100-CPU snapshot had two restarted seeded `k=15` CP-SAT lanes and
one window-LNS lane:

* the seed starts at 47 lower-`q2` and 95 upper missing orbits;
* both restarted CP-SAT lanes replayed the seed exactly in round zero and
  were still solving their first 48-cover constrained round; neither had
  emitted a new candidate;
* window LNS remained at its initial score 142 after 200 iterations;
* the old unseeded `k=13` lane had terminated before the warm-start fix and
  had not been relaunched.

No bound or certificate changed.

## 7. Correct integration path

Use Claude's reduction, not the current overclaimed wrapper:

1. branch on the compact lifetime/gap schedule rather than 6,435 raw bits;
2. reconstruct `alpha,beta` and audit middle/first-shadow injectivity and
   every required shadow exactly;
3. apply proof-safe shadow Benders cuts (or complete selector clauses), not
   capped-cover `UNSAT`;
4. pass every candidate to the exact fixed-carrier Hall/compiler oracle;
5. independently enumerate all contiguous ORs before accepting a word.

This is a materially better search coordinate system, but it is not yet a
`k=15` solution or an all-`k` existence proof.
