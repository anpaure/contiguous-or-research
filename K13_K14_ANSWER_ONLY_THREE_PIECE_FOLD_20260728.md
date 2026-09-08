# An answer-only `k=13 -> 14` three-piece fold

This computation reads only `answers/k01.word` through `answers/k14.word`.
It does not read a certificate, checkpoint, solver log, or pre-existing
analyzer output.

## Canonical middle order extracted from a word

For a word `a_0,...,a_{L-1}` and middle rank `r=ceil(k/2)`, start at each
column `i` and OR entries to the right until the rank first reaches `r`.
Keep the cell when its rank is exactly `r`, deduplicate equal masks, and order
the representatives by their right endpoint.  For every saved answer this
gives exactly `binom(k,r)` different middle masks.  This is the monotone
endpoint order `F_i=i+f_i`; it also handles the non-constant boundary depths
in the small/even answers.

## Exact fold identity

Let `P13[0..1715]` and `P14[0..3431]` be the extracted middle orders.  In
`P14`, keep precisely the rank-7 masks that do **not** contain zero-based
coordinate `13`, then delete that coordinate.  Call the resulting order `S`.

Under the coordinate relabeling from the section coordinates to the `k=13`
coordinates

```text
[8, 6, 4, 2, 7, 1, 10, 12, 11, 9, 0, 3, 5]
```

the following identity holds entry by entry:

```text
S = P13[0:419]
    + P13[1446:1716]
    + reverse(P13[419:1446]).
```

Thus the section is the saved `k=13` Hamilton path cut at exactly two edges,
with its three pieces reordered/oriented.  Its component lengths in section
order are

```text
419, 270, 1027.
```

There is no loss inside a component: all `1713` component edges are literally
relabelled `P13` edges.  The only two non-Johnson transitions are the two
deliberate seams between the three pieces.

The complementary section (coordinate `13` present, then delete it and
complement the remaining 13 coordinates) is also exceptionally structured:
it has only three Johnson components, of lengths `3, 966, 747`.  It is not a
cut/reassembly of the archived `P13` under the same exact anchor test, so an
induction should range over a **family** of optimal lower carriers rather than
insist on one canonical saved word.

Equivalently, the new-coordinate membership word along `P14` is the six-block
word

```text
0^419  1^3  0^270  1^966  0^1027  1^747.
```

So the two three-component sections are not produced by a complicated
interleaving: they are six literal sector batches.  Every old coordinate has
between 526 and 530 runs along `P14`; the new coordinate has only 6.  This
makes the lift coordinate intrinsically recognizable without knowing the
construction or trying all relabelings.

Every other one-coordinate section of `P14` has between 246 and 254
components.  Hence coordinate `13` is not a post-hoc favorable choice; it is
a uniquely visible lift coordinate.

## Candidate recurrence lemma

The finite identity suggests the following odd-to-even construction target.

> **Three-piece section-lift lemma.**  Given a suitable optimal carrier on
> `2r-1` coordinates, there is an optimal carrier on `2r` coordinates and a
> distinguished new coordinate such that one middle section is obtained from
> the old carrier by two cuts, a permutation of the three pieces, and optional
> piece reversals.  The other section is a bounded-component dual carrier;
> the six pieces are concatenated as alternating new-coordinate sector
> batches, and compatible collars at the five cross-sector seams suffice to
> lift the lower compiler.

The saved answers do **not** support a recurrence in which every next answer
is a relabelled copy of the immediately previous archived answer.  The
measured component counts for the best one-coordinate sections from `k=6`
through `13` are

```text
3, 5, 9, 17, 37, 22, 119, 3.
```

The right general object is therefore a family-valued carrier recurrence with
bounded seam interfaces, not a canonical-word recurrence.  The `13 -> 14`
fold is the first large exact member presently visible in the saved answers.

## Reproduction

```bash
python3 scratch/analyze_answer_section_recurrence.py \
  --output scratch/answer_section_recurrence_20260728.json --top 4
```

SHA-256:

```text
dfe51f3407768790a5c5b3910a9900758b5fb4e1448b3f50e9689c12a2f5f264  scratch/analyze_answer_section_recurrence.py
7776a563daaa1b4dc3fff911702336cea49860971db7eff74e5107f957bf5d89  scratch/answer_section_recurrence_20260728.json
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0  answers/k13.word
7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17  answers/k14.word
```
