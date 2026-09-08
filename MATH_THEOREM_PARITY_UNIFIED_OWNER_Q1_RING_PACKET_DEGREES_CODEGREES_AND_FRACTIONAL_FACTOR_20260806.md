# Parity-unified owner/q1 ring packets: exact degrees, codegrees, and fractional factor

## Status

This note closes the fractional owner-plus-immediate-lower factor gate for
both parities of the trace depth.  One parity-unified ring packet contains
the same number of rank-`r` owners and rank-`(r-1)` q1 roots.  The packet
hypergraph is exactly regular on both shores, its maximum normalized pair
codegree is exactly `2/r`, and uniform packet weight gives a fractional
perfect factor.

The result is fractional.  It does not round the packets to an owner/root
perfect matching, connect their state components, or assign the deeper named
targets.

## 1. Unified packet

Put

\[
 n=2r-1,\qquad D=d+1,                                      \tag{1.1}
\]

and let `L` be the least even integer strictly larger than `D`.  Write

\[
 a=L-D\in\{1,2\},\qquad c=r-D.                              \tag{1.2}
\]

Thus `a=1` when `d` is even and `a=2` when `d` is odd.  Assume `d>=2` and
`c>=0`.

A packet consists of

\[
 K\subset H\subset[n],\qquad |K|=c,\quad |H|=r+a,           \tag{1.3}
\]

together with an unoriented cyclic order of

\[
                         F=H-K,\qquad |F|=L.                \tag{1.4}
\]

For cyclic intervals `I_b(t)` of length `b` in `F`, the packet resources
are

\[
 \begin{aligned}
 O_t&=H-I_a(t),       &&t\in\mathbb Z_L,\\
 Q_t&=H-I_{a+1}(t),   &&t\in\mathbb Z_L.
 \end{aligned}                                             \tag{1.5}
\]

There are `L` distinct rank-`r` owners and `L` distinct rank-`(r-1)` roots.

### Proposition 1.1 (literal ring realization)

The source word

\[
                         A_t=K\cup\{f_t\}                   \tag{1.6}
\]

is a state-balanced depth-`d` all-high ring.  Its length-`D` owner windows
and intersections of consecutive owners are exactly (1.5).

#### Proof

A length-`D` source window contains `K` and `D` consecutive labels of the
`L=D+a` private labels, hence omits the complementary cyclic `a`-interval.
Two consecutive such owners omit two shifted `a`-intervals whose union is
one cyclic `(a+1)`-interval, giving the root formula.  Since `L` is even,
the even-start two-step macros form a balanced cyclic state component.
`square`

## 2. Exact degree on both shores

Let

\[
 \mathcal O=\binom{[n]}r,qquad
 \mathcal Q=\binom{[n]}{r-1},qquad
 W=|\mathcal O|=|\mathcal Q|.                              \tag{2.1}
\]

Regard every packet as one `2L`-element hyperedge on the disjoint resource
shore `mathcal O dotcup mathcal Q`.

### Theorem 2.1 (exact biregularity)

Every owner has packet degree

\[
 D_O
   =\binom{r-1}{a}\binom rD\,{a!D!\over2},                 \tag{2.2}
\]

and every q1 root has packet degree

\[
 D_Q
   =\binom r{a+1}\binom{r-1}{D-1}
        \,{(a+1)!(D-1)!\over2}.                            \tag{2.3}
\]

These numbers are equal.  Denote their common value by `D_0`.

#### Proof

Fix an owner `O`.  Choose the omitted `a` labels

\[
                         H-O\subset[n]-O                    \tag{2.4}
\]

in `binom(r-1,a)` ways, and choose `K subset O` in
`binom(r,c)=binom(r,D)` ways.  To count cyclic orders in which the fixed
`a`-set is an interval, contract it to one block.  There are `D+1` cyclic
objects, `D!` oriented cyclic orders, and `a!` internal orders.  Quotienting
by reversal gives (2.2).

For a root `Q`, choose `H-Q`, an `(a+1)`-set in an `r`-set, and choose
`K subset Q`.  Contracting the fixed `(a+1)`-interval leaves `D` cyclic
objects.  This gives (2.3).

Finally,

\[
 {\binom{r-1}{a}a!\binom rD D!
  \over
  \binom r{a+1}(a+1)!\binom{r-1}{D-1}(D-1)!}=1,             \tag{2.5}
\]

because each of the two missing ratios is `r`. `square`

### Corollary 2.2 (packet count and fractional perfect factor)

The number of packets is

\[
 |\mathcal P|
   =\binom{2r-1}{r+a}\binom{r+a}c{(L-1)!\over2}
   ={WD_0\over L}.                                         \tag{2.6}
\]

Giving every packet weight `1/D_0` covers every owner and every q1 root
with total weight one.  Hence the combined `2L`-uniform packet hypergraph
has an exact fractional perfect matching.

## 3. The incident cross-codegree

### Theorem 3.1 (exact incidence codegree)

For every incident pair `Q subset O`,

