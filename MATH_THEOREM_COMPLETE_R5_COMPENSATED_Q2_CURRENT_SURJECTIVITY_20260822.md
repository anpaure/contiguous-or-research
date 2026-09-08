# The complete `r=5` compensated kernel realizes every balanced depth-two current

**Date:** 2026-08-22

**Status:** exact finite theorem with a streaming integral exposure
calculation and a bit-sliced modular-rank certificate. It extends the
complete-`r=4` phenomenon to the first depth-two layer containing two
nontrivial Specht components. It is not an all-`r` or stopped-residual
theorem.

## 1. The three maps

Put `Omega=[11]`. For a word `w=(w_0,...,w_10)`, with subscripts read
modulo eleven, define

\[
 E(w)=\{(M,I_5^w(s)):1\le s\le10\}
 \mathbin{\dot\cup}
 \{(L,I_4^w(s)):1\le s\le10\},                    \tag{1.1}
\]

where `I_k^w(s)={w_s,...,w_(s+k-1)}`. Let

\[
 \mathcal C=\{E(w):w\in S_{11}\},\qquad
 \mathcal V={\Omega\choose5}\mathbin{\dot\cup}{\Omega\choose4}.
                                                               \tag{1.2}
\]

The catalogue has `11!` labelled columns. Indeed, with
`L_s=I_4^w(s)` and `M_s=I_5^w(s)`, the tagged containment graph is the
intrinsically oriented path

\[
 L_1-M_1-L_2-M_2-\cdots-L_{10}-M_{10}.
\]

The differences `M_s-L_s={w_(s+4)}` recover ten word positions, and the
unique unused label recovers position four.

Define the central incidence and unnormalised rooted duplicate exposure by

\[
 A_{vG}=\mathbf1_{\{v\in G\}},\qquad
 \widetilde P_{vG}
 =\sum_{\substack{F\in\mathcal C\\v\in F}}
       (|F\cap G|-1)_+.                            \tag{1.3}
\]

All complete-catalogue target degrees are positive. Dividing every row of
`\widetilde P` by its target degree therefore changes neither its row space
nor its kernel; this gives the normalized exposure matrix `P` used by the
compensated-rate theorem.

Every `G=E(w)` remembers its unique word. For `k in {2,3,4}`, define the
full cyclic rank-`k` incidence

\[
 Q^{(k)}_{XG}=\mathbf1\{X=I_k^w(s)\text{ for some }
             s\in\mathbb Z_{11}\},
 \qquad X\in{\Omega\choose k}.                    \tag{1.4}
\]

The primary depth-two operator is `Q=Q^(3)`.

and stack

\[
                              B=\begin{bmatrix}A\\\widetilde P\end{bmatrix}.
                                                               \tag{1.5}
\]

Thus `A` and `\widetilde P` each have

\[
 {11\choose5}+{11\choose4}=462+330=792
\]

rows, while `Q` has `{11\choose3}=165` rows.

## 2. Exact rational ranks

### Theorem 2.1

Over the rationals,

\[
 \boxed{
 \operatorname {rank}B=1581,\qquad
 \operatorname {rank}Q=155,\qquad
 \operatorname {rank}\!\begin{bmatrix}B\\Q\end{bmatrix}=1735.}
                                                               \tag{2.1}
\]

#### Rational upper bounds

Every configuration has ten targets on each central shore, so

\[
 \sum_{v\in{\Omega\choose5}}A_{vG}
 =\sum_{v\in{\Omega\choose4}}A_{vG}=10.            \tag{2.2}
\]

Put

\[
 D_0=\sum_{F\in\mathcal C}(|F\cap G|-1)_+.
\]

Coordinate transitivity makes `D_0` independent of `G`, and it is positive.
Swapping the sums in (1.3) gives

\[
 \sum_{v\in{\Omega\choose5}}\widetilde P_{vG}
 =\sum_{v\in{\Omega\choose4}}\widetilde P_{vG}
 =10D_0.                                          \tag{2.3}
\]

The shore difference in (2.2), the shore difference in (2.3), and

\[
 \sum_{v\in{\Omega\choose5}}\widetilde P_{vG}
 =D_0\sum_{v\in{\Omega\choose5}}A_{vG}             \tag{2.4}
\]

are three independent row relations. Since `B` has 1584 rows,

\[
                              \operatorname {rank}B\le1581.   \tag{2.5}
\]

Every `Q`-column is the set of eleven cyclic triples of a Hamilton order,
and every coordinate occurs in exactly three of them. Hence the ten
differences among its eleven coordinate-degree row sums are row relations.
They are independent: if real numbers `c_a` satisfy
`c_a+c_b+c_c=0` for every triple, swapping one coordinate between two
triples shows that all `c_a` are equal, and then `3c_a=0`. Thus the
vertex--triple incidence matrix has rank eleven and

