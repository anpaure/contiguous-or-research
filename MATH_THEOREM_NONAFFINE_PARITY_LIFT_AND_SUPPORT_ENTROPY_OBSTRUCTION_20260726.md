# A nonlinear exact parity lift and the support-entropy obstruction

Date: 2026-07-26

## 0. Outcome

The parity complete-mapping equations do not force the affine construction.
Using the two common-phase `Q_4` factors, one can choose the row factor by
an arbitrary Boolean function of two context coordinates.  Taking a
quadratic function gives a literal nonlinear exact `C_16`-factor of `Q_8`.

This extra freedom is nevertheless far too small for the trace problem.
The main theorem below gives a general, ownership-independent obstruction.
At aligned completed-pair depth `d`, put

\[
 N_d(x)=\#\{J_{p,d}(x):p\in Q_r^{\rm even}\},                 \tag{0.1}
\]

the number of different completed direction supports visible from a fixed
coarse start `x` as the parity context varies.  If `D_d` is the number of
distinct aligned lower traces (or upper traces), then

\[
 \boxed{
 D_d\le 2^{r-d}\sum_{x\in Q_r}N_d(x).}                       \tag{0.2}
\]

Consequently an asymptotically injective trace map requires

\[
 \frac1{2^r}\sum_xN_d(x)\ge(1-o(1)),2^{d-1}.                \tag{0.3}
\]

Thus the completed support itself must carry essentially one bit of
context information per erased parity coordinate.  In particular, every
`s`-bit palette ansatz has trace multiplicity at least
`2^(d-s-1)` somewhere and collision excess at least

\[
              2^{2r-1}-2^{2r+s-d}.                            \tag{0.4}
\]

Every bounded-palette construction fails already at `d=floor(sqrt r)`.
More generally, a fixed-order block-local recursion has support entropy
only `O(log r)` at such a depth and therefore has
`2^{sqrt r-O(log r)}`-fold trace fibres.  This closes the entire class of
local recursions which vary only the internal order of bounded packets.

The correct nonlinear target is now sharp: exact ownership must be coupled
to a **rate-one support code**, not merely to nonconstant context dependence.

## 1. The two-sided exactness equations

Let

\[
 E=Q_r^{\rm even},\qquad O=Q_r^{\rm odd}.
\]

For every `p in E`, let

\[
 F_p(x)=x\oplus e_{d_p(x)}.                                   \tag{1.1}
\]

The paired physical lift is exact precisely when both of the following
hold:

1. for every `p`, the map `F_p` is a permutation of `Q_r`;
2. for every `x`, the map
   \[
                 T_x(p)=p\oplus e_{d_p(x)}                    \tag{1.2}
   \]
   bijects `E` and `O`.

Condition 2 can equivalently be written as the pointwise predecessor
identity

\[
 \sum_{i=1}^r {\bf1}\{d_{q\oplus e_i}(x)=i\}=1
 \qquad(q\in O).                                               \tag{1.3}
\]

Thus an exact solution is a two-dimensional array of cube directions:
every row is a neighbour permutation in `x`, and every column is a perfect
matching in `p`.

## 2. A genuinely nonlinear exact `Q_4` solution

Use the common phase colouring `c` and the factors `G_0,G_1` from
`MATH_THEOREM_Q4_COMMON_PHASE_BLOCK_TRANSPOSITION_20260726.md`.
Put `t=c(x) mod 4`.  Their outgoing directions are

\[
\begin{array}{c|cccc}
t&0&1&2&3\\ \hline
\delta_0&1&2&3&4\\
\delta_1&1&4&3&2.
\end{array}                                                    \tag{2.1}
\]

Let `f:F_2^2 -> F_2` be arbitrary, and for even `p` define

\[
 a(p)=f(p_1,p_3),\qquad F_p=G_{a(p)},\qquad
 d_p(x)=\delta_{a(p)}(x).                                     \tag{2.2}
\]

### Theorem 2.1 (nonlinear common-phase solution)

