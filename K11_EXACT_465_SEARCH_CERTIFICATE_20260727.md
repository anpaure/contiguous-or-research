# Exact computational certificate for k=11

Date: 2026-07-27

## Result

The search produced a nonzero 465-entry word on the nonempty subsets of
`[11]` whose contiguous unions contain every one of the `2^11-1=2047`
nonempty subsets.  The independently audited counting bound gives

\[
W=\binom{11}{6}=462,
\qquad
\Lambda=\sum_{j=1}^{5}\binom{11}{j}=1023,
\]

and the least `d` with

\[
dW+\binom{d+1}{2}\geq\Lambda
\]

is `d=3`, because `2W+3=927<1023` whereas `3W+6=1392>=1023`.
Consequently `B(11)=W+d=465`.  The word therefore proves the finite exact
result

\[
\boxed{\nu(11)=B(11)=465}.
\]

This closes the previously missing case in the verified range `k<=12`.
It is not a proof of `nu(k)=B(k)` for every `k`.

## Artifacts

- Exact word: `scratch/sigma_sat_k11_465.word`
- Minimal independent verifier: `scratch/sigma_sat_verify_word.py`
- Quotient SAT search: `scratch/sigma_sat_solver.py`
- Independent Hall compiler: `scratch/sigma_sat_verify_certificate.py`
- Central certificate: `scratch/sigma_sat_k11_allcentral_cap2.certificate.json`
- Compiler report: `scratch/sigma_sat_k11_allcentral_verify.json`
- Detailed reproduction guide: `scratch/sigma_sat_README.md`
- Independent structural audit: `scratch/sigma_calibration_final_k11_audit.md`

The word's SHA-256 is

```text
746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850
```

### Cleaner bulk-compiler representative

The later first-derivative compiler produces a second independently verified
optimal word,

```text
scratch/sigma_calibration_bulk_k11_465.word
```

with SHA-256

```text
bda651d3e40d0920d3e6ed12e6a2091e477695d8ad7f6bd186b831f087cf136a
```

Its derivative profile is cleaner:

| row | rank histogram |
|---|---|
| `D^0` | `1:11, 2:57, 3:397` |
| `D^1` | `4:464` |
| `D^2` | `5:463` |
| `D^3` | `6:462` |

It preserves the entire derivative tower by enforcing only `DC=DP`, then
uses the exact surplus-Hall criterion on the strict-low targets.  Translation
uncrossing reduces its bulk Hall proof to 63 quotient inequalities, whose
minimum nonempty margin is two.  The original word remains the frozen first
certificate; this second word is the more economical mathematical normal
form.

### Full multirow representative

The depth-`d` sandwich compiler produces a third independently verified
optimal word:

```text
scratch/sigma_multirow_k11_465.word
```

Its SHA-256 is

```text
a7b4395d35658e2860cfa12e6419aef1e528dd7b6ab40833edeeb7dc153ccaf3
```

The compiler has 3,784 variables and 11,913 clauses and solves in about
0.004 seconds.  Unlike the literal-base-row compiler, it searches all three
lower derivative rows simultaneously while preserving the middle and upper
tower through `D^3C=D^3P`.  Its profile is

| row | rank histogram |
|---|---|
| `D^0` | `1:11, 2:55, 3:399` |
| `D^1` | `3:8, 4:456` |
| `D^2` | `5:463` |
| `D^3` | `6:462` |

This is the representative whose architecture remains meaningful after the
one-row asymptotic capacity correction.

### PBBS cycle-space representative

An independent central route begins at the canonical PBBS factor.  A
17-orbit alternating circuit yields one voltage-two quotient cycle with
complete shadows and zero depth-three residence defects.  The multirow
compiler produces

```text
scratch/pbbs_k11_res3_conn_multirow_465.word
```

with SHA-256

```text
52d16a4b280601645e1d0265bf6f102c38667285e9c3ebbcadfd6f073b78ef59
```

and the independent verifier again reports 2,047/2,047 masks.  This proves
that the central solution is not isolated: a canonical carrier can be
coherently repaired by explicit cycle-space trades and passed through the
same exact compiler.

