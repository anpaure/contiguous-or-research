# Exact fixed-prefix `k=14`, 241-entry append encoding

## 1. Decision problem and result of this implementation pass

Let `P` be the certified 3,434-entry word
`k14_pinnable_factor_missing260.txt`.  It misses exactly the 260 masks in
`k14_missing_260.txt`: 238 of rank nine and 22 of rank ten.

The source

```text
scratch/k14_append241_exact.cpp
```

is an exact SAT encoding of the following question:

> Is there a word `W` of 241 arbitrary nonzero 14-bit masks such that
> `P || W` covers every nonzero 14-bit mask by contiguous interval OR?

It retains every append-only interval and every interval crossing the old/new
seam.  It makes no literal-mask, fixed-forest, fixed-order, or bounded
rank-ten-window assumption.

The encoding is split into 52 formulas.  Their disjunction is equivalent to
the decision problem.  This is a reduction, not a SAT or UNSAT result.  A SAT
branch would produce a 241-entry suffix and improve the full nonzero upper
bound to 3,675.  A rigorous nonexistence result requires checked refutations
of all 52 formulas.

The independent audit is
`K14_APPEND241_ENCODING_INDEPENDENT_AUDIT.md`; its verdict is **PASS**.

## 2. Why only 52 branches are needed

Choose one witness for every missing rank-nine mask.  All 238 right endpoints
are distinct and lie among the 241 new positions.  Let `x` be the number of
chosen witnesses beginning in the old prefix.  The certified seam theorem
gives

```text
1 <= x <= 3.
```

The four usable old suffixes, in increasing old-start order, are

```text
12411, 12409, 12393, 12329.
```

For a candidate sequence `(C_i,S_i)`, where `C_i` is an old suffix and `S_i`
is its assigned rank-nine target, define

```text
P_0 = 0,
P_i = P_(i-1) OR (S_i without C_i).
```

Increasing appended-prefix ORs realizing all seam events exist exactly when
`P_i` is a subset of `S_i` at every step.  Exhaustive application of this
finite criterion gives

```text
x=1: 27 raw crossing patterns,
x=2: 27 raw crossing patterns,
x=3:  6 raw crossing patterns.
```

Let `h=2` when old position 3434 is not consumed by a selected rank-nine
witness and `h=1` when it is.  Let `f` count the seven unique-base hard
rank-ten witnesses whose selected new right endpoint is not a selected
rank-nine right endpoint.  The eighth hard target, 15346, always consumes one
of the three lower-free right endpoints.  Endpoint capacity leaves precisely

| `x` | allowed `(f,h)` |
|---:|---|
| 1 | `(2,2)` |
| 2 | `(2,1)`, `(2,2)`, `(1,2)` |
| 3 | `(1,1)`, `(2,1)` |

Combining patterns and profiles gives

```text
x=1:  9 branches,
x=2: 31 branches,
x=3: 12 branches,
total: 52 branches.
```

`--list` prints the complete deterministic branch manifest, including each
old start, fixed suffix, assigned target, and cumulative minimum prefix OR.

## 3. Exact interval representation

For each missing target `S` and each appended position `p`, the formula has
five unary endpoint variables:

```text
left[p]       p is at or after the appended left endpoint,
right[p]      p is at or before the right endpoint,
inside[p]     left[p] AND right[p],
new_start[p]  the append-only interval starts at p,
end[p]        the interval ends at p.
```

`left` has shape `0...01...1`, while `right` has shape `1...10...0`.
For a crossing interval, an old-start selector forces all `left[p]` true, so
the appended part is exactly `[0,end]`.  Otherwise the unique transition of
`left` selects an appended-only interval `[start,end]`.

For every target, the source enumerates every actual old position whose fixed
suffix OR is a subset of that target.  Earlier suffixes are discarded only
when their bits make an exact target OR impossible.  Thus the two represented
interval forms are exactly all possible new witnesses:

```text
append-only: [new start, new end],
cross-seam:  [old start, end of old prefix] || [0, new end].
```

