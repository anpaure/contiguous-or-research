# J6 endpoint continuation: exact triangular-debt census

Date: 2026-08-01

Status: exact finite audit of every oriented contiguous continuation from one
active SCD component at each endpoint of the safe-open J6 path.  Such
continuations can fill the six original short fragments, but none is a
residence-transparent socket: every fill exports a fresh `(3,2,1)` bundle.

## Setup

The safe-open owner path is

```text
30781 28797 20733 4605 511 959 1855 3647 7742 15422 30782.
```

At its left endpoint the short coordinates require respectively three, two,
and one further occurrences; the right endpoint has the reversed analogous
requirements.  The enumerator considers every owner Johnson-adjacent to either
endpoint and every outward oriented contiguous range in that owner's active
SCD component.  A retained range must have

* distinct owners;
* distinct local lower-q1 and upper-q1 colours;
* no wholly internal positive run shorter than four.

For each range the audit separately records whether the original J6 fragments
reach length four and whether the new outer endpoint has any short fragment.

## Exact census

```text
base components                         4862
base internal edges                    19448
Johnson-near owners, left/right        70 / 70
oriented ranges tested                 711 / 679
residence-only continuations           266 / 243
q1-clean continuations                 213 / 188
original-debt-filling continuations     77 / 61
minimum filling rail length              3 / 3
compatible filling pairs                    4484
saturated continuations                  0 / 0
saturated pairs                              0
```

Every minimum filling rail uses three external owners.  It fills J6's old
ages while creating three new private labels whose endpoint ages are exactly

```text
3,2,1.
```

For example, the first left rail exports `10:3,15:1,16:2`; paired right rails
export a permutation of the same triangular ages.  Searching longer ranges all
the way to the available component boundaries produces no saturated option.

## Consequence

J6 is not an ordinary transparent internal macro in the one-native-component
continuation class.  It may be used only with

1. a recursively routed endpoint clock state;
2. a genuinely richer multi-component absorber; or
3. termination at the global boundary.

The 4,484 exact pair rows are immediately usable by a selector.  Each row
contains both seam colours, both exported signatures, the required outer cuts,
and the internal cuts that must remain absent.  They are not saturated macros;
adding one as a terminal socket without another continuation is unsound.

At the age-composition quotient level the transported bundle is the self-loop
tail `(1,1,1)`, hence type `(6,1,1,1)` in `C_(9,3)`.  This explains why scalar
or fractional type debt does not grow while literal socket debt persists.

## Scope

The census is exhaustive for one oriented contiguous active-SCD range on each
side.  It does not exclude continuations that themselves use additional
non-native seams, macro exchanges, or a global reroot.  Global killed-palette
coverage, topology, deeper upper decks and the common-cap compiler remain
separate.

## Artifacts

```text
scratch/enumerate_k17_j6_resident_external_continuations_20260801.cpp
61d520fddfb8796f09613567d3a4c066b37b84666ed99b8a8b0765acf992b225

scratch/k17_j6_external_continuations_20260801.tsv
01eaa61a27ea726b7f63a8a95229fa27a81de5801b9e3fa09b3224982304fdf8

scratch/k17_j6_external_continuation_pairs_20260801.tsv
d2cd0d0b2af834bd607a6f57ac43f2e5fe21a3ef5a20209d6564f652e16a9498

scratch/k17_j6_external_continuations_20260801.audit.json
2130522e0c56b353cc1e96c49136367c7a561d4bb1aa348e564647f87690d802
```

The production enumeration ran on one H100 CPU.  No GPU was used.
