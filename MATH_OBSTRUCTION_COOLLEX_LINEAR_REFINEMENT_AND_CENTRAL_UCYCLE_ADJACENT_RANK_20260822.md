# Cool-lex has a linear singleton-refinement cost, and a central subset ucycle does not force adjacent-rank coverage

**Date:** 2026-08-22  
**Status:** proved obstruction and exact finite certificate  
**Scope:** the direct singleton/sliding-window interpretation of cool-lex and
natural subset universal cycles.  No assertion is made about set-valued
letters, a reordering that abandons cool-lex, or a specially constructed
multirank universal cycle.

## 1. Setup and conclusions

Put

\[
 n=2m+1,\qquad W=\binom{2m+1}{m}.
\]

A cyclic singleton word is a cyclic sequence `w=(w_i)` over `[n]`.  Its
length-`ell` window at `i` realizes the set

\[
 [w_i,\ldots,w_{i+\ell-1}]
 :=\{w_i,\ldots,w_{i+\ell-1}\}.
\]

There are two distinct candidate constructions that are sometimes conflated.

1. **Cool-lex order:** list the characteristic binary words of the
   `m`-subsets by prefix rotation and try to lift that list to successive
   singleton windows.
2. **Natural subset ucycle:** construct a singleton word of length `W` whose
   length-`m` windows themselves enumerate all `m`-subsets.

The first route has an asymptotically linear obstruction:

\[
 \boxed{
 N\ge W+\binom{2m-1}{m-1}-1
   =\left(\frac54+o(1)\right)W
 }
\tag{1.1}
\]

for every order-preserving singleton refinement of the standard cool-lex
cycle.  Thus this literal cool-lex route cannot prove a coefficient-one
upper bound.

The second route avoids (1.1), but central exactness alone gives no
adjacent-rank guarantee.  There is an explicit cyclic `(7,3)` subset ucycle
whose arbitrary interval unions realize only `21` of the `35` four-subsets.
The loss is already `40%` one rank above the central layer.

The durable positive output is an exact criterion: for any central subset
ucycle, coverage of ranks `m-1` and `m+1` is precisely coverage by the
intersection and union labels of consecutive central windows.  Hence a
useful ucycle must be designed as a multirank object; being a central ucycle
is not by itself such a theorem.

## 2. The standard cool-lex successor has one quarter distance-two moves

For a weight-`m` binary word of length `n`, the standard cool-lex successor
finds the shortest prefix ending in `010` or `011` and cyclically rotates
that prefix one place to the right.  If there is no such prefix, it rotates
the entire word one place to the right.  The resulting cyclic list is the
standard cool-lex listing of the weight-`m` words.

### Lemma 2.1 (exact bad-transition catalogue)

For `m>=2`, a cool-lex transition has Hamming distance four exactly when its
source has the unique form

\[
                  1^a0^b10\gamma,
 \qquad a,b\ge1.                                      \tag{2.1}
\]

All other transitions have Hamming distance two.

**Proof.**  Before the first occurrence of `01`, a binary word has the form
`1^a0^b`, allowing `a=0`.  If that first `01` has a following bit `c`, the
shortest rotated prefix is therefore

\[
                    1^a0^b1c.
\]

When `c=1`, right rotation changes one zero to one and one one to zero.
When `c=0` and `a=0`, the same is true.  When `c=0` and `a>=1`, direct
comparison gives four changed positions: the first position, the end of the
initial one-run, the isolated `1`, and the final `0`.  This is exactly
(2.1).  If there is no eligible prefix, the word has only the terminal
`01` or no `01`; rotating the whole word merely moves across its unique
cyclic run boundary and again changes two positions.  ∎

### Lemma 2.2 (exact count)

The number of Hamming-distance-four transitions in the weight-`m`,
length-`2m+1` cool-lex cycle is

\[
                  B_m=\binom{2m-1}{m-1}-1.             \tag{2.2}
\]

Consequently

\[
 \frac{B_m}{W}
 =\frac{m+1}{2(2m+1)}-\frac1W
 =\frac14+o(1).                                       \tag{2.3}
\]

