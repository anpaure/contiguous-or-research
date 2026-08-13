# A `p`-tag cyclic clock dilates odd owner cycles with a finite all-width support test

**Date:** 2026-08-13  
**Status:** unconditional local theorem under an explicit common cyclic
tagging and finite support-domination hypothesis.  It removes the
bipartite/even-cycle restriction of the half-clock dilation.  Application
to the frozen `T_2` relay has a common `Z_13` tagging; its remaining finite
tag-refined support certificate and complete-return audit are stated as the
last gates below.

## 1. Tagged base closures

Let `F^-` and `F^+` be two collections of oriented simple Johnson cycles
on the same rank-`rho` owner occurrence bank

\[
                         v\longmapsto V_v\subseteq X. \tag{1.1}
\]

Assume both immediate base palettes are simple.  Fix `p>=2`.  A **common
cyclic `p`-tagging** is a map

\[
                         t(v)\in\mathbb Z_p           \tag{1.2}
\]

such that on every directed edge `v -> w` of either state,

\[
                         t(w)=t(v)+1.                 \tag{1.3}
\]

In particular every component length in either state is divisible by
`p`.  The condition is joint: independently taggable old and new states
need not admit one common map on their shared occurrence bank.

For a cyclic lifted interval it is convenient to work in the periodic
universal cover of its base component.  Its projection meets a consecutive
list of block occurrences

\[
                         I=(v_1,\ldots,v_s),          \tag{1.4}
\]

where the first and last named occurrence may coincide after one wrap.
Put

\[
                         T(I)=\bigcup_{j=1}^sV_{v_j} \tag{1.5}
\]

and define the conservative tagged signature

\[
                         \sigma_p(I)=(T(I),s,t(v_1)). \tag{1.6}
\]

Let `Sigma_p^-` and `Sigma_p^+` be the supports of these signatures over
all based cyclic block arcs which can arise as projections of nonempty
proper lifted intervals.  Including every arc through one complete base
turn and its repeated endpoint is a fail-closed finite convention.

## 2. The block

Fix `h>=2`.  Choose pairwise disjoint coordinate sets

\[
 X,\qquad P=\{p_0,\ldots,p_{p-1}\},\qquad
 U=\{u_0,\ldots,u_{2h-1}\},\qquad C,               \tag{2.1}
\]

and put

\[
 D_j=\{u_j,u_{j+1},\ldots,u_{j+h-1}\},             \tag{2.2}
\]

with clock indices modulo `2h`.  Require

\[
 |C|=R-\rho-h-1\ge0,
 \qquad |C\sqcup X\sqcup P\sqcup U|\le k.          \tag{2.3}
\]

Equivalently,

\[
 R\ge\rho+h+1,qquad k-R\ge |X|-\rho+h+p-1.         \tag{2.4}
\]

For a base occurrence `v` of tag `a=t(v)`, replace it by the `2h+2`
owners

\[
\begin{aligned}
 \Gamma(v,a)=(&C+V_v+p_a+D_0,\ldots,C+V_v+p_a+D_h,\\
              &C+V_v+p_{a+1}+D_h,
                C+V_v+p_{a+1}+D_{h+1},\ldots,
                C+V_v+p_{a+1}+D_{2h}),              \tag{2.5}
\end{aligned}
\]

where `D_(2h)=D_0`.  The two occurrences carrying `D_h` are separated by
the tag exchange; the final owner carries `(p_(a+1),D_0)`.  If `v -> w`
is a base edge, then (1.3) makes the first owner of `Gamma(w,t(w))` carry
the same `(p_(a+1),D_0)`, so the blocks join by exactly the base Johnson
exchange `V_v -> V_w`.

Apply (2.5) to every component of both states.  Denote the lifted closures
by `F^-[p,h]` and `F^+[p,h]`.

## 3. Literal graph, palettes, and residence

### Theorem 3.1

Under `(1.1)--(2.4)`, each lifted state is a simple rank-`R` Johnson
two-factor.  Its owner, immediate-lower, and immediate-upper occurrence
palettes are simple.  Every nonconstant coordinate has all positive and
zero runs of length at least `h`.  The lifted size is

\[
                         (2h+2)e_0,                  \tag{3.1}
\]

where `e_0` is the number of base owner occurrences.  The component/socket
permutation is the same as in the base state.

#### Proof

Every owner in (2.5) has rank

\[
                         |C|+\rho+1+h=R.             \tag{3.2}
\]

Clock edges exchange `u_j` for `u_(j+h)`.  The middle edge exchanges
`p_a` for `p_(a+1)` at fixed `D_h`; block-joining edges perform the base
exchange at fixed `(p_(a+1),D_0)`.  Thus every edge is a Johnson edge.

The disjoint `(X,P,U)` profiles identify the base occurrence, tag, and
clock state of an owner.  The repeated clock anchors `D_h` and `D_0`
carry different tags or different base owners, so they do not duplicate an
owner.  Base simplicity finishes owner simplicity.

