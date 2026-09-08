# Exact primitive-factor criterion for an outgoing PBBS q1 occurrence

**Date:** 2026-08-05  
**Method:** cyclic-parenthesis factorization only; no computation or search  
**Status:** unconditional for every `m>=2`.  This theorem distinguishes
three notions which must not be conflated: eligibility under the
max-height rule, forced selection independently of tie-breaking, and
global multiplicity one of the q1 colour.

## 1. Setup

Put `n=2m+1`.  Normalize a rank-`m` PBBS state as

\[
                         A=0_rD,
\tag{1.1}
\]

where `D` is a Dyck word of semilength `m`.  Write its primitive
factorization as

\[
                         D=C_1C_2\cdots C_t.
\tag{1.2}
\]

Let `H` be the maximum height of `D`, let `C_j` be the **first** primitive
factor of height `H`, and let `p=p_+(D)` be the first up-step ending at
height `H`.  The distinguished-deletion formula gives

\[
 g(A)=f^2(A)=(A+\{r\})-\{p\}.
\tag{1.3}
\]

Thus the outgoing q1 colour at `A` is

\[
                         K=A-\{p\}.
\tag{1.4}
\]

If `H>=2`, let `z_1` be the first down-step of `C_j` after `p` which
goes from height two to height one, and let `z_2` be the final step of
`C_j`, which goes from height one to height zero.  These steps exist
because `C_j` is primitive.  Define

\[
 H_{\rm tail}:=
 \max\{h_D(s):s\hbox{ lies strictly after }z_1
                    \hbox{ and before }z_2\},
\tag{1.5}
\]

with the maximum taken to be one when the interval is empty, and

\[
 H_{\rm later}:=
 \max_{i>j}\operatorname {ht}(C_i),
\tag{1.6}
\]

with value zero if `j=t`.

## 2. Exact deficit-three decomposition

### Lemma 2.1

Assume `H>=2`.

After changing the bit `p` from one to zero, the deficit-three word `K`
has the cyclic Dyck decomposition

\[
                 K=0_rE_0\,0_{z_1}E_1\,0_{z_2}E_2,
\tag{2.1}
\]

where

* `E_0` consists of `C_1,...,C_(j-1)` followed by the prefix of `C_j`
  ending immediately before `z_1`, with `p` changed to a down-step;
* `E_1` is the segment of `C_j` strictly between `z_1` and `z_2`;
* `E_2=C_(j+1)\cdots C_t`.

Their heights are exactly

\[
 \boxed{
 \operatorname {ht}(E_0)=H-1,\qquad
 \operatorname {ht}(E_1)=H_{\rm tail}-1,\qquad
 \operatorname {ht}(E_2)=H_{\rm later}.}
\tag{2.2}
\]

Moreover the rightmost height-`(H-1)` visit of `E_0` is immediately
followed by the changed step `p`.  Therefore the q1 occurrence associated
with the block `E_0` is exactly the outgoing edge `A--g(A)`.

#### Proof

Before `p`, the path in `C_j` first reaches height `H-1` immediately
before `p`.  Changing `p` from an up-step to a down-step lowers every
subsequent height by two.  Until the first old descent `2->1`, the changed
path is nonnegative; that descent is the first new unmatched zero.  Until
the final old descent `1->0` of the primitive factor, the path measured
above the new level `-1` is nonnegative; that final descent is the second
new unmatched zero.  What remains is precisely the concatenation of the
later primitive factors.  This proves (2.1).

Every earlier primitive factor has height at most `H-1`, because `C_j`
is the first factor attaining `H`.  The changed prefix of `C_j` reaches
height `H-1` immediately before `p`; after `p` it has height at most
`H-2`.  Hence `ht(E_0)=H-1`, and its rightmost maximum is followed by
`p`.  On `E_1` the old absolute height is shifted down by one, giving
`ht(E_1)=H_tail-1`.  The formula for `E_2` is immediate from its primitive
factorization.  The first-shadow occurrence formula now associates
`E_0`, its preceding unmatched zero `r`, and its post-maximum down-step
`p` with the edge having endpoints `K+r=g(A)` and `K+p=A`.  `square`

## 3. Eligibility and forced-selection criteria

### Theorem 3.1

For the outgoing occurrence `A--g(A)`:

1. it is a maximum-height occurrence of its q1 colour if and only if
   `C_j` is the unique primitive factor of `D` having height `H`;
2. if `H>=2`, it is the unique maximum-height occurrence, and hence is selected by
   **every** max-height tie rule, if and only if

   \[
        H_{\rm tail}\le H-1
        \quad\hbox{and}\quad
        H_{\rm later}\le H-2.
   \tag{3.1}
   \]

#### Proof

If `H=1`, then `D=(10)^m`.  Since `m>=2`, a later primitive factor also
has height one, and the outgoing block is not maximal.  This agrees with
part 1.  We may therefore assume `H>=2` for the rest of the proof.

The first block has height `H-1`.  The middle block never exceeds
`H-1`, because the old path never exceeds `H`.  The last block has height
`H_later`.

If a later primitive factor also has height `H`, then `E_2` has height
`H>H-1`, so the outgoing occurrence is not eligible.  Conversely, if
`C_j` is the unique height-`H` primitive factor, then
`H_later<=H-1`, and all three blocks have height at most `H-1`; hence
`E_0` is eligible.  This proves part 1.

The block `E_0` is uniquely tallest precisely when both competing
heights in (2.2) are strictly smaller than `H-1`.  Since heights are
integral, these inequalities are exactly (3.1).  `square`

### Warning 3.2 (the height-gap term is essential)

The condition “`C_j` is the unique tallest primitive factor and its own
post-descent tail never returns to height `H`” is **not** enough for
forced selection.  A later primitive factor of height `H-1` makes `E_2`
tie `E_0`.  The second inequality in (3.1), with `H-2` rather than
`H-1`, is therefore necessary.

### Corollary 3.3 (forced whole components)

A PBBS `g=f^2` component is contained in every max-height q1 section if
and only if every rooted Dyck phase on that component satisfies (3.1).

This criterion concerns the prescribed max-height family only.  It does
not imply that the q1 colour has global PBBS multiplicity one.  The
single-soliton component has that stronger rigidity, while a different
component can be max-height-forced even when another non-maximal
occurrence of the same colour exists.

## 4. Checks against the two known forced sectors

For the single-soliton shape `D=1^m0^m`, one has

\[
 H=m,\qquad H_{\rm tail}=1,\qquad H_{\rm later}=0,
\]

so (3.1) holds for every spatial phase.

For the two-soliton shape cycle recorded in
`MATH_THEOREM_PBBS_CLEAN_C6_Q2_NEUTRAL_GRAPHIC_NEUTRAL_20260805.md`, the
explicit deficit-three decompositions have current height `m-2` and
competing heights at most one.  Thus (3.1) also holds for every phase when
`m>=4`.

The theorem gives an exact Dyck-language starting point for classifying
all wholly selected components.  It does not assert that the two displayed
components are the only ones.
