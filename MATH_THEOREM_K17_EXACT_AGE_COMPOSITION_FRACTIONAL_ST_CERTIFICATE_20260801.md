# Exact age-composition certificate for the `k=17` fractional trace gate

Date: 2026-08-01

Status: unconditional exact rational certificate.  It proves that the
unpunctured triangular rank vector for `k=17` belongs to the symmetric
rank-only fractional marked-trace polytope `ST_(17,9,3)`.  It does not select
one trace per owner and does not solve the physical `k=17` construction.

## 1. Parameters

For `k=17`,

\[
 r=9,\qquad d=3,\qquad W={17\choose9}=24310=17\cdot1430.
\]

The triangular boundary correction is zero, so the required marked mass at
rank `s` is

\[
                         q_s={\binom{17}s\over24310}.
\]

Use denominator `D=1430`.

## 2. Stationary age types

Place the following integer masses on age compositions
`c=(c_0,c_1,c_2,c_3)`:

| type | mass |
|---|---:|
| `(1,5,2,1)` | 139 |
| `(1,6,1,1)` | 297 |
| `(2,5,1,1)` | 8 |
| `(3,3,2,1)` | 20 |
| `(3,4,1,1)` | 20 |
| `(4,3,1,1)` | 140 |
| `(5,1,2,1)` | 127 |
| `(5,2,1,1)` | 237 |
| `(6,1,1,1)` | 442 |

Their total is `1430`.

The following directed arc masses give the same row and column sums:

```text
(1,5,2,1) -> (6,1,1,1) : 139

(1,6,1,1) -> (5,1,2,1) : 127
(1,6,1,1) -> (6,1,1,1) : 170

(2,5,1,1) -> (6,1,1,1) :   8
(3,3,2,1) -> (5,2,1,1) :  20
(3,4,1,1) -> (3,3,2,1) :  20
(4,3,1,1) -> (4,3,1,1) : 139
(4,3,1,1) -> (6,1,1,1) :   1

(5,1,2,1) -> (2,5,1,1) :   8
(5,1,2,1) -> (5,2,1,1) : 119

(5,2,1,1) -> (1,5,2,1) : 139
(5,2,1,1) -> (5,2,1,1) :  98

(6,1,1,1) -> (1,6,1,1) : 297
(6,1,1,1) -> (3,4,1,1) :  20
(6,1,1,1) -> (4,3,1,1) :   1
(6,1,1,1) -> (6,1,1,1) : 124
```

Every displayed arc satisfies

\[
                         c'_{i+1}\le c_i
                         \qquad(0\le i<3).
\]

Thus these masses form an exact normalized circulation on the
age-composition graph.  Its positive directed support is weakly connected:
the two unit cross-arcs between `(4,3,1,1)` and `(6,1,1,1)` splice the
otherwise isolated self-loop bank into the main Eulerian component.

## 3. Exact marked-rank capacities

For a type `c`, its distinct proper suffix ranks are

\[
 R(c)=\{c_0,\ c_0+c_1,\ c_0+c_1+c_2\}\cap[1,8].
\]

Summing stationary mass over the types containing each rank gives:

| rank `s` | required `D q_s=binom(17,s)/17` | capacity | slack |
|---:|---:|---:|---:|
| 1 | 1 | 436 | 435 |
| 2 | 8 | 8 | 0 |
| 3 | 40 | 40 | 0 |
| 4 | 140 | 140 | 0 |
| 5 | 364 | 364 | 0 |
| 6 | 728 | 728 | 0 |
| 7 | 1144 | 1144 | 0 |
| 8 | 1430 | 1430 | 0 |

Marks are splittable and independent across distinct available ranks, so
these inequalities give exact mark variables with total required mass at
every rank.  The audited age-composition quotient therefore yields

\[
                         \boxed{q\in ST_{17,9,3}}.
\]

## 4. What this closes

The formerly open `k=17` **fractional rank-circulation** row is now closed.
In particular, the triangular lower-rank histogram has no hidden stationary
age/trace obstruction.

The certificate deliberately repeats owner mass fractionally.  It does not
provide:

* one selected literal trace for each of the 24310 named owners;
* a connected/rooted Euler trail;
* Johnson adjacency, q1 rainbows, or a Catalan Hamilton connector;
* residence after physical opening and joining;
* arbitrary-width upper witnesses; or
* an occurrence-labelled lower/common-cap compiler matching.

Consequently it does not change the certified interval

\[
                  24313\le\nu(17)\le25746.
\]

## 5. Independent executable audit

The exact integer verifier is

```text
scratch/audit_k17_age_composition_fractional_certificate_20260801.cpp
SHA256 866b30d1c05424eb606153e70d670af3aedb19d4269f3244bce71cb411121fc6
```

It was compiled on H100 with `g++ -O3 -std=c++20 -Wall -Wextra -pedantic`
and reports

```text
PASS_K17_AGE_COMPOSITION_FRACTIONAL_ST_CERTIFICATE
```

The H100 binary used for that replay had SHA256
`8ec9e432cc68fb46c2c04492152b7e9b8fda474ed502d901429726571619c3c1`.

The connected type-transition multigraph was also expanded by a deterministic
Hierholzer replay into one 1430-position cyclic type word:

```text
scratch/build_k17_age_type_euler_word_20260801.cpp
SHA256 02c098c7fa691b20115a7c63ec4beb5afe90c6492b878965253bc08ad46c4fd8

scratch/k17_age_type_euler_word_20260801.tsv
SHA256 e55bea5534c80560755dbc34a1f40e5cb9e67bca23e82d72caf902d2a1fd39f8
```

The H100 replay reports

```text
PASS_K17_CONNECTED_AGE_TYPE_EULER_WORD length=1430 start_type=0
```
