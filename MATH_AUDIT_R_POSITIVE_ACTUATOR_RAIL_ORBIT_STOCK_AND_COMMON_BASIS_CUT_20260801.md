# Independent audit: positive actuator rail, orbit stock, and common-basis cut

Date: 2026-08-01  
Lane: R / age-actuator physicalization / protected stock  
Audited source:
`MATH_THEOREM_R_POSITIVE_ACTUATOR_RAIL_ORBIT_STOCK_AND_COMMON_BASIS_CUT_20260801.md`  
Audited source SHA-256:
`4005cf7ede82235ad1cce11b76fe4a8788932b15e7f0f38815bb9455fd479acb`

## 0. Verdict

The corrected theorem note passes its stated local and conditional claims.
In particular:

1. every strict-positive legal age path of at most `d` transitions has the
   asserted literal owner-simple Johnson lift;
2. its adjacent lower and upper colours are separately injective;
3. the orbit-simple criterion and unit-voltage concatenation theorem are
   exact;
4. the non-equivariant spread inequality is a valid sufficient condition
   after the now-explicit internal-simplicity hypothesis;
5. all constants in the three-strand protected-factor corollary are correct;
6. the polynomial-size `Q<=3k` open-stock extension follows for all
   sufficiently large `k`;
7. the equivariant residual matching quotient is necessary and sufficient;
8. the forced two-matroid common-basis inequality is exactly Edmonds'
   contracted min--max formula; and
9. the protected two-factor condition is exactly the Ore--Ryser cut; and
10. the final zero-accumulation theorem is valid under its strengthened
   literal-packet, guard, matching, and joint-compatibility hypotheses.

This audit does **not** certify existence of the seed required by the final
conditional theorem.  It also does not promote owner-membership run control
to source-letter residence.

The source's final rebase on the independently audited monotone-rotor
theorem is scope-correct: that theorem closes the unconditioned invariant
fractional trace gate, but not a residual circulation conditioned on the
preplanted actuator rows.  No proof below depends on conflating those two
quantifiers.

The source also correctly incorporates the buffered semigroup sequel.  It
closes the integer residue only in the aggregate age-type/signature quotient.
The primitive mixed cycle `(1,2,1)<->(2,1,1)` shows why this is not yet a
one-copy labelled factor.  Accordingly, NRFC owner/nested-target colouring
and rethreading remains prior to the Ore--Ryser and compiler rows audited
below.

The latest OFHT rebase is also scope-correct.  Complete labelled transition
layers are biregular, but only a chosen owner/flag transversal with zero
induced Hall deficiency gives a one-copy cycle cover.  The sharp primitive
facet module pays `d` extra low roles locally; it does not establish a
globally disjoint packing into the prescribed Ferrers targets.

## 1. Literal age transition and open rail

For a state

```text
T=C_0 dotunion ... dotunion C_d
```

and a Johnson owner move

```text
T'=T-{alpha}+{beta},
```

the displayed update

```text
C'_(i+1)=S_i,
C'_0=(C_d-{alpha}) union {beta}
     union union_(i=0)^(d-1)(C_i-S_i)
```

is correct provided

```text
alpha in C_d,
|S_i|=c'_(i+1)<=c_i.
```

The classes are disjoint, their union is `T'`, and their total sizes force
`|C'_0|=c'_0`.  Conversely, every literal shift has precisely this survivor
form.

### Audit of Theorem 2.1

Let the legal type path have `ell<=d` transitions and all age coordinates
positive.  Placing the future deletion labels as

```text
alpha_t in C^(0)_(d-t),       0<=t<ell,
```

is valid because these are distinct positive-capacity classes.  At time
`u`, the label `alpha_t`, for `t>=u`, has age

```text
d-t+u.
```

Thus `alpha_u` is oldest and the other future deletions occupy distinct
younger classes.  Strict positivity of the target type reserves the one
required survivor place in each such class; the legal inequalities provide
the rest of every survivor quota.

Choosing distinct fresh labels `beta_t` is possible from `k-r>=ell`.  The
owners are

```text
T_t=(T_0-{alpha_0,...,alpha_(t-1)})
       union {beta_0,...,beta_(t-1)},
```

so they are pairwise distinct and successive owners differ by one deletion
and one insertion.

The adjacent colours are exactly

```text
K_t=(T_0-{alpha_0,...,alpha_t})
       union {beta_0,...,beta_(t-1)},

U_t=(T_0-{alpha_0,...,alpha_(t-1)})
       union {beta_0,...,beta_t}.
```

Their intersections with the initial label bank have respective sizes
`r-t-1` and `r-t`; hence each family is injective in `t`.

The run conclusion is correctly restricted to the owner-membership
sequence.  It is not a source-letter residence result.  Indeed, the
canonical initialization may spell the disjoint age classes in reverse
chronological order, giving some coordinates only one literal source-letter
occurrence while they persist in several owner windows.  Endpoint-clipped
owner runs are also outside the asserted floor.

