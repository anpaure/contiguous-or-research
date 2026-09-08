# An explicit length-6459 covering word for `k=15`

Date: 2026-07-29

## Result

There is an explicit nonzero word of length

\[
                              \boxed{6459}
\]

whose contiguous ORs contain every nonempty subset of `[15]`.  Together
with the proved monotone-deadline lower bound `B(15)=6438`, this gives

\[
                         \boxed{6438\le \nu(15)\le6459}.       \tag{1}
\]

The word is

```text
scratch/k15_h19_exact_compiler_maxcoverage_s1501.incumbent.word
```

with SHA-256

```text
997b50c0ff40b3c6b9d9506dfea0d3c01024fcf9ccb6988d6ee6a4f55ac46e7f
```

The solver-independent verifier

```text
scratch/verify_k15_6459_upper_bound.py
```

checks every one of the `2^15-1=32767` required masks directly.

## Construction

Start from the certified Hall-19 middle carrier

```text
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
```

whose SHA-256 is

```text
86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
```

It is a Johnson path through all 6,435 rank-eight masks, is depth-three
resident, and has complete upper shadows.  Its maximal erosion has length
6,438.

The old `Hall 19` number was only an outer incidence relaxation: it matched
16,364 of the 16,383 lower targets to individually compatible short
intervals, but did not assert that all those assignments coexist in one
source word.  The exact common-word model in

```text
scratch/optimize_k15_exact_compiler_maxcoverage.py
```

implements the negative-window realization theorem directly.  It chooses
distinct target intervals and defines

\[
 A_{p,x}=1
 \quad\Longleftrightarrow\quad
 x\in P_p\text{ and no selected interval containing }p\text{ omits }x.
                                                               \tag{2}
\]

The model simultaneously enforces:

1. exact OR on every selected lower-target interval;
2. `D^3 A=T` for the fixed middle carrier;
3. nonzero source letters; and
4. distinct physical witness intervals.

Its audited dimensions are

```text
lower targets          16,383
physical cells         19,311
outer Hall edges      133,852
source incidences      32,202
```

CP-SAT found a 6,438-entry common word covering 16,362 lower targets and
reported that objective optimal for this fixed model in 69.7 seconds.  The
prefix itself misses exactly 21 masks.  Appending those 21 masks as singleton
letters gives the displayed length-6,459 word.  The upper-bound claim uses
only the explicit word and exhaustive verifier; it does not depend on
trusting the solver's optimality status.

## Exact residual

The 6,438-entry prefix misses

```text
685, 960, 1103, 2420, 2575, 2676, 4469,
5801, 7267, 7504, 8250, 9524, 12825,
13616, 13620, 17683, 17738, 19098, 19568,
21641, 29776
```

with rank histogram

```text
rank 4:  1
rank 5:  1
rank 6: 14
rank 7:  5
```

The suffix of the stored word is exactly this residual set.  Thus every old
prefix interval survives and each missing mask acquires a one-letter witness.

## Independent verification

Run

```bash
python3 scratch/verify_k15_6459_upper_bound.py \
  scratch/k15_h19_exact_compiler_maxcoverage_s1501.incumbent.word \
  scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json \
  --output scratch/k15_h19_exact_compiler_maxcoverage_s1501.verify.json
```

The verifier checks:

- length 6,459 and every entry nonzero;
- all 32,767 nonempty masks by direct contiguous-OR enumeration;
- the first 6,438 entries miss exactly the listed 21 masks;
- the appended suffix equals that residual;
- `D^3` of the prefix is the certified 6,435-mask carrier; and
- the carrier is a permutation of the rank-eight layer.

The resulting compact certificate is

```text
scratch/k15_h19_exact_compiler_maxcoverage_s1501.verify.json
```

## Interpretation

For this fixed carrier, the outer Hall relaxation and the exact common-word
compiler differ by two units:

```text
outer matching deficiency        19
exact realizable prefix deficit   21
```

This explains why `Hall 19` did **not** itself imply a length-6,457 word.
The general `k=15` problem is now only 21 positions from the conjectured
optimum, but closing those positions still requires either a better carrier
or a joint carrier/compiler move; the fixed carrier cannot simply realize
its entire outer matching independently.
