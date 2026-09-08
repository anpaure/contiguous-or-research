# A depth-`d` sandwich compiler for the full lower band

Date: 2026-07-27

## 1. Motivation

The first-derivative identity

\[
C\subseteq A\subseteq P,qquad DC=DP
\quad\Longrightarrow\quad
D^tA=D^tP\ (t\ge1)
\]

is ideal at `k=11`, but it freezes every row above `D^0`.  It therefore
forces all masks below the deepest fixed rank into the base word, which is
asymptotically impossible.

The correct block version preserves only the central deadline row.  It
leaves all `d` lower rows free to share the lower ideal.

For a cyclic set word `A=(A_i)_{i in Z_N}`, write

\[
(D^hA)_i=\bigcup_{t=0}^{h}A_{i+t}.
\]

## 2. Block sandwich lemma

### Theorem 2.1

Let `0<=h<N`, and let `C,A,P` be cyclic set words of length `N` with

\[
C_i\subseteq A_i\subseteq P_i\quad(i\in\mathbb Z_N),
\qquad
D^hC=D^hP.
\tag{2.1}
\]

Then

\[
D^hA=D^hP
\tag{2.2}
\]

and

\[
D^{h+q}A=D^q(D^hP)
\qquad(q\ge0).
\tag{2.3}
\]

#### Proof

Monotonicity of union gives

\[
D^hC\subseteq D^hA\subseteq D^hP.
\]

The outside words agree, proving (2.2).  Applying `D^q` gives (2.3).  □

The first-derivative compiler is the special case `h=1`.  The useful
uniform choice is `h=d(k)`.

## 3. A canonical sparse `h`-core

The equality `D^hC=D^hP` is coordinatewise.  Fix a coordinate `x` and look
at the binary cyclic support word of `x` in `P`.

For every proper maximal 1-run

\[
R=[a,b],
\]

select `a`, `b`, and positions spaced by `h+1` from `a` until `b` is
reached.  If the support is the whole cycle, select cyclic positions so that
the distance between consecutive selected positions is at most `h+1`.
Put `x` in `C_i` exactly at the selected positions, independently for every
coordinate.

### Lemma 3.1

The resulting word satisfies

\[
C_i\subseteq P_i,
\qquad
D^hC=D^hP.
\tag{3.1}
\]

#### Proof

It is enough to show that every cyclic interval `J` of `h+1` positions which
meets the support of `x` also contains a selected support position.

If `J` meets a proper run at one of its boundary positions, that endpoint
was selected.  Otherwise its support intersection lies between consecutive
selected positions in that run.  Their cyclic distance is at most `h+1`, so
an interval of `h+1` positions cannot meet the open gap while excluding both
selected endpoints.  The full-support case is identical using the cyclic
gap condition.  Thus `J` meets the support of `C` exactly whenever it meets
the support of `P`, which is (3.1).  □

For a proper run of length `ell`, the construction uses at most

\[
1+\left\lceil\frac{\ell-1}{h+1}\right\rceil
\tag{3.2}
\]

positions.  At the deadline scale `h=Theta(sqrt(k))`, this is much sparser
than the alternating first-derivative core.

## 4. Exact central preservation

Let `T` be a cyclic chronology of all `W=binom(k,r)` middle masks and let
`d=d(k)`.  Suppose `T` is `d`-resident, so its depth-`d` erosion `P`
satisfies

\[
D^dP=T.
\tag{4.1}
\]

Construct the canonical depth-`d` core `C` of Section 3.  Then

\[
D^dC=D^dP=T.
\tag{4.2}
\]

By Theorem 2.1, **every** nonzero word `A` in the coordinatewise box

\[
C_i\subseteq A_i\subseteq P_i
\tag{4.3}
\]

has

\[
D^dA=T,
\qquad
D^{d+q}A=D^qT\quad(q\ge0).
\tag{4.4}
\]

Thus the middle row and the entire upper tower are protected while all rows

\[
A,DA,\ldots,D^{d-1}A
\]

remain available for a coupled lower-ideal construction.

## 5. Multirow compiler theorem

### Theorem 5.1

Assume the chronology `T`, erosion `P`, and core `C` above have the following
properties.

1. `T` is the complete middle layer.
2. Every upper mask occurs in some `D^qT` window which survives a common
   linear cut.
