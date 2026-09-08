# Independent audit: Boolean rail fibres, Euler fusion, and exact cut charge

**Date:** 2026-08-02  
**Status:** independent line-by-line proof audit of
`MATH_THEOREM_K_BOOLEAN_RAIL_INTERVAL_HALL_AND_COMPLETE_TRANSITION_EULER_FUSION_20260802.md`
and
`MATH_THEOREM_K_BOOLEAN_INTERVAL_FIBRE_HALL_AND_SHADOW_RESERVED_TREE_20260802.md`.
One scope correction was made to the SCD calibration: it is root/target
exact before the trace-owner row, not an owner-exact fixed-`T_i` instance.
No finite search was used.

## 1. Predecessor and fibre replay

For role `i`, a chosen trace has tail

\[
       (B,A_{i,1},\ldots,A_{i,d-1})
\]

and fixed head `h_i=(A_(i,1),...,A_(i,d))`.  Equating the tail to head
token `h_j` forces

\[
 B=A_{j,1},\qquad
 (A_{j,2},\ldots,A_{j,d})
 =(A_{i,1},\ldots,A_{i,d-1}).                               \tag{1.1}
\]

The owner identity is

\[
 B\cup U_i=T_i
 \iff T_i\setminus U_i\subseteq B\subseteq T_i.             \tag{1.2}
\]

Thus Lemma 1.1 and formulas (2.4)--(2.5) of the rail theorem are exact.
They count occurrence tokens, so duplicate physical heads cause no error.
Every assignment lies in one and only one rail fibre
`rho_j=lambda_i`; hence fibrewise perfect matchings are equivalent to
balanced one-copy selection.

The degree-domination proof is valid: edges incident with
`X subseteq R_w` number at least `delta_w|X|` and at most
`Delta_w|N(X)|`.

## 2. Complete-transition and rectangle replay

For a fixed rail `w`, every pair `(j,i)` is legal iff

\[
                    P_i\subseteq c_j\subseteq T_i.           \tag{2.1}
\]

Taking the union over `P_i`, intersection over `c_j`, union over `c_j`,
and intersection over `T_i` gives exactly the two cap tests

\[
 \bigcup_iP_i\subseteq\bigcap_jc_j,
 \qquad
 \bigcup_jc_j\subseteq\bigcap_iT_i.                         \tag{2.2}
\]

The rail edge of role `i` is `lambda_i -> rho_i`.  Balance is
`out(w)=|R_w|=|H_w|=in(w)`.  A connected balanced rail multigraph has an
Euler circuit.  If edge `j` is followed by edge `i`, then
`rho_j=lambda_i`; (2.2) supplies the remaining owner containment.  The
Euler order therefore gives a literal predecessor cycle on all occurrence
roles and preserves every fixed owner and marked payload.

For two distinct transition cycles, replacing matched pairs
`j-i,j'-i'` by `j-i',j'-i` cuts one arc from each cycle and cross-joins
the two paths.  It therefore merges, rather than splits, the cycles.  If
the rail multigraph is connected and every fibre is complete, two circuits
in any circuit decomposition meet at a rail vertex, so such a rectangle is
available.

The Woodall statement is used only as a sufficient condition on the
loopless cloned predecessor digraph.  Contracting a protected path is
sound only after arcs into the contracted vertex are restricted to arcs
into the path's first role and arcs out are restricted to arcs out of its
last role, exactly as stated.  It is not claimed that an arbitrary pinned
path passes the contracted degree test.

## 3. Singleton and SCD scope

When all chain differences and the owner gap are singletons, predecessor
compatibility fixes the first head block and the remaining `d-1` blocks.
If the full marked chains are distinct, at most one head token has that
word.  Hence every role has predecessor degree at most one; any cycle cover
and its component profile are forced.

The `(7,3,3)` recursive-SCD dead flag independently confirms that a
root/target-exact SCD table may have a zero successor row.  Its turn owner
is selected only after attaching a predecessor, so it is not an
owner-exact fixed-`T_i` table of the rail theorem.  The rail note was
patched to make this scope explicit.  The example refutes
root/target-exactness plus raw Johnson degree as a chronology theorem; it
does not refute the stronger fixed-owner hypotheses.