Same-rank selected left endpoints and, independently, same-rank selected
right endpoints are constrained to be distinct.  This is valid because two
different equal-rank target intervals sharing either endpoint would be nested,
forcing comparable equal-size OR masks.

## 4. Exact OR clauses

For every target bit absent from `S`, every selected appended entry is forced
to omit that bit.  Compatible old suffixes were already filtered to be
subsets of `S`.

For every bit present in `S`, a support disjunction requires either:

* a selected old suffix already containing the bit; or
* a `hit` variable implying both `inside[p]` and the corresponding entry bit.

Therefore each selected physical interval has OR exactly `S`.  Conversely,
any exact physical witness assigns the threshold and hit variables
consistently.  The 241 appended entries themselves have only the nonzero
constraint and are otherwise arbitrary 14-bit masks.

## 5. Safe rank-nine reductions

Let selected rank-nine right endpoints be `r_0<...<r_237` in zero-based new
positions `0,...,240`.  Then

```text
r_i <= i+3.
```

The `x` old-start witnesses are the first `x` intervals in left-endpoint
order.  The `i`-th such branch witness is therefore restricted to endpoint at
most `i+3`, and the branch witnesses' right endpoints are forced into their
nonnesting order.

For a new-start witness whose start is the `s`-th selected new start, its
start position is at least `s`, while its overall interval index is `x+s`.
Its appended length is therefore at most `x+4`.  The encoding imposes exactly
this safe bound.  No rank-ten length restriction is imposed.

The `f` profile is encoded rather than assumed: `used9[p]` is equivalent to a
rank-nine witness ending at `p`; each hard target's `free` flag is equivalent
to ending at an unused rank-nine endpoint; and a direct seven-variable
cardinality encoding requires exactly the branch's `f` value.  Target 15346
is separately forced to end free.

## 6. Soundness and completeness

### Soundness

A model yields 241 nonzero masks.  Each old omission has a genuine selected
append-only or crossing interval whose OR is exactly that target.  Every other
mask retains its old witness in `P`.  The source independently recomputes all
subarray ORs before writing a SAT output.

### Completeness

Take any completing 241-entry suffix and select one witness for each old
omission.  Equal-rank nonnesting supplies distinct ordered endpoints.  The
fixed-prefix endpoint theorem places its rank-nine witnesses in one of the
`x=1,2,3` crossing patterns and one of the allowed `(f,h)` profiles.  The
right-endpoint and length inequalities above hold.  Entry bits, unary
thresholds, old selectors, endpoint flags, and one actual occurrence for each
required bit then satisfy that branch.

Hence

```text
some one of the 52 formulas is SAT
    iff
the designated prefix has a 241-entry completing suffix.
```

## 7. Build inventory

All 52 formulas were constructed remotely with the production CaDiCaL
library and GCC `-O3`.  Source-level clause counters are:

| branch family | formulas | variables | minimum clauses | maximum clauses |
|---|---:|---:|---:|---:|
| `x=1,f=2` | 9 | 1,012,539 | 2,632,175 | 2,632,175 |
| `x=2,f=1` | 4 | 1,012,539 | 2,632,394 | 2,632,394 |
| `x=2,f=2` | 27 | 1,012,539 | 2,632,414 | 2,632,414 |
| `x=3,f=1` | 6 | 1,012,539 | 2,632,632 | 2,632,632 |
| `x=3,f=2` | 6 | 1,012,539 | 2,632,652 | 2,632,652 |

The known 242-entry suffix, truncated only for phase selection, gives exact
phase witnesses for 259 of the 260 targets.  Phases do not add clauses or
restrict the solution set.

For the representative branch `x=1, pattern=0, f=2`, CaDiCaL's DIMACS writer
emits the already unit-simplified header

```text
p cnf 1012539 2617305
```

and a 47 MB formula.  The difference from the source clause counter consists
of clauses simplified by CaDiCaL while ingesting branch units.

