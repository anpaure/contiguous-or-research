# Canonical one-transposition bridges: an exact dichotomy reduction

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let `F=F_m^MSW`, let `tau` be a coordinate transposition, and let
`K_1,...,K_c` be the ownership components of `F` versus `tau F`.  Write
`k_i` for the number of rows on either shore of `K_i`, so

\[
 \sum_i k_i=B=\operatorname{Cat}_m.
\]

Every corner of this complete component cube has a first-shadow hole count
bounded from below by two independent mechanisms.

1. **Endpoint stability.**  If the switched components have total old-shore
   row mass `b`, then

   \[
    H_1\ge K_m-(m-1)\min\{b,B-b\}-{2W\over m+2},
    \qquad
    K_m=(2m-3)\operatorname{Cat}_{m-2}.
    \tag{0.1}
   \]

   Hence an `o(W)`-hole corner requires a component subset sum

   \[
    \left({1\over8}-o(1)\right)B
    \le \sum_{i\in I}k_i\le
    \left({7\over8}+o(1)\right)B.
    \tag{0.2}
   \]

   In particular a connected overlay, or an overlay with one shore
   component of size `(7/8+o(1))B`, cannot help.

2. **Fixed-target freezing.**  Every canonical hole fixed by `tau` remains
   a hole at every cube corner.  For the recursion-adjacent transposition

   \[
    \tau_p=(2p+2\ \ 2p+3),
    \qquad 0\le p\le m-3,
   \]

   the contextual marked-gap construction gives

   \[
    \boxed{
    M_{\rm fix}(\tau_p)
    \ge
    \operatorname{Cat}_p(m-p-3)\operatorname{Cat}_{m-p-2}
    -{2W\over m+2}.}
    \tag{0.3}
   \]

   For every fixed `p`, the right side is

   \[
    \left({\operatorname{Cat}_p\over2^{2p+5}}-o(1)\right)W.
    \tag{0.4}
   \]

Thus every fixed-depth recursion-adjacent bridge is closed, as is every
bridge without a macroscopic component subset sum.  To close all canonical
one-transposition bridges it now suffices to prove the explicit structural
dichotomy

\[
 \boxed{
 \text{central component subset sum}
 \quad\Longrightarrow\quad
 \text{linear fixed marked-gap floor}.}
 \tag{D}
\]

Equivalently, a counterexample must be a transposition which simultaneously
fragments the canonical row partition macroscopically and fixes only
`o(W)` canonical holes.  Neither property alone is enough.

## 1. Row-distance stability at both antipodes

The canonical marked-gap family contains

\[
 K_m=(2m-3)\operatorname{Cat}_{m-2}
 \tag{1.1}
\]

pairs of pointed first-shadow occurrences with common targets, and all
pointed occurrences are disjoint.  One canonical row occurs in at most
`m-1` pairs.

Let a factor `G` be obtained from `F` by deleting `b` canonical rows and
inserting `b` other rows.  At least `K_m-(m-1)b` canonical certificate
pairs survive.  If `D_1(G)` is first-shadow duplicate excess, disjointness
gives

\[
 D_1(G)\ge K_m-(m-1)b.
\]

Since

\[
 D_1(G)=H_1(G)+W-N_1
       =H_1(G)+{2W\over m+2},
\]

we obtain

\[
 H_1(G)\ge K_m-(m-1)b-{2W\over m+2}.
 \tag{1.2}
\]

Now take a cube corner.  If components in `I` are switched, its row
distance from `F` is

\[
 b=\sum_{i\in I}k_i.
\]

Its row distance from the opposite antipode `tau F` is `B-b`.  Relabeling
the marked-gap certificates by `tau` gives the same inequality at that
antipode.  Taking the larger of the two lower bounds proves (0.1).

Finally,

\[
 {K_m\over(m-1)B}\longrightarrow {1\over8},
 \qquad
 {2W/(m+2)\over(m-1)B}=O(m^{-1}),
\]

which proves (0.2).

## 2. Why fixed targets are frozen componentwise

For every row `C`, let `d_C<=m` be the shorter cyclic distance between the
two labels moved by `tau`.  Exactly `n-2d_C>=1` middle intervals of `C`
are fixed by `tau`.  A fixed middle owner supplies an ownership edge
joining the left copy of `C` to the right copy of `tau C`.  Hence these two
row vertices lie in the same ownership component.

