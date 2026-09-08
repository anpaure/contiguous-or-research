# Independent audit of the amortized subcube-density theorem

## Verdict

**PASS for the main theorem, with one novelty correction and one equality-scope
correction.**

The following claims are correct and unrestricted:

\[
 |J|\le d+\binom{|U(J)|}{r},
 \qquad
 p_R+q_R\ge c_{r,d},
 \qquad
 \sum_Rq_R\le \binom kr,
\]

\[
 \sum_R(c_{r,d}-p_R)_+\le\binom kr,
\]

and

\[
 \boxed{
 \sum_{i=1}^n\binom{k-|A_i|}{r-|A_i|}
 \ge
 \left(\left\lceil\frac{2(2^r-1)}{d+1}\right\rceil-1\right)
 \binom kr.}
\]

The lower-tail consequence and all displayed `k=11,n=465,r=6`
arithmetic are also correct.

There are two qualifications.

1. The physical containment lemma is not new relative to the workspace.  It
   is exactly Section 169, item 663 of `MATHEMATICAL_HANDOFF.md`, and its
   simultaneous minimum is item 664.  The genuinely new part is the
   `q_R` long-window credit, its global amortization, and the resulting
   distributional theorem and general rank-moment inequality.  At the
   particular `k=11,n=465` checkpoint, however, the scalar `14322` moment
   cut is already implied by the stronger cumulative rank-truncation cuts;
   the new information there is the lower-tail/deficiency control.
2. Equality in the moment cut forces all length-`d+1` windows to have rank
   `r` and forces `p_R+q_R=c_{r,d}` for every `R`.  In general it does **not**
   alone force the `M` window values to be distinct or every raw local run
   inequality to be tight.  Section 6 of the current
   `AMORTIZED_SUBCUBE_DENSITY_THEOREM.md` already uses the safe formulation;
   the stronger wording in the submitted message should be replaced by that
   version.

There is no gap in the theorem itself.

## 1. Endpoint normal form

Put

\[
 M=\binom kr,\qquad n=M+d,
\]

and select one witness interval for each rank-`r` target.  Two selected
intervals cannot contain one another: containment of intervals implies
containment of their ORs, while two distinct `r`-sets are incomparable.

Order the witnesses by increasing left endpoint and write

\[
 I_i=[\ell_i,u_i],\qquad 1\le i\le M.
\]

The left endpoints are distinct.  The right endpoints are distinct and occur
in the same order, since `ell_i<ell_j` and `u_i>=u_j` would give
`I_j subseteq I_i`.  Each endpoint sequence is an `M`-element subset of
`[M+d]`; hence

\[
 i\le \ell_i\le i+d,
 \qquad
 i\le u_i\le i+d.
\]

Consequently

\[
 I_i\subseteq[i,i+d].                                      \tag{1}
\]

No shortest-witness assumption, fixed derivative row, Johnson adjacency, or
grading is used here.

## 2. Audit of the containment lemma

Let `J=[a,b]` have length `L=b-a+1`.  The claimed inequality is trivial when
`L<=d`.  If `L>d`, then every index

\[
 a\le i\le b-d
\]

is a valid witness index and satisfies

\[
 I_i\subseteq[i,i+d]\subseteq J.
\]

The endpoint check is sound: `b<=M+d` gives `b-d<=M`, while `L>d`
gives `a<=b-d`.  Thus `J` contains exactly `L-d` of the selected witnesses
indexed in this range.  Their OR values are distinct rank-`r` subsets of
`U(J)`.  If `s=|U(J)|`, then

\[
 L-d\le\binom sr,
\]

where the right side is zero for `s<r`.  Therefore

\[
 \boxed{|J|\le d+\binom{|U(J)|}{r}}.                       \tag{2}
\]

In particular, OR-rank below `r` implies length at most `d`, and OR-rank
exactly `r` implies length at most `d+1`.

Applying (2) independently at every eligible rank gives the simultaneous cap
in the submission.  This is mathematically correct, but it is the already
audited containment-multiplicity theorem in handoff items 663--664.

## 3. The `q_R`/run equivalence

Fix `R in binom([k],r)` and let

\[
 P_R=\{i:A_i\subseteq R\}.
\]

Every run `C` of `P_R` has `U(C) subseteq R`.  Equation (2) therefore bounds
its length by `d+1`.

