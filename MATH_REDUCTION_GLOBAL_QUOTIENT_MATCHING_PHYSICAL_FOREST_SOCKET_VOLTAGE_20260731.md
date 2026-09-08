# Global quotient matching with physical forest, sockets, and voltage

Date: 2026-07-31  
Status: exact matching/forest/closure/voltage reduction; conditional
socket and Benders modules; no existence theorem for the coupled lift

## 1. Rebased quantifier

Let \(|\Omega|=2m\), let \(H\cong\mathbb Z_h\) be a clean subgroup acting
freely on the two outer shores

\[
 \mathcal L=\binom{\Omega}{m-1},
 \qquad
 \mathcal U=\binom{\Omega}{m+1},
\]

and on the middle layer \(\mathcal V=\binom{\Omega}{m}\).  The complete
lower--upper diamond graph is balanced and regular.  Its quotient by \(H\)
is a balanced regular bipartite multigraph, with parallel occurrence edges
retained.  It therefore has a quotient perfect matching.

The existential construction must choose this global matching first.  Any
exceptional filters are then its restriction.  It must not prescribe filters
first and ask for a residual Kneser extension.

When

\[
 q=2m-1=6a+3,\qquad v_3(q)=1,
\]

the restriction contains exactly \(2\operatorname{Cat}_a\) clean-subgroup
filter orbits, one for every exceptional quotient vertex on each typed shore.
It covers every exceptional typed colour once, is globally extendable by the
same matching, occupies exactly one third of each relevant free full-rotation
edge orbit, and has pairwise-distinct physical middle endpoints.

The opposite endpoints are distinct separately on the two typed physical
shores.  After complement-identifying both shores as one Kneser label set, a
lower-family opposite label may equal an upper-family opposite label.  No
cross-family distinctness in that auxiliary label space is used or claimed.

The quantifier is

\[
 \exists\,\bar M\in\operatorname{PM}(\mathcal B_m/H),
 \qquad
 F=\bar M|_{\text{exceptional banks}}.
\]

It is not

\[
 \forall F_{\rm local}\ \exists\,\bar M\supseteq F_{\rm local}.
\]

Thus residual-Kneser Hall is removed from the existential route.

## 2. Occurrence-labelled quotient atoms

Let \(\bar{\mathcal L},\bar{\mathcal U},\bar{\mathcal V}\) denote the clean
outer and middle orbit sets.  Every quotient diamond atom \(a\) records

\[
 \ell(a)\in\bar{\mathcal L},\qquad
 u(a)\in\bar{\mathcal U},
\]

its two middle endpoint orbits

\[
 p(a),q(a)\in\bar{\mathcal V},
\]

its voltage gain \(g(a)\in\mathbb Z_h\), and the complete list of literal
physical diamond occurrences in its lift.  Parallel quotient atoms are not
identified: different phases can have the same outer orbit endpoints while
giving different middle edges, gains, collars, or sockets.

The catalogue is canonical at the carrier level: every atom is exactly one
distinct \(H\)-orbit of physical diamond edges, and the middle-layer action
is a free regular \(H\)-cover.  Alternative collars or socket states on the
same carrier orbit are refinements of that atom, not additional \(x\)-atoms.
This convention is required for the edge count and for the forest lift below.

Fix once and for all one physical representative \(\widetilde v\) of every
middle orbit \(v\in\bar{\mathcal V}\).  For an oriented atom from \(p(a)\)
to \(q(a)\), define \(g(a)\) by requiring its representative occurrence to
join \(\widetilde {p(a)}\) to \(g(a)\widetilde {q(a)}\).  Reversal has gain
\(-g(a)\).  Closure-arc gains below use this same representative system.
Without this common gauge, gains from different catalogues cannot be summed.

Let \(x_a\in\{0,1\}\).  The global quotient perfect matching is exactly

