# Unrestricted Cylinder Completion by Sublinear Dimension Extension

Date: 2026-09-05. The compact self-contained proof is incorporated in
`MASTER_HANDOFF.md`, Sections 3.9 and I.7. This expanded note is supplemental.

Status: proved exact construction and asymptotic almost-cover equivalence.
No near-width almost-cover family is asserted to exist. This route uses no
punctured Gate A/B, coherent-tour Gate C, or new matching theorem.

## 1. Main Result

Let a nonzero cyclic set-word on `[k]`, `k>=1`, have period `m` and miss
`h` of the nonempty subsets under literal cyclic interval union. Then, for
every integer `t>=0`,

\[
 \boxed{\nu(k+t)\le 2^t\{m+(k-2)_+\}+h\{\nu(t)+1\}.}       \tag{1}
\]

For a nonempty linear base word of length `n>=1`, replace the braces in the
first term by `n` and count its linear, not cyclic, holes. A sharper cyclic first term
uses the actual normalization length, at most

\[
 m+\max(0,|U|-\max_i|A_i|-1),\qquad U=\bigcup_i A_i.
\]

In particular, suppose for every sufficiently large `k` there is a cyclic
word with

\[
 m_k\le(1+\varepsilon_k)W(k),\qquad
 h_k=\eta_k2^k,\qquad \varepsilon_k,\eta_k\ge0,\qquad
 \varepsilon_k,\eta_k\longrightarrow0.
                                                               \tag{2}
\]

Then `nu(K)=(1+o(1))W(K)` for all dimensions `K`. Thus an unrestricted
near-width word covering a `1-o(1)` fraction of the entire cube suffices.
The holes need not total `o(W(k))`, need not be rank-balanced, and may
include whole central ranks.

Conversely, the desired asymptotic theorem supplies such cyclic words by
closing its universal linear words, with no holes. Therefore (2) is an
equivalent asymptotic existence criterion, not just a necessary condition.

For one base dimension with `0<=epsilon<=1` and `eta=o(1)`, take

\[
 t=\left\lceil k\eta^{2/3}+\sqrt{k}\right\rceil.
\]

The resulting universal word satisfies the quantitative estimate

\[
 \boxed{\frac{\nu(k+t)}{W(k+t)}
 \le 1+O\!\left(\varepsilon+\eta^{2/3}+k^{-1/2}\right).}     \tag{3}
\]

In particular, `h_k=O(W(k))` is sufficient with `t=Theta(k^(2/3))`
(choosing that value even when there are fewer holes) and relative error
`O(epsilon_k+k^(-1/3))`. More generally, `h_k=O(k^alpha W(k))`, for fixed
`0<=alpha<1/2`, permits
`t=Theta(k^((2alpha+2)/3))` and relative error
`O(epsilon_k+k^((2alpha-1)/3))`.

## 2. Exact Literal-OR Construction

### Partial top-bit lift

For any nonzero linear word `A=(A_1,...,A_n)` and a fresh coordinate `z`,
write

\[
 L_z(A)=(A_1,\ldots,A_n,\{z\},
               A_1\cup\{z\},\ldots,A_{n-1}\cup\{z\}).       \tag{4}
\]

Its length is exactly `2n`. If `T` has old witness `[i,j]`, then `T` still
has that witness. If `j<n`, the lifted copy of `[i,j]` realizes `T union
{z}`. If `j=n`, the old suffix `[i,n]` followed by the bridge `{z}` realizes
it. The bridge itself realizes `{z}`. Universality of the old word was
never used.

After `t` such lifts, the length is exactly `2^t n`. Every target
`T union Z`, for `T` an old realized nonempty target and `Z` any subset of
the new coordinate set `Q`, is covered. So is every nonempty subset of
`Q`. This follows by induction, including the new-coordinate-only targets.

### One missing fiber

Let `B=(B_1,...,B_v)` be universal on `Q`, with `v=nu(t)`, and let `T` be
one missing nonempty old target. Append the block

\[
 (T,\ T\cup B_1,\ldots,T\cup B_v).                       \tag{5}
\]

