# Exact q369 short-band saturation cut

## Status

This note proves and records the optional exact cut enabled by

```text
K11_FOREST_Q369_TOP_LAYER_CUT=1
```

in `k11_forest_sat.cpp`.  The flag is accepted only together with

```text
K11_FOREST_PORTAL_BRANCH=q369_schedule
```

It introduces no variables.  With containment caps enabled it changes the
formula from 2,882,282 variables / 14,459,954 clauses to 2,882,282 variables /
14,919,116 clauses.  The 459,162 added clauses comprise 462 rank-five schedule
clauses and 458,700 exact rank-four next-layer clauses.

This is a satisfiability-preserving theorem cut for the q369 branch, not a
heuristic restriction.

## 1. Saturation of all short physical intervals

Use zero-based physical positions.  In `q369_schedule`, the first 369 selected
rank-six witnesses are fixed to

\[
  [i,i+2],\qquad 0\le i\le 368.
\]

There are 1023 nonempty masks of ranks 1 through 5.  The unrestricted
rank-count theorem says every one has a witness of length at most three in any
465-entry solution.  The branch therefore places

\[
  1023+369=1392
\]

different target values into short physical intervals.  But the number of
physical intervals of lengths one, two, and three is exactly

\[
  465+464+463=1392.
\]

One physical interval has only one OR value.  Hence the 1392 witnesses are
pairwise different and exhaust every short physical interval.  In particular:

* the 369 fixed triples contain the selected rank-six values;
* every other short cell contains exactly one mask of rank at most five;
* no two short cells have the same OR.

## 2. The forced rank-five pool

Delete the 369 fixed rank-six triples from the containment poset of short
physical intervals.  Its maximal remaining cells are exactly

\[
  P_s=[s,s+1]\quad(0\le s\le368)
\]

and

\[
  T_s=[s,s+2]\quad(369\le s\le462).
\]

There are 369+94=463 such cells, in the displayed endpoint order.

Every selected rank-five witness must occupy one of them.  Otherwise it has a
strict residual supercell whose distinct OR has rank at most five and properly
contains a rank-five set, which is impossible.  The 462 rank-five masks occupy
462 different maximal cells, so exactly one cell of this ordered list is
omitted.

Let row `i` be the `i`-th selected rank-five interval in monotone endpoint
order.  It can only select pool cell `i` or pool cell `i+1`.  In the solver's
`(alpha,beta)` state convention this is

```text
rows   0..367 : 01 or 12
row       368 : 01 or 13
rows 369..461 : 02 or 13
```

The existing exact-one and endpoint-monotonicity clauses make the second
choice a monotone Boolean threshold.  It is false before the omitted pool cell
and true from that omission onward.  Consequently the 462 binary positive
clauses added by the implementation encode every possible single omission and
nothing else.

## 3. Exact next-layer rank-four cut

After deleting the selected rank-five cells, 561 cells remain, in bijection
with the masks of ranks 1 through 4.  Hence every rank-four cell is maximal in
this residual poset.

If pool cell `e` is omitted, the residual maximal cells are precisely:

* `e` itself;
* early singleton cells `[p,p]`, `0<=p<=368`, not contained in `e`;
* late pair cells `[p,p+1]`, `369<=p<=463`, not contained in `e`.

A crossed rank-four witness in the adjacent-shadow encoding has length one or
two and must have proper selected rank-five extensions at both endpoints.  The
omitted early pair, if it has rank four, has no same-left rank-five extension;
an omitted late triple is not a crossed candidate.  Thus every crossed
rank-four witness is an early singleton or late pair.

The implementation first disables every other crossed `q` flag.  It then uses
the rank-five threshold state to forbid the exact omissions that would contain
an otherwise eligible candidate:

* early singleton `[p,p]`: omissions `P_p` and, when present, `P_(p-1)`;
* late pair `[p,p+1]`: omissions `T_p` and, when present, `T_(p-1)`.

Write `skip(i)` for the second allowed rank-five state in row `i`.  The omitted
pool index is encoded by

```text
j = 0   :  skip(0)
0<j<462 : !skip(j-1) & skip(j)
j = 462 : !skip(461)
```

so every candidate/omission exclusion is a binary or ternary clause.  There
are exactly 153,450 unconditional negative units and 305,250 guarded
omission clauses, totaling 458,700.

Exception slots remain unrestricted.  This is necessary: the single omitted
early pair or late triple may itself be a rank-four cell and then cannot be a
crossed candidate.

## 4. Mechanical checks

An exhaustive 463-omission poset script checked:

```text
PASS omissions=463 short_cells=1392 maximal_rank5_pool=463
residual_cells=561 residual_maxima_sizes=[463,464]
```

A separate state-machine enumeration checked that the binary row clauses plus
the pre-existing monotonicity constraints have exactly 463 schedules, in
bijection with omitted pool indices 0 through 462.

The source passes a C++20 syntax build.  A real remote CaDiCaL build gives the
counts above.  With the flag absent, all previously audited portal branch
counts are unchanged:

```text
q19_factor_prefix  2,882,282 / 14,460,196
q19_fixed_row      2,882,282 / 14,459,977
q19_abstract       2,882,282 / 14,460,414
q369_schedule      2,882,282 / 14,459,954
```

The flag-without-q369 validation exits with status 2.

## 5. Frozen build and remote commands

Frozen source SHA-256:

```text
4e63cce6d95099cb0571aa5aa50b405b1d63b05bb18742e5262c484ac6325c07
```

Copy, build, and check on the remote machine:

```bash
mkdir -p /root/q369_top_layer_4e63cce6d950
g++ -O3 -std=c++2a -I/root/cadical/src \
  k11_forest_sat_4e63cce6d950.cpp \
  /root/cadical/build/libcadical.a -lpthread \
  -o k11_forest_sat_q369_top

env K11_FOREST_BUILD_ONLY=1 \
    K11_FOREST_ADJACENT_SHADOWS=1 \
    K11_FOREST_RANK3_SHADOWS=1 \
    K11_FOREST_CONTAINMENT_CAPS=1 \
    K11_FOREST_PORTAL_BRANCH=q369_schedule \
    K11_FOREST_Q369_TOP_LAYER_CUT=1 \
    ./k11_forest_sat_q369_top \
      /root/k11_upper549_natural_array.txt /tmp/no-output.txt 1931
```

A bounded search differs only by deleting `K11_FOREST_BUILD_ONLY` and wrapping
the executable in the desired `timeout`, `taskset`, and `nice` command.

## 6. Live remote seeds

Four one-hour cut-enabled runs were started from the same frozen binary and
seed array:

```text
SAT seed 1931 : core 12
SAT seed 1932 : core 21
SAT seed 1933 : core 25
SAT seed 1934 : core 28
```

Their files are `q369_top_<seed>.log`, `.stdout`, and (on SAT)
`candidate_q369_top_<seed>.txt` in the frozen remote directory.  These are
searches only: timeout or solver silence is not an UNSAT certificate.
