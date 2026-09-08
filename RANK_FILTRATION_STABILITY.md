# Rank-filtration stability and the Rayleigh onion law

## 1. Rank-specific notation

For `1<=r<=k`, put

\[
M_r=\binom kr,\qquad
L_r=\sum_{s=1}^{r-1}\binom ks,
\]

and let `d_r=tau(k,r)` be the least nonnegative integer satisfying

\[
L_r\le d_rM_r+\binom{d_r+1}{2}.
\]

Write

\[
\beta_r(k)=M_r+d_r.
\]

Any zero-free word covering every mask of ranks at most `r` has length at
least `beta_r(k)`.

## 2. Canonical rank reduction

Let `A=(A_1,...,A_n)` cover the complete rank-at-most-`r` ideal.  Define

\[
h_r(A)=|\{i:|A_i|>r\}|.
\]

If `m_R=|{i:A_i=R}|` for `R in binom([k],r)`, define

\[
\delta_r(A)=\sum_R(m_R-1)_+.
\]

The **canonical `r`-reduction** deletes every entry above rank `r` and all
but one occurrence of each literal rank-`r` value.  Fix any deterministic
retention convention if a unique reduced word is desired; every statement
below holds for every choice of the retained occurrences.

### Lemma 2.1

The canonical reduction still covers every nonempty mask of rank at most
`r`.

#### Proof

A witness for a target below rank `r` contains only entries of still lower
rank, so it survives.  If an `r`-target occurs literally, retain one copy.
If it does not occur literally, none of its witnesses can contain a different
rank-`r` entry: containment between two `r`-sets would force equality.  Such
a witness also survives.  Deleting other positions merely compresses the
surviving interval.  QED.

Consequently, if `n=beta_r(k)+c`, then

\[
h_r(A)+\delta_r(A)\le c.                                  \tag{2.1}
\]

## 3. Segment capacity

Suppose a segment of length `q+t` contains selected witnesses for `q`
distinct rank-`r` masks.  Equal-rank incomparability orders both endpoint
sequences, so the `i`th selected interval lies in `[i,i+t]`.  Every physical
interval of length at least `t+1` contains one selected witness and has rank
at least `r`.  Therefore the number of distinct lower-rank masks representable
inside the segment is at most

\[
F(q,t)=tq+\binom{t+1}{2}.                                  \tag{3.1}
\]

The same formula for `q=0` is simply the total number of intervals in a
segment of length `t`.

## 4. Stability theorem

### Theorem 4.1 (rank-filtration stability)

Let `r>=2`, and let `A` have length

\[
n=\beta_r(k)+c
\]

while covering every mask of ranks at most `r`.  Put

\[
e=h_r(A)+\delta_r(A).
\]

In the canonical reduction, let `s` be the number of nonempty contiguous
components of entries having rank below `r`.  Then

\[
\boxed{e+s-1\le c.}                                       \tag{4.1}
\]

In the original word, the rank-below-`r` positions form at most `c+1`
components.

#### Proof

The reduced word has length

\[
M_r+d_r+\varepsilon,qquad\varepsilon=c-e.
\]

Let `z` be its number of distinct literal rank-`r` entries.  Delete them;
the remaining `s` low-rank segments have lengths `n_j`.  The `M_r-z`
nonliteral rank-`r` targets have witnesses wholly inside these segments.
Assign one witness per target and let `q_j` be the number assigned to segment
`j`.  Put `t_j=n_j-q_j`.  Then

\[
\sum_jq_j=M_r-z,qquad
\sum_jt_j=d_r+\varepsilon.                                \tag{4.2}
\]

Each `t_j>=1`.  Otherwise `q_j=n_j` incomparable intervals would use all
left and right endpoints of an `n_j`-position segment, forcing all selected
intervals to be singletons, impossible because every segment entry has rank
below `r`.

Set

\[
u=d_r+\varepsilon-s+1.
\]

Then every `t_j<=u`.  Applying (3.1) in every segment and using convexity of
`C(t+1,2)` on positive integers gives

\[
L_r\le
u(M_r-z)+\binom{u+1}{2}+s-1.                              \tag{4.3}
\]

At least `s-1` retained rank-`r` entries separate the segments, so
`z>=s-1`.  Since `u>=1`, (4.3) implies

\[
L_r\le uM_r+\binom{u+1}{2}.
\]

Minimality of `d_r` forces `u>=d_r`, hence `s<=epsilon+1` and (4.1).
Restoring each of the `e` deleted non-low positions increases the number of
low components by at most one, proving the original-word claim.  QED.

For a universal word this yields, simultaneously at every rank,

\[
\kappa_r(A):=\#\operatorname{comp}\{i:|A_i|<r\}
 \le n-\beta_r(k)+1.                                     \tag{4.4}
\]

## 5. Exact equality and the iteration gate

At `c=0`, equation (4.1) gives `h_r=delta_r=0` and `s=1`.  Thus

\[
A=P_r\,\Vert\,C_{<r}\,\Vert\,Q_r,                       \tag{5.1}
\]

where the boundary entries are distinct literal `r`-sets, the core contains
only lower-rank entries, and the core covers the complete lower ideal.

If `z=|P_r|+|Q_r|`, then

\[
z\le
\min\left\{
 \beta_r(k)-\max_{s<r}\beta_s(k),
 \left\lfloor\frac{\sigma_r}{d_r}\right\rfloor
\right\},                                                \tag{5.2}
\]

where

\[
\sigma_r=d_rM_r+\binom{d_r+1}{2}-L_r.
\]

The second bound follows by applying segment capacity to the core, which has
length `(M_r-z)+d_r` and represents the remaining `M_r-z` rank-`r` masks.

