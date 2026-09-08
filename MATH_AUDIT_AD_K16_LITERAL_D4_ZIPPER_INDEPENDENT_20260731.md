# Independent audit of the exact `K15 -> K16` literal `D^4` zipper

Date: 2026-07-31  
Lane: AD, independent audit  
Status: **PASS for every finite raw-word identity and for all
dimension-free lemmas in the currently scoped theorem**

## 1. Audited objects and independence

This note audits

```text
MATH_THEOREM_AD_K16_LITERAL_D4_ZIPPER_AND_PHASE_JUMP_RULE_20260731.md
scratch/audit_ad_k16_literal_d4_zipper_phase_rule_20260731.py
```

against only the promoted raw words

```text
answers/k15.word
answers/k16.word
```

The independent checker is

```text
scratch/audit_independent_ad_k16_literal_zipper_20260731.py
```

It does not import the primary checker or any construction checkpoint.  It
discovers the low bridge rows and omitted owners from ranks in the two raw
derivative rows, reconstructs both bipartite graphs, obtains the unique
matching by endpoint stripping, and checks the four Pascal deck equalities
as sets and as selectable literal occurrences.

Hashes at audit time are

```text
theorem
bcc8fb188eeb6f9dd5fc1bbce398dc4179a2b1d9cbbc076cceba936830437153

primary checker
db47171a9c0c9ac269c5870727812d5bf9cb4dd0bfca670475c86ccb33a2dfed

primary JSON
6b79652f47d512cee53913f397cc56a2cafaaeb592756b04b631b19e4aa8509b

independent checker
ac0a0969ec62c31a2d83b473fc19919054fe60e7cb643ab76a25353b519266cb

independent JSON
d210b3a9dc11d0fa606a6fa22420b256b8338d0cef838988afcb0a5af2c81926

answers/k15.word
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b

answers/k16.word
890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

The independent JSON's canonical pre-field payload hash is

```text
5da1af3e359a45f9fa595d9f51cc2cca2c5f4c1c830192dca8382e95161198d1
```

## 2. Literal indexing audit

Use the theorem's convention

\[
 D^qA_i=\bigcup_{j=0}^q A_{i+j}.
\]

Thus `D^3` is a four-cell interval and `D^4` is a five-cell interval.
Direct replay discovers, without supplying their locations, exactly 49
top-containing rank-eight `D^3` rows, at starts

\[
 [6386,6390)\ \dot\cup\ [12825,12870).
\]

The 6386 top-containing rank-nine `D^3` rows omit from the parent rank-eight
deck precisely

\[
 T[5109,5113)\ \dot\cup\ T[6390,6435).
\]

For `i=0,1,2,3`, raw OR replay gives

\[
 D^3A^{16}_{6386+i}setminus\{z\}
   =T_{5108+i}\cap T_{5109+i},
 \qquad
 D^4A^{16}_{6386+i}=z\cup T_{5109+i}.
\]

These are four right extensions, on inclusive physical intervals
`[6386+i,6390+i]`.

For `r=0,...,44`, putting

\[
 a_r=6390+(35+r\bmod45),\qquad
 b_r=6390+(36+r\bmod45),
\]

gives

\[
 D^3A^{16}_{12825+r}\setminus\{z\}=T_{a_r}\cap T_{b_r},
 \qquad
 D^4A^{16}_{12824+r}=z\cup T_{a_r}.
\]

These are 45 left extensions.  The final one is the ordinary linear
five-cell interval `[12868,12872]`; no cyclic or suffix-padded interval is
being smuggled into the proof.  The matched-owner permutation is exactly

\[
 i\mapsto i\quad(0\le i<4),\qquad
 4+r\mapsto4+(35+r\bmod45).
\]

The finite claims in Theorem 2.1 are therefore exact, including every
off-by-one convention.

## 3. The `P_8 \dot\cup P_{90}` audit

The independent checker constructs an edge only when one of the two actual
adjacent five-cell intervals equals `z` joined with the proposed omitted
owner.  It obtains

```text
chronological edges                 96
left degree multiset                1^2 2^47
right degree multiset               1^2 2^47
connected-component vertex orders  8, 90
```

Each component is connected, has maximum degree two, has exactly two
degree-one vertices, and has one fewer edge than vertices.  Hence the graph
is literally `P_8` disjoint union `P_90`, where the subscripts count total
bipartite vertices.  Both paths have even order.  Endpoint stripping forces
all 49 matched pairs and leaves no choice, proving uniqueness independently
of the explicit zipper formula.

The unlabelled containment graph independently has 128 edges and degree
multisets

\[
 1^1 2^{17}3^{31},\qquad 1^1 2^{18}3^{29}4^1.
\]

Thus the theorem correctly distinguishes containment allocation from
literal chronology.  The 128-edge matching is not used as a surrogate for
the 96-edge chronological matching.

## 4. First-band deck equalities

All four assertions of Theorem 3.1 are exact set equalities.

1. The plain rank-eight `D^3` family has 6435 occurrences, all distinct,
   and is exactly `binom([15],8)`.
2. The plain rank-nine `D^4` family has 6434 occurrences and 5005 distinct
   values, exactly `binom([15],9)`.  Selecting one occurrence for each value
   gives the claimed selected-occurrence cover; the whole occurrence family
   itself is intentionally not bijective.
3. The tagged rank-eight `D^2` family has 6388 occurrences and 6388 distinct
   old rank-seven projections.  The 49 bridge facets are distinct, their
   intersection with the `D^2` set is exactly

   ```text
   0x5b06  0x730c
   ```

   and their union is the complete 6435-element rank-seven layer.  Removing
   the two overlapping values from the `D^2` choice leaves a literal
   `6386+49` selected-occurrence decomposition.
4. The high tagged `D^3` family has 6386 occurrences and 6386 distinct
   projections.  It is disjoint from the 49 owners selected by the unique
   `D^4` matching, and their union is the complete parent rank-eight layer.

The use of mixed derivative depths is legitimate because the theorem claims
literal contiguous-OR coverage, not a flat single-depth row.

## 5. Phase and count audit

The independent checker also derives from the raw parent word that
`T=D^3 answers/k15.word` consists of two Johnson cycles of lengths 6390 and
45, with globally distinct lower edge colours.  Each is a strict
`Z_15` spiral of voltage `+4`, with base lengths 426 and 3 respectively.
The equation

\[
 4\tau\equiv3\pmod {15}
\]

has the unique solution `tau=12`, giving the sheet lengths

\[
 3(426),\ 12(426),\ 3(3),\ 12(3)
   =1278,5112,9,36.
\]

The high marked order retains the large component except for a four-owner
predecessor collar.  Its two affine shifts are 5113 and 5158; their
difference is exactly the reserved component mass 45.  The singleton top
cell is `A16[6389]=z`; precisely the four `D^3` starts 6386 through 6389
contain it.  Therefore the two count identities have the claimed separate
causes:

\[
 45=15\cdot3,\qquad 49=45+(3+1).
\]

The primary checker verifies the arithmetic once `q=15`, voltage 4, clean
generator 3, and base lengths 426 and 3 are supplied.  It does not itself
replay the strict-spiral equalities from the raw parent.  This is a coverage
limitation of that script, not a failure of the theorem; the independent
checker replays all 6435 sheet equalities.

## 6. Dimension-free statements and exact scopes

### 6.1 Statements that are sound as written

* **Lemma 4.1** is an exact equivalence for its explicitly restricted
  one-cell, slot-bijective repair class.  Overlap of intervals causes no
  extra compatibility condition because all candidate intervals already
  occur in one fixed word.  The lemma correctly disclaims longer, remote,
  or nonbijective coverage.
* **Lemma 4.2** is a conditional literal identity.  It does not infer the
  existence of the displayed derivative cores; once they occur, the stated
  extensions give the slot-preserving zipper.  Distinct lower colours are
  exactly what makes the lowered slots distinct.
* **Theorem 4.3**, in the audited version with `d>=1`, is precisely Pascal's
  partition of the two child layers into four disjoint shores.  It is a
  sufficient first-band cover criterion and makes no deeper-row claim.
* **Lemma 5.1** holds for every chosen solution `tau` of its congruence.  It
  does not claim that such a solution exists or is unique in a non-coprime
  general instance.

### 6.2 Component-skip scope

The displayed slices and cardinalities in Lemma 5.2 require

\[
 0\le a<L,\qquad \alpha=a+1,\qquad 0\le c\le\alpha,
\]

and `C` plus the reserved bank must be interpreted as disjoint
occurrence-labelled component vertices (as they are in a factor).  The
audited theorem now states all of these hypotheses explicitly, including
the stronger inequalities needed when both chunks are required to be
nonempty.  Under these hypotheses its proof is exact.  The actual values

\[
 (L,S,a,\alpha,c)=(6390,45,5112,5113,4)
\]

satisfy them.

The final component-absorption rule is consequently a valid sufficient
criterion when read with Lemma 5.2's linear component layout and the
lower-rainbow distinctness already stated there.  It is not an existence
theorem for such a layout, zippers, deeper shadows, residence, or the common
lower compiler.

## 7. Final verdict

The decisive finite claim survives adversarial replay:

> the exact 49-facet nonflat substitution is not merely containment-Hall;
> it has 49 honest five-cell witnesses in the promoted word, organized as a
> unique matching in `P_8 \dot\cup P_{90}`, and these witnesses complete the
> full literal rank-eight/rank-nine first band.

No all-dimension recurrence follows.  The current theorem has already made
the required range/distinctness scope explicit; no remaining correction was
identified.
