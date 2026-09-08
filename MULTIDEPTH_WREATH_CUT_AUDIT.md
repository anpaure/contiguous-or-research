# Independent audit of `MULTIDEPTH_WREATH_CUT_RESEARCH.md`

## Verdict

The finite combinatorics in the note are correct.  In particular:

* the full-cut and core slot counts are exact;
* both collision ledgers are exact;
* the several-cut amplification bound and its falling-factorial form are
  correct;
* the exponential estimate has the stated sign and denominator;
* the two uniform logarithmic sufficient conditions follow; and
* the fourteen-row `m=4` example is an exact middle wreath factor with a
  rainbow cut at coordinate `9` but with the two stated depth-two colours
  absent globally.

The note proves a new **sufficient reduction**, not a new wreath factor and
not a new unconditional OR-array upper bound.  To invoke the inherited weak
vertical wreath theorem and conclude asymptotic optimality, `H` must still be
chosen in its tail-compatible regime

\[
 H=\sqrt{m\,\omega(m)},\qquad \omega(m)\to\infty,
 \qquad H=o(m^{2/3}).
\]

This condition is implicit through the citation in Section 4, but it should
be restated whenever equation (4.11) is quoted independently.

There are two minor presentation qualifications.

1. A “coordinate cut” has `m+q+1` full slots **per wreath** and
   `(m+q+1)Cat_m` slots across the entire factor.  The opening wording “one
   coordinate cut has ... slots” means the latter aggregate.
2. The supplied verifier prints all decisive `m=4` data, but its process exit
   status checks only middle exactness, first-core exactness, and that at
   least one depth-two pair is missing.  It does not fail when the missing
   pair list differs from the claimed two-element list.  The printed output
   and an independent rerun do verify the proposition; for a standalone
   Boolean certificate, the exit predicate should also assert the row
   permutations and the exact missing-pair list.

## 1. Setup and basic arithmetic

Put

\[
 n=2m+1,\qquad W=\binom{2m+1}{m},\qquad
 B=\frac{W}{2m+1}.
\]

Then

\[
 B=\frac{(2m)!}{m!(m+1)!}
  =\frac1{m+1}\binom{2m}{m}=\operatorname{Cat}_m.
\]

An exact middle wreath factor has `B` cyclic orders and `n` middle
intervals per order, so it has exactly `Bn=W` middle occurrences.

Fix `q` with `1<=q<=m-1` and put `r=m-q`.  After rotating one cyclic order
to

\[
 (z,y_0,\ldots,y_{2m-1}),
\]

an `r`-interval avoids `z` precisely when it is an ordinary interval in the
linear `y`-word.  Its possible starts are

\[
 0\le s\le 2m-r=m+q,
\]

so there are exactly

\[
                        m+q+1
\]

full-cut slots in each wreath and

\[
 K_q=(m+q+1)B
\]

across the factor.  This part uses only that each row is a cyclic order; it
does not use middle exactness.

The number of possible coordinate-free targets is

\[
 A_q=\binom{2m}{m-q}.
\]

The ratio in (3.4) is correct:

\[
 \frac{A_q}{B}
  =(m+1)\frac{\binom{2m}{m-q}}{\binom{2m}{m}}
  =(m+1)\frac{(m)_q}{(m+1)^{\overline q}}.
\]

## 2. Audit of the full-cut collision ledger

Let `h` be the number of absent target colours and let

\[
 e=\sum_S(\mu(S)-1)_+
\]

be total multiplicity beyond the first occurrence of every occupied colour.
The number of occupied colours is `A_q-h`, and hence

\[
 K_q=(A_q-h)+e.
\]

With `Delta_q=K_q-A_q`, rearrangement gives the exact identity

\[
                         h=e-\Delta_q.
\]

Thus the wording “every additional repeat is exactly one hole” is accurate
when “additional” means beyond the unavoidable aggregate excess
`Delta_q`.  The identity does not say which repeated colour causes which
hole, only that the two total counts differ exactly by `Delta_q`.

For fixed `q`, logarithmic expansion of

\[
 \prod_{i=0}^{q-1}\frac{m-i}{m+1+i}
\]

gives

\[
 \frac{A_q}{B}=m+1-q^2+O_q(m^{-1}).
\]

Since `K_q/B=m+q+1`, it follows that

\[
 \frac{\Delta_q}{B}=q(q+1)+O_q(m^{-1}).
\]

The error term is asserted only for fixed `q`; no growing-`q` uniformity is
proved or needed in this section.  At `q=1`, the exact calculation is

\[
 \frac{A_1}{B}=m,qquad \frac{K_1}{B}=m+2,
 \qquad \Delta_1=2B.
\]

## 3. Audit of the nested core

For

\[
 X_i=\{y_i,\ldots,y_{i+m-1}\},\qquad0\le i\le m,
\]

one has, for `q<=s<=m`,

\[
 \bigcap_{i=s-q}^{s}X_i
   =\{y_s,\ldots,y_{s+m-q-1}\}.
\]