It follows that every component is invariant under the involution which
applies `tau` and swaps shores; its right shore is exactly `tau` of its left
shore.  If `S=tau S`, the two shore loads of `S` in each component are
therefore equal.  Every component signing preserves `mu(S)`.  In
particular, a canonical fixed hole is frozen throughout the cube.

## 3. Contextual fixed certificates

Fix `p`, put

\[
 M=m-p,
 \qquad \tau_p=(2p+2\ \ 2p+3),
\]

and fix a Dyck prefix `P` of semilength `p`.  Write a canonical root as

\[
 PZ,
\]

where `Z` has semilength `M`.  The concatenation law is

\[
 \rho(PZ)=(\rho(P),2p+\rho(Z)).
 \tag{3.1}
\]

Inside `Z`, perform the marked-gap construction: for a Dyck word `R` of
semilength `M-2` and one of its `2M-3` gaps, insert `1100` or `1010`.
The insertion--erasure lemma is unchanged by the even prefix block
`rho(P)`.  After rotating the inserted four-label block to the front, the
outside cyclic word consists of the erased local suffix order, the omitted
label, and the even block `rho(P)` (with a cyclic cut depending on the
gap).  The common first-shadow target takes alternate outside positions.

Because `rho(P)` has even length, deleting it does not change the parity
class on the local outside cycle.  The intersection of the target with the
suffix coordinates is therefore exactly the local erased marked-gap target
in dimension `2M-3`; the prefix contributes some `p`-set disjoint from the
support of `tau_p`.  Consequently global fixedness under `tau_p` is
equivalent to local fixedness under the transposition `(2\ 3)`.

For one fixed prefix, the gap-permutation theorem and upper-layer
bijection therefore give at least

\[
 (M-3)\operatorname{Cat}_{M-2}
 \tag{3.2}
\]

fixed certificate pairs: discard the three local gaps `0,1,2`, count all
remaining fixed erased targets, and add back gaps `0,1`, whose inserted
blocks contain both moved labels while the target avoids the whole block.
Different prefixes give disjoint pointed occurrences.  Summing over the
`Cat_p` prefixes proves

\[
 K_{\rm fix}(\tau_p)
 \ge
 \operatorname{Cat}_p(M-3)\operatorname{Cat}_{M-2}.
 \tag{3.3}
\]

As usual, disjoint pointed pairs imply

\[
 D_{\rm fix}(\tau_p)\ge K_{\rm fix}(\tau_p).
\]

The fixed-target occurrence baseline is label-independent:

\[
 L_{\rm fix}(\tau_p)-N_1^{\rm fix}le {2W\over m+2}.
\]

Thus

\[
 M_{\rm fix}(\tau_p)
 =D_{\rm fix}-(L_{\rm fix}-N_1^{\rm fix})
\]

gives (0.3).  For fixed `p`,

\[
 {\operatorname{Cat}_{m-p-2}\over\operatorname{Cat}_m}
 \longrightarrow4^{-p-2},
 \qquad
 {m-p-3\over2m+1}\longrightarrow{1\over2},
\]

which proves (0.4).

## 4. The exact remaining classification problem

Let `G_tau` be the graph on canonical rows in which `C,D` are joined when
some middle set owned by `C` is sent by `tau` to a middle set owned by `D`.
Its connected-component sizes are exactly `k_1,...,k_c`.

Equivalently, `G_tau` is disconnected precisely when there is a nonempty
proper row family `A` whose owner union

\[
 U_A=\bigcup_{C\in A}\mathcal W(C)
\]

is invariant under `tau`.  This is the exact block-system form of the
component question.

The remaining theorem sufficient to close every one-transposition bridge
is:

> If the component sizes of `G_tau` admit a subset sum in the interval
> `(B/8+o(B),7B/8-o(B))`, then the canonical first-shadow hole family has
> `Omega(W)` members fixed by `tau`.

The contextual theorem proves this fixed-hole alternative for every
`tau_p` with fixed `p`; endpoint stability proves the other alternative
whenever the component subset-sum interval is absent.  What is not yet
proved is that every macroscopically fragmenting transposition belongs to
one of these recursion-local classes, or has an equivalent fixed-certificate
localization.

