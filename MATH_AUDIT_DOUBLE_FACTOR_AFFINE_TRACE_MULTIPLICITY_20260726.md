# Audit of the double-factor affine lift: ownership is exact, trace coding fails

Date: 2026-07-26

## 0. Verdict

The affine complete-mapping theorem in
`MATH_THEOREM_DOUBLE_FACTOR_AFFINE_PARITY_COMPLETE_MAPPING_20260726.md`
is correct.  In particular, its `Q_4` specialization really does give an
exact physical `C_16`-factor of `Q_8`, and the coarse successor genuinely
depends on the parity context.

However, this context dependence does **not** reduce the aligned parity
collision from
`MATH_THEOREM_PARITY_COMPLETE_MAPPING_PAIRED_ORDER_LIFT_20260726.md`.
For the affine `Q_4` seed, the exact multiplicities of the aligned
length-`2d` lower traces (and, identically, upper traces) are

\[
\begin{array}{c|cccc}
d&1&2&3&4\\ \hline
\text{number of distinct traces}&128&64&16&1\\
\text{multiplicity of every trace}&1&2&8&128.
\end{array}                                                   \tag{0.1}
\]

Thus at `d=2` the construction exactly attains the old lower bound
`2^(d-1)=2`, while at `d=3,4` it is strictly worse.  Its collision excess
among the `128` even-time starts is respectively

\[
                         0,\quad64,\quad112,\quad127.           \tag{0.2}
\]

Consequently Corollary 2.1 is a valid ownership construction but is not a
positive trace-code seed.  Any recursion based on it must first replace
the affine phase function, rather than merely amplify it.

## 1. Owner-by-owner check of the complete-mapping identity

Put `S=(2 4)`.  For the common-phase factors, group the sixteen vertices
by phase modulo four:

\[
\begin{array}{c|c|c|c}
t&V_t&\delta_0&\delta_1\\ \hline
0&0000,0101,1111,1010&1&1\\
1&1000,1101,0111,0010&2&4\\
2&1100,1001,0011,0110&3&3\\
3&1110,1011,0001,0100&4&2.
\end{array}                                                   \tag{1.1}
\]

Hence `delta_1(y)=S delta_0(y)` at every one of the sixteen owners.
For even `p`, set

\[
 y=Sp\oplus x,\qquad d_p(x)=\delta_0(y).
\]

Then the two identities

\[
 Sp\oplus F_p(x)=G_0(y),\qquad
 S\bigl(p\oplus e_{d_p(x)}\bigr)\oplus x=G_1(y)               \tag{1.2}
\]

prove, respectively, that every `F_p` is a neighbour permutation and
that `p -> p+e_{d_p(x)}` bijects the even and odd shores for every `x`.
This verifies the abstract parity-lift hypothesis without any phase or
owner mismatch.

## 2. Exact aligned code

For an even-time start `(p,x)`, the change of variables

\[
                              y=Sp\oplus x                     \tag{2.1}
\]

is a bijection between `E x Q_4` and itself.  Along the associated coarse
cycle, `y` advances under `G_0`; therefore the completed direction set for
`d<=4` depends only on the phase class `t` of `y`:

\[
 J_{t,d}=\{t+1,t+2,\ldots,t+d\}\pmod4.                         \tag{2.2}
\]

Writing `K=[4]\setminus J_{t,d}`, the aligned signed trace is exactly

\[
 \left(J_{t,d},\ x|_K,\ p|_K\right)
 =\left(J_{t,d},\ (Sp\oplus y)|_K,\ p|_K\right).              \tag{2.3}
\]

There is no omitted order datum: a lower trace is empty on both physical
coordinates of each completed pair and records the two unchanged bits on
each pair in `K`; an upper trace is full on each completed pair and records
the same unchanged bits on `K`.  Thus (2.3) counts the actual physical
traces, not merely a coarser necessary code.

## 3. Fibre count

For fixed `t`, output `(u,v)=(x|_K,p|_K)`, and `y in V_t`, equations
(2.1)--(2.3) say

\[
 p|_K=v,\qquad p_{S k}=u_k\oplus y_k\quad(k\in K),             \tag{3.1}
\]

with the single additional condition that `p` has even parity.

### `d=1`

Here `|K|=3`.  If the omitted coordinate is fixed by `S`, then `K` is
`S`-invariant; otherwise `K union SK=[4]`.  In both cases (3.1), even
parity, and the displayed phase fibre determine `p` and `y` uniquely.
The relevant three-coordinate punctures of every `V_t` in (1.1) are
injective.  Hence all `128` starts give distinct traces.

### `d=2`

Here `K` and `SK` are two-sets meeting in exactly one coordinate.  The
overlap equation fixes one coordinate of `y`.  In every `V_t`, exactly two
vertices have either value of that coordinate.  For each such `y`, the
union `K union SK` fixes three coordinates of `p`, and even parity fixes
the fourth.  Hence every trace has multiplicity exactly two.  There are
four possible `J` and sixteen traces for each, giving `64` traces.

### `d=3`

Now `K={k}`.  If `S(k)=k`, fixing `(x_k,p_k)` fixes `y_k`; exactly two
members of `V_t` have that value, and each permits four even contexts.
If `S(k)ne k`, each of the four choices of `y` fixes `p_{S(k)}`, after
which two even contexts remain.  Either way every trace has multiplicity
eight.  There are four possible `J` and four traces for each, giving
sixteen traces.

### `d=4`

Here `J=[4]` and `K` is empty.  Formula (2.3) is constant on all
`8*16=128` starts.  The lower trace is the empty physical set and the
upper trace is all eight physical coordinates.

This proves (0.1)--(0.2).

## 4. Correct boundary for the affine construction

The affine double-factor identity solves exactly three things:

1. whole-owner exactness;
2. context-dependent coarse successors;
3. adjacent physical pair clustering.

It does not solve even the finite aligned trace-code gate.  The obstruction
is visible already at `d=2`, before any recursion or outer-packet coupling:
the completed direction set carries too little information about the
erased parity coordinates.  A successful double-factor seed needs a phase
partition whose punctured fibres shrink approximately like `2^{-d}`;
the four fibres in (1.1) instead have puncture fibres of sizes
`1,2,2,4` in the relevant affine equations, producing (0.1).

## 5. General residual ambiguity of a coordinate-affine seed

There is a seed-independent linear reason that the construction can retain
parity ambiguity.  Keep the affine ansatz

\[
                         y=Sp\oplus x
\]

for an arbitrary coordinate permutation `S`, and fix `y` and its completed
direction set `J`; put `K=[r]\setminus J`.  The aligned trace knows
`p|_K` and `(Sp)|_K=x|_K+y|_K`.  Hence it knows `p` precisely on

\[
                         K\cup S^{-1}K.
\]

Its unobserved context coordinates are therefore

\[
 A=[r]\setminus(K\cup S^{-1}K)=J\cap S^{-1}J.                 \tag{5.1}
\]

Holding `y` fixed, two even contexts give the same trace exactly when
their difference is an even-weight vector supported on `A`.  Thus the
fixed-`y` fibre has size

\[
 \begin{cases}
 1,&|A|=0,\\
 2^{|A|-1},&|A|\ge1.
 \end{cases}                                                  \tag{5.2}
\]

Additional collisions can then come from distinct `y` in one phase fibre,
as they do in (0.1).  Formula (5.2) is a useful design test for any proposed
affine recursion: it must make `J` nearly disjoint from `S^{-1}J` at every
protected depth *and* make the relevant punctures of its phase fibres
nearly injective.  The `Q_4` transposition seed satisfies neither condition
past depth two.