Equations (2.2) satisfy both exactness conditions in Section 1.  Hence
their adjacent-pair expansion is an exact physical `C_16`-factor of
`Q_8`.  Taking, for example,

\[
                              f(u,v)=uv                         \tag{2.3}
\]

gives a quadratic context selector.

#### Proof

For fixed `p`, `F_p` is either `G_0` or `G_1`, hence is an exact `C_8`
factor permutation.

Fix `x`.  At phases `t=0` and `t=2`, equation (2.1) makes `T_x` the fixed
coordinate matchings `p -> p+e_1` and `p -> p+e_3`, respectively.  At
phase `t=1`, fix `(p_1,p_3)`.  The two even contexts in that fibre have
the same value of `a(p)`; if it is zero both toggle coordinate two, and if
it is one both toggle coordinate four.  Either choice bijects those two
even contexts with the two odd contexts having the same `(p_1,p_3)`.
Different fibres are disjoint.  The phase `t=3` has the two coordinate
choices interchanged and the identical argument applies.  Therefore every
`T_x` is a bijection.  The parity lift theorem completes the proof.
\(\square\)

This is not the affine ansatz

\[
                         d_p(x)=\delta_0(Sp\oplus x)            \tag{2.4}
\]

for any coordinate permutation `S`.  Indeed, at every `x` of phase zero,
(2.2) has direction one for all eight even contexts.  In (2.4), however,
`Sp+x` ranges over an eight-element parity coset, while
`delta_0^{-1}(1)` has only four elements.  Thus even exact nonlinear
ownership is easy; trace entropy is the real constraint.

## 3. The support-entropy theorem

For an even context `p`, a coarse start `x`, and a depth `d<=r`, let

\[
 J_{p,d}(x)=\{d_p(x),d_p(F_px),\ldots,
                    d_p(F_p^{d-1}x)\}.                         \tag{3.1}
\]

Assume, as required for a physical isometric cycle, that these `d`
directions are distinct.  An aligned lower or upper physical trace is
equivalent to

\[
 \mathcal C_d(p,x)=
 \bigl(J_{p,d}(x),\ x|_{J_{p,d}(x)^c},\
                    p|_{J_{p,d}(x)^c}\bigr).                  \tag{3.2}
\]

Let `Omega=E x Q_r`, so `|Omega|=2^(2r-1)`, and let `D_d` be the cardinality
of the image of (3.2).

### Theorem 3.1 (rate-one support is necessary)

With `N_d(x)` as in (0.1),

\[
 D_d\le 2^{r-d}\sum_xN_d(x).                                  \tag{3.3}
\]

In particular the collision excess satisfies

\[
 |\Omega|-D_d
 \ge 2^{2r-1}-2^{r-d}\sum_xN_d(x).                            \tag{3.4}
\]

#### Proof

Fix `x`.  Once a support `J` of size `d` is fixed, `x|J^c` is fixed as
well.  The only remaining trace datum which varies with `p` is `p|J^c`,
which has at most `2^(r-d)` possible values.  There are `N_d(x)` possible
supports.  Hence at most `N_d(x)2^(r-d)` traces arise from this `x`.
Summing this upper bound over all `x` can only overcount the global trace
image, proving (3.3); subtracting from `|Omega|` proves (3.4).
\(\square\)

### Corollary 3.2 (support entropy must be rate one)

If the collision excess is `o(2^(2r))`, then

\[
 \frac1{2^r}\sum_xN_d(x)\ge(1-o(1))2^{d-1}.                   \tag{3.5}
\]

Thus `log_2 N_d(x)` must be `d-O(1)` on average.  Merely making the row
order context-dependent is quantitatively irrelevant unless its completed
support distinguishes essentially every erased even context.

### Corollary 3.3 (bounded-key and finite-palette no-go)

Suppose that for every fixed `x`, the map

\[
                         p\longmapsto J_{p,d}(x)               \tag{3.6}
\]

factors through at most `s` Boolean features of `p`.  Equivalently,
`N_d(x)<=2^s`.  Then

