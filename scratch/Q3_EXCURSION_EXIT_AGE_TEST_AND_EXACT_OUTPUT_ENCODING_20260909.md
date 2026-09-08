# Exact parent-continuation test at a q3 excursion exit

Date: 2026-09-09. Status: pure necessary-and-sufficient boundary theorem.
No computation, source preparation, matching run or new construction.

This specializes the existing age interface to the five-step bank in
[the disjoint excursion theorem](Q3_CANONICAL_PHI_DISJOINT_ROOT_PORT_EXCURSIONS_BY_SHADOW_HALL_20260909.md).
The general identification of residence with insertion/deletion gaps is
already in [the long-run reduction, Section2](../MATH_THEOREM_LONG_RUN_MIDDLE_LEVELS_RESIDENCE_REDUCTION_20260802.md).
The new statements below are the exact three exclusion tests at this
particular exit, and its explicit Dyck/prefix encoding. They do not prove
that a simultaneous Hall assignment satisfying the exclusions exists.

## 1. Exit data and exact ages

Retain the fixed-root notation L=0D, root u, parent deletion d=d(L),
P=sigma(L)=L+u-d, and a chosen second deletion e in L minus {d}. Put

    G=L minus {d,e},       K=G+u,
    alpha=kappa(K),        K'=J(K)-u=G+alpha,
    beta=kappa(K'),        T=J(K')=G+alpha+beta.

The six lower states of the child excursion are

    L+a,  L+u,  P+b,  K+a+b,  K'+a+b,  T+a.

At the last state, every member of G has age at least6; alpha has age
exactly2; beta has age exactly1; and the new a has age exactly3. The old
root u and the new b are absent. Alpha and beta are distinct and neither
belongs to G. A deleted coordinate may be reinserted as beta; that does
not alter its fresh age1. All age claims count consecutive lower states,
as in the preceding proof.

## 2. Complete test for following the prescribed parent

Let T_j=sigma^j(T), j>=0, and delta_j=T_j minus T_(j+1). Every delta_j is
a single old coordinate. Follow this parent trajectory in the balanced10
sector, namely T_j+a. Its insertions are child Phi insertions by the
balanced-block identity. Then the concatenation is residence-three valid
for all subsequent steps if and only if

    delta_0 not in {alpha,beta},
    delta_1 != beta.                                  (2.1)

Equivalently, the exact state tests are

    {alpha,beta} subseteq sigma(T),
    beta in sigma^2(T).                               (2.2)

Necessity is literal: deleting alpha or beta on the first step closes a
run of length2 or1. If they survive that step, deleting beta on the second
closes a run of length2. Conversely, (2.1) protects precisely these three
possibilities. By the start of the third transition, every surviving
coordinate inherited from T is at least age3. Every coordinate inserted
after T follows exactly the parent trajectory; the parent's residence-
three property protects it until it is old enough. The same reasoning
applies to an inherited coordinate deleted and subsequently reinserted.
The new a remains present, and b remains absent. Therefore no further
comparison with the parent's incoming age history is needed.

This is an age-continuation statement. Following a parent cycle can still
hit a state reserved elsewhere in the child construction. Such inventory
collisions and global cycle topology are not resolved by (2.1).

## 3. The chosen facet determines two explicit Dyck returns

Index old positions from u=0, and write h(t) for the Dyck height of D
after old position t. Thus h(t)>=0 and h(2r)=0. Let p=max(d,e) in physical
order. Then

    alpha = first position t>=p with h(t)=0,
    beta  = first position t>=p with h(t)=1.            (3.1)

In particular beta<alpha. The latter return can occur at p itself if p
is an up-step from height0; beta may therefore be d or e.

For a direct proof, K is the word 1D with the two old ones d,e flipped
to zero. Before both deletions its height is at least -1. After both its
height is h(t)-3, whose minimum is exactly -3 and whose first attainment
is the first return h(t)=0 after p. This proves the alpha formula. Flipping
alpha raises the suffix by2, giving J(K) minimum exactly -2. Removing its
initial root u lowers every nonempty prefix by2, so K' has minimum exactly
-4. Before alpha, the first such minimum occurs when h(t)=1 after p;
after alpha its height is at least -3. This proves the beta formula.

Consequently the output is the explicit set

    T(e)=L minus {d,e} plus {alpha(e),beta(e)},          (3.2)

and has prefix minimum exactly -3, not merely at most -2.
The accepted-facet predicate is therefore the following finite test:
compute (3.1)-(3.2), read only the first two parent deletion coordinates
at T(e), and apply (2.1). No indefinite age simulation is necessary.

All choices e<d have the same return pair alpha(d),beta(d). Their outputs
are distinct rank-r facets H minus {e} of the fixed rank-(r+1) set

    H=(L minus {d}) plus {alpha(d),beta(d)}.

Choices e>d split according to the two specified returns after e. This
is concrete control of the dependence on e, but it does not by itself
bound how many candidates the parent's deletion colors reject.

## 4. Exact inverse encoding of a named output

The fresh labels can be recovered from T alone:

    beta  = the up-step immediately after T's last height -3;
    alpha = the up-step immediately after T's last height -2. (4.1)

For beta this is the inverse-J formula. To see the second assertion, put
K'=T-beta and U=K'+u=J(K). Before beta, the heights of U are those of T
plus2 and hence at least -1. From beta onwards they equal those of T and
are at least -2. Their last minimum therefore coincides with the last
height -2 in T, and the inverse-J formula recovers alpha as in (4.1).

Conversely take any old rank-r word T starting with zero at u and having
minimum exactly -3. The steps in (4.1) exist because T ends at height -1.
Set K'=T-beta, U=K'+u, and K=U-alpha. The inverse-J calculation gives
J(K')=T and J(K)=U, with beta<alpha and u in K. Thus such T has exactly
one possible first11 old state K for this excursion architecture.

For a prescribed input port L with P=sigma(L), this named T is attainable
by the three-step entrance and fixed closure if and only if

    K subseteq P,       |P minus K|=1,
    the unique e in P minus K is not u.                (4.2)

The size condition follows from the ranks but is included to make the
test explicit. Under (4.2), e belongs to L minus {d} and is automatically
old enough at the entrance. Parent continuation from that output is then
possible exactly when (2.1) holds. This completely identifies the local
named-state/age interface without an unproved endpoint-relabeling freedom.

## 5. What this closes and what it does not

The prior unfiltered shadow theorem proves simultaneous distinct first11
facets. It does not show that Hall survives deleting the facets rejected
by (2.1). No claim is made here that the three tests hold automatically,
that each port has an accepted facet, or that accepted choices can be
made simultaneously. Nor is a counterexample to those possibilities
asserted; none has been proved or computed.

If a selected facet violates (2.1), retaining the same prescribed first
one or two parent transitions is impossible: the indicated literal
coordinate run is too short. A repair must change the selected facet,
change those parent edges, or change the incoming history. Merely waiting
along a closed10-sector path and returning to the same T repeats a child
middle vertex, so it is not a repair within a one-copy minimum-width bank.
This last observation concerns that specific state-preserving delay only.

The next precise task is to arrange accepted facet choices or a compatible
rethreading of the untouched parent states. No broad construction search,
extra age-padding gadget, or computation was performed for this note.

Independent internal review: the structure agent read the complete note
and passed the exact ages and three exclusions, Dyck return formulas,
output minimum -3, inverse prefix encoding and its converse. It explicitly
confirmed that this is a local predicate, not a proof of Hall after
filtering. No computation was used in that review.
