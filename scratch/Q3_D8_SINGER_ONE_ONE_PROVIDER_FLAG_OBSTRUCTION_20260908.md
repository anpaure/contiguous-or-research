# A pure obstruction to the two-B/B plus one-L/N provider plan

2026-09-08. Pure proof by ternary_lift, with the final endpoint-only
strengthening suggested by root and independently audited by
direct_route. No computation is a premise. Root's separate bounded
provider inventory agrees with the obstruction.

## 1. Scope and the 40-edge quotient

Use the fixed endpoint words

    C_end=00112244, D_end=33776655

and their seven Singer translates with ranks 0,...,7, together with
their upper complements. Write the fixed coordinate as infinity and
the cyclic coordinates as 0,...,6, corresponding to global labels
(1,2,4,3,6,7,5).

A rank-seven target with exactly one one is a Boolean flag

    T subset T union {o},  |T|=3,

where T is its two-set and o is its one-coordinate. There are 40
Singer flag orbits. Their quotient graph has eight rank-three
vertices and ten rank-four vertices, with degrees five and four.
The endpoint pair covers fourteen distinct flag orbits. Consider
partitioning the other 26 using exactly two generic fourteen-row
B/B bundles and one L/N bundle, with literal profiles

    B=AABBCCDD, L=ABABCDCD, N=ABACBDCD.

Coordinate infinity is in an interior B or C block of each B/B
shore word. L/N may have any coordinate embedding; its permissible
positions are derived below. This is the provider problem in the
original and amended literal profile ledgers. The theorem does not
exclude arbitrary different providers or endpoint words.

For x_infinity=0, normalize the unique cyclic one to zero. The
endpoint-covered two-triple signatures are

    F={123,126,135,146,234,245,456}.                 (1)

For x_infinity=2, the covered two-pair signatures are 16,35,25,26,
45,56. For x_infinity=1, the endpoint covers necklace 115. The
four residual necklaces have gap types 124,142,133,223.

## 2. Rank-four parity forces the L/N flags

For a B/B row with block orders (a,b,c,d) and (e,f,g,h), its six
short critical flags form the alternating path

    efg -- aefg -- aef -- abef -- abe -- abce -- abc.

Its endpoints have rank three, so it has even degree at every
rank-four vertex, also after the Singer quotient. Its complemented
constituent has the same property. Every B/B bundle therefore has
even rank-four degrees.

The lower endpoint row gives an eight-edge path between its two
complementary rank-four shores. The upper complement gives a
six-edge path with rank-three ends. Hence the residual graph has
odd rank-four degree at exactly the two complementary shore
vertices H and H-complement, where H=infinity+012 has type115.

The two L/N flags must meet these two vertices. If infinity is N's
B or C axis, one L/N flag has unique one at infinity. Its upper
vertex forces two-triple necklace115, already endpoint-covered.
Such an L/N cannot be in an exact residual partition. This rules
out both internal N positions even if B/B endpoint positions had
otherwise been allowed by a different quota calculation.

At every remaining L/N position both unique ones are cyclic. The
only residual flag at H has x_infinity=2 and pair12; the only
residual flag at H-complement has x_infinity=0 and triple156.
Thus L/N must supply precisely

    (x_infinity=2, pair12), (x_infinity=0, triple156). (2)

It supplies none of the four residual infinity-one necklaces.

## 3. A B/B supplier of necklace223 repeats an endpoint flag

Reverse globally if necessary to put infinity in B/B's second
block. Write the block orders as

    (a,infinity,c,d), (e,f,g,h).

Translate so that g=0 and put U={a,e,f}, V={c,d,h}. These two
triples partition {1,2,3,4,5,6}. Two x_infinity=0 critical flags
have unique one g and two sets U,V: original split(2,5), and the
complement of original rank-nine split(4,5). Both U,V must avoid
the set F in (1).

The same U,V are the two-triples of the bundle's x_infinity=1
critical flags: original split(3,4), and the complement of original
rank-nine split(3,6). The exhaustive complementary three-set
partitions avoiding F are:

| U/V partition | Cyclic gap types |
| --- | --- |
| 124 / 356 | 124 / 142 |
| 125 / 346 | 133 / 124 |
| 134 / 256 | 142 / 133 |
| 145 / 236 | 133 / 133 |

None contains223. Equivalently the only triples in {1,...,6} of
gap type223 are135,136,146,246. Their complementary partitions
are135/246,136/245,146/235; each contains an endpoint signature
from F. Thus covering223 with such a B/B necessarily repeats an
endpoint-covered x_infinity=0 flag.

An exact residual partition permits no repetition. Neither B/B
can supply223, and Section2 shows that L/N cannot supply it.
Therefore the proposed26-edge partition is impossible. A literal
uncovered target is

    x_infinity=1, cyclic two-set {0,2,4},
    global vector (1,2,0,0,2,0,2,0).