\[
 D_d\le2^{2r+s-d},\qquad
 |\Omega|-D_d\ge2^{2r-1}-2^{2r+s-d}.                          \tag{3.7}
\]

There is also a trace of multiplicity at least

\[
                              2^{d-s-1}.                        \tag{3.8}
\]

The same conclusions hold whenever the entire row factor `F_p` is chosen
from a palette of at most `2^s` factors.  These statements do not assume
the features are linear or low degree; arbitrary nonlinear hashes of `p`
are included.

#### Proof

The image bound follows from Theorem 3.1.  For a fixed `x`, the
`2^(r-1)` even contexts are distributed among at most
`2^s 2^(r-d)` possible pairs `(J,p|J^c)`.  Pigeonhole gives (3.8).
If `F_p` lies in a palette of size `2^s`, then its `d`-step support at a
fixed `x` also has at most `2^s` values. \(\square\)

At `d=floor(sqrt r)`, every `s=o(sqrt r)` ansatz therefore has a trace
of multiplicity `2^(sqrt r-o(sqrt r))` and collision excess
`(1-o(1))2^(2r-1)`.  This is uniform over the whole Gaussian window:
for every `d<=sqrt r`, the lower bound is exactly `2^(d-s-1)` whenever
positive.

The nonlinear construction in Section 2 has a two-factor palette, so
`s=1`.  It is ownership-exact but necessarily fails at all growing depths.

## 4. Fixed-order block-local recursions are impossible

The most common local recursion partitions `[r]` into coordinate packets
of size at most `b`, traverses the packets in one fixed cyclic order, and
allows the parity context to choose one of at most `L` internal orders in
each packet.  Permit also a context-dependent cyclic starting position.

### Theorem 4.1 (block-local no-go)

For every such recursion and every fixed coarse start `x`,

\[
                         N_d(x)\le 2rL^2.                       \tag{4.1}
\]

Consequently every aligned depth-`d` trace system has a trace of
multiplicity at least

\[
                         \frac{2^{d-1}}{2rL^2},                 \tag{4.2}
\]

and collision excess at least

\[
 2^{2r-1}-2^{2r-d}(2rL^2).                                    \tag{4.3}
\]

In particular, if `log L=o(sqrt r)`, the construction fails at
`d=floor(sqrt r)` with exponentially large fibres and asymptotically full
collision excess.

#### Proof

A consecutive direction window consists of some whole packets together
with at most two partial boundary packets.  Whole packets contribute their
entire coordinate sets, independent of their internal orders.  After the
cyclic starting position is chosen (at most `2r` choices, including the
half-cycle phase), only the internal states of the two boundary packets can
change the support.  This gives at most `2rL^2` supports.  Apply Corollary
3.3 with `2^s=2rL^2`. \(\square\)

This theorem applies even if the local state choices are nonlinear,
owner-dependent, and arranged so that all complete-mapping equations hold.
It therefore rules out tensoring the `Q_4` braid, or any other bounded
packet palette, while leaving the global packet order fixed.  A viable
recursion must let the context change **which packets enter the window**,
not merely their internal direction order.

## 5. Exact remaining nonlinear target

The two exact gates can now be stated without an affine ansatz.

Construct arrays `d_p(x)` such that

1. every row `x -> x+e_{d_p(x)}` is an isometric `C_(2r)`-factor;
2. every column `p -> p+e_{d_p(x)}` is a perfect matching;
3. for every protected `d<=sqrt r`,
   \[
   \frac1{2^r}\sum_x
       \#\{J_{p,d}(x):p\in E\}
        =(1-o(1))2^{d-1};                                    \tag{5.1}
   \]
4. after the support is fixed, the puncture `p|J^c` has only
   `1+o(1)` average multiplicity.

Condition 3 is the rate-one support requirement forced by Theorem 3.1;
condition 4 is the remaining hash-collision requirement.  The nonlinear
`Q_4` construction proves that conditions 1--2 alone have abundant local
solutions.  Theorems 3.1 and 4.1 prove that conditions 3--4 require a
global, context-dependent packet scheduler.  No bounded-state or
fixed-order local recursion can supply it.

