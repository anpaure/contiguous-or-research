# K16 five-phase complete arbitrary-two-edit provider-pair normal form

Date: 2026-07-30  
Lane: R  
Status: exact structural reduction and preflight counts; no broad SAT solve
was launched.

## 0. Result

Fix the canonical blocker word

```text
U = scratch/r_k16_fivephase_blocker_a879_state_independent_20260730.word
SHA256 aee4b0d00670e887e75d642ba186f0c04e8f279b82253c34d8541ae26dd0af70
```

of length `n=12874`, whose sole missing target is

```text
A = 0xa879 = 43129.
```

The obvious necessary filter—an `A` witness interval may contain at most two
current cells having a bit outside `A`—does **not** prune the unordered support
pairs.  Every coordinate can be changed to the literal singleton `A`, so all

```text
C(12874,2) = 82,863,501
```

unordered pairs are `A`-provider pairs.  Even retaining both sharp portal
coordinates leaves 82,837,756 pairs; fixing the two portals and the terminal
seam leaves 82,824,885 pairs.

Nevertheless, the complete problem has an exact two-class overlapping cover:

1. **One-site `A` witnesses.**  One edit alone already creates `A`; the other
   edit is a collateral-return action.  The existing one-cell census reports
   27,926 possible first `A`-service actions, each to be followed by one exact
   off-service-site hole-state return census.
2. **Joint-witness class.**  Both edited sites lie in one `A`
   witness interval.  Only 13,223 unordered pairs can do this, represented by
   13,953 interval/pair patterns.  Each is an exact fixed-pair, 32-bit CNF.

The union of these two classes is complete but may overlap.  The proposed
schedule has 41,149 top-level job instances (`27,926+13,223`), not 41,149
disjoint logical cases or distinct candidates.  This is a tractable
structural formulation, but its aggregate running time is not yet certified;
none of these new subproblems was solved in this turn.

## 1. Exact interval criterion

Let the two final changed positions be `p<r`, with new nonzero masks `x,y`.
For an interval `I`, define

```text
B(I) = { i in I : U_i has a bit outside A }.
```

### Theorem 1.1 (two-edit `A` witness criterion)

An interval `I` is an `A` occurrence after the two edits if and only if:

1. `B(I) subseteq {p,r}`, hence `|B(I)|<=2`;
2. at least one of `p,r` lies in `I`;
3. every new value whose site lies in `I` is a nonzero submask of `A`; and
4.

   ```text
   OR(U_i : i in I\{p,r})
     | (x if p in I)
     | (y if r in I)
     = A.
   ```

#### Proof

If the final interval OR is `A`, every cell in it is a submask of `A`.
Every unedited current cell carrying an outside bit is therefore impossible,
which proves condition 1; conditions 3 and 4 are immediate.  If neither edit
lies in `I`, then `I` was already an `A` occurrence in `U`, contrary to the
authenticated sole-hole replay.  Conversely, conditions 1–4 say exactly that
all final cells in `I` are submasks of `A` and their union is `A`.  QED.

This includes all three requested cases:

* `|B(I)|=2`: both bad sites are forced to be the two edited sites;
* `|B(I)|=1`: its bad site is edited, while the second site may lie in `I` or
  outside it solely to repair collateral;
* `|B(I)|=0`: at least one edited site still lies in `I`, because `U` itself
  has no `A` occurrence.

## 2. Exact preflight counts

The complete interval scan stops each left endpoint immediately after its
third bad cell.  It finds 26,776 eligible intervals:

| bad cells | intervals |
|---:|---:|
| 0 | 350 |
| 1 | 13,218 |
| 2 | 13,208 |

Their full length distribution is

```text
bad0: len1 331, len2 19;
bad1: len1 12543, len2 624, len3 51;
bad2: len2 12230, len3 890, len4 88.
```

Thus the maximum eligible interval length is four.

For each interval, enumerate the nonempty set `S={p,r} intersect I` subject
to `B(I) subseteq S`.  There are

```text
13,587 one-site-inside local patterns,
13,953 two-sites-inside local patterns,
27,540 local patterns total.
```

The 13,953 joint patterns collapse to 13,223 unordered pairs, with interval
multiplicity histogram

```text
1^12542, 2^638, 3^37, 4^6.
```

Expanding every one-site-inside pattern by every possible outside repair site
would create 174,904,687 rows; including the joint terms gives 174,918,640.
This is why the one-site class must be represented as service action followed
by return, not as a flat pair-term master.

The fail-closed preflight is

```text
scratch/k16_fivephase_complete_twoedit_pair_preflight_20260730.audit.json
SHA256 64cf4b34e4adf4740d9da9384012ab5bc729e0d1625336c324c0a2c25d97d847

scratch/audit_r_k16_fivephase_complete_twoedit_pair_normal_form_20260730.py
SHA256 a62b371ad2c750326aa4d49a99a417bd34449d18760a8a50e47d39e812371874
```