This is an endpoint-only availability obstruction. It does not use
the seed's other critical targets, central projection constraints,
the remaining seven profiles, or a candidate catalogue.

## 4. Independent bounded inventory

Root's one0.036014-second inventory read720 B/B placements and24
endpoint-position L/N placements with additional necessary
positive-weight filters. Three B/B and five L/N candidates passed
the individual filters; no provider triple passed. Artifacts:

- `q3_d8_singer_one_one_provider_inventory_20260908.py`
- `Q3_D8_SINGER_ONE_ONE_PROVIDER_INVENTORY_20260908.json`.

All three surviving B/B candidates share the infinity-one133
necklace. The pure proof is stronger: already the larger family
with only endpoint-flag avoidance has no223 supplier. The finite
result is independent verification, not a premise.

## 5. The earlier L-interior overlap, with its narrower scope

Orient infinity as L's B axis and write
L=(a,infinity,a,infinity,c,d,c,d), N=(e,f,e,g,f,h,g,h).
The forced flags(2) normalize as

    f=0, g=5, {a,e}={1,2}, {c,d,h}={3,4,6}.

All twelve such embeddings repeat the seed critical orbit with
x_infinity=1, cyclic Z=346,T=12, which translates by minus three
to seed signature Z=013,T=56. Their central cell(3,5) has unique
cyclic one5 and twos012, hence normalized triple234; its complement
has triple156. Both central orbits are in the seed.

This narrower calculation applies only to L-interior placements,
not to L-endpoint or N-endpoint placements. Section3 gives the
stronger endpoint-only proof for all L/N positions consistent
with an exact provider partition, under the B/B-interior scope.

## 6. A different endpoint: necklace matching passes, flags still fail

The following separate endpoint pair has distinct critical signatures
and is compatible with the old seed's positive projection targets:

    C_end=00446655, D_end=77223311.

Its cyclic block orders are (infinity,2,4,6) and (5,1,3,0).
Its infinity-one necklace is223. Its forbidden x_infinity=0 triples
and x_infinity=2 pairs are respectively

    F'={135,246,245,134,236,256,124},
    P'={25,36,14,15,46,35}.                         (3)

Its surviving complementary triple partitions include125/346 and
126/345, which match the four residual necklace classes as
133/124 and142/115. Thus there is no missing-necklace obstruction
at this first level. This observation does not construct a flag
partition or a full cover.

In fact the more detailed flags prevent the required125/346 B/B.
The residual rank-four133 vertex has only the infinity-one edge
and pair34; the other incident pair signatures14 and36 belong to
P'. Use the normalized B/B parameters from Section3.

If U=125,V=346, this forces f=5 and {a,e}=12. The critical triple
((V minus {c}) union {0})-c, from complemented split(5,4), is134
or236 when c=3 or4. Both are in F', so c=6. But then the critical
pair {a,c}-e is46 or15, both in P'.

If U=346,V=125, the133 vertex forces h=5 and {c,d}=12. The
original split(1,6) has triple((U minus {a}) union {0})-a; avoiding
F' forces a=6. Pair{a,e}-c avoids P' only when (e,c)=(4,2), but
then pair{a,c}-e=25 belongs to P'.

Both orientations are impossible. Every perfect matching of the
four residual necklaces would need125/346 (the other choice would
need the already-forbidden134/256 partition). Hence this particular
replacement endpoint also has no two-B/B plus one-L/N provider
partition. This proof is pure; no inventory ran for this endpoint.

## 7. A general necessary condition, not a universal obstruction

For arbitrary endpoint B/B orders, the ten complementary triples
give this universal necklace graph:

| Complementary partition | Necklace pair |
| --- | --- |
| 123 / 456 | 115 / 115 |
| 124 / 356 | 124 / 142 |
| 125 / 346 | 133 / 124 |
| 126 / 345 | 142 / 115 |
| 134 / 256 | 142 / 133 |
| 135 / 246 | 223 / 223 |
| 136 / 245 | 223 / 142 |
| 145 / 236 | 133 / 133 |
| 146 / 235 | 223 / 124 |
| 156 / 234 | 124 / 115 |

The nonloop part is K_(2,3) between {124,142} and {115,133,223},
together with the124--142 edge. If the endpoint removes necklace124
or142, the four residual necklaces contain only one left vertex
and three right vertices. They cannot be paired by two nonloop
edges. Therefore an endpoint in either of those two classes is
universally excluded under the two-B/B-interior provider plan.

Endpoint necklaces115,133,223 are the only possible classes. The
preceding sections exclude two specific orders among those classes;
they do not prove that every endpoint order is impossible. No
universal obstruction or full positive provider triple is claimed.
