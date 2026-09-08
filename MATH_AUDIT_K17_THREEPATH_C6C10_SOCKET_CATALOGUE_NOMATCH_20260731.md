# The frozen `K17` three-path tail pairs have no applicable saved `C6/C10` packet, and direct geodesics fail residence

Date: 2026-07-31  
Status: exact source-relative catalogue audit and finite direct-geodesic
no-go; wider occurrence-labelled rethreads remain open

## Result

The frozen three-path fallback exports two complementary-tail pairs:

```text
X shore: 43747 -> 44597, Johnson distance 3;
Y shore: 92614 -> 72813, Johnson distance 5.
```

They suggest a shore-preserving incidence `C6` and `C10`, respectively.
Neither pair is realized by an authenticated applicable packet already in
the workspace:

1. the old-flow `C6` catalogue moves only pure-`U` owners in
   `binom([15],9)`, whereas all four requested owners carry tag bit 15 or
   16; and
2. the common-exterior `C8/C10` catalogue belongs to a different source
   factor.  In its own exact state graph the `X` pair has no correctly typed
   endpoint states.  The `Y` pair has one typed state at each endpoint, but
   their directed distances are `8` in both directions and no length-five
   circuit contains the pair.  No packet contains either requested pair in
   any owner role.

The complete shortest-Johnson-path normal form is also closed.  Exact
enumeration gives

```text
                         C6       C10
shortest geodesics        36     14400
intermediate-owner clear  25      5066
lower-facet clear         22      4052
jointly clear             20      2207
full direct residence      0         0
```

Every raw direct splice creates exactly two strict `D2` runs of length two
and two strict `D3` runs of length three.  For the `X`-shore `C6`, the
blocked coordinate is tag bit 16; for the `Y`-shore `C10`, it is tag bit
15.  This is a boundary theorem, independent of the geodesic order.

Therefore the proposed direct shortest-geodesic physicalization is

\[
                    \boxed{\text{infeasible in both sockets}.}
\]

No residual `b`-matching or connectivity solve is reached or needed.

## Boundary proof

At each socket, the selected left atom ends with exactly two consecutive
owners carrying the opposite tag, and the selected right atom begins with
exactly two such owners.  Every owner on a shore-preserving geodesic has
the shore tag equal to one and the opposite tag equal to zero.  Direct
insertion therefore brackets both length-two strings by zero.  They become
two strict bad `D2` runs.  Applying adjacent OR extends each by one edge,
so the derivative has two strict length-three `D3` runs.  The conclusion
does not depend on the order of deleted or inserted old-coordinate bits.

The exact geodesic counts are `(3!)^2=36` and `(5!)^2=14400`.  The audit
nevertheless enumerates every path literally and checks owner ranks,
Johnson adjacency, lower-facet ranks, collisions, and the complete local
run ledger.

## Port and palette scope

The four exposed endpoint ports

```text
10979, 11829, 27078, 7277
```

all have fixed macro degree two and residual pure-`U` demand zero.  Thus an
ordinary residual connector cannot use them; a valid repair must exchange
or rephase saturated incidences.

An open owner geodesic is not by itself a palette-preserving circuit.  It
does not specify occurrence-labelled deleted and inserted incidences.  The
saved common-exterior packet guards transport neither to the frozen
three-path source nor to the repaired six-swap forest.

The result excludes only:

* membership in the two authenticated saved catalogue domains; and
* literal insertion of a shortest shore-preserving Johnson geodesic into
  the frozen endpoint collars.

It does **not** exclude a non-common-exterior occurrence-labelled circuit,
a simultaneous macro rethread that changes either endpoint collar, a
longer packet, a different three-path witness, or the primary radius-two
occurrence frontier.  It is not a `K17` no-go.

## Reproducibility

Run

```text
python3 scratch/audit_k17_tailpair_c6c10_catalogue_nomatch_20260731.py
python3 -m py_compile scratch/audit_k17_tailpair_c6c10_catalogue_nomatch_20260731.py
```

Frozen audit artifacts:

```text
scratch/audit_k17_tailpair_c6c10_catalogue_nomatch_20260731.py
SHA-256 21ca3b3322809fc5c66ae7665ae090f13c27aa1f3b03ed2673326833e8e44674

scratch/k17_tailpair_c6c10_catalogue_nomatch_20260731.audit.json
SHA-256 8202932399108decbca30cb88c5cb6f857f028fd2337e3e2b5824b2cb211143b
payload 13d07a4c311e3cbe124bb7e44c8c8b54ba2d65a12d9386572e940532ef39dd90
```

An independent static replay of the rejected constructor recovered the
same raw counts `20/2207`, the same full-context counts `0/0`, and the same
four bad boundary runs per candidate.  That prototype must not be treated
as a completed residual-factor constructor: it aborts before its flow call.