The full construction log is `k14_append241_build_inventory.log`; the exact
ordered branch list is `k14_append241_branch_manifest.txt`.

## 8. Reproduction

On a machine with a built CaDiCaL tree at `/root/cadical`:

```bash
g++ -O3 -std=c++2a -I/root/cadical/src \
  scratch/k14_append241_exact.cpp /root/cadical/build/libcadical.a \
  -lpthread -o k14_append241_exact

./k14_append241_exact --list \
  k14_pinnable_factor_missing260.txt k14_missing_260.txt

K14_APPEND241_BUILD_ONLY=1 \
K14_APPEND241_DIMACS=k14_append241_x1p0f2.cnf \
./k14_append241_exact \
  k14_pinnable_factor_missing260.txt k14_missing_260.txt \
  k14_append_242.txt candidate.txt 1 1 0 2
```

The final four numerical arguments are `sat_seed x pattern_index f`.
`K14_APPEND241_PROOF=path` enables CaDiCaL proof tracing during a solve.

`launch_k14_append241_exact.sh` schedules all 52 branches in deterministic
manifest order, one sequential worker per supplied CPU core.  For example:

```bash
./launch_k14_append241_exact.sh \
  ./k14_append241_exact \
  k14_pinnable_factor_missing260.txt k14_missing_260.txt \
  k14_append_242.txt run_append241 3600 5,26,35,39
```

It records `SAT`, `TIMEOUT`, or `UNSAT_UNCHECKED` per branch and deliberately
does not promote a solver exit code to a mathematical UNSAT claim.  Setting
`K14_APPEND241_PROOF_DIR` enables one proof file per branch for a subsequent
independent proof-checking pass.

## 9. Provenance

| artifact | SHA-256 |
|---|---|
| designated prefix | `4c71a5e59985ff8d78a4ae80845defd21cebfe240c16ad4604b57e9b9cb999ad` |
| exact missing family | `152e7e9d951e96c0600875d674f78333b634622e4c34262f44de51053fbd64ab` |
| phase seed `k14_append_242.txt` | `41d7028668cde93d6f9347ae881b352dfbc3de446845324a185b21414099d8a8` |
| exact source | `b4b7b586766906bf0727adeb587cccb98cb57b9783e9e3059498bce292fab964` |
| 52-formula build log | `3b4b636628eafbce3bc1634e71775ac80c18ab6c11639ad35e5cac7fdda02498` |
| branch manifest | `5f5881811446be60dd83e51da8adfe7577e6331b7277219161800eb95280602e` |
| independent audit | `1cba6d5371d9bb02d970944ea1e8fe77dd460283074f73ea242a70e25e3704d1` |
| 52-branch launcher | `fd5d9fedb6d7afb152182d5aff71f480d76c782fecd36341355fa806437846fa` |
| representative DIMACS | `00ef7647b726ebbed8144fc1c0705a041b552a2684e3bd02ac91379822566f58` |
| remote binary | `236f3e1597aa9d7590e974915b2cecb73749eded640cae9529d82a173b585231` |

The hard-target identities and `h` interpretation are certified for this
designated prefix.  They are deliberately not claimed as a generic interface
for an arbitrary substitute prefix.

## 10. Initial exact searches

Two one-hour representative searches were launched on remote host
`213.173.111.107:48809`; neither had returned SAT or UNSAT at the time of this
record.

| PID | core | output/log stem | complete descriptor |
|---:|---:|---|---|
| 169302 | 26 | `/root/k14_append241_x2p23f2` | `x=2, pattern=23, f=2, h=1; 3433:12393 -> 13423 (prefix 1030); 3434:12329 -> 15407 (prefix 3078)` |
| 170134 | 5 | `/root/k14_append241_x1p5f2` | `x=1, pattern=5, f=2, h=2; 3433:12393 -> 13423 (prefix 1030)` |

The first is branch 36 and the second branch 5 in the manifest.  They were
chosen because target 13423 is the seam target used by the certified
242-entry suffix.  A timeout is only an incomplete search, never an UNSAT
result.
