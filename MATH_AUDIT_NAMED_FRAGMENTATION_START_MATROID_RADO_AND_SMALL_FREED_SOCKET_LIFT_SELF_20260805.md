# Self-audit: named fragmentation, collar-start Rado, and freed sockets

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_NAMED_FRAGMENTATION_START_MATROID_RADO_AND_SMALL_FREED_SOCKET_LIFT_20260805.md`  
**Method:** line-by-line pure-mathematical audit; no computation, search, or
solver  
**Verdict:** **GO in the stated scope.**  The fixed-bank criterion and the
co-selected Rado criterion are exact.  The protected-start and small-bank
claims follow from the cited Boolean surplus theorem.  The physical
freed-socket result is valid only as the stated reserved-pair overlay; it
does not name or attach the unrestricted bulk.

## 1. Parameter and load check

At new depth `D^+=D+1`, the collar bottom is `b=r-D^+`.  A collar chain
starting in rank `u` contains `r-u` marked collar cells, so the available
residual load is

\[
 D^+-(r-u)=u-b.
\]

For a residual chunk `F` of length `ell_F` and top `S_F`, attachment to a
socket with bottom `T_D` and start rank `u_D` is therefore equivalent to

\[
 S_F\subset T_D,
 \qquad
 \ell_F\le u_D-b.
\]

Once the two named banks are fixed, injective attachment is consequently
exactly ordinary bipartite Hall.  No hidden rank or capacity inequality is
missing from Theorem 1.1.

## 2. Collar-start matroid and Rado check

For `b<u<=r`, let `M_u` be the transversal matroid on the rank-`u` shore
of the Boolean inclusion graph from ranks `u-1` to `u`.  Normalized
matching gives rank `C_(u-1)`.  A subset `Z_u` of the rank-`u` shore is a
base of `K_u=M_u^*` if and only if its complement is a base of `M_u`, hence
is the image of a matching saturating the entire rank-`u-1` shore.

Choosing these matchings independently at every collar interface gives a
genuine chain forest: every non-top vertex has one outgoing edge; every
upper vertex either has one incoming edge or is a declared start; and all
rank-`r` owners occur once.  Conversely, every saturated collar forest
induces exactly such bases.  The direct sum over tagged ranks is therefore
the correct start matroid.

Rado's theorem applied to candidate sets

\[
 N(F)=\{(u,T):b+\ell_F\le u\le r, S_F\subset T\}
\]

is exactly equivalent to choosing distinct compatible starts which extend
to one collar forest.  Thus the all-cut condition

\[
 r_{\mathsf K}(N(X))\ge |X|
\]

is necessary and sufficient, not merely sufficient.

## 3. Protected-start reserve check

At the interface from rank `u-1` to rank `u` in `B_(2r)`, Proposition
1.2A of the cited nested-intersection theorem gives

\[
 \eta_{u-1}=\left\lfloor\min\left\{
 2r-u,
 { (2r-2u+1)(2r-u)^2\over u}
 \right\}\right\rfloor.
\]

For `u<=r`, both terms inside the minimum are at least `r`.  Hence deleting
any at most `r` proposed starts still leaves a matching saturating the
lower shore.  This is precisely independence in the dual start matroid.

For a chunk top of rank `s<u`, the number of containing rank-`u` sets is

\[
 \binom{2r-s}{u-s}\ge 2r-s\ge r+1.
\]

Therefore a group of at most `r` chunks assigned to one rank satisfies
ordinary Hall: every nonempty subfamily has a candidate union of size at
least `r+1`, while the whole group has size at most `r`.  The selected
starts are then independent by the preceding paragraph.  Tagged ranks are
independent summands, proving Theorem 4.2.  A total `O(D)` bank is covered
eventually because `D=Theta(sqrt(r))<r`.

## 4. Freed-socket overlay check

Theorem 5.1 starts from `h` **already reserved distinct anonymous**
old-singleton/socket pairs.  This hypothesis is essential and is explicit
in the audited source.

For pair `i`, old bottom `t=b+1` and old type `c_i>=1` put its collar start
at

\[
 u_i=t+c_i=b+1+c_i.
\]

Its old capacity is `c_i`; after the depth shift its capacity is `c_i+1`.
The small-bank theorem co-chooses distinct containing starts `T_i` at these
ranks.  Since `u_i>=b+2`, every `T_i` contains at least
`binom(b+2,2)` rank-`b` subsets.  Under the displayed hypothesis this is at
least `h`, so Hall chooses distinct `A_i subset T_i`.

At the last old residual interface, deleting the `A_i` from the rank-`b`
shore leaves a complete matching from rank `b-1` by the same protected-top
reserve (now with `h<=r`).  Thus each `A_i` is one of the exactly `H_b`
unmatched rank-`b` starts.  The additional assumption `h<=H_b` lets the
canonical colour-passing rule assign distinct newly born length-one job
colours to those starts.  Lower interfaces can then be named successively
by the interval-histogram Boolean lift.

The collar chainization reserves the `T_i` as starts.  Restricting the new
collar forest from bottom `b` to the old collar ranks `t,...,r` does not
change any `T_i`, because every `u_i>=b+2`.  Hence `A_i subset T_i` uses the
named occurrence at old depth.  The singleton job vanishes in the new
residual system, while the same occurrence gains one capacity unit and
accepts `F_i` because `ell_(F_i)<=c_i+1` and `S_(F_i) subset T_i`.

This proves only the named realization of the reserved exceptional pairs.
The anonymous bulk retains the complementary type counts, but attaching
its named chunks to the complementary starts is exactly the unresolved
bulk Rado gate.  The source states this restriction.

## 5. Bulk frontier and no-overclaim check

For complete occurrence-labelled layer batches, the earlier joint-start
orbit lift verifies all Rado cuts.  For an arbitrary integral interval
fragmentation, the interval Boolean theorem supplies named chains but does
not guarantee that some such naming meets the collar-start Rado cuts.
Choosing interval labels and start-matroid representatives is one
correlated problem.

The determinant-two variable-slot minor rules out a generic total-
unimodularity proof only.  It is not a counterexample in the dense Boolean
instance.  Conversely, normalized shadow or random-SCD marginals alone do
not imply every Rado cut.  The audited source correctly leaves this bulk
choice open and does not claim serialization, residence, upper coverage,
topology, fractional configuration feasibility, or the full additive
upper bound.

## 6. Final audit verdict

The theorem package proves exactly:

\[
 \boxed{
 \begin{array}{c}
 \text{fixed named banks}\iff\text{ordinary Hall},\\
 \text{co-chosen collar starts}\iff\text{Rado in }\bigoplus_u\mathsf K_u,\\
 O(D)\text{ exceptional starts lift for large }r,\\
 \text{and reserved vanished-singleton sockets can be named faithfully.}
 \end{array}}
\]

It does **not** prove the corresponding statement for the unrestricted
configuration-rounded bulk.  Within that scope, the audit verdict is GO.
