# Reported full-cube 25,374-letter construction: literal artifact verified

Received from the user on 2026-09-08. Update: the actual literal word was
subsequently supplied at Downloads/k17_upper25374.word and independently
verified on h100. All131071 nonempty targets and their ordinary interval
witnesses passed. See the root record `K17_UPPER25374_VERIFIED_20260908.md`.
The two middle matchings, recoloring, Hall certificate, repair word and
deletion indices still have not been supplied. This original filename
is retained to preserve the submission's provenance.

The reported improvement is

    24313 <= nu(17) <= 25374,
    25745-25374=371 saved positions,
    25374-24313=1061 remaining gap.

The literal upper bound25374 is now independently verified. The matching
and optimization history below remains user-reported; the supplied word's
validity does not depend on reconstructing that history.

## Reported construction and complete accounting

The user's two matchings in the seventeen-coordinate rotation quotient
have1430 vertices at each of ranks8 and9. They allegedly develop to19
genuine cycles on all24310 positions, with every target at both ranks
appearing once. Their residence guard prevents a newly inserted lower
coordinate from being deleted on either of the next two transitions.
Fourfold backward intersections of upper owners give six-letter source
sets with adjacent pair rank7, triple owners at rank8 and four-window
owners at rank9.

Independent-position matching recolors those actual letters while
preserving every neighboring pair OR. The reported lower coverage is
1261 of1281 rotation orbits, or21437 of21777 targets below rank7.
The remaining340 lower holes consist of255 five-sets and85 six-sets.
A claimed153-to134 orbit Hall obstruction would force at least323 lower
holes for this fixed envelope, irrespective of recoloring.

Before opening, the19 recolored cycles reportedly cover130068 targets.
Their1003 holes by rank are

| Rank | 5 | 6 | 7 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|
| Missing | 255 | 85 | 272 | 289 | 85 | 17 |

Opening each with10 added letters gives24500 letters. New cross-component
intervals allegedly cover16 holes, leaving987. A facet-tree repair covers
those with970 letters; subsequent exact tests remove96 positions. Thus

    24310+190+970-96=25374.

All of these dataset-dependent counts await the actual certificate.

## What can be audited without the word

The independent-position recoloring theorem is valid. Given a fixed
envelope E and current letters A with the same adjacent pair unions,
the exact permissible new letter at an independent position i is

    nonempty S, E_i\(A_(i-1) intersection A_(i+1)) subset S subset E_i.

Independent positions remove interactions between changed letters.
All ordinary intervals of length at least two are unions of their
neighboring pair unions, so they remain unchanged. Matching target
vertices to permissible positions gives the exact optimum within this
one independent-position update. An augmenting-path extension of the
existing target matching retains every previously represented target
in the desired family F. To assert retention of all old one-letter-only
targets, F must include those targets, as it does when F is the entire
lower family in this application.

The middle erosion argument additionally requires nontrivial alternating
components: the two perfect incidence matchings must not share an edge.
A shared edge would yield a one-lower/one-upper component where the
insertion guard is vacuous and the claimed six-set erosion fails.
For nontrivial components, distinct upper owners imply
U_(i-1) intersection U_i=L_i, which excludes one-step lower zero runs;
the stated insertion guard then provides the required positive-run
lengths. This condition is straightforward to check in the certificate.

These symbolic statements do not prove that the reported matchings or
letter assignment exist. Conversely, once a literal25374 word is supplied,
its full coverage alone proves the advertised finite upper bound,
independently of the construction algorithm or the asymptotic manuscript.

## Prepared independent verification

`verify_reported_k17_upper25374_20260908.py` accepts the literal decimal
mask word and an output directory. It checks exactly25374 nonzero masks
on17 coordinates, enumerates suffix ORs at every endpoint, and then
independently checks every saved witness by a segment-tree range OR.
It records a SHA-256 hash, rank census and all target witnesses.

The checker subsequently ran on the supplied word on h100 with90 CPU
seconds,110 wall seconds and1 GiB address space. It certified zero missing
targets. The canonical retained copy is `scripts/verify_k17_upper25374.py`,
with the report and all witnesses in `witnesses/k17_upper25374/`.
