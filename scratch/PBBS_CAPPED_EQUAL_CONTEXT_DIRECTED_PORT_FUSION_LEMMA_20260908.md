# A capped equal-context directed-port fusion lemma

2026-09-08. Pure-proof note by `exact_b_induction`, developing and
auditing the directed-port criterion proposed by root. No mathematical
computation was run for this note. It gives a concrete conditional
zero-extra fusion of H=3 components, preserving the complete rank-eight
and rank-nine palettes. Actual port occurrence and all-rank coverage
after the fusion are separate questions.

The inherited sources, read for this task, are
`PBBS_HEIGHT_ADAPTIVE_COLLAR_OVERLAP_AND_COMMON_CONTEXT_GRAFT_OBSTRUCTIONS_20260908.md`,
`PBBS_CAPPED_APERTURE_EXACT_MIDDLE_AND_LOWER_PIN_INTERFACE_20260908.md`,
and `PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md`.
The old native-context obstruction explicitly applied before changing
the port letters. The present lemma explains how capping can change it.

## 1. A single directly testable native port

Use H=3 source letters

    D_i = X_i intersect X_(i+1) intersect X_(i+2) intersect X_(i+3),

where X_i is the rank-nine owner. Every native letter has rank six,
pair rank seven, triple rank eight, and four-letter window rank nine.
Every native rank-eight triple label and every rank-nine owner label
is globally unique in its corresponding complete canonical layer
inventory.

Take a coordinate a such that

    a in D_i intersect D_(i+1),
    a not in Pin_i union Pin_(i+1).                       (1.1)

Change only these two letters to

    E=D_i minus {a},   F=D_(i+1) minus {a},   K=E union F.

Then |E|=|F|=5 and |K|=6. Each cap retains its pins. With all neighboring
letters full, every native triple is preserved by the exact length-two
pin criterion. Hence a is supplied by the left neighbor D_(i-1) and
by the right neighbor D_(i+2); the central triple on either side would
otherwise lose it. All longer original windows are preserved as well.

Define the unchanged flank triples

    P=D_(i-1) union E union F,
    Q=E union F union D_(i+2).

There are unique coordinates u,v outside K union {a} such that

    P=K union {a,u},   Q=K union {a,v}.                   (1.2)

They are distinct: their union is the original rank-nine seam owner

    T=P union Q=K union {a,u,v}=X_(i+2).                 (1.3)

Thus a port is specified exactly by its source component and index i,
removed coordinate a, ordered literal pair (E,F), and outer coordinates
u,v. The direction (left versus right) in (1.2) must be retained.

## 2. The directed-cycle criterion

Group candidate ports by the IDENTICAL ordered triple (E,F,u). In one
such group record a directed edge a -> v for each port. Suppose the
group contains a directed cycle

    a_0 -> a_1 -> ... -> a_(ell-1) -> a_0,

whose ell ports lie in ell distinct native components. At port j the
unchanged flank and seam labels are therefore

    P_j=K union {a_j,u},
    Q_j=K union {a_j,a_(j+1)},
    T_j=K union {a_j,a_(j+1),u}.                         (2.1)

All indices j in this section are modulo ell. First perform the two
caps from Section1 at each port. These edits occur in different
components and therefore preserve every old triple and longer window
independently.

Next cut each component immediately after its occurrence of F. Attach
the right tail of port j-1 after F at port j. This replaces the successor
edge of that F occurrence, retaining every letter occurrence exactly
once and adding no letters.

There is one cut in each of ell distinct cycles. Since the routing
permutation j -> j-1 is one ell-cycle, the resulting directed word is
one cyclic component containing the sum of their original periods.

## 3. Exact window transport and owner indices

Write a port neighborhood before the reconnection as

    ... L_j, E, F | R_j, B_j, C_j, ...,

where L_j=D_(i_j-1), R_j=D_(i_j+2), and E,F are the two common capped
letters. After reconnection the neighborhood is

    ... L_j, E, F | R_(j-1), B_(j-1), C_(j-1), ... .

For window lengths one through three, every window crossing a cut
equals an old window at the destination port: the required suffix of
length at most two is literally identical. Windows not crossing a cut
remain unchanged. Because the tails are permuted, this preserves the
ENTIRE multiset of such windows, including repeated labels.

For windows of length four, all crossing windows except

    L_j, E, F, R_(j-1)

likewise agree with an old destination window. The exceptional window
has OR

    P_j union Q_(j-1)
      = K union {a_j,u,a_(j-1)}
      = T_(j-1).                                         (3.1)

