# The state-level suspension gate for legal Haar circuits

> **July 2026 update.**  The shadow-space part of the gate is now solved by
> the antipodal gap operator in
> [HAAR_ANTIPODAL_SUSPENSION.md](./HAAR_ANTIPODAL_SUSPENSION.md).  If two new
> coordinates are inserted at gap distance \(m\) and one sums over all
> pointings, then
>
> \[
> B_{m+1}P_mw=B_mP_mw=0,
> \qquad
> (B_{m-1}P_mw)_{U\cup\{x\}}=(m-1)(B_{m-2}w)_U.
> \]
>
> The unresolved part is purely integral.  The translate sum repeats middle
> targets and is not a factor packing.  The note gives an exact coarse
> five-state/three-state criterion for a one-point-per-wreath thinning.
> Bi-flat voltage is a stronger translation-stable sufficient ansatz, not a
> necessary condition.  Thus (2.3) is no longer the missing algebraic
> identity; the remaining gate is **coarse pointing plus packing
> completion**, with a separate deeper-effect proof unless the stronger
> bi-flat ansatz is available.

## 1. Heat-bath generators

Let `F_m` denote the set of exact middle-wreath factors on `2m+1`
coordinates.  If `F in F_m`, `tau` is a coordinate transposition, and `K`
is a connected component of the `F` versus `tau F` interaction graph, write

\[
                  H_{\tau,K}(F)
\]

for the factor obtained by switching the `F` side of `K` to its `tau F`
side.  These are genuine `0/1` generators of the exact-factor fibre.

For the certified `m=4` circuit, the four-generator path is

\[
\begin{aligned}
 F_1&=H_{(1\,3),K_1}(F_0),& |K_1|&=7,\\
 F_2&=H_{(2\,4),K_2}(F_1),& |K_2|&=2,\\
 F_3&=H_{(1\,5),K_3}(F_2),& |K_3|&=8,\\
 F_4&=H_{(1\,2),K_4}(F_3),& |K_4|&=4,
\end{aligned}                                           \tag{1.1}
\]

where `F_0` is the MSW factor.  The final edge

\[
                         w_4={\bf1}_{F_4}-{\bf1}_{F_3} \tag{1.2}
\]

satisfies

\[
                         B_4w_4=B_3w_4=0,
                 \qquad B_2w_4\ne0.                  \tag{1.3}
\]

The full order lists and a direct verifier are in
[NONLOCAL_HAAR_M4.md](./NONLOCAL_HAAR_M4.md).

This representation is the useful one: the circuit is created by changing
the interaction components available at the current state.  It is not a
combination of components exposed at the original MSW factor.

## 2. The exact scalable lemma

The following is the clean all-dimensional target.

### State-level suspension lemma

Let `m>=4`.  Suppose `F,G in F_m` are reachable exact factors, `G` is one
interaction-component switch from `F`, and

\[
 w={\bf1}_G-{\bf1}_F,
 \qquad B_mw=B_{m-1}w=0.                              \tag{2.1}
\]

There exist reachable exact factors

\[
                    \widehat F,\widehat G\in F_{m+1} \tag{2.2}
\]

such that `widehat G` is one interaction-component switch from
`widehat F`, and linear maps on shadow spaces satisfy

\[
\begin{aligned}
 B_m(\mathbf1_{\widehat G}-\mathbf1_{\widehat F})
    &=L_m B_{m-1}w,\\
 B_{m-1}(\mathbf1_{\widehat G}-\mathbf1_{\widehat F})
    &=J_m B_{m-2}w,                                   \tag{2.3}
\end{aligned}
\]

where `J_m` is injective on the image of legal component effects.

The middle equation

\[
 B_{m+1}(\mathbf1_{\widehat G}-\mathbf1_{\widehat F})=0
\]

is automatic because both lifted states are exact factors.

If this lemma holds, applying it repeatedly to (1.2) produces, for every
`m>=4`, a legal component circuit

\[
                   B_mw_m=B_{m-1}w_m=0,
            \qquad B_{m-2}w_m\ne0.                   \tag{2.4}
\]

Thus (2.3), not another local square identity, is the exact missing
all-dimensional theorem.

The lemma may be weakened: it is enough to lift the particular marked edge
created by (1.1), rather than every edge of the fibre.

## 3. Why the lift must be state-level

Three natural orderwise suspensions of the eight-order certificate were
exhaustively ruled out from `m=4` to `m=5`.

1. Insert a common adjacent pair, allowing an independently chosen gap and
   orientation in each of the eight orders.
2. Insert two antipodal labels, again allowing independent placements while
   preserving each old cyclic order.
3. Use the marked MSW concatenation cut, replacing the old distinguished
   label `9` by either orientation of `(10,9,11)` independently in every
   order.

In each case a meet-in-the-middle enumeration compared all legal four-order
positive and negative extensions.  None simultaneously preserved the new
middle and first-lower shadows.

There is also no direct stability of the generator word (1.1).  At `m=5`,
all component choices under the same three preparatory transpositions were
enumerated, and no final `(1 2)` component was first-shadow invisible.  The
natural alternating extension

\[
 (1\,3),(2\,4),(1\,5),(2\,6),(1\,2)                 \tag{3.1}
\]

also fails, even when every component choice at every stage is allowed.

Therefore a proof of (2.3) must lift **the factor state and its completion
simultaneously**.  It cannot attach two symbols independently to each of
the eight changed cyclic orders, and it cannot keep a dimension-independent
word of coordinate transpositions.

## 4. A Dyck-recursive formulation

The concatenation identity

\[
                         \rho(PQ)=\rho(P)\Vert
                                  (|P|+\rho(Q))        \tag{4.1}
\]

still gives the natural coordinate system for a proof.  What is required is
an affine completion operator

\[
 \Sigma_R:(F,G,K)\longmapsto
       (\widehat F,\widehat G,\widehat K),             \tag{4.2}
\]

indexed by a Dyck suffix `R`, with the following properties.

* The cyclic orders whose Dyck indices end in `R` carry the marked local
  state.
* All other Dyck sectors provide a completion common to the two sides.
* `widehat K` is sealed in the new interaction graph, so switching it alone
  is legal.
* The cut table across the `R` boundary proves (2.3).

The crucial point is the second bullet: the completion is allowed to depend
on the current factor state.  The failed orderwise insertions omitted this
global correction.

This is now a precise recursive-stability problem.  A candidate
`Sigma_R` can be checked using only:

1. exact ownership of middle masks in the affected Dyck sectors;
2. connected-component sealing at the chosen transposition; and
3. the two shadow identities (2.3).

No raw search over universal OR arrays is involved.
