# Ramsey coordinate hosts, Boolean hexes, and the reset attachment-parity gate

**Date:** 2026-08-01  
**Lane:** K, depth-three functional attachment  
**Status:** unconditional projection and parity theorems, an exact abstract
phase-paired open-module sufficient lemma, and sharply scoped obstructions.
No all-dimensional high-target table, functional attachment, or compiler is
constructed.

## 0. Verdict

The Ramsey/two-sided-coordinate-cover idea can be used at the opened reset
only after a matrix entry has been upgraded from an endpoint incidence to a
**literal phase-paired open module**.  Ordinary row/column cover and separated
palettes do not choose the high-target flag table or the functional owner
bijection.

There are two exact reasons.

1.  In the forward Boolean-hex orientation, the head--owner columns are
    fixed pointwise.  The hex can reroute the predecessor matching but
    cannot supply a nontrivial owner-attachment return.
2.  In the reversed orientation, the predecessor and attachment projections
    both change by the same three-cycle.  Thus every matching-closed Boolean
    hex has even sign in both projections.  The two phases of a closed
    rolling reset have signature

    \[
       (\operatorname {sgn}\pi_{\rm att},
        \operatorname {sgn}\pi_{\rm pred})=(-1,+1).
    \]

    Consequently no composition of matching-closed Boolean-hex toggles can
    implement the reset phase trade.  Any successful host must use the open
    boundary: equivalently it must contain an odd attachment return, or a
    gain/loss buffer whose final closure has that odd sign.

There is nevertheless a useful conditional statement.  A pair of open
Boolean-hex modules, one completing each reset phase, gives the required
common literal three-return lift provided the two contractions have the same
residual resource system and the modules carry lossless depth-three flag
lifts.  A single standard Cartesian gain ear in each phase does **not**
instantiate this interface on the zero-extra-quarantine face: their typed
old-pair tail supports differ for every one of the \((m-1)^4\) option pairs.
This avoids pointed-Steiner regularity and is compatible with a nonregular
table.  What a Ramsey coordinate cover does **not** prove is the existence
of such a paired cell with root-coloured target balance, owner injectivity,
and a common residual cap.

The smallest exact warning is already present at \(m=3\): a primitive
resource-zero three-root circuit can have empty functional graph before and
after the circuit.  Hence support three, static target balance, and endpoint
palette separation do not imply functional attachment.

There is now an explicit central open module on the live side of these
obstructions.  The two orientations of one Johnson square, with the seam
atom omitted in both phases, have one head--owner alternating return and
exactly two tail--head parity returns.  They share all three retained lower
and upper colours, and support four is minimal among exact orientation-flip
trades.  This instantiates Theorem 3.1 only at the central four-resource
level: its fresh square coordinate has an internal run of length two, so a
resident depth-three flag/collar lift and the common compiler minor remain
open.

## 1. The two projections of the Boolean hex

Use the Boolean-hex notation

\[
\begin{array}{lll}
 A=S+a+u,&B=S+a+c,&C=S+c+u,\\
 D=S+b+c,&E=S+b+u,&F=S+a+b,
\end{array}
\]

and put

\[
 O=\{A\to B,C\to D,E\to F\},\qquad
 N=\{A\to F,C\to B,E\to D\}.                 \tag{1.1}
\]

The corresponding owners are, in the old order,

\[
             U_b=S+a+c+u,\quad
             U_a=S+b+c+u,\quad
             U_c=S+a+b+u.                         \tag{1.2}
\]

Let

\[
                         \sigma=(1\ 3\ 2)                 \tag{1.3}
\]

on the ordered triples used below.  Its orientation is immaterial; only
that it is a three-cycle matters.

### Theorem 1.1 (forward projection law)

Index the tails by \((A,C,E)\), the heads by \((B,D,F)\), and the owners by
\((U_b,U_a,U_c)\).  Passing from \(O\) to \(N\):

* changes the tail--head matching by \(\sigma\); and
* leaves every head--owner pair fixed pointwise:

\[
              B\leftrightarrow U_b,qquad
              D\leftrightarrow U_a,qquad
              F\leftrightarrow U_c.                       \tag{1.4}
\]

In particular a forward hex is a predecessor circuit with attachment
signature equal to the identity.

#### Proof

The new edges send \(A,C,E\) to \(F,B,D\), respectively, which is the
three-cycle (1.3).  Their owner--head pairs are