\[
 \sum_{\ell(a)=L}x_a=1
       \quad(L\in\bar{\mathcal L}),
 \qquad
 \sum_{u(a)=U}x_a=1
       \quad(U\in\bar{\mathcal U}).                       \tag{QM}
\]

There are no exceptional-filter variables and no residual-palette Hall rows.
The selected atoms incident with exceptional outer rows are the filters.

## 3. Exact spanning-linear-forest lift

For \(v\in\bar{\mathcal V}\), let
\(\iota_v(a)\in\{0,1,2\}\) be the incidence multiplicity of the quotient
middle edge \(p(a)q(a)\) at \(v\). The selected diamond lift is a spanning
linear forest, with isolated vertices allowed as trivial paths, exactly when

\[
 \sum_a\iota_v(a)x_a\le2
       \quad(v\in\bar{\mathcal V}),                       \tag{D}
\]

and

\[
 \sum_{a:\ p(a),q(a)\in W}x_a\le |W|-1
       \quad(\varnothing\ne W\subseteq\bar{\mathcal V}).  \tag{G}
\]

The singleton instances of (G) exclude quotient loops.  Its two-vertex
instances exclude selected parallel-edge two-cycles.  At an integral
incumbent, (G) is separated by finding a selected quotient cycle.

For the nontrivial path forest required by the block-wedge construction,
replace (D) by

\[
1\le \sum_a\iota_v(a)x_a\le2
       \quad(v\in\bar{\mathcal V}).                       \tag{D+}
\]

These conditions are necessary and sufficient.  A quotient circuit of total
voltage \(v\in\mathbb Z_h\) lifts to \(\gcd(h,v)\) physical circuits, so every
quotient cycle violates physical acyclicity.  A quotient forest gauges to
zero and lifts to \(h\) disjoint physical copies.  Put

\[
 M=\binom{2m}{m},\qquad
 N=\binom{2m}{m-1},\qquad
 K=M-N=\operatorname{Cat}_m.
\]

Equations (QM), (D), and (G) select \(N/h\) quotient edges on \(M/h\)
middle orbits, hence exactly \(K/h\) quotient path components and \(K\)
physical path components. Under (D), isolated middle vertices are allowed as
trivial paths; under (D+) every component is nontrivial.

The matching subsystem (QM) is totally unimodular.  Adding (D) and (G) is a
genuine matching-plus-graphic problem; no residual-Hall or TU shortcut is
asserted.

## 4. Exact closure without component identifiers

Introduce the two directed orientations \(d_{a,+},d_{a,-}\) of each selected
forest atom, with

\[
 d_{a,+}+d_{a,-}=x_a.                                    \tag{C0}
\]

Let \(\mathcal S\) be the occurrence-labelled catalogue of legal closure
arcs. Every selected record is one **complete \(H\)-orbit** of Johnson
edges. A record \(c\in\mathcal S\) contains that literal edge orbit,
its tail and head middle orbits, gain \(g(c)\), physical phase occurrences,
collar state, and every literal resource it consumes.  Let
\(y_c\in\{0,1\}\).  Distinct records that use the same literal edge orbit
remain distinct catalogue records, but explicit link/exclusion rows impose

\[
 \sum_{c:\,o(c)=o}y_c+\sum_{a:\,o(a)=o}x_a\le1
       \qquad(o\text{ a literal Johnson edge orbit}).    \tag{CE}
\]

Thus a closure edge cannot reuse a selected forest edge or a second closure
record. Phase data inside a record may refine collars and resources, but not
the selected edge set. A genuinely partial-phase closure requires a separate
physical expansion of the degree, subtour and voltage rows and is outside
this quotient system.

On the union of the directed forest arcs and the closure arcs impose

\[
 \deg^+(v)=\deg^-(v)=1
       \quad(v\in\bar{\mathcal V}),                       \tag{C1}
\]

and every proper directed subtour cut

