# Exact audit of the braided-complement odd-to-even recipe

Date: 2026-07-29

This note audits `Downloads/opusproblem/work/braidrecipe.py`.  Its useful
observation is correct, but it is only the cross-edge legality test.  The
claimed reduction to a small CSP over offsets and block lengths omits the
palette, residence, higher-shadow, and compiler constraints.  Moreover, the
strict recipe cannot lift the known optimal `k=15` factor to `K=16`; there is
a four-edge, solver-free obstruction.

## 1. Exact two-rail identities

Let `k=2m+1`, let `V=[k]`, let `r=m+1`, and add a new point `z`.  For
rank-`r` sets `X,Y subset V`, define

```text
A_X = X,
B_Y = (V \ Y) union {z}.
```

Both are rank-`r` vertices of `J(2m+2,r)`.

### Cross-edge lemma

`A_X` and `B_Y` are Johnson-adjacent if and only if

```text
X union Y = V.
```

Indeed, this is equivalent to `V\Y subset X`; the low part of `B_Y` then
has size `r-1` and differs from `X` by one point.  At such a cross edge,

```text
A_X intersection B_Y = X \ Y,          (rank r-1, no z)
A_X union        B_Y = X union {z}.     (rank r+1, with z)
```

Thus `union = FULL` proves exactly one thing: the hand-off is a legal
Johnson edge.  It supplies a no-top lower-q1 colour and a top upper-q1
colour.  It does not supply a top lower-q1 colour.

For rail edges, with `X,X'` and `Y,Y'` Johnson-adjacent,

| edge | lower-q1 colour | upper-q1 colour |
|---|---|---|
| `A_X A_X'` | `X intersection X'` | `X union X'` |
| `B_Y B_Y'` | `{z} union (V \ (Y union Y'))` | `{z} union (V \ (Y intersection Y'))` |
| cross | `X \ Y` | `X union {z}` |

Consequently:

1. Cutting an `AA` edge can destroy a no-top lower or upper colour.
2. Cutting a `BB` edge can destroy a top lower or upper colour.
3. Cross edges can repair only the first lower type and the second upper
   type.  The other losses must retain another rail witness.

These are global palette constraints, not consequences of cross-edge
legality.

## 2. Residence and shadows are separate constraints

Along the `A` rail, an old coordinate `x` has trace `1[x in X]`; along the
`B` rail it has trace `1[x notin Y]`.  At an `A->B` cross edge an old
coordinate can only be deleted, and at a `B->A` cross edge it can only be
inserted.  The new coordinate is precisely the indicator of being on the
`B` rail.

Therefore a child carrier of depth `d` additionally requires:

* every internal `B` block has length at least `d+1` (new-point
  residence);
* every old-coordinate run created within or across the rail blocks has
  length at least `d+1`.

For a same-parent complement rail, a parent gap of length `<d+1` becomes
a short positive run on the `B` rail.  It must be hit by a rail cut or put
at a global boundary.  The identity `X union Y=V` does not do this.

Higher shadows are independent as well.  For a `B`-only window, De Morgan
gives

```text
intersection_j B_{Y_j} = {z} union (V \ union_j Y_j),
union_j        B_{Y_j} = {z} union (V \ intersection_j Y_j).
```

Segmenting the parent cycle deletes witnesses, while mixed windows create a
different family of values.  All relevant fixed-window palettes must be
audited after stitching.  Finally, even a carrier passing residence and all
upper/lower palettes still needs the lower erosion-envelope SDR (the exact
compiler Hall condition).  The `K=8` validation below needed a favourable
linear cut; this is not automatic.

## 3. Small exact fixed-parent model

The reproducible model is

[`scratch/audit_braided_complement_fixed_parent_20260729.py`](scratch/audit_braided_complement_fixed_parent_20260729.py).

For a fixed cyclic parent `F`, its graph contains:

* both copies of every parent-cycle edge;
* **all** cross edges satisfying the cross-edge lemma (not merely one
  offset family).

It chooses a spanning Hamilton path, imposes every child lower- and
upper-q1 colour directly from the literal edge intersections/unions, and
adds sound lazy cuts for subtours and short residence motifs.  Hence
`INFEASIBLE` is exact for this fixed graph and these gates.  A `PASS` is
then sent to the exact compiler and exhaustive OR verifier.

Results (CPU only on `h100`; peak RSS at most 137 MB):

| child | fixed parent | graph | result |
|---|---:|---:|---|
| `K=8` | fresh decorated `k=7` spiral | 70 vertices, 210 edges | `PASS_Q1_RESIDENCE`; compiled to a verified 72-word |
| `K=10` | fresh decorated `k=9` spiral | 252 vertices, 882 edges | `INFEASIBLE` after 4 sound lazy rounds |
| `K=12` | the known optimal `k=11` spiral | 924 vertices, 3696 edges | `INFEASIBLE` after 5 sound lazy rounds |

