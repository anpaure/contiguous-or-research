# Independently audited K16 length-12,874 phase-collar certificate

Date: 2026-07-30

## Theorem and scope

The retained word

```text
answers/k16_upper12874.word
```

has length `12874`, SHA-256

```text
631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e,
```

and every one of the `65535` nonempty K16 masks is the OR of a literal
contiguous interval of this word.  Consequently

\[
                         \boxed{12873\le \nu(16)\le12874}.
\]

The lower endpoint is the general counting bound

\[
\binom{16}{8}+d(16)=12870+3=12873.
\]

This theorem does **not** determine whether `nu(16)` is `12873` or `12874`.

## Frozen source and exact SAT model

The source is the length-12,874 one-hole word

```text
scratch/k16_append0200_12874_onehole.word
SHA-256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18.
```

Independent suffix-state replay gives its exact missing family

\[
                              \{0x287d\}.
\]

The SAT model makes every cell in the three half-open collars

\[
[0,5),\qquad[6436,6445),\qquad[12870,12874)
\]

an arbitrary nonzero 16-bit mask.  Their widths are `5,9,4`, for 18 editable
cells.  All other source cells are frozen.

The two intervening fixed gaps have total ORs

\[
                              0x7fff,\qquad0xffff.
\]

Intervals wholly inside a fixed gap are replayed before formula construction.
For every remaining target, each entire gap has a forbidden bit; consequently
no missing target can have a witness crossing a fixed gap.  Every relevant
new witness is therefore contained in one collar, possibly extended by a
suffix of its left adjacent gap and a prefix of its right adjacent gap.

For each such interval pattern and target (t), its witness variable forces:

* every zero bit of (t) absent from every chosen collar cell; and
* each one bit of (t) missing from the adjacent fixed OR present in at least
  one chosen collar cell.

An at-least-one clause over exact patterns is imposed for each of the 57
residual targets, and every editable cell has a nonzero clause.  Hence the CNF
is satisfiable exactly when this 5/9/4 template contains a literal universal
word.

An independent implementation reconstructed the complete ordered DIMACS
clause sequence and matched the retained CNF exactly:

```text
288 cell-bit variables
4818 witness variables
5106 total variables
18 cell-nonzero clauses
57 target-ALO clauses
35854 positive-bit witness clauses
121818 zero-bit exclusion clauses
157747 total clauses
```

## Independent SAT decode

The CaDiCaL output has exit code `10`, status `SATISFIABLE`, and a complete,
consistent assignment of all `5106` variables.  Independent evaluation found
zero failed clauses.  Decoding only variables `1..288`, without using the
primary decoder, gives the following 18-cell ledger:

| position | source | decoded | changed |
|---:|---:|---:|:---:|
| 0 | 34860 | 18553 | yes |
| 1 | 10281 | 10240 | yes |
| 2 | 8297 | 8297 | no |
| 3 | 109 | 101 | yes |
| 4 | 1069 | 1060 | yes |
| 6436 | 18033 | 16497 | yes |
| 6437 | 32768 | 32768 | no |
| 6438 | 18553 | 2169 | yes |
| 6439 | 10361 | 10345 | yes |
| 6440 | 41065 | 8301 | yes |
| 6441 | 32877 | 32877 | no |
| 6442 | 33837 | 33828 | yes |
| 6443 | 36873 | 36873 | no |
| 6444 | 50209 | 50209 | no |
| 12870 | 35938 | 35938 | no |
| 12871 | 35937 | 3 | yes |
| 12872 | 52289 | 52321 | yes |
| 12873 | 512 | 52833 | yes |

All 18 decoded values are nonzero.  Twelve cells change and six retain their
source values.  Every one of the other `12856` positions is byte-for-byte
identical to the source.  The independently decoded token stream equals both

```text
scratch/ad_k16_upper12874_phase_collar_5_9_4.word
answers/k16_upper12874.word
```

including raw whitespace bytes.

## Literal coverage audit

At each right endpoint, the independent replay retains every distinct OR of a
suffix ending there.  The candidate has at most 11 such states at an endpoint.
Their union is the complete family of `65535` nonzero masks, so the missing
set is empty.

Two retained C++ verifier outputs independently report complete coverage:

```text
phase_collar_5_9_4.verify_suffix.out
SHA-256 8d9270b00247392ac05d380c4aec7cab60a2c943edd1c3ddc81311efb2cfbd3a

phase_collar_5_9_4.verify_array.out
SHA-256 0bcfa9898658a9bfbc34a0a621b484e04e6d7e28f02c53c83c4c4135a97ce7f3
```

The literal word alone is sufficient for the upper bound; the SAT model and
decode ledger authenticate its construction.

## Frozen construction artifacts

```text
emitter
  scratch/build_ad_k16_append0200_phase_collar_cnf_20260730.py
  b3f5527a19c81069c393af3e7bece3e92d933fdfb32d4e7cd324512d02c8295f

CNF
  scratch/phase_collar_5_9_4.cnf
  5114fafcaf64009543988a1caaec6a61984bc09163200f4e18e5d1e3cd2fb9db

CNF map
  scratch/phase_collar_5_9_4.cnf.map.json
  123640e351146dabe1681d59a420658ded82cd69ce7b04dc661ab5b1a9fa517c
  payload 238075bf930c840a28e674900bbfcebf00d73d7efc3452a8251d75a31d4a036c

CaDiCaL output
  scratch/phase_collar_5_9_4.cadical.out
  59dd4dae6a6e1115d240fe077a366cc630a0b639932fb169fc2b0732e9a91669

primary decoder
  scratch/decode_verify_ad_k16_append0200_phase_collar_cnf_20260730.py
  7f2c62c697327ce50f97867060a1e153e70313803baa10c7c4726571fb0d8056

primary decode audit
  scratch/ad_k16_upper12874_phase_collar_5_9_4.decode.audit.json
  44b57f68223fff0cfab0d3dedafad4f4835c86db3e5085aca6776fa96e418a26
  payload aa0a1bfaed27440f228aa7a55f758d5e1aa2e5f352caf033282e843d39744162
```

## Independent replay artifacts

```text
scratch/audit_ad_k16_upper12874_phase_collar_independent_20260730.py
SHA-256 daa12d77fe5ca736136fd06d70635b77aa91c56eed195ddd337a7b0cf0d2122e

scratch/ad_k16_upper12874_phase_collar_independent_20260730.audit.json
file SHA-256    dc800a738a0c771a50c01dd9b8cfb39df6e3b4e25769f713814d0926b5b458ea
payload SHA-256 9fbb3caeab9d479547f714a00c98b828268596d92a433afcc4902a414f9ed0c5
```

The independent replay is local-light, solver-free after reading the retained
assignment, and completed in 0.20 seconds.
