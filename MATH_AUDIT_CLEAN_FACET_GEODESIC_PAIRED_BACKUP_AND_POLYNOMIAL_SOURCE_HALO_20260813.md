# Audit of the ordered clean-facet source-halo theorem

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_CLEAN_FACET_GEODESIC_PAIRED_BACKUP_AND_POLYNOMIAL_SOURCE_HALO_20260813.md`  
**Audited SHA-256:**
`d59fae9de89d21e58a3e368cc9f42bbe4dd6c213270365f360babc59cb716f3e`  
**Verdict:** **PASS, with the residence qualification in the source
statement essential.**

## 1. Local package and halo algebra

For `|S|=R-q` and `Z=\bar S`, the lower-shore geodesic has

\[
 L_j=C\cup\{d_{j+1},\ldots,d_q\}
       \cup\{i_1,\ldots,i_j\},
\]

and its owner at step `j` is

\[
 A_j=C\cup\{d_j,\ldots,d_q\}
       \cup\{i_1,\ldots,i_j\}.
\]

Hence `\bigcup_jA_j=Z`; complementation gives
`\bigcap_jW_j=S`.  Three successive owners cannot lie in one
rank-`(R-1)` star, and three successive facets cannot lie below one
rank-`R` owner.  Thus each of the two central paths contributes at most
two resources to a fixed exposure row, as used in Step 2.

The four deletion/insertion banks in Sections 3--4 give monotone
coordinate words.  The forced first exchanges on the upper-witness path
reuse precisely `L_0,L_q`; they do not create a third protected incidence
at either endpoint.  After the two arms are attached, every protected
lower vertex has degree two and every protected owner has degree at most
two, so the union is an incidence lift of a vertex-disjoint owner-path
forest.

The only delta from the initially inspected bytes is the added
cross-halo disjointness argument in Corollary 4.1.  It is valid.  Every
owner in an intersection-side arm retains at least
`R-q-(d+1)` elements of `S`, whereas every owner in an upper-side arm has
at most `d+1` elements of `S`.  Under `q<=d` and `R>=3d+3`, the former is
at least `d+2`, strictly larger than the latter.  Owners therefore cannot
coincide.  An intersection-side lower facet retains at least
`R-q-(d+1)>=d+2` elements of `S`, while an upper-side lower facet contains
at most `d` elements of `S` (the next insertion from `S` occurs only after
that facet).  Thus lower resources cannot coincide either, and the two
collared paths inside each package are resource-disjoint.

For `q<=h<=d`, the window defining `P_{i+h}` contains the whole central
block `W_0,\ldots,W_q`.  It is therefore contained in `S`.  Every
`x\in S\setminus D^+` survives the window ending at `i+d`, and every
`x\in D^+` survives the window ending at `i+q`, since
`D^-\cap D^+=\varnothing`.  This proves the protected union identity
(3.7), and the reflected argument proves it in the reverse orientation.

## 2. Step 2: central-orbit avoidance

Put `N=|Z|=R+q-1`.  At a fixed role the four resource orbits have sizes

\[
 {N\choose R},\quad {N\choose R-1},\quad
 {N\choose q},\quad {N\choose q-1}.
\]

For `3<=q<=d=o(R)`, the minimum is
`{N\choose q-1}`.  At `q=3` it is `Theta(R^2)`, whereas the protected
intermediate bank has only `O(dR)=O(R^{3/2})` resources.  Same-depth
packages add only `O(dq^2)` resources, and packages at smaller depths add
`O(dq^3)`.  Thus the rejection probability, including the `O(q)` roles
of the package, is `o(1)` uniformly.  The conditioning cost is consequently
at most `1+o(1)` for the upper bounds actually used.

For a fixed opposite-shore exposure row, the worst role probability is

\[
 {q\over {N\choose q-1}}.
\]

For example, a fixed rank-`(R-1)` set contained in `Z` has exactly `q`
rank-`R` extensions inside `Z`; the three other role/shore cases give
the same bound by complementation.  Together with
`|\mathcal D_q|=O(dq)` and the four-unit deterministic increment bound,
the sum of conditional means is `o(1)`.  The bounded-increment
exponential-moment estimate therefore gives the stated
`exp(-Omega(R log R))` tail, which safely beats the fewer than `2^(2R)`
exposure rows.

The ordering in Theorem 5.1 is indispensable.  In particular, the proof
would be false with an arbitrary `O(dR)` bank placed before the depth-two
packages, because the relevant depth-two orbit has only `R+1` resources.
The theorem explicitly excludes that order.

## 3. Step 3: conditional shells and stopped exposure

Before the stopping time, fewer than `R/10` used facets lie below the
current owner, and fewer than `R/10` used owners lie above any proposed
facet.  The permitted deletion and insertion banks each have size
`R-O(d)`.  Hence an ordinary reveal has `Omega(R^2)` legal ordered
exchanges; a first upper-halo exchange through its prescribed endpoint
facet has `Omega(R)` legal new owners.  Uniform choice among these legal
exchanges gives an `O(1/R)` conditional upper bound for any prescribed
deletion or insertion label, even after all earlier avoidance choices.

If `x` is a fixed rank-`(R-1)` row and
`a=|U_0\setminus x|`, then reaching an owner containing `x` requires
`a` prescribed deletions and `a-1` prescribed insertions.  Revealing
these distinct labels in order gives

\[
 \Pr(\text{the arm hits the row}\mid\text{past})
 \le {C^a(a!)^2\over R^{2a-1}}.
\]

The facet-row calculation is identical for **new** arm facets, with
possible hits only at steps `a` and `a+1`.  The prescribed endpoint facet
of an upper halo is excluded: it was already counted in the central path
and adds no new beta load.  After that reused facet, a distance-one row
requires the random first insertion and is hit with probability `O(1/R)`.
A forced first deletion either makes the unique
`a=1` event deterministic, which can occur only over a central endpoint
already charging that row, or removes one of at least two required labels
and leaves probability `O(R^{-2})`.  Thus the deterministic alpha charge
is bounded by the central endpoint exposure and the remaining alpha
conditional mean is `O(1)`.

Central resource disjointness implies that at most one arm starts at a
fixed rank-`R` owner.  For beta, all other distance-one starts cost
`O(1/R)` each and all starts at distance at least two cost `O(1/R^3)`.
There are `O(d^3)` arms, so the conditional beta mean is
`O(d^3/R)=O(d)`.  Each arm adds at most two units to a fixed row.  The
bounded-increment Chernoff estimate at threshold `Theta(R)` is therefore

\[
 \exp\{-\Omega(R\log(R/d))\}
 =\exp\{-\Omega(R\log R)\},
\]

again strong enough for the union bound over all rows.  This proves that
the stopped process has a realization which never stops and establishes
the two sub-half exposure bounds.

## 4. Exact scope of the factor and source conclusion

The total bank has polynomial size and the two all-occurrence exposures
are below `R/3`; these are stronger than the hypotheses of the polynomial
protected-forest extension theorem.  Therefore a simple spanning
middle-levels two-factor extension follows.

What survives every extension unconditionally is the local protected
identity (3.7) and the paired proper-upper witness.  Calling the maximal
candidate word an actual source chronology still requires the completed
owner trace to be `d`-resident.  The theorem states this premise
explicitly and does not infer global residence, connectedness, deep
payload coverage, or cap routing from the halo packing.
