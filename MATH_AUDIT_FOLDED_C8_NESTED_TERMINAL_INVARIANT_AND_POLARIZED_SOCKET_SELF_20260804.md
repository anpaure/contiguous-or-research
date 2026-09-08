# Self-audit: folded-C8 to nested-terminal invariant and polarized socket

**Date:** 2026-08-04

**Audited theorem:**
`MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md`

**Audited theorem SHA-256:**
`a6dba7ab6eab0e14e47552ab52ce00a2962969a6168f08972946720c6224fe53`

**Method:** independent symbolic replay of the Boolean-lattice identities,
state lower bound, physical occurrence count, and terminal/Rado scope.  No
computation, catalogue, or remote run was used.

## 1. Verdict

**GO as a proof-safe no-go and conditional conversion theorem.**

The source correctly separates two semantics which must not be conflated:

1. Under literal OR-target semantics, a native nested pair cannot replace
   the incomparable folded-C8 ray pair.
2. Under socket semantics, with the exact ray witnesses retained upstream,
   one polarity bit gives a reversible type code on a native nested pair.

The second statement is conditional on one accepted complete cap/background
state.  It does not make the native cells literal witnesses for the old ray
values.

## 2. Canonical diamond replay

For

\[
 X=C\cup F[1,j],
 \qquad
 Y=C\cup F[j+1,d],
 \qquad 1\le j<d,
\]

the two filler parts are nonempty and disjoint.  Therefore

\[
 X\cap Y=C,
 \qquad
 X\cup Y=C\cup F=U,
\]

and neither of `X,Y` contains the other.  The four values
`C,X,Y,U` are distinct and form the Boolean lattice `B_2`.

The native first-exit and q1/q2 pairs are chains `R<V` with one Boolean
rank step.  The canonical meet-to-join interval has rank `d>=2`.  Thus both
comparability and interval rank distinguish the two types.

## 3. Lattice no-go replay

If an injective meet-preserving map sends incomparable `X,Y` to a chain,
say `phi(X)<=phi(Y)`, then

\[
 \phi(X\cap Y)=\phi(X)\cap\phi(Y)=\phi(X).
\]

Injectivity gives `X cap Y=X`, contrary to incomparability.  Hence the
literal no-go is correct.

For a noninjective lattice map with

\[
                         \phi(X)=R< V=\phi(Y),
\]

meet and join force

\[
                         \phi(C)=R,
 \qquad \phi(U)=V.
\]

So exactly the pairs `C,X` and `Y,U` collapse.  Reversing the atom images
gives the other orientation.  This verifies the claimed one-bit loss.

A literal assignment to target `Z` requires a physical cell whose OR is
exactly `Z`.  Consequently a semantic tag cannot repair a missing literal
ray occurrence.  The additional-occurrence lower bound

\[
 2-|\{X,Y\}\cap\{R,V\}|
\]

is exact as a counting lower bound: every ray target not already equal to a
native cell value needs a distinct exact occurrence.  A nested pair can
contain at most one of the two incomparable targets, so the bound is at
least one.

## 4. Polarized-chain coding replay

The proposed code is

\[
 C\mapsto(R,0),
 \quad X\mapsto(R,1),
 \quad Y\mapsto(V,0),
 \quad U\mapsto(V,1).
\]

Under the coordinatewise product order,

\[
 (R,1)\wedge(V,0)=(R,0),
 \qquad
 (R,1)\vee(V,0)=(V,1).
\]

Thus the atom meet and join are correct, and all four covers agree.  The
map is a lattice isomorphism.

A reversible code on a two-element physical chain with state set `S` has
at most `2|S|` values.  Four diamond values require `|S|>=2`; one binary
state is therefore minimal.  If the common ticket label no longer carries
`j`, the fixed-core family has

\[
 2+2(d-1)=2d
\]

distinct values, so `|S|>=d`.  Both information bounds are correct.

The source correctly observes that the terminal Rado signature already
contains a binary occurrence-coordinate/role label.  A fixed phase
normalization may use this as the polarity coordinate, so the one-bit
repair need not add a new field.  The still-new premise is acceptance of
the product type `(native value, role polarity)` in one common cap state.

## 5. Terminal semantics and capacity replay

