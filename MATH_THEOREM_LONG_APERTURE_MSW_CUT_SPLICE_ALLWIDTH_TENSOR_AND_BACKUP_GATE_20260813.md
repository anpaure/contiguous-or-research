# Long-aperture MSW fusion has an exact collar tensor, and a Latin successor rule does not preserve it automatically

**Date:** 2026-08-13  
**Status:** unconditional seam-current theorem for the literal odd MSW
long-aperture source; unconditional obstruction to bounded completion of the
canonical upper deck  
**Scope:** the canonical odd MSW factor, with arbitrary rotations and
orientations of its source cycles before cutting

## 1. The literal long-aperture source

Put

\[
 \Omega=[2m]\sqcup\{\infty\},\qquad n=2m+1,
 \qquad R=m+1.                                      \tag{1.1}
\]

Let `2<=q=d+1<=m` and set

\[
                         a=m-q+2.                    \tag{1.2}
\]

For one canonical MSW component, choose either orientation and any cyclic
rotation of its omitted-label order

\[
                         \sigma=(z_0,\ldots,z_{n-1}). \tag{1.3}
\]

Its flat long-aperture source is

\[
 A_s=I_s^a(\sigma)
     =\{z_s,z_{s+1},\ldots,z_{s+a-1}\},
 \qquad s\in\mathbb Z/n\mathbb Z.                  \tag{1.4}
\]

The union of `ell` consecutive source positions is

\[
 \bigcup_{r=0}^{\ell-1}A_{s+r}
   =I_s^{a+\ell-1}(\sigma)                           \tag{1.5}
\]

whenever `a+ell-1<n`.  Thus source widths `q-1,q,q+1`
are respectively the immediate-lower, owner, and immediate-upper rows of
ranks `m,m+1,m+2`.

Consider a family of such components indexed by a finite set `T`.  Open
component `t` between `A_{-1}^t` and `A_0^t`.  A blockwise fusion is specified
by a permutation `pi` of `T`: the left end of block `t` is rejoined to the
right end of block `pi(t)`.  The new source components are the cycles of
`pi`.  This includes every fusion rule which merely chooses the next opened
MSW block by a cyclic or Latin successor table.

Write

\[
 s=|\{t:\pi(t)\ne t\}|                               \tag{1.6}
\]

for the number of genuinely changed seams.

## 2. Exact all-width seam ledger

For `h,j>=1`, define the cumulative collars

\[
 \begin{aligned}
 L_h^t&=\bigcup_{r=1}^{h}A_{-r}^t
       =I_{-h}^{a+h-1}(\sigma_t),\\
 R_j^t&=\bigcup_{r=0}^{j-1}A_r^t
       =I_0^{a+j-1}(\sigma_t),                       \tag{2.1}
 \end{aligned}
\]

as long as the displayed arcs are proper.  The set formulas themselves
remain valid after replacing an overlong displayed arc by its union.

### Theorem 2.1 (literal MSW cut-splice current)

Fix `2<=ell<n`.  At one changed seam, the `ell-1` old crossing values are

\[
 X_{t,\ell,h}
   =L_h^t\cup R_{\ell-h}^t,
 \qquad 1\le h\le\ell-1,                            \tag{2.2}
\]

and the corresponding new crossing values are

\[
 Y_{t,\ell,h}
   =L_h^t\cup R_{\ell-h}^{\pi(t)}.                  \tag{2.3}
\]

Every noncrossing source interval is literally unchanged.  Consequently:

1. exactly `s(ell-1)` source-interval occurrences enter the old ledger and
   the same number enter the new ledger;
2. the unlabelled width-`ell` current is zero if and only if

   \[
    \boxed{
    \{\!\{X_{t,\ell,h}:\pi(t)\ne t,
                      1\le h<\ell\}\!\}
    =
    \{\!\{Y_{t,\ell,h}:\pi(t)\ne t,
                      1\le h<\ell\}\!\}.}           \tag{2.4}
   \]

3. occurrence-labelled zero current additionally requires a bijection in
   (2.4) which preserves the required address, history, residence, phase,
   and socket tickets.

#### Proof

Two successive opened-block seams in the fused word are `n` source
positions apart.  Since `ell<n`, a width-`ell` interval meets at most one
changed seam.  If it takes `h` positions from the tail and `ell-h` from the
head, its old and new unions are exactly (2.2) and (2.3).  The cut can occupy
any of the `ell-1` internal positions of the interval.  All other intervals
retain the same ordered source positions.  This proves the occurrence count
and the necessary and sufficient multiset identity.  Retaining the tickets
gives Item 3. \(\square\)

When

\[
                         2\le\ell\le n-a=m+q-1,       \tag{2.5}
\]

the old value is the proper cyclic interval

 \[
 X_{t,\ell,h}=I_{-h}^{a+\ell-1}(\sigma_t),
 \qquad |X_{t,\ell,h}|=a+\ell-1.                   \tag{2.6}
 \]

The two collars in (2.3) have sizes `a+h-1` and
`a+ell-h-1`.  Hence:

### Corollary 2.2 (the exact rank-collar equation)

