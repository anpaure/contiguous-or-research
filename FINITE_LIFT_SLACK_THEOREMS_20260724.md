# Finite lift slack: exact endpoint lifts and a many-seam barrier

## 1. Setup

A word `A=(a_1,...,a_n)` on `[k]` is **universal** if every nonempty
`S subseteq [k]` is the union of a nonempty contiguous interval of `A`.
All entries of `A` are nonempty.  Write `x` for one new coordinate.

The ordinary trimmed lift is

```text
A, x, x|a_1, ..., x|a_(n-1),
```

and has length `2n`.  An old target is witnessed in the first copy.  If
`[i,j]` witnesses `S`, then `x|S` is witnessed in the transformed copy when
`j<n`, and by

```text
a_i, ..., a_n, x
```

when `j=n`.  The singleton `x` gives the empty old projection.  This is the
only fact about the stored construction used below.

## 2. Endpoint-compressed lifts

### Theorem 2.1 (one-ended compression)

Suppose the last `t` entries of `A` form a weakly descending inclusion chain:

```text
a_p superseteq a_(p+1) superseteq ... superseteq a_n,
p=n-t+1.
```

Then there is a universal word on `[k] union {x}` of length

```text
2n-t+1,
```

namely

```text
a_1,...,a_n, x, x|a_1,...,x|a_(p-1).                 (2.1)
```

#### Proof and seam audit

Targets not containing `x` use their old witnesses wholly inside the first
copy.  The target `{x}` uses the displayed singleton.

Let `[i,j]` be any old witness for a nonempty `S`.  If `j<p`, its transformed
copy is present in (2.1).  If `j>=p`, descending inclusion gives

```text
a_(j+1) | ... | a_n subseteq a_j,
```

and hence

```text
a_i | ... | a_n = a_i | ... | a_j = S.
```

Thus the single contiguous interval `a_i,...,a_n,x` has union `S union {x}`.
No interval that jumps over an omitted transformed entry is used.  These
cases cover every target.  The length is `n+1+(p-1)=2n-t+1`.  QED.

The reversed statement is equally useful.  If

```text
a_1 subseteq ... subseteq a_t,
```

then

```text
x|a_(t+1),...,x|a_n, x, a_1,...,a_n
```

has length `2n-t+1`.  A witness starting after `t` is copied; a witness
`[i,j]` with `i<=t` is replaced by `x,a_1,...,a_j`, since the added prefix is
contained in `a_i`.

### Theorem 2.2 (two-ended compression)

Suppose

```text
a_1 subseteq ... subseteq a_s
```

and

```text
a_p superseteq ... superseteq a_n,  p=n-t+1.
```

Then the following word is universal:

```text
x|a_(s+1),...,x|a_(p-1), x, a_1,...,a_n, x,          (2.2)
```

where the transformed block is empty when `s+1>p-1`.  Its length is

```text
n+2+max(0,n-s-t).
```

In the usual disjoint case `s+t<=n`, this is

```text
2n-s-t+2.                                             (2.3)
```

#### Proof and complete case split

Again the middle copy handles targets without `x`, and either singleton
handles `{x}`.  Choose an old witness `[i,j]` for `S`.

* If `i<=s`, then `x,a_1,...,a_j` is contiguous in (2.2), and its old
  projection is unchanged because `a_1|...|a_(i-1) subseteq a_i`.
* If `i>s` and `j>=p`, then `a_i,...,a_n,x` is contiguous, and its old
  projection is unchanged because `a_(j+1)|...|a_n subseteq a_j`.
* If `i>s` and `j<p`, the whole transformed interval
  `x|a_i,...,x|a_j` occurs in the first block.

The cases are exhaustive.  In particular, no claim is made about an
interval crossing from the transformed block through the first singleton
and into the old copy.  QED.

### Reduced endpoint chains

Adjacent equal entries can be coalesced without losing any interval union.
Consequently a shortest word may be assumed to have no adjacent equal
entries.  In such a word every weak endpoint inclusion chain is strict, so
each of `s,t` is at most `k` (entries are nonempty subsets of `[k]`).  Thus
one-ended compression saves at most `k-1` positions, and two-ended
compression saves at most `2k-2`.  This already shows that endpoint nesting
cannot supply a Catalan-sized saving.

