# Growing-prefix catalogues: full overlaps and central matching

Date: 2026-09-07. Pure proof; no computation. This extends the accepted
four-prefix counting argument to a slowly growing number of groups.
Its intended application is a higher-valence grid, but no such geometry
or noncentral coverage is assumed to exist in this theorem.

## 1. Finite hypotheses and full-subset bound

Partition a 2b-set into g ordered coordinate groups. Let P be a nonempty
family of distinct b-sets, each a union of group prefixes. Suppose:

- the common intersection of P has size at least b-a;
- the complement of the union of P has size at least b-a;
- P is covered by t Johnson geodesics contained in P;
- 2a<b.

Develop P under all coordinate permutations and retain distinct simple
supports, using complement-paired middle vertices. No two members of P
are complements, and all coherent orientations have diameter below b/2.
Write D for the folded orbit degree. At a reference E and anchor v set

    K_v(z)=sum_{S subset E, v in S, |S|>=2}
                  z^(|S|-1) deg(S)/D,       w=1+z.

For an anchored S let d=|v minus intersection S|,
e=|union S minus v|, u=d+e. Then 2<=u<=2a and d,e<=a.
Put Q=b-a. The exact signature-allocation proof gives

    deg(S)/D <= g^u product(variable-atom factorials)
                          /[(b)_d(b)_e]
              <= (g u/Q)^u.                                  (1)

Indeed each of the u variable target coordinates is assigned to one
of g source groups. Within each group its nested membership signatures
and the anchor cut fix the compatible source tuple, if there is one.
There are at most g^u assignments. Conditional permutation probabilities
retain the exact Venn factorials; their product is at most u!<=u^u.
The anchor roles are averaged, not summed with an extra |P| factor.
Folding adds no factor: all signs in a compatible tuple are global,
since mixed signs would turn a distance below b/2 into one above b/2.

The variable coordinate set is determined by two extents at the anchor
cut in each group. There are at most binom(u+2g-1,u) extent profiles.
Along a geodesic the vertices agreeing with v outside this set form
an index interval of at most floor(u/2)+1 vertices. Thus at most
t(u/2+1) eligible template vertices occur in a profile.

Subtracting the anchor-only subset before bounding gives

    K_v(z) <= t z w^t sum_{u=2}^{2a}
             (u+1)binom(u+2g-1,u) (u A_span)^u,
    A_span=(g/Q)w^t.                                        (2)

This finite bound includes all disconnected subsets and repeated
membership signatures. It is zero when z=0. No decomposition into
independent overlap components is used.

## 2. A growing-dimension tail estimate

Suppose b tends to infinity through a sequence for which

    a=b^(1/2+o(1)),    g=b^o(1),    t=b^o(1),
    t log w=o(log b).                                       (3)

Then A_span=b^(-1+o(1)) and beta=2a A_span=b^(-1/2+o(1)). In particular
g beta=o(1). For every fixed integer m>=1, writing d0=2g,

    sum_{u>=m}(u+1)binom(u+d0-1,u) beta^u
       <= binom(m+d0-1,m) beta^m (1-beta)^(-d0-m)
             [m+1+(d0+m)beta/(1-beta)].                     (4)

To prove (4), put u=m+j and use

    binom(m+j+d0-1,m+j)
      <=binom(m+d0-1,m) (d0+m)_j/j!;

the rising-factorial series and its derivative sum the remaining
terms. Since m is fixed and g beta=o(1), the right side of (4) is
b^(-m/2+o(1)).

In (2), retain u=2,3,4 separately and apply (4) with m=5 to its
remaining tail, using u A_span<=beta. This proves uniformly over anchors

    K_v(z) <= z b^(-2+o(1)).                              (5)

Retaining u=3,...,6 separately and using m=7 instead proves that the
contribution of u>=3 is at most z b^(-3+o(1)). The u=2 term consists
exactly of the anchor and one Johnson neighbor. If d_P(v) is the
induced Johnson degree of the anchor's template role in the represented
reference edge, and bar_d is its catalogue average,
symmetry of the b^2 ambient neighbors therefore gives the sharper

    K_v(z)=z d_P(v) bar_d/b^2 + O(z b^(-3+o(1))).         (6)

The remainder is nonnegative. Here d_P(v)<=g(g-1), so the displayed
leading term is consistent with (5) even when g grows. The role-average
coefficient in the independent-retention variance is bar_d^2.

## 3. Pair caps and template size

For a prescribed folded pair, choose its coherent oriented representatives
and let j be their Johnson distance (the smaller of its two antipodal
distances). The sharper two-target version of the signature count gives

    deg(v,u)/D <= g^(2j)/binom(b,j)^2,       1<=j<=a.      (7)

No pair at greater oriented distance can occur in a coherently rooted
copy. Under (3), g(a+1)/(b-a)=b^(-1/2+o(1)), so successive terms on
the right of (7) decrease for all 1<=j<a, eventually. Thus one may use

    delta=g^2/b^2=b^(-2+o(1)).                            (8)

Each covering geodesic has at most a+1 vertices: all its members
contain the common (b-a)-subset. Hence the folded uniformity r=|P|
satisfies r<=t(a+1)=b^(1/2+o(1)). We assume r>=2 below; r=1 is the
trivial singleton-edge case.

## 4. Consequence of the accepted equalized matching theorem

Strengthen (3) to t log log b=o(log b), and put p=1/log b. Then
(5) applies at every z=p^(-c)-1 for fixed c>0, giving

    Xi(p^c)<=b^(-2+o(1)).

Apply the fully audited adaptive equalized-nibble theorem with

    L=b^(1/8), alpha=b^(-1/16), q'=64, m=33,
    total deletion time Lambda=log log b,
    r lambda_max=o(1).

Using (8) and r<=b^(1/2+o(1)), its interaction parameter
A_ad=Lambda L delta satisfies
A_ad r^2<=b^(-7/8+o(1)); its vertex-ban charge is at most
b^(-1/4+o(1)); its aggregate pair-ban charge is at most b^(-2+o(1)).
Thus the folded coordinate-orbit hypergraph admits a matching covering
1-o(1) of its vertices. This is CENTRAL matching only.

The same application permits predictable proposal weights bounded by
C_w=b^o(1), not only a fixed C_w: replace A_ad by C_w Lambda L delta.
Here C_w is a deterministic uniform bound fixed throughout each run.
All polynomial exponents remain unchanged. The exact weighted-degree and
total-mass constraints of the accepted weighted variant are still
required; no useful hole-favoring weights are supplied here.

This conclusion does not construct the g-prefix template, bound its
serializer cost, supply enough possible noncentral witnesses, or make
those witnesses globally fresh. Those are independent geometric and
coverage requirements.

Proof dependencies: the signature allocation and extent/geodesic count
are the same finite arguments fully spelled out above and in
scratch/SHARP_FULL_GRID_KERNEL_AND_SMALL_STEP_BOUND_20260907.md.
The matching step invokes Sections1--8 of chat03's
research_round1/ROUND4_ADAPTIVE_EQUALIZED_NIBBLE.md, including every
candidate-ban and waste hypothesis. Its bounded-weight extension is
Section10. These sources have passed independent audits.

Status: independent root-agent audit passed the full finite signature
bound, growing-g generating-function tail, coherent folded-pair
normalization, size bound, and adaptive matching parameter transfer.
The geometric and noncentral coverage requirements remain separate.
