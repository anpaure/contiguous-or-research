# Fixed-core `k=17` GK ear completion has an internal-edge Hall obstruction

Date: 2026-07-31  
Status: **exact scoped no-go** for the corrected fixed-core ear ledger.  This
does not rule out cutting and rethreading the Greene--Kleitman core, nor any
other `k=17` architecture.

## 1. Authenticated input and exact ear columns

Take the verified two-cut Greene--Kleitman forest literally: it has `10152`
edges, `15376` rank-seven vertices, `10448` degree-one endpoints, `4928`
degree-two vertices and `5224` path components.  Its occupied rank-eight and
rank-nine palettes have sizes `10152` and `4928`.  There are `4072` unused
rank-seven vertices.

A length-`j` fixed-core ear is a path

\[
  e=(u=w_0,w_1,\ldots,w_{j-1},w_j=v),
\]

where `u,v` are original degree-one endpoints in different GK components and
the `j-1` internal vertices are previously unused rank-seven sets.  Its exact
resources are:

* the two old endpoints and their two original components;
* its `j-1` internal rank-seven vertices;
* the `j` rank-six intersections \(w_{i-1}\cap w_i\);
* the `j` rank-eight unions \(w_{i-1}\cup w_i\);
* the `j+1` rank-nine turns, including the two boundary turns against the
  retained old neighbours of `u` and `v`.

For a locally clean column, consecutive vertices are Johnson-adjacent, the
rank-eight unions avoid the old palette and are pairwise distinct, and the
rank-nine turns have rank nine, avoid the old palette and are pairwise
distinct.  The last pairwise rank-eight clause is worth stating explicitly:
the earlier producer checked old-palette avoidance but did not spell out this
within-ear injectivity row.  An independent strict replay shows that adding
it does **not** change the advertised all-unused local split: `252` rows have
a clean three-edge witness and the remaining `42` have a clean four-edge
witness.

The proposed simultaneous selection would use

\[
  (x_1,x_2,x_3,x_4)=(4024,905,252,42).
\]

It therefore selects `5223` component links, consumes `10446` old endpoints
and `1535` unused rank-seven vertices, and introduces `6758` rank-eight edge
colours and `11981` rank-nine turn colours.  Endpoint, unused-vertex,
rank-eight and rank-nine resources must each obey a partition cap; every
missing rank-six colour must be covered; and the component links must form a
spanning tree.  Because every old component has two endpoints, that tree is
then one path.

## 2. The weighted Hall cut

Let \(Y\) be the missing rank-six colours with no rank-seven superset among
the original GK endpoints.  Literal reconstruction gives

\[
  |Y|=674.
\]

If a selected new edge carries a colour in \(Y\), neither endpoint of that
edge can be an original endpoint.  It must be an internal--internal edge of
an ear.  A length-`j` endpoint-to-endpoint ear has exactly

\[
  (j-2)_+=\max(j-2,0)
\]

such edges.  Since one Johnson edge has only one rank-six intersection,
the rank-six cover rows imply the necessary weighted Hall inequality

\[
  \boxed{\sum_j (j-2)_+x_j\ \ge\ 674.}                \tag{2.1}
\]

The corrected ledger has only

\[
  x_3+2x_4=252+84=336
\]

internal--internal slots.  Thus (2.1) fails by

\[
  674-336=338.                                      \tag{2.2}
\]

This argument permits repeated rank-six colours and ignores every other
resource collision, so it is a genuine first projection of the full master,
not an injectivity assumption in disguise.

There is an equivalent sharp direct-ear row.  For any positive-length ear
ledger with `E=5223` ears and `I=1535` internal vertices, put
\(x_1\) for the number of direct ears.  Then

\[
 \sum_j(j-2)_+x_j
 =I-(E-x_1)=x_1-3688.
\]

Consequently every fixed-core no-cut ledger must satisfy

\[
  \boxed{x_1\ge4362.}                               \tag{2.3}
\]

The declared value `4024` again misses by `338`.

### The first proof-safe scalar repair

If ears are still restricted to lengths at most four and the `42` declared
four-edge assignments are retained, tightness in (2.1) forces

\[
 (x_1,x_2,x_3,x_4)=(4362,229,590,42).               \tag{2.4}
\]

Indeed this is obtained from the failed ledger by `338` copies of

\[
 2E_2\longmapsto E_1+E_3.                            \tag{2.5}
\]

Each replacement preserves the number of joins, inserted vertices, new
edges and new turns, while adding one internal--internal provider slot.
Equation (2.4) is only a necessary scalar face, not a construction.

It is zero-slack already at rank six.  The `6758` new edges split into
exactly `674` internal--internal slots and `6084` endpoint-incident slots.
Thus every internal--internal slot must carry a different member of (Y).
The other slots must carry the remaining `1550` missing colours and the
`4534` repeated colours.  In particular both internal edges of each
four-edge ear must be useful (Y)-providers; a catalogue recording only one
designated colour per long ear is insufficient.

## 3. Why exposing old internal vertices is outside the theorem

An original internal GK vertex already has degree two.  Using it as a new
attachment without deleting an old edge creates degree three and cannot be
part of the desired spanning path.  Deleting an old edge exposes it, but
also changes the number of core components, deletes an authenticated
rank-eight colour, changes up to two old rank-nine turns, and invalidates the
fixed `10152`-edge scalar ledger.  Such cut-and-rethread columns are a valid
new architecture, but they are not repairs inside the fixed-core ear master
audited here.

Thus the `252+42` local witnesses establish only local availability for the
294 all-unused rows.  They cannot be selected into the advertised global
schedule: after assigning one insulated edge to each of those 294 rows, only
`42` insulated slots remain for the other `380` members of `Y`.

For a replacement catalogue on the tight face (2.4), the first polynomial
projection is a matching problem: each four-edge ear offers a pair of
(Y)-colours and each three-edge ear one (Y)-colour.  The `42` forced
four-edge demands must be paired with `42` distinct partners, after which
the other `590` colours need singleton three-edge providers.  This matching
projection is necessary only.  Lifting an ear consumes its two endpoint
sockets, internal rank-seven vertices, rank-eight unions and rank-nine
turns simultaneously.

The complete lifted master is therefore a `0-1` ear-bundle packing with
rank-six cover equations, partition caps for all literal resources, fixed
length rows, and graphic-base inequalities on the component links.  It is
not ordinary matroid intersection: overlapping resource bundles fail
exchange, and arbitrary endpoint compatibility already contains Hamilton
path.  A genuine flow face appears only after fixing an acyclic component
order and making every non-target bundle private, leaving a bipartite
target-to-slot matching.

## 4. Reproducer and scope

The independent reproducer reconstructs the labelled core, authenticates
the upstream JSON, recomputes the `2224/674/294` missing-colour census,
replays the `252/42` local split with strict within-ear rank-eight
injectivity, and checks both forms of the Hall inequality:

```text
scratch/audit_k17_corrected_gk_ear_hall_obstruction_20260731.py
scratch/k17_corrected_gk_ear_hall_obstruction_20260731.audit.json
```

The JSON verdict is

```text
UNSAT_FIXED_CORE_CORRECTED_EAR_LEDGER
```

with canonical payload

```text
c5807baabd336d7aecb388e55c02cae1c713d004092c2c7a5e972892aec3103e
```

No conclusion is made about a cut-and-rethread GK core, prefix completion,
upper coverage, or unrestricted optimal `k=17` words.