## 3. A chain-product lemma for seam targets

Let two set-valued chains be

```text
P_1 subseteq ... subseteq P_a,
Q_1 subseteq ... subseteq Q_b.
```

Fix a set `C`.  Among the unions

```text
P_u union C union Q_v,
```

at most `min(a,b)` distinct sets of one fixed cardinality can occur.

Indeed, choose one pair `(u,v)` for each distinct output of that cardinality.
Pairs belonging to distinct outputs form an antichain in the product of the
two chains: comparable pairs give comparable output sets, and two distinct
sets of the same cardinality cannot be properly comparable.  An antichain in
an `a` by `b` product of chains has size at most `min(a,b)` (sort by the first
coordinate; the second must then strictly decrease).

For chains of subsets of `[k]`, duplicates may first be collapsed and each
chain then has at most `k+1` states.  Therefore one fixed two-sided seam can
produce at most `k+1` distinct targets in a fixed old rank.

There is a useful one-unit sharpening.  If either chain contains only
nonempty states, it has at most `k` states.  The same conclusion holds if
the fixed core `C` is nonempty: after unioning every state with `C`, a strict
chain can add only coordinates outside `C` and has at most
`k-|C|+1<=k` states.  In either situation the seam bound is `k`.

## 4. The exact one-transition ceiling

### Theorem 4.1

Let `W` be a word on `[k] union {x}`.  Suppose its high-bit indicator has
exactly one transition, so `W` consists of one block `Z` of entries avoiding
`x` and one block `H` of entries containing `x`, in either order.  Put

```text
z=|Z|, h=|H|, M=C(k,r),  1<=r<=k.
```

If `W` covers all masks, then

```text
z >= M,
h >= M-k,
|W| >= 2M-k.                                          (4.1)
```

If, more specifically, `Z` is an intact universal base word of length `n`,
then

```text
|W| >= n+M-k.                                         (4.2)
```

#### Proof

For every old rank-`r` target choose a witness not containing `x`.  All such
witnesses lie in `Z`.  Intervals for distinct equal-rank targets are
nonnested: containment of intervals implies containment of their unions.
An antichain of intervals in a block of length `z` has size at most `z`, so
`z>=M`.

Now choose witnesses for the `M` targets `{x} union R`, `|R|=r`.  Those lying
wholly in `H` form an interval antichain and number at most `h`.  Every other
chosen witness crosses the unique seam.  Its old projection is the union of
a suffix-OR state on one side and a prefix-OR state on the other.  The
zero-block side consists of nonempty projected suffixes or prefixes, so it
has at most `k` states.  Section 3 therefore bounds the number of distinct
rank-`r` projections across the seam by `k`.  Hence `M<=h+k`, proving (4.1);
(4.2) substitutes `z=n`.  QED.

If the intact base has exact length `n=M+d`, then a one-transition lift can
save at most

```text
2n-[n+M-k] = d+k                                      (4.3)
```

against the black-box `2n` lift.  This is an `O(k)` ceiling with an exact
constant.

## 5. The many-run theorem

The one-transition result extends to an exact quantitative obstruction for
any number of high-bit runs.

### Theorem 5.1

Let `W` be universal on `[k] union {x}`.  Let

* `q` be the number of maximal runs of entries containing `x`;
* `h` be their total length;
* `z=|W|-h` be the total length of all zero-high-bit runs;
* `M=C(k,r)`, where `1<=r<=k`.

Then

```text
z >= M,                                                (5.1)
M <= h+k(C(q,2)+3q),                                  (5.2)
|W| >= 2M-k(C(q,2)+3q).                               (5.3)
```

#### Proof of (5.1)

Every witness for an old rank-`r` target is wholly inside one zero run.
Within a zero run of length `ell`, chosen intervals for distinct rank-`r`
targets form an interval antichain and number at most `ell`.  Summing over
the zero runs gives (5.1).

#### Proof of (5.2), including every seam type

Number the high runs `H_1,...,H_q`.  Choose one witness for every
`{x} union R`, `|R|=r`.

