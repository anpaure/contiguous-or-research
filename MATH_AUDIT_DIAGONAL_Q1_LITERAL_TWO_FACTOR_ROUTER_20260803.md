# Independent audit: diagonal q1 literal two-factor router

**Date:** 2026-08-03  
**Audited theorem:** `MATH_THEOREM_DIAGONAL_Q1_LITERAL_TWO_FACTOR_ROUTER_20260803.md`  
**Audited theorem SHA256:** `34021deb43b579d2ad68a2aac071705a867d90278b74031f092e3da32a43945b`  
**Verdict:** **PASS**, with the theorem's stated fixed-row, explicit-resource-ledger, and terminal-socket scope retained. No theorem edit was made.

## 1. Cyclic identities and q1 scope

For indices in `Z_W`,

\[
P_i=\bigcup_{h=i+1}^{i+d}A_h,
\quad
P_i\cup A_i=T_i,
\quad
P_i\cup A_{i+d+1}=T_{i+1}.
\]

The wrap edge uses exactly the same identities, so there is no endpoint exception. The incidence graph has edges `p_i o_i` and `p_i o_(i+1)`; hence `o_i` has neighbours `p_i,p_(i-1)` and the addressed graph is the single alternating cycle claimed in (1.5).

The q1 hypothesis is genuinely necessary for the **Middle-Levels factor** conclusion. Flat rank-`r` owners alone give the two literal union identities, but do not force the addressed length-`d` cell to have rank `r-1`. Under the stated full enumerations, the two shore sizes agree, and

\[
{k\choose r}={k\choose r-1}
\iff k=2r-1.
\]

Thus the spanning-factor and central-layer statements have the correct scope.

## 2. Occurrence aliases and the `d=1` exclusion

At `d=1`, `p_i=[i+1,i+1]` is the same physical interval cell as the source occurrence `a_(i+1)`. This is not merely a cosmetic alias: in the minus phase, for example, `R_i^-` uses `p_i=a_(i+1)` while `R_(i+1)^-` uses that same occurrence as its boundary letter. Hence the asserted phasewise disjointness fails if the two names are split into independent capacities. The theorem correctly excludes this case from its packing claims.

For `2<=d<W`, a length-`d` addressed port cell cannot equal a length-one addressed boundary cell. Equal set values at different addresses remain distinct occurrence resources, as explicitly stipulated. Any additional alias involving a socket, guard, or hidden transport resource is not silently ignored: Section 4 conditions 1, 3, and 5 require it to be coalesced or included in the capacity ledger.

## 3. Full phases and the multiplicity-two ledger

The minus phase uses

\[
(p_i,a_i,\tau_i),
\]

and the plus phase uses

\[
(p_i,a_{i+d+1},\tau_{i+1}).
\]

Each coordinate map is injective in `i`; translations on `Z_W` are bijections regardless of any gcd. Thus each phase is a full pairwise-disjoint linkage in the displayed ledger.

In the union of both phases the exact incidences are:

* `p_i`: `R_i^-`, `R_i^+`;
* `a_h`: `R_h^-`, `R_(h-d-1)^+`;
* `tau_h`: `R_h^-`, `R_(h-1)^+`.

Therefore every priced resource has raw multiplicity two and uniform weight `1/2` has load one. If the native owner occurrence `o_h` is itself represented as a unit-capacity vertex before its private socket attachment, it likewise lies on `R_h^-` and `R_(h-1)^+`, so including it does not change the conclusion. The warning about cross-route switching at a shared source is correct: the fractional union is an overload certificate, while either complete phase is the literal identity-safe integral linkage.

## 4. Typed terminal sockets and the reserved-owner face

An injection from the `W` addressed owners to compatible unused unit sockets, with private attachments in one common state, is sufficient exactly as claimed: substitute those sockets into either full phase. The terminal-cut lower bound proves necessity of **`W` units of terminal capacity** on the stated unit-sink face. It does not prove a globally necessary one-socket-per-owner placement when remote supplier types or interchangeable socket banks are admitted; the theorem already limits the sharpness statement to the co-located/native interface and separately allows a compatible terminal matching.

The reserved-owner counterface is correct and properly one-way. If the admitted routes are only the two native diagonal extensions and every native owner capacity is deleted, no port has even a singleton path to a terminal, so the suffix rank is zero. This says nothing about remote duplicate owners, alternating recourse, or other supplier types, all of which the theorem explicitly excludes from that proposition.

## 5. Linear-block variant

For a linear block with `n` owners and `n-1` q1 port occurrences, the minus phase reaches `T_0,...,T_(n-2)` and leaves `T_(n-1)` unused; the plus phase reaches `T_1,...,T_(n-1)` and leaves `T_0` unused. Hence a family of `b` occurrence-disjoint diagonal blocks has exactly `b` more owner sockets than ports. Global phasewise boundary-letter injectivity follows from the same index translations when the blocks retain their original source addresses.

This is only a cardinality/interface statement. It neither supplies q1-exactness on architecture-free blocks nor reduces an `O(d)` block count to `O(1)`, and the theorem states both limitations.

## 6. Final scope judgment

The theorem validly proves a literal `h=2` suffix router from:

\[
\text{one cyclic flat q1-exact literal diagonal row}
+
\text{one compatible unused unit socket per addressed owner}.
\]

It does not prove existence of that row, availability of the sockets after compensation, cross-coordinate product closure, or the all-`k` upper bound. No hidden inference of any of those statements was found.