The three edge types have the following `(base,tag,clock)` sizes after
removing `C`:

\[
\begin{array}{c|c|c}
 &\text{lower ticket}&\text{upper ticket}\\ \hline
\text{clock}&(\rho,1,h-1)&(\rho,1,h+1)\\
\text{tag}&(\rho,0,h)&(\rho,2,h)\\
\text{base}&(\rho-1,1,h)&(\rho+1,1,h).
\end{array}                                           \tag{3.3}
\]

The profiles separate edge types.  Proper cyclic clock intervals, the
tag, the base occurrence, and base palette simplicity separate tickets
within a type.

A base coordinate is repeated for the entire `2h+2`-owner block, so each
of its nonconstant base runs is dilated to length at least `2h+2`.
Within a block the clock trace is

\[
 D_0,D_1,\ldots,D_h,D_h,D_{h+1},\ldots,D_{2h}=D_0. \tag{3.4}
\]

Every clock coordinate is positive on `h` consecutive cyclic clock states
and zero on the other `h`; repeating the antipodal anchors only lengthens
both runs.  Hence both run types have length at least `h`.

Finally, `p_a` occurs on the second half of every tag-`a-1` block and the
first half of every tag-`a` block.  These halves are consecutive by (1.3),
giving a positive run of `2h+2`; the complementary zero gap has length at
least `(p-1)(2h+2)`.  Core coordinates are constant.  Block substitution
does not change the base component or socket permutation, and the count is
immediate.  \(\square\)

## 4. All-height support theorem

Let `Deck_w(G)` denote the support of unions of all cyclic intervals of
`w` consecutive lifted owners in `G`.

### Theorem 4.1 (`p`-tag support dilation)

If

\[
                         \boxed{\Sigma_p^-\subseteq\Sigma_p^+,} \tag{4.1}
\]

then, simultaneously for every `h>=2` and every lifted width `w`,

\[
                 \boxed{
 Deck_w(F^-[p,h])\subseteq Deck_w(F^+[p,h]).}         \tag{4.2}
\]

Only support inclusion is required; no refined multiplicity identity is
needed.

#### Proof

Take an old lifted interval `J`, and project it to the periodic base block
arc `I=(v_1,...,v_s)`.  Let `a,b in {0,...,2h+1}` be its first and last
offsets in the endpoint blocks.  Its lifted value is

\[
 C\cup T(I)\cup K_{p,h}(t(v_1),s,a,b),              \tag{4.3}
\]

where the last set is the literal union of the tag and clock coordinates
on those endpoint pieces and all complete intervening blocks.  Crucially,
the right side depends on the base arc only through the signature
`(T(I),s,t(v_1))` and the two offsets.

By (4.1), choose a new base arc `I'` with the same signature, and use the
same offsets `a,b`.  Formula (1.3) gives the same successive tag sequence,
and (2.5) gives the same clock sequence in every block.  Hence the literal
`P union U` contribution in (4.3) is identical.  Since every block has
length `2h+2`, the lifted widths are also identical.  The new interval is
a width-`w` witness of the old value.  This proves (4.2).  \(\square\)

The conservative signature (1.6) may be quotiented further.  For example,
after a complete intervening block the clock union is all of `U`, and
after a full `p`-tag traversal the tag union is all of `P`.  Such
optimizations are unnecessary for the theorem.

## 5. The `T_2` gate

The full lifted MSW wreath cycles used by the two-hex `T_2` actuator have
`13` owner occurrences each; the switched state merges five such cycles
into one `65`-owner cycle.  Therefore uniform tag increment by one closes
with

\[
                         p=13.                       \tag{5.1}
\]

The joint voltage equations on the shared owner occurrence bank have
exactly two solutions, related by global reversal.  In one orientation the
merged cycle is deterministic and the five affected old cycles use mask
`28`; the reverse solution uses mask `3`.  Each tag occurs five times on
the affected owner bank.  Thus the common-tagging hypothesis (1.2)--(1.3)
is satisfied literally; it is not an independently chosen phase on each
cycle.

The remaining local calculation is finite and height-independent:

\[
                         \boxed{\Sigma_{13}^-\subseteq\Sigma_{13}^+.} \tag{5.2}
\]

Once (5.2) is certified on the complete old and switched wreath closures,
Theorems 3.1 and 4.1 give a two-sided resident, owner/palette-simple,
all-width support-monotone `T_2` actuator of protected size `O(h)` for
every `h`.  If (5.2) fails, the failed signatures identify the exact finite
return/backup collars required; no new large-`h` search is needed.

This theorem does not assert (5.2).  It isolates it as the decisive finite
certificate.  Nor does it by itself plant the protected lifted bank in a
spanning factor or supply the terminal typed cap.
