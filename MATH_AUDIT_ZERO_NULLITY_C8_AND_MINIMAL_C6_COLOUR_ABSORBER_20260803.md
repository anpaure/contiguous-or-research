# Audit: zero-nullity C8 actuator and minimal C6 colour absorber

**Date:** 2026-08-03  
**Scope:** pure mathematics only.  No finite search, solver result, or
dimension-specific computation is used.

## 0. Binding and verdict

The requested source
`MATH_THEOREM_ZERO_NULLITY_C8_AND_MINIMAL_C6_COLOUR_ABSORBER_20260803.md`
was initially supplied at SHA-256

```text
05ed49b1ef2060589a11b444592aa9896d4ccb914752128efb4b0166283367fc
```

That version had one exact formal omission: Theorem 4.1 called `A_i` a
predecessor owner but did not state the incidence `L_i subseteq A_i`, which
its proof uses.  Rank-`(m+1)` of the two unions alone does not imply that
containment.  The statement was corrected by adding only `A_i` containing
`L_i`.

The final audited source has SHA-256

```text
a8802baa998f535461de5e5628785cd266ddc8db1d277c860eab333c9c4eb7fd
```

**Verdict: GO.**  Three independent proof reads of this exact digest found
no remaining mathematical correction.

## 1. Protected C8 actuator and its sharp scope

All sets in (1.1) have the stated ranks, and every consecutive pair in
(1.2) is incident.  Missing-`z_i` data separates punctured objects across
cycles, while the petal/exterior data separates all remaining objects.
Thus the four `C8` components are simple and vertex-disjoint.

The turn colours are exactly `B_i,X_i,Y_i,Z_i`.  Each `Y_i` is distinguished
by its missing `z_i`; the full-`S` families are separated by their `e,f`
pattern and by the singleton or cyclic petal pair.  Hence all sixteen
protected colours are distinct.

Replacing `C_iT_i` by `C_iT_(i-1)` opens the four old cycles and reconnects
their paths by one 4-cycle.  It preserves both matching shores and all
degrees.  At `C_i` the colour changes from `B_i` to `B_(i-1)`, so the full
colour multiplicity vector is merely permuted.  The successor permutation
is multiplied by a 4-cycle and component parity flips.

Proposition 1.3 is sharply and correctly scoped to the saturated
**off-phase** host.  A saturated protected component cannot be a `C4` in
the middle-levels incidence graph.  A simple `C6` is the top Boolean
triangle, so its three lower turns have one common colour and repeat excess
two.  Zero nullity therefore forces each of the four private components to
have length at least eight.  The construction attains

\[
                              4\cdot8=32.
\]

The four new cross incidences are distinct from those 32 incidences, so the
two-phase union has 36 incidences.  No sharpness claim is made for that
union.

## 2. C6 classification and exact prospective count

Simplicity excludes the star type of a Johnson triangle, leaving the three
facets `B_i=R-b_i` of one rank-`(m+1)` top.  Upper validity forces the extra
predecessor labels `e_i` outside `R`.  Consequently

\[
 O_i=(R-b_i)+e_i,\qquad N_i=(R-b_{i-1})+e_i.
\]

Equality `O_i=N_j` holds exactly when `j=i+1` and `e_i=e_(i+1)`.  A cyclic
three-letter word has zero, one, or three equal adjacencies, never two.
This proves the palette trichotomy and the impossibility of a one-for-one
simple `C6` repair.  The choice `e_0=e_1\ne e_2` gives the stated four-corner
Boolean rectangle; reserve occurrences preserve both displaced old-only
colours, while every previously missing new-only colour is genuinely added.

For Proposition 3.2, a designated target
`Y=(R-b_2)+e` determines a labelled tuple by the reversible choices

\[
 \underbrace{m+1}_{e\in Y}
 \underbrace{(m-2)}_{b_2\notin Y}
 \underbrace{m(m-1)}_{(b_1,b_0)\text{ ordered in }Y-e}
 \underbrace{(m-3)}_{f\notin R,\ f\ne e}.
\]

Here `R=(Y-e)+b_2` is forced.  Thus the exact raw prospective count is

\[
                  (m+1)(m-2)m(m-1)(m-3).
\]

This is a labelled prospective count only; it does not assert joint
placement with the predecessor, reserves, or global topology.

## 3. Coordinate-current conservation

With the corrected hypothesis `L_i subseteq A_i`, write

\[
 B_i=L_i+p_i,\qquad B_{i-1}=L_i+q_i.
\]

Upper validity makes the extra point of `A_i` different from `p_i,q_i`, so

\[
             1_{N_i}-1_{O_i}=1_{q_i}-1_{p_i}.
\]

On the closed Johnson walk, every coordinate departs as often as it
arrives.  Summation proves Theorem 4.1 coordinatewise.

For Theorem 4.2, fix a coordinate and put

\[
 A={2m-2\choose m-1},\qquad B={2m-2\choose m-2}.
\]

Exactly `B` lower vertices already contain the coordinate.  For either
perfect matching it is the added label at exactly `A-B` further lower
vertices.  Edge-disjointness prevents the two matchings from adding the
same label at one lower vertex.  Hence its turn replication is exactly

\[
                         B+2(A-B)=2A-B.
\]

## 4. Duplicate design and rooted puncture

After subtracting one copy of every upper colour, the duplicate block count
is

\[
 {2m-1\choose m-1}-{2m-1\choose m+1}
 =\operatorname{Cat}_m.
\]

Every coordinate occurs in
`{2m-2 choose m}={2m-2 choose m-2}=B` members of the complete upper layer.
Subtracting this from the turn replication gives

\[
 (2A-B)-B=2(A-B)=2\operatorname{Cat}_{m-1}.
\]

Thus the Catalan duplicate multiset is a genuine block-multiset
1-design.  Deleting the rooted turn `U_o` removes exactly that one block.
If `U_o` has another occurrence, upper-surjectivity survives, and the
duplicate multiset has `Cat_m-1` blocks with coordinate replication

\[
       2\operatorname{Cat}_{m-1}-1_{\{x\in U_o\}}.
\]

Corollary 4.4 is therefore the exact puncture of Corollary 4.3.

## 5. Parity and global scope

A `C_(2s)` successor toggle multiplies the successor permutation by an
`s`-cycle.  Its sign is `(-1)^(s-1)`, so component-count parity changes by
`s-1 mod 2`.  Accordingly the `C6` absorber is topology-even and the `C8`
actuator is topology-odd.  The C8 multiplicity vector is unchanged, so it
cannot itself repair missing colour support.

All conclusions are local/prospective.  The theorem does not claim that
the C6 predecessor, reserve occurrences, C8 socket, and required component
placement coexist in one globally upper-exact resident carrier; that
correlated planting statement remains explicitly open.
