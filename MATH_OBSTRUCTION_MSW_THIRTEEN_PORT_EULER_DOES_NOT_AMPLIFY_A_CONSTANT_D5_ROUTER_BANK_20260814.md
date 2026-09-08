# Thirteen-port Euler fusion does not amplify a constant D5 router bank into Catalan upper coverage

**Date:** 2026-08-14  
**Status:** exact scale obstruction plus a conditional local-compilation
implication.  A single flat D5 atlas has a bounded-degree physical constraint
graph and needs only 226 closed three-cycle packages, conditionally on an
unproved cut-open collar compiler.  But no fixed number of such packages can
complete the canonical MSW proper-upper deck: coalesced Euler fusion reuses
histories, not owner occurrences, and the explicit Catalan hole family forces
Catalan-scale exceptional occurrences.

## 0. Outcome

There are two different scale questions.

1. **One local D5 actuator.**  Its flat algebraic word has 226 router nodes
   and 477 token strands.  The router--token incidence graph has maximum
   degree three, 25 tree blocks, and eight unicyclic `K2,2` cores.  If the
   prospective token collars exist and one protected-bank insertion theorem
   is supplied, 226 closed packages suffice for this one actuator.  They are
   not replicated once for every edge of the native Catalan arborescence.
2. **The complete asymptotic upper row.**  The canonical MSW factor misses
   `Cat_(m-6)` distinct immediate-upper targets.  Any architecture in which
   only a bounded set `S` of owner occurrences participates in
   non-common-history package/collar edits can witness at most `2|S|` of
   them.  Hence `|S|>=Cat_(m-6)/2`.  With owner-disjoint 36-owner packages,

   \[
             P_m\ \ge\
             \left\lceil\frac{\operatorname{Cat}_{m-6}}{72}\right\rceil.
                                                               \tag{0.1}
   \]

Thus the correct answer is:

> `226` is the constant package count for one fixed D5 macro, conditional on
> a physical compiler.  It is not an asymptotic upper-completion count.
> Complete upper coverage requires Catalan-scale physical instantiation
> (equivalently, a bounded template tensored over Catalan-many contexts), up
> to the constant capacity of one package.

The thirteen universal ports remove Catalan **port-degree** growth in the
native source arborescence.  They do not remove Catalan **occurrence** demand
in an upper-witness bank.

## 1. The fixed local incidence graph

For the certified flat factorization, let `R` be the 226 three-cycle routers
and let `T` be the 477 moved logical tokens.  Join a router to its three
tokens.  The audited graph has

```text
router degrees                         3:226
token degrees              1:292, 2:169, 3:16
incidences                               678
components                                33
trees / unicyclic blocks               25 / 8
unicyclic two-cores                    K2,2.
```

The proposed strand reduction groups the token vertices as

```text
461 prospective C6 collars = 292 dummy-completed leaves + 169 joints,
 16 prospective C8 collars = the degree-three tokens.
```

These are exact graph counts only.  The word “prospective” remains
load-bearing: no theorem yet constructs the prescribed-edge q1-exact C6 or
C8 collars, makes their owner/q1/q2 banks disjoint, proves their residence,
or embeds them in the native factor.  The eight `K2,2` cores are eight
finite-state closure subproblems, not eight already-solved scalar equations.

Nevertheless the graph rules out a false scale diagnosis.  A single atlas
is not a dense 226-by-477 constraint instance: its maximum incidence degree
is three.  Once a total local extension menu exists, tree propagation and
eight independent core closures are a plausible finite SDR/LLL problem.

## 2. What the thirteen-port theorem actually coalesces

The thirteen-port theorem assigns every native highest-valley arborescence
edge one of thirteen separated source starts.  Arbitrarily many incidences
at a native row may reuse one start because they request one literal common
history.  The coalesced Euler theorem then reuses a de Bruijn history vertex,
and even one incoming occurrence as a sequential successor-swap handle.

Neither operation copies an occurrence.  In the final Euler circuit:

* every occurrence-labelled source edge is traversed exactly once;
* every owner occurrence still has one predecessor and one successor; and
* a reused handle is one occurrence of final degree two, not a bank of new
  sockets.

The theorem therefore controls the number of **distinct physical starts per
native row**, not the number of independent package owners or upper-witness
edges.  It also preserves the literal deck only through width `d+1`.  The
immediate-upper source row has width `d+2`, and the theorem explicitly does
not preserve it or compile an unrelated protected ticket bank.

Consequently neither of the following deductions is valid:

```text
13 native starts  =>  678 package ports already exist;
one reused Euler handle  =>  one exceptional owner occurs many times.
```

## 3. A general exceptional-occurrence bound

Put `R=m+1`, and in the joint range

\[
 m\ge8,\qquad 4\le d<R,
 \qquad 2m+1\ge13(d+1),                            \tag{3.1}
\]

consider the explicit canonical upper-hole family

\[
 {cal U}_m={(1100)^2,1111,V:V\in D_{m-6}\}.
                                                               \tag{3.2}
\]

Its members are distinct and

\[
                         |{cal U}_m|=\operatorname{Cat}_{m-6}. \tag{3.3}
\]

The canonical MSW chronology contains none of them.  Moreover the absolute
portal theorem says that no new common-history seam between two canonical
owner occurrences can have union in `(3.2)`.

Let `S` be the set of owner occurrences incident with every successor edge
whose legality is supplied by an added package, collar, dilation, or other
non-common-history actuator.  Assume every successor edge outside the edge
boundary of `S` is either canonical or is created by literal common-history
Euler fusion between canonical occurrences.  This is exactly the
“constant protected bank plus native thirteen-port fusion” architecture.