The first letter realizes `T`. For nonempty `Z subseteq Q`, an interval
`[i,j]` witnessing `Z` in `B` gives the literal equality

\[
 \bigcup_{p=i}^j(T\cup B_p)=T\cup\bigcup_{p=i}^jB_p=T\cup Z.
\]

All letters of (5) are nonempty, including when `t=0`, when the block is
just `(T)`. No witness used in this proof crosses a join between appended
blocks. Each missing fiber therefore costs exactly `nu(t)+1` positions.
This is also the minimum length of an isolated word covering the entire
fiber: projection onto `Q` would otherwise be a word shorter than `N(t)`
covering every subset of `Q`, including the empty set. The zero theorem
gives `N(t)=nu(t)+1`. This optimality concerns one isolated fiber, not
globally shared repairs of several fibers.

For a cyclic base, first use the handoff's cyclic normalization. For
completeness, cut immediately after a largest letter `Z`, and scan the
rotated period, recording nonempty fresh-coordinate blocks outside `Z` as
`C_1,...,C_q`. Append only `C_1,...,C_(q-1)`. A proper wrapping target is an
old suffix, which contains `Z`, plus a prefix whose fresh coordinates are
an initial segment of these blocks. If it needs all `q` blocks it is the
full support `U`, already witnessed by the period. Otherwise its suffix
and the appended initial blocks are a literal witness. Hence every old
cyclic target is retained, with the length bound above. Normalization can
create additional targets; counting the original cyclic holes only
overestimates the repair cost. Now (4) and (5) prove (1).

## 3. Asymptotic Accounting

Only the already proved unconditional estimate is used for the repair word:

\[
 \nu(t)+1=O(2^t/\sqrt t),\qquad t\longrightarrow\infty.
\]

Together with `W(k)=2^k sqrt(2/(pi k))(1+O(1/k))`, formula (1) gives, for
`t=o(k)` and `t->infinity`,

\[
 \frac{2^t(m+O(k))}{W(k+t)}
 \le (1+\varepsilon)\sqrt{1+t/k}(1+O(1/k))
      +O(k^{3/2}2^{-k}),
\]

\[
 \frac{h(\nu(t)+1)}{W(k+t)}
 =O\!\left(\eta\sqrt{\frac{k+t}{t}}\right).
\]

For the choice in (3), `t/k=O(eta^(2/3)+k^(-1/2))` and
`eta sqrt(k/t)<=eta^(2/3)`, with the latter expression zero if `eta=0`.
This proves (3). In particular the exponential duplication factor is
fully counted: it is canceled by the corresponding `2^t` in `W(k+t)`,
leaving the nontrivial dimension penalty `sqrt(1+t/k)`.

There is no missing interpolation assumption in (2). For a desired large
`K`, let

\[
 d_K=\sup_{j\ge\lfloor K/2\rfloor}\eta_j,\qquad
 t=\left\lceil Kd_K^{2/3}+\sqrt K\right\rceil,\qquad k=K-t.
\]

Then `d_K->0`, eventually `k>=floor(K/2)`, and the base word in dimension
`k` has `eta_k<=d_K` and `epsilon_k=o(1)`. Applying the same calculation
at exactly `k+t=K` proves the assertion for every large `K`.

It also suffices to have the base family on a sequence of dimensions whose
successive ratios tend to one: the completed dimensions are still
relatively dense, and the ordinary top-bit bound gives

\[
 \frac{2^{K-n}W(n)}{W(K)}
  =\sqrt{K/n}(1+O(1/n))=1+o(1)\quad(K-n=o(n)).
\]

For calibration, if along a growing family `m/W(k)->c`, `h/2^k->eta`,
and `t/k->lambda>0`, the stronger constant from the proved `sqrt(2)` upper
bound gives

\[
 \limsup\frac{\nu(k+t)}{W(k+t)}
 \le \sqrt{1+\lambda}\left(c+\frac{\sqrt2\eta}{\sqrt\lambda}\right).
                                                               \tag{6}
\]

For `c,eta>0`, its minimum over `lambda` is attained at
`lambda=(sqrt(2)eta/c)^(2/3)` and equals

