# Cyclic pivot reservoirs separate common-basis avoidance from one nested splice gate

Date: 2026-08-01

Status: unconditional fixed-`H` planting/avoidance and exact opening-debt
theorems, followed by a proof-sufficient socket reduction.  The socket
extension, ambient Catalan connector, higher upper deck and common compiler
cap remain open.  No all-`k` upper bound is claimed.

## 0. Verdict

Let `h=d(2m-1)`.  One shared-bank pivot cycle has `3h+2` owner edges and
therefore `6h+4` edges in its middle-levels incidence lift.  Consequently a
resource-disjoint bank of `H` such cycles is planted by the existing small
protected-factor theorem whenever

\[
                         H(6h+4)\le m-2.                \tag{0.1}
\]

For fixed `H`, (0.1) holds in every sufficiently large dimension because
`h=Theta(sqrt(m))`.

On a two-coordinate Catalan recursion face, any fixed collision/casualty
projection `R` of order `O(Hh)` can simultaneously be avoided by the
synchronized common basis.  This follows from the exact uniform marginal
and does not require concentration.

These two facts do not make a linear chronology.  Every cut of a shared-bank
cycle creates exactly

\[
                             \boxed{2h}                  \tag{0.2}
\]

positive endpoint fragments shorter than the required length `h+1`.  The
number is independent of the cut.  Thus retaining packets cyclically
removes packet-internal residence from the Catalan selector, but a final
internal opening still requires a trace-compatible splice.

For the safe J6 opening `R_(h-1)->H`, the endpoint record is two nested
banks.  If the packet is the global prefix, the left bank is absorbed by the
global boundary and the only residence obligation is the explicit right
socket

\[
 p\in Y_1,\qquad d_i\in Y_1\cap\cdots\cap Y_{i+1}
       \quad(1\le i<h),                                 \tag{0.3}
\]

where `Y_1,Y_2,...` are the succeeding owners.  Hence the packet-specific
`B+1` gate is no longer an unspecified residence collar: it is one nested
outgoing socket, one protected duplicate of the removed upper colour, and
the already known global host/deck/compiler rows.

Keeping the packet cyclic therefore weakens the **protected** Catalan
connector problem, but it does not solve the ambient Catalan-scale connector.

## 1. Fixed-`H` cyclic planting

Use the notation of
`MATH_THEOREM_SHARED_BANK_PIVOT_RESIDENT_CYCLE_20260801.md`.  One packet has
the owner cycle

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,
 R_0,\ldots,R_{h-1},H.                                  \tag{1.1}
\]

Every Johnson transition in (1.1) lifts through its rank-`m-1`
intersection to two incidence edges in `ML_m`.  Thus its lift is a cycle of
length

\[
                         2(3h+2)=6h+4.                  \tag{1.2}
\]

### Theorem 1.1 (fixed-`H` cyclic reservoir)

Let `P` be a bank of `H` copies of (1.1) sharing neither owner vertices nor
rank-`m-1` intersection vertices.  If (0.1) holds, `P` extends to a spanning
owner/lower-`q1` two-factor of `ML_m`.

In every such extension each cycle of `P` is a complete factor component.

### Proof

The incidence lift of `P` is 2-bounded and has `H(6h+4)` edges.  The small
protected-factor theorem extends every 2-bounded bank of at most `m-2`
edges to a spanning two-factor, proving the first assertion.

Every incidence vertex on a protected cycle already has protected degree
two.  A two-factor cannot add another incident edge.  Hence no unprotected
edge leaves that cycle, so it remains a complete component.  `square`

The second assertion is both useful and limiting.  A cyclic packet is fully
resident without any external collar, but it cannot be connected to the
ambient factor until at least one of its protected transitions is replaced.

## 2. Uniform-marginal avoidance of the fixed casualty bank

Use the constants of the automatic synchronized common-basis theorem:

\[
 N={2n\choose n-1},\qquad C=\operatorname{Cat}_{n+1},
 \qquad {N\over C}={n(n+2)\over2(2n+1)}>{n\over4}.      \tag{2.1}
\]