If a physical interval `J` of length `d+1` has OR `R`, then all its entries
belong to `P_R`, so `J` lies inside one `P_R`-run.  Since that run has length
at most `d+1`, it equals `J`.

Conversely, if a `P_R`-run has length `d+1`, its OR cannot have rank below
`r`, by (2).  Its OR is contained in the `r`-set `R`, so it must equal `R`.

Hence

\[
 q_R
 =\#\{\text{length-}(d+1)\text{ intervals with OR }R\}
 =\#\{\text{length-}(d+1)\text{ runs of }P_R\}.             \tag{3}
\]

Both directions of the asserted equivalence are valid.

## 4. Audit of the local credit inequality

For `1<=ell<=d+1`, let

\[
 f_d(\ell)=\sum_{j=1}^{d}(\ell-j+1)_+.
\]

This is exactly the number of internal intervals of length at most `d` in a
run of length `ell`.  If `ell<=d`, then

\[
 2f_d(\ell)=\ell(\ell+1)\le(d+1)\ell.
\]

If `ell=d+1`, then

\[
 2f_d(d+1)=d(d+3)=(d+1)^2+(d-1).
\]

Thus

\[
 2f_d(\ell)
 \le(d+1)\ell+(d-1){\bf1}_{\{\ell=d+1\}}.                 \tag{4}
\]

Every nonempty proper subset `S` of `R` has OR-rank below `r`, so every
witness for `S` has length at most `d` by (2).  Such a witness lies wholly
inside a `P_R`-run.  Distinct target sets require distinct physical
intervals.  Therefore the runs contain short witnesses for at least
`2^r-2` distinct targets.

If `q_R=0`, a witness for `R` itself also has length at most `d`, so there are
at least `2^r-1` required short intervals.  Summing (4) gives

\[
 (d+1)p_R\ge2(2^r-1).
\]

If `q_R>=1`, summing (4) gives

\[
 (d+1)p_R+(d-1)q_R\ge2(2^r-2).
\]

Adding `2q_R` and using `q_R>=1` yields

\[
 (d+1)(p_R+q_R)\ge2(2^r-1).
\]

Since `p_R+q_R` is integral,

\[
 \boxed{p_R+q_R\ge
 c_{r,d}:=\left\lceil\frac{2(2^r-1)}{d+1}\right\rceil.}    \tag{5}
\]

The local proof is sound.  In particular, it never assigns a separate
length-`d+1` credit to each target; `q_R` counts actual physical runs.

## 5. Global amortization and moment cut

There are exactly

\[
 n-(d+1)+1=n-d=M
\]

physical intervals of length `d+1`.  Equation (2) says every one has OR-rank
at least `r`.  A window of rank exactly `r` contributes to the unique
`q_R` indexed by its OR; a higher-rank window contributes to none.  Hence

\[
 \boxed{\sum_Rq_R\le M.}                                   \tag{6}
\]

Equation (5) gives `(c-p_R)_+<=q_R` pointwise.  Summing and applying (6)
proves

\[
 \boxed{\sum_R(c_{r,d}-p_R)_+\le M.}                       \tag{7}
\]

If `p_R<=c-j`, its contribution to (7) is at least `j`; therefore

\[
 \boxed{|\{R:p_R\le c_{r,d}-j\}|\le M/j}.                 \tag{8}
\]

Finally, double counting pairs `(i,R)` with `A_i subseteq R` gives

\[
 \sum_Rp_R
 =\sum_{i=1}^n\binom{k-|A_i|}{r-|A_i|}.                 \tag{9}
\]

For every `R`,

\[
 p_R\ge c_{r,d}-(c_{r,d}-p_R)_+.
\]

Summing this and using (7) proves the stated moment cut.  All invalid lower
arguments in (9) correctly contribute zero.

## 6. Exact `k=11` arithmetic

For `k=11,n=465,r=6`,

\[
 M=\binom{11}{6}=462,
 \qquad d=3,
 \qquad
 c_{6,3}=\left\lceil\frac{126}{4}\right\rceil=32.
\]

Thus

\[
 \sum_U(32-p_U)_+\le462,
 \qquad
 \sum_Up_U\ge31\cdot462=14322.                            \tag{10}
\]

An entry of rank `s` lies in

\[
 \binom{11-s}{6-s}
\]

six-sets.  For `s=1,...,6`, these coefficients are

