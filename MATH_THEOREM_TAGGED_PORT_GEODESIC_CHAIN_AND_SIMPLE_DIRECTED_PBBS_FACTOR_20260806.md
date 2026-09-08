# Tagged-port geodesics synchronize the forced PBBS components

**Date:** 2026-08-06  
**Method:** explicit Johnson geodesics and the polynomial protected-factor
theorem; no computation or search  
**Status:** unconditional owner/`q1` theorem.  A phase-forced bank with
`O(sqrt R)` path components and a common missing-tag reservoir can be joined
prospectively into one consistently oriented protected path.  Unoriented
upper-backup paths may then be added and the whole bank extends to a simple
directed two-factor.  No source antecedent, clipped-residence, or typed-cap
claim is made.

## 1. A two-tag connector

Work in the Johnson graph on the rank-`R` subsets of a ground set `Omega`.
Let `T subseteq Omega` be a tag set.  Say that an owner has **port tag** `a`
when

\[
 A\cap T=T\setminus\{a\}.
\tag{1.1}
\]

### Lemma 1.1 (pair-tag geodesic)

Let `A,B` be rank-`R` owners with distinct port tags `a,b`:

\[
 A\cap T=T\setminus\{a\},\qquad
 B\cap T=T\setminus\{b\}.
\tag{1.2}
\]

There is a shortest Johnson path from `A` to `B` such that every internal
owner and every lower facet on the path has tag trace

\[
 T\setminus\{a,b\}.
\tag{1.3}
\]

In particular the path is simple, its lower facets are pairwise distinct,
and a connector for one unordered tag pair cannot share an internal owner
or lower facet with a connector for another tag pair.

#### Proof

Put `ell=|A\setminus B|=|B\setminus A|`.  Necessarily

\[
 b\in A\setminus B,\qquad a\in B\setminus A.
\tag{1.4}
\]

If `ell=1`, the single edge `A B` works: its lower facet is
`A-{b}=B-{a}` and has trace (1.3).

Suppose `ell>=2`.  Choose

\[
 y\in(A\setminus B)\setminus\{b\},\qquad
 x\in(B\setminus A)\setminus\{a\}.
\tag{1.5}
\]

Both `x,y` are non-tags, because the only tag in the first difference is
`b`, and the only tag in the second is `a`.  Set

\[
 A'=A-\{b\}+\{x\},\qquad
 B'=B-\{a\}+\{y\}.
\tag{1.6}
\]

Both new owners omit exactly `a,b`, both contain `x,y`, and

\[
 |A'\setminus B'|=\ell-2.
\tag{1.7}
\]

Join `A'` to `B'` by any standard shortest geodesic which exchanges the
remaining elements of `A'\setminus B'` for those of `B'\setminus A'`.
Prepend `A,A'` and append `B',B`.  The result has length
`1+(ell-2)+1=ell`, so it is a shortest path from `A` to `B`.

Every internal exchange is between non-tags, proving (1.3).  The first
facet is `A-{b}` and does not contain `x`, whereas every facet of the
middle geodesic contains `x`; the last facet is `B-{a}` and does not
contain `y`, whereas every middle facet contains `y`.  The two boundary
facets are different when `ell>=2`.  The facets inside a shortest Johnson
geodesic are pairwise distinct.  Hence all facets of the concatenated path
are distinct.  Simplicity of the owner path follows from shortestness.
Finally, (1.3) recovers the unordered pair `{a,b}`, proving separation of
different connector paths. \(\square\)

### Lemma 1.2 (one-edge port whisker)

Let `E` be a free rank-`R` endpoint which contains every tag.  Reserve a
tag `g in T` not assigned to any other port and whose one-missing-tag
signature is absent from the existing protected bank.  Choose
`z in Omega\E` so that both `E-{g}` and `E-{g}+{z}` are unused protected
resources.
If every tag lies in `E`, then `z` is automatically a non-tag.  The edge

\[
 E\;--\;E'=E-\{g\}+\{z\}
\tag{1.8}
\]

is a one-edge terminal whisker whose new endpoint has port tag `g`; its
lower facet has the same one-missing-tag signature.  Distinct reserved
tags make distinct whiskers resource-disjoint.

In the PBBS application the freeness premise is enforced prospectively:
insert every whisker tag into the global reservoir before choosing any
collar deletion set, and make every old protected resource have either all
tags or exactly its own collar tag missing.  A fresh whisker signature is
then absent automatically.

## 2. Joining an oriented path forest

Let `P` be a protected owner-path forest with oriented components
`C_1,...,C_q`.  Assume that each component has a declared entrance and
exit port, that all `2q` port tags are distinct, and that each port owner
contains every global tag except its own.  Also assume that no non-port
resource of `P` has an exactly-two-missing-tag signature.  Untagged free
endpoints may first be converted to ports by Lemma 1.2.

### Theorem 2.1 (tagged-port chain)

For any prescribed order of the components, there is a protected owner
path

\[
 C_1\longrightarrow C_2\longrightarrow\cdots
 \longrightarrow C_q
\tag{2.1}
\]

obtained by joining the exit port of `C_i` to the entrance port of
`C_(i+1)` with the pair-tag geodesic of Lemma 1.1.  The added connectors
are mutually resource-disjoint and disjoint from `P` away from their
declared endpoints.

If the ground set has size `2R-1`, then the added connector bank has at
most