The deterministic polarized-socket theorem does not apply two marginal
Rado selections.  It assumes one complete conjunctive record per ticket,
including:

* both exact upstream ray occurrences;
* both native terminal occurrences;
* the polarity and ticket/cut labels;
* the common state, phase normalization, flags, guards, and background;
* every physical capacity.

Pairwise disjoint native pairs then give one simultaneous deterministic
selection.  This is proof-safe and avoids the product-closure fallacy.

The phrase "no new cell" is also scoped correctly.  It means all ray and
native occurrences already exist in the word.  The ray cells remain used
capacities; the theorem does not replace four occurrence facts with two.

For join coalescence, both roles terminate on one existing occurrence only
when they declare the same envelope fact `OR(u)=U` and the cap explicitly
permits dual-role coinstantiation.  Applying this to a native top `V`
requires exact equality `V=U`, not containment or equal rank.  This matches
the source-free dual-role theorem's semantic boundary.

## 6. Weakest-data audit

The contextual equivalence relation in the source is the mathematically
correct coarsest signature: two records may be identified precisely when
every admitted context gives the same legality, target/type assertions,
capacity conflicts, and paired relation.

No cited theorem proves that the canonical ticket can forget its exact ray
value, phase/role, occurrence address, or cap/guard state.  Meet and union
alone are insufficient because all `d-1` cuts share them.  With the ordered
filler schema and logical cut `j` retained, `(C,U,j,role)` determines the
value-level pair, but not a literal physical witness.  The source states
this distinction explicitly.

## 7. Scope boundary

The theorem does not claim:

* that the canonical and native values coincide;
* that current first-exit/q1-q2 banks accept the polarity bit;
* that both exact ray banks coexist in an owner-legal endpoint;
* that transported phase 1 is native;
* that the background avoids the native pair;
* regeneration, an all-dimensional carrier, or an OR-word upper bound.

The precise remaining construction is correctly stated: materialize one
complete polarized bundle per ticket in one cap/background state, or prove
that the actual terminal predicate factors through the union-envelope
quotient and supplies exact dual-role join occurrences.

## 8. Frozen dependency hashes

| role | file | SHA-256 |
|---|---|---|
| native diagonal diamond/dual role | `MATH_THEOREM_DIAGONAL_INTERVAL_DIAMOND_SOURCE_FREE_DUAL_ROLE_ROUTER_20260803.md` | `2e71b1f3a7c26c23accf9e3cee9a23ba01ef17658f959b73ac69c622ce2a2802` |
| first-exit nested terminal bank | `MATH_THEOREM_DIAGONAL_FIRST_EXIT_SECOND_TERMINAL_BANK_20260803.md` | `25dc0c20f14254a9f9419caa41912c5fdc480f6fb3178e20822a6e6cd8a89ab0` |
| q1/q2 native ladder | `MATH_THEOREM_DIAGONAL_Q1_Q2_TWO_COORDINATE_UPPER_LADDER_ROUTER_20260803.md` | `dbd2f671d07e1e4c09ecadbbade9e9ea0a55e1dfca4054ead15fd09fbe8a7151` |
| two-cross-ray Rado/gammoid | `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md` | `108c4b0ad2adc99d9e9c91df9f1bfdb9f816494670f7473c51e7751f134177cc` |
| folded-C8 address/halo gate | `MATH_THEOREM_THREAD_D_FOLDED_C8_ANTIDIAGONAL_ADDRESS_AND_HALO_GATE_20260801.md` | `ab8519229624c97a1cede8bacdf5b5b60add4fe47035e2a1f61f9031c5afee22` |
| folded address/transport scope audit | `MATH_AUDIT_ZERO_BLOCK_BIRAIL_CROSSMATCH_AND_ADDRESSED_TRANSPORT_SCOPE_20260801.md` | `ccc29b2ae8a5f4036d2a707a84091f0c08b669a378a441fd4e5d3f4da50d88d5` |

## 9. Final conclusion

The theorem is proof-safe.  Its main unconditional conclusion is a no-go:
raw literal target semantics cannot be converted from an incomparable pair
to a native nested pair using only those two native cells.  The minimal
semantic repair is a polarized socket carrying the logical cut label and
one bit, but it is valid only while the two exact ray witnesses remain in
the complete bundle.