\[
 252,126,56,21,6,1.
\]

Therefore (10) is exactly

\[
 \boxed{252n_1+126n_2+56n_3+21n_4+6n_5+n_6\ge14322.}      \tag{11}
\]

The previous pointwise bound `p_U>=28` gave

\[
 28\cdot462=12936,
\]

and the improvement is

\[
 14322-12936=1386=3\cdot462.
\]

Combining (10) with `p_U>=28` gives

\[
 4a_{28}+3a_{29}+2a_{30}+a_{31}\le462.
\]

Consequently the stated tail counts `115`, `154`, and `231` are all correct.

This raises the earlier density-only comparator from `12936` to `14322`.
It is not, however, the strongest aggregate consequence already present in
the full unrestricted framework.

### Comparison with cumulative rank truncation

Handoff Section 191 proves, for

\[
 P_s:=\#\{i:|A_i|\le s\},
\]

the cumulative constraints

\[
 P_s\ge b_s(11)=\binom{11}{s}+\tau(11,s).
\]

At length 465, entries have rank at most six, and the relevant exact lower
bounds are

\[
 P_1\ge11,
 \quad P_2\ge56,
 \quad P_3\ge166,
 \quad P_4\ge331,
 \quad P_5\ge464,
 \quad P_6=465.                                            \tag{12}
\]

Because the six-set weights `252,126,56,21,6,1` decrease with entry rank,
their minimum subject to (12) occurs at all five lower cumulative bounds.
Equivalently the minimizing rank-count vector is

\[
 (n_1,n_2,n_3,n_4,n_5,n_6)
 =(11,45,110,165,133,1).
\]

Its six-set moment is

\[
 252(11)+126(45)+56(110)+21(165)+6(133)+1
 =\boxed{18866}.                                           \tag{13}
\]

Thus the scalar `14322` inequality is redundant at this particular
checkpoint, and describing it as the strongest current aggregate cut would
be incorrect.  The deficiency theorem

\[
 \sum_U(32-p_U)_+\le462
\]

is not recovered from these cumulative rank counts: they constrain only the
total `sum_U p_U`, while the new theorem controls how that total may be
distributed among the 462 individual six-sets.

The general moment theorem is nevertheless not always redundant.  At the
active `k=6,n=21,r=3` checkpoint, `d=1`, `c_{3,1}=7`, and it gives

\[
 10n_1+4n_2+n_3\ge120.
\]

The cumulative rank-truncation bounds there are

\[
 P_1\ge6,\qquad P_2\ge16,\qquad P_3=21,
\]

whose minimum for the same objective is only

\[
 10(6)+4(10)+5=105.
\]

So the new aggregate inequality can be a genuine strengthening even though
its `k=11` specialization is not.

## 7. What equality really forces

Let `c=c_{r,d}` and define

\[
 D_R=(c-p_R)_+,
 \qquad
 E_R=(p_R-c)_+.
\]

Then

\[
 p_R=c-D_R+E_R.
\]

Suppose equality holds in the moment cut:

\[
 \sum_Rp_R=(c-1)M.
\]

It follows that

\[
 \sum_RD_R=M+\sum_RE_R.
\]

But `D_R<=q_R` pointwise and `sum_R q_R<=M`.  Therefore all of the following
are forced:

\[
 E_R=0\quad\hbox{for every }R,
\]

\[
 \sum_RD_R=\sum_Rq_R=M,
\]

and, because nonnegative pointwise differences sum to zero,

\[
 D_R=q_R,
 \qquad
 \boxed{p_R+q_R=c\quad\hbox{for every }R.}                 \tag{14}
\]

Moreover `sum q_R=M` means all `M` physical length-`d+1` windows have
OR-rank exactly `r`.  These conclusions in the submission are correct.

The stronger generic claim about every local run inequality needs a precise
rounding qualifier.  Put

\[
 N=2^r-1,
 \qquad
 \varepsilon=(d+1)c-2N,
 \qquad 0\le\varepsilon\le d.
\]

Let `F_R` be the total number of short intervals inside the `P_R`-runs.  The
two nonnegative sources of local slack are the gap in (4) and the number of
short intervals beyond the mandatory distinct targets.  Under (14), their
combined doubled slack is

\[
 \varepsilon\quad(q_R=0),
\]

and

\[
 \varepsilon+2-2q_R\quad(q_R\ge1).                        \tag{15}
\]