In the proper range (2.5), a new crossing value has the required rank if
and only if

\[
 \boxed{
 |L_h^t\cap R_{\ell-h}^{\pi(t)}|=a-1.}              \tag{2.7}
\]

In particular, already at source width two every new seam must satisfy

\[
 |A_{-1}^t\cap A_0^{\pi(t)}|=a-1.                  \tag{2.8}
\]

Thus its two long source letters must be adjacent in the Johnson graph on
`a`-sets.  A Latin rule on component names imposes no such equation.

#### Proof

For `j=ell-h`, inclusion-exclusion gives

\[
 |Y_{t,\ell,h}|
 =2a+\ell-2-|L_h^t\cap R_j^{\pi(t)}|.
\]

Equating this with (2.6) gives (2.7); the case `ell=2` gives (2.8).
\(\square\)

There is also a useful closed form for the stronger identity which keeps
each crossing address fixed.  Write

\[
 x_i=\sigma_t(i),\qquad y_i=\sigma_{\pi(t)}(i),
 \qquad G=n-a,                                      \tag{2.9}
\]

and put

\[
 K=\{x_{n-1},x_0,\ldots,x_{a-2}\}=L_1^t.          \tag{2.10}
\]

### Proposition 2.3 (complete addresswise collar normal form)

The addresswise identities

\[
 L_h^t\cup R_j^{\pi(t)}=L_h^t\cup R_j^t
 \quad(h,j\ge1,\ h+j\le G)                        \tag{2.11}
\]

hold if and only if there is one label `z in K` such that

\[
 \begin{aligned}
 \{y_0,\ldots,y_{a-1}\}
    &=\{x_{a-1}\}\cup(K\setminus\{z\}),\\
 y_i&=x_i \qquad(a\le i\le n-3),\\
 \{y_{n-2},y_{n-1}\}&=\{x_{n-2},z\}.              \tag{2.12}
 \end{aligned}
\]

The first and last displayed sets may be internally ordered arbitrarily.

#### Proof

Take `h=1`.  At `j=1`, (2.11) says

\[
 R_1^{\pi(t)}\setminus K=\{x_{a-1}\}.
\]

Both `R_1` and `K` have size `a`, so the first line of (2.12) follows for
some `z in K`.  Increasing `j` one step at a time in (2.11) forces the new
right-head labels successively to be

\[
                         y_a=x_a,\ldots,y_{n-3}=x_{n-3}.
\]

The two unused labels are then exactly `x_(n-2)` and `z`, proving the last
line.  Conversely, (2.12) gives

\[
 R_j^{\pi(t)}\setminus K
   =\{x_{a-1},x_a,\ldots,x_{a+j-2}\}
   =R_j^t\setminus K.
\]

Every `L_h^t` contains `K`, so adjoining either right collar gives the same
union for all `h`. \(\square\)

The normal form yields an actual-column obstruction when the flat depth is
at least three.

### Corollary 2.4 (no addresswise native seam for `q>=4`)

Suppose `q>=4` and `t,pi(t)` are distinct components of the exact canonical
MSW owner factor.  Then (2.11) cannot hold through every proper width.

#### Proof

The middle line of (2.12) is a common consecutive coordinate run of length

\[
 (n-3)-a+1=n-a-2=m+q-3\ge m+1=R.                 \tag{2.13}
\]

Hence the two cyclic orders have a common consecutive `R`-set.  But their
cyclic `R`-intervals are the rank-`R` owners, and the canonical MSW factor
uses every owner in exactly one component.  Two distinct components cannot
share one. \(\square\)

Corollary 2.4 rules out identity-at-address fusion.  It does not replace the
multiset test (2.4): a genuine three-way Boolean-C6 tensor can transport an
old occurrence to a different component address.  Such transport is
precisely the extra structure that must be proved.

### Remark 2.5 (dense Latin interleaving)

The exact count in Theorem 2.1 uses whole opened MSW blocks, so changed
seams are `n` positions apart.  A phase-by-phase Latin interleaving may put
changed seams closer together, and then a longer source interval can meet
several of them.  This does not weaken the first obstruction: at source
width two every changed directed adjacency `U->V` is local, and it has the
canonical rank `a+1` if and only if

\[
                              |U\cap V|=a-1.          \tag{2.14}
\]

After (2.14), every longer interleaved window must still be checked by its
literal union.  Thus a dense Latin schedule requires a larger overlapping
window tensor; the Latin property of its index table is not an interval-OR
identity.

## 3. The three compiler rows and the full proper deck

At one changed seam the exact numbers of altered crossing occurrences in
the three central rows are

\[
 \begin{array}{c|c|c}
 \text{source width}&\text{target rank}&\text{old/new occurrences}\\ \hline
 q-1&m&q-2\\
 q&m+1&q-1\\
 q+1&m+2&q.
 \end{array}                                        \tag{3.1}
\]

Therefore a blockwise fusion with `s` moved blocks exposes respectively
`s(q-2),s(q-1),sq` old/new cells in those rows.  It does **not** preserve
even the owner ranks unless every relevant instance of (2.7) holds.
Immediate-upper rank correctness alone already requires the `q`
simultaneous collar equations

