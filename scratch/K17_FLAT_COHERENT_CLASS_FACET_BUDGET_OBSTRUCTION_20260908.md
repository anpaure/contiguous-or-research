# Coherent flat port classes force repeated facets

Date: 2026-09-08. Pure proof; no mathematical computation.

Status: proved necessary condition for specified flat four-window ports and the one-pivot k17 schedule. This is not an obstruction to unrestricted OR words, arbitrary schedules, or sparse transition graphs.

## 1. The set-theoretic biclique lemma

Let A_1,...,A_q be sets of size eight, and let R_1,...,R_q be distinct sets of size nine, with q>=2. Suppose letters X_j satisfy

    A_i union X_j = R_j for every i,j.

Then every A_i is contained in the intersection of all R_j. Two distinct nine-sets intersect in at most eight elements. Since the intersection contains an eight-set, it has exactly eight elements, and

    A_1=...=A_q=intersection_j R_j=:A.

Every destination is therefore A plus one coordinate. The lemma only uses necessary union equations; it does not assume that they are sufficient for a literal recency transition.

The same proof works in any rank m, replacing eight and nine by m-1 and m.

## 2. Which owner facet is the source's last-three union?

At a flat four-window source endpoint let the last four literal letters be E_0,E_1,E_2,E_3, with current rank-nine owner

    T=E_0 union E_1 union E_2 union E_3.

Its last-three union is A=E_1 union E_2 union E_3. Appending X gives the next owner R=A union X. If |A|=8, |T|=|R|=9 and T!=R, then A is contained in T intersect R and that intersection has size at most eight. Hence

    T intersect R=A.

This is the OUTGOING facet at the source owner. Its incoming facet uses the preceding triple E_0,E_1,E_2, when that triple has rank eight. Confusing those two triples would miscount the effect of a cut.

In an actual chronology with distinct selected middle owners, T=R cannot occur. Thus each retained flat graft transition satisfying these hypotheses creates one actual rank-eight owner-adjacency occurrence, not merely an abstract candidate label.

## 3. The one-pivot repetition budget

Use the established k17 schedule with W=24,310 owners:

    I_i=[i,i+2] for i<L,
    I_i=[i,i+3] for i>=L,

where the word ends at its final deadline and there is one interior depth increase. The active construction has L=306. Let b count non-Johnson selected owner adjacencies and let e count repeated rank-eight color occurrences among the Johnson adjacencies.

There are W-1 adjacencies, so their rank-eight palette has W-1-b-e distinct colors and misses 1+b+e of the W rank-eight targets. The proved exceptional-facet theorem permits at most three targets outside that palette: one nested initial-prefix family, the one pivot family, and one nested terminal-suffix family. Therefore universality requires

    b+e<=2.

This is the theorem used in `K17_PBBS_PREFIX_ONE_PIVOT_NOGO_AND_CONSECUTIVE_START_BUDGET_20260908.md`; it concerns the final linear selected chronology, not an intermediate cyclic graph.

Suppose a coherent q-source class from Section 1 is actually used at q distinct flat source occurrences in this final chronology, with all q graft transitions retained. The common facet A then occurs at least q times, so e>=q-1. Consequently

    q<=3.

This necessary bound allows redesigning the port menus: only the last-three rank-eight condition, distinct rank-nine destinations, complete cross-compatibility, and final retained transitions are used. In particular, six retained coherent ports of this type cannot occur in the one-pivot construction.

The bound can be stronger if other retained adjacencies already consume non-Johnson or repetition budget. It is only a necessary bound: q=2 or q=3 is not thereby constructible.

## 4. Temporary cycles and current-bank bookkeeping

A later opening can delete a graft transition. If only p of the q class transitions remain as distinct flat selected adjacencies in the final chronology, the argument proves p<=3, not q<=3. If at most a transitions are deleted or cease to have the required status, it proves

    q<=3+a.

Thus a temporary six-source gadget followed by one cyclic opening still cannot fit this one-pivot architecture: at least five common-facet transitions remain. A temporary four-source gadget with one deleted transition is not excluded by this counting argument alone. A reusable source anchor in a sequence of switches does not multiply the final number of its outgoing edges; the count is on the final retained transitions.

The current 1513-stage mixed prefix/cycle bank has W-1 rank-eight adjacency occurrences, exactly two missing colors and one repeated occurrence, so its repeat excess is e=1. If proposed flat ports retain their EXISTING outgoing facet values in this unchanged bank, a common-facet class has at most two source occurrences. A redesign after cutting an edge can change that outgoing facet; in that case the old e=1 count is not automatically preserved, and the final one-pivot budget must be applied instead.

## 5. Ways a construction can avoid the hypotheses

These are alternative requirements for further construction, not proved solutions:

- A source last-three union can have rank below eight. Then the set-theoretic lemma does not force equality of the source unions. Its middle-edge and lower-target costs must be checked separately.
- The selected intervals can use a different deadline geometry or avoid treating all graft edges as flat selected adjacencies. The appropriate endpoint budget must then be recomputed; the one-pivot allowance cannot simply be reused.
- Compatibility can be sparse. In particular, two distinct source facets cannot have two distinct common rank-nine destinations under the stated union equations, but a six-cycle compatibility graph with three sources and three destinations can have only one common destination per source pair. Such a graph is not a coherent complete class and is not ruled out here.
- Some temporary class transitions can be removed or altered before the final chronology, subject to the retained-transition count above and all resulting coverage and length obligations.

Repeated rank-nine destinations are another algebraic escape, but they cannot stand for distinct selected owners in an attaining chronology. They must be accounted for as repeated or unselected occurrences rather than silently counted as separate middle targets.

No conclusion in this note rules out general clean C6 surgery, general recency-state fusion, or nu(17)=B(17).
