# Mirrored Dyck phases fail monodromy, and their exact palette fails at powers of two

**Date:** 2026-08-21  
**Status:** unconditional monodromy obstruction for one mirrored phase
ansatz, plus an independent infinite-subsequence palette obstruction; not
an obstruction to arbitrary wreath factors or arbitrary `C_8` paths

## 1. The mirrored phase ansatz

Let `r` be even, put `J=[2r]`, and let

\[
                         {\cal D}^0,\ldots,{\cal D}^r       \tag{1.1}
\]

be the canonical Chung--Feller partition of the rank-`r` subsets of `J`.
Every class has size

\[
                         m=\operatorname {Cat}_r,           \tag{1.2}
\]

`D^0` is the Dyck class, and complementation sends `D^t` to `D^{r-t}`.
Write `h=r/2`.

A phase-respecting path cover chooses, for each `0<=t<r`, a perfect
matching of Johnson edges from `D^t` to `D^{t+1}`.  A tempting
complement/time-reversal **palette ansatz** is to choose only the first-half
matchings and set

\[
 E_{r-1-t}=\{(J-X',J-X):(X,X')\in E_t\}.                    \tag{1.3}
\]

This symmetry pairs the two intersection-colour palettes, but it does not
force complementary path endpoints; Section 2 proves the exact monodromy
failure.

For a first-half transition `e=(X,X')`, put

\[
 T(e)=X\cap X',\qquad C(e)=J-(X\cup X').                   \tag{1.4}
\]

Both are `(r-1)`-sets.  Under the mirrored transition in (1.3), the
intersection colour is `C(e)`.  Therefore, if this mirrored path cover is
required to have an exact non-anchor q1 intersection-colour palette, it
must satisfy

\[
 \biguplus_{t=0}^{h-1}\ \biguplus_{e\in E_t}
             \{T(e),C(e)\}=\binom J{r-1}.                  \tag{1.5}
\]

## 2. Mirroring never gives complementary endpoints

For `0<=t<h`, write the first-half matching as a bijection

\[
 f_t:{\cal D}^t\longrightarrow {\cal D}^{t+1},
 \qquad G=f_{h-1}\cdots f_0:{\cal D}^0\longrightarrow{\cal D}^h.  \tag{2.1}
\]

Let `c` denote set complementation.

### Theorem 2.1 (universal monodromy failure)

The full endpoint map of the mirrored path cover (1.3) is

\[
                         cG^{-1}cG,                          \tag{2.2}
\]

and it is never the required complement map `c`.  Thus (1.3) alone never
closes its length-`2r` inclusion paths into length-`(2r+1)` wreath cycles.

#### Proof

The mirrored transition at the cut corresponding to `f_t` is
`c f_t^{-1}c`.  In path order, the second-half composition is therefore
`cG^{-1}c`, proving (2.2).  If (2.2) equalled `c`, left composition by
`c` would give

\[
                              G^{-1}cG=\operatorname{id}.    \tag{2.3}
\]

This would make complementation the identity on the central class
`D^h`, which is impossible: no rank-`r` subset of a `2r`-set equals its
complement. `square`

The induced permutation on the `D^0` starts after closing each endpoint by
its actual complement edge is

\[
                         c(cG^{-1}cG)=G^{-1}cG.              \tag{2.4}
\]

It is a conjugate of central complementation and hence a fixed-point-free
involution.  Thus, whenever the intermediate union colours are distinct so
that these lifts are genuine odd-graph paths, the complement edges pair
exactly two length-`2r` paths into cycles of length `4r+2`, rather than
length-`(2r+1)` wreath cycles.  Without that colour-distinctness hypothesis,
the statement is only about the serialized Johnson path cover.

## 3. The independent palette-parity obstruction

Even if endpoint closure is set aside or delegated to a later correction,
the exact palette equation (1.5) has its own obstruction.

### Theorem 3.1

If

\[
                              r=2^s\qquad(s\ge1),            \tag{3.1}
\]