For every oriented child ground `E` of order `N`, there is a distribution on
synchronized common bases `Q` with

\[
                         \Pr(e\in Q)={C\over N}
                         \quad(e\in E).                 \tag{2.2}
\]

### Theorem 2.1 (fixed-`H` casualty avoidance)

Fix constants `a,b,H`.  Suppose the already selected cyclic packet bank and
its literal guards induce a fixed forbidden child-edge set `R subset E`
satisfying

\[
                         |R|\le aHh+bH,                 \tag{2.3}
\]

where `h=O(sqrt(n))`.  For all sufficiently large `n`, there is a
synchronized common basis `Q` with

\[
                              Q\cap R=emptyset.          \tag{2.4}
\]

### Proof

For fixed `a,b,H`, equation (2.3) is `O(sqrt(n))`, while (2.1) is larger
than `n/4`.  Hence `|R|<N/C` eventually.  Under (2.2),

\[
                         E|Q\cap R|={C\over N}|R|<1.
\]

The random variable is a nonnegative integer, so one common basis has value
zero.  `square`

The quantifier in Theorem 2.1 is important: the packet and its casualty
projection are fixed before `Q` is chosen.  The theorem applies to the
cycle's `O(Hh)` incidence/cut/provider bank only when that bank has been
identified as a fixed subset of the common-basis ground `E`.  It does not
choose physical side representatives, construct the rooted Catalan forest,
or make a casualty set that depends on `Q` avoidable.

In particular, if that fixed projection has no more than the full protected
incidence count, then the explicit sufficient inequality is

\[
                  H(6h+4)<{n(n+2)\over2(2n+1)},         \tag{2.5}
\]

which again holds eventually for every fixed `H`.

### Theorem 2.2 (linear-bank bounded intersection)

Under the same uniform-marginal law (2.2), let `R subset E` be any fixed
forbidden or casualty bank with

\[
                         |R|\le A n+B                           \tag{2.6}
\]

for absolute constants `A,B`.  Then some synchronized common basis `Q`
satisfies

\[
 \boxed{
 |Q\cap R|
 \le
 \left\lfloor {C\over N}|R|\right\rfloor
 \le 4A+O_{A,B}(n^{-1}).}                                  \tag{2.7}
\]

In particular a fixed `O(n)` protected battery or cut bank costs only
`O(1)` common-basis elements, even when it is too large to avoid completely.

#### Proof

Equation (2.2) and linearity of expectation give

\[
                    \mathbb E|Q\cap R|={C\over N}|R|.         \tag{2.8}
\]

Some outcome is no larger than its mean.  Since the intersection size is
an integer, the first inequality in (2.7) follows.  Equation (2.1) gives

\[
 {C\over N}={2(2n+1)\over n(n+2)}={4\over n}+O(n^{-2}),       \tag{2.9}
\]

and substitution of (2.6) proves the second inequality.  \(\square\)

The quantifier remains the same as in Theorem 2.1: `R` must be fixed before
the common basis is sampled.  The theorem does not control a casualty bank
chosen adaptively from `Q`, nor does it turn an abstract common-basis edge
into a typed physical compiler bundle.  Its exact terminal use is to fix a
linear-size protected battery first, choose the common basis last, discard
its `O(1)` intersecting elements, and append those logical masks once.

Thus fixed-`H` incidence planting and common-basis noncollision are no
longer scalar obstructions.  Their physical correlation with the connector
still is.

## 3. Exact cycle-opening debt

The nonconstant coordinate runs of (1.1) are as follows:

\[
\begin{array}{c|c}
\text{coordinate family}&\text{cyclic positive-run length}\\ \hline
x_L&2h+2\\
x_R,p&2h+1\\
\rho_h&h+2\\
\lambda_1,\ldots,\lambda_h&h+1\\
\rho_1,\ldots,\rho_{h-1}&h+1\\
d_1,\ldots,d_{h-1}&h+1.
\end{array}                                              \tag{3.1}
\]

The coordinates in `C=B-{x_L,x_R}` are constant and create no boundary
state.

### Theorem 3.1 (cut-independent debt)