\[
                              \operatorname {rank}Q\le165-10=155.       \tag{2.6}
\]

Finally, the constant column function belongs to both row spaces:
`sum_X Q_(XG)=11`, whereas the first sum in (2.2) is ten. Therefore

\[
 \operatorname {rank}\!\begin{bmatrix}B\\Q\end{bmatrix}
 \le1581+155-1=1735.                               \tag{2.7}
\]

#### Matching modular lower bounds

Use the prime field `F_3`. Take the base word `(0,1,...,10)` and compute
its exposure column (1.3) by a literal streaming enumeration of all

\[
                              11!=39,916,800
\]

words `F`. The resulting exact checks are

\[
 D_0=9,913,785,\qquad
 \sum_{v\in{\Omega\choose5}}\widetilde P_{v,E(1)}
 =99,137,850.                                      \tag{2.8}
\]

The middle and lower exposure sums agree, as required by (2.3).

Relabel this base column by 4000 deterministic coordinate permutations.
For `0<=t<4000`, take the permutation of Lehmer rank

\[
                         j_t=7919t\pmod {11!}.      \tag{2.9}
\]

Since `gcd(7919,11!)=1`, these relabellings are distinct. Exact Gaussian
elimination over `F_3` on the restricted columns gives

\[
 \operatorname {rank}_{\mathbb F_3}B=1581,\qquad
 \operatorname {rank}_{\mathbb F_3}Q=155,\qquad
 \operatorname {rank}_{\mathbb F_3}
       \begin{bmatrix}B\\Q\end{bmatrix}=1735.      \tag{2.10}
\]

The accompanying checker streams the `11!` configurations in eleven
disjoint first-letter classes. Its ternary Gaussian elimination stores
each row in two bit planes; an independent scalar elimination tests that
rank engine on every matrix size through `12 by 15` before the certificate
is evaluated. It also records the deterministic exposure checksums

\[
 408475218,\qquad915177100\pmod {1,000,000,007}.    \tag{2.11}
\]

A nonzero minor modulo three is a nonzero integer minor. Thus (2.10)
gives rational lower bounds matching (2.5)--(2.7), proving (2.1).
`square`

### Theorem 2.2 (the adjacent tested shallow ranks)

Over the rationals,

\[
\begin{array}{c|c|c}
k&\operatorname {rank}Q^{(k)}&
\operatorname {rank}\!\begin{bmatrix}B\\Q^{(k)}\end{bmatrix}\\ \hline
2&45&1625\\
4&320&1900
\end{array}                                                   \tag{2.12}
\]

#### Proof

For any `1<=k<=10`, every full cyclic rank-`k` column contains eleven
targets and every coordinate belongs to exactly `k` of them.  The ten
differences among the eleven coordinate-degree row sums are therefore row
relations.  They are independent over the rationals: if

\[
                         \sum_{a\in X}c_a=0          \tag{2.13}
\]

for every `k`-set `X`, comparing two sets that differ only by replacing
`a` with `b` shows `c_a=c_b`; then (2.13) gives `kc_a=0`.  Thus the
vertex--`k`-set incidence matrix has rank eleven, and

\[
              \operatorname {rank}Q^{(k)}
                   \le {11\choose k}-10.            \tag{2.14}
\]

The constant column function belongs to both `row(B)` and
`row(Q^(k))`, by (2.2) and `sum_X Q^(k)_(XG)=11`.  Combining (2.5) and
(2.14) gives

\[
 \operatorname {rank}\!\begin{bmatrix}B\\Q^{(k)}\end{bmatrix}
 \le1581+{11\choose k}-11.                          \tag{2.15}
\]

On the same deterministic orbit columns used above, exact elimination
over `F_3` gives

\[
\begin{array}{c|c|c}
k&\operatorname {rank}_{\mathbb F_3}Q^{(k)}&
\operatorname {rank}_{\mathbb F_3}
 \!\begin{bmatrix}B\\Q^{(k)}\end{bmatrix}\\ \hline
2&45&1625\\
4&320&1900.
\end{array}                                                   \tag{2.16}
\]

These are exactly the rational upper bounds (2.14)--(2.15).  Nonzero
minors modulo three again give the matching rational lower bounds.
`square`

## 3. Surjectivity onto balanced shallow currents

For `k in {2,3,4}`, let

\[
 \mathcal Z_k=\left\{j\in\mathbb R^{\binom{11}k}:
       \sum_{X\ni a}j_X=0\text{ for every }a\in\Omega\right\}.           \tag{3.1}
\]

The vertex--`k`-set incidence matrix has rank eleven by the argument above,
so, for the three tested ranks,