The exceptional owners are therefore permuted, not lost or duplicated.
Before the operation, T_j is X_(i_j+2), the four-letter owner ending at
R_j. Afterward, the exceptional window entering R_(j-1) still has that
destination's owner T_(j-1). The next four-letter window entering
B_(j-1) is the identical old destination window because its first two
letters are E,F. This supplies the precise source-index accounting.

Consequently every width-at-most-four source-window OR has the same
multiset before and after reconnection, measured relative to the
already capped bank. In particular:

* all old rank-eight native triple labels remain, once each;
* all old rank-nine owner labels remain, once each;
* all short lower targets of the capped bank remain;
* the number of source positions is unchanged.

No rank-nine label is hiding at another width: shorter windows have
rank at most eight, and every five-letter window contains two distinct
consecutive rank-nine owners, so has rank at least ten. The seam owners
are distinct because they are a permutation of the globally unique
original owners.

## 4. Why the native no-graft proof no longer applies

For unchanged H=3 source letters, a shared two-letter context has OR
of rank seven. Its two rank-eight flank labels are formed by adjoining
one coordinate on each side. Global injectivity of the rank-eight
labels then forces the two arm banks to be disjoint, and preserving
the rank-nine owner set forces the identity routing. That is the old
proved obstruction.

Here the common context union K has rank six. Each flank label adds
TWO coordinates. On four outside coordinates u,a,b,c, the pattern

    left tags:   {u,a}, {u,b}, {u,c},
    right tags:  {a,b}, {b,c}, {c,a}

has six distinct rank-eight labels after adjoining K. The three old
rank-nine owners have tags {u,a,b}, {u,b,c}, {u,c,a}. Rotating the
right tails as in Section2 preserves exactly those three owners.
Thus global uniqueness of the rank-eight and rank-nine labels alone
does not extend the native no-graft conclusion to capped contexts.

There is also no hidden incompatibility with being a cap of a local
native six/seven/eight/nine rank pattern. To display one symbolic
instance, let K have six coordinates, choose distinct p,q in K, and
put E=K minus {p}, F=K minus {q}. Choose x in E and y in F. For a
directed edge a -> b use original central letters

    D=E union {a},   D'=F union {a},

and full outer letters

    L=(E minus {x}) union {a,u},
    R=(F minus {y}) union {a,b}.

All four letters have size six; consecutive central-neighbor pairs
have rank seven; the two relevant triples are K union {a,u} and
K union {a,b}; the central four-window is K union {a,b,u}. Removing a
from D,D' preserves both triples because L,R still supply it. Source
entry/exit pins at D,D' are among x,q and p,y, respectively, so a is
not forced at either center position. This is a local consistency
check, not an assertion that the canonical PBBS bank contains these
particular symbolic flanks. Section1's actual-source test is what
establishes a usable port.

## 5. Constraints that simplify a deterministic port census

Within a fixed (E,F,u) group, two ports cannot have the same tail a:
their left triples would both equal K union {a,u}, contradicting the
global rank-eight uniqueness. Thus the directed graph has outdegree
at most one. It has no loop because u and v in (1.2) are distinct from
a, and no directed two-cycle: edges a -> b and b -> a would give the
same right triple K union {a,b} at distinct ports. A directed cycle
therefore has length at least three, as required by the clean-C6
example. The component-distinctness test remains essential for the
one-step fusion conclusion.

These observations prescribe a finite algebraic census, not a random
rewiring search: enumerate each actual adjacent pair and shared
unpinned coordinate, calculate its exact key and edge, then inspect
the resulting functional directed groups for cycles with distinct
component labels. This note itself runs no such census.

## 6. The exact remaining coverage and chronology boundaries

The preliminary caps can delete the original rank-six center letters
E union {a}, F union {a}, and the rank-seven center pair K union {a}.
They do not automatically preserve those named lower targets elsewhere.
The later common-context reconnection preserves all width-at-most-four
labels of the capped bank, so it causes no additional short-window
losses relative to that bank. These are two different comparison steps.

All upper targets survive the preliminary caps, since all original
triples and longer windows remain. **All upper targets are not yet
proved to survive the reconnection.** A target whose necessary witness
has length at least five can cross a changed seam with more than the
common two-letter context on its left. Its old label needs an exact
transport or outside-provider proof; preservation of the rank-nine
owner palette alone does not imply it.

Indeed a common three-letter context at distinct H=3 ports is impossible
under triple preservation, since its OR would repeat a globally unique
rank-eight label. The missing longer-window transport cannot simply be
assumed from a longer identical context.

Finally, a cyclic fusion is not a free linear opening. This conditional
lemma reduces a chosen ell-component group to one cycle at the same
number of positions; it does not solve every remaining component,
recover the preliminary lower losses, or justify a complete universal
linear word of length24,313. Those obligations remain explicit.
