# Multidepth coordinate cuts for exact wreath factors

## 1. Outcome

This note gives an exact depth-by-depth version of the coordinate-cut
argument from `WREATH_FIRST_SHADOW_RESEARCH.md`.

There are three conclusions.

1. At depth `q`, one coordinate cut has exactly

   \[
      (m+q+1)\operatorname {Cat}_m
   \]

   slots avoiding the cut coordinate.  The excess over the number of
   possible colours is explicit, and every additional repeated occurrence
   beyond this forced excess is exactly one missing colour.
2. If `t_q` coordinates cover their coordinate-free sectors at depth `q`,
   then

   \[
      \frac{M_q}{W}
      \leq 2^{-t_q}
         \exp\!\left(-\frac{q(q+t_q+1)}{m+q+1}\right).
   \]

   Consequently the weak multiscale wreath lemma follows from the strictly
   local condition

   \[
      \sum_{q\leq H}2^{-t_q}e^{-q^2/(2m)}=o(1).
   \]

   The covering coordinates may be different at different depths.  In
   particular, only

   \[
      \tfrac12\log_2m+\omega(1)
   \]

   covering cuts at every controlled depth are sufficient.
3. A rainbow cut at depth one does **not** automatically cover depth two.
   A fourteen-wreath certificate on nine coordinates has an exact middle
   factor and a rainbow cut at coordinate `9`, but the two depth-two colours
   `{1,3}` and `{4,6}` never occur in any wreath.

Thus the first-shadow program does not propagate for free.  The remaining
multiscale gate is sharply narrowed to obtaining logarithmically many
covering coordinate sectors at each relevant depth (or satisfying the
weighted variant above).

## 2. Setup

Put

\[
 n=2m+1,\qquad
 W=\binom nm,\qquad
 B=\frac Wn=\operatorname {Cat}_m.
\tag{2.1}
\]

Let `F` be an exact middle wreath factor: it consists of `B` cyclic orders,
and their cyclic intervals of length `m` partition
\(\binom{[n]}m\).

Fix

\[
 1\le q\le m-1,\qquad r=m-q.
\tag{2.2}
\]

For a coordinate `z`, rotate a wreath order to the form

\[
 \pi=(z,y_0,y_1,\ldots,y_{2m-1}).
\tag{2.3}
\]

The cyclic `r`-intervals which avoid `z` are precisely the ordinary linear
intervals

\[
 A_{s,q}(\pi,z)=\{y_s,y_{s+1},\ldots,y_{s+r-1}\},
 \qquad 0\le s\le m+q.
\tag{2.4}
\]

Call these the **full depth-`q` cut slots**.

## 3. Exact slot and collision ledger

For an `r`-set \(S\subseteq[n]\setminus\{z\}\), define

\[
 \mu_{z,q}(S)
 =\#\{(\pi,s):\pi\in F,\ A_{s,q}(\pi,z)=S\}.
\tag{3.1}
\]

Let

\[
 h_{z,q}=\#\{S:\mu_{z,q}(S)=0\},
 \qquad
 e_{z,q}=\sum_S(\mu_{z,q}(S)-1)_+.
\tag{3.2}
\]

### Theorem 3.1 (full-cut ledger)

For every exact wreath factor, coordinate `z`, and
\(1\le q\le m-1\),

\[
 \boxed{
 h_{z,q}=e_{z,q}-\Delta_q
 }
\tag{3.3}
\]

where

\[
 \begin{aligned}
 K_q&=(m+q+1)B,\\
 A_q&=\binom{2m}{m-q}
     =B(m+1)\frac{(m)_q}{(m+1)^{\overline q}},\\
 \Delta_q&=K_q-A_q.
 \end{aligned}
\tag{3.4}
\]

Here `(a)_q` is a falling factorial and
\(a^{\overline q}\) is a rising factorial.

In particular, the `z`-free sector is completely covered at depth `q` if
and only if

\[
 e_{z,q}=\Delta_q.
\tag{3.5}
\]

Thus \(\Delta_q\) is the unavoidable overlap, and every unit of overlap
beyond \(\Delta_q\) is exactly one hole.

#### Proof

There are `m+q+1` linear intervals in (2.4) in each of the `B` wreaths, so
there are `K_q` occurrence slots.  There are `A_q` possible `z`-free
targets.  The occupied colours contribute one occurrence apiece and all
further occurrences contribute `e_{z,q}`.  Therefore

\[
 K_q=(A_q-h_{z,q})+e_{z,q},
\]

which is (3.3).  The binomial ratio in (3.4) follows from

\[
 \frac{\binom{2m}{m-q}}{\binom{2m}{m}}
 =\frac{(m)_q}{(m+1)^{\overline q}},
 \qquad
 B=\frac1{m+1}\binom{2m}{m}.
\]

This proves the theorem.  \(\square\)

For fixed `q`, expansion of (3.4) gives

