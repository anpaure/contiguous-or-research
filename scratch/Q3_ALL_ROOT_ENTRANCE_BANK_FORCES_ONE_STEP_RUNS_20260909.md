# Retaining every root entrance forces a one-state positive run

Date: 2026-09-09. Status: pure-proof obstruction to extending the specified
entrance bank. No mathematical execution or search.

For every r>=1, no strict child canonical-Phi cycle cover with all positive
lower-coordinate runs of length at least2 can retain ALL prescribed
fixed-root first entrance edges. At least Cat_(r-1) of its Cat_r entrance
incidences must change. This conclusion needs neither the later Hall
facets nor the whole01 strip, and does not rule out other Phi factors.

## 1. Precise setup and matching convention

There are 2r+1 old positions, followed by new positions a,b. Write u for
the first old position, x for the second and y for the third. A child
lower state has rank r+1 and a child upper state rank r+2. Canonical Phi
adds the zero at the first global minimum of the ones-minus-zeros prefix
walk. A strict successor is an upper facet OTHER THAN its own outgoing
Phi preimage; returning along the same matching edge to the same lower
state is excluded.

Let I be all old root states L=0D' where D' is Dyck of semilength r.
The prescribed first entrance is

    L+a -> Phi_old(L)=1D'  (child00).                   (1.1)

It uses the child upper Phi_old(L)+a and occupies the incoming socket of
the lower00 state 1D'. The head bank

    H={1D':D' Dyck of semilength r}

is exactly the old rank-(r+1) words whose EVERY nonempty prefix has
strictly positive height. Its cardinality is Cat_r. Suppose (1.1) is
retained at all these heads.

The inverse matching rule used below is standard and proved in the
[sector law, Section2](COMPLETE_CANONICAL_PHI_SECTOR_LAW_AND_EXPLICIT_01_STRIP_EXTENSION_20260909.md):
in a child upper word, delete the up-step immediately after its LAST
global minimum, including the empty prefix. Flipping a first-minimum
zero in a lower word raises that minimum by one and makes its last
attainment the position immediately before the flipped bit.

## 2. A family of forced upper00 sockets

For every Dyck word D of semilength r-1, consider the old masks

    Z=111D,       U=011D,       V=101D,                 (2.1)

all followed by00 in the child. Z has old rank r+2. U has old rank r+1
and minimum -1 first attained at u, so child Phi(U00)=Z00.

Enumerate EVERY facet of Z00:

- Deleting u gives U00, its forbidden self successor.
- Deleting x gives V00. Its old walk has heights1,0,1 and then at least1.
  Thus V is nonnegative, but not strictly positive, so V is not in H.
- Deleting y gives 110D. Every nonempty old prefix has height at least1,
  so this head is in H and its incoming socket is occupied by (1.1).
- Deleting any one belonging to D likewise leaves all old prefixes at
  least1: before that deletion Z is positive, and after it the height is
  1 plus a Dyck prefix height. These heads also belong to H.

There are no facets involving new letters because Z00 contains neither
a nor b. Hence V00 is the ONLY permitted successor of Z00 if all first
entrances are retained. The forced lower transition is

    U00 -> V00: insert u, delete x.                    (2.2)

## 3. Every legitimate arrival at U inserts x freshly

Every upper containing U00 is U00+z for one coordinate z outside U00.
These coordinates are exactly u, the zero positions of D, a and b.

If z=u, this is Z00. Its complete child walk has strictly positive
nonempty prefixes: old heights1,2,3 followed by at least3, then2,1 at
the new zeros. The inverse matching therefore deletes its first up-step
u and gives U00 itself. Using this incoming edge would be the excluded
self successor.

For EVERY other z, the complete upper walk has minimum -1 LAST attained
at old position u. Indeed it begins with old heights -1,0,1. Adding a
zero of D only raises a later suffix, leaving subsequent old heights at
least1; its appended00 then has heights2,1. Adding a gives appended
heights2,1, and adding b gives appended heights0,1. None revisits -1.

The inverse matching therefore deletes the next up-step, which is x.
The unique outgoing source of this upper is

    (U00+z)-x.

It omits x, so arriving at U00 inserts x. Thus in ANY strict full factor,
regardless of which permissible incoming upper is used, x has age exactly1
at U00. The forced next edge (2.2) deletes x immediately and closes a
positive lower run of length1.

This contradicts residence at least2. No information about incoming age
choices, parent chronology, later excursion steps or topology is needed.
For r=1 the word D is empty and the same enumeration still includes all
facets and incoming uppers, so the boundary case is valid.

## 4. Quantitative number of first incidences that must change

There are Cat_(r-1) distinct upper00 words Z=111D. In any strict canonical-
Phi factor of residence at least2, each must choose a successor in

    H_Z={Z-t:t is a one of Z other than u,x}.           (4.1)

Its self facet is forbidden, and V always deletes the freshly inserted
x. Every member of H_Z belongs to H, as shown in Section2. A selected
head in H_Z cannot still receive the prescribed first-entrance edge
(1.1), since incoming matching degree is one.

Moreover the selected heads for different Z must be DISTINCT. Therefore
at least Cat_(r-1) different prescribed first-entrance incidences must be
omitted, replaced or reopened. The exact fraction is

    Cat_(r-1)/Cat_r = (r+1)/(2(2r-1)) -> 1/4.          (4.2)

This is stronger than a degree-cover bound that divides by the number of
possible containing Z: matching injectivity already forces distinct heads.
The available incidence choices in (4.1) have an explicit injection
D -> 110D. Thus this particular head family has no individual containment
or distinct-head obstruction if those heads are freed. This does NOT
establish compatible residence-three histories, a residual perfect
matching, or a global factor after they are freed.

## 5. Consequence for the current induction route

The previously proved five-step paths are still pairwise disjoint and
locally residence-three valid. This theorem does not contradict that
finite path statement. It proves they cannot ALL be installed wholesale
in a spanning canonical-Phi factor with residence at least2 while their
first entrances are retained. The failure appears before the Hall facet
choices, their internal11 closures, and the enlarged whole01 cover matter.

For the actual19 parent used as input to the proposed21 induction, the
necessary number of changed first incidences is Cat_8, out of Cat_9.
This is a symbolic application, not a new numerical census. Selective
port replacement or reopening is required; merely filling unused sectors
while keeping every root entrance fixed cannot work.

No impossibility is claimed for canonical-Phi factors in general, for
other port families, for optimal21 words, or for the all-dimensional
equality objective. No new matching or literal word has been constructed.

## 6. Attribution and audit status

Root proposed the family Z=111D and its forced residual head. The induction
agent established the universal fresh-arrival obstruction; root checked it
independently and strengthened the count to Cat_(r-1) distinct changed
heads. The proof reuses the first/last-minimum inverse already established
in the sector notes. Independent structure review was requested before
adding retrospective links to earlier proofs. No execution occurred.

The structure agent subsequently read this complete note and passed all
cases and the quantitative count. Its complete independent proof is
[recorded here](ALL_ROOT_FIRST_ENTRANCE_BANK_RESIDENCE_OBSTRUCTION_INDEPENDENT_AUDIT_20260909.md).
The root's independent review also passed. These are internal mathematical
reviews, not external formal certification.