The intersection has `m-q` elements and the number of starts is

\[
                         m-q+1.
\]

Therefore

\[
 K_q^\circ=(m-q+1)B.
\]

The full starts range from `0` through `m+q`, while the core starts range
from `q` through `m`; the omitted starts are exactly `q` on each side.  Thus

\[
 K_q=K_q^\circ+2qB.
\]

The claimed inequality `K_q^circ>=A_q` is correct.  If

\[
 a_q=A_q/B,
\]

then

\[
 a_1=m,qquad
 a_{q+1}=a_q\frac{m-q}{m+q+1}.
\]

Inductively, if `a_q<=m-q+1`, then

\[
 a_{q+1}
 \le(m-q+1)\frac{m-q}{m+q+1}
 \le m-q.
\]

This proves the inequality for the full stated range.  Applying the same
occupied-colour count to the core slots yields

\[
 \Delta_q^\circ=K_q^\circ-A_q,
 \qquad
 \Delta_q=\Delta_q^\circ+2qB.
\]

For fixed `q`, subtraction from the preceding expansion gives

\[
 \frac{\Delta_q^\circ}{B}=q(q-1)+O_q(m^{-1}).
\]

At `q=1`, `K_1^circ=A_1=mB`; hence pairwise distinct core colours, full
core coverage, and exact enumeration of the coordinate-free first-shadow
layer are equivalent.  The note's use of “rainbow cut” agrees with the
earlier definition.

## 4. Audit of several-cut amplification

Let `Z_q` be a set of `t=t_q` coordinates whose full coordinate-free
sectors are covered at depth `q`.  If a globally missing target `S` omitted
any `z in Z_q`, it would occur in the covered `z`-free sector.  Every missing
target must therefore contain all of `Z_q`.  There are at most

\[
 \binom{2m+1-t}{m-q-t}
\]

such targets, with value zero for `t>m-q`.  This proves (4.2); it requires no
compatibility between the witnesses supplied by different cuts.

For `t<=m-q`, division by `W` gives

\[
 \frac{\binom{2m+1-t}{m-q-t}}{\binom{2m+1}{m}}
 =\frac{(m)_{q+t}}
       {(m+2)^{\overline q}(2m+1)_t}.
\]

The factorization

\[
 \frac{(m)_t}{(2m+1)_t}
 \frac{(m-t)_q}{(m+2)^{\overline q}}
\]

is exact.  In its first product,

\[
 \frac{m-i}{2m+1-i}\le\frac12.
\]

In its second product,

\[
 \frac{m-t-i}{m+2+i}
 =1-\frac{t+2+2i}{m+2+i}
 \le\exp\!\left(-\frac{t+2+2i}{m+2+i}\right).
\]

Since `m+2+i<=m+q+1`, replacing every denominator by `m+q+1` weakens the
negative exponent in the correct direction.  Moreover,

\[
 \sum_{i=0}^{q-1}(t+2+2i)=q(q+t+1).
\]

Consequently

\[
 \frac{M_q(F)}W
 \le2^{-t_q}
       \exp\!\left(-\frac{q(q+t_q+1)}{m+q+1}\right).
\]

When `t>m-q`, the left side is already zero and the same upper inequality is
trivial; the product proof need only be applied in the nonzero range.

For `1<=q<=m-1`, one has `m+q+1<=2m` and
`q(q+t+1)>=q^2`.  Hence

\[
 \frac{q(q+t+1)}{m+q+1}\ge\frac{q^2}{2m}.
\]

This validates the Gaussian simplification used in Corollary 4.2.

## 5. Audit of the asymptotic sufficient conditions

Summing the preceding pointwise inequality gives

\[
 \frac1W\sum_{q=1}^{H}M_q(F)
 \le
 \sum_{q=1}^{H}2^{-t_q}e^{-q^2/(2m)}.
\]

Thus condition (4.6) is exactly a sufficient condition for the weak defect
sum; it is not claimed or proved necessary.

The first uniform specialization is correct.  If, uniformly for `q<=H`,

\[
 t_q\ge\log_2H+g(m),\qquad g(m)\to\infty,
\]

then the right side is at most `2^{-g(m)}`.

For the Gaussian specialization, the standard integral comparison gives

\[
 \sum_{q\ge1}e^{-q^2/(2m)}=O(\sqrt m).
\]

If, uniformly for `q<=H`,

\[
 t_q\ge\tfrac12\log_2m+g(m),\qquad g(m)\to\infty,
\]

the right side is `O(2^{-g(m)})=o(1)`.  The coordinates are allowed to vary
with `q` because the containment argument is performed separately at each
depth.

To obtain equation (4.11), however, one needs a sequence of exact wreath
factors and a depth cutoff satisfying the inherited tail hypotheses

\[
 H=\sqrt{m\omega(m)},\quad\omega(m)\to\infty,
 \quad H=o(m^{2/3}).
\]

Under those hypotheses, Corollary 4.2 supplies the defect assumption of the
weak vertical wreath lemma; that lemma plus the truncated-tail construction
and the odd/even lift gives