\[
 \frac{A_q}{B}=m+1-q^2+O_q(m^{-1}),
 \qquad
 \frac{\Delta_q}{B}=q(q+1)+O_q(m^{-1}).
\tag{3.6}
\]

The familiar first cut has two forced extra slots per wreath:

\[
 \Delta_1=2B.
\tag{3.7}
\]

### The nested core slots

The complementary middle path at the cut is

\[
 X_i=\{y_i,\ldots,y_{i+m-1}\},\qquad 0\le i\le m.
\tag{3.8}
\]

For `q>=1`, intersections of `q+1` consecutive vertices of this path are

\[
 \bigcap_{i=s-q}^{s}X_i
 =\{y_s,\ldots,y_{s+m-q-1}\},
 \qquad q\le s\le m.
\tag{3.9}
\]

Call these the **core depth-`q` slots**.  There are

\[
 K_q^\circ=(m-q+1)B
\tag{3.10}
\]

of them.  The remaining full-cut slots form two fringes with `q` slots on
each side, so

\[
 K_q=K_q^\circ+2qB.
\tag{3.11}
\]

The core count is at least `A_q`.  This follows inductively from

\[
 \frac{A_1}{B}=m,
 \qquad
 \frac{A_{q+1}}B=\frac{A_q}B\frac{m-q}{m+q+1}.
\tag{3.12}
\]

Applying the same occurrence count as in Theorem 3.1 gives a core ledger
with unavoidable excess

\[
 \Delta_q^\circ=K_q^\circ-A_q,
 \qquad
 \Delta_q=\Delta_q^\circ+2qB.
\tag{3.13}
\]

For fixed `q`,

\[
 \frac{\Delta_q^\circ}{B}=q(q-1)+O_q(m^{-1}).
\tag{3.14}
\]

At `q=1`, the core has exactly as many slots as targets.  Consequently a
depth-one rainbow cut is exactly the statement that its core slots cover
the entire coordinate-free first shadow.  At greater depth, even a perfect
core cover necessarily has repeated colours.

## 4. Amplification by several covering cuts

Call `z` a **depth-`q` covering coordinate** if

\[
 h_{z,q}=0.
\tag{4.1}
\]

Core coverage is a stronger sufficient condition, but full-cut coverage is
all that is needed below.

### Theorem 4.1 (multidepth cut amplification)

Suppose `Z_q` is a set of `t_q` depth-`q` covering coordinates.  Then

\[
 \boxed{
 M_q(F)\le
 \binom{2m+1-t_q}{m-q-t_q}
 }
\tag{4.2}
\]

with the usual value zero when \(t_q>m-q\).  More precisely,

\[
 \boxed{
 \frac{M_q(F)}W
 \le
 \frac{(m)_{q+t_q}}
 {(m+2)^{\overline q}(2m+1)_{t_q}}
 \le
 2^{-t_q}
 \exp\!\left(-\frac{q(q+t_q+1)}{m+q+1}\right).
 }
\tag{4.3}
\]

#### Proof

If a missing depth-`q` target `S` avoided some \(z\in Z_q\), the covering
property at `z` would represent it.  Therefore every missing target contains
all of `Z_q`, proving (4.2).

Dividing (4.2) by `W` gives

\[
 \frac{\binom{2m+1-t}{m-q-t}}{\binom{2m+1}m}
 =\frac{(m)_{q+t}}
 {(m+2)^{\overline q}(2m+1)_t}.
\tag{4.4}
\]

Split its right side as

\[
 \frac{(m)_t}{(2m+1)_t}
 \frac{(m-t)_q}{(m+2)^{\overline q}}.
\tag{4.5}
\]

Every factor in the first product is at most `1/2`.  In the second product,

\[
 \frac{m-t-i}{m+2+i}
 =1-\frac{t+2+2i}{m+2+i}
 \le \exp\!\left(-\frac{t+2+2i}{m+2+i}\right).
\]

Since \(m+2+i\le m+q+1\), summing the numerators for
\(0\le i<q\) gives

\[
 \sum_{i=0}^{q-1}(t+2+2i)=q(q+t+1).
\]

This proves (4.3).  \(\square\)

### Corollary 4.2 (a sufficient multiscale cut theorem)

If, for \(1\le q\le H\), the factor has `t_q` depth-`q` covering
coordinates and

\[
 \boxed{
 \sum_{q=1}^H
 2^{-t_q}\exp\!\left(-\frac{q^2}{2m}\right)=o(1),
 }
\tag{4.6}
\]

then

\[
 \sum_{q=1}^H M_q(F)=o(W).
\tag{4.7}
\]

Indeed, for `q<=m-1`, (4.3) is at most
\(2^{-t_q}e^{-q^2/(2m)}\).

Two useful uniform special cases are:

\[
 t_q\ge \log_2H+\omega(1)\qquad(1\le q\le H),
\tag{4.8}
\]

and the sharper Gaussian form

