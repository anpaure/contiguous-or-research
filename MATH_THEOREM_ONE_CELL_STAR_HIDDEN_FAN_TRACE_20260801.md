# Exact trace algebra of a one-cell seam: what the star hides, and what it cannot hide

Date: 2026-08-01  
Status: exact local theorem.  This characterizes, coordinate by coordinate,
the simultaneous values of the `2d-1` new fan cells and the `d-1` destroyed
crossing cells in the one-cell seam exchange.  It is an interface theorem,
not an all-`k` construction: carrier-envelope containment, protected exterior
pins, and host planting remain separate requirements.

## 0. Result

Insert a new source position `*` at an internal cut.  The star payload is
seen by every new fan cell and by none of the old length-`d` crossing cells.
This gives a genuine hidden channel, but not an arbitrary one.

Once the left and right fan chains are prescribed, the crossing trace of
every coordinate outside the star payload is forced.  A coordinate inside
the star payload remains invisible to the fans when copied to old side
positions; its crossing membership can be programmed exactly when its zero
set is an interval.  Thus the phrase “star-hidden coding” has the precise
meaning

\[
 \boxed{\text{programmable bits} = \text{star coordinates with
 interval-zero crossing traces}.}
\tag{0.1}
\]

In particular, the fan targets and lost-crossing targets are not independent.
The exact compatibility criterion is Theorem 2.1 below.

## 1. The seam equations

Fix `d>=2`.  Around the cut write the old source positions as

\[
 -(d-1),\ldots,-1\mid 1,\ldots,d-1
\]

and put the inserted position at `0=*`.  Let their nonempty set values be
`A_t`.  For `1<=h<=d`, define the two fan unions

\[
 L_h=\bigcup_{t=0}^{h-1}A_{-t},\qquad
 R_h=\bigcup_{t=0}^{h-1}A_t,
 \qquad A_{-0}=A_0.
\tag{1.1}
\]

Thus `L_1=R_1=A_0`; call this common value `Z`.  Index the old crossing
length-`d` intervals by the number `i` of old points taken on the left:

\[
 I_i=\{-i,\ldots,-1,1,\ldots,d-i\},\qquad 1\le i\le d-1,
\]

and write

\[
 C_i=\bigcup_{t\in I_i}A_t.
\tag{1.2}
\]

### Theorem 1.1 (exact fan--crossing identity)

For every `1<=i<=d-1`,

\[
 \boxed{Z\cup C_i=L_{i+1}\cup R_{d-i+1}.}
\tag{1.3}
\]

For a coordinate `x`, let

\[
 \lambda_x=\min\{t\ge1:x\in A_{-t}\},\qquad
 \rho_x=\min\{t\ge1:x\in A_t\},
\tag{1.4}
\]

with a missing minimum interpreted as infinity.  Then

\[
 \boxed{x\in C_i\iff i\ge\lambda_x\ \text{ or }\ i\le d-\rho_x.}
\tag{1.5}
\]

Consequently the zero set

\[
 \{i\in[1,d-1]:x\notin C_i\}
\tag{1.6}
\]

is an interval, possibly empty or all of `[1,d-1]`.

#### Proof

Both sides of (1.3) are the union of `A_0`, the nearest `i` old positions
on the left, and the nearest `d-i` old positions on the right.  Equation
(1.5) follows because a left occurrence at distance `t` belongs to `I_i`
exactly when `i>=t`, while a right occurrence at distance `t` belongs to
`I_i` exactly when `i<=d-t`.  The complement of a prefix union a suffix is
an interval.  \(\square\)

The useful threshold dictionary is therefore

\[
 x\in A_{-t}\Longrightarrow \mathbf 1_{x\in C_i}\ge \mathbf 1_{i\ge t},
 \qquad
 x\in A_t\Longrightarrow \mathbf 1_{x\in C_i}\ge \mathbf 1_{i\le d-t}.
\tag{1.7}
\]

An occurrence at the star changes neither trace in (1.7): it is present in
all fans and absent from every `C_i`.

## 2. Exact simultaneous realization criterion

Let

\[
 Z=L_1=R_1\subseteq L_2\subseteq\cdots\subseteq L_d,
 \qquad
 Z=L'_1\subseteq R_2\subseteq\cdots\subseteq R_d
\tag{2.1}
\]