\[
 2(q-1)(R-1)
\tag{2.2}
\]

incidence edges.  Its contribution to each protected exposure parameter
is at most `2(q-1)`.

#### Proof

Every port tag is used once.  Hence the unordered tag pair attached to a
connector is unique.  Lemma 1.1 says that all of its internal owners and
lower facets have exactly that two-tag signature.  The base forest has no
such resource and different connectors have different signatures.  This
proves resource-disjointness and makes the concatenation in (2.1) one
simple oriented path.

The maximum Johnson distance between two rank-`R` sets on `[2R-1]` is
`R-1`, giving (2.2) after passing to the incidence lift.

On a shortest Johnson geodesic, a fixed rank-`(R-1)` set is contained in
at most two path owners: two nonconsecutive owners have intersection rank
at most `R-2`.  Dually, a fixed rank-`R` owner contains at most two path
facets: nonconsecutive path facets have union rank at least `R+1`.
Summing over the `q-1` connectors proves both exposure bounds. \(\square\)

The same crude `O(q)` exposure bound covers the at most `2q` one-edge
whiskers.  Thus when `q=O(sqrt R)`, the complete port-and-connector bank
has polynomial size and exposure `O(sqrt R)`.

## 3. Simple directed factor completion

### Theorem 3.1 (one oriented component before completion)

Let `P_forced` be an oriented protected path forest with

\[
 q=O(\sqrt R),\qquad
 e=R^{O(1)},\qquad
 \alpha,\beta=O(\sqrt R),
\tag{3.1}
\]

and suppose it has the tagged-port interface of Theorem 2.1.  Join its
components into one oriented protected path.  Afterward let `P_backup` be
an **unoriented** protected owner-path forest selected against this
enlarged bank, disjoint from it in both owners and lower facets, such that
their union is an incidence path forest and

\[
 e(P_forced\cup P_backup)=R^{O(1)},\qquad
 \alpha,\beta\le R/3.
\tag{3.2}
\]

For all sufficiently large `R`, the union extends to a simple spanning
two-factor.  The factor can be oriented so that every edge of the forced
path has its prescribed direction.  Splitting every oriented factor cycle
into its incoming and outgoing incidence edges gives two disjoint perfect
matchings; in particular no common-edge directed two-cycle occurs.

#### Proof

The tagged-port construction adds only `O(R^(3/2))` incidence edges and
`O(sqrt R)` exposure.  Equation (3.2) therefore satisfies the polynomial
protected-forest extension theorem with a fixed sub-half margin.  It gives
a **simple** spanning two-factor containing the whole protected bank.

All pre-oriented protected resources lie on one path.  The factor cycle
containing that path has a unique orientation agreeing with it.  Orient
every other factor cycle arbitrarily.  The backup paths carried no prior
orientation, so they create no compatibility condition.  On a simple
bipartite factor cycle, the incoming and outgoing incidence classes are
distinct perfect matchings. \(\square\)

## 4. PBBS application

Use Theorem 5.1 of
`MATH_AUDIT_PBBS_TAGGED_COLLAR_ENDPOINT_OVERLAP_AND_RANK_STRATIFIED_BACKUP_20260806.md`,
namely the terminal phase of the endpoint-corrected five-collar PBBS
forest.  It has
`q=O(H)=O(sqrt R)` path components.  Enlarge the common reservoir before
choosing **any** collar deletion set so that it contains:

1. the distinct collar tags already used by the synchronized construction;
2. one fresh tag for every free component endpoint which is not already a
   one-tag collar endpoint.

Require each collar deletion set to avoid every old or new tag except its
own.  The common reservoir has size `R-O(H)`, while only `O(H)` tags are
needed.
Every untagged free endpoint contains the whole reservoir and therefore
gets a one-edge whisker by Lemma 1.2.  Every terminal forced component now
has two distinct tagged **owner** ports.  A singleton component, if one is
present, receives two different whiskers.  Orient each component in its
required PBBS direction and apply Theorem 2.1.

Next select the prospectively named rank-stratified upper-backup paths by
Theorem 7.1 of the same audited file,
treating the enlarged forced chain as part of the forbidden base.  The
backup-packing theorem remains applicable: the new base has polynomial
size and only `O(sqrt R)` additional exposure.  Its construction supplies
an unoriented backup forest satisfying (3.2).  Theorem 3.1 then gives a
simple directed owner/`q1` factor containing:

* every terminal PBBS head edge and synchronized collar;
* all phase-forced pieces in one consistently oriented component; and
* every named upper-backup path.

Thus the earlier separate-colour matching extensions and their possible
common-edge two-cycles are unnecessary on this bank.

## 5. Exact scope

This closes the graph-level **simple/directed/forced-component** row.  The
connectors are planted outside the local PBBS heads and do not delete any
protected owner or upper-backup occurrence.  However a Johnson connector
is not automatically the derivative of the required literal source word.
The theorem does **not** prove:

1. a depth-`delta` antecedent for the completed directed factor;
2. clipped residence across the new connector seams;
3. transport of the strict-lower common histories; or
4. occurrence-labelled, capacity-disjoint typed-cap suffix routes.

Those source/history/cap conditions must be imposed on, or regenerated
after, the simple directed factor.  Consequently this theorem removes one
of the four rows in the five-collar audit, but it is not by itself a proof
of the PBBS correlated planting theorem or of `nu(k)<=B(k)+O(1)`.
