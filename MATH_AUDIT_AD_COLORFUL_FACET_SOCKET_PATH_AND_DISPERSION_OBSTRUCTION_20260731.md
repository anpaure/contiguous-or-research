# Independent audit of the colorful facet-socket path theorem

Date: 2026-07-31  
Audited file:
`MATH_THEOREM_AD_COLORFUL_FACET_SOCKET_PATH_AND_DISPERSION_OBSTRUCTION_20260731.md`  
Audited SHA-256:
`094356c38ff6dc603074909a4a67f64165f9d9019a83e515fcef183456d0f3d5`  
Status: **PASS after three integrated scope corrections**.

## 1. Corrections integrated before freezing

1. The `4I_cd` identity counts wedge-source to wedge-destination signed
   openings.  An arbitrary safe root need not be a wedge centre.  The final
   theorem now gives the separate exact formula (6.4), summing all safe
   source endpoints with their opening multiplicities.
2. The Hall--two-switch hypothesis is now quantified over every
   non-Hamilton cycle cover reached during the process.  A switch promised
   only for the initial cover would not justify iteration.
3. A wedge-free `k=15` small component alone excludes only the all-wedge
   path and the large-root order.  The final theorem now imports the exact
   opposite-order audit: `120` small-root facet sockets, all provider-unsafe,
   with literal defect split `90` depth-three only and `30` depth-one plus
   depth-three.

## 2. Independently checked statements

The following claims were rederived independently and passed.

* For a fixed assigned tower and component order, the endpoint recursion
  `X_t=T_(sigma(t))(X_(t-1))` is sound and complete.  Endpoint labels are a
  sufficient state because the preceding transition has already certified
  the incoming opening, and only the endpoint enters the next socket
  equation.
* The binary degree system selects one safe-rooted path plus directed
  cycles.  The component rows

  \[
                 y(E[I])\le |I|-1
  \]

  eliminate exactly those cycles.  Summing indegrees gives the equivalent
  rooted cut `y(delta^-(I))+a(I)>=1`; at most `b` forced-sink directed
  min-cuts separate the fractional family.
* The robust mutual quotient with minimum degree
  `ceil((b-1)/2)` has a Hamilton core by the included Dirac proof and lifts
  greedily.  Hall plus the universally quantified crossed-successor
  two-switch also merges a cycle cover to one Hamilton cycle.
* The input/output palette rectangle is sufficient; separate large input
  and output marginals without the rectangle are not.
* The three-colour chamber construction has complete component projection,
  option colour-semidegree `b-2`, paths on every proper colour subfamily,
  and no full path.  Its local `J(9,5)` realization is valid: the three
  six-sets have pairwise intersection four, so no five-facet sockets across
  chambers, while the two facet triples inside each chamber socket
  reciprocally.
* Every cross-component wedge-centre incidence gives exactly four signed
  arcs, and a destination wedge has at most `r-2` external predecessor
  facets because its centre and two neighbours are three distinct facets on
  its own component.
* Under q1 completeness and no monochromatic component,

  \[
     D\le {k\choose r}-{k\choose r+1}={2W\over m+2}
  \]

  at `k=2m+1,r=m+1`.  The stabilizer action is free because
  `gcd(2m+1,m+1)=1`.  Hence a unit-voltage component consumes at least `k`
  wedges and

  \[
             b_{\rm wedge}\le {2\operatorname{Cat}_m\over m+2}.
  \]

* For individually unit-voltage invariant core components, the quotient
  incidence bound gives

  \[
   n\left\lceil{n\over2}\right\rceil
       \le {2(m-1)\over m+2}\operatorname{Cat}_m,
  \]

  and therefore `n<2 sqrt(Cat_m)`.  This is only a dense-Dirac obstruction,
  not a sparse-Hamilton obstruction.
* The `k=13` maximum-flexibility counts `130+52=182` and the separate
  distinguished all-wedge count `52` are not conflated in the final text.
  The latter is a subset of the `130` big-root order, not the second summand.

## 3. Scope boundary

The report proves an upper fixed-width chronology theorem relative to a
selected witness assignment.  It does not prove that the PBBS factor has
enough wedge-bearing components, that its sparse transducer expands, or that
arbitrary voltages may be normalized away.  It also deliberately leaves
residence, lower-`q1` restitution, and the common lower compiler/Hall system
as independent gates.

The separately audited incidence-budget note is

```text
THREAD_AD_PBBS_MULTISPIRAL_FACET_SOCKET_DISPERSION_BUDGET_20260731.md
SHA-256 93cda9411a7c5b8d933b3ba3b112cf11b344314e23141147badc945752f8247c
```