Witnesses wholly inside a single `H_a` contribute at most `|H_a|`; summed
over all runs, at most `h`.

Consider a witness not wholly inside one high run, and let `H_a,H_b` be the
first and last high runs it meets.

* If `a<b`, fix this pair.  The start lies in `H_a` or in the zero run just
  before it, and the end lies in `H_b` or in the zero run just after it.
  Its old projection has the form

  ```text
  P_u union C_(a,b) union Q_v,
  ```

  where `P_u` ranges over suffix-OR states of the left wing, `Q_v` ranges
  over prefix-OR states of the right wing, and the material strictly between
  the wings has fixed union `C_(a,b)`.  Distinct maximal high runs have a
  nonempty zero run between them.  Its entries have nonempty old
  projections, so `C_(a,b)` is nonempty.  The sharpened form of Section 3
  gives at most `k` distinct rank-`r` targets for this pair.  There are
  `C(q,2)` pairs.

* If `a=b`, a noninternal witness has exactly one of three endpoint types:
  it starts in the preceding zero run and ends in `H_a`; it starts in `H_a`
  and ends in the following zero run; or it starts in the preceding zero run
  and ends in the following zero run.  Each type is again a product of two
  OR-state chains around a fixed middle.  In the first two types one chain
  consists of nonempty suffixes or prefixes of a zero run; in the third type
  both do.  Hence each type contributes at most `k` distinct rank-`r`
  targets.  Missing boundary-side runs only reduce this count.  Thus these
  cases contribute at most `3qk`.

The categories are disjoint and exhaustive.  Adding their bounds to the
`h` internal witnesses proves (5.2), and (5.1)+(5.2) gives (5.3).  QED.

## 6. Exact finite consequences for the hard even-to-odd steps

For old even dimension `k=2r`, put `M=C(k,r)`.  At an exact target length
`B(k+1)`, (5.1) gives `h<=B(k+1)-M`, while (5.2) gives

```text
h >= M-k(C(q,2)+3q).
```

Consequently a necessary condition is

```text
k(C(q,2)+3q) >= 2M-B(k+1).                            (6.1)
```

The exact arithmetic below uses only the certified rank-count values.

| old `k` | `M` | `B(k)` | target `B(k+1)` | saving `2B(k)-B(k+1)` | one-transition ceiling `d+k` | `2M-B(k+1)` | required `q` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 12 | 924 | 926 | 1,719 | 133 | 14 | 129 | at least 3 |
| 14 | 3,432 | 3,434 | 6,438 | 430 | 16 | 426 | at least 6 |
| 16 | 12,870 | 12,873 | 24,313 | 1,433 | 19 | 1,427 | at least 12 |
| 18 | 48,620 | 48,623 | 92,381 | 4,865 | 21 | 4,859 | at least 21 |

For example, at `k=12`, `q=2` gives only
`12(C(2,2)+6)=84<129`, while `q=3` gives `144`; the other thresholds are
checked in the same way.  Thus:

* no one-transition lift can preserve `B(k)` in any hard row;
* the two-ended endpoint lift, which has at most two high runs, cannot even
  meet the first required architecture;
* the number of genuinely separate high runs must grow: `3,6,12,21` in the
  four finite hard steps.

The bound does not prohibit those values of `q`; it is necessary, not
sufficient.  At the least allowed `q`, (5.2) and exact total length force the
following high-position ranges:

| old `k` | least `q` | high positions `h` allowed by the two bounds |
|---:|---:|---:|
| 12 | 3 | `780 <= h <= 795` |
| 14 | 6 | `2,970 <= h <= 3,006` |
| 16 | 12 | `11,238 <= h <= 11,443` |
| 18 | 21 | `43,706 <= h <= 43,761` |

So a viable theorem would need long high runs as well as many transitions;
inserting a few isolated high-bit separators is not enough.

## 7. Exact abstract criterion for a multi-transition fusion

There is a clean necessary-and-sufficient target for any future fusion.
Let `p_1,...,p_N` be subsets of `[k]` (empty is allowed at high-tagged
positions), and let `epsilon_i in {0,1}`.  Assume entries with `epsilon_i=0`
have `p_i` nonempty.  Define

