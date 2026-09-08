# Hostile audit of the endpoint-corrected PBBS collar/backup directed factor

**Date:** 2026-08-13  
**Audited theorem:** Theorem 3.1 of
`MATH_THEOREM_PBBS_SYNCHRONIZED_COLLAR_PLANTING_DECISION_AND_EXACT_SOURCE_HOST_QUANTIFIER_20260813.md`  
**Audited SHA256 after scope correction and source-section extension:**
`30102c3f348618460ef9515bc4ea3daa26f695a02b15f3be7d8932e6acc433c1`  
**Verdict:** **PASS for the high-height graph face after two scope details
were made explicit:** the common tag reservoir is enlarged before collar
selection by the tags needed at all free forced ports, and heights `2,3`
are excluded unless a separate compatible bounded planting is supplied.
The conclusion is a genuine simple directed spanning two-factor of the
middle-level incidence graph, not merely two separately extendible partial
matchings.  It remains only a graph theorem.

## 1. Endpoint degrees and simplicity

At high height `h`, retain incoming collars at

\[
                         P_{h,i},\qquad i=1,2,3,4,   \tag{1.1}
\]

and put one outgoing full-union collar at `Q_(h,0)`.  The only equality
between a high `P` endpoint and a high `Q` endpoint is

\[
                         P_{h,0}=Q_{h-1,1}=U_h.     \tag{1.2}
\]

No collar is placed at `P_(h,0)`.  The owner `U_h` therefore sees exactly
the two adjacent height-spine edges and has protected degree two.  Each
owner in (1.1) sees its pentagon edge and its incoming collar edge.  Each
`Q_(h,0)` sees its pentagon edge and its outgoing collar edge.  Every other
pentagon endpoint has degree at most one.  Thus no endpoint has protected
degree greater than two.

Give every one of the five collars at every high height a distinct tag in
the common reservoir and make its deletion set contain exactly that tag.
Every positive collar owner and collar lower facet then has the one-missing-
tag signature belonging to its collar.  Every pentagon owner and pentagon
lower facet contains the full tag bank.  Consequently:

* collar interiors on different paths are disjoint;
* no collar interior meets a pentagon resource;
* the first collar facet is different from the adjacent pentagon facet;
* endpoints cannot equal collar interiors; and
* within one collar, owner and lower-facet simplicity is the audited
  sliding-window lemma.

The `P` endpoints are mutually distinct, the `Q` endpoints are mutually
distinct, and (1.2) is their only cross-family equality.  The protected
owner graph is therefore a path forest.  Its incidence lift has every used
lower vertex of degree two and every owner of degree at most two, so it is
exactly the type of incidence path forest required by the protected-factor
theorem.

The high bank has

\[
 e=10(H-4)(r+4)+O(1)=O(Hr),                        \tag{1.3}
\]

and the established bounds

\[
 \alpha\le85(H-4)+O(1),\qquad
 \beta\le30(H-4)+O(1).                              \tag{1.4}
\]

For `H=O(sqrt(r))`, these are `e=O(r^(3/2))` and
`alpha,beta=O(sqrt(r))`.

## 2. The residual upper bank is fixed before completion

The four incoming collars retain one common cumulative-union profile.  The
outgoing role-zero collar is protected data as well.  Therefore every
unmatched one-cut or zero-arc two-cut target is determined before any
unprotected factor edge is selected.  Multi-cut intervals containing a
complete positive-length collar have full-ground value.  The audited
product-antichain/nested-profile argument gives, at every excess rank,

\[
                         |\mathcal D_s|=O(HR)       \tag{2.1}
\]

and total target count `O(HR^2)`.  The first nontrivial protected exterior
letter makes these residual ranks at least `R+2`; immediate-upper values
are already covered on the high face.  Thus the rank-stratified backup
theorem applies with

\[
                         M=O(HR)=O(R^{3/2}).        \tag{2.2}
\]