**Proof.**  Fix the initial one-run length `a` in (2.1).  The displayed
prefix already contains `a+1` ones, so `gamma` has length
`n-a-b-2` and weight `m-a-1`.  Summing first over `b` and then using the
hockey-stick identity gives

\[
\begin{aligned}
B_m
 &=\sum_{a=1}^{m-1}\sum_{b\ge1}
       \binom{n-a-b-2}{m-a-1}\\
 &=\sum_{a=1}^{m-1}\binom{n-a-2}{m-a}\\
 &=\sum_{j=1}^{m-1}\binom{m+j-1}{j}
  =\binom{2m-1}{m-1}-1.
\end{aligned}
\]

The quotient in (2.3) follows from

\[
 \frac{\binom{2m-1}{m-1}}{\binom{2m+1}{m}}
 =\frac{m+1}{2(2m+1)}.
\]
∎

### Theorem 2.3 (linear order-preserving refinement cost)

Suppose a cyclic singleton word contains clean length-`m` windows equal to
all cool-lex `m`-subsets in their cool-lex cyclic order.  Intervening windows
are allowed, and they need not have rank `m`.  If the singleton word has
length `N`, then (1.1) holds.

**Proof.**  Sliding a singleton window one position deletes at most one
coordinate from its union and adds at most one coordinate.  Hence moving
between two rank-`m` endpoint sets takes at least their Johnson distance,
half their symmetric-difference size.  A Hamming-distance-two cool-lex move
costs at least one slide, while a Hamming-distance-four move costs at least
two.  The cyclic arcs between successive prescribed cool-lex windows are
disjoint and contain all `N` slides.  Lemma 2.2 therefore gives

\[
 N\ge (W-B_m)+2B_m=W+B_m.
\]

Substitution of (2.2) proves the theorem.  ∎

This obstruction is invariant under a fixed relabelling of the coordinates.
It also explains the type mismatch in a binary fixed-density de Bruijn or
prefix-shift construction: prefix rotation is a short move on *positions of
a characteristic word*, but fixed-coordinate singleton windows can change
only one entering/leaving coordinate pair per slide.

## 3. Exact adjacent-rank calculus for a true central subset ucycle

Let `w=(w_i)_{i in Z_W}` be a natural central subset ucycle, meaning that

\[
 U_i:=\{w_i,w_{i+1},\ldots,w_{i+m-1}\}
\tag{3.1}
\]

enumerates every `m`-subset of `[2m+1]` exactly once.  Each displayed window
is clean because it has `m` positions and rank `m`.

### Lemma 3.1 (the next rank is also clean)

Every length-`m+1` window of `w` has `m+1` distinct symbols.

**Proof.**  The shifted window `U_{i+1}` is clean, so `w_{i+m}` differs from
`w_{i+1},...,w_{i+m-1}`.  If `w_{i+m}=w_i`, then (3.1) gives
`U_{i+1}=U_i`, contradicting exact enumeration.  Thus it differs from all
`m` preceding symbols.  ∎

### Theorem 3.2 (arbitrary intervals reduce to consecutive edge labels)

For a central subset ucycle:

\[
\begin{aligned}
\{\text{rank-}(m-1)\text{ interval unions}\}
 &=\{U_i\cap U_{i+1}:i\in\mathbb Z_W\},\\
\{\text{rank-}(m+1)\text{ interval unions}\}
 &=\{U_i\cup U_{i+1}:i\in\mathbb Z_W\}.              \tag{3.2}
\end{aligned}
\]

In particular, allowing intervals longer than their target rank does not
create any additional adjacent-rank targets.

**Proof.**  Every interval of length at least `m` contains a clean
length-`m` window and therefore has union size at least `m`.  A rank-`m-1`
interval consequently has length at most `m-1`; since a singleton interval
of length below `m-1` cannot have rank `m-1`, its length is exactly `m-1`.
These windows are precisely

\[
 \{w_{i+1},\ldots,w_{i+m-1}\}=U_i\cap U_{i+1}.
\]

