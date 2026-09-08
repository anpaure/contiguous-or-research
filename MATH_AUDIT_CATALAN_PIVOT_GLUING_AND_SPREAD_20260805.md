# Independent audit of Catalan pivot gluing and its spread frontier

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Audited sources:**

* `MATH_THEOREM_CATALAN_SCALE_PIVOT_TRACE_FACTOR_GLUING_20260805.md`;
* `MATH_THEOREM_FULLY_FLAGGABLE_OVERLAPPING_CORE_PIVOT_BRIDGE_20260805.md`.

**Verdict:** `GO AFTER TWO SCOPE CORRECTIONS`.  The owner geodesic, trace
concatenation, maximal-matching supply, even and odd Catalan constants, and
upper/lower witness transport are exact.  The overlapping-core suffix deck
is also exact.  Two corrections were required:

1. the overlapping-core construction needs `|Q|=r-h>=2`, not merely
   `h<r`, because it chooses distinct `a,b in Q`;
2. the inequality called the lower-slot charge is necessary and sufficient
   only inside the deliberately restricted owner-ending suffix bank.  For
   the full source word it is a stronger sufficient inequality, since it
   discards the initial triangular cells.

Both source files have been patched accordingly.  No conclusion asserting
`B(k)+1`, `B(k)+O(1)`, or a protected factor on the complementary owners is
justified by these local theorems.

## 1. Pivot-window audit

For the basic pivot choose disjoint

\[
 |Q|=r-h,\qquad
 \lambda_1,\ldots,\lambda_h,\qquad
 \rho_1,\ldots,\rho_h.
\]

Both the singleton-rail and overlapping-core realizations traverse the
same windows

\[
 M_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
       \cup\{\rho_1,\ldots,\rho_j\},\qquad0\le j\le h.
\tag{1.1}
\]

Consequently

\[
 |M_j|=r,qquad
 M_{j+1}=M_j-\{\lambda_{j+1}\}+\{\rho_{j+1}\}.
\tag{1.2}
\]

The windows are distinct, form an induced Johnson geodesic, and consume
exactly `h+1` owner colours.  Appending the pivot letter followed by the
`h` right-state letters leaves exactly the prescribed right state in the
order-`h` memory.  Thus there is no hidden owner or source-position charge.

For `c` trace components, the `c-1` bridges contribute
`(h+1)(c-1)` owners.  If the component and bridge owner sets partition the
rank-`r` layer, their total is exactly `W`, so the concatenated source has
exactly `W+h` letters.  This verifies the owner accounting in the gluing
theorem.

## 2. Overlapping-core suffix audit

Assume `r-h>=2`, choose distinct `a,b in Q`, and put

\[
 C=Q-\{a\},\qquad X=Q-\{b\},\qquad
 U_i=C\cup\{\lambda_i\},\quad V_i=C\cup\{\rho_i\}.
\tag{2.1}
\]

Because `C union X=Q`, (1.1) is unchanged.  The proper suffixes are:

* at `j=0`, the exceptional value `X`, followed by

  \[
  Q\cup\{\lambda_{h-\ell+2},\ldots,\lambda_h\},
                 \qquad2\le\ell\le h;
  \tag{2.2}
  \]

* at `1<=j<=h`, before the pivot letter enters,

  \[
  C\cup\{\rho_{j-\ell+1},\ldots,\rho_j\},
                 \qquad1\le\ell\le j;
  \tag{2.3}
  \]

* after the pivot letter enters,

  \[
  Q\cup\{\rho_1,\ldots,\rho_j\}
   \cup\{\lambda_{h-\ell+j+2},\ldots,\lambda_h\},
                 \qquad j+1\le\ell\le h.
  \tag{2.4}
  \]

These values are pairwise distinct.  The exceptional value contains `a`
but not `b`; (2.3) contains `b` but not `a`; and (2.2),(2.4) contain all of
`Q`.  Inside (2.3), the rho interval recovers `(j,ell)`.  Inside the
`Q`-containing family, the rho prefix recovers `j` and the lambda-tail
length recovers `ell`.

Their exact rank histogram is

\[
 1\text{ at }r-h-1,\qquad
 h\text{ at }r-h,\qquad
 h+1\text{ at every }r-h+1,\ldots,r-1.
\tag{2.5}
\]

The total is `1+h+(h-1)(h+1)=h(h+1)`.  Hence every proper suffix cell of
every bridge owner is strict and no two such cells collide *inside one
bridge*.  The local raw bridge charge is therefore zero.  This does not say
that the decks of different bridges, or a bridge deck and a component
deck, are target-disjoint.

## 3. Upper and lower preservation audit

A literal component flag is a proper suffix union of its exact source
window.  Concatenation changes neither that window nor its letters, so the
flag survives literally.  The same statement applies to any selected
natural bridge flag.

If upper target `Z` has an internal component witness

\[
 Z=T_a\cup T_{a+1}\cup\cdots\cup T_b,
\]

then, writing `T_i=A_i union ... union A_(i+h)`, associativity gives

\[
 Z=A_a\cup A_{a+1}\cup\cdots\cup A_{b+h}.
\tag{3.1}
\]

The component remains contiguous after gluing, so (3.1) survives.  Thus the
strong internal-upper convention is sufficient.  It is deliberately
strong: no theorem here creates such internal witnesses.

## 4. Exact bridge-hypergraph degree and codegrees

Let `H_piv` be the simple `(h+1)`-uniform hypergraph on the rank-`r` layer
whose edges are the owner sets (1.1).  Put `s=h+1` and use falling
factorials `(x)_j=x(x-1)...(x-j+1)`.  Oriented geodesics are obtained by
ordering `h` deleted coordinates and `h` inserted coordinates.  Reversal
is the only second orientation of the same induced path.  Therefore