\[
 \sum_{\substack{a:\,p(a)\in W,\ q(a)\notin W}}d_{a,+}
 +\sum_{\substack{a:\,q(a)\in W,\ p(a)\notin W}}d_{a,-}
 +\sum_{\substack{c:\,\operatorname{tail}(c)\in W\\
                      \operatorname{head}(c)\notin W}}y_c\ge1
       \quad(\varnothing\ne W\subsetneq\bar{\mathcal V}). \tag{C2}
\]

Equivalently, use one circuit constraint on the quotient middle vertices,
with every vertex mandatory and every solver-style exclusion self-loop
absent or forced false.
Because \(x\) is already a forest, (C0), (CE), and (C1)--(C2) orient every
forest path coherently, use closure arcs only at its endpoints (two closure
darts at an isolated path vertex), select exactly \(K/h\) closure arcs, and
join all quotient paths into one quotient cycle.  No dynamic component labels
are needed.  This statement assumes that \(\mathcal S\) is the exhaustive
literal edge-orbit catalogue; a coarse endpoint-pair catalogue is not enough.

The rows above certify topology, not the stronger block-wedge interface. For
that interface replace \(\mathcal S\) by an exhaustive catalogue
\(\mathcal S_{\rm bw}\). Each record \(c\) additionally names the selected
oriented first forest atom \((a(c),\theta(c))\) at its head, and is admitted
only when, phase by phase,

\[
u(c)=u(a(c),\theta(c)).                                  \tag{BW0}
\]

It records the corresponding lower orbits

\[
\alpha(c),\qquad \beta(c),\qquad d(c),
\]

and is linked by

\[
y_c\le d_{a(c),\theta(c)}.                              \tag{BW1}
\]

For the full lower floor and zero-slack smoothed-base ledger impose

\[
\sum_{c:\alpha(c)=A}y_c\le1,qquad
\sum_{c:d(c)=D}y_c\le1,                                \tag{BW2}
\]

for every relevant lower orbit, together with the untyped separation

\[
\sum_{c:d(c)=D}y_c+\sum_{c:\beta(c)=D}y_c\le1
       \qquad(D\in\bar{\mathcal L}).                    \tag{BW3}
\]

The \(\beta\)-bank is already injective because it is a subset of the exact
lower-colour matching selected by (QM). Equations (BW0)--(BW3), with the
literal phase data in each record, are exactly the additional wedge and
\(\alpha,d,\beta\) conditions of the block-wedge theorem. They are not
implied by (C0)--(C2).

## 5. Unit-voltage lift and the linear boundary

For \(h>1\), choose fixed representatives
\(\widetilde g(a),\widetilde g(c),\widetilde r\in\{0,\ldots,h-1\}\)
of all gains and residues.  The reverse dart of \(a\) contributes
\(-\widetilde g(a)\).  Choose \(b_r\in\{0,1\}\) for the unit residues
\(r\in\mathbb Z_h^\times\), with

\[
 \sum_{r\in\mathbb Z_h^\times}b_r=1.
\]

For an integer \(t\), impose

\[
 \sum_a \widetilde g(a)(d_{a,+}-d_{a,-})
 +\sum_c \widetilde g(c)y_c
   =ht+\sum_{r\in\mathbb Z_h^\times}\widetilde r\,b_r. \tag{V}
\]

The physical lift of the quotient cycle is connected exactly when (V)
holds: its total voltage generates \(\mathbb Z_h\).  For \(h=1\), omit the
unit selectors and (V); the unique quotient cycle already has one physical
lift.

A final linear carrier is obtained by deleting one declared physical phase
occurrence of a selected closure orbit. Introduce
\(\delta_{c,\phi}\in\{0,1\}\) for every physical phase occurrence \(\phi\)
in closure orbit \(c\), and impose

\[
\sum_{c,\phi}\delta_{c,\phi}=1,
\qquad
\delta_{c,\phi}\le y_c.                                \tag{B}
\]