\[
 \left(c^{2/3}+(\sqrt2\eta)^{2/3}\right)^{3/2}.             \tag{7}
\]

This is the optimum of this upper-bound ledger, not a lower bound on
arbitrary dimension-extension constructions.

## 4. An Almost-Cover Still Needs Asymptotic Width

For any linear or cyclic word of length `m`, fixed-start interval unions
are nested. It follows without assumptions on its letters that its hole
count obeys

\[
 h\ge\sum_{s=1}^k[\binom ks-m]_+.                       \tag{8}
\]

Thus a word covering `1-o(1)` of the cube cannot have length below
`(1-o(1))W(k)`. A quantitative elementary version is

\[
 \frac m{W(k)}\ge1-O\!\left((h/2^k)^{2/3}+1/k\right).    \tag{9}
\]

Here is a proof of the rate, rather than an appeal to a Gaussian picture.
Write `m=(1-epsilon)W(k)` with `0<epsilon<=1`. Adjacent-binomial products,
and `product(1-a_i)>=1-sum(a_i)` for `0<=a_i<=1`, give for
`r=floor(k/2)` and `0<=j<=r`

\[
 \binom{k}{r-j}/W(k)\ge1-2j(j+1)/k.
\]

If `epsilon k>=16`, take `J=floor(sqrt(epsilon k)/4)`. Each of the `J+1`
ranks `r-J,...,r` has at least `(1-epsilon/4)W(k)` targets, and so at least
`3epsilon W(k)/4` holes. For sufficiently large `k` these ranks are
nonzero and `sqrt(k)W(k)/2^k>=1/2`. Since `J+1>=sqrt(epsilon k)/4`,
`h/2^k>=3epsilon^(3/2)/32`. If `epsilon k<16`, the `O(1/k)` term suffices.
This proves (9).

For a fixed `0<c<1`, (8) has the more precise Gaussian limit lower bound

\[
 \liminf\frac h{2^k}\ge
 \operatorname{erf}(\sqrt{\log(1/c)})
 -\frac{2c}{\sqrt\pi}\sqrt{\log(1/c)}
 \quad\text{if }m/W(k)\longrightarrow c.                \tag{10}
\]

Indeed rank `k/2+x sqrt(k)` has normalized size tending uniformly on
bounded `x` intervals to `exp(-2x^2)`: taking logarithms in the same
adjacent-binomial products gives `-2j^2/k+O(j/k+j^3/k^2)` for
`j=O(sqrt(k))`, with either parity of `k`. Apply the corresponding Riemann sum
to (8), or first restrict to a bounded interval to obtain the lower bound.
The integral is `sqrt(2/pi) integral (exp(-2x^2)-c)_+ dx`, which evaluates
to (10). As `c` tends to one from below, its right side is
`4(1-c)^(3/2)/(3sqrt(pi))+O((1-c)^(5/2))`.

## 5. Counterexample to Same-Dimension Hole Repair

The tempting stronger statement, "any `o(2^k)` missing targets admit an
`o(W(k))` repair word in the original dimension," is false. Take the
missing family to be the entire middle layer, of size `W(k)=o(2^k)`.
Every word covering that family needs at least `W(k)` endpoints.

There is also an explicit append-only counterexample. List every nonempty
proper subset of rank different from `floor(k/2)`, putting a full-set
letter `[k]` between consecutive listed letters and at the ends. Every
interval of length at least two contains a full-set letter, so the old
word realizes every nonempty nonmiddle target and no middle target. Each
newly covered middle target after appending requires a new right endpoint;
at least `W(k)` appended letters are necessary. This base word is long,
not near-width. It refutes the unqualified sparse-hole repair lemma, not
a special conjecture about near-width bases.

Sublinear dimension extension avoids this obstruction: a fixed missing
old target becomes a full `t`-dimensional fiber, and that fiber costs
`nu(t)+1=O(2^t/sqrt(t))`, not one position per lifted target.

## 6. A Weaker Completed-Tour Selector

This consequence uses the proved completed-tour construction and cleanliness
in `MASTER_HANDOFF.md`, I.3A.3, not the open selector (I.41). For every
sufficiently large odd `b`, put

