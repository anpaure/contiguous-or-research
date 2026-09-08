# Small-family shadow Hall under forbidden facet choices

Date: 2026-09-09. Pure proof; no execution, numerical census, matching run,
or search. This audits the proposed extension of the
[residence-three root-port theorem](Q3_CANONICAL_PHI_DISJOINT_ROOT_PORT_EXCURSIONS_BY_SHADOW_HALL_20260909.md).

**Conclusion.** Distinctness and the Catalan family-size bound alone do
not make that Hall argument robust to a growing number of forbidden
facets. For every r>=7, an explicit family of at most Cat_r distinct
(r-1)-sets fails Hall after forbidding only

    t_r = ceil(log_4(2(r+1))) - 1

removals at each left vertex. This is O(log r), already much smaller than
the proposed order sqrt(r) allowance. The obstruction is abstract; it is
not shown to arise from the correlated ages of an actual parent carrier.

## 1. A general sufficient robust bound

Let F be a family of distinct k-sets. At each A in F, forbid at most t
of its k facets, where 0<=t<=k-1. Define the real number

    x_t = k-1 + k/(t+1).

If |F|<=binom(x_t,k), then the remaining incidence graph still has a
matching saturating F, for EVERY choice of the forbidden facets.

Proof. For any nonempty subfamily G, write |G|=binom(x,k), x>=k.
The size hypothesis gives x<=x_t. The same continuous shadow inequality
used in the existing root-port proof gives

    |partial G| >= binom(x,k-1)
                = |G| k/(x-k+1)
                >= (t+1)|G|.

There are at most t|G| forbidden incidence edges. A shadow vertex that
vanishes from the remaining neighborhood must lose an incidence edge,
so at most t|G| distinct shadow vertices can vanish. The remaining
neighborhood therefore has at least |G| members. Applying this to every
subfamily is Hall's condition. The empty subfamily is immediate.

For t=0 this is exactly the original threshold binom(2k-1,k). For t>0
it is a sufficient, deliberately unoptimized robustness bound. No claim
that it characterizes the sharp threshold is made. For t>=k an isolated
left vertex is possible, so a nonempty-family universal guarantee fails.

## 2. A concrete forbidden-core obstruction

Set k=r-1. For any integer t with 0<=t<=r-2, put s=k-t>=1.
Choose disjoint sets Z,V of sizes

    |Z|=t,       |V|=2s,

inside the 2r old coordinates other than the distinguished root u.
This fits because |Z union V|=2r-2-t<=2r. Define

    F = {Z union B : B subset V, |B|=s}.

Every member is a distinct k-set. At A=Z union B, forbid precisely the
t removals of elements of Z. Its remaining facets are Z union (B-b),
b in B. Consequently the FULL remaining neighborhood is exactly

    N(F) = {Z union D : D subset V, |D|=s-1}.

Thus

    |F|=binom(2s,s),
    |N(F)|=binom(2s,s-1)=s/(s+1)*|F|,
    |F|-|N(F)|=binom(2s,s)/(s+1)=Cat_s > 0.             (1)

This is an explicit Hall failure, with all allowed facets accounted for.
It applies whenever binom(2s,s)<=Cat_r, so the only remaining issue is
an explicit finite choice of t ensuring the required family-size bound.

## 3. A finite logarithmic choice valid for every r>=7

Let t=t_r be the least nonnegative integer with

    4^(t+1) >= 2(r+1).                                  (2)

For r>=3 it satisfies t<=floor((r-1)/2). One way to see this is the
elementary inequality

    2(r+1) <= 4^floor((r+1)/2),

whose two parity base cases r=3,4 are immediate and which is preserved
when r increases by two. Thus s=r-1-t>=1 and t+1<=s+1.

The exact adjacent central-binomial ratio gives

    binom(2r,r)/binom(2s,s)
      = 4^(t+1) product_(j=s+1)^r (1-1/(2j)).

For numbers a_j in [0,1], product(1-a_j)>=1-sum(a_j). Therefore

    product_(j=s+1)^r (1-1/(2j))
       >= 1-(t+1)/(2(s+1)) >= 1/2.

Combining this with (2) yields

    binom(2r,r)/binom(2s,s) >= 4^(t+1)/2 >= r+1,

or precisely

    |F|=binom(2s,s) <= binom(2r,r)/(r+1)=Cat_r.           (3)

Equations (1)--(3) prove the claimed counterexample for every r>=7.
The onset r>=7 agrees with the existing root-port Hall application; no
optimal onset or smallest possible t is claimed.

If a family of EXACTLY Cat_r left vertices is desired, append arbitrary
new distinct k-sets. There are enough available because

    binom(2r,r-1)=r Cat_r.

Assign the added left vertices any permitted facet lists. The original
subfamily F retains the same deficient neighborhood, so Hall still fails.

For t=O(log r), the exact product also shows

    binom(2(r-1-t),r-1-t)/Cat_r
       = (r+1)/4^(t+1) * (1+O((t+1)/r)).

This explains the logarithmic scale without any numerical computation.
The finite proof above, rather than this asymptotic expression, establishes
the asserted counterexamples.

## 4. What this does and does not say about larger residence

At the q3 entrance, every candidate second old deletion is present in
three successive states, so no facets are forbidden by age. For a larger
required residence q, the proposed bound allows at most q-3 forbidden
removals per left. Whenever

    q-3 >= ceil(log_4(2(r+1))) - 1,

the preceding construction is already permitted by that ABSTRACT bound:
it uses only t_r forbidden removals. In particular, an allowance of
order sqrt(r) cannot be handled using only distinctness, cardinality at
most Cat_r, and an arbitrary per-left bound of q-3.

This does not refute an actual larger-q root-port construction. Its left
sets also satisfy prefix-walk constraints and arise as specific parent
successors; its forbidden coordinates are the young coordinates from
actual predecessor histories. The common forbidden core Z and the whole
family F above have not been realized under those correlated conditions.
A positive extension must exploit such additional structure, strengthen
the available-neighborhood estimate, or change the entrance architecture.
The unrestricted q3 Hall theorem remains unchanged.
