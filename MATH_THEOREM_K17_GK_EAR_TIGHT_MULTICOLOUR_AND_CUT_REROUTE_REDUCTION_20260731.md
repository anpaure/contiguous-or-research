# The post-Hall `k=17` GK ear gate is a tight multicolour exact cover

Date: 2026-07-31  
Status: exact reconciliation of the bounded-ear census with the stronger
all-length fixed-core Hall no-go; exact cut projection and lower bound only.
No cut-and-reroute ear packing or `k=17` word is claimed.

## 0. Superseding outcome

The length-five catalogue below was a useful diagnostic, but it is no longer
a live completion branch.  Its complete strict projection has only `851`
provider triples.  Of the `280` colours unresolved through length four, only
`44` occur in any such triple, leaving `236` literal zero rows at length five.

More decisively, the greatest supported edge/wedge catalogue closes **all**
ear lengths on the immutable half-rotation (`s=8,9`) GK forest.  After three
monotone support-peeling
rounds it has `145117` edges and `4194675` wedges.  Its missing-rank-six versus
fresh-rank-eight provider graph has

\[
       \nu=1780<2224,
\]

with `416` zero rows and a Dulmage--Mendelsohn witness of `584` rows against
only `140` unions.  Every locally clean fixed-core ear family is a post-fixed
point of the peeling operator, so every one of its carrier edges survives;
rank-eight injectivity would then induce a matching saturating all `2224`
rows.  This proves that no immutable-core completion exists at arbitrary ear
length for that fixed cyclic separation.

For that fixed forest, the remaining live architecture must cut and reroute.
In the fixed non-direct ledger with `336` inserted--inserted slots, the exact
cut-port census strengthens the scalar `c>=169` bound to

\[
                              \boxed{c\ge175}.
\]

This is still only a necessary relaxed-provider row.  A separate CP-SAT model
reports optimum `312` for a narrower subproblem: assign the `380`
zero-endpoint colours having an old internal provider injectively to vertices
exposed by pairwise vertex-disjoint old-edge cuts.  Its current literal
certificate has `312` cuts and all `380` assignments, but it selects no ears
and does not replay deleted colours, fresh rank-eight/rank-nine resources, or
topology.  Thus `312` is neither an attained physical cut count nor a bound on
architectures outside that exposure model.

The subsequent all-cut sweep in
`MATH_THEOREM_K17_GK_CYCLIC_CUT_SUPPORTED_EAR_SWEEP_20260731.md` finds a
different escape: adjacent cyclic separations `s=1,16` have full supported
provider rank `8736/8736`.  Nothing in the present half-rotation no-go applies
to their different endpoint and unused-vertex banks.

## 1. Authoritative corrected input

The fixed two-cut Greene--Kleitman forest has `5224` path components,
`15376` used rank-seven vertices and `4072` unused rank-seven vertices.  Its
completion has room for exactly

\[
 J=5223\quad\hbox{joins},\qquad I=16911-15376=1535
\]

new internal rank-seven vertices.

Among the `2224` missing rank-six colours, let (Y) be the `674` having no
original path-endpoint superset.  The full strict local census is

| first clean fixed-core provider | colours |
|---|---:|
| length 3 | 266 |
| length 4 but not length 3 | 128 |
| none through length 4 | 280 |

The obsolete `(4024,905,252,42)` ledger has only `336` internal--internal
edge positions.  It is impossible by the exact Hall row

\[
             \sum_{j\ge3}(j-2)x_j\ge674.             \tag{1.1}
\]

## 2. The tight no-cut face

For any no-cut fixed-core ledger,

\[
 \sum_jx_j=J,qquad \sum_j(j-1)x_j=I.
\]

Writing (x_1) for the direct ears, the number of internal--internal edge
positions is

\[
 Q=I-(J-x_1)=x_1-3688.                              \tag{2.1}
\]

Thus (x_1\ge4362).  The smallest face has

\[
 x_1=4362,qquad \sum_{j\ge2}x_j=861,qquad Q=674.   \tag{2.2}
\]

This face is zero-slack at rank six.  Every one of the `674`
internal--internal edges must carry a different member of (Y).  The other
`6084` new edges must carry exactly the other `1550` missing colours and
the `4534` repeated colours.

Consequently a long ear cannot be represented by one designated missing
colour.  All of its internal intersections are compulsory resources:

* a length-three ear supplies one (Y)-colour;
* a length-four ear supplies a pair;
* a length-five ear supplies a triple;
* in general a length-(j) ear supplies a ((j-2))-set.

The selected sets must partition (Y).

## 3. The first length-five equality pattern

The `280` colours with no provider through length four force at least

\[
                  \left\lceil{280\over3}\right\rceil=94          \tag{3.1}
\]

length-five ears if lengths are capped at five.  A class-segregated scalar
equality pattern is

\[
 (x_1,x_2,x_3,x_4,x_5)=(4362,439,264,64,94).         \tag{3.2}
\]