It is a count/replay audit only; it contains no SAT claim.

## 3. Complete-cover theorem

### Theorem 3.1 (sequential-or-joint dichotomy)

Every universal word at Hamming distance exactly two from `U` belongs to at
least one of the following classes.

#### Class S: sequential service and return

Some final `A` witness interval contains exactly one edited site.  Applying
that site's final value to `U` already creates the same `A` interval, because
the other edit lies outside it.  Hence the first action is one of the exact
27,926 one-cell `A`-service rows reported by

```text
scratch/k16_fivephase_to43129_onecell.audit.json
SHA256 7e6feaad4a5d3456829a28d034181ace6abdf7126998d51851846c541c623643
```

That audit's histogram sums to 27,926 and has maximum debt 19, but its schema
does not bind the blocker-word and driver hashes.  Those two numbers are
internally checked evidence, not yet a fail-closed authenticated certificate.
The lost-target set is the exact hole set of the intermediate word, and the
other edit must be a debt-free one-cell return at a *different* coordinate;
re-editing the service coordinate would not have Hamming distance exactly two.

#### Class J: joint witness

Some final `A` witness interval contains both edited sites.  By Theorem 1.1,
their unordered pair is one of the 13,223 joint pairs in the preflight.  The
final word is represented by the exact fixed-pair CNF for that pair.

#### Proof

Choose any final `A` witness.  It contains one or two edited positions by
Theorem 1.1.  In the first case the final value at its unique edited site
creates `A` before the other edit, giving Class S.  In the second case its
pair occurs in the joint catalogue, giving Class J.  These cases exhaust the
possibilities.  QED.

The classes may overlap; disjointness is neither claimed nor needed.

## 4. Exact fixed-pair evaluator

Fix `p<r`.  Let

```text
F(p,r) = { target != A : every occurrence of target in U meets {p,r} }.
```

These and `A` are exactly the targets which must be supplied by a new interval
meeting at least one edited site.  All other targets retain an old occurrence
wholly in one of the three fixed runs.

Let the following slices exclude the edited cells:

* `L_p` be the suffix-OR set of the half-open run `U[0:p]`, including zero;
* `P_M` and `S_M` be the prefix- and suffix-OR sets of `U[p+1:r]`, including
  zero;
* `M=OR(U[p+1:r])`;
* `R_r` be the prefix-OR set of the half-open run `U[r+1:n]`, including zero.

The OR of an empty run is zero.  Targets range over the nonempty masks
`1,...,65535`.

For replacement masks `x,y`, every affected *interval type* belongs to
exactly one of the following three classes, and hence every affected label
lies in their union:

```text
N_p(x)   = { l|x|m : l in L_p, m in P_M },
N_r(y)   = { m|y|s : m in S_M, s in R_r },
N_pr(x,y)= { l|x|M|y|s : l in L_p, s in R_r }.
```

Therefore the fixed pair produces a universal word if and only if

```text
x,y are nonzero,
x != U_p, y != U_r,
{A} union F(p,r) subseteq N_p(x) union N_r(y) union N_pr(x,y).
```

This is an exact 32-value-bit CNF with ordinary reified witness terms.  It is
also exactly the support-two specialization of the already audited dynamic
fixed-substitution encoder.  No independent rankwise ownership or abstract
coverage surrogate enters.

## 5. Exact implementation schedule

The complete future computation is:

1. Re-emit all 27,926 blocker `A`-service rows in a fail-closed artifact which
   binds the blocker and driver hashes, including their exact debt sets.
2. For each intermediate state, run the exact one-cell return census.  The
   current generic guard must be extended from at most 16 holes to the
   internally reported maximum of 19; it must forbid the service coordinate
   and retain full literal replay.
3. Emit and solve one fixed-pair CNF for each of the 13,223 joint pairs.
4. Independently replay any SAT word against all 65,535 nonempty masks.

This schedule is complete by Theorem 3.1.  It is dramatically smaller than
the flat pair catalogue, but no wall-time or aggregate-memory theorem is
claimed.  The support-40 DRAT-certified UNSAT result is merely one small
subfamily of this complete model.

## 6. Boundary

Proved:

* the bad-cell interval criterion, including all 0/1/2-bad cases;
* the exact interval and joint-pair counts;
* the fact that provider-position filtering alone leaves all 82,863,501
  unordered pairs;
* the complete sequential-or-joint-witness cover;
* the exact fixed-pair universality criterion.

Not proved or run:

* any SAT/UNSAT result for the complete two-edit class;
* a fail-closed certificate for the 27,926/max-19 one-cell census;
* that all 41,149 scheduled job instances fit a particular time budget;
* a global radius-four no-go or a length-12873 construction.

After this reduction was completed, the literal word
`answers/k16_upper12874.word`, SHA256
`631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e`,
was independently verified universal.  It is not in the frozen two-edit
class above.  Thus this report remains a local normal form, while the global
problem has moved to the one-cell compression question
`12873 <= nu(16) <= 12874`.