Important scope: the two negative rows refute these fixed parents, not every
possible odd parent.  They nevertheless refute the idea that a decorated
odd solution automatically lifts by choosing a few seam offsets.  The known
even optima reinforce this: when their `A` and complemented-`B` rail edges
are superposed, many vertices have degree 3 or 4, so they are not cuts of one
common odd parent cycle.

The verified `K=8` word is
[`scratch/k8_exact.word`](scratch/k8_exact.word) (SHA-256
`f47a5f5789210816a21465ddfbc2fd07eb6c22a2007838d80fbe6d03dbfa1416`),
length 72, with all 255 nonempty ORs covered.

## 4. A solver-free obstruction for the known k=15 factor

Let `F` be the verified optimal `k=15` two-cycle factor (cycle lengths
6390 and 45) used to produce `nu(15)=6438`.  Child depth is `d(16)=3`, so
every internal positive run must have length at least 4.

In the 6390-cycle, the five consecutive parent states at positions
796 through 800 are

```text
7621, 7652, 7412, 6390, 4343.
```

For coordinate 0 their trace is

```text
1, 0, 0, 0, 1.
```

On the complemented `B` rail this becomes `0,1,1,1,0`, a forbidden
positive run of length 3.  Therefore any valid same-parent braid must cut
at least one of the four `B` edges 796,797,798,799.

Their parent union labels are respectively

```text
7653, 7668, 7414, 6391.
```

Each label occurs **exactly once among all 6435 edges of both parent
cycles**.  Therefore each corresponding child top lower-q1 colour

```text
{z} union (V \ U)
```

also occurs on exactly that `BB` edge.  Numerically the four child colours
are `57882, 57867, 58121, 59144`.  No `AA` or cross edge contains `z` in
its intersection, so none can recreate one of these colours.  Lower-q1
completeness therefore forces all four edges to remain.

This contradicts residence.  Hence:

> **No-go theorem.** No chronology obtained from the two copies of the
> known optimal `k=15` factor by cutting rail edges and inserting arbitrary
> legal complement cross seams can be both depth-3 resident and lower-q1
> complete.  In particular it cannot yield an optimal `K=16` word.

There are 270 such immediately contradictory short-gap motifs; the single
one above is already a complete certificate.  Its solver-free replay is
[`scratch/verify_k15_braided_complement_four_edge_nogo_20260729.py`](scratch/verify_k15_braided_complement_four_edge_nogo_20260729.py).
The larger payload and exact
hitting/palette replay are saved as
[`scratch/k15_complement_braid_gapcut_payload.json`](scratch/k15_complement_braid_gapcut_payload.json)
and [`scratch/k15_gapcut_result.json`](scratch/k15_gapcut_result.json).

## 5. Verdict for K15 -> K16

The strict proposal in `braidrecipe.py` is **not a live lift of the known
`k=15` answer**.  Its intended parent is ruled out before connectivity,
higher shadows, or compilation enter.

A generalized construction in which the `A` and `B` rails are independently
rethreaded remains open.  But then the task is no longer “odd spiral plus a
small seam schedule”: it is the full bilayer/dual-rail carrier problem, since
the new `BB` edges must redesign the top lower-q1 palette while repairing
complement residence.  That is plausibly useful architecture, but not the
cheap explicit recipe claimed in the Claude ledger.

## Artifact hashes

```text
fixed-parent model
  ca0870ba2531f6d546b8ab92243742fb3d2f91920f1839c1489363ede35d9b3f
k=7 parent
  6840481200f331919019da1a5fca2dc6430bb78bab368c3a26f077ee5b5a46dd
K=8 fixed-parent carrier
  1f31d3b53c6620d828d996af0187b5ecf5d73f37b14c9ea015b47a2e1bf1d73f
K=8 verified word
  f47a5f5789210816a21465ddfbc2fd07eb6c22a2007838d80fbe6d03dbfa1416
k=9 parent / K=10 negative
  a8422de1f1caccf6cbf509896688fe578390f8f854352a08b794899f96d10528
  a8e548c0f9ed09787442f01ea0f3883129f5fda6635647ed461d1b7f220ab530
k=11 parent / K=12 negative
  7626e82e0370bfca70ab32aac062a40787e0ef987919094fc916b54f539b05d7
  ff126789edcea39eb32d4e3ac51fc8753ff2cca0d4542f0c4988c0a6a2fc832c
k=15 gap/palette payload / result
  ea0f15ec07fd27a09d0ba65e0ddc912e54772a88c202bb5d82a3bf2b9a73c21f
  76ec0b736a7b6ffe9ac0b190f56c26818d46c44b18baf5a8af889525b7816c27
k=15 four-edge solver-free verifier
  56ddb1402f704ff274a20cdadf1a250aedbf4f0d4dfb5eaf2732611d99f18d5b
```
