# Iterated boundary--core rigidity

## 1. Status

The boundary--core theorem can be iterated, but only across an exact
rank-count equality.  The equality gate is rigid and checkable: the boundary
mass peeled at the current active rank must equal the complete gap to the next
lower record bound.  A positive boundary mass, or even the largest boundary
mass allowed by one of the two estimates, is not enough unless it equals that
gap.

This note gives the exact all-dimensional recursion, its failure budget, and
the complete arithmetic for `1 <= k < 20`.  It produces no contradiction to
`nu(k)=B(k)`.  It does show that a *fully saturated* recursive onion is
arithmetically impossible for every `6 <= k < 20`, so that architecture cannot
be the general construction hidden behind the conjectured formula.

## 2. Rank-count records

For fixed `k`, put

    M_r = C(k,r),
    L_r = sum_(s=1)^(r-1) C(k,s),
    d_r = tau(k,r),
    b_r = M_r+d_r,
    sigma_r = d_r M_r+C(d_r+1,2)-L_r.

Let

    beta_j = max_(1<=s<=j) b_s,       beta_0=0.

Call `r` a **strict record rank** when

    b_r=beta_r>beta_(r-1).

Its record gap and boundary cap are

    g_r = b_r-beta_(r-1),
    H_r = min(g_r,floor(sigma_r/d_r))                 (d_r>0).

Rank one is the terminal base case.  At exact length `b_1=k`, all entries are
the `k` distinct singleton masks.

When several ranks tie for an envelope value, the correct active rank is the
*least* maximizer.  Applying exact rank truncation at that rank gives the
strongest diagonal ceiling.  A later rank in the same tie is not another
onion layer.

## 3. Exact record-onion theorem

**Theorem.**  Suppose a zero-free word `W` covers every mask through rank `j`
and has exact envelope length

    |W|=beta_j.

Let

    r=min{s<=j:b_s=beta_j}.

Then `r` is a strict record rank and

    W = P_r || C_r || Q_r,

where:

1. every entry has rank at most `r`;
2. `P_r,Q_r` consist of distinct rank-`r` entries;
3. every entry of the single contiguous core `C_r` has rank below `r`;
4. `C_r` covers every mask below rank `r`;
5. if `h_r=|P_r|+|Q_r|`, then

       h_r <= H_r <= g_r;

6. the core reaches the next lower envelope exactly if and only if

       h_r=g_r.

In that event

    |C_r|=beta_(r-1),

and the theorem applies again to `C_r` at the least rank attaining
`beta_(r-1)`.

**Proof.**  Since `|W|=b_r` and `W` covers ranks through `r`, exact rank
truncation and boundary--core rigidity apply at rank `r`.  They give items
1--4.

The core covers the whole lower ideal, hence

    |C_r| >= beta_(r-1).

Therefore

    h_r=b_r-|C_r| <= b_r-beta_(r-1)=g_r.

The independent short-band residual estimate from boundary--core rigidity
gives

    d_r h_r <= sigma_r,

which proves `h_r<=H_r`.  Finally,

    |C_r|=b_r-h_r
           =beta_(r-1)+(g_r-h_r),

so equality with the next envelope is equivalent to `h_r=g_r`.  In that
case `C_r` has the exact hypotheses required for the next application.  QED.

## 4. The exact failure budget

The amount by which a peel fails to reach the next equality has a direct
meaning.  Put

    e_r=g_r-h_r.

Then

    |C_r|=beta_(r-1)+e_r.

If `p` is the least rank with `b_p=beta_(r-1)`, rank-excess stability applied
inside `C_r` gives

    #{i in C_r: |A_i|>p} <= e_r.                         (4.1)

This is the strongest unconditional continuation when `e_r>0`.  It does
*not* put those exceptional positions at the boundary and does not turn the
remaining pieces into one contiguous equality word.  Only `e_r=0` permits
the next onion peel.

## 5. Iterated form

Suppose the successive record gaps are saturated at ranks

    r_0>r_1>...>r_t.

Repeated substitution gives the nested form

    P_(r_0)||P_(r_1)||...||P_(r_t)||C
       ||Q_(r_t)||...||Q_(r_1)||Q_(r_0),                 (5.1)

with exactly `g_(r_i)` distinct literal rank-`r_i` entries in the two blocks
of each saturated layer.  If the recursion reaches rank one, the center is
the `k` singleton masks.

Equation (5.1) is a canonical *conditional* normal form.  It is not an
existence theorem: `H_r=g_r` says only that the two numerical bounds do not
forbid saturation.  It does not establish compatible interval witnesses,
pin survival, or upper-rank coverage.

## 6. Exact arithmetic for every `k<20`

In the table, an entry `r:g/H` means that rank `r` is a strict record, its
gap is `g`, and every exact equality word has at most `H` literal rank-`r`
boundary entries.  `!` means `H<g`, so an exact peel to the preceding record
is impossible.  Rank one is the direct singleton base.