### Theorem 3.1 (degree-two exceptional-edge bound)

If the final owner chronology contains every target in `U_m`, then

\[
                         |S|\ge\frac12\operatorname{Cat}_{m-6}. \tag{3.4}
\]

#### Proof

Choose a witnessing consecutive-owner edge for each target `U` in `U_m`.
One edge has one union value, so distinct targets need distinct witnessing
edges.

No witness is an old canonical edge, by canonical absence.  If neither
endpoint belonged to `S`, the architectural hypothesis would make the edge
a literal common-history seam between canonical occurrences.  The absolute
portal theorem excludes that as well.  Hence every witnessing edge is
incident with `S`.

The final chronology is degree two.  At most `2|S|` edge occurrences are
incident with `S`, even if every such edge has a different union value.
Equations `(3.3)` and this bound give `(3.4)`. `square`

The proof is unaffected by coalescing many Catalan arborescence incidences at
one history.  Sequential handle reuse changes a successor permutation but
does not raise the final degree of the reused occurrence above two.

### Corollary 3.2 (36-owner package scale)

If `P_m` owner-disjoint closed packages are the only exceptional owners and
each contributes at most 36 owner occurrences, then `(0.1)` holds.  This is
a lower bound, not a construction: cut-open collars and resource avoidance
can only increase the physical cost.

## 4. The fixed 226 bank, even with the prospective collars

The fixed router bank has at most

```text
226*36 = 8,136
```

exceptional owner occurrences, hence at most `16,272` incident final edges.
The hole family first exceeds that numerical capacity at `m=16`, where
`Cat_10=16,796`.

For an intentionally generous comparison, charge every owner of all
prospective token collars as exceptional and disjoint:

```text
461*6 + 16*8 = 2,894 collar owners,
total exceptional budget = 8,136+2,894 = 11,030,
edge capacity             = 22,060.
```

The hole family exceeds even this bound at `m=17`, where
`Cat_11=58,786`.  These two thresholds are arithmetic diagnostics; the
joint universal-port/absolute-hole range `(3.1)` begins later for fixed
`d>=4`.  In every asymptotic regime satisfying `(3.1)`, the same constant
bank is therefore far below the required scale.

If a real graft touches an additional bounded number of context owners per
router/collar, replace `36` in `(0.1)` by that larger constant.  The
Catalan-scale conclusion is unchanged.

## 5. Precise conditional implication for one local actuator

The existing theorems do support the following implication, and no stronger
one.

Assume a **protected flat-atlas insertion** at ambient `m` with all of these
properties:

1. 226 copies of the closed 36-owner three-cycle package and the required
   token collars are coinstantiated with simple, mutually compatible
   owner/lower/upper/q2 banks;
2. their cut-open boundary functor suppresses exactly to the certified flat
   226-word on the 477 logical tokens, with all 678 port incidences ordered;
3. the package/native attachment histories are jointly feasible with the
   selected thirteen-port arborescence classes; and
4. the subsequent Euler tour either avoids every protected upper ticket or
   is covered by an extension theorem which preserves those tickets beyond
   width `d+1`.

Then one physical copy of this whole 226-package bank realizes the one D5
owner-changing actuator before native source serialization.  Unlimited
native arborescence incidences may still coalesce at the thirteen starts, so
there is no factor of `Cat_m` in the package count merely from arborescence
degree.

Items 1--4 are not consequences of the thirteen-port theorem.  In
particular, the audited 36-owner theorem is a closed local package with a
conditional overlap-one interface, and the pseudoforest theorem supplies
only the constraint shape of the missing collar selector.

## 6. Exact asymptotic escape

To use the D5 mechanism for complete upper coverage, a bounded template must
be **tensored across contexts** so that the physical exceptional set has
Catalan size.  It is enough at the scale level to seek

\[
 |S_m|=\Theta(\operatorname{Cat}_{m-6}),            \tag{6.1}
\]

not to place a separate package on every native arborescence edge.  One
36-owner package may in principle witness several named targets, so the
rigorous lower bound is `(0.1)`, rather than literally one package per hole.
But the number of physical copies is necessarily Catalan up to a constant
factor.

The local maximum-degree-three pseudoforest remains useful after tensoring:
each context copy has only tree propagation plus eight `C4` closures.  What
is still missing is a context-separation theorem showing that cross-copy
owner/q1/q2 conflicts have bounded dependency degree, followed by a
protected-upper Euler theorem.  Thirteen source starts solve neither row.

## 7. Computational check

The H100 verifier independently reconstructs the router--token incidence
degrees from the flat certificate, obtains the `461/16` prospective collar
counts, evaluates both generous constant owner budgets, and checks the
Catalan thresholds and `(0.1)`.

```text
verifier
  scratch/verify_d5_flat226_msw13_scale_bound_20260814.py
  SHA256 0f9330d63c4c51f37c2d339161e4f3b635a510b511526930ac90a25e2933a3c9

H100 output
  scratch/verify_d5_flat226_msw13_scale_bound_20260814.h100.out
  SHA256 dbdb1753b69edb0e789a5eadf7aeaa241c614bdf25af32d0e92480f1ebe34118

flat certificate
  scratch/build_t2_suffix_d5_flat_minimum_c6_atlas_20260814.h100.out
  SHA256 2b7bc68cb4559696c0dcf6bc0f7464c8dbe0d7d398dfab2b0996282a7f419dcc
```

All enumeration, verification, and hashing were run through SSH on H100.
