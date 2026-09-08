# A sharp endpoint-port obstruction to independent connector tests

Date: 2026-07-31  
Status: exact Johnson path-interface counterexample and finite minimality
within the complete simple-port class; not a Catalan linear-matching no-go

## 0. Verdict

Independent seam residence, deep-target Hall, and a Dirac component graph do
not guarantee a component-spanning Johnson path.  The missing correlation is
already the matching constraint on the two physical endpoint ports of each
path component.

There is a literal six-component rank-six Johnson interface with all of the
following properties.

1. Its component connector graph is `K_6`, hence has minimum degree five.
2. There is exactly one endpoint seam for every component pair, and all
   twelve endpoint ports have positive seam degree.
3. Every one of the fifteen seams is individually residence-safe for minimum
   internal run length three.
4. Five prescribed abstract deep-debt labels may each use every seam, so
   their debt--seam service graph is `K_{5,15}` and satisfies every Hall row
   with wide slack.
5. Nevertheless the endpoint-port graph has matching number four.  A linear
   spanning chronology needs five port-disjoint seams and exactly two global
   unmatched endpoints, so none exists.

Thus even the strongest possible simple component adjacency and service Hall
conditions miss a Tutte--Berge obstruction.  Any all-`m` connector theorem
must correlate topology, endpoint ports, residence collars, and debt service;
the component graph and target incidence graph cannot be tested separately.

## 1. Exact path interface

Work in `J(n,6)` on the disjoint coordinate banks

```text
S={0,1,2,3,4},       U={10,11,12,13,14,15},
E={20,21,22,23,24},  t_i=30+i  (0<=i<=5).
```

For a list of removed coordinates `r_1,...,r_s` and added coordinates
`a_1,...,a_s`, the notation

```text
A -- (r_1/a_1, ..., r_s/a_s)
```

means the Johnson path obtained by performing the swaps in that order.  Take
the following six pairwise vertex-disjoint paths:

```text
P_0: U
     -- (10/t0,11/20,12/21,13/22,14/23,15/24)

P_1: S+t1
     -- (0/24,1/23,2/22,3/21,4/20)

P_2: S+t2 -- (1/10,0/13,2/14,3/15,4/11)
P_3: S+t3 -- (2/10,0/12,1/14,3/15,4/11)
P_4: S+t4 -- (3/10,0/12,1/13,2/15,4/11)
P_5: S+t5 -- (4/10,0/12,1/13,2/14,3/11).
```

Call the displayed initial endpoint port zero and the final endpoint port
one.  Direct intersection testing gives exactly these cross-component
endpoint seams:

```text
P_0^1--P_1^1;
P_0^0--P_i^1                         for 2<=i<=5;
P_i^0--P_j^0                         for 1<=i<j<=5.
```

There are fifteen seams, exactly one for each unordered component pair.  In
particular the contracted graph is `K_6`.  The endpoint-port graph itself is
the disjoint union

```text
K_2  sqcup  K_{1,4}  sqcup  K_5.                    (1.1)
```

Every port occurs in (1.1).

## 2. Literal residence check

For an endpoint port `p` and a coordinate `z` in its middle set, let
`lambda_p(z)` be the length of its positive boundary run, measured inward
along its component.  If a seam joins endpoint sets `A,B`, the following is
the robust local collar test which makes the seam safe without relying on
either remote port becoming one of the two eventual global endpoints:

```text
lambda_A(z) >= r                         for z in A-B,
lambda_B(z) >= r                         for z in B-A,
lambda_A(z)+lambda_B(z) >= r             for z in A intersect B.    (2.1)
```

The first two rows concern runs terminated or begun by the seam; the third
concerns the common-coordinate runs merged by it.  This robust test is
sufficient, but is not necessary when a short run reaches a final global
endpoint and is therefore exempt.  Replaying the six paths
above gives minimum left-hand side at least three on every one of the
fifteen seams.  Each unjoined path itself has no short internal run, and
literal concatenation across each single candidate seam has none either.
The seam margins are

```text
6, 3,3,3,3, 3,3,3,3, 4,4,4,4,4,4.
```

Thus this is not an obstruction caused by an individually unsafe collar.
As required for a linear rather than cyclic chronology, no condition is
imposed on the two endpoint runs that would remain globally exposed.

## 3. The exact Tutte obstruction