Thus equality implies `q_R<=1+epsilon/2`, but unless the appropriate
quantity in (15) vanishes, it does not force every individual run inequality
to be tight.  It also gives only average `q_R=1`; duplicate window values are
not excluded in general.  For example, at the level of the displayed local
inventories, `(r,d,c)=(5,3,16)` permits both

\[
 q=0,\ p=16,\ \text{run lengths }(3,3,3,3,3,1),
\]

and

\[
 q=2,\ p=14,\ \text{run lengths }(4,4,3,3).
\]

This does not assert that those profiles extend to a universal global word;
it shows why the displayed equalities alone do not prove distinctness or a
unique run decomposition.

The corrected equality-scope paragraph in the current theorem note is
therefore the right generic statement.

### Extra rigidity in the eleven-bit case

The `k=11` parameters allow a stronger specialization that was not stated in
the submission.  Here `d=3`, `c=32`, and `epsilon=2`.  If the moment cut
is tight, (14) gives `p_U+q_U=32`.  For `q_U>=1`, the local inequality gives

\[
 4p_U+2q_U\ge124,
\]

so `q_U<=2`.

If `q_U=2`, then `p_U=30` and equality must hold in the local capacity
bound.  For `d=3`, the run inequality is tight only at run lengths `3` and
`4`.  Two length-four runs leave `22` support positions, which cannot be
partitioned into length-three runs.  Hence `q_U=2` is impossible.

Thus `q_U<=1` for every six-set.  Since `sum_Uq_U=462` over exactly 462
six-sets, one gets

\[
 \boxed{q_U=1,\qquad p_U=31\quad\hbox{for every }U.}        \tag{16}
\]

For `q_U=1`, the unique length-four run leaves 27 positions.  The available
rounding slack is two; a run of length one or two consumes both units, but
then the remaining position count is not divisible by three.  Therefore the
run multiset is forced to be

\[
 \boxed{(4,3,3,3,3,3,3,3,3,3).}                          \tag{17}
\]

Consequently, in this special tight branch, the 462 length-four window ORs
do enumerate the 462 six-sets exactly once.  Each six-set support contains
63 short physical intervals, of which 62 realize its nonempty proper
subsets; there is exactly one surplus short interval.  This is a legitimate
stronger `k=11` equality branch, though it is not a generic consequence of
the theorem.

## 8. Novelty relative to the handoff

The workspace comparison gives the following precise split.

* The endpoint normal form is handoff Section 6.
* The multiplicity containment cap and simultaneous physical cap are already
  handoff Section 169, items 663--664.
* The pointwise `p_U>=28` and aggregate threshold `12936` are handoff Section
  171, items 675--677.
* No `q_R`-credit inequality, global deficiency budget, or lower-tail theorem
  appears in the handoff before this note.  The `14322` formula is a new
  consequence of the displayed amortized theorem, but at `k=11` it is weaker
  than the existing rank-truncation consequence `18866`.

Accordingly, the amortization theorem is new relative to the recorded
project state, while Lemma 1 should be presented as the existing containment
lemma used as its input.  This audit does not make a claim about novelty in
the external literature.

## 9. Finite independent check

As a secondary guard against endpoint and rounding mistakes, the theorem was
checked by exhaustive enumeration of all universal nonzero words in the
following ranges:

```text
k=1, n<=4
k=2, n<=6
k=3, n<=7
```

This covered `88,714` universal words and `265,285` eligible `(word,r)`
instances with `d>=1`.  For every instance the check independently verified:

1. the `q_R`/maximal-run equivalence;
2. `p_R+q_R>=c_{r,d}` for every `R`;
3. `sum_R q_R<=M`;
4. the deficiency budget;
5. the exact double count and moment inequality.

All checks passed.  The exhaustive test is corroboration; Sections 1--7 are
the proof.

## Final assessment

The central amortization is theorem-level and correct.  Its distributional
form supplies a new unrestricted necessary condition at `n=465`, but its
scalar moment specialization there is redundant.  It neither proves
`nu(11)>465` nor constructs a length-465 word.  The mathematically safe
headline is:

> The known containment-multiplicity lemma, combined with globally shared
> length-`d+1` credit, yields a new deficiency theorem and rank-moment cut.

The current theorem note already repairs the generic equality overclaim and
records the stronger special `k=11` tight-branch conclusion.
