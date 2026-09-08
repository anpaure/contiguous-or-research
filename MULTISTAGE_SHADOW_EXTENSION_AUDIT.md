# Adversarial audit of `MULTISTAGE_SHADOW_EXTENSION.md`

## 0. Audit verdict

The new note is mathematically sound after the checks recorded below.

Its status is deliberately limited:

* the one-depth clone calculations, forest-capacity ledger, defect identities,
  switch bound, and conditional sufficiency theorem are proved;
* no construction at `H/sqrt(m)->infinity` is proved;
* the positional-clone matching is only a marginal depth-`q` object and is
  not claimed to assemble into a word;
* `D_q` counts duplicate **occurrences**, while `M_q` counts genuinely
  missing target **masks**.  They are not interchangeable.

The most delicate point is the finite-boundary erosion identity in Theorem 7.
It is valid: no cyclic wraparound is silently used.

## 1. Audit of the positional-clone degrees

At depth `q`, a directed geodesic path is specified by

1. its initial middle set `X_0` (`W` choices);
2. an ordered `q`-tuple of distinct removed elements (`(m)_q` choices);
3. an ordered `q`-tuple of distinct inserted elements (`(m)_q` choices).

Therefore

\[
 |E(Q_q)|=W(m)_q^2.                                      \tag{A1.1}
\]

### Target degree

Fix a lower target `L` of rank `m-q`.  Choose the `2q` active elements from
the `m+q` elements outside `L` and put them into the ordered removal and
insertion lists.  Hence

\[
 d(L)=\binom{m+q}{2q}(2q)!=(m+q)_{2q}
     =(m)_q(m+1)_q.                                      \tag{A1.2}
\]

Complementation gives the same upper degree.

### Positional middle degree

Every path has one vertex in each positional class and the symmetric group
is transitive on that class.  Dividing (A1.1) by `W` gives

\[
 d(X^t)=(m)_q^2.                                         \tag{A1.3}
\]

Since

\[
 \rho_q=\frac{N_q}{W}=\frac{(m)_q}{(m+1)_q},             \tag{A1.4}
\]

the degree ratio is exactly `1/rho_q`.

These counts agree with direct exhaustive enumeration for every `m<=4` and
every `q<=m`.

## 2. Audit of all pair codegrees

### Lower--upper pair

For fixed `L subset U`, the `2q` elements of `U-L` may be placed into the two
ordered lists in `(2q)!` ways.  No other choice remains.  Thus

\[
 d(L,U)=(2q)!.                                           \tag{A2.1}
\]

### Target--middle pair

Fix `L subset X` and a position `t`.  Of the `q` elements in `X-L`, choose
which `t` were already inserted.  Choose the complementary active elements
outside `X`, split them according to whether they were removed before `t` or
inserted after `t`, and order both portions.  Cancellation gives

\[
 d(L,X^t)=\binom mq(q!)^2=(m)_q q!,                     \tag{A2.2}
\]

independently of `t`.  The upper case is complementary.

### Two positional middle clones

Let `s<t`, `d=t-s`, and fix middle sets `X,Y`.  Compatibility forces
`d_J(X,Y)=d`.  The fixed segment has `(d!)^2` orders.  The remaining `q-d`
swaps use disjoint common and outside coordinates, giving

\[
 d(X^s,Y^t)=(m-d)_{q-d}^2(d!)^2.                         \tag{A2.3}
\]

If the Johnson distance is not `d`, the codegree is zero.

Dividing by the minimum degree `(m)_q^2` gives exactly

\[
 \frac{(2q)!}{(m)_q^2},\qquad
 \binom mq^{-1},\qquad
 \binom md^{-2}.                                        \tag{A2.4}
\]

For `q=1`, the maximum is `1/m`.  Uniformly for `2<=q=o(m)`, it is
`O(m^-2)`:

* `1/binom(m,q)<=2/(m(m-1))` eventually;
* `1/binom(m,d)^2<=1/m^2` for `1<=d<=q=o(m)`;
* `(2q)!/(m)_q^2=O(m^-2)`.  For `2<=q<=sqrt(m)`, use
  `(2q)!<=(2q)^(2q)` and `(m)_q>=(m-q)^q`; the resulting base is at most
  `3/sqrt(m)` and its exponent is at least four.  For
  `sqrt(m)<q=o(m)` the resulting ratio is superpolynomially small.