Equation (5.1) is one exact peel.  It is **not automatically recursive**.
The core reaches the next lower record length only if `z` equals the complete
record gap

\[
\beta_r(k)-\max_{s<r}\beta_s(k).
\]

Only in that saturated case may exact boundary--core rigidity be applied
again.  With smaller boundary mass, Theorem 4.1 supplies an excess/component
budget instead.

## 6. Rank--dimension transform

Let `a_s=|{i:|A_i|=s}|`, and let `nu_{<=r}(ell)` be the shortest zero-free
word on `ell` coordinates covering every nonempty mask of rank at most `r`.
For every `1<=r<=ell<=k`,

\[
\boxed{
 \sum_{s=1}^ra_s\binom{k-s}{\ell-s}
 \ge\binom{k}{\ell}\nu_{\le r}(\ell)
 \ge\binom{k}{\ell}\beta_r(\ell).}                      \tag{6.1}
\]

To prove this, fix an `ell`-set `Y` and retain exactly the entries
`A_i subseteq Y` with rank at most `r`.  Every witness for every rank-at-most-
`r` target inside `Y` survives.  Sum the resulting length bound over all
`Y`.  An entry of rank `s` survives for exactly `C(k-s,ell-s)` choices.

The cases `ell=k` and `r=ell` recover cumulative rank truncation and ordinary
coordinate restriction respectively.

## 7. Rayleigh lower tail

Let `k=2m`, `W=C(2m,m)`, and suppose a universal word has

\[
n=(1+\varepsilon_m)W,qquad\varepsilon_m\to0.
\]

For a uniformly random position `I`, define

\[
D_m=(m-|A_I|)_+.
\]

For every fixed `x>=0`, take `q=ceil(x sqrt(m))`.  Cumulative rank
truncation gives

\[
\Pr(D_m\ge x\sqrt m)
\ge\frac{\binom{2m}{m-q}}{n}
=e^{-x^2}-o(1).                                          \tag{7.1}
\]

Thus the normalized lower-rank deficit has the pointwise asymptotic lower
tail `e^{-x^2}`; this is a stochastic lower bound, not a claim of
distributional convergence.  In particular,

\[
\mathbb E D_m\ge
\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m.              \tag{7.2}
\]

More generally, tail integration and Fatou's lemma give, for every fixed
`p>0`,

\[
\liminf_{m\to\infty}
 \mathbb E\left[\left(\frac{D_m}{\sqrt m}\right)^p\right]
 \ge \Gamma\left(1+\frac p2\right).                      \tag{7.3}
\]

The exact finite moment is

\[
\sum_i(m-|A_i|)_+
\ge2^{2m-1}-\frac12W-1.                                  \tag{7.4}
\]

At exact middle-rank length all entries have rank at most `m`, so

\[
\frac1n\sum_i|A_i|
\le m-\frac{\sqrt{\pi m}}2+\frac12+o(1).                 \tag{7.5}
\]

This is a useful asymptotic interpretation of the simultaneous cumulative
rank cuts, not an independent obstruction beyond them.

The component law (4.4) adds ordering.  For `q=o(sqrt(m))`,

\[
\kappa_{m-q}(A)
=O\left(\left(\varepsilon_m+\frac{(q+1)^2}{m}\right)W\right).
                                                                    \tag{7.6}
\]

At the full square-root scale, for fixed `x>=0` and
`q=ceil(x sqrt(m))`, the same exact component law gives

\[
\limsup_{m\to\infty}\frac{\kappa_{m-q}(A)}W
 \le 1-e^{-x^2}.                                         \tag{7.7}
\]

For fixed `q`, the leading binomial loss is `(q^2+o(1))W/m`; at `q=1`
this is the Catalan scale.  The resulting onion is a laminar hierarchy of
nested level sets and component budgets, not a claim that every shell is a
literal boundary block.

## 8. Odd dimensions and `k=11`

Let `k=2m+1` with `m>=2`,
`M=C(2m+1,m)=C(2m+1,m+1)`, and set

\[
d_-=\tau(2m+1,m),\qquad d_+=\tau(2m+1,m+1).
\]

Then `d_-<=d_+<=d_-+1`.  If a universal word has exact upper-middle length
`M+d_+`, it has at most one literal `(m+1)`-set; if present, that entry is
unique and occurs at one physical endpoint.

* If it is present, then `d_+=d_-+1`; deleting it leaves an exact rank-`m`
  equality word.
* If it is absent and `d_+=d_-`, the whole word is an exact rank-`m` word.
* If it is absent and `d_+=d_-+1`, then at rank `m` there is at most one
  duplicate literal occurrence and the rank-below-`m` positions form at most
  two components.  If the duplicate exists, deleting it leaves one component;
  if it does not, two components remain possible.

At `k=11`,

\[
\beta_4=331,\qquad\beta_5=464,\qquad\beta_6=465.
\]

Every hypothetical length-465 universal nonzero word has exactly one of two
forms.

1. **One six-set endpoint.**  Deleting it leaves an exact 464-position
   rank-five word.  Its distinct literal five-sets lie in two boundary blocks;
   its rank-at-most-four core covers ranks one through four, has length at
   least 331, and the rank-five boundary mass is at most 133.
2. **No literal six-set.**  Every entry has rank at most five; the total
   duplicate excess `delta_5` among literal five-set values and the physical
   component count `kappa_5` of the rank-at-most-four positions obey
   `delta_5+kappa_5<=2`; at least 331 entries have rank at most four, so at
   most 134 entries have rank five.  In particular, if `delta_5=1`, those
   low-rank positions already form one component in the original word.

This dichotomy is globally without loss.  It remains necessary structure,
not a construction or an impossibility proof.