\[
 |E(H_{piv})|={W(r)_h(k-r)_h\over2},
 \qquad
 \Delta={s(r)_h(k-r)_h\over2}.
\tag{4.1}
\]

Let `T,T'` be rank-`r` owners at Johnson distance `ell`.  If `ell>h`, no
pivot edge contains both.  If `1<=ell<=h`, the exact pair-codegree is

\[
 \lambda_\ell
  =(h-\ell+1)(\ell!)^2
       (r-\ell)_{h-\ell}(k-r-\ell)_{h-\ell}.
\tag{4.2}
\]

Indeed, orient each unoriented path uniquely so that `T` precedes `T'`.
Choose the position of `T` in `h-ell+1` ways, order the `ell` forced
deletions and insertions independently, and fill the remaining pre- and
post-segment positions from the common and exterior coordinates.  Every
unoriented path containing the pair is then counted exactly once.

Dividing by (4.1) gives

\[
 {\lambda_\ell\over\Delta}
 = {2(h-\ell+1)\over h+1}
   {1\over {r\choose\ell}{k-r\choose\ell}}.
\tag{4.3}
\]

In the central regime, the maximum occurs at `ell=1`, and

\[
 {\Delta_2(H_{piv})\over\Delta}
 \le {2\over r(k-r)}=O(r^{-2}).
\tag{4.4}
\]

More generally, any `t` distinct owners lying in one pivot edge occupy
positions whose extremes have distance at least `t-1`.  Hence, for fixed
`t>=2`,

\[
 {\Delta_t(H_{piv})\over\Delta}
 \le {2\over {r\choose t-1}{k-r\choose t-1}}.
\tag{4.5}
\]

These are much stronger local-spread estimates than the maximal-matching
argument uses.

## 5. An unconditional prescribed-bank avoidance theorem

### Theorem 5.1

Let `D` be any prescribed set of `f` rank-`r` owners.  The pivot hypergraph
induced on the complement of `D` contains an owner-disjoint bridge family
of size at least

\[
                 {W\over s^2}-{f\over s}.
\tag{5.1}
\]

#### Proof

Each forbidden owner lies in exactly `Delta` pivot edges, so at most
`f Delta` edges meet `D`.  By (4.1), the induced hypergraph has at least

\[
 |E|-f\Delta=\Delta(W/s-f)
\]

edges and maximum degree at most `Delta`.  A maximal matching of size `m`
dominates every induced edge.  The `s` stars through one selected edge
contain at most `s Delta` edges, whence

\[
 \Delta(W/s-f)\le ms\Delta.
\]

This is (5.1). `square`

For even `k=2r`, this still supplies at least `W/(r+1)` bridges whenever

\[
 f\le W\left({1\over s}-{s\over r+1}\right).
\tag{5.2}
\]

Since `s/sqrt(r) -> sqrt(pi)/2<1`, the right side of (5.2) is
`Theta(W/sqrt(r))`.  The odd Catalan target has still more room.  Thus the
bridge bank can avoid any independently prescribed polynomial-size collar,
damage set, or owner socket bank.  This does not let it avoid the almost
entire owner set of a separately completed factor.

## 6. A proof-safe spread route, and its remaining black box

Sample owners independently with

\[
 p=c_0h/r,
\tag{6.1}
\]

where `c_0>1` is fixed.  For every lower set `S` of rank at most
`r-h-1`, its containment star has size at least

\[
 {k-r+h+1\choose h+1}
   =\exp(\Theta(\sqrt r\log r))
\tag{6.2}
\]

in the central regime.  Chernoff's inequality followed by a union bound
over all at most `2^k` targets proves that, with positive probability, all
these stars retain `(1+o(1))p` of their owners simultaneously.  This part
is unconditional.

For a fixed owner, the expected degree of the induced pivot hypergraph is

\[
                 \Delta p^{s-1}.
\tag{6.3}

For a pair of owners its expected codegree-to-degree ratio is bounded by

\[
 {1\over p}{\Delta_2\over\Delta}=O(r^{-3/2}),
 \qquad
 s^2{1\over p}{\Delta_2\over\Delta}=O(r^{-1/2}).
\tag{6.4}

The higher ratios obtained from (4.5) decay still faster.  A
**growing-uniformity nibble theorem** asserting an almost-perfect matching
under the concentrated versions of (6.3)--(6.4) would produce

\[
 (1-o(1)){pW\over s}=(c_0-o(1)){W\over r}
\]

owner-disjoint bridges while inheriting the simultaneous containment-star
spread.  Taking `c_0>1` would cover both Catalan targets.

The usual fixed-uniformity Pippenger--Spencer theorem cannot be cited
verbatim here because `s=Theta(sqrt(r))` grows.  Nor do (4.3)--(4.5) alone
prove uniform concentration of every induced degree.  Therefore this note
records (6.1)--(6.4) as a sharply quantified route, **not** as an
unconditional spread matching theorem.  A quantitative growing-rank nibble
or a direct isolated-bite proof remains required.

## 7. Exact frontier after the audit

The unconditional gains are:

1. correct zero-length pivot gluing;
2. a locally fully flaggable bridge with exact lower-central histogram;
3. exact owner hypergraph degrees and all fixed-order codegree bounds;
4. Catalan-scale bridge avoidance of any prescribed
   `O(W/sqrt(r))` owner bank.

The unresolved correlated theorem still has two parts:

* select Catalan-many modules whose owner banks **and natural suffix decks**
  are mutually disjoint and sufficiently spread for the named MLD forest;
* construct the internally upper-complete protected trace factor on the
  complementary resources with exactly the exposed rail states.

Separate scalar abundance, the owner-only matching, and local bridge
flagability do not imply that joint statement.