\[
 d(O,Q)
  =\binom{r-1}{a}\binom{r-1}{D-1}a!(D-1)!,                 \tag{3.1}
\]

and consequently

\[
 \boxed{
                         {d(O,Q)\over D_0}={2\over r}.}      \tag{3.2}
\]

#### Proof

Write `O=Q union {x}`.  Choose the `a` labels `A=H-O` and choose
`K subset Q`, giving the two binomial factors in (3.1).  In the cyclic
order, `A` must be an `a`-interval and `A union {x}` an `(a+1)`-interval.
Thus `x` is attached to one of the two ends of the ordered `A`-block.
There are `2a!` internal oriented orders.  After contraction there are `D`
cyclic objects, hence `(D-1)!` oriented cyclic orders; quotienting by
reversal cancels the factor two.  This proves (3.1).

Divide by (2.2) and use

\[
 {\binom{r-1}{D-1}\over\binom rD}={D\over r}               \tag{3.3}
\]

to obtain (3.2). `square`

## 4. Complete pair-codegree table

For two owners put `s=|O-O'|`.  For two roots put `s=|Q-Q'|`.  For an
owner/root pair put `j=|O-Q|`.  Unlisted cases have codegree zero.  As usual,
binomial coefficients with an inadmissible lower index are zero.

### Theorem 4.1 (the `a=1` table)

When `a=1`, the nonzero codegrees of distinct resources are

\[
\begin{array}{c|c|c}
\text{pair type}&\text{separation}&\text{codegree}\\ \hline
O,O'&s=1&\binom{r-1}{D-1}D!/2\\
Q,Q'&s=1&(r-1)\binom{r-2}{D-2}(D-2)!\\
Q,Q'&s=2&2\binom{r-3}{D-3}(D-2)!\\
O,Q&j=1&(r-1)\binom{r-1}{D-1}(D-1)!\\
O,Q&j=2&\binom{r-2}{D-2}(D-1)!.
\end{array}                                                 \tag{4.1}
\]

### Theorem 4.2 (the `a=2` table)

When `a=2`, the nonzero codegrees are

\[
\begin{array}{c|c|c}
\text{pair type}&\text{separation}&\text{codegree}\\ \hline
O,O'&s=1&(r-2)\binom{r-1}{D-1}(D-1)!\\
O,O'&s=2&2\binom{r-2}{D-2}(D-1)!\\
Q,Q'&s=1&2\binom{r-1}{2}\binom{r-2}{D-2}(D-2)!\\
Q,Q'&s=2&4(r-2)\binom{r-3}{D-3}(D-3)!\\
Q,Q'&s=3&18\binom{r-4}{D-4}(D-3)!\\
O,Q&j=1&2\binom{r-1}{2}\binom{r-1}{D-1}(D-1)!\\
O,Q&j=2&2(r-2)\binom{r-2}{D-2}(D-2)!\\
O,Q&j=3&6\binom{r-3}{D-3}(D-2)!.
\end{array}                                                 \tag{4.2}
\]

#### Proof of the tables

Once two resources are fixed, first choose the extra labels needed to
complete their union to `H`, then choose `K` inside their intersection.  The
remaining factor is the number of unoriented cyclic orders in which the two
fixed omitted sets are intervals.

For (4.1), the required interval pairs are respectively: two singletons;
two 2-intervals sharing one label; two disjoint 2-intervals; a singleton
nested at an end of a 2-interval; and a disjoint singleton/2-interval pair.
Contracting the intervals gives the five displayed factorial factors.

For (4.2), owner intervals have length two and root intervals length three.
Two 3-intervals with overlap sizes two, one, zero have respectively

\[
                    2(D-2)!,\qquad4(D-3)!,\qquad18(D-3)!   \tag{4.3}
\]

unoriented cyclic orders.  For overlap two the four involved labels form
one path; for overlap one the five involved labels form one path with the
shared label internal; for overlap zero contract two independently ordered
3-blocks.  The mixed interval counts at `j=1,2,3` are

\[
                    2(D-1)!,\qquad2(D-2)!,\qquad6(D-2)!.   \tag{4.4}
\]

Multiplying these factors by the choices of `H` and `K` gives (4.2).
The owner-owner rows are the analogous two-edge path and disjoint-edge
counts. `square`

### Corollary 4.3 (sharp maximum codegree)

For both `a=1` and `a=2`,

\[
 \boxed{
        \Delta_2={2D_0\over r},\qquad
        {\Delta_2\over D_0}={2\over r}.}                    \tag{4.5}
\]

Equality is attained exactly by incident cross-shore pairs `Q subset O`
(apart from vacuous small-parameter coincidences).

#### Proof

The incident row is (3.2).  Dividing every other entry in (4.1)--(4.2) by
`D_0` and cancelling adjacent binomial factors gives a strict smaller value.
For example, the largest same-shore ratios are