Its witness for `Z in D_s` is the simple owner path

\[
 V_i=C\cup\{b_1,\ldots,b_i\}
       \cup\{a_{i+1},\ldots,a_s\},\qquad0\le i\le s,\tag{2.3}
\]

where `|C|=R-s` and `|A|=|B|=s`.  It has rank-`R` owners,
distinct lower facets, and complete union `Z`.  The theorem selects all
such paths mutually owner/facet-disjoint from the enlarged forced base,
with polynomial total size and combined exposures at most `R/3`.  Hence
the backups are an **unoriented incidence path forest**, not a collection
of marginal witnesses in separately chosen factors.

## 3. Tagged forced-component chain

Before any collar deletion set is fixed, enlarge the common high tag
reservoir by one fresh tag for every free forced endpoint not already the
far end of a tagged collar.  Only `O(H)` tags are needed, whereas the
reservoir has `R-O(H)` coordinates.

An all-tag free endpoint receives a one-edge whisker deleting its fresh
tag.  Fresh one-missing-tag signatures make those whiskers disjoint from
the collar bank.  Every forced component now has distinct entrance and exit
port tags.  Joining an exit tag `a` to the next entrance tag `b` by the
pair-tag geodesic gives internal owners and facets with signature

\[
                         T\setminus\{a,b\}.         \tag{3.1}
\]

Every unordered tag pair is used once.  These connectors are therefore
mutually disjoint and disjoint from the zero/one-missing-tag base.  They
join all `q=O(H)` forced components into one oriented protected owner path,
add `O(HR)` incidence edges, and add `O(H)` to each exposure.

The enlarged forced path still has `O(HR)=O(R^(3/2))` vertices, so it meets
the forbidden-base size and `o(R)` exposure hypotheses of the backup
packing theorem.  Selecting the backups *after* this chain is built makes
their avoidance quantifier correct.

## 4. Factor extension and orientation

After the backups are added, the whole protected bank is one incidence
path forest plus unoriented disjoint backup paths, has polynomial edge
count, and has

\[
                         \alpha,\beta\le R/3.       \tag{4.1}
\]

On a ground set of size `2R-1`, the polynomial protected-forest theorem
therefore extends this exact forest to a **simple spanning two-factor** of
the balanced middle-level incidence graph.  This is stronger than extending
the two alternating partial matchings separately: no common coloured edge
or directed two-cycle is introduced.

The complete forced bank lies on one oriented protected path.  Any factor
cycle containing that path has one orientation agreeing with it.  Orient
that cycle accordingly and orient all other factor cycles arbitrarily.
The backup paths were deliberately left unoriented, so they cannot create
an orientation contradiction if the completion puts several of them on
one cycle.  The output is consequently a genuine simple directed spanning
two-factor.  Contracting its lower shore gives exact owner degree two and
uses every lower-`q1` colour once.

## 5. Scope corrections and remaining boundary

The common high reservoir does not automatically separate a pre-existing
realization at heights `2,3`.  The proof-safe theorem omits those bounded
heights, paying their targets as a bounded terminal bank, or includes them
only after an explicit compatible bounded planting.  This has no effect on
the asymptotic graph statement or on a `B(k)+O(1)` target.

Nothing in this audit upgrades the output to a literal source carrier.  In
particular, the unprotected completion may have short coordinate runs, the
prescribed histories may fail their pinned erosion halos, and the typed
suffix cap may have deficient rank.  The directed two-factor conclusion is
fully graph-theoretic and should not be cited for any of those three rows.

The rebind from the previously audited SHA changes the source-host discussion
after Theorem 3.1, not the protected graph bank or its proof.  The graph PASS
therefore remains valid for the current bytes.  It is now complemented by the
separate deterministic spine-residence no-go: the very protected spine which
makes this graph face possible prevents it from being a literal
depth-`delta` source face in the nonvacuous height range.