## 4. Boolean-interval formula audit

Fix a spine `s`.  The realized neighbours of role `i` are exactly

\[
 \{(C,s):a_s(C)>0,\ K_i\subseteq C\subseteq T_i\}.            \tag{4.1}
\]

Because `T_i=K_i dotcup U_i`, the ambient menu has size `2^|U_i|` when
`K_i` is nonempty, and `2^|T_i|-1` otherwise.  Intersecting several lists
replaces their lower ends by the union of the `K_i` and their upper ends by
the intersection of the `T_i`; the degree, codegree and weighted Hall
formulas follow.

For a reservation `R`, residual Hall subtracts exactly `b_s(C)` from tail
capacity and deletes the reserved roles.  Therefore the cutwise budget

\[
 b_s(N(X))\le a_s(N(X))-|X|                                 \tag{4.2}
\]

for every unreserved role family is necessary and sufficient.  In
particular no tail capacity may be spent inside a tight pre-reservation
shore.

## 5. Uniform containment charge audit

Between `a`-sets and `b`-sets of an `n`-set, the two degrees are

\[
 D=\binom{n-a}{b-a},\qquad E=\binom ba.                      \tag{5.1}
\]

With `g=gcd(D,E)`, `p=D/g` role copies per `a`-set and `q=E/g`
capacity units per `b`-set balance because

\[
 \binom naD=\binom nbE,
 \qquad p\binom na=q\binom nb.                              \tag{5.2}
\]

For `Y` on the `b`-shore and
`Z={K:N(K) subseteq Y}`, one has `N(Z) subseteq Y`.  Moreover

\[
 E|N(Z)|-D|Z|=e\left(\binom Qa\setminus Z,N(Z)\right).       \tag{5.3}
\]

Consequently

\[
 q|Y|-p|Z|
 =q|Y\setminus N(Z)|
   +{e(\binom Qa\setminus Z,N(Z))\over g}.                   \tag{5.4}
\]

This verifies identity (3.7).  In a connected containment graph equality
can hold only at the empty and full dual cuts.  All quantities are integral,
so every proper cut has charge at least one.

If a reservation uses `u_R(Y)` tail units in `Y` and deletes
`r_R(Z)` role copies indexed by `Z`, its residual dual charge is exactly

\[
        \kappa(Y)-u_R(Y)+r_R(Z).                             \tag{5.5}
\]

This proves Corollary 3.3, including the one-charge sufficient condition.

For the one-sided shadow lemma, complementing an `a`-family and applying
Lovasz--Kruskal--Katona gives the adjacent surplus `n-a-1` when
`a+1<=floor((n-1)/2)`.  The derivative check is

\[
 {d\over dx}\log\left(\binom{x}{k-1}-\binom{x}{k}\right)
 =\sum_{j=0}^{k-2}{1\over x-j}-{1\over2k-1-x}\ge0,
\]

because `x<=n<=2k-3`, where `k=n-a`.  Normalized matching and monotonicity
of binomial coefficients extend this to every
`a<b<=floor((n-1)/2)`.  The range and arithmetic are therefore sound.

## 6. Exact conclusion

The Boolean lower-side gate is now separated into:

1. choose an owner/target-exact table whose **realized**, spine-conditioned
   interval graphs satisfy Hall;
2. select a distinct-role projected tree which obeys every cut-charge
   budget; and
3. use the residual exact matching to obtain the one-cycle chronology.

Complete transition fibres and Woodall's condition are unconditional
sufficient faces.  On a balanced uniform containment fibre, (5.4) gives
the exact budget for a prospective tree.  Neither theorem proves that the
canonical triangular table lies on those faces.  Raw Boolean menu size is
insufficient: a literal role can have `2^q` leading letters but no realized
head in its interval.

Upper interval decks, residence, exterior opening and terminal common-cap
compilation remain separate.
