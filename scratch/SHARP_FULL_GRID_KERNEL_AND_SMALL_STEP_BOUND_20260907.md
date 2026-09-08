# Sharp full overlap kernel and its small-step factor

Date: 2026-09-07. Symbolic synthesis of the four-prefix allocation proof
(chat02), geodesic variation-box proof (chat04), and the coordinator's
anchored counting. No computation. This note does not prove maintained
regularity or a near-perfect matching.

## 1. Finite setup

Let P be a family of b-subsets of a 2b-set, each a union of prefixes of
four fixed disjoint ordered coordinate groups. Suppose P is covered by t
Johnson geodesics. Its common included and common excluded sets each have
size at least b-a, where 1<=a<b. Develop P under coordinate permutations,
retaining distinct hyperedge supports. Let D be the resulting degree.

The folded version uses antipodal pairs as vertices and requires the
ambient Johnson diameter of P to be less than b/2. In that version D
always denotes the FOLDED degree, not the ordinary degree. A fixed folded
edge is represented by its coherent oriented copy of P.

Fix an anchor v in an edge E and define

    K_v(z)=sum_{S subset E, v in S, |S|>=2}
               z^(|S|-1) deg(S)/D,          z>=0.

Equivalently, if Q is a uniform simple orbit edge containing v, then
K_v(z)=E[(1+z)^(|E intersect Q|-1)]-1.

Write

    F(x)=(1-x)^(-8)-1-8x,
    beta=(4a/b)(1+z)^(t/2).

**Theorem.** If beta<1, then

    K_v(z) <= (1+z)^(t-1) F(beta),                       (1)
    K_v(z) <= z t (1+z)^(t-2) beta F'(beta).             (2)

Here beta F'(beta)=8beta[(1-beta)^(-9)-1]. Both bounds are uniform
over anchors and coordinate-developed edges. The second, unlike a
coarse subset bound, vanishes at z=0 and retains a linear small-z factor.

## 2. Proof, including disconnected overlap families

For S containing v let I=intersection S, J=union S, U=J minus I,
d=|v minus I|, e=|J minus v|, and u=d+e. Then d,e<=a, and u>=2 for
a nontrivial family.

Condition on a specified source anchor mapping to v. Assign the u
variable target coordinates to the four ordered source groups, in at
most4^u ways. Within a group their membership signatures must form a
chain under inclusion. Its order is forced; the anchor prefix cut fixes
the constant included portion and every variable signature interval.
Thus each assignment gives at most one compatible ordered source tuple.
Repeated assignments or incompatible tuples only enlarge this bound.

For a compatible tuple the exact conditional permutation probability is
the product of all Venn-atom factorials divided by b!^2. The variable
atoms inside v have total size d, so their factorial product is at most
d!; those outside contribute at most e!. Hence

    deg(S)/D <= 4^u / [binom(b,d) binom(b,e)]
              <= (4a/b)^u.                              (3)

The anchor roles partition the conditioning event, so averaging adds no
factor |P|. In the folded case any mixed signs would map a pair at
distance less than b/2 to one at distance greater than b/2. All signs
are therefore global, even for disconnected S, and merely exchange d,e.
Uniform coordinate permutations give uniform simple orbit edges.

The variation set U is specified by a lower and upper extent from the
anchor cut in each of four groups. There are at most binom(u+7,7) such
eight-ray choices of total size u. On each covering geodesic, vertices
agreeing with v outside U form an index interval; its endpoints differ
on at most u coordinates. It has at most floor(u/2)+1 vertices. Thus
the number n_U of eligible template vertices is at most t(u/2+1).

The weighted sum of NONTRIVIAL subsets of those vertices containing v
is exactly (1+z)^(n_U-1)-1. Bounding it first by
(1+z)^[t(u/2+1)-1], multiplying (3), and summing u>=2 proves (1).

For the small-step refinement, use

    (1+z)^(n_U-1)-1 <= (n_U-1)z(1+z)^(n_U-2)
                      <= t u z(1+z)^[t(u/2+1)-2],

since u>=2. The remaining series is
sum_{u>=2} u binom(u+7,7) beta^u=beta F'(beta), proving (2).
No probability product over disconnected components has been used.

## 3. Independent retention and polynomial density

Let the orbit hypergraph have uniformity r and N vertices. Independently
retain its vertices with probability rho, condition on retaining v, and
let X_v count wholly retained incident edges. Exactly

    mu=E X_v=D rho^(r-1),
    Var(X_v)/mu^2=E_{E,Q containing v}
                         [rho^(-(|E intersect Q|-1))]-1.

Thus either bound (1) or (2) at z=rho^(-1)-1 bounds this variance,
with

    beta_rho=(4a/b)rho^(-t/2).

For the crossed-rail grid, a=8Kh and t=4(2K+1). At fixed K and
h=Theta(sqrt b), setting rho=b^(-gamma) gives beta_rho->0 and

    Var(X_v)/mu^2=O_K(b^[-1+gamma(2t-1)])                (4)

whenever gamma<1/(2t-1). At slowly growing K the same finite bound is
used without treating K-dependent constants as fixed. The diagonal
term in the second moment is included; no separate omission of identical
edge pairs is permissible.

## 4. Why the small-step factor matters

For z near zero and beta bounded away from one, (2) is

    K_v(z)=O(z t (a/b)^2 (1+z)^(2t-2)).                 (5)

In the grid scale h=Theta(sqrt b), r=Theta(K^2 sqrt b), a=Theta(K sqrt b),
t=Theta(K), take lambda=epsilon/r and z=exp(lambda)-1. For bounded
epsilon and slowly growing K, (5) becomes

    K_v(z)=O(epsilon K / b^(3/2)).                       (6)

This is a static, anchored kernel bound at a small argument. It does not
say that the induced hypergraph after many selections has the same
kernel. That persistence is a separate requirement.

For orientation, the exact first-proposal comparison is elementary.
In a D-regular r-uniform hypergraph with maximum pair codegree delta D,
run independent Poisson edge clocks of rate lambda/D for unit time and delete
their incident vertices. For a vertex set S, let N(S) be the number of
edges meeting S. Then

    0 <= |S|-N(S)/D <= delta binom(|S|,2),
    P(S survives)=rho^|S| exp(lambda[|S|-N(S)/D]),
    rho=exp(-lambda).

Conditional on an anchor surviving, its induced degree Y_v satisfies

    D rho^(r-1) <= E Y_v
      <= D rho^(r-1) exp(lambda delta binom(r,2)),
    Var(Y_v)/(E Y_v)^2
      <= exp(2lambda delta r^2)[1+K_v(rho^(-1)-1)]-1,    (7)

provided K_v is replaced by a uniform rooted-kernel bound over reference
edges when necessary. The joint survival formula for two incident edges
proves (7) directly; no independent vertex-retention assumption is made.

Keeping only proposed edges that meet no other proposed edge gives an
integral matching. The expected number of deleted vertices not covered
by this matching is at most N r lambda^2, by a union bound over ordered
intersecting proposed edge pairs at each vertex. With lambda=epsilon/r
this waste is O(epsilon) of the expected removed mass. This first-step
fact does not establish a maintained multi-round state hypothesis.

At the initial grid catalogue in the stated a=o(b), slowly growing-K
regime, delta=O(b^(-2)), so the correction term
lambda delta r^2 in (7) is O(epsilon K^2/b^(3/2)). These estimates
motivate a multi-round argument; they do not substitute for it.

Independent root-agent audit passed the full proof, including the
small-z refinement and the anchor-conditioned one-proposal comparison.
Chat02 independently checked these same finite bounds.