\[
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]

Without an existence theorem for factors carrying the required covering
cuts, this remains conditional.  “Strictly local” should be understood as
local in `(coordinate, depth)` at the level of the certificate.  Covering
one sector is still a global property of all wreaths in the factor, and
finding logarithmically many such sectors at every depth is the unresolved
global design problem.

## 6. Independent audit of the `m=4` certificate

Here

\[
 m=4,\quad n=9,\quad B=\operatorname{Cat}_4=14,
 \quad W=14\cdot9=126.
\]

The fourteen displayed rows are permutations of `[9]`.  Direct enumeration
gives:

1. exactly `126` cyclic length-four occurrences, and each of the
   `binom(9,4)=126` four-sets has multiplicity one;
2. after rotating at coordinate `9`, exactly four first-core triples per
   row, and the resulting `56` occurrences give each of the
   `binom(8,3)=56` triples once;
3. the coordinate-`9` full depth-two slots are the seven adjacent pairs of
   the linear eight-symbol word in each row, and exactly two pairs of `[8]`
   are absent:
   \[
                            \{1,3\},\qquad\{4,6\};
   \]
4. those two pairs are absent even among all cyclic adjacent pairs of all
   fourteen rows, not merely from the coordinate-`9` full slots.

The supplied C++ verifier was compiled with `-O3` and rerun independently on
the remote Linux worker.  It reproduced exactly

```text
middle_bad=0 first_core_bad=0 full1_missing=1 core2_missing=2 cut_depth2_missing=2 global_depth2_missing=2
0 2
3 5
cut_distinct: 51 45 44 47 44 44 43 44 56
```

The zero-based pairs `0 2` and `3 5` are the stated one-based pairs.  The
final `56` shows that coordinate `9` is rainbow, while every other entry is
strictly below `56` and hence every other coordinate cut is non-rainbow.

The verifier's internal indexing agrees with the mathematical core:

* first-core starts are array positions `2,...,5`, corresponding to
  `y_1,...,y_4`;
* second-core starts are positions `3,...,5`, corresponding to
  `y_2,...,y_4`; and
* filtering cyclic pairs to masks not containing bit `8` leaves exactly the
  seven full coordinate-`9` depth-two slots per row.

The only certificate-engineering weakness is the return statement

```cpp
return badmid || badcore || missing.empty();
```

which does not itself assert `missing.size()==2` or the identities of the
two missing pairs.  The program nevertheless prints those values, and the
enumerated data verify the proposition.  A proof-certificate version should
make all printed decisive conditions part of its exit predicate.

## 7. Exact logical status

| Statement | Status | Qualification |
|---|---|---|
| Full coordinate-cut slot count | proved | `m+q+1` per wreath, `(m+q+1)B` across the factor. |
| Full collision ledger | proved exactly | Aggregate identity; no pointwise pairing of repeats with holes. |
| Fixed-`q` asymptotic expansions | proved | Not uniform for growing `q`. |
| Core slot count and core ledger | proved exactly | Core coverage is stronger than the full-cut coverage used later. |
| Several-cut binomial bound | proved exactly | Missing targets must contain every covering coordinate. |
| Falling-factorial identity and exponential bound | proved exactly | Product proof applies directly for `t<=m-q`; larger `t` gives zero defect. |
| Weighted multiscale condition implies `sum M_q=o(W)` | proved | Sufficient, not necessary. |
| Half-logarithmic cuts at every controlled depth suffice | proved conditionally | Uniform additive `omega(1)` is required. |
| Such exact factors exist asymptotically | open | This note provides no construction or existence proof. |
| Asymptotic OR optimality follows | conditional | Also requires the inherited admissible growth regime for `H`. |
| One rainbow cut propagates automatically to depth two | false | Refuted by the certified `m=4` factor. |
| Many rainbow first cuts force deeper coverage | open | The one-cut example does not address interacting cuts. |

## 8. Safe handoff statement

The result can safely be reused as follows.

> For an exact middle wreath factor on `2m+1` coordinates, if `t_q`
> coordinates cover their entire coordinate-free depth-`q` sectors, then
> \[
>   \frac{M_q}{\binom{2m+1}{m}}
>   \le2^{-t_q}
>      \exp\!\left(-\frac{q(q+t_q+1)}{m+q+1}\right)
>   \le2^{-t_q}e^{-q^2/(2m)}.
> \]
> Therefore, for a tail-compatible cutoff `H`, the condition
> \[
>   \sum_{q\le H}2^{-t_q}e^{-q^2/(2m)}=o(1)
> \]
> is a sufficient local certificate for the weak vertical wreath lemma and
> hence for asymptotically width-optimal OR arrays.  Existence of exact
> factors carrying these cuts is the remaining theorem.

> A single depth-one rainbow cut does not imply depth-two coverage: the
> explicit fourteen-wreath factor on nine coordinates has a rainbow cut at
> coordinate `9`, while `{1,3}` and `{4,6}` are absent from every cyclic
> length-two interval.