At every owner edge of (1.1), exactly `h+1` nonconstant runs cross the cut.
Opening there splits those runs into exactly `2h` positive endpoint
fragments of length below `h+1`.

### Proof

Two adjacent owners have intersection rank `m-1`.  Removing the constant
core `C`, of size `m-h-2`, leaves exactly `h+1` crossing nonconstant
coordinates.

A run of total length `h+1` contributes two short fragments whenever it is
cut internally.  A run of total length `2h+1` contributes exactly one.  A
run of length `2h+2` contributes one except at its balanced cut, where it
contributes zero.  The run of `rho_h`, of length `h+2`, contributes one at
an end cut and two at an internal cut.  The seven edge classes give:

\[
\begin{array}{c|c|c|c}
\text{cut}&\text{special crossing runs}&
 \#(h+1)\text{-runs}&\text{short fragments}\\ \hline
L_tL_{t+1}&p,x_L&h-1&2(h-1)+2\\
L_{h-1}M_0&x_L\text{ balanced}&h&2h+0\\
M_jM_{j+1}&x_L,x_R&h-1&2(h-1)+2\\
M_hR_0&x_R,\rho_h&h-1&2(h-1)+2\\
R_tR_{t+1}&p,x_R,\rho_h&h-2&2(h-2)+4\\
R_{h-1}H&p,\rho_h&h-1&2(h-1)+2\\
HL_0&p,x_L&h-1&2(h-1)+2.
\end{array}                                              \tag{3.2}
\]

Every last entry equals `2h`.  The empty internal edge classes at `h=2`
cause no exception.  `square`

Consequently no choice of opening edge reduces the total residence debt.
At most two endpoint sides among all opened components can be the two global
word boundaries.  Hence opening `H` packet cycles in a single final linear
chronology leaves between `2H-2` and `2H` packet endpoint sides requiring
compatible continuation.

## 4. The J6 boundary state is one nested socket

Remove the edge `R_(h-1)->H` and orient the resulting path as

\[
 H,L_0,\ldots,L_{h-1},M_0,\ldots,M_h,
 R_0,\ldots,R_{h-1}.                                    \tag{4.1}
\]

### Theorem 4.1 (exact J6 endpoint record)

The only short positive fragments at the start of (4.1) are

\[
 \rho_h:1,qquad d_i:i+1\quad(1\le i<h),                \tag{4.2}
\]

and the only short positive fragments at its end are

\[
 p:h,qquad d_i:h-i\quad(1\le i<h).                    \tag{4.3}
\]

In particular, if the start of (4.1) is the global left boundary, a host
continuation `Y_1,Y_2,...` heals residence exactly when it keeps

\[
 p\in Y_1,qquad d_i\in Y_1,\ldots,Y_{i+1}              \tag{4.4}
\]

before any of those coordinates is deleted.  Continuing them longer is
also legal.

### Proof

The `p` run is

\[
 R_0,\ldots,R_{h-1},H,L_0,\ldots,L_{h-1};
\]

the `rho_h` run is

\[
 M_h,R_0,\ldots,R_{h-1},H;
\]

and the `d_i` run is

\[
 R_i,\ldots,R_{h-1},H,L_0,\ldots,L_{i-1}.
\]

Cutting `R_(h-1)->H` gives (4.2)--(4.3).  A suffix of length `h-i`
needs `i+1` further ones to reach `h+1`, while the `p` suffix needs one.
This is (4.4).  `square`

The removed lower and upper q1 colours are

\[
 C+p+D+\rho_h,qquad B+p+D+\rho_h.                     \tag{4.5}
\]

In an additive-one owner Hamilton path, the first value in (4.5) may be the
single forced missing lower boundary colour.  The second must have a
protected duplicate provider or be recreated by the splice.  This is why
the k17 J6 macro protects the old upper provider `1484:6`.

## 5. What keeping the packet cyclic does and does not reduce

While a packet remains cyclic:

1. all its owner, q1, pivot, ray and source pins are literal;
2. cyclic residence is complete, with no exported clipped state;
3. Theorem 2.1 permits the synchronized common basis to avoid any fixed
   `O(Hh)` collision bank; and