Now let an arbitrary interval have union `S` of size `m+1`.  Its first `m`
positions form some clean set `U` of size `m`.  Scan forward to the first
symbol `x` outside `U`; such a symbol exists because the full interval has
union `S`.  The `m` symbols immediately preceding `x` are a clean
length-`m` window, all belong to `U`, and hence equal `U`.  Therefore the
length-`m+1` window ending at `x` has union `U\cup\{x\}=S`.  Lemma 3.1 says
these length-`m+1` windows are exactly

\[
 \{w_i,\ldots,w_{i+m}\}=U_i\cup U_{i+1}.
\]

This proves both identities.  ∎

There are `W` upper edge labels and exactly `W` upper targets, so covering
rank `m+1` up to `o(W)` loss requires the union labels in (3.2) to be
injective up to `o(W)` collisions.  On the lower side there are

\[
 \binom{2m+1}{m-1}=\frac{m}{m+2}W
\]

targets, so even perfect lower coverage has the unavoidable
`2W/(m+2)=o(W)` excess labels.  None of these near-injectivity properties is
part of the definition of a central ucycle.

More generally, suppose every symbol occurs at most once in each
length-`m+q` window.  Then

\[
 \{w_i,\ldots,w_{i+m+q-1}\}=\bigcup_{t=0}^{q}U_{i+t},
\tag{3.3}
\]

and

\[
 \{w_i,\ldots,w_{i+m-q-1}\}=\bigcap_{t=0}^{q}U_{i-t}.
\tag{3.4}
\]

Thus all-band coverage asks for simultaneous near-injectivity/surjectivity
of a growing family of consecutive union and intersection labels, together
with a symbol-return gap.  It is substantially stronger than central
exactness.

## 4. A central exact ucycle with a forty-percent adjacent-rank hole

Consider the following cyclic word on `[7]`:

\[
 w=12341253162371452673546157436572467.                \tag{4.1}
\]

Its consecutive cyclic triples, in order, are

```
123 234 134 124 125 235 135
136 126 236 237 137 147 145
245 256 267 367 357 345 456
146 156 157 457 347 346 356
567 257 247 246 467 167 127
```

They are `35` distinct triples, hence all `binom(7,3)=35` triples.  Thus
(4.1) is an exact natural `(7,3)` subset ucycle.

Its consecutive pairs are all `21` pairs:

```
12 13 14 15 16 17 23 24 25 26 27
34 35 36 37 45 46 47 56 57 67
```

so the lower adjacent rank is complete.  In contrast, its distinct
four-windows are only

```
1234 1235 1236 1237 1245 1267 1347
1356 1456 1457 1467 1567 2367 2456
2457 2467 2567 3456 3457 3467 3567
```

and the fourteen missing four-subsets are

```
1246 1247 1256 1257 1345 1346 1357
1367 2345 2346 2347 2356 2357 4567.
```

By Theorem 3.2 these fourteen targets are not recovered by *any* longer
cyclic intervals.  The adjacent upper coverage is therefore exactly
`21/35=3/5`.

## 5. Research verdict

The literal cool-lex-prefix-rotation construction is decisively excluded as
a coefficient-one singleton lift: retaining its cyclic order costs an
asymptotic factor at least `5/4` before any other ranks are repaired.

A true central subset ucycle remains a potentially useful starting object,
but the central property alone does not move the coefficient-one proof.  A
positive theorem would have to construct, not infer,

1. `o(W)` collision loss among both adjacent edge-label families;
2. the analogous consecutive union/intersection property throughout a
   Gaussian-width rank band; and
3. a symbol-return gap long enough to make those band windows clean.

The `(7,3)` certificate shows why item 1 cannot be omitted.  The result does
not rule out a specially engineered multirank ucycle; it identifies that
strengthening as the exact new theorem such a route would need.

## 6. Reproduction certificate

The checker
`scratch/verify_coollex_ucycle_obstruction_20260822.py` verifies, for
`1<=m<=9`, the exact cool-lex transition count, and verifies all cyclic
windows and all arbitrary cyclic interval unions of (4.1).  Its output is

```
COOLLEX_UCYCLE_OBSTRUCTION_VERIFY_PASS
```

The checker is only a reproduction aid.  The general count, the refinement
lower bound, the adjacent-rank reduction, and the literal finite certificate
are all proved or displayed above.