\[
 (U_c,F),\qquad(U_b,B),\qquad(U_a,D),
\]

the same three pairs as in the old phase.  This proves both claims.
\(\square\)

Reverse every directed atom.  Thus

\[
 O^{\rm rev}=\{B\to A,D\to C,F\to E\},\qquad
 N^{\rm rev}=\{F\to A,B\to C,D\to E\}.             \tag{1.5}
\]

### Theorem 1.2 (reversed diagonal law)

Index the heads by \((A,C,E)\).  Passing from \(O^{\rm rev}\) to
\(N^{\rm rev}\) changes both

* the predecessor tail assigned to a head, and
* the owner assigned to that head

by the same three-cycle \(\sigma\).  Equivalently, the tail--owner pairs

\[
              B\leftrightarrow U_b,qquad
              D\leftrightarrow U_a,qquad
              F\leftrightarrow U_c                       \tag{1.6}
\]

are fixed pointwise.

#### Proof

At heads \((A,C,E)\), the old tails are \((B,D,F)\) and the new tails are
\((F,B,D)\).  The old owners are \((U_b,U_a,U_c)\), while the new owners
are \((U_c,U_b,U_a)\).  These are the same cyclic permutation.  Pairing by
tail gives (1.6).  \(\square\)

Both projection laws are occurrence-level statements.  Equality of the
three owner or head sets without these pairings is weaker and is not enough
for functional attachment.

## 2. Exact parity obstruction for a matching-closed host

Let two perfect matchings on the same labelled shores be compared by the
relative permutation obtained after identifying one shore.  Its sign is
invariant under relabelling.  A Boolean-hex cycle toggle has, by Theorems
1.1--1.2, one of the signatures

\[
                         (+1,+1),                           \tag{2.1}
\]

in attachment and predecessor parity: the identity and every three-cycle
are even.

### Theorem 2.1 (hex-generated matching-closed subgroup)

Suppose a sequence of forward or reversed Boolean-hex **cycle-mode**
toggles starts and ends with perfect attachment and predecessor matchings
on the same resource shores.  Then the relative attachment permutation and
the relative predecessor permutation are both even.

This remains true when the hex supports overlap and the toggles are made
serially, provided every intermediate step is a legal cycle-mode matching
toggle.

#### Proof

Each forward toggle has attachment permutation the identity and predecessor
permutation a three-cycle.  Each reversed toggle has a three-cycle in both
projections.  Hence each step has even sign in each projection.  Signs
multiply under serial composition.  Overlap of supports does not affect
this group identity.  \(\square\)

Now let the rolling reset have

\[
                         N=2(d+1).                          \tag{2.2}
\]

Identify its heads and owners with \(\mathbb Z_N\).  Its forward and reverse
attachments are

\[
             \theta_\rightarrow(b)=b-1,qquad
             \theta_\leftarrow(b)=b.                       \tag{2.3}
\]

The corresponding predecessor permutations are the two directed neighbour
cycles, and their relative permutation is translation by two.

### Theorem 2.2 (rolling-reset parity signature)

The relative attachment permutation of the two closed reset phases is one
\(N\)-cycle and hence is odd.  The relative predecessor permutation is the
union of two cycles of length \(N/2=d+1\), and hence is even.  Therefore

\[
  (\operatorname {sgn}\pi_{\rm att},
   \operatorname {sgn}\pi_{\rm pred})=(-1,+1).             \tag{2.4}
\]

#### Proof

Equation (2.3) makes the relative attachment map translation by one on
\(\mathbb Z_N\), an \(N\)-cycle.  Since \(N\) is even its sign is
\((-1)^{N-1}=-1\).

The predecessor phases differ by translation by two.  Because
\(\gcd(2,N)=2\), this is two cycles, each of length \(N/2=d+1\).  Their
product has sign

\[
                    (-1)^{2((d+1)-1)}=+1.
\]

\(\square\)

### Corollary 2.3 (exact closed-host no-go)

No matching-closed host generated solely by Boolean-hex cycle toggles can
carry the complete bidirectional rolling-reset phase trade.  In particular,
two-sided coordinate cover, palette separation and arbitrarily many
support-three hexes do not remove the obstruction if all matrix entries are
closed cycle toggles.