\[
 {D\over r(r-1)}\quad(a=1, O-O'),
 \qquad
 {2\over r(r-1)}\quad(a=2, O-O'\text{ or }Q-Q'),          \tag{4.6}
\]

and the nonincident mixed rows are smaller by at least one further factor
of order `1/r`.  Since `D<=r` and `r>=3`, all are at most `2/r`; direct
inspection covers equality-boundary cases. `square`

## 5. What the theorem changes

Owners and q1 roots no longer need to be constructed in two stages.  The
single packet hypergraph already correlates them, is exactly balanced on the
two equal shores, has no fractional separator, and has normalized maximum
codegree tending to zero:

\[
                              {\Delta_2\over D_0}={2\over r}. \tag{5.1}
\]

The precise remaining integral statement is:

> **Parity-unified ring-factor theorem.**  Round the uniform fractional
> packet factor to a matching covering all but a bounded structured leave
> on both shores, while retaining a prescribed bounded packet bank.

After that rounding one must still choose pull decorations and a connected
serialization which cover the deeper named targets.  Those requirements are
not consequences of the degree/codegree ledger alone, especially because
the packet uniformity `2L=Theta(sqrt(r))` grows.

## 6. The actual within-packet collision mass tends to zero

Multiplying the maximum codegree `2/r` by all `Theta(L^2)` resource pairs
is far too pessimistic.  Only `2L` pairs in a packet attain that maximum.

For a packet `P`, define its normalized pair-collision mass

\[
 \Xi(P)={1\over D_0}
          \sum_{\{X,Y\}\in\binom P2}d(X,Y).                 \tag{6.1}
\]

By transitivity, this number is independent of `P`; write it as `Xi_a`.

### Theorem 6.1 (exact collision mass, `a=1`)

When `a=1` and `L=D+1`,

\[
\begin{aligned}
\Xi_1={}&
 \binom L2{D\over r(r-1)}
 +L{2\over r(r-1)}\\
&+\left(\binom L2-L\right)
       {4(D-2)\over r(r-1)^2(r-2)}\\
&+2L{2\over r}
 +(L^2-2L){2(D-1)\over r(r-1)^2}.
                                                               \tag{6.2}
\end{aligned}
\]

### Theorem 6.2 (exact collision mass, `a=2`)

When `a=2` and `L=D+2`,

\[
\begin{aligned}
\Xi_2={}&
 L{2\over r(r-1)}
 +\left(\binom L2-L\right)
       {4(D-1)\over r(r-1)^2(r-2)}\\
&+L{2\over r(r-1)}
 +L{8\over r(r-1)^2(r-2)}\\
&+\left(\binom L2-2L\right)
 {36(D-3)\over r(r-1)^2(r-2)^2(r-3)}\\
&+2L{2\over r}
 +2L{4\over r(r-1)^2}\\
&+(L^2-4L)
 {12(D-2)\over r(r-1)^2(r-2)^2}.
                                                               \tag{6.3}
\end{aligned}
\]

Terms with a zero combinatorial multiplicity are omitted in the smallest
admissible cases.

#### Proof

For `a=1`, every two owners in one packet have separation one.  Among the
root pairs, exactly `L` are adjacent cyclic edges and have separation one;
the other `binom(L,2)-L` have separation two.  Exactly `2L` owner/root pairs
are incident, because every cyclic 2-interval contains two singleton owner
omissions.  The remaining `L^2-2L` mixed pairs have `j=2`.  Substitute the
corresponding rows of (4.1) and divide by `D_0`; this is (6.2).

For `a=2`, owners are indexed by cyclic edges.  Exactly `L` pairs of those
edges meet and the rest are disjoint.  Roots are indexed by cyclic
3-intervals: `L` pairs have shift one, `L` have shift two, and the remaining
`binom(L,2)-2L` are disjoint.  For an owner edge and a root 3-interval,
there are respectively

\[
                         2L,\qquad2L,\qquad L^2-4L          \tag{6.4}
\]

pairs with intersection sizes two, one, zero, equivalently mixed
separations `j=1,2,3`.  Substitute (4.2). `square`

### Corollary 6.3 (aggregate near-linearity)

If `D=O(sqrt(r))`, as at triangular depth, then

\[
 \boxed{
                         \Xi_a=O(L/r)=O(r^{-1/2}).}          \tag{6.5}
\]

For any fixed packet `P`, the number of packets `P'` with
`|P intersect P'|>=2` is at most

\[
                         D_0\Xi_a=o(D_0).                   \tag{6.6}
\]

#### Proof

Equations (6.2)--(6.3) give (6.5) term by term.  A packet `P'` meeting `P`
in at least two resources contributes at least one to

\[
             \sum_{\{X,Y\}\in\binom P2}d(X,Y),             \tag{6.7}
\]

so (6.1) gives (6.6). `square`

This removes a false growing-uniformity alarm.  The crude estimate

\[
                      \binom{2L}{2}{\Delta_2\over D_0}
                         =Theta(1)                           \tag{6.8}
\]

does not reflect the packet geometry: maximum-codegree pairs are sparse.
The packet system is aggregate-near-linear around every edge.  An integral
matching theorem still needs a cover-down/absorption argument, but it may
exploit the stronger local input (6.6), rather than only the worst-case
codegree (4.5).