then no first-half transition matchings can satisfy (1.5).  Consequently
the complement-symmetric phase ansatz (1.3) cannot make the **non-anchor q1
intersection-colour sector** exactly rainbow for these `r`.

#### Proof

For a coordinate `x in J`, let `d_x` and `a_x` be the numbers of selected
first-half transitions which respectively delete and add `x`.  Telescoping
the membership of `x` through the perfect transition matchings gives

\[
 d_x-a_x
 =\deg_{{\cal D}^0}(x)-\deg_{{\cal D}^{h}}(x).              \tag{3.2}
\]

There are `hm=rm/2` selected first-half edges.  For one edge, the two
colour sets in (1.4) are disjoint and satisfy

\[
                         T(e)\cup C(e)=J-\{u,v\},            \tag{3.3}
\]

where `u` is its deleted coordinate and `v` its added coordinate.  If
(1.5) holds, the total number of selected colour sets containing a fixed
coordinate is

\[
                         \binom{2r-1}{r-2}.                  \tag{3.4}
\]

Equations (3.3)--(3.4) therefore give

\[
 d_x+a_x={rm\over2}-\binom{2r-1}{r-2}={m\over2}.            \tag{3.5}
\]

It follows from (3.2) and (3.5) that the necessary parity condition

\[
 {m\over2}\equiv
 \deg_{{\cal D}^0}(x)-\deg_{{\cal D}^{h}}(x)\pmod2          \tag{3.6}
\]

must hold for every coordinate.

Apply (3.6) at `x=2`.  The central class `D^h` is invariant under
complementation, which pairs sets containing 2 with sets avoiding 2.
Thus

\[
                         \deg_{{\cal D}^{h}}(2)={m\over2}.   \tag{3.7}
\]

Every Dyck word begins with 1.  Those whose second bit is 0 are exactly
the words `10w` with `w` an arbitrary Dyck word of semilength `r-1`.
Consequently

\[
             \deg_{{\cal D}^0}(2)=m-\operatorname {Cat}_{r-1}.
                                                                    \tag{3.8}
\]

Substituting (3.7)--(3.8) into (3.6) says that

\[
                         \operatorname {Cat}_{r-1}\equiv0\pmod2.   \tag{3.9}
\]

But when `r=2^s`, the Catalan number `Cat_{r-1}` is odd.  One direct
verification is

\[
 \operatorname {Cat}_{r-1}={1\over r}\binom{2r-2}{r-1}.
\]

Kummer's theorem gives
`v_2(binomial(2r-2,r-1))=s`, since `r-1` has `s` ones in binary, and
division by `r=2^s` leaves valuation zero.  This contradicts (3.9) and
proves the theorem. `square`

## 4. What the theorems do and do not rule out

The monodromy obstruction applies to the mirroring rule (1.3) for every
even `r`.  The separate parity obstruction applies to the exact combination
of:

1. the fixed canonical Chung--Feller phase classes;
2. complement/time-reversal mirroring of the second half; and
3. exact non-anchor q1 intersection-colour coverage.

The palette obstruction explains the exact palette infeasibility observed
at `r=2,4` and predicts the same at every power of two without computation.
The two theorems do **not** rule out:

- a phase construction without complement mirroring;
- a construction which allows `o(A)` q1 holes rather than exact coverage;
- paths which migrate between the canonical flaw layers;
- endpoint correction by a sparse higher trade; or
- an arbitrary `C_8`-reachable wreath factor.

Indeed, complete small-orbit enumeration shows that physical `C_8` moves
can leave the phase-respecting class.  Therefore Theorems 2.1 and 3.1 are
scope gates for one attractive recursive ansatz, not an asymptotic no-go
for the compiler.

## 5. Checker

The finite audit

```text
scratch/audit_complement_symmetric_dyck_phase_parity_20260821.py
```

reconstructs the canonical layers for `r=2,4,8`, checks complement
duality, (3.7)--(3.8), and the parity contradiction, and checks the Catalan
valuation arithmetically through `r=2^10`.  The computation is an audit;
the proof above is independent of it.
