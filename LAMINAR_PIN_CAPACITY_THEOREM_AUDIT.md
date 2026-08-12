# Self-audit of the laminar pin-capacity theorem

## Verdict

The component Hall inequality, its fixed-pin and averaged moment
corollaries, and the cross-rank deficit merge law are valid.  They are
unrestricted necessary conditions for every universal zero-free word.

The result is stronger than imposing physical component capacity and
coordinate support separately because both bounds constrain one actual
assignment of lower targets to components.  It does not establish that any
profile satisfying the displayed inequalities is realizable.

The quantities `q_C,K_C` depend on a choice of one witness for every
nonliteral rank-`r` target.  The proof works for every fixed choice.  Choices
at different ranks are independent; it is the component deficits and merge
identities, not the chosen `q` profiles, that are canonically coupled across
ranks.

## 1. Localization of witnesses

If `|S|<r`, every entry in a witness for `S` is a nonempty submask of `S`, so
the entire witness lies in one component of `{i:|A_i|<r}`.

If `|R|=r` and `R` does not occur literally, a witness for `R` cannot contain
an entry of rank greater than `r`.  It also cannot contain an entry of rank
exactly `r`, because such an entry is a rank-`r` submask of `R` and hence is
equal to `R`, contradicting nonliterality.  Thus every nonliteral rank-`r`
target also has a witness in one low component.  Literal rank-`r` values are
deliberately omitted from the `q_C` total, so equation (2.1) is exact even
when literal values have repeated occurrences.

## 2. Positivity of component slack and physical capacity

Within an `n_C`-position component, `q_C` selected rank-`r` witnesses are
pairwise incomparable.  Their left endpoints are distinct, their right
endpoints are distinct, and the two endpoint orders agree.  Hence `q_C<=n_C`.

If equality held, both endpoint sets would be all `n_C` positions.  In the
common increasing order the `j`th left and right endpoints would both be
`j`, so every witness would be a singleton.  This is impossible because all
entries of the component have rank below `r`.  Therefore `t_C=n_C-q_C>=1`.

The standard ordered-antichain argument then puts the `j`th selected witness
inside `[j,j+t_C]`.  Every component interval of length at least `t_C+1`
contains one selected rank-`r` witness and cannot have lower rank.  The
number of component intervals of length at most `t_C` is exactly

```text
t_C q_C + C(t_C+1,2),
```

including the case `q_C=0`.  Thus `K_C` bounds all distinct lower labels
realized in the component, not merely a chosen set of lower witnesses.

## 3. Audit of the family inequality

Choose one witness for every member of an arbitrary family `F` of lower
targets and assign it to its unique low component.  If `m_C` members are
assigned to `C`, then

```text
m_C <= K_C
```

by the physical argument.  Also, each assigned target is contained in the
total coordinate union `V_C`, giving

```text
m_C <= |{S in F:S subseteq V_C}|.
```

The latter condition is exactly `S intersect D_C=empty`.  Therefore
`m_C` is at most the minimum of the two displayed resources.  Since every
target is assigned exactly once, summing proves (3.1).  No assumption of
unique witnesses is used.

The fixed-`Q` specialization counts precisely

```text
H_(r,a)(v)=sum_(s=a)^(r-1) C(v-a,s-a)
```

eligible targets when `Q subseteq V_C`, and none otherwise.  Averaging over
all `a`-sets `Q` counts each component exactly `C(|V_C|,a)` times.  Equations
(4.1)--(4.3) follow without an independence assumption.

The strictness example only compares relaxations.  It is correctly not
claimed to be a feasible universal word.

The transversal corollary is also valid.  If a nonempty set `Q` of fewer
than `r` coordinates meets every component deficit, then `Q` is contained
in no component union.  But `Q` is itself a lower target and its witness must
lie in one low component.  The convention that an empty deficit has infinite
transversal number is essential and is stated explicitly.

## 4. Audit of the laminar merge identity

The level sets `X_r={i:|A_i|<r}` are nested.  A parent component of
`X_(r+1)` consists exactly of its `X_r` child components plus the positions
of rank exactly `r` between or around them.  Taking coordinate unions and
then complements gives (5.1), including a parent with no child under the
empty-intersection convention.

A coordinate absent from every child but present in the parent must occur in
one of the exact-rank positions.  Hence `G_r(P)` is contained in their union
and has size at most `r|E_r(P)|`.  Each rank-`r` position belongs to one and
only one parent component of `X_(r+1)`, so summing gives (5.3).

This is an occurrence-pin statement: if `O_b={i:b in A_i}`, then
`b in D_C` is exactly `O_b intersect C=empty`.  It should not be read as a
claim that every position legal for `b` under an arbitrary selected witness
schedule is actually occupied by `b`.

## 5. Interaction with rank-filtration stability

The Hall theorem itself does not need near-extremality.  For a word of length
`beta_r(k)+c`, the independently audited rank-filtration theorem supplies

```text
|C_r|=kappa_r(A)<=c+1.
```

Thus a near-extremizer must satisfy the entire family of pin-load inequalities
using at most `c+1` components.  Across ranks, the component nodes are nested
and their deficits obey (5.1), so these are not independent per-rank support
profiles.

This still leaves substantial freedom: a coordinate-complete component may
be short, capacities can be uneven, and eligible masks need not be realized.
The theorem therefore changes neither the current `k=11` bracket nor the
all-dimensional conjecture by itself.

The separator corollary correctly uses the canonical component only after
taking its convex hull back in the original word.  Deleted exceptional
positions may lie in that hull, but adding them cannot destroy the full
coordinate union.  A proper target cannot have a witness reaching both
sides of a full-OR hull.  Charging left-reaching witnesses by their left
outside endpoint and right-reaching witnesses by their right outside endpoint
is injective within each fixed rank because the ORs at one endpoint form an
inclusion chain.  Hence the per-rank loss `n-|H|` and total loss
`(k-1)(n-|H|)` are valid.  The full set is not an extra loss: the hull itself
represents it.

For `t_C=1`, the ordered-antichain containment puts every selected rank-`r`
witness in a singleton or adjacent pair.  Singleton rank `r` is excluded in
a low component, and the number of witnesses equals the number of adjacent
pairs.  Hence all adjacent pairs are used and every longer interval has rank
at least `r`; the lower labels represented there are exactly singleton-cell
values.  The slack-one rigidity statement is sound.

## 6. Remaining sharp target

The natural next step is to optimize (3.1) jointly with the merge erosion
budget and the exact rank profile.  A useful obstruction would show that a
near-width rank profile cannot create enough high-capacity, coordinate-rich
nodes within the allowed component counts.  A constructive counterpart would
give an explicit laminar component forest whose pin-load system has a
capacity-respecting target assignment and then refine that coarse assignment
to actual interval witnesses.