be two desired fan chains (the prime on `L'_1` only emphasizes that it is
the same set `Z`).  Let `C_1,...,C_(d-1)` be desired crossing values.

### Theorem 2.1 (star-hidden compatibility)

There exist side source values whose fan and crossing unions are exactly
the prescribed sets if and only if the following hold.

1. The fan sequences are nested and have the same first value `Z`.
2. For every `x notin Z` and every `i`,

   \[
   x\in C_i
   \iff
   x\in L_{i+1}\ \text{or}\ x\in R_{d-i+1}.
   \tag{2.2}
   \]

3. For every `z in Z`, the set

   \[
   \{i:z\notin C_i\}
   \tag{2.3}
   \]

   is an interval.

Empty side source values are allowed in this abstract statement.  If every
fan inclusion is strict, the canonical realization below has nonempty side
sources, as required for an OR word.

#### Proof

Necessity of item 1 is immediate from (1.1).  If `x notin Z`, membership in
the right side of (1.3) is equivalent to membership in `C_i`, proving item
2.  Item 3 is Theorem 1.1.

Conversely, start with the canonical increments

\[
 A_0=Z,\quad A_{-t}=L_{t+1}\setminus L_t,\quad
 A_t=R_{t+1}\setminus R_t\qquad(1\le t\le d-1).
\tag{2.4}
\]

This realizes the two fan chains.  For `x notin Z`, equation (2.2) and the
first-appearance thresholds make its crossing trace correct.  For `z in Z`,
the desired zero interval `[a,b]` is realized by putting an additional copy
of `z` at left distance `b+1` when `b<d-1`, and at right distance `d-a+1`
when `a>1`; omit the corresponding copy at an absent boundary.  The empty
zero interval is obtained by one sufficiently near side copy, and the full
zero interval by no side copy.  These copies do not alter either fan chain
because `z` was already present at the star.  Equation (1.5) now gives the
desired trace.  \(\square\)

The endpoint formulas in the preceding proof include the conventions:
a left copy at distance `lambda` gives ones on `i>=lambda`, and a right copy
at distance `rho` gives ones on `i<=d-rho`.  They are often safer to use
directly than the displayed interval endpoints.

## 3. The typed-socket corollary and its exact price

A target `S` can occupy the shared singleton fan address if one plants a cut
whose legal source envelope contains `S` and sets

\[
                             A_*=Z=S.                 \tag{3.1}
\]

This is a literal target occurrence, not merely a Hall edge.  The remaining
fan cells must be two nested target chains above `S`, and their simultaneous
lost-crossing values must pass Theorem 2.1.  Therefore a **typed seam
socket** consists of all three pieces:

* envelope legality `S subseteq P_*` and preservation of protected pins;
* two strict nested fan chains with common base `S`;
* compatible crossing targets satisfying (2.2)--(2.3).

### Corollary 3.1 (one credit repairs one task, not one task plus a free fan)

Suppose a phase switch has `2(d-1)` old-only nested-chain targets and the
two fans excluding their common singleton realize those targets.  Then:

* leaving the singleton unassigned gives one free fan address;
* assigning a hard target `S` to the singleton consumes that address;
* if the `d-1` destroyed crossing pins are reassigned to native new-phase
  cells, the surviving former assignments contribute exactly `d-1` other
  free addresses.

Thus a typed one-cell seam repairs one new task and leaves `d-1` addresses,
whereas an untyped seam leaves `d` addresses.  This is exactly the global
net gain of `d` short cells from one added source position; there is no
unpriced extra address.

#### Proof

The fan bank has `2d-1` addresses.  The two strict chains use `2d-2` of
them.  The shared singleton is the only remainder.  The rest is the
one-cell seam ledger: the `d-1` crossing addresses disappear, while the
other `d-1` old assignments made redundant by the native new-phase chain
survive and become free.  \(\square\)

## 4. Scope and obstruction

Theorem 2.1 refutes the strongest informal version of star-hidden coding:
one cannot independently prescribe arbitrary fan values and arbitrary lost
crossing values.  For `x notin Z`, equation (2.2) leaves no freedom at all;
for `z in Z`, only interval-zero traces are possible.