\[
 |L_h^t\cap R_{q+1-h}^{\pi(t)}|=a-1,
 \qquad 1\le h\le q,                                \tag{3.2}
\]

at every changed seam.  Thus the upper-only gate still contains a literal
set-intersection tensor even if widths below `q-1` are not protected.

Over all proper upper widths, namely

\[
                         q+1\le\ell\le m+q-1,        \tag{3.3}
\]

the number of old crossing occurrences, and separately the number of new
ones, is

\[
 s\sum_{\ell=q+1}^{m+q-1}(\ell-1)
 =s\left\{\binom{m+q-1}{2}-\binom q2\right\}.       \tag{3.4}
\]

This is a ledger, not automatically a named loss: equal values can cancel
only through the exact tensor identity (2.4).  It does show that a bounded
exception bank is not a substitute for proving that identity.

If there are `c=Cat_m` original MSW components and the blockwise fusion is
required to leave at most `C` components, then `pi` has at most `C` fixed
points and

\[
                         s\ge \operatorname{Cat}_m-C. \tag{3.5}
\]

Thus the immediate-upper tensor alone has `q(Cat_m-C)` exposed cells, and
the all-proper-upper tensor has order `m^2 Cat_m` exposed cells.  Exact
zero-current fusion is possible only by a coherent collar identity; it is
not a bounded-error consequence of Latin component ordering.

## 4. What a genuine zero-current port must prove

For a three-block cyclic splice, Theorem 2.1 specializes, for every
`h,j>=1`, to

\[
 \{\!\{L_h^t\cup R_j^t:t\in\mathbb Z/3\}\!\}
 =
 \{\!\{L_h^t\cup R_j^{t+1}:t\in\mathbb Z/3\}\!\}.  \tag{4.1}
\]

This is exactly the Boolean-C6 boundary tensor.  A masked-core triangle is
a sufficient solution because one cut-side marker masks the change of the
other core.  The canonical MSW theorem supplies cyclic orders
`sigma_t`; it does not supply (4.1) for any prescribed triples of cuts.
In fact, the previously proved native-port audit shows that the published
same-phase pull does not expose a directed common-core C6 on the canonical
factor; see
`MATH_THEOREM_MSW_WREATH_STANDARD_PULL_COLLAR_AND_QUOTIENT_NOGO_20260806.md`.
Hence the masked tensor may be used only after an additional
planting theorem; it cannot be inferred from the MSW owner factor or from a
Latin successor schedule.

There are two logically different claims:

* **rank-correct rethreading** requires all equations (2.7);
* **complete-current rethreading** requires the stronger simultaneous
  multiset identities (2.4), with ticket transport in the protected form.

Checking only owner incidence, or only the source-width-two Johnson
condition (2.8), proves neither claim.

## 5. No bounded backup for the canonical factor

Even before any fusion, the canonical odd MSW interval deck misses the
explicit immediate-upper family

\[
 T_V=(1100)^2 1111\,V,
 \qquad V\text{ a Dyck word of semilength }m-6,       \tag{5.1}
\]

proved in
`MATH_THEOREM_CANONICAL_ODD_MSW_ALLWIDTH_INTERVAL_DECK_AND_EXPLICIT_UPPER_DEFECT_20260813.md`.
The targets in (5.1) are distinct and there are

\[
                         \operatorname{Cat}_{m-6}     \tag{5.2}
\]

of them.  Consequently any external bank which completes the canonical
immediate-upper row needs at least `Cat_(m-6)` additional named witnesses.
No backup of bounded total occurrence size can do this.  If the backup is
itself made of period-`n` long-aperture cycles, each supplies at most `n`
immediate-upper occurrences, so it needs at least

\[
                         \frac{\operatorname{Cat}_{m-6}}{2m+1} \tag{5.3}
\]

additional cycles.

Moreover a repair which changes only chronology transitions needs at least

\[
                         \frac{\operatorname{Cat}_{m-6}}{m+2} \tag{5.4}
\]

changed transitions, because one changed transition belongs to at most
`m+2` immediate-upper cyclic intervals.  A Latin rethreading can therefore
be relevant only as a Catalan-scale global replacement selected
simultaneously for upper coverage.  It is not a bounded local completion of
the canonical chronology.

## 6. Sharp conclusion

The odd long-aperture MSW factor remains an exact owner/immediate-lower,
flat-biresident skeleton.  Its literal fusion gate is now exact:

\[
 \boxed{
 \text{MSW block fusion preserves the all-width current}
 \iff \text{its cumulative cut collars satisfy (2.4) at every width}.}
\]

A Latin successor rule by itself does not imply even the first rank equation
(2.8).  If the tensor is not supplied, the damage occurs already at source
width two and includes `sq` exposed immediate-upper cells.  If the tensor is
supplied, fusion causes zero interval-current damage, but the canonical deck
still has the independent exponential missing family (5.1).  Therefore the
all-width gate cannot be closed by a bounded backup: it requires either a
globally upper-aware MSW rethreading/factor or a genuinely global alternative
carrier.