Every admitted \((c,\phi)\) record contains the literal endpoints, collar,
protected resources and boundary ledger, with the corresponding compatibility
and resource rows. Deleting that one occurrence preserves the selected
quotient matching and opens the primitive-voltage physical Hamilton cycle
into one path. Deleting the whole quotient orbit would create \(h\) paths
for \(h>1\) (one path when \(h=1\)).

## 6. Conditional private-socket module

Distinct filter middle endpoints do not by themselves give private sockets.
Other matching atoms, closure arcs, collars, or protected witnesses can still
consume the same literal resources.

Private sockets are an additional collar/compiler hypothesis, not a
consequence of the global matching theorem.  In particular, an inherited
matching diamond is not automatically a \(P_4\) packet or a native socket.

The following is a sufficient separated socket normal form, not a necessary
characterization of every possible lift: in a general lift an exceptional
filter can lie internally on a final path and sockets can instead be indexed
by final components.

To express the separated hypothesis without double-counting nested records, use an
exhaustive occurrence-labelled *refinement* catalogue.  For every exceptional
atom \(a\), a refinement \(\sigma\in\Sigma(a)\) declares one local socket,
phase/orientation, ordered endpoints, gain, and the union of all literal
resources used by that refined atom configuration.  Let
\(z_{a,\sigma}\in\{0,1\}\) and impose

\[
\sum_{\sigma\in\Sigma(a)}z_{a,\sigma}=x_a
       \quad(a\text{ incident with an exceptional row}). \tag{S1}
\]

If \(\sigma\) fixes the carrier traversal sign
\(\epsilon(\sigma)\in\{+,-\}\), also impose

\[
 z_{a,\sigma}\le d_{a,\epsilon(\sigma)}.               \tag{S1o}
\]

Any refinement that names a closure or boundary record has the analogous
exact link \(z_{a,\sigma}\le y_c\) (or a displayed allowed-state selector).
Here refinements are topology-neutral: they inherit the parent's middle edge
and gain.  A topology- or gain-changing refinement must replace the parent
arc in (C0), (C1), and (V), not merely satisfy (S1).

Here one \(\sigma\)-record is, by definition, an **orbit-complete package**:
its resource list is the union over all \(h\) physical translates of the
chosen phase-aligned socket pattern. Thus the single selector in (S1)
services every physical occurrence in the selected atom orbit. A catalogue
whose records describe only one physical phase would require one linked
selector and one service equation for every phase; it is not represented by
(S1). The one physical boundary deletion of Section 5 is likewise handled
only after materialization and is not an orbit-complete \(\sigma\)-record.

The physical resource ledger uses \(z_{a,\sigma}\), not both
\(z_{a,\sigma}\) and its parent \(x_a\), for this local configuration.
Nonexceptional atoms continue to use their unrefined \(x_a\) records.  For
every *exclusive* socket/collar/host/protected-occurrence resource \(\rho\),
impose the Boolean union-capacity row

\[
 \sum_{a,\sigma:\,\rho\in R(a,\sigma)}z_{a,\sigma}
 +\sum_{c:\,\rho\in R(c)}y_c
 +\sum_{a\ {\rm nonexceptional}:\,\rho\in R(a)}x_a
 \le \kappa_\rho.                                      \tag{S2}
\]

Here \(\kappa_\rho=1\) for a private resource.  Shared carrier endpoints are
*not* put under a blanket capacity-one row: they obey (D), (C1), and any
typed local compatibility rows in the exhaustive refinement catalogue.  If
compatibility is not a pure capacity constraint, include its explicit
incompatibility row (or an allowed-local-state selector).  A designated
physical boundary socket, if required, is likewise a declared refined
resource and is protected from every competing record.

If the refinements have pre-certified disjoint private resource blocks,
(S1)--(S2) reduce to bipartite matching and ordinary Hall/min-cut is exact.
With intersecting multi-resource refinements the recourse is set packing or a
more general flow problem; a plain Hall inequality is not automatically
exact.  Pairwise endpoint distinctness or a scalar socket count is never
sufficient.