4. the packet can be contracted to one protected component for purposes of
   later topology.

This removes the need to force all `O(Hh)` internal packet incidences
through the rooted-Catalan connector selection.  Only the chosen break,
the two endpoint traces and the lost palette providers remain packet-specific.

However, the ambient factor still has to connect its Catalan-scale family
of unprotected components.  Theorem 1.1 by itself may return arbitrarily
many such components, and Theorem 2.1 chooses no physical representatives.
Keeping `H` bounded cycles intact therefore does not prove the ambient
Catalan connector or physical side-forest theorem.  It merely separates
that global theorem from the packet's internal residence algebra.

## 6. The shortest remaining socket theorem

The preceding results isolate the following proof-sufficient statement.

> **Cyclic-reservoir socket extension `CRS(H,C)`.**  For every sufficiently
> large parameter and every fixed bank of `H` shared-bank pivot cycles,
> choose a synchronized common basis avoiding their fixed casualty bank and
> a fully guarded ambient Catalan realization such that:
>
> 1. one break is selected in each packet cycle and the contracted
>    packet/host attachment graph is a linear forest with at most two
>    unjoined global ends;
> 2. every joined endpoint passes the exact capped residence test (for J6,
>    the test is (4.2)--(4.4));
> 3. every removed upper q1 colour and every nonboundary removed lower q1
>    colour has a protected old or new provider, while the unique declared
>    lower boundary colour is assigned to the controlled boundary
>    cell/common cap;
> 4. all ambient arbitrary-width upper witnesses and compiler assignments
>    survive the joins; and
> 5. at most `C` literal targets remain unserved.

### Theorem 6.1 (conditional additive implication)

If `CRS(H,C)` holds for fixed `H,C` and the `H` pivot insertions are the
only added source letters, then

\[
                         \nu(k)\le B(k)+H+C.             \tag{6.1}
\]

For `H=1`, if the J6 path is the global prefix, (4.4) is supplied, the
second colour in (4.5) has a protected provider, and `C=0`, then

\[
                         \nu(k)\le B(k)+1.               \tag{6.2}
\]

### Proof

Each monotone pivot insertion costs one source position, preserves every
old interval-OR value, and places its pivot target and two compiler rays
literally.  Conditions 1--2 turn the cyclic packets and ambient host into a
resident linear chronology.  Condition 3 preserves both immediate palettes,
including literal service of the unique lower boundary colour in the `H=1`
path case.
Condition 4 preserves every remaining upper and lower assignment.  Append
the at most `C` residual targets as literal letters.  The total extra length
is `H+C`, proving (6.1), and (6.2) is its stated specialization. `square`

`CRS` is weaker on the packet side than the earlier protected
Catalan--pivot theorem: the common basis and bulk connector need not carry
the packet's internal `O(Hh)` edge bank.  It is not weaker on the ambient
side.  It still needs one correlated physical Catalan realization with
topology, socket traces, deep providers and the common cap.

For exact `B+1`, the shortest packet-specific missing row is therefore the
one-sided nested socket (4.4), not another local pivot construction.  For
general `B+O(1)`, it is a fixed collection of such socket records together
with the still-open ambient guarded connector.

## 7. Independent finite audit

The O3 C++ audit

```text
scratch/audit_shared_bank_cycle_opening_debt_20260801.cpp
a41b6754586da1488a750ceeb13cdecd6bec3a1fc6b692df97af0c98701032db
```

checks every cut for every `2<=h<=96`, a total of `14155` cuts, and verifies

```text
crossing nonconstant runs = h+1
short endpoint fragments = 2h
J6 start = rho_h:1; d_i:i+1
J6 end   = p:h; d_i:h-i.
```

Its retained output is

```text
scratch/shared_bank_cycle_opening_debt_20260801.audit.json
d67672ec6e0a6f01e8adbdaabe153eca21eab336f686f2f04efda4b5ac8f0a22
```

and reports `PASS_SHARED_BANK_CYCLE_OPENING_DEBT`.  It was compiled and run
on one H100 CPU; no GPU was used.  The audit corroborates Theorems 3.1 and
4.1 but is not used to infer them.
