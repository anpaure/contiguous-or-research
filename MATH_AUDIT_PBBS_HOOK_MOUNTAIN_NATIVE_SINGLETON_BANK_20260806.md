# Audit of the native PBBS hook singleton bank

**Date:** 2026-08-06  
**Audited theorem:**
`MATH_THEOREM_PBBS_HOOK_MOUNTAIN_NATIVE_SINGLETON_BANK_20260806.md`  
**Method:** symbolic ledger against the exact hook-period, mountain-return,
and mandatory-core theorems; no computation or search  
**Verdict:** **PASS**, with the scope exclusions in Section 6.

## 1. Parameter ledger

The theorem uses

\[
 n=2m+1,\qquad h=d+1,\qquad p=2h-1,\qquad b=m-h>0.
\]

The hook vacancy is exactly `p`.  The angle `(0,b,0,...,0)` has exact
period `p`, regardless of whether `p` is prime, because it has one nonzero
entry.  Thus its symmetry parameter is `gamma=1`.

## 2. Action--angle ledger

For

\[
 F=\begin{pmatrix}n-2&2\\2b&2h+1\end{pmatrix},
 \quad v=(1,h)^T,
\]

direct expansion gives

\[
 \det F=(n-2)(2h+1)-4b=np.
\]

The first-column replacement determinant is

\[
 \det\begin{pmatrix}1&2\\h&2h+1\end{pmatrix}=1,
\]

so the PBBS translation generates the whole torus.

The rooted hook update gives

\[
                         r_{t+1}-r_t=-(2z_t+1).
\]

Over one slot period, `sum z_t=b`, so the total root displacement is

\[
                         -(2b+p)=-(2m-1)=2\pmod n.
\]

Hence `tau^p=rho^2`.  Since `n` is odd, this still traverses all
coordinate rotations.  The theorem's coexistence claim is therefore
stronger than mere factor invariance: all coordinate rotations occur on
one component, at exact time spacing `p`.

## 3. Return/run ledger

The mountain inverse-fibre theorem gives predecessor times

\[
                         2,2+p,2+2p,\ldots.
\]

At terminal occupancy zero the first return is the second predecessor
selection, hence has odd-factor gap `p+2=2h+1`.  The centered step-two
dictionary converts a first gap `2L+1` into a positive owner run of length
`L`; therefore the selected run has length `h=d+1`.

No shorter run occurs on the component.  Any shorter return would have
gap below `p+2<n`, hence would lie before the outer circumference and be
governed by an earlier predecessor selection.  There is none.

## 4. Distinctness ledger

The `n` selected phases are `tau^(jp)D=rho^(2j)D`.  A nontrivial rotation
fixing a rank-`m` owner would partition its support into equal rotation
orbits of a length dividing both `m` and `n`.  Since
`gcd(m,2m+1)=1`, this is impossible.  Thus the selected phases are
distinct.

Their inserted coordinates are also distinct: spatial rotation carries
the initial omitted coordinate through all `n` labels.  Equivalently, a
simple Johnson transition inserts only one coordinate, so two distinct
singleton labels cannot use one selected source position.

For `h<=m-2`, the hook partition `(h,1^(m-h))` has at least three
solitons.  The full rigid-rotation cut ledger touches only the one- and
two-soliton edge orbits, so the selected component is untouched by that
rethread.  This holds automatically in the eventual `h=d+1` regime.

## 5. Antecedent ledger

Depth residence gives the maximal envelope `P`.  An exact length-`d+1`
run has eroded support one, and at that position the mandatory insertion
and deletion labels coincide; hence `F_t={x}`.

The selected positions are cyclically spaced by

\[
                         p=2d+1>d.
\]

Replacing `P_t` by `{x}` at all selected positions therefore changes a
union of isolated free intervals, each of length one, while retaining all
mandatory cores.  The short-gap localization theorem applies verbatim and
gives `D^dA=T`.

The owner row and every owner edge are untouched.  Consequently q1
palettes and component topology are untouched.  The identity

\[
 \bigcup_{i=a}^{b}T_i=\bigcup_{t=a}^{b+d}A_t
\]

also confirms that every upper owner-interval witness on this component
still has a literal source-interval witness.

## 6. Scope exclusions

The theorem and this audit do **not** assert:

1. residence of every other canonical PBBS component;
2. a global antecedent for the full untouched PBBS factor;
3. literal tickets for nonsingleton ranks below the owner aperture;
4. preservation of an independently fixed lower occurrence matching at
   the shrunk positions; or
5. completion of the common-cap, component-gluing, or all-`k` theorem.

Within its stated scope, the singleton bank is literal, simultaneous, and
already native to the one fixed PBBS factor.