A connector set for a linear chronology uses an endpoint port at most once.
After contraction, five seams connecting all six components therefore form
a Hamilton path and consume ten of the twelve ports, leaving exactly the two
global endpoints.

But (1.1) has matching number

```text
nu(K_2)+nu(K_{1,4})+nu(K_5)=1+1+2=4.                 (3.1)
```

Equivalently, delete the center `P_0^0` of the `K_{1,4}` block.  The
remainder has five odd components: its four isolated leaves and the `K_5`.
The Tutte--Berge deficiency is therefore at least `5-1=4`, forcing at least
four unmatched ports and proving (3.1).  Five port-disjoint seams—and hence
a six-component linear path—are impossible.

The role of the two global endpoints is exact here.  A cyclic closure would
need six port-disjoint seams (a perfect port matching), while the requested
linear object needs only five.  The fixture rules out even the latter; it is
not using a cyclic requirement by accident.

## 4. Why the independent tests all pass

The component graph is complete, so every Dirac or ordinary graphic-rank
test passes: its graphic rank is five and it contains many spanning trees.
Declare five bounded deep-debt labels `d_1,...,d_5`, with each label
serviceable by every one of the fifteen seams.  This is abstract service
metadata, not a claim that the short fixture realizes five specified
contiguous-OR masks.  The target--seam graph is `K_{5,15}`;
for every target set `X`,

```text
|N(X)| = 15 >= |X|.
```

It has a five-edge service transversal.  Every seam in that transversal is
individually residence-safe by Section 2.  What fails is simultaneous port
disjointness.  This proves that the correct joint row must see the physical
two-port matching (or an equivalent matching-parity/gammoid encoding), not
only graphic rank plus a separate service transversal.

## 5. Sharp finite scope

Within the following natural class the order six is minimal:

* the component graph is complete;
* there is exactly one seam per unordered component pair;
* each seam chooses one of the two ports at either end; and
* both ports of every component have positive seam degree.

Exhaustive enumeration of all `4^{n choose 2}` port labelings gives

```text
n       admissible labelings       no linear port-respecting path
2                0                              0
3                8                              0
4             1296                              0
5           537824                              0
```

The displayed `n=6` labeling is the first counterexample.  This minimality
claim is deliberately limited to the complete, simple, two-active-port
class; smaller counterexamples exist if an endpoint port may be isolated or
the contracted component graph is weakened.

## 6. Consequence for a positive theorem

Let `R` be the graph on occurrence-labelled endpoint ports whose edges are
the seams surviving literal residence and local shadow replay.  A necessary
linear connector condition is

```text
nu(R) >= K-1,                                      (6.1)
```

with a size-`K-1` matching whose contracted component edges are connected.
Because every component supplies only two ports, connectedness then forces
the contraction to be a path and leaves exactly two physical endpoints.
Prescribed deep service must be imposed on that same matching, not assigned
to an independent copy of the seam catalogue.  The fixture proves that
Dirac on the contraction and Hall on the service projection do not imply
(6.1).

The port-only relaxation does have an exact min--max row.  By Tutte--Berge,
for a graph on the `2K` ports,

```text
nu(R) >= K-1

iff  o(R-S)-|S| <= 2                       for every S subseteq V(R).  (6.2)
```

The right side permits exactly the two unmatched global ports.  In the
fixture, `S={P_0^0}` gives `o(R-S)-|S|=4`, so (6.2) fails sharply.  Condition
(6.2) still does not impose connectedness after contraction or correlated
deep service; it is the exact first relaxation, not the full connector
theorem.

The exact min--max theorem for the full serviced, component-spanning problem
is not ordinary Hall plus graphic rank: already its service-free projection
contains an endpoint matching/Tutte row.  Whether the special recursively
generated Catalan catalogues force the required correlated matching remains
open.

## 7. Reproduction and scope

Run

```text
python3 scratch/audit_catalan_connector_port_tutte_counterexample_20260731.py
```

The replay reconstructs all paths, all endpoint adjacencies, every residence
margin, literal absence of short internal runs before and after each
one-seam concatenation, the maximum port matching, the zero Hamilton-path
count, the complete abstract debt Hall rows, and the `n<=5` minimality
census.

This note is an exact **interface counterexample**.  The six paths are not a
spanning Catalan linear matching, do not claim exact global lower/upper
palettes, and do not address deeper-shadow generation inside a recursive
Pascal carrier.  Its conclusion is only that independent connector
projections are insufficient, even on a literal Johnson endpoint interface.