| k | B(k) | strict-record ledger `r:g/H` |
|---:|---:|:---|
|1|1|`1:1/1`|
|2|2|`1:2/2`|
|3|4|`1:3/3, 2:1/1`|
|4|7|`1:4/4, 2:3/3`|
|5|12|`1:5/5, 2:6/6, 3:1/1`|
|6|21|`1:6/6, 2:10/10, 3:5/0!`|
|7|37|`1:7/7, 2:15/15, 3:14/8!, 4:1/1`|
|8|72|`1:8/8, 2:21/21, 3:28/21!, 4:15/15`|
|9|128|`1:9/9, 2:28/28, 3:48/40!, 4:43/43`|
|10|254|`1:10/10, 2:36/36, 3:75/66!, 4:90/36!, 5:43/43`|
|11|465|`1:11/11, 2:45/45, 3:110/100!, 4:165/100!, 5:133/133, 6:1/1`|
|12|926|`1:12/12, 2:55/55, 3:154/143!, 4:275/198!, 5:297/0!, 6:133/133`|
|13|1719|`1:13/13, 2:66/66, 3:208/196!, 4:429/339!, 5:572/196!, 6:430/430, 7:1/1`|
|14|3434|`1:14/14, 2:78/78, 3:273/260!, 4:637/533!, 5:1001/533!, 6:1002/1002, 7:429/196!`|
|15|6438|`1:15/15, 2:91/91, 3:350/336!, 4:910/791!, 5:1638/1064!, 6:2002/63!, 7:1431/1431, 8:1/1`|
|16|12873|`1:16/16, 2:105/105, 3:440/425!, 4:1260/1125!, 5:2548/1853!, 6:3640/1125!, 7:3433/3433, 8:1431/1431`|
|17|24313|`1:17/17, 2:120/120, 3:544/528!, 4:1700/1548!, 5:3808/2976!, 6:6188/2976!, 7:7073/7073, 8:4862/3699!, 9:1/1`|
|18|48623|`1:18/18, 2:136/136, 3:663/646!, 4:2244/2074!, 5:5508/4522!, 6:9996/5950!, 7:13260/646!, 8:11935/11935, 9:4863/4863`|
|19|92381|`1:19/19, 2:153/153, 3:798/780!, 4:2907/2718!, 5:7752/6594!, 6:15504/10470!, 7:23256/6594!, 8:25195/25195, 9:16796/7497!, 10:1/1`|

The top-down conditional routes, stopping at the first rank where saturation
is numerically impossible, are

| k | conditional equality route |
|---:|:---|
|1|`1`|
|2|`1` (rank two ties and is skipped)|
|3|`2 -> 1`|
|4|`2 -> 1`|
|5|`3 -> 2 -> 1`|
|6|`3 !`|
|7|`4 -> 3 !`|
|8|`4 -> 3 !`|
|9|`4 -> 3 !` (rank five ties and is skipped)|
|10|`5 -> 4 !`|
|11|`6 -> 5 -> 4 !`|
|12|`6 -> 5 !`|
|13|`7 -> 6 -> 5 !`|
|14|`7 !`|
|15|`8 -> 7 -> 6 !`|
|16|`8 -> 7 -> 6 !`|
|17|`9 -> 8 !`|
|18|`9 -> 8 -> 7 !`|
|19|`10 -> 9 !`|

Thus full saturation down to the singleton base is arithmetically possible
only for `k<=5` in this range.  It is impossible for every `6<=k<20`.

## 7. Sharp finite consequences

For `k=11`, the deepest possible saturated branch is exact:

* `h_6=1` gives a 464-position rank-five equality core;
* `h_5=133` gives a 331-position rank-four equality core;
* within that core `h_4<=100<165`, so the next exact peel is impossible;
* the remaining rank-at-most-three core has length at least `331-100=231`
  and covers every mask through rank three.

Hence this branch has the rigorously nested form

    P_6 || P_5 || P_4 || C_(<=3) || Q_4 || Q_5 || Q_6,

with total layer masses `1,133,at most 100`.  Since `h_6=1`, one of `P_6,Q_6`
is empty.  No assertion is made about the split of the other layers between
the two sides.

Other notable blockers are:

* `k=12`: if the 133 rank-six positions are fully peeled, the exact
  rank-five core has `h_5=0`; it cannot descend to rank four.
* `k=14`: already the outer layer has `h_7<=196<429`; no exact rank-six
  equality core can arise by boundary peeling.
* `k=16`: saturation can pass ranks eight and seven, but rank six has
  `h_6<=1125<3640`.
* `k=18`: saturation can pass ranks nine and eight, but rank seven has
  `h_7<=646<13260`.

There is no numerical contradiction: taking less boundary mass, including
zero, is always compatible with these necessary inequalities.

## 8. Construction verdict

The known exact words reinforce that last point.  Their diagonal rank
profiles are

    k=8:   1^25 2^47,
    k=9:   1^9  2^36 3^83,
    k=10:  1^16 2^90 3^144 4^4,
    k=12:  1^20 2^137 3^262 4^507.

Each has zero literal mass at its active record rank.  Thus known optimal
constructions live in the non-saturated branch rather than exhibiting a
recursive boundary onion.

The theorem is consequently most useful as a lossless case split and search
cut:

* saturated boundary mass gives a smaller exact equality instance and a
  rigorously nested normal form;
* any smaller mass comes with the exact excess budget (4.1), but no further
  boundary localization;
* a general construction still has to solve ordered interval geometry, pin
  survival, and upper-shadow coverage inside the low-rank core.

All arithmetic and the four displayed certificate profiles are independently
recomputed by `scratch/check_iterated_boundary_core_rigidity.py`.