## 2. Orbit stock

### Audit of Theorem 3.1

For one declared resource species, suppose

```text
gR=hR'.
```

Then `R` and `R'` lie in the same group orbit.  Orbit-simplicity first forces
the two seed occurrences to have the same value and then its trivial
stabilizer forces `g=h`.  Conversely:

* duplicate seed occurrences already collide in the identity translate;
* two distinct seed values in one orbit collide after suitable translates;
* a nontrivial stabilizer collides two translates of one seed value.

Thus the criterion is necessary and sufficient.  The corrected source now
includes the duplicate-occurrence case explicitly in the definition and
does not confuse resources of different species.

### Audit of Theorem 3.2

For `Gamma=<sigma>`, equivariance transports the one guarded connector
`P -> sigma P` to every connector `gP -> g sigma P`.  Since `sigma`
generates the group, these connectors form one cycle on all translates.
Orbit-simplicity of packet and connector resources, together with their
declared disjointness, gives exact resource injectivity.  This is a genuine
literal theorem only because legality and guards of the connector are
hypotheses; type-level common-entry fusion alone would not suffice.

### Audit of Proposition 3.3

The added internal-simplicity hypothesis is necessary.  Under it, after
`j` relabelled packets have been chosen, a fixed new rank-`s` resource
equals a fixed old one with probability

```text
1/binom(k,s).
```

There are at most `j M_s^2` comparisons in class `s`.  Hence the collision
probability is at most

```text
j sum_s M_s^2/binom(k,s).
```

For every `j<=H-1`, condition

```text
(H-1) sum_s M_s^2/binom(k,s)<1
```

leaves a legal relabelling.  Sequential choice proves the proposition.  It
is only sufficient, as the corrected note now states.

## 3. Protected-factor constants

For a monotone owner path of length `ell`, the exact number of choices is

```text
N_ell=binom(k,r)(r)_ell(k-r)_ell.
```

The path contains `ell+1` distinct owners, `ell` distinct lower colours,
and `ell` distinct upper colours.  Transitivity and double counting give

```text
Pr[fixed owner used]=(ell+1)/binom(k,r),
Pr[fixed lower used]=ell/binom(k,r-1),
Pr[fixed upper used]=ell/binom(k,r+1).
```

Therefore the fixed-bank loss is bounded by

```text
theta=f_0(d+1)/binom(k,r)
     +f_-d/binom(k,r-1)^(-1)
     +f_+d/binom(k,r+1)^(-1),
```

and one previously selected path excludes at most

```text
eta=(d+1)^2/binom(k,r)^(-1)
    +d^2 binom(k,r-1)^(-1)
    +d^2 binom(k,r+1)^(-1).
```

At most three paths are selected, so `theta+2eta<1` is the correct greedy
condition.  Their total transition length is at most `3d`; the incidence
lift has exactly twice that many edges.  Hence

```text
6d<=r-2
```

is exactly the small protected-factor edge budget in the odd host
`k=2r-1`.  Owner and lower-colour disjointness makes the protected
incidence union 2-bounded.  Upper-colour injectivity is additional local
information but is not supplied or extended outside the protected bank by
the two-factor theorem.

The corrected title “complete open-body bank” is essential.  Corollary 3.4
does not install the cut transitions, join the paths, impose exterior
residence, or preserve deep-shadow/common-cap guards.

### Audit of Corollary 3.5

Suppose at most `A(k)<=k` arbitrary-hole packets are prescribed.  Each
packet contributes at most three cut constituent paths, hence

```text
Q<=3k.
```

In the triangular regime, `d=Theta(sqrt(k))` and `r=ceil(k/2)`.  Therefore
`k-r>=d` for all sufficiently large `k`.  Each of

```text
binom(k,r), binom(k,r-1), binom(k,r+1)
```

is exponential in `k`, whereas `d`, `Q`, and every stipulated fixed-bank
order are polynomial.  Consequently

```text
theta=o(1),
Q eta=o(1),
theta+(Q-1)eta=o(1)<1.
```

The same sequential union bound used for Corollary 3.4 therefore selects
all `Q` paths with mutually distinct owner, lower-`q1`, and upper-`q1`
resources, avoiding the fixed polynomial banks.  Varying path lengths only
improves the displayed worst-case `d` bounds.

This is exactly an `O(kd)` collision-free **open-strand stock** theorem.
It does not put that bank in a common spanning factor, order its strands,
or create one literal source chronology.

## 4. Equivariant residual matching

Let the residual allowed-cell graph be bipartite and `Gamma`-invariant.
Averaging any perfect matching over `Gamma` gives an invariant fractional
perfect matching constant on each residual edge orbit `eta`.  Its edge
weight `w_eta` satisfies, at every left and right vertex orbit `O`,