Here the `94` triples have `282` slots for the `280` unresolved colours and
two others, the `64` pairs have `128` slots, and the `264` singleton ears
use the remaining slots.  Direct calculation gives

\[
 \sum x_j=5223,quad
 \sum(j-1)x_j=1535,quad
 \sum(j-2)_+x_j=674,                                \tag{3.3}
\]

and retains `6758` new edges and `11981` new turns.

Equation (3.2) is **not** an existence claim.  It is the smallest obvious
palette-level target for a strict length-five census.  The completed census
answers its first question negatively: only `44/280` unresolved rows occur in
any strict provider triple.  The stronger supported-catalogue Hall theorem in
Section 0 closes every larger fixed-core length as well.

## 4. Exact multicolour master

For each locally clean ear (e), record:

* its two old endpoint sockets and component pair;
* its internal rank-seven vertices;
* all rank-eight edge unions and rank-nine turns, including boundary turns;
* its full set (Y(e)\) of internal rank-six intersections; and
* the remaining boundary rank-six intersections.

On the tight face the first master row is

\[
                    \bigsqcup_{e:z_e=1}Y(e)=Y.       \tag{4.1}
\]

The lift adds partition caps for every endpoint, internal rank-seven value,
rank-eight union and rank-nine turn, fixed length counts, coverage of the
other missing rank-six colours, and graphic-base cuts on the `5224`
component nodes.  With `5223` component links and endpoint degree at most
two, a graphic base is one spanning path.

There is no generic ordinary-matroid or flow theorem for this master.
Lengths three and four alone give monomers and dimers, hence a matching
projection.  Length five introduces triples and therefore general
hypergraph exact cover.  Resource bundles also fail matroid exchange, while
arbitrary endpoint compatibility already contains Hamilton path.  A
polynomial flow face survives only after fixing an acyclic component order
and making every non-target bundle private.

## 5. Exact cut-and-reroute projection

Let (D) be a set of (c) deleted old GK edges.  Since the old core is a
forest, deletion gives

\[
 E_{\rm old}=10152-c,quad K=5224+c,quad
 J=5223+c,quad E_{\rm new}=6758+c.                  \tag{5.1}
\]

The truly new rank-seven budget remains `1535`.  Each cut releases one old
incidence at each endpoint, so capacity alone gives at most `2c` new old
ports.  If one kept the obsolete `Q=336` internal capacity, the first
optimistic port bound would be

\[
                  336+2c\ge674,qquad c\ge169.       \tag{5.2}
\]

This is only a lower bound and is not attainable in the relaxed labelled-port
census.  The `674` hard colours require `338` cut-port services.  All eligible
two-useful-endpoint old edges collectively see only `294` of them; the outside
contribution profile forces at least twelve one-useful-endpoint cuts.  Hence
`2c-338>=12` and `c>=175`.

For a fixed cut set, the first exact projection
is a bipartite max-flow from colours in (Y) to released old-vertex port
copies, with unmatched colours charged to internal--internal slots.  Choosing
the cut set is a paired-port activation problem: one binary old-edge cut
opens capacity at both endpoints.  In addition, every cut deletes a formerly
unique rank-six edge colour, a rank-eight colour and up to two old rank-nine
turns.  Those debts and the changed component ledger must be replayed in the
literal master; (5.2) alone is not a cut construction.

## 6. Scope and next exact experiment

The strict length-five census and every immutable-core longer-ear search at
the half-rotation `s=8,9` are retired.  Inside that fixed forest, the next
proof-safe finite gate is cut-relative:

1. choose a vertex-disjoint old-edge cut set `C`;
2. add the deleted old rank-six colours to the demand shore and release only
   the rank-eight/rank-nine resources actually destroyed by `C`;
3. rebuild the supported edge/wedge fixed point relative to the new ports;
4. require full provider matching rank `2224+|C|` before attempting literal
   ear packing, resource disjointness, or component-path topology.

The `312`-cut exposure assignment is only a candidate cut bank for step 1 and
one part of step 2.  It does not pass steps 3--4 by construction.  No result
here certifies a tail, prefix, upper continuation, residence, compiler, or
`k=17` word.

Audit:

```text
scratch/audit_k17_gk_ear_tight_multicolour_cut_reduction_20260731.py
scratch/k17_gk_ear_tight_multicolour_cut_reduction_20260731.audit.json

scratch/census_k17_fixed_gk_tight_length5_provider_triples_20260731.cpp
scratch/k17_fixed_gk_tight_length5_provider_triples_20260731.census.json

scratch/verify_h2_k17_gk_ear_compact_incidence_20260731.py
scratch/h2_k17_gk_ear_compact_incidence_20260731.verify.json

scratch/audit_k17_gk_cut_port_matching_lower_bound_20260731.py
scratch/k17_gk_cut_port_matching_lower_bound_20260731.audit.json
```
