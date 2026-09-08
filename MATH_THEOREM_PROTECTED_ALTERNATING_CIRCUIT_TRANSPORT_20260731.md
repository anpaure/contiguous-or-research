# Protected alternating-circuit transport

## Setup

Let `L` be a family of lower colours and `V` a family of owners, with an
incidence relation `C ~ v`.  A feasible selection `M` prescribes exact
degrees on both sides.  In the Boolean-layer application, `C` is a set of
rank `r-1`, `v` is a rank-`r` superset, and the two owners selected at `C`
form the physical Johnson edge of lower colour `C`.

Write

`sigma_M(C) = v_0(C) union v_1(C)`

for the corresponding immediate-upper target (with the fixed sector bits
restored).  Let `m_M(T)` be the number of physical edges whose upper target
is `T`.

Some rows in the integrated K17 construction have one residual owner and one
fixed cross-sector owner.  The statements below include those rows: regard
the fixed owner as part of the row data and rotate only the selected residual
incidence.

## Lemma 1: alternating-circuit invariance

Suppose

`C_0-v_0-C_1-v_1-...-C_{ell-1}-v_{ell-1}-C_0`

is an alternating circuit: every `C_i-v_i` is selected and every
`C_{i+1}-v_i` is admissible.  Replace the selected incidences by

`C_{i+1}-v_i` (indices modulo `ell`).

Then every lower-row degree and every owner degree is unchanged.  Therefore
the physical graph retains every middle vertex degree and still has exactly
one physical edge of every lower colour.

### Proof

Each row loses and gains one incidence.  Each owner loses and gains one
incidence.  The physical edge indexed by a row may change, but its lower
colour remains that row.  All other rows are untouched.  QED.

For consecutive Boolean layers there are no 4-cycles, so `ell=3` (a
six-edge bipartite circuit) is the primitive move.

## Lemma 2: exact protection criterion

For an alternating circuit, let `R(T)` and `A(T)` be the numbers of removed
and added physical edges with upper target `T`.  The move preserves immediate
upper surjectivity if and only if

`m_M(T) - R(T) + A(T) >= 1`

for every upper target `T` touched by the circuit.

Equivalently, whenever a target loses its last current provider, the same
compound move must install another provider.

### Proof

Targets outside the circuit keep their multiplicity.  On a touched target
the displayed expression is its new multiplicity.  Surjectivity is exactly
positivity of every multiplicity.  QED.

Call a circuit satisfying this condition **protected**.  A composition of
alternating circuits is protected precisely when the same inequality holds
for its *net* removed/added multisets; the individual circuits need not be
protected.  This is the useful compound-move form.

## Lemma 3: residence locality

Let `G_M` be the physical 2-factor.  For coordinate `x`, the positive runs
are the connected components of the induced graph

`G_M[{v : x in v}]`.

For residence depth `d`, define

`Phi_d(M) = sum_x sum_P (d+1-|P|)^+`,

where `P` ranges over positive-run components.  An alternating circuit can
change only those run components meeting an endpoint of a removed or added
physical edge.  Consequently `Delta Phi_d` is computed exactly by tracing
the induced components from those finitely many endpoints, before and after
the move.

### Proof

Outside the changed physical edges, adjacency is identical.  A connected
component disjoint from all changed endpoints therefore has exactly the same
vertices and edges before and after.  Only components meeting an endpoint
can split, merge, appear, or disappear.  QED.

This gives an `O(ell)`-endpoint exact score; its practical cost is the total
length of the touched coordinate runs, not the size of the middle layer.

## Corollary: protected-fibre descent

A protected alternating circuit with `Delta Phi_d <= 0` preserves both q1
shadow gates and does not worsen residence.  A finite composition with net
`Delta Phi_d < 0` strictly improves residence while preserving both gates.

The K17 trajectory is a certificate that this fibre has substantial
mobility:

- a neutral/improving primitive-circuit walk drove rank-10 holes
  `4413 -> 0` while lower q1 remained exact;
- starting at the zero-hole factor, protected primitive and length-3-to-8
  alternating circuits reduced `Phi_3` while rank-10 coverage remained
  complete.

At the first zero-hole K17 factor, 1,742 of 19,554 deduplicated primitive
circuits are q1-protected.  The exact q1 load histogram is
`1^15166 2^3733 3^519 4^29 5^1`, so most upper targets are protected by a
unique current provider, but the forced excess still supplies a large
neutral transport fibre.

## The open all-k statement

The following would turn the mechanism into a construction theorem.

> **Protected-fibre transport conjecture.** In the relevant Pascal-sector
> b-matching fibre, every q1-surjective state with `Phi_d>0` is connected by
> protected alternating circuits to a state of smaller `Phi_d`; iterating
> reaches `Phi_d=0`.  A strengthened form simultaneously merges components
> and covers deeper upper shadows.

The immediate-improvement version is false as a proof strategy: the K17
search encountered states with no improving primitive circuit, and escaped
through long neutral walks.  Thus a correct theorem must allow a plateau
path or one compound circuit, not demand a single locally improving hexagon.

## Explicit obstruction certificate

For a fixed state, form the directed state graph of protected circuits.  A
closed class on which `Phi_d` is constant and positive is an exact
obstruction to protected descent in that move catalogue.  Equivalently, a
set of singleton-loaded upper targets whose unique-provider rows separates
every residence-improving alternating circuit is a protection cut.

This identifies the finite dual object to search for if descent stalls:

1. either exhibit a protected compound circuit crossing the cut; or
2. certify that every alternating circuit crossing it removes a last
   provider without compensating addition.

No such obstruction is claimed for all K17 circuits.  The present theorem
is the invariant/locality reduction; connectivity of the protected fibre is
the remaining global statement.

## K17 audit anchors

- double-rainbow flow SHA-256:
  `30501377d3186135d85e984330d50fbf0356de37f6351c15ae2e40766056af78`
- extension-map audit payload:
  `9b274c704707ab60d9b3c816f0d193076b63f3cc5d19695521b74268c9d6328c`
- primitive-circuit census payload:
  `10138753eca6c4ca9024ae621470a19ea55abb22b2fec2a6c5d7ab7cb479440b`
