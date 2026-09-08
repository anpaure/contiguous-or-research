# Audit of growing-band lossless queue packing

## Verdict

The theorem is valid after correcting three reciprocal typographical errors
in the submitted derivation.  Assume `d>=1`, let the atom length parameter be
`L>=2`, and let

\[
K=(2d+1)L,
\qquad d/L\to0,
\qquad K\log K=o(\log m).
\]

Then a simple `K`-uniform atom hypergraph has a matching with zero duplicate
ledger and only

\[
O\!\left(
 K^2\left(\frac{L\log m}{m}\right)^{1/(K-1)}W
\right)=o(W)
\]

uncovered band masks.  Concatenating its literal atom words and appending
the missing masks gives length

\[
W+(2d/L)W+o(W)=(1+o(1))W.
\]

This proves every depth

\[
d=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right)
\]

by taking `L=floor(sqrt(log m/log log m))`.

The condition `d>=1` is needed by the stated exact quotient: for `d=0` the
rank-`m-d+1` orientation marker is absent and reversal can double the
representation multiplicity.  This does not affect any growing-depth
application.

## 1. Literal atom

For an injection

\[
a_0,\ldots,a_{m+d+L-2}
\]

define

\[
C_t=\{a_{2d+t},\ldots,a_{m+d+t-1}\},\qquad 0\le t<L,
\]

and emit the `2d` singletons `a_0,...,a_(2d-1)` followed by
`C_0,...,C_(L-1)`.  The suffix of length `d+q+1` ending at `C_t` is exactly

\[
S_{t,q}=\{a_{d+t-q},\ldots,a_{m+d+t-1}\},
\qquad -d\le q\le d.
\]

Thus one word of length `L+2d` exposes `L` distinct masks in every band
rank.  Distinctness follows from cardinality across `q` and shifted
equal-length intervals across `t`.

## 2. Exact quotient

Put

\[
s=m+d+L-1,
\qquad r=m-d-L+1,
\qquad s+r=2m.
\]

The lowest-rank masks `C_t` recover an oriented Johnson path.  Adjacency
recovers the path up to reversal; the rank-`m-d+1` masks distinguish
`C_(L-1)` as the unique endpoint lying in only one such mask.  Higher ranks
then recover every `t` label.  The successive differences recover

\[
a_0,\ldots,a_{2d+L-2},
\]

and the core transitions recover

\[
a_{m+d},\ldots,a_{m+d+L-2}.
\]

Only the order of the common core

\[
\{a_{2d+L-1},\ldots,a_{m+d-1}\}
\]

is invisible.  It has size `r`, so every simple atom edge has exactly `r!`
injection representations.  Since the number of length-`s` injections is
`(2m)!/r!`, the number of distinct atom edges is

\[
|E|=\frac{(2m)!}{(r!)^2}.
\]

## 3. Degrees and the reciprocal corrections

Let

\[
N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\]

A rank-`m+q` vertex has degree

\[
D_q=\frac{|E|L}{N_{|q|}},
\]

and the maximum is `Delta=|E|L/N_d`.  Hence

\[
\frac{D_q}{\Delta}=\frac{N_d}{N_{|q|}}.
\tag{3.1}
\]

The correct shallow-rank product is

\[
\frac{N_d}{W}
=\prod_{i=0}^{d-1}\frac{m-i}{m+i+1}
\ge1-d^2/m.
\tag{3.2}
\]

Equations (3.1)--(3.2) give

\[
(1-d^2/m)\Delta\le D_q\le\Delta.
\]

The submitted text accidentally wrote the reciprocals in the product and
in the sampled expected-degree formula.  Its final degree interval is the
one above and is correct.

Likewise, the middle degree is

\[
D_0=L\frac{|E|}{W}
=L\left(\frac{m!}{r!}\right)^2,
\tag{3.3}
\]

not `L(r!/m!)^2`.  The subsequent lower bound
`D_0>=L(m/2)^(2L)>>m^4` uses the correct form (3.3).

## 4. Pair codegree

A slot `(t,q)` corresponds to a position interval

\[
J_{t,q}=[d+t-q,m+d+t-1].
\]

For two slots, put

\[
a=|J_\alpha\setminus J_\beta|,
\qquad b=|J_\beta\setminus J_\alpha|.
\]

Conditioned on one slot mapping to a prescribed rank-`m+q` mask, a second
compatible prescribed mask has conditional probability

\[
\left[
\binom{m+q}{a}\binom{m-q}{b}
\right]^{-1}.
\]

Distinct slots have `a+b>0`, and every positive parameter is between one
and the relevant top minus one.  Therefore the denominator is at least
`m-d`.  There are `L^2` ordered slot pairs at fixed ranks.  Counting in the
injection multiset and dividing by the exact `r!` representation
multiplicity yields

\[
\Delta_2/\Delta\le L/(m-d).
\tag{4.1}
\]

## 5. Sparsification and ABKV matching

Retain every simple atom edge independently with probability

\[
p=m^4/\Delta.
\]

This is below one by (3.3).  All expected degrees lie in

\[
[(1-d^2/m)m^4,m^4],
\]

and expected pair codegrees are at most `m^4L/(m-d)`.  Chernoff bounds and
union bounds over `exp(O(m))` vertices and pairs give a deterministic simple
hypergraph with degree error `m^(-2/5)m^4` and maximum codegree at most

\[
C=2m^4L/(m-d).
\]

The near-regular ABKV matching theorem applies.  The relative degree spread
is smaller than

\[
(C\log D/D)^{1/3}=\Theta((L\log m/m)^{1/3}),
\]

and

\[
e^{2K}C\log D/D=o(1)
\]

because `K log K=o(log m)` implies `K=o(log m)` and `L<=K`.  Its matching
leaves at most

\[
O\!\left(
K^2(L\log m/m)^{1/(K-1)}W
\right)
\]

vertices uncovered.  The logarithm of the multiplier is

\[
2\log K-(1-o(1))\frac{\log m}{K}\to-\infty,
\]

exactly by `K log K=o(log m)`.

## 6. Exact ledger and scope

If the matching has `J` edges, it covers exactly `JL` distinct masks in
every band rank.  Therefore

\[
M_0=W-JL,
\qquad M_q^-=M_q^+=N_q-JL,
\]

all duplicate terms vanish, and their sum is exactly the number of
uncovered hypergraph vertices.  The word length is at most

\[
J(L+2d)+U\le W+(2d/L)W+U.
\]

For the explicit corollary, take

\[
L=\left\lfloor\sqrt{\frac{\log m}{\log\log m}}\right\rfloor.
\]

Then every `d=o(L)` satisfies all hypotheses.  A concrete choice is

\[
d=\left\lfloor\frac{\sqrt{\log m}}{\log\log m}\right\rfloor,
\]

for which `2d/L=O(1/sqrt(log log m))` and
`K~2log(m)/(log log m)^(3/2)`.

The theorem has the same exponent ceiling as the earlier quantitative
profile-queue rounding, but gives a cleaner simple orbit, exact equal
occupancy in every band rank, and no dummy vertices.
