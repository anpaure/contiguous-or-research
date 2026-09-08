# Independent audit: banded double-chain equality theorem

## Verdict

**PASS, with three scope/edge-case repairs.**

The proposed implication

\[
\nu(k)=B(k)\Longrightarrow
\text{an almost-full ordered orthogonal double-chain realization of the lower ideal}
\]

is correct.  The endpoint argument, the exact band-cell count, the strict-chain
rank argument, and the deletion/spoil charging in the rank-profile inequality
all check out.

The repairs are:

1. the displayed `n` left and right chains are allowed to be empty;
2. the pin-survival lemma is exact for the **chosen lower-mask intervals only**,
   not by itself for the rank-`r` and upper-mask witnesses of a full universal
   word;
3. the useful form of the rank-profile inequality has a positive part,
   because `sigma <= M` is not automatic:

   \[
   q\,[n-d+1-\sigma]_+
   \le \sum_{s=1}^{r-d+q-1}\binom ks.
   \tag{A}
   \]

Without the positive part, the submitted inequality is still formally true
when its left side is negative, but it then says nothing.

No correction to the principal theorem is otherwise needed.

## 1. Setup and the selected rank-`r` witnesses

Let `r` attain `B(k)`, put

\[
M=\binom kr,\qquad n=M+d=B(k),
\qquad L=\sum_{s=1}^{r-1}\binom ks,
\]

and choose one witness interval for every rank-`r` mask.  Write the witnesses,
ordered by increasing left endpoint, as

\[
I_i=[a_i,b_i],\qquad 1\le i\le M.
\]

The endpoint facts used in the submission are valid, but the noncontainment
step should be made explicit.

* Two distinct selected intervals cannot be nested.  If `I_i` contains `I_j`,
  then `OR(I_i)` contains `OR(I_j)`.  Both values have rank `r`, so they would
  be equal, contrary to the choice of one interval for each distinct rank-`r`
  mask.
* In particular, left endpoints and right endpoints are separately distinct.
  Once the intervals are ordered by left endpoint, noncontainment forces

  \[
  a_1<\cdots<a_M,\qquad b_1<\cdots<b_M.
  \]

* Since these are increasing `M`-subsets of `[n]`, with `n=M+d`, one has

  \[
  a_i\ge i,\qquad b_i\le i+d.
  \]

  Hence

  \[
  I_i\subseteq[i,i+d]. \tag{1}
  \]

Now take any physical interval `J=[u,v]` of length at least `d+1`.  Since
`v <= M+d`, its left endpoint satisfies `u <= M`.  Equation (1) gives

\[
I_u\subseteq[u,u+d]\subseteq J.
\]

Thus every interval of length at least `d+1` contains a selected rank-`r`
witness and consequently has OR-rank at least `r`.  Therefore every mask of
rank below `r` has a witness of length at most `d`.  This is the exact premise
needed for the band theorem.

## 2. The two chain partitions and the exact hole count

Choose one length-at-most-`d` witness

\[
I_S=[\ell_S,\rho_S]
\]

for each nonempty mask `S` of rank below `r`.  Distinct masks necessarily use
distinct physical intervals.  Define

\[
C_i=\{S:\ell_S=i\},\qquad D_j=\{S:\rho_S=j\}.
\]

These are partitions into `n` indexed chains, some of which may be empty.

For fixed `i`, increasing the right endpoint nests the intervals increasingly.
Their OR-values are therefore weakly increasing; distinct labels make the
inclusions strict.  Hence `C_i` is a strict inclusion chain.  There are at
most `d` admissible endpoints `i,...,i+d-1`, so `|C_i|<=d`.

For fixed `j`, decreasing the left endpoint enlarges the interval.  Thus
`D_j` is a strict inclusion chain when read in reverse order of its left
indices, again of size at most `d`.

A mask belongs to `C_i intersect D_j` exactly when its selected witness is
the cell `[i,j]`.  A physical interval has one OR-value, so

\[
|C_i\cap D_j|\le1.
\]

Every occupied cell lies in

\[
\mathcal B_{n,d}=\{(i,j):1\le i\le j\le n,\ j-i<d\}.
\]

Conversely, all `L` selected lower-mask witnesses are distinct cells of this
band.  Since `d<n`,

\[
|\mathcal B_{n,d}|
=\sum_{h=1}^{d}(n-h+1)
=dn-\binom d2
=dM+\binom{d+1}{2}
=L+\sigma.
\]

Therefore the incidence graph is exactly the complete one-sided `d`-band
with `sigma` cells omitted.  This part of the submitted theorem is exact.

The assumption `sigma <= M` is **not** a consequence of rank-count equality.
It may be imposed in a later single-switch construction, but it is unnecessary
for this necessary theorem.  A valid (small, degenerate) counterexample is
`k=3,r=3`: here `r` really does attain `B(3)=4`, while `M=1`,
`d=tau(3,3)=3`, `L=6`, and `sigma=3>M`.  (The alternative maximizing choice
`r=2` has `sigma<=M`.)  By contrast, `k=7,r=3` is **not** a counterexample:
there `tau(7,3)=1` and `binom(7,3)+tau(7,3)=36<B(7)=37`; the attaining rank
is `r=4`.

This distinction matters: for an attaining rank,

\[
d=B(k)-\binom kr=\tau(k,r),
\]

whereas for a nonattaining rank `B(k)-binom(k,r)` must not be substituted for
`tau(k,r)`.  Minimality of `d=tau(k,r)` only gives, for `d>=1`,