Direct enumeration independently reproduced (A2.2)--(A2.3) for all
`m<=4`, all `q<=m`, and all positional pairs.

### What the nibble conclusion does and does not say

For fixed `q`, the degree ratio tends to one, uniformity `q+3` is fixed, and
the pair codegree is `o(D)`.  The ordinary almost-perfect matching theorem
therefore gives `N_q-o(W)` marginal windows.  The slight class-size imbalance
`W-N_q=O_q(W/m)` is itself `o(W)` and is absorbed in the uncovered set.

This does **not** imply shift overlap.  The audit accepts only the marginal
claim.

## 3. Audit of the forest capacity inequalities

Let a spanning linear forest have component sizes `v_1,...,v_c` and
`N_1-e` edges.  A forest on `W` vertices has

\[
 c=W-(N_1-e)=\frac{W}{m+1}+e.                            \tag{A3.1}
\]

The number of internal `q`-transition paths is exactly

\[
 P_q=\sum_i(v_i-q)_+
    =W-\sum_i\min(v_i,q),                                \tag{A3.2}
\]

so

\[
 P_q\ge W-qc.                                           \tag{A3.3}
\]

The needed binomial inequality is

\[
 \rho_q\le1-\frac q{m+1}.                               \tag{A3.4}
\]

It is equality at `q=1`.  Assuming it at `q-1` and multiplying by

\[
 \rho_q/\rho_{q-1}=\frac{m-q+1}{m+q}

\]

reduces the next step to `m+2-q<=m+q`.  Therefore (A3.4) holds for every
`1<=q<=m`.  It was also checked exactly for every `m<=299`.

Combining (A3.1)--(A3.4) gives

\[
 P_q\ge N_q-qe.                                         \tag{A3.5}
\]

This has two important interpretations.

1. The unavoidable Catalan number `W/(m+1)` of forest components is already
   absorbed by the shrinkage of the rank classes.  It is not by itself a
   deeper-slot obstruction.
2. `qe` is only a **capacity** error.  It does not assert that the available
   paths have distinct or even correct-rank shadows.

Summing the possible capacity shortage gives `eH(H+1)/2`.  Thus
`e=o(W/H^2)` is a sufficient rate for this crude count; the note correctly
states that it is not necessary if additional structure recovers slots.

## 4. Actual missing masks versus duplicate occurrences

Discard every non-geodesic depth-`q` path and let `E_q` be the number of
remaining correct-rank occurrences.  For one sign, write

\[
 \mu(S)=\#\{\text{occurrences with value }S\},
\]

\[
 C_q=|\{S:\mu(S)>0\}|,qquad
 M_q=N_q-C_q,                                           \tag{A4.1}
\]

and

\[
 D_q=\sum_S(\mu(S)-1)_+.
\]

Then

\[
 D_q=E_q-C_q=E_q-N_q+M_q,
\]

so

\[
 \boxed{M_q=D_q-(E_q-N_q).}                             \tag{A4.2}
\]

This distinction is essential.

* `M_q` is the number of masks which must still be repaired.
* `D_q` counts all occurrences beyond the first.
* `E_q-N_q` is the unavoidable duplicate baseline when there are more slots
  than targets.

In deep ranks `E_q/N_q` can be large, so `D_q` is necessarily much larger
than `M_q`.  Minimizing `D_q` itself, or using quadratic collision energy,
would reject valid deep coverage.  Only the excess in (A4.2) is the repair
defect.

Likewise, maximum-matching deficiency `kappa_q` in the bipartite shadow graph
is a certificate satisfying

\[
 M_q^-,M_q^+\le\kappa_q,                                 \tag{A4.3}
\]

but it may be strictly larger than both actual missing counts.  The note
correctly labels the matching condition as sufficient and stronger, not as
an equivalence.

## 5. Audit of the finite-component factor and its boundaries

Let one path component be

\[
 T_1,T_2,\ldots,T_v
\]

and let the delay be `H`.  Define its truncated maximal factor