\[
 t_q\ge \tfrac12\log_2m+\omega(1)\qquad(1\le q\le H).
\tag{4.9}
\]

For (4.9), use

\[
 \sum_{q\ge1}e^{-q^2/(2m)}=O(\sqrt m).
\tag{4.10}
\]

The sets `Z_q` need not agree as `q` changes.  This is materially weaker
than finding one growing coordinate set which is simultaneously perfect at
all depths.

Combined with Theorem 3.1 of
`GLOBAL_MTF_ATOM_ROUNDING_FINAL_AUDIT.md`, Corollary 4.2 is sufficient for

\[
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{4.11}
\]

Here this implication uses the tail-compatible inherited scale

\[
 H=\sqrt{m\,\omega(m)},\qquad \omega(m)\longrightarrow\infty,
 \qquad H=o(m^{2/3}).
\tag{4.12}
\]

Corollary 4.2 by itself is only a sufficient estimate on the controlled
depths; it is not an existence theorem for such wreath factors.

## 5. First-shadow rainbows do not propagate

Under a rainbow cut at `z`, the first core rows

\[
 P_i=\{y_i,\ldots,y_{i+m-2}\},\qquad 1\le i\le m,
\tag{5.1}
\]

over all wreaths enumerate every member of
\(\binom{[n]\setminus\{z\}}{m-1}\) exactly once.  The depth-`q` core
colour is

\[
 P_{s-q+1}\cap\cdots\cap P_s.
\tag{5.2}
\]

Thus depth one fixes the vertices of a path cover, while deeper coverage is
a new consecutive-intersection colour condition on its edges and longer
windows.  It is not a formal consequence of the vertex enumeration.

The following exact factor gives a concrete separation already at depth
two.  Each row is a cyclic order on `[9]`; coordinate `9` is written first.

```text
9 1 2 3 4 5 6 7 8
9 1 2 7 3 5 6 8 4
9 1 4 7 8 5 2 3 6
9 1 6 2 4 5 8 3 7
9 1 8 6 2 5 7 4 3
9 2 3 7 4 1 6 5 8
9 2 4 3 8 1 7 5 6
9 2 4 8 6 1 7 3 5
9 3 8 6 7 4 2 1 5
9 4 3 6 7 2 8 1 5
9 4 7 8 3 2 1 5 6
9 4 8 3 6 1 2 7 5
9 6 3 5 1 8 4 2 7
9 7 5 1 4 3 6 2 8
```

### Proposition 5.1 (finite non-propagation certificate)

The fourteen rows above have all three properties:

1. their `14*9=126` cyclic intervals of length four are the `126`
   four-subsets of `[9]`, each exactly once;
2. after cutting at `9`, their `14*4=56` core intervals of length three
   are the `56` triples of `[8]`, each exactly once, so `9` is a rainbow
   depth-one cut;
3. neither `{1,3}` nor `{4,6}` occurs as a cyclic interval of length two in
   any row.

Hence a depth-one rainbow coordinate need not even be a depth-two covering
coordinate.

#### Verification

Items 1 and 2 are finite equality checks between two collections having the
same stated cardinality.  Item 3 can be read directly from the rows: neither
pair ever appears consecutively, including across a cyclic seam.  An
independent verifier is

`scratch/verify_m4_rainbow_not_depth2.cpp`.

Its decisive output is

```text
middle_bad=0 first_core_bad=0 full1_missing=1 core2_missing=2 cut_depth2_missing=2 global_depth2_missing=2
0 2
3 5
cut_distinct: 51 45 44 47 44 44 43 44 56
```

The two displayed missing pairs are zero-based versions of `{1,3}` and
`{4,6}`.  The final `56` belongs to cut coordinate `9`; all other cuts are
non-rainbow.

The proposition depends only on the displayed table and these finite checks,
not on the method by which the table was discovered.

This proposition refutes automatic one-cut propagation.  It does **not**
rule out a new theorem saying that many simultaneous first-shadow rainbow
cuts force partial deeper coverage.  Any such theorem must use interaction
between the cuts, since one cut alone contains insufficient information.

## 6. Exact remaining target

The weak multiscale wreath lemma can now be replaced by the following
stronger but sharply local sufficient target.

> **Logarithmic multidepth cut target.**  Construct exact middle wreath
> factors such that, for each `q<=H`, there are `t_q` coordinates whose
> `z`-free depth-`q` sectors are covered, with
> \[
>    \sum_{q\le H}2^{-t_q}e^{-q^2/(2m)}=o(1).
> \]

Core coverage via the consecutive intersections (3.9) is a convenient
certificate, but the weaker full-cut coverage is enough.  A uniform
\(\frac12\log_2m+\omega(1)\) covering coordinates at each depth suffices,
and the coordinates may vary with depth.

The finite certificate proves why an all-depth argument must be present:
perfect first-shadow vertex enumeration by itself leaves the deeper edge
and window colours uncontrolled.