Consequently, (QM), (D), (G), (C0), (CE), (C1)--(C2), and (V) are an exact
finite formulation of the matching/forest/closure/voltage gate allowing
trivial path components. For a nontrivial block-wedge package use (D+) and
the exhaustive wedge catalogue with (BW0)--(BW3). For a linear boundary add
(B). Equations (S1), (S1o), and (S2) are exact for the sufficient separated
socket normal form only after the stated orbit-complete refinement catalogue
and resource-union convention have been supplied. They do not characterize
the broader final-component socket architecture. The sufficient combined
block-wedge target is:

> choose a global quotient perfect matching whose physical diamond lift is a
> spanning nontrivial linear forest, whose inherited exceptional filters have
> private sockets, and whose wedge-compatible closure is one unit-voltage
> physical cycle.

## 7. Physical Benders and asymmetric compilation

The quotient matching/forest/socket/voltage model sits above the existing
physical palette and flow recourse.  Its safe pipeline is:

1. solve the quotient variables \(x,d,y\), and, when the socket or boundary
   modules are instantiated, \(z,\delta\);
2. materialize their complete literal physical lift, including the
   phase-labelled boundary cut;
3. run physical palette, protected-flow, Hamilton/topology, residence, and
   arbitrary-width literal replay;
4. invoke the compiler as a separate literal recourse problem; and
5. return only exact physical min-cut or resource-conflict rows.

A physical inequality may be pulled back to quotient atoms only through the
complete atom-to-lift identity for orbit-complete decisions.  If
\(Q_e=x_{a(e)}\) for every literal
physical occurrence \(e\), then

\[
 \sum_e\alpha_e Q_e
   =\sum_a\left(\sum_{e\in\operatorname{lift}(a)}\alpha_e\right)x_a.
                                                               \tag{P}
\]

Equation (P) is exact substitution, not covariance.  It does not pull back a
phase deletion, orientation-specific collar, refined socket, protected tail,
or compiler choice unless that choice has its own master variable and exact
link equation.  Its certificate must
retain the expanded physical support, atom-to-lift map, exceptional
representatives, multiplicities, and hashes.  A protected guard remains
physical unless the model literally protects the entire orbit.

Likewise, a physical min-cut found at one incumbent is a globally valid
master row only after proving the inequality independently of the fixed
recourse choices.  Otherwise it must be emitted as a guarded row or an exact
incumbent no-good over the phase/orientation/socket decisions in its scope.

No compiler constraint of the forms

\[
 A_{h\cdot i}=hA_i,
\]

orbit-averaged letter load, or quotient-letter equality is valid.  The
compiler may break every carrier symmetry, as it does in the authenticated
K16 optimum.

The existing K17 seam-set-cover executable is therefore not this new master.
Its physical flow separator, protected/ejection distinction, and exact
Hamilton recourse remain reusable after a quotient candidate is physically
materialized.

## 8. Scope

This reduction proves neither that a matching satisfying (QM), (D+), (G),
(C0)--(C2), (CE), (BW0)--(BW3), (V) and the conditional socket rows exists,
nor that a linear boundary satisfying (B) compiles. It removes only the
preliminary residual-Kneser extension gate. The surviving obstruction is
Hamilton-compatible, block-coherent structure inside the global quotient
perfect-matching polytope.

The global matching theorem is

    MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md

The physical forest/socket/voltage conditions specialize the exact lift and
connector criteria already isolated in

    MATH_THEOREM_CATALAN_PERIOD3_FILTER_PACKET_AND_NEUTRAL_CONNECTOR_20260731.md
    MATH_THEOREM_CATALAN_ABSTRACT_COLOUR_FOREST_AND_PHYSICAL_LIFT_GATE_20260731.md

No all-dimension or K17 equality claim is made.
