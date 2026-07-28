# Exact k=14 certificate at the conjectured lower bound

## Result

There is a word of length

\[
B(14)=\binom{14}{7}+2=3434
\]

whose nonempty contiguous ORs are all (2^{14}-1=16383) nonzero masks.
Together with the proved lower bound, this establishes

\[
\boxed{\nu(14)=3434}.
\]

The word is
`scratch/k14_intersection_sixpiece_hallpass_004a.word`, with SHA-256

`7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17`.

Run the independent verifier with

```sh
python3 scratch/verify_k14_exact_3434.py
```

## Construction

Start from strict k=13 intersection-lift carrier candidate 004.  Write its
two length-1716 sectors as (A) (without the new coordinate) and (B)
(with it).  Cut (A) after positions 418 and 1445, and cut from (B) the
three-vertex block beginning at position 966.  The middle path is the
six-piece braid

\[
A_1,\quad B_2^{\rm rev},\quad A_3,\quad B_1,\quad
A_2^{\rm rev},\quad B_3.
\]

The two A cuts are not arbitrary: they expose the two rank-7 colours lost
when the length-three B block is cut out.  Consequently the five new cross
seams restore every deleted rank-8 colour.

The resulting middle path:

- contains every rank-7 mask exactly once;
- is a Johnson path;
- satisfies exact depth-two residence;
- covers every upper shadow at every depth;
- has a three-vertex run of the new coordinate, enabling its singleton in
  the lower compiler;
- passes the combined all-rank Hall audit.

The exact lower compiler then solves in under one second and produces the
length-3434 word.  Its rank profile is

\[
1^{22},\ 2^{156},\ 3^{455},\ 4^{1018},\ 5^{1782},\ 6^1.
\]

## Artifacts

- strict source: `scratch/k14_intersection_strict_candidates/candidate_004.json`
- braided carrier: `scratch/k14_intersection_sixpiece_hallpass_004a.json`
- compiler report: `scratch/k14_intersection_sixpiece_hallpass_004a.compile.json`
- exact word: `scratch/k14_intersection_sixpiece_hallpass_004a.word`
- independent verifier: `scratch/verify_k14_exact_3434.py`
- finite braid search: `scratch/search_k14_intersection_four_piece.cpp` (`six` mode)
- materializer: `scratch/materialize_k14_six_piece.py`

## Why five pieces failed and six pieces worked

An internal singleton of the new coordinate requires a middle run of length
exactly three.  Cutting such a block from (B) deletes two unique upper
rank-8 colours.  With only one cut in (A), the five-piece braid cannot
expose enough prescribed A endpoints to restore both colours; the exhaustive
100-carrier census always left at least one upper hole.  A second A cut
exposes both colours, and the six-piece alternating braid restores them while
retaining the length-three run.  This is the structural step that closes
k=14.