```text
w_i = p_i                    if epsilon_i=0,
w_i = p_i union {x}          if epsilon_i=1.
```

Then `W=(w_i)` is universal on `[k] union {x}` if and only if both hold:

1. for every nonempty `S subseteq [k]`, some interval with all tags zero has
   projected union `S`;
2. for every `S subseteq [k]`, including the empty set, some interval meeting
   a tag-one position has projected union `S`.

The proof is immediate but the seam content is exact: condition 1 gives
precisely the targets avoiding `x`; condition 2 gives precisely
`S union {x}`.  Conversely, witnesses for those two kinds of target in any
universal word have exactly these properties after projecting away `x`.

Thus a multi-transition theorem can meet the run counts in Section 6 in
principle; the rank arithmetic does not rule them out.  But it must construct
a genuine **double interval cover** with at least the displayed number of
high runs.  Universality of one intact base word supplies only condition 1
in one zero block and gives no such multi-run decomposition.  Endpoint
nesting supplies at most the two outer seams in (2.2).  Therefore no claimed
recursive improvement follows from the base length or from endpoint chains
alone.

## 8. Conditional finite upper improvements from an endpoint chain

Let `U(k)` be the currently certified nonzero upper length.  If an
independently certified word of length `U(k)` has a terminal descending chain
of length `t`, Theorem 2.1 gives `2U(k)-t+1` in the next dimension.

| target `K` | base `k` | current `U(k)` | current `U(K)` | endpoint bound | improves current when |
|---:|---:|---:|---:|:---|:---|
| 13 | 12 | 926 | 1,852 | `1,853-t` | `t>=2` |
| 14 | 13 | 1,852 | 3,676 | `3,705-t` | `t>=30` (impossible in a reduced word) |
| 15 | 14 | 3,676 | 7,352 | `7,353-t` | `t>=2` |
| 16 | 15 | 7,352 | 14,704 | `14,705-t` | `t>=2` |
| 17 | 16 | 14,704 | 29,408 | `29,409-t` | `t>=2` |
| 18 | 17 | 29,408 | 58,816 | `58,817-t` | `t>=2` |
| 19 | 18 | 58,816 | 117,632 | `117,633-t` | `t>=2` |

No endpoint data from the stored certificates was inspected here, so these
are conditional implications, not new certified numeric upper bounds.
With an ascending prefix of length `s` as well, Theorem 2.2 replaces the
one-ended saving `t-1` by `s+t-2`.  For the exceptional target `K=14`, it
would require `s+t>=31`, impossible after adjacent-duplicate reduction since
`s,t<=13`.

If the odd-dimensional base were itself optimal, the easy odd-to-even steps
would need only short endpoint chains:

| exact base | exact target | sufficient terminal `t` | sufficient `s+t` |
|:---|:---|---:|---:|
| `B(13)=1,719` | `B(14)=3,434` | 5 | 6 |
| `B(15)=6,438` | `B(16)=12,873` | 4 | 5 |
| `B(17)=24,313` | `B(18)=48,623` | 4 | 5 |

By contrast, the hard even-to-odd steps would require one-ended chain lengths
`134,431,1,434,4,866`, respectively, far beyond the strict-chain maximum.
This cleanly separates the potentially endpoint-solvable odd-to-even seams
from the necessarily many-run even-to-odd fusions.

## 9. Final seam audit

The constants in Sections 4--6 use `k`, not `k+1`.  This is justified in
every cross category, with no implicit empty-state assumption:

* at a unique zero/high transition, the zero-side suffix or prefix is
  nonempty;
* when the first and last high runs differ, the fixed middle contains the
  nonempty old projection of an intervening zero run;
* when they agree but the interval is noninternal, at least one endpoint
  lies in a zero run, giving a nonempty suffix/prefix chain.

The three same-run endpoint types are exhaustive, and intervals wholly in a
high run were already charged to `h`.  Rechecking (6.1) with the sharpened
factor gives the final required run counts `3,6,12,21`.  In particular, for
`k=16`, eleven runs give only

```text
16(C(11,2)+33)=16*88=1,408 < 1,427,
```

whereas twelve give `16(C(12,2)+36)=16*102=1,632`.