\[
 W_b=\binom{2b}{b},\qquad
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,\qquad q=b(b-1).
\]

Suppose one selects a family `T_b` of `a_b` completed tours whose internal
middle supports, of size `q` each, are pairwise disjoint. Write `S_h(T)`
for a tour's distinct cyclic length-`b+h` windows and assume only

\[
 D_b:=\sum_{0<|h|\le H}
 \left[\binom{2b}{b+h}
       -\left|\bigcup_{T\in\mathcal T_b}S_h(T)\right|\right]
 =\delta_b4^b,\qquad \delta_b\longrightarrow0.             \tag{11}
\]

Then the full coefficient-one conjecture follows in all dimensions. This
weakens the same-family aggregate deficit `o(W_b)` in (I.41) to `o(4^b)`.
It is an implication, not a construction of the selected families.

### Proof

Each completed cyclic singleton tour has period `b^2`, and its windows of
length at most `2b-2` are clean. Since `H=o(b)`, the entire displayed band
is clean for large `b`. Apply the high OR-derivative compiler separately to
each tour, with `L=b^2`, `ell=b-H`, and `u=b+H`. A periodic source prefix
of length `b^2+b+H-1` supplies the required windows; the resulting
set-valued block has exactly `b^2+2H` letters. Concatenate these blocks
without appending any missing targets.

Internal disjointness gives `q a_b<=W_b`, so the output length `n_b` is

\[
 n_b=(b^2+2H)a_b
 \le W_b\left(1+\frac1{b-1}+\frac{2H}{b(b-1)}\right)
 =W_b\left(1+O(b^{-1}+H/b^2)\right).                     \tag{12}
\]

The assumed family is nonempty for large `b`: an empty family would miss
`4^b-W_b-o(4^b)` off-middle band targets, contradicting (11).
Every designated witness is retained inside one block. The actual hole
count `g_b` therefore satisfies

\[
 g_b\le D_b+W_b+F_b,\qquad
 F_b:=\sum_{\substack{1\le s\le2b\\|s-b|>H}}\binom{2b}s.
                                                               \tag{13}
\]

Here `W_b` pays for all possible middle holes; no middle coverage claim is
needed. The binomial exponential-moment bound in the handoff, or its
elementary proof in Section 3.3 there, gives

\[
 F_b\le2\,4^b e^{-H^2/b}\le\frac{4^b}{2b^2}.
\]

Set

\[
 \bar\eta_b=\delta_b+\frac{W_b}{4^b}+\frac1{2b^2}
 =\delta_b+O(b^{-1/2}),\qquad
 t_b=\left\lceil2b\bar\eta_b^{2/3}+\sqrt{2b}\right\rceil.
\]

Apply the nonempty linear version of (1) to (12)--(13). Equations (3)
and `(x+y)^{2/3}<=x^{2/3}+y^{2/3}` yield

\[
 \boxed{t_b=O(b\delta_b^{2/3}+b^{2/3})=o(b),\qquad
 \frac{\nu(2b+t_b)}{W(2b+t_b)}
 \le1+O(\delta_b^{2/3}+b^{-1/3}).}                         \tag{14}
\]

The dimensions `2b+t_b` have successive ratios tending to one as `b`
runs through odd integers. They need not be increasing: for any large
desired dimension `K`, choose the largest index whose completed dimension
does not exceed `K`. The next completed dimension exceeds `K`, their
ratio tends to one, and ordinary top-bit lifts cost only a `1+o(1)`
relative factor by Section 3. This proves the all-dimension conclusion.
The same proof works along any increasing base sequence with successive
dimension ratios tending to one.

### Scope of the weaker condition

- The deficit in (11) is summed over one entire growing band and one
  common selected family. Separate choices for different ranks do not
  satisfy it. A termwise `o(4^b)` bound says nothing: every rank by itself
  already has size `O(W_b)=o(4^b)`.
- No holes are appended before dimension extension. Doing so could cost
  much more than `o(W_b)` and would invalidate the length estimate (12).
