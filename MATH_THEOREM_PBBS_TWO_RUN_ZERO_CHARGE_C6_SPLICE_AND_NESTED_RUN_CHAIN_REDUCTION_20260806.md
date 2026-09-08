# A clean common-history C6 gives an exact zero-charge two-run splice

**Date:** 2026-08-06  
**Method:** literal common-history screens, moved-context induction, and a
sparse-bank count; no computation or search  
**Status:** unconditional local source lemma and exact global reduction.
One prospectively planted clean C6 concatenates two arbitrary target runs
without adding a source position, including singleton runs.  Iterating this
construction is reduced to a precise nested-context exposure theorem which
is not supplied by the present PBBS planting results.

## 1. Clean-C6 source normal form

Let the owner rank be `r` and the source deadline be `d`, with

\[
 d\le r-2.
\tag{1.1}
\]

The common-history lift of a clean C6 uses a core `K` of rank `r-2`, four
active labels `a_0,a_1,a_2,c` outside `K`, and the screens

\[
 X_i=\{c,a_i\},
 \qquad
 Y_i=\{a_{i-1},a_i\}.
\tag{1.2}
\]

For any ordered partition into nonempty source letters

\[
 K=C_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_d,
\tag{1.3}
\]

the fragment

\[
 (X_i,C_1,\ldots,C_d,Y_i,H_i)
\tag{1.4}
\]

has the two displayed rank-`r` owner windows

\[
 K\cup X_i,
 \qquad
 K\cup Y_i.
\tag{1.5}
\]

Here `H_i` is the complete right context attached to the screen `Y_i`.
The clean rethread cyclically permutes the three pairs `(Y_i,H_i)` while
leaving every `(X_i,C_1,...,C_d)` fixed.  It preserves source length
exactly.  With the authenticated PBBS common-pivot occurrence it also
preserves owner, q1, and selected q2, and its occurrence bijection
transports every strict-lower source cell.

## 2. Literal two-run splice

Let

\[
 R=(x_1,x_2,\ldots,x_a),
 \qquad
 S=(y_1,y_2,\ldots,y_b)
\tag{2.1}
\]

be two disjoint nonempty target runs in their desired source order, and
assume

\[
 a+b\le d.
\tag{2.2}
\]

Choose one distinguished C6 role and identify

\[
 Y_i=\{x_a,y_1\}.
\tag{2.3}
\]

Choose `K` disjoint from `x_a,y_1` and containing
`x_1,...,x_(a-1)`.  Complete the active four-label frame with two fresh
labels.  In `(1.3)`, prescribe the final `a-1` history blocks by

\[
 C_{d-a+j+1}=\{x_j\},
 \qquad 1\le j<a,
\tag{2.4}
\]

and partition the remaining elements of `K` arbitrarily among the earlier
nonempty blocks.  This is possible because `|K|=r-2>=d`.

Finally require the moved right context to begin with

\[
 \{y_2\},\{y_3\},\ldots,\{y_b\}.
\tag{2.5}
\]

The list is empty when `b=1`.

### Theorem 2.1 (zero-charge two-run splice)

Under the prospective literal planting hypotheses above, the rethreaded
source contains the contiguous interval

\[
 \boxed{
 \{x_1\},\ldots,\{x_{a-1}\},
 \{x_a,y_1\},
 \{y_2\},\ldots,\{y_b\}.}
\tag{2.6}
\]

Its width is `a+b-1`, its literal union is `R union S`, and the C6 adds no
source position.

#### Proof

After the rethread, the distinguished role has the literal order

\[
 (X_i,C_1,\ldots,C_d,Y_i,H_i).
\]

Take the interval beginning at the prescribed suffix `(2.4)` and ending
at the prefix `(2.5)`.  Equations `(2.3)--(2.5)` give exactly `(2.6)`.
Every letter is a nonempty subset of `R union S`; every member of the two
runs occurs; and the displayed count is

\[
 (a-1)+1+(b-1)=a+b-1\le d.
\]

The common-history theorem proves that the rethread is a permutation of
existing source occurrences, so its physical length charge is zero.  Its
strict-lower occurrence bijection carries the displayed interval as one
literal occurrence.  \(\square\)

The theorem is valid when `a=1`, when `b=1`, or when both runs are
singletons.  Thus the local splice has neither the native even-gap
restriction nor the native independent-envelope singleton obstruction.

## 3. Canonical word for an arbitrary run chain

Let a target `T` be the disjoint union, in cyclic order, of maximal runs

\[
 R_j=(x_{j,1},\ldots,x_{j,\ell_j}),
 \qquad 1\le j\le t,
\tag{3.1}
\]

with total rank

\[
 A=\sum_{j=1}^t\ell_j\le d.
\tag{3.2}
\]

For `t=1`, use the singleton word for that run.  For `t>=2`, define the
target-only source word as follows.

1. Write singleton cells for `x_(1,1),...,x_(1,ell_1-1)`.
2. For every `j<t`, write the bridge cell
   
   \[
   B_j=\{x_{j,\ell_j},x_{j+1,1}\}.
   \tag{3.3}
   \]
3. Between `B_(j-1)` and `B_j`, for `2<=j<t`, write singleton cells for
   `x_(j,2),...,x_(j,ell_j-1)`.
4. After `B_(t-1)`, write singleton cells for
   `x_(t,2),...,x_(t,ell_t)`.

Empty lists are omitted.  In particular, an intermediate singleton run
appears in the two adjacent bridge cells and nowhere else.