\[
0\le\sigma<M+d=n,
\]

not `sigma<=M`.

## 3. Pin survival

For the chosen lower witnesses define

\[
Z_b=[n]\setminus\bigcup_{S:\,b\notin S} I_S.
\]

Then the submitted condition

\[
I_S\cap Z_b\ne\varnothing
\quad(S\ne\varnothing,\ b\in S)
\tag{2}
\]

is necessary and sufficient for realizing **all of these chosen lower
interval labels simultaneously**.

Necessity follows because an occurrence of `b` cannot lie in an assigned
interval whose target omits `b`.  For sufficiency, either put `b` at every
position of `Z_b`, or choose any hitting set `H_b subseteq Z_b` meeting every
assigned interval whose target contains `b`.  Targets omitting `b` then see no
copy of `b`, while targets containing `b` see at least one.

There are two important scope qualifications.

* To require every array entry to be nonempty, one additionally needs

  \[
  \bigcup_{b=1}^{k} Z_b=[n]. \tag{3}
  \]

  This condition is also sufficient: after satisfying (2), add at each still
  empty position any coordinate for which that position lies in `Z_b`.
  Equivalently, with sparse hitting sets require `union_b H_b=[n]`.
* Conditions (2)--(3) only realize the selected lower-mask intervals.  A full
  converse also has to impose the rank-`r` witnesses and the upper ranks; those
  extra interval labels can shrink the corresponding legal pin sets.  The
  theorem is therefore a necessary global reduction, not a sufficient
  characterization of a universal word.

Under the forward hypothesis of an actual nonzero universal word, (3) holds
automatically: every physical position contains a coordinate, and any such
occurrence is legal for all selected lower witnesses.

## 4. Audit of the rank-profile inequality

Fix `1<=q<=d`.  First count all physical band cells of length at most `q`:

\[
qn-\binom q2.
\]

Only left endpoints `i<=n-d+1` admit the complete right-extension string

\[
[i,i], [i,i+1],\ldots,[i,i+d-1].
\]

There are exactly `q(n-d+1)` candidate cells of lengths at most `q` on these
full rows.  Equivalently, the number discarded at the right boundary is

\[
\left(qn-\binom q2\right)-q(n-d+1)
=qd-\binom{q+1}{2}
=\sum_{h=1}^{d-1}\min(q,h),
\]

so the submitted boundary count is correct.

A deleted band cell of length `h` can spoil the property "all right
extensions through length `d` are selected" only for candidate lengths
`ell<=min(q,h)` in the same row.  It therefore spoils at most `q` candidates.
Charging `q` to each of the `sigma` holes is safe even when several holes
spoil the same candidate and even when a hole lies in a boundary row.

It follows that at least

\[
q(n-d+1)-q\sigma=q(n-d+1-\sigma)
\]

candidates survive whenever this expression is positive.  The universally
clean statement is the positive-part count in (A).

For a surviving cell of length `ell<=q`, all `d-ell+1` cells from it through
the length-`d` extension are selected lower-mask witnesses in one strict
chain.  Its top mask has rank at most `r-1`; every strict inclusion raises
rank by at least one.  Hence its bottom label has rank at most

\[
(r-1)-(d-\ell)\le r-d+q-1.
\]

Surviving cells have distinct labels, so (A) follows.  If
`r-d+q-1<1`, the binomial sum is empty and interpreted as zero.

The left-extension/right-endpoint argument is genuinely symmetric: retain
right endpoints admitting a complete length-`d` left extension, charge each
hole to at most `q` shorter candidates in its column, and read the strict
`D_j` chain in reverse left-endpoint order.  It gives the same scalar
inequality.  The two versions may carry additional structural information
when row and column hole distributions are tracked jointly, but their
unrefined numerical inequalities coincide.

## 5. Small-parameter sanity checks

The corrected inequality is consistent with the exact cases and is sometimes
tight:

* `k=4`, take `r=2`, `M=6`, `d=1`, `L=4`, `sigma=3`.  At `q=1`, (A) is
  `4 <= binom(4,1)=4`.
* `k=6`, take `r=3`, `M=20`, `d=1`, `L=21`, `sigma=0`.  At `q=1`, (A) is
  `21 <= binom(6,1)+binom(6,2)=21`.
* `k=9`, take the upper middle rank `r=5`, giving `M=126`, `d=2`,
  `L=255`, `sigma=0`.  The tests are `127<=129` for `q=1` and
  `254<=255` for `q=2`.
* `k=14`, `r=7`, `M=3432`, `d=2`, `L=6475`, `sigma=392`.  The two
  necessary tests become `3041<=3472` and `6082<=6475`.

These checks are arithmetic sanity tests, not existence proofs.

## 6. Audited conclusion

The valid theorem is:

> Equality `nu(k)=B(k)` forces the entire punctured lower ideal into an
> ordered orthogonal pair of (possibly empty) chains occupying all but
> `sigma` cells of the one-sided `d`-band.  The labels are strictly ordered
> along rows and reverse-ordered along columns, satisfy lower-interval pin
> survival and nonempty-position coverage, and obey the positive-part
> rank-profile inequalities (A) and their left-extension analogues.

This is a real strengthening of the scalar rank count.  It remains only a
necessary reduction: constructing such a lower-band labeling, preserving
pins after adding the central witnesses, and covering all upper ranks are the
unproved directions.