\[
 \dim\mathcal Z_2=44,\qquad
 \dim\mathcal Z_3=154,\qquad
 \dim\mathcal Z_4=319.                              \tag{3.2}
\]

### Corollary 3.1

\[
                              \boxed{Q(\ker B)=\mathcal Z_3.} \tag{3.3}
\]

Consequently every rational balanced triple current has a rational signed
configuration vector `eta` satisfying

\[
                              A\eta=0,\qquad P\eta=0,\qquad Q\eta=j.
                                                               \tag{3.4}
\]

#### Proof

The rank identity gives

\[
 \dim Q(\ker B)
 =\operatorname {rank}\!\begin{bmatrix}B\\Q\end{bmatrix}
  -\operatorname {rank}B=1735-1581=154.            \tag{3.5}
\]

If `eta in ker B`, summing either central-shore incidence equation gives
`sum_G eta_G=0`. Every cyclic-triple column has coordinate degree three,
and hence

\[
                     \sum_{X\ni a}(Q\eta)_X=3\sum_G\eta_G=0. \tag{3.6}
\]

Thus `Q(ker B) subseteq Z_3`; equality follows from (3.2)--(3.5).
Rational row reduction supplies a rational preimage of every rational
current. `square`

### Corollary 3.2

The same conclusion holds at the two adjacent tested ranks:

\[
 \boxed{Q^{(2)}(\ker B)=\mathcal Z_2,\qquad
        Q^{(4)}(\ker B)=\mathcal Z_4.}              \tag{3.8}
\]

#### Proof

Theorem 2.2 gives image dimensions `1625-1581=44` and
`1900-1581=319`.  If `eta in ker B`, summing either central incidence
shore again gives `sum_G eta_G=0`; hence, for every coordinate `a`,

\[
 \sum_{X\ni a}(Q^{(k)}\eta)_X
      =k\sum_G\eta_G=0.                            \tag{3.9}
\]

Thus each image is contained in the corresponding space in (3.2), and
the dimensions force equality. `square`

For the positive uniform law `lambda_G^0=1/11!`, every finite signed
solution admits some sufficiently small real amplitude `epsilon>0` for
which

\[
                         \lambda^0+\epsilon\eta\ge0.           \tag{3.7}
\]

This is fixed-dimensional feasibility only. Neither (2.1) nor (3.3)
bounds `epsilon`, the Fisher-normalized right inverse, or the coordinate
ratio `max_G|eta_G|/lambda_G^0`.

## 4. Representation-theoretic meaning and scope

The multiplicity-free decomposition of the permutation module on
`k`-sets is

\[
 \mathbb R^{\binom{11}k}
   \cong\bigoplus_{j=0}^{k}V_{(11-j,j)}\qquad(k\le5).           \tag{4.1}
\]

For completeness, map a `j`-set to the sum of the `k`-sets containing it.
The nested images give successive quotients of dimensions
`binom(11,j)-binom(11,j-1)`; the standard polytabloid differences identify
the quotient with the two-row irreducible `V_(11-j,j)`.  The coordinate-
degree map is nonzero precisely on the first two summands.  Consequently

\[
\begin{aligned}
 \mathcal Z_2&\cong V_{(9,2)},&&44,\\
 \mathcal Z_3&\cong V_{(9,2)}\oplus V_{(8,3)},&&44+110=154,\\
 \mathcal Z_4&\cong V_{(9,2)}\oplus V_{(8,3)}\oplus V_{(7,4)},
   &&44+110+165=319.
\end{aligned}                                                   \tag{4.2}
\]

Thus the complete-catalogue Gram Schur complement is genuinely positive
on every nontrivial module occurring at each of the tested ranks
`k=2,3,4`.  In particular it is positive on both depth-two modules at
`k=3`.  Together with `r=4`, this is evidence for the all-`r` qualitative
Gram conjecture, not a proof of it.

The exact asymptotic inputs remain:

1. Fisher-normalized lower bounds for the relevant constrained singular
   values through the required depth band;
2. a coordinatewise-delocalized simultaneous right inverse;
3. stability of the analogous current restricted operators after the
   stopped residual loses symmetric-group invariance; and
4. accumulation and terminal-hole alignment of
   `Omega(log(1/x))` exact protection gain.

## 5. Checker

Compile and run

```text
clang++ -std=c++20 -O3 -march=native -pthread \
  scratch/verify_complete_r5_compensated_q2_surjectivity_20260822.cpp \
  -o /tmp/verify_complete_r5_compensated_q2_surjectivity_20260822
/tmp/verify_complete_r5_compensated_q2_surjectivity_20260822
```

The checker uses no external data files and performs only exact integer and
finite-field arithmetic.