3. There is a nonzero `A` satisfying (4.3) for which

   \[
   \bigcup_{t=0}^{d-1}\{(D^tA)_i:i\in\mathbb Z_W\}
   \supseteq
   \{S:1\le |S|<r\}.
   \tag{5.1}
   \]

Cut the cycle at the common safe edge and append the first `d` entries.
Then the resulting linear word has length `W+d` and covers every nonempty
mask.  Hence

\[
\nu(k)=B(k).
\]

#### Proof

Appending the first `d` entries preserves every cyclic window of length at
most `d+1`, so (5.1) and the middle row survive.  Equation (4.4) identifies
the longer windows with the upper shadows of `T`; hypothesis 2 supplies a
witness not deleted at the seam for every upper mask.  The monotone-deadline
lower bound gives the reverse inequality.  □

## 6. Exact status of the remaining lower problem

Theorem 5.1 removes the artificial literal-base-row requirement.  Its only
new construction problem is

\[
\boxed{
\text{find }A\in[C,P]
\text{ whose first }d\text{ OR--Pascal rows cover the lower ideal}.}
\tag{6.1}
\]

The total number of available cells is exactly

\[
dW+\binom{d+1}{2}=\Lambda+e,
\]

so the arithmetic is optimal up to the known slack `e`.  A proposed
assignment of lower masks to these cells is realizable exactly when its
coordinate intervals pass the full witness criterion in
`MATH_OPTIMAL_NORMALIZATION_EXCHANGE_20260727.md`.

This is the correct uniform descendant of the `k=11` surplus-Hall compiler:

* `h=1` gives a dense core and a one-row matching;
* `h=d` gives a sparse core and exposes the whole lower band;
* intermediate block sizes give possible recursive compilers.

No existence theorem for (6.1) is claimed here.  The advance is an exact,
dimension-uniform reduction which preserves the successful rotor while no
longer violating base-row capacity.

## 7. Exact `k=11` calibration

The executable compiler is `scratch/sigma_multirow_compiler.py`.

On the certified `k=11` rotor, the depth-three erosion has 1,386 coordinate
incidences.  Its canonical depth-three core has only 858 incidences, with
rank profile

\[
1^{99}2^{330}3^{33}.
\]

The complete multirow SAT instance has only 3,784 variables and 11,913
clauses, and solves locally in about 0.004 seconds.  It produces a third
independent optimal word,

```text
scratch/sigma_multirow_k11_465.word
```

with SHA-256

```text
a7b4395d35658e2860cfa12e6419aef1e528dd7b6ab40833edeeb7dc153ccaf3
```

The exhaustive verifier reports 2,047/2,047 masks and the rows

| row | length | rank profile |
|---|---:|---|
| `D^0` | 465 | `1^11 2^55 3^399` |
| `D^1` | 464 | `3^8 4^456` |
| `D^2` | 463 | `5^463` |
| `D^3` | 462 | `6^462` |

This differs from both previous optimal words.  In particular, it really
uses more than one lower row: eight rank-three masks occur in `D^1`.  That
is the behaviour the uniform compiler must permit.

Reproduction:

```sh
python3 scratch/sigma_multirow_compiler.py \
  scratch/sigma_sat_k11_allcentral_cap2.certificate.json \
  --k 11 --depth 3 \
  --output-word scratch/sigma_multirow_k11_465.word

python3 scratch/sigma_sat_verify_word.py \
  --k 11 scratch/sigma_multirow_k11_465.word
```

## 8. Independent PBBS-rotor calibration

The distance-17 coherent PBBS trade in
`scratch/pbbs_k11_cap2_lowerq2_res3_conn_winner.json` produces a different
resident universal-shadow rotor.  Its exhaustive shadow table is complete
at every depth `q=1,...,5`.  The same multirow compiler gives

```text
scratch/pbbs_k11_res3_conn_multirow_465.word
```

with SHA-256

```text
52d16a4b280601645e1d0265bf6f102c38667285e9c3ebbcadfd6f073b78ef59
```

The compiler has 3,652 variables and 11,583 clauses, solves in about 0.005
seconds, and verifies 2,047/2,047 masks.  Its linear rank profile is

\[
D^0:1^{17}2^{184}3^{264},\qquad
D^1:3^8 4^{456},\qquad
D^2:5^{463},\qquad
D^3:6^{462}.
\]

This establishes that the depth-`d` sandwich is not tuned to the original
SAT rotor: two structurally different central constructions compile through
the same small multirow gate.