The smallest nontrivial obstruction occurs at `d=4`: ask for constant fan
chains `L_h=R_h=Z` and a coordinate `x notin Z` to occur in `C_2` only.
Equation (2.2) forces `x` to occur in no crossing cell, so the request is
impossible.  Even for a star coordinate, the trace `0,1,0` has zero set
`{1,3}`, which is not an interval and is impossible.

On the positive side, prefix/suffix coatom flags have exactly the nested
shape required by the fan bank.  The remaining physical theorem is now
sharply stated: plant a cut for which their induced crossing targets obey
(2.2)--(2.3), and whose star base is an admissible hard target in the same
legal cap state.  This is the literal host-planting/U5 gate; no signed or
cardinality ambiguity remains.

### Corollary 4.1 (direct self-repayment is incompatible with a simple flat row)

Assume the new depth-`d` carrier is flat of rank `r`, so every crossing
owner `Z union C_i` has rank `r`.  If all lost crossing targets `C_i` are
repaid directly by one fan chain (for example `C_i=L_(i+1)`), then the
corresponding crossing owners are all equal.  In particular, a simple
middle-owner chronology cannot use this direct self-repayment at two or
more crossings.

#### Proof

Every fan value contains `Z`.  Hence `Z union C_i=C_i` under the displayed
identification.  The `C_i` form a nested chain, while all have the same rank
`r`; therefore they are equal.  \(\square\)

This small no-go explains why the one-cell credit still needs a nonlocal
augmenting route or an exterior return bank at zero slack.  The star gives
one literal new socket, but it does not make all `d-1` displaced targets
repay themselves locally while retaining distinct middle owners.

There is nevertheless a useful carrier-valid local pattern.  Take disjoint
`Z,{x},F={f_1,...,f_d}`.  Put left increments in the order
`f_1,...,f_(d-1)` and right increments in the order
`x,f_d,f_(d-1),...,f_3`.  Then, for `1<=i<=d-1`,

\[
 C_i=\{x\}\cup(F\setminus\{f_{i+1}\}),\qquad
 Z\cup C_i=Z\cup\{x\}\cup(F\setminus\{f_{i+1}\}).
\tag{4.1}
\]

Thus the internal crossing owners are distinct coatoms of one fixed
`(r+1)`-set and all have the same rank.  This is the correct physical shape,
but its `C_i` are incomparable rather than a fan chain, so their return must
be routed elsewhere.  That is exactly the exterior-ear/gammoid problem.

### Corollary 4.2 (canonical old-chain fans cannot hide the new-chain pins)

Use one canonical mixed-coatom packet with common core `Z`, active labels
`a,b`, and filler flag `G=(g_1,...,g_d)`.  Its old-only chains may be
oriented as

\[
 L_{t+1}=Z\cup\{b\}\cup P_t(G),\qquad
 R_{t+1}=Z\cup\{a\}\cup S_t(G),qquad 1\le t\le d-1.
\tag{4.2}
\]

If these chains are realized on the two fans with star value `Z`, then every
destroyed crossing cell has the same value

\[
                         C_i=\{a,b\}\cup G,
                 \qquad 1\le i\le d-1.                \tag{4.3}
\]

In particular the destroyed cells cannot carry the packet's `d-1`
distinct new-phase chain targets.  Hence “native new cells repay the lost
new-chain pins” is not a literal local consequence of the fan cardinality.
It requires a different cross-packet pairing or a nonlocal augmenting route.

#### Proof

The first left increment is `{b,g_1}` and the later ones are
`g_2,...`; the first right increment is `{a,g_d}` and the later ones are
`g_(d-1),...`.  Therefore (1.2) gives

\[
 C_i=\{a,b\}\cup P_i(G)\cup S_{d-i}(G)
     =\{a,b\}\cup G.
\]

The new-phase chain targets are distinct nested prefix/suffix values, so no
injective bank of them can occupy the repeated cells (4.3).  \(\square\)

## 5. Independent audit

The dependency-free audit enumerates every set-valued local word over a
three-coordinate universe for `2<=d<=6`.  It verifies (1.3), (1.5), the
interval-zero condition, and reconstructs every observed `(L,R,C)` triple
from the criterion in Theorem 2.1:

```text
scratch/audit_one_cell_star_hidden_fan_trace_20260801.py
```

No all-`k`, recursive planting, or common-cap claim is made here.