- Adjacent-target disjointness, exact adjacent coverage, and the balanced
  coset restriction are not used by this implication. Internal middle
  disjointness is used only to obtain the slot bound in (12); it can be
  replaced by a directly proved `b^2 a_b<=W_b+o(W_b)`.
- The original proof of (I.42) from a small adjacent deficit is not
  applicable under (11). Nevertheless, Section 4 applied to the actual
  word proves `n_b>=(1-o(1))W_b`, hence `q a_b=(1-o(1))W_b`.
- For arbitrary physical fragments, the same argument applies once the
  actual compiled length, including every fragment overhead, is
  `(1+o(1))W(k)` and the actual hole count is `o(2^k)`.

The punctured capacity obstruction also changes scale, but is not solved.
The lower bound in C.9.11 has size
`Omega(A sqrt(r) x^{3/2})`, where `A=W(2r+1)`. As a fraction of the
whole cube this is only `Omega(x^{3/2})`. Moreover C.9.15 bounds that raw
occurrence-capacity deficit above by `O(A x(1+sqrt(rx)))`, whose cube
density tends to zero for any `x=o(1)`. Thus the necessary
`x=o(r^{-1/3})` condition belongs to the original `o(A)`-hole interface;
raw capacity no longer forces it for the weaker density-hole interface.
Neither calculation controls the actual repeated windows, so a two-rank
near-factor still does not establish the new hypothesis.

## 7. What Remains Open

The concrete unrestricted construction target is now:

> Construct cyclic nonzero set-words of period `W(k)+o(W(k))` with only
> `o(2^k)` distinct nonempty literal-OR holes, on all large dimensions or
> a sequence with successive dimension ratios tending to one.

An `O(W(k))` aggregate-hole bound would already be more than sufficient.
No rankwise bound, cleanliness, witness-length bound, or fixed derivative
depth is needed for this criterion. This is a proved weakening of the
required covering input, not a proof that such an input exists.

The handoff's `mu(7)=35` and width-length `k=9` cycle with 12 holes are
consistent finite test cases, not an asymptotic family. Extending a fixed
finite seed to unbounded dimension does not give coefficient one: the
primary term `2^t m/W(k+t)` grows like a positive constant times
`sqrt(k+t)` when `k,m` are fixed. The deterministic narrow-band bridge
word is also insufficient here: its missing fraction tends to
`1-2/pi>0`, rather than zero. Thus none of the handoff's scope walls is
bypassed by an unstated covering assumption.

## 8. Reproducible Checks

Run `python3 scratch/unrestricted_cylinder_completion_20260905_astra.py`.
The checker has no dependencies or external word files. It verifies:

- Every nonzero word of lengths one through three on up to three
  coordinates, with both linear and cyclic semantics.
- Preservation of all cyclic unions by normalization and its exact bound.
- The literal completion and exact position count for `t=0,1,2,3`.
- The endpoint capacity inequality (8) on the enumerated cycles.
- The handoff's explicit `mu(7)` word and the exact twelve `k=9` holes,
  followed by literal fiber completions in up to three new coordinates.
- The explicit same-dimension sparse-hole counterexamples for `k=3,...,8`.

Observed result: all 441 exhaustive base words and 3,528 completions pass,
as do the eight finite-seed completions and six sparse-hole counterexamples.
The generic normalization and fiber repair are not finite-optimal; these
tests do not improve any value of `nu(k)` in the handoff.

An independent mathematical audit checked the exact construction, the
`2/3` exponent, the nonmonotone completed-dimension interpolation, and
the tour implication (11)--(14). It also ran 11,132 additional cyclic
completions, the adjacent-binomial inequality through `k=400`, and
completed-tour/compiler checks at `b=11,13,21,51`. These checks are
corroboration, not premises of the proofs. The audit identified the
necessary `n>=1` qualification in the linear variant, now stated above.

For example, the base `(1,2,4)` on three coordinates misses only mask `5`.
Two lifts followed by its one missing-fiber block produce the universal
five-coordinate word

```
1 2 4 8 9 10 16 17 18 20 24 25 5 13 21
```

Its length is exactly `2^2*3+(nu(2)+1)=15`. This is a construction test,
not a finite-optimality claim.