The scope is important.  Gain ears pass through a state with one free
tail, head, owner and lower colour, so the relative permutation is not
defined at that intermediate state.  They are the exact way to escape
Corollary 2.3.  Equivalently, an opened-reset host must export an **odd
attachment return** (or an occurrence-labelled gain/loss buffer realizing
one).  Endpoint matrices which do not record this parity bit can satisfy
all row and column margins while living entirely in the wrong component.

## 3. The exact phase-paired open-module interface

For an oriented target atom

\[
                         e=(L,U,E,F),                         \tag{3.1}
\]

the Boolean Cartesian fan gives \((m-1)^2\) hexes with

\[
 O^-_e=\{o_1,o_2\},\qquad N_e=\{n_1,n_2,n_3\},             \tag{3.2}
\]

and

\[
       \operatorname {res}(N_e)
       =\operatorname {res}(O^-_e)\mathbin{\dot\cup}
          \operatorname {res}(e)                            \tag{3.3}
\]

in the lower, owner, tail and head shores.  At depth three the lossless
flag lift additionally preserves both suffix-target multisets and every
positional rail histogram.

Call two open modules \(\mathcal E_\rightarrow,\mathcal E_\leftarrow\)
**phase-paired** at an opened reset if each module is either one lossless
gain ear satisfying (3.2)--(3.3), or a coupled union of such ears with the
same net resource identity, and:

1. in phase \(\varepsilon\), its missing atom \(e_\varepsilon\) is exactly
   the phase's free literal boundary tuple (including its lower and owner
   labels);
2. every deleted atom is present in the selected phase matching, every
   inserted atom is root-admissible, and the module is a lossless
   depth-three flag lift with net gain exactly the free boundary tuple;
3. contracting the selected phase module leaves the same occurrence-labelled
   residual tail, head, owner and marked-target system in the two phases;
4. every nonendpoint resource of either module is private to that phase
   module, and the common endpoint resources have capacity one; and
5. the two completed global matchings do not use the direct opposite
   orientations of one seam owner as a closed doubleton.

### Theorem 3.1 (phase-paired Boolean-hex open-module completion)

If an opened bidirectional reset has a phase-paired pair of open modules, then
each phase extends to an exact functional predecessor matching on the same
residual resource system.  The symmetric difference of the two completed
systems supplies one attachment return and the two predecessor-parity
returns required by the rolling-reset functional exchange theorem, and
these returns are projections of common literal turns.

#### Proof

In a single-ear phase, (3.3) replaces the two old atoms by three atoms and
fills exactly the free lower, owner, tail and head resources of the missing
boundary tuple.  In a coupled module the same conclusion is its defining
net resource identity.  The depth-three lift preserves the marked suffix resources.
Thus each phase is a complete literal matching.

By condition 3, deleting the two contracted phase modules identifies the
same residual matching instance.  Compare the two completed perfect
matchings.  Their attachment symmetric difference is a union of alternating
cycles; removing the common residual part leaves the internal opened-reset
attachment path plus an exterior return.  The same argument in the
tail--head projection gives the two internal parity paths plus exterior
returns.  Because every selected object was a literal turn triple, the
three projected returns have a common atomic lift.  Conditions 4--5 exclude
resource collisions and direct closed-doubleton closure.  This is exactly
the compatible three-return criterion.  \(\square\)

The theorem is not circular: its test is equality of two finite contracted
occurrence-labelled systems, not the prior existence of the three projected
paths.  On the other hand, it is a sufficient interface, not an existence
proof for the paired modules.

### Corollary 3.2 (standard opposite-ear face is empty)

On the zero-extra-quarantine face, where the two phases must consume the
same literal old-pair support, Theorem 3.1 cannot be instantiated by one
standard Cartesian gain ear at each oppositely oriented seam.  Their old
tail sets are