```text
sum_eta d^L_(eta,O) w_eta=1,
sum_eta d^R_(eta,O) w_eta=1.
```

Conversely these equations assign a nonnegative fractional perfect
matching to the residual graph.  Bipartite matching-polytope integrality
then gives an integral perfect matching.  The equations automatically
force equality of the residual shore sizes.

The theorem is exact for saturation of both shores.  A one-shore compiler
problem would require the corresponding one-sided quotient system; that is
not claimed here.

## 5. Forced common basis

If `F` is independent in both rank-`R` matroids, each contraction has rank
`R-|F|`.  A common basis containing `F` is equivalent to a common
independent set of size `R-|F|` in the two contractions.  Edmonds' theorem
gives exactly

```text
min_(X subseteq E-F)
 [r_(M_1/F)(X)+r_(M_2/F)((E-F)-X)] >= R-|F|.
```

This is necessary and sufficient for the prepared two-matroid face.  It is
not sufficient for the grouped three-resource face, and the corrected note
does not claim otherwise.

## 6. Exact protected two-factor cut

For the prescribed protected incidence bank `P`, put

```text
b(v)=2-d_P(v),       G_0=G-P.
```

The hypothesis `Delta(P)<=2` makes every demand nonnegative.  Since `G` is
balanced and each edge of `P` contributes once to each shore,

```text
sum_(x in L)b(x)=sum_(y in U)b(y).
```

To complete `P`, it is enough to find a subgraph of `G_0` giving exact
degree `b(x)` on the left and capacity `b(y)` on the right.  Equal total
demands then force every right capacity to be saturated.  The capacitated
bipartite-flow cut for a fixed `S subseteq L` is obtained by minimizing over
which right vertices lie on the source side.  Each right vertex contributes

```text
min{b(y),d_(G_0)(y,S)}.
```

Thus max-flow/min-cut gives precisely

```text
sum_(x in S)b(x)
 <=sum_(y in U)min{b(y),d_(G_0)(y,S)}
```

for every `S subseteq L`.  Integrality of the bipartite network gives an
integral completion.  Hence Theorem 4.3 is necessary and sufficient, not
merely a relaxation.

For the full dispersed bank of Corollary 3.5, this cut remains a separate
gate: resource injectivity alone does not imply it.  For Corollary 3.4, the
small protected-factor theorem proves it from the stronger edge bound.

## 7. Corrections incorporated before this frozen audit

The audited source incorporates all issues found during the adversarial
pass:

1. Proposition 3.3 now assumes internal resource simplicity.
2. The orbit-simple converse covers duplicate seed occurrences.
3. The spread bound is described as sufficient rather than exact.
4. Corollary 3.4 is explicitly an open-body, not completed-actuator,
   theorem.
5. Its `6d` quantity is explicitly the incidence-edge count.
6. Theorem 5.1 requires the seed, including internal joins, already to be
   one literal open packet whose translates add no source cells outside the
   main owner bank.
7. Every internal collar cell must be charged as a bank owner/resource,
   not hidden as per-translate excess.
8. If common-cap and common-basis completions are simultaneously required,
   they must be disjoint, be two descriptions of the same choice, or carry
   an explicit joint-compatibility certificate.  Separate marginal
   feasibility is expressly rejected.
9. The polynomial-size dispersed bank is claimed only as a collision-free
   open-strand stock; its spanning-factor extension is isolated as the exact
   Ore--Ryser condition (4.5).
10. Theorem 5.1 now assumes that the full translated incidence bank passes
    (4.5), unless a spanning protected factor is already part of the seed;
    it also requires this residual factor choice to be resource-disjoint
    from the compiler choice or covered by one joint certificate.

With these corrections, the implication in Theorem 5.1 is valid: resource
injectivity comes from Theorem 3.1, cyclic topology from Theorem 3.2,
residual matching from Theorem 4.1, and the optional prepared common basis
from Theorem 4.2.  Its item 6 supplies the spanning owner/lower two-factor
through Theorem 4.3.

## 8. Exact remaining scope

Still unproved are:

1. an orbit-simple seed in the canonical Catalan/PBBS host carrying all
   owner, adjacent-colour, upper/deep-witness, returned-witness, and
   addressed compiler resources;
2. a literal unit-voltage connector that carries the lower-palette change
   and every guard;
3. simultaneous common-cap/common-basis compatibility outside the prepared
   disjoint or explicitly coupled cases;
4. verification of the Ore--Ryser cuts for the full dispersed bank;
5. source-letter residence and endpoint joining for the complete physical
   actuator;
6. a grouped three-resource completion theorem; and
7. any implication to `B(k)+O(1)` or exact `nu(k)=B(k)` without the missing
   seed theorem.

Accordingly, the source note is a valid unconditional local rail theorem,
an exact orbit/matching/basis reduction, and a valid conditional stock
theorem.  It is not a global protected-host existence theorem.
