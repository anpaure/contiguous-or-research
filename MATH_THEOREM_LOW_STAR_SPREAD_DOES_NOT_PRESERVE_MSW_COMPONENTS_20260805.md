# Low-star spread does not preserve canonical MSW components

**Date:** 2026-08-05  
**Method:** pure mathematics; no finite computation, enumeration, or solver  
**Status:** unconditional obstruction to a reserve-first argument based only
on owner density and low-containment-star spread.

## 0. Outcome

The canonical MSW geodesics partition the rank-`r` owner layer on a
`2r`-element ground set into

\[
 C=\operatorname {Cat}_r
\]

paths, each containing `r+1` owners.  A reserved owner bank of global
density `1/(r+1)` can meet **every** one of those paths while still having
simultaneous low-star density only `2/(r+1)`.

This is much stronger spread than the `O(1/s)=O(r^{-1/2})` guarantee in the
three-palette collar-bank theorem.  Consequently, that theorem's owner
density and star-spread rows do not imply that a canonical MSW path, or an
aligned Catalan cube of such paths, survives the reservation intact.

The conclusion is proof-theoretic: it does not say that every
three-palette bank destroys every component.  It says that the existing
spread invariant cannot prove the needed co-selection.  A successful
reserve-first theorem must record incidences with the MSW components or
their exact rail states.

## 1. General transversal-spread theorem

Let `Omega` have size `2r`, put

\[
 W={2r\choose r}=(r+1)C,
\]

and let

\[
 \mathcal P=\{P_1,\ldots,P_C\}
\]

be any partition of `\binom{\Omega}{r}` into blocks of size `r+1`.  In
particular, the owner sets of the canonical MSW complementary geodesics
have this form.

For a lower set `S`, write

\[
 \mathcal O(S)=\{T\in{\Omega\choose r}:S\subseteq T\}.
\]

### Theorem 1.1

Let `h` be at the deadline scale.  For all sufficiently large `r`, there
is an owner set `F` such that

1. `|F\cap P_i|=1` for every `i`, and hence `|F|=C`;
2. for every `S\subseteq\Omega` with `|S|\le r-h-1`,

   \[
   |F\cap\mathcal O(S)|
       \le {2\over r+1}|\mathcal O(S)|.             \tag{1.1}
   \]

#### Proof

Independently in every block `P_i`, choose one owner uniformly, and let
`F` be the chosen transversal.  Its size and the first assertion are
deterministic.

Fix a star `A=\mathcal O(S)`.  The random variable

\[
 X_A=|F\cap A|
\]

is a sum of independent Bernoulli variables, one from each block.  Since
the blocks partition the owner layer,

\[
 \mathbb E X_A
 =\sum_i {|P_i\cap A|\over r+1}
 ={|A|\over r+1}=:\mu_A.                            \tag{1.2}
\]

The multiplicative Chernoff bound gives

\[
 \Pr\{X_A>2\mu_A\}\le\exp(-\mu_A/3).               \tag{1.3}
\]

Among `|S|\le r-h-1`, the smallest star has size

\[
 L_*={r+h+1\choose h+1}.                            \tag{1.4}
\]

At deadline depth `h=\Theta(\sqrt r)`,

\[
 \log L_*=\Theta(\sqrt r\log r),
\]

so

\[
 {L_*\over r+1}\gg r.                              \tag{1.5}
\]

There are at most `2^{2r}` choices of `S`.  Equations (1.3)--(1.5) and a
union bound show that, with positive probability, no star violates (1.1).
Choose such a transversal `F`. \(\square\)

## 2. Application to the canonical MSW factor

Every canonical MSW path has `r` Johnson edges and `r+1` distinct owner
vertices.  The paths are owner-disjoint and cover all `W` owners.  Applying
Theorem 1.1 to those owner blocks gives a set `F` which punctures every
canonical path.

Nevertheless, its star coefficient is

\[
 {2\over r+1}=O(1/r),                               \tag{2.1}
\]

whereas the three-palette bank theorem permits coefficient

\[
 {256s\over r+1}=O(1/\sqrt r).                      \tag{2.2}
\]

Thus even strengthening the bank's star-spread conclusion by a factor of
order `\sqrt r` would not imply that any MSW path is untouched.

The same observation applies to aligned cube classes of roots.  Those
cubes are built from the exact canonical paths and their endpoint cores.
A spread owner bank may puncture at least one owner in every root path,
even though it is sparse in every low containment star.

## 3. Exact consequence for co-selection

The implication

\[
 \text{small owner density + low-star spread}
 \quad\Longrightarrow\quad
 \text{many intact canonical MSW components}        \tag{3.1}
\]

is false.

Therefore reserving a three-palette collar bank first and then invoking
the unmodified aligned-cube theorem on the complement is not proof-safe.
The bank and cube cover must be selected jointly, or the path theorem must
be upgraded to allow prescribed punctures inside its MSW components.

A sufficient new invariant would have to control at least one of:

1. the number of reserved owners in each canonical path;
2. the exact MSW exchange ranks of the reserved owners;
3. the set of aligned cube directions destroyed by the reservation; or
4. literal compatibility between each reserved collar rail and a selected
   cube-path endpoint.

None of these is encoded by low-star spread alone.