\[
 \{U-b,L-b+c+d\}\quad\hbox{and}\quad
 \{U-b',L-b'+c'+a\},
\]

and are unequal for all \(b,b'\in L\), \(c,c'\notin U\).  Thus the active
search on the fixed reset host begins with the support-four Johnson-square
open path, a collared enlargement of it, or another coupled multi-ear
module.  The abstract criterion still
allows separately private modules only when their complete contraction to
one common exterior is proved independently.

## 4. What a Ramsey coordinate cover does and does not supply

A two-sided coordinate cover asserts only that every endpoint state occurs
in some available row and in some available column.  Even universal
endpoint compatibility is a statement about one return at a time.  The
phase-paired condition of Section 3 contains three extra correlations:

* **root-coloured target balance:** the three substitutions must separately
  permute the rank-\((m-1)\) and rank-\((m-2)\) target occurrences (and the
  aligned \(z\)-occurrences when that deck is frozen);
* **owner/root injectivity:** the selected atoms must be one-to-one on the
  literal owner, tail and head occurrences, not only on endpoint types; and
* **common residual contraction:** the two phase choices must expose the
  same remaining table and cap.

Separated internal palettes make already valid entries commute.  They do
not imply any of these three rows.  In particular, the two direct reset
closures have perfect endpoint compatibility but are the opposite
orientations of one physical seam and repeat its unique owner if combined.

There is a second, easily missed distinction.  It is safe to separate
**auxiliary chronology palettes**: private interior vertices, guards and
compiler sinks belonging to different return paths may live in disjoint
grounds.  It is fatal to separate the high-target cancellation resources
themselves.

### Theorem 4.1 (direct-sum target-palette obstruction)

Let three changed depth-three rows have signed normalized target deltas

\[
 \delta_i=e_{T'_i}+e_{P'_i}-e_{T_i}-e_{P_i},
                         \qquad i=1,2,3.                    \tag{4.1}
\]

Suppose their complete \(T/P\) supports lie in pairwise disjoint coordinate
grounds \(E_1,E_2,E_3\).  If

\[
                         \delta_1+\delta_2+\delta_3=0,       \tag{4.2}
\]

then \(\delta_i=0\) for every \(i\).  Consequently no primitive
support-three resource circuit can have return-wise disjoint high-target
palettes.

The same conclusion holds on the fixed-alignment face after adding the
\(z\)-deck: disjointness in the full \((T,P,z)\) resource ground makes every
augmented row delta zero separately.

#### Proof

The target resource group is the direct sum

\[
                         \mathbb Z^{E_1}\oplus
                         \mathbb Z^{E_2}\oplus
                         \mathbb Z^{E_3}.
\]

Project (4.2) to the \(i\)th summand.  Only \(\delta_i\) survives, so it is
zero.  Primitivity requires every row delta to be nonzero, giving the
contradiction.  The augmented statement is identical.  \(\square\)

Thus the correct separated-host architecture is

\[
 \boxed{\text{one shared Latin-cross cancellation core in }(T,P,z)}
 \quad+\quad
 \boxed{\text{disjoint auxiliary chronology/guard palettes}.} \tag{4.3}
\]

This is exactly the algebra of an external puncture with protected two-sum
completion.  If the anchor row has delta \(\delta_a\), its two completing
rows must satisfy

\[
                         \delta_b+\delta_c=-\delta_a.        \tag{4.4}
\]

The transparent realization is the Latin cross which cyclically permutes
the old \(P\)- and \(T\)-occurrences (and the old \(z\)-occurrences when
alignment is frozen).  Equation (4.4) requires shared target labels across
the three return cells; return-wise target-palette separation makes it
impossible.  Conversely, auxiliary paths realizing the three literal turns
may be resource-separated after this common cancellation core has been
fixed.

The same rule is load-bearing in Theorem 3.1.  Its owner return and two
predecessor returns are not three independently chosen endpoint paths.
They must be projections of one literal Latin-cross/open module.
Only their auxiliary interiors may be placed in separated Ramsey palettes.

The same point appears in the normalized depth-three resource system.  A
primitive three-root circuit must be a root-admissible Latin cross in its
two target decks; if alignment is fixed it must also permute the three
\(z\)-occurrences.  An endpoint matrix which records only source and sink
types can select a structural-zero cross corner.  Ramsey homogeneity does
not turn that corner into a literal flag option.

### Proposition 4.2 (smallest static-versus-functional obstruction)

At \(m=3\) there is a protected three-root table with a unique primitive
resource-zero support-three circuit such that the functional predecessor
graph is empty before and after the circuit.

#### Proof

Use the three roots and the two binary options in Proposition 5.2 of
`MATH_THEOREM_A_D3_NORMALIZED_RESOURCE_CIRCUITS_AND_FUNCTIONAL_CUT_DESCENT_BOUNDARY_20260801.md`.
Their three nonzero target deltas telescope, and their old and new aligned
label multisets agree.  For every option, however, the tail bottom lies in
\(\{1,2,3\}\) while the required head pointer lies in
\(\{4,5,6\}\).  The literal condition \(\gamma\in S\) therefore fails on
every ordered pair in both phases.  \(\square\)

Thus even exact target balance, exact aligned-label balance, and a primitive
support-three packet do not manufacture one functional edge.  This is a
literal obstruction, not a failure of a probabilistic estimate.

### Corollary 4.3 (proof-safe Ramsey interface)

The Ramsey/separated-palette method can be invoked proof-safely only after
each matrix cell is labelled by at least

\[
 \boxed{\text{literal root options};\ \text{two target decks};\ z\text{-flux};
 \ \text{tail/head/owner occurrences};\
 \text{attachment parity};\ \text{common residual cap}.}   \tag{4.5}
\]

On this augmented state space, a universal phase-paired open-module cell gives
Theorem 3.1.  Without these labels, coordinate cover is merely a marginal
endpoint statement and supplies neither the missing high-target table nor
the functional owner bijection \(\theta\).

## 5. A scoped positive use away from the phase trade

The forward hex remains useful on a fixed attachment face.  Its
head--owner columns are pointwise fixed by Theorem 1.1.  Therefore, if its
lossless depth-three gain ear is rooted outside a critical Hall shore and
adds one new punctured predecessor without deleting the last witness of any
old neighbour, it raises that shore's neighbour count by one while
preserving \(\theta\), both target decks, and every central four-resource
palette.

For any fixed target atom the Cartesian fan has \((m-1)^2\) choices and
each non-target typed resource occurs in at most \(m-1\) choices.  Hence a
bounded family of already specified, pairwise resource-disjoint target
atoms has disjoint forward ears whenever

\[
                         m-1>16(H-1).                        \tag{5.1}
\]

This is a genuine bounded prepared-bank lemma, but not a functional descent
theorem: the all-cut inequalities, the root-admissible target cross, and
the existence of the old pair \(O^-\) remain explicit hypotheses.  In a
pair of simple reset rings there is also the independent forward-tail
obstruction: all three tail flags delete the same coordinate first, so one
forward hex needs at least three native rings.  A general Ramsey host may
avoid that ring restriction, but palette separation alone does not.

## 6. Exact remaining boundary

Pointed-Steiner regularization is unnecessary for the conditional theorem
above and impossible in the relevant complete-host face at \(m=8\).  The
live nonregular construction problem is narrower and more concrete:

> Give the central support-four Johnson-square return a resident all-depth
> flag/collar lift, preserve its exterior upper tickets, and prove that
> forcing its two phases leaves one common residual functional/Rado and
> compiler minor.  A larger coupled multi-ear module is the fallback.

The Boolean hex can provide cubic predecessor rerouting and bounded critical
cut repair.  It cannot, in matching-closed cycle mode, provide the odd
attachment transition of the reset.  The Ramsey construction can organize
and separate literal cells once they exist; it does not prove the root- and
target-injective cells exist.  This is the precise proved/conditional
boundary.

No assertion is made about global connectivity, voltage, residence outside
the packet, arbitrary-width upper transparency, or the terminal common-cap
compiler.

## 7. Dependencies

The note uses the exact statements in:

```text
MATH_THEOREM_A_D3_NORMALIZED_RESOURCE_CIRCUITS_AND_FUNCTIONAL_CUT_DESCENT_BOUNDARY_20260801.md
MATH_THEOREM_BOOLEAN_HEX_TERNARY_FOUR_RESOURCE_ABSORBER_20260801.md
MATH_THEOREM_D3_BOOLEAN_HEX_RESET_SPLICE_AND_PRIVATE_UPPER_OBSTRUCTION_20260801.md
MATH_THEOREM_K_BIDIRECTIONAL_ROLLING_RESET_FUNCTIONAL_ATTACHMENT_AND_DOUBLETON_GATE_20260801.md
MATH_ASSESSMENT_SATURATED_ENDPOINT_MATRICES_MEDIAN_EXPANDER_AND_PROTECTED_RESET_GATE_20260801.md
MATH_THEOREM_D3_COMPLEMENT_LIST_COLOURING_STEINER_NECESSITY_AND_ODD_M_NOGO_20260801.md
MATH_THEOREM_OPPOSITE_SEAM_CARTESIAN_GAIN_EAR_COMMON_RESIDUAL_NOGO_20260801.md
MATH_THEOREM_BOOLEAN_JOHNSON_SQUARE_OPEN_THREE_RETURN_MACRO_20260801.md
```

No computation is used.