### Lemma 3.1 (exact width)

Let `s` be the number of singleton runs among
`R_2,...,R_(t-1)`.  The word above has union exactly `T` and width

\[
 \boxed{w(T)=A-t+1+s\le A\le d.}
\tag{3.4}
\]

#### Proof

Every target coordinate occurs, and no outside coordinate occurs.  The
first and last runs save one cell at their incident bridge.  An
intermediate run of length at least two saves one cell, while an
intermediate singleton is repeated in its two incident bridges and saves
none.  Hence the total saving from the `A` singleton word is

\[
 1+(t-2-s)=t-1-s,
\]

which gives `(3.4)`.  Since `s<=t-2`, the displayed width is at most `A`.
\(\square\)

This word is the correct zero-charge source target for a multi-segment
splice.  It handles the rank-eight two-bad-gap example from the native
hook obstruction with no parity choice and no envelope payload.

## 4. Exact nested-context reduction

The two-run lemma can be applied recursively from right to left.  At stage
`j`, use a common-history suffix for the still-unwritten coordinates of
`R_j`, use the screen `(3.3)`, and require the moved right context to begin
with the already constructed word for `R_(j+1),...,R_t`.

The word *require* is essential.  The current common-history theorem says
that an arbitrary complete right context moves unchanged **once the C6 is
literally planted**.  It does not prove that the output target-bearing path
is exposed as the right context of another selected PBBS C6.

Define the following statement.

> **Nested clean-C6 exposure lemma.**  Given the run chain `(3.1)`, there
> are `t-1` serial selected common-pivot C6 occurrences such that:
>
> 1. at stage `j`, the common-history suffix and screen are the literal
>    cells prescribed above;
> 2. the target-bearing output path of stage `j+1` is the complete moved
>    right context of stage `j`;
> 3. every intermediate C6 is available after the later stages have been
>    planted;
> 4. all q1/q2 halos and protected upper witnesses are compatible; and
> 5. the terminal path can be opened without deleting the displayed
>    target interval.

### Theorem 4.1 (conditional complete low source atlas)

The nested clean-C6 exposure lemma implies that every nonempty target of
rank at most `d` has a literal source interval of width at most `d`, with
zero additional source-length charge.

#### Proof

Apply Theorem 2.1 from the last seam to the first.  At each step the
complete previously built suffix moves unchanged, so induction produces
the word of Section 3.  Lemma 3.1 bounds its width by `d` and proves its
union is the target.  Each C6 preserves source count.  \(\square\)

Thus parity, run count, and singleton placement disappear completely once
nested exposure is available.  The remaining issue is physical
regeneration/planting, not source-language expressiveness.

## 5. Why the existing C6 theorem does not already prove nesting

The common-history lift proves:

* one literal rethread after its old phase and contexts are fixed;
* zero source-length charge;
* exact owner/q1 and, for the selected common-pivot PBBS occurrence, q2;
* exact strict-lower occurrence transport; and
* serial composition **conditional on every next move being planted**.

It does not prove:

* that an arbitrary target-bearing output path is a legal next moved
  context;
* a bank of selected PBBS C6 occurrences with the prescribed active labels
  and history suffixes;
* simultaneous q2-halo separation for that bank;
* arbitrary-width exterior upper protection; or
* regeneration of the packet bank after a same-parity lift.

Consequently one C6 is an unconditional algebraic zero-charge splice, but
the nested run-chain construction is a conditional reduction rather than
an all-k theorem.

The aligned double-ear topology theorem does not fill this gap.  Two cuts
on three cycles alternate the selected and complementary cut paths in the
output cycle.  It merges components, but it does not by itself expose the
selected short path as the moved context of the next seam.

## 6. A private packet per low target is scalar-affordable

Let

\[
 L_d=\sum_{s=1}^d\binom ns.
\tag{6.1}
\]

For `d=Theta(sqrt(n))`,

\[
 L_d\le(d+1)\left({en\over d}\right)^d
     =\exp(O(\sqrt n\log n))
     =2^{o(n)}.
\tag{6.2}
\]

The middle width is

\[
 W=\binom n{\lfloor n/2\rfloor}
   =2^{n-O(\log n)}.
\tag{6.3}
\]

Every target uses at most `d-1` C6 seams.  Even charging `O(d)` protected
source/halo occurrences to each seam, the complete private bank costs

\[
 O(d^2L_d)=2^{o(n)}=o(W).
\tag{6.4}
\]

### Corollary 6.1 (no scalar sharing requirement)

A general proof need not make one fixed seam serve many lower targets.
There is asymptotic room to allocate a private nested seam packet to every
target of rank at most `d`, with an `o(W)` total support bank.

This is only a count.  It does not imply that the required labelled PBBS
occurrences exist or that their protected halos are disjoint.

## 7. Sharpened remaining theorem

The low-payload gate is reduced to the following sparse embedding problem.

> **Sparse protected nested-C6 bank.**  Simultaneously for all targets of
> rank at most `d`, plant private nested clean-C6 exposure trees realizing
> Section 3, with total support `o(W)`, while preserving the selected PBBS
> owner/q1/q2 factor, the arbitrary-upper witness bank, residence, and the
> terminal common-cap state.

The local source construction and the global scalar ledger are now exact.
What remains is an occurrence-labelled protected embedding theorem.  It is
strictly weaker than asking one packet or one hook component to carry the
entire low atlas.