\[
 A_j=\bigcap_{t=\max(1,j-H)}^{\min(v,j)}T_t,qquad
 1\le j\le v+H.                                         \tag{A5.1}
\]

If every internal coordinate `1`-run of `T` has length at least `H+1`, then

\[
 T_i=\bigvee_{s=0}^HA_{i+s}.                             \tag{A5.2}
\]

An `H`-geodesic path has this run property: an internal positive run shorter
than `H+1` would insert and remove the same coordinate within at most `H`
transitions.

For every valid path window `T_a,...,T_(a+q)`, `0<=q<=H`, the two exact
witness formulas are

\[
 \bigcap_{t=a}^{a+q}T_t
   =\bigvee_{s=0}^{H-q}A_{a+q+s},                       \tag{A5.3}
\]

and

\[
 \bigcup_{t=a}^{a+q}T_t
   =\bigvee_{s=0}^{H+q}A_{a+s}.                         \tag{A5.4}
\]

All indices in (A5.3)--(A5.4) lie in `[1,v+H]`, including when `a=1` or
`a+q=v`.  Thus neither identity uses a cyclic seam or a witness from the next
component.

For additional protection against an indexing mistake, (A5.2)--(A5.3) were
exhaustively checked coordinatewise for every binary word of length at most
eight satisfying the run condition, for every `H<=4`, every `q<=H`, and
every valid boundary position.  No exception occurred.  Equation (A5.4)
then follows directly by taking the union of (A5.2) for `i=a,...,a+q`.

## 6. Seam and length accounting in the sufficiency theorem

For component sizes `v_i`, factoring separately costs

\[
 \sum_i(v_i+H)=W+Hc.                                    \tag{A6.1}
\]

No extra seam repair is hidden: witnesses (A5.3)--(A5.4) remain wholly in
their own factor blocks.  Concatenating blocks can create additional OR
values but cannot destroy an existing internal witness.

Under `Hc=o(W)`, (A6.1) is `W+o(W)`.  Append every actually missing central
mask as one literal entry; condition

\[
 \sum_{q<=H}(M_q^-+M_q^+)=o(W)                          \tag{A6.2}
\]

makes this cost `o(W)`.  If the stronger matching condition is used,
(A4.3) implies (A6.2).

For

\[
 H/\sqrt m\to\infty,qquad H=o(m^{2/3}),                 \tag{A6.3}
\]

the independent truncated-ideal construction covers the ranks outside the
central band in `o(W)` further entries.  The central and tail words may be
concatenated because all their old witnesses remain internal.

Some entries in (A5.1) may be empty.  Deleting all empty entries after every
witness has been fixed preserves the OR of every nonempty witness: its
remaining nonempty entries become consecutive.  Therefore zero deletion can
only shorten the result.

The complete length is consequently

\[
 W+Hc+\sum_{q<=H}(M_q^-+M_q^+)+o(W)=W+o(W).             \tag{A6.4}
\]

This proves the conditional implication in Theorem 7 without a cyclic-boundary,
pinning, or seam-cost gap.

## 7. Audit of the negative conclusions

The note does **not** claim that small pair codegree is an impossibility
theorem.  It says only that it solves the wrong marginal object.

The four negative conclusions have separate rigorous bases:

1. **Direct conflicts:** `FIXED_DEPTH_SHADOWS.md` proves the violating
   `Delta_(2q,q)=Omega(D^q)` codegree.
2. **Independent clones:** shift closure is a positive constraint absent
   from the hypergraph; the history-space expectation is explicitly labelled
   a benchmark, not a universal lower bound.
3. **Local switches:** a changed adjacency lies in at most `q` depth-`q`
   windows, giving the exact locality bound for block re-splicings.
4. **Nested Hall/absorption:** with `N_(q-1)` edges on `N_q+N_q` vertices,
   the degree excess is exactly `N_(q-1)-N_q`; hence only that many vertices
   per side can have degree at least two when a perfect matching exists.

Accordingly the final status is correct: the current depth-one theorem has
not been extended to the required growing depth.  The proved contribution is
the exact obstruction ledger and the weaker independent-depth successor
lemma.