## Search architecture

Translation by `Z_11` reduces the middle-layer problem to 42 five-set
orbits.  Each orbit has 15 possible two-point extensions.  The final CNF
enforces:

1. one extension per lower orbit;
2. degree two at every middle orbit;
3. full rank-seven coverage with load at most two;
4. full lower and upper depth-two coverage;
5. no residence violation at delays one, two, or three;
6. a quotient Hamilton cycle with nonzero voltage.

The final formula has 27,103 variables and 1,728,029 clauses.  Kissat solved
it in 13.95 seconds in the original run.  A clean rerun took 17.83 seconds
including Python construction and reproduced the same central certificate.

The lifted object is a 462-cycle of all rank-six masks.  It has voltage two,
zero residence violations, and complete lower and upper shadows at every
depth.  All 242 safe cuts pass the flat-delay-three short-cell Hall gate.
The deterministic compiler uses cut 1 and the boundary flag

```text
155 > 154 > 152
```

and obtains a 231/231 residual matching.  Compilation takes about 0.04
seconds and deterministically reproduces the exact word.

## Independent verification

The final word was checked in three independent ways:

1. direct enumeration of all 108,345 contiguous intervals;
2. a suffix-state dynamic program;
3. the derivative/tableau structural auditor.

All report zero missing masks.  The derivative rows are:

| row | length | distinct | rank histogram |
|---|---:|---:|---|
| `D^0` | 465 | 231 | `1:11, 2:55, 3:399` |
| `D^1` | 464 | 332 | `2:1, 3:1, 4:462` |
| `D^2` | 463 | 462 | `5:463` |
| `D^3` | 462 | 462 | `6:462` |

In particular, `D^3` is exactly the set of all 462 rank-six masks.

Run the standalone check with:

```sh
python3 scratch/sigma_sat_verify_word.py \
  --k 11 scratch/sigma_sat_k11_465.word
```

Expected headline:

```text
PASS k=11 length=465 covered=2047/2047
```

## Reproduction

```sh
python3 scratch/sigma_sat_solver.py \
  --k 11 --q2 --lower-q2 \
  --residence 3 --direct-residence --direct-connectivity \
  --time-per-round 600 --max-rounds 30 \
  --prefix scratch/sigma_sat_k11_allcentral_cap2

python3 scratch/sigma_sat_verify_certificate.py \
  scratch/sigma_sat_k11_allcentral_cap2.certificate.json \
  --compiled-word scratch/sigma_sat_k11_465.word \
  --report scratch/sigma_sat_k11_allcentral_verify.json

python3 scratch/sigma_sat_verify_word.py \
  --k 11 scratch/sigma_sat_k11_465.word
```

## Smaller-instance calibration

The same standalone verifier passes the stored exact words throughout the
nontrivial smaller calibration range, as well as the prior `k=12` result:

| k | B(k) | masks covered |
|---:|---:|---:|
| 3 | 4 | 7/7 |
| 4 | 7 | 15/15 |
| 5 | 12 | 31/31 |
| 6 | 21 | 63/63 |
| 7 | 37 | 127/127 |
| 8 | 72 | 255/255 |
| 9 | 128 | 511/511 |
| 10 | 254 | 1023/1023 |
| 11 | 465 | 2047/2047 |
| 12 | 926 | 4095/4095 |

The central SAT modules benchmarked as follows:

| k | model | solve time |
|---:|---|---:|
| 5 | translation quotient, both depth-two sides | 0.0029 s |
| 7 | translation quotient, both depth-two sides | 0.0036 s |
| 9 | full non-quotient, both depth-two sides | 4.20 s |
| 11 | translation quotient, both depth-two sides plus residence | 13.95 s |

For `k=5,7`, cyclic equivariant residence is stronger than the structure of
the known optimal linear words, so those rows calibrate the central modules
and the final-word verifier separately.  The `k=11` calculation is the first
end-to-end success of this quotient-central-plus-Hall pipeline.
