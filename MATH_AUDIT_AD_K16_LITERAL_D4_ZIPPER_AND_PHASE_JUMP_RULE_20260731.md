# Independent audit of the literal `D^4` zipper and phase-jump rule

Date: 2026-07-31  
Lane: AD  
Status: finite `k=15 -> 16` zipper and first-band theorem PASS; generic
lemmas PASS after the explicit scope/indexing corrections in Section 7

## 0. Audited objects and verdict

This note audits

```text
MATH_THEOREM_AD_K16_LITERAL_D4_ZIPPER_AND_PHASE_JUMP_RULE_20260731.md
SHA-256 bcc8fb188eeb6f9dd5fc1bbce398dc4179a2b1d9cbbc076cceba936830437153

scratch/audit_ad_k16_literal_d4_zipper_phase_rule_20260731.py
SHA-256 db47171a9c0c9ac269c5870727812d5bf9cb4dd0bfca670475c86ccb33a2dfed

scratch/ad_k16_literal_d4_zipper_phase_rule_20260731.audit.json
SHA-256 6b79652f47d512cee53913f397cc56a2cafaaeb592756b04b631b19e4aa8509b
payload 066477d7912cfd9bc4e622615d75fb21000fb581ac8bd56cf6aeed82e13a6f3a
```

The two input hashes reproduce as

```text
answers/k15.word
f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b

answers/k16.word
890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

The finite core passes:

1. every identity in Theorem 2.1 is an honest linear four- or five-cell
   interval identity;
2. the chronological graph in Theorem 2.2 is exactly
   `P_8 disjoint-union P_90`, and the displayed matching is its unique
   perfect matching;
3. all four set equalities in Theorem 3.1 hold, so the word literally covers
   the complete child ranks eight and nine by the selected derivative
   families;
4. Lemma 4.1 is an exact if-and-only-if for a **fixed-word,
   occurrence-bijective, one-cell-extension witness assignment**;
5. the algebra in Lemmas 5.1 and 5.2 is correct.

The theorem does not establish an all-dimension recurrence, residence,
deeper shadows, or a common lower compiler.  Its stated final scope respects
these boundaries.

The final theorem now contains every scope/indexing correction found in the
first audit pass: `d>=1`; first-band cover terminology; `gcd(g,q)=1` and a
chosen representative `0<=tau<q`; the distinction between actual source
starts and affine shifts; the bounds on `a,c,alpha` and the output-index
origin in Lemma 5.2; and the separation between direct replay and imported
strict-spiral provenance.  No substantive or remaining scope correction was
found in the final SHA above.

## 1. Independent check of Theorem 2.1

Write

\[
 T=D^3A^{15},\qquad z=2^{15}.
\]

The parent row has 6435 distinct rank-eight values.  Closing the two
declared intervals `T[0:6390]` and `T[6390:6435]` separately gives 6435
distinct rank-seven intersections, namely the complete rank-seven layer.
Thus “two-factor” in Section 1 must be read with those two closure edges;
the linearly concatenated row itself contains the intercomponent seam.

For `0<=i<4`, direct expansion of the derivative definitions gives

\[
D^3A^{16}_{6386+i}
 =z\cup(T_{5108+i}\cap T_{5109+i}),
\]

\[
D^4A^{16}_{6386+i}=z\cup T_{5109+i}.
\]

The first interval is `[6386+i,6389+i]`, of length four, and the second is
`[6386+i,6390+i]`, of length five.  No endpoint wraps.

For the tail, put

\[
a_r=6390+((35+r)\bmod45),\qquad
b_r=6390+((36+r)\bmod45).
\]

For every `0<=r<45`, direct replay gives

\[
D^3A^{16}_{12825+r}=z\cup(T_{a_r}\cap T_{b_r}),
\]

\[
D^4A^{16}_{12824+r}=z\cup T_{a_r}.
\]

The last five-cell interval is `[12868,12872]`, so this family is also
linear, not cyclic.  The `a_r` enumerate exactly parent indices
`6390,...,6434`.  Together the two families recover exactly

\[
T[5109:5113]\ \dot\cup\ T[6390:6435].
\]

Hence the 49 omitted tagged upper owners receive 49 literal witnesses.

## 2. Independent check of Theorem 2.2

For a low occurrence `(p,F)`, there are at most two allowed one-cell
extensions:

\[
D^4A^{16}_{p-1},\qquad D^4A^{16}_{p}.
\]

Comparing those literal values to the 49 omitted owners gives 96 edges.
Both shore degree profiles are

\[
1^2 2^{47}.
\]

The two connected components have the following exact ledgers:

\[
(|V|,|E|)=(8,7),\qquad(90,89).
\]

Each is connected by definition of component, has maximum degree two and
exactly two degree-one vertices.  Therefore they are paths, proving

\[
\Xi=P_8\dot\cup P_{90}.
\]

An even path has a unique perfect matching, forced from either endpoint.
The four right extensions and 45 left extensions of Theorem 2.1 form a
perfect matching, so they are necessarily that unique matching.

The unlabelled containment graph independently has 128 edges, with profiles

\[
1^1 2^{17}3^{31}
\]

and

\[
1^1 2^{18}3^{29}4^1.
\]

The chronological perfect matching is a subgraph of it, so containment Hall
also holds.  The strict edge-count difference `128-96=32` proves that
containment alone does not certify a literal one-cell extension.

## 3. Full first-band deck audit

Let `Omega=[15]`, and project away `z` on tagged intervals.  The exact set
equalities are

\[
\{D^3_i:z\notin D^3_i, |D^3_i|=8\}
   =\binom{\Omega}{8},
\tag{3.1}
\]

\[
\{D^4_i:z\notin D^4_i, |D^4_i|=9\}
   =\binom{\Omega}{9}.
\tag{3.2}
\]

For the tagged middle shore, let `Q` be the old projections of tagged
rank-eight `D^2` rows and let `B` be the 49 bridge facets.  Then

\[
|Q|=6388,qquad |B|=49,
\]

\[
Q\cap B=\{\mathtt{0x5b06},\mathtt{0x730c}\},
\]

\[
Q\cup B=\binom{\Omega}{7}.
\]

Consequently

\[
(Q\setminus B)\ \dot\cup\ B=\binom{\Omega}{7},
\qquad |Q\setminus B|=6386.
\tag{3.3}
\]

“`D^2` outside the bridge” in Theorem 3.1 must mean values in `Q\B`, not
physical `D^2` start positions outside the two bridge position intervals.
Choosing one occurrence of every value in `Q\B` is legitimate because each
is, by definition, represented by at least one literal `D^2` interval.

For the tagged upper shore, let `H` be the 6386 old projections of the high
tagged `D^3` rows and let `O` be the 49 matched `D^4` projections.  Then

\[
H\cap O=\varnothing,qquad
H\ \dot\cup\ O=\binom{\Omega}{8}.
\tag{3.4}
\]

Equations (3.1)--(3.4), together with the Pascal partitions

\[
\binom{\Omega\cup\{z\}}8
 =\binom\Omega8\dot\cup
   \bigl(z+\binom\Omega7\bigr),
\]

\[
\binom{\Omega\cup\{z\}}9
 =\binom\Omega9\dot\cup
   \bigl(z+\binom\Omega8\bigr),
\]

prove Theorem 3.1 as set equalities, not merely by cardinality.  The result
is an exact selected first-band cover/decomposition.  The current theorem
wording correctly does not call it a common-cap compiler or claim one common
owner schedule beyond these literal intervals.

## 4. Exact scope of Lemma 4.1

Fix the word `W`, the occurrence-labelled low rows and the omitted-owner
bank before forming `Xi_W`.  Define a one-step repair to mean a bijection
from the low occurrences to the omitted owners such that every assigned pair
is witnessed by one of the two displayed one-cell extensions in that same
word.  Under this definition, Lemma 4.1 is exactly equivalent to a perfect
matching:

* every matching edge already is a literal nested interval pair;
* overlapping witness intervals create no conflict because no word value is
  being changed;
* conversely every allowed assigned pair is an edge, and the two bijection
  requirements make the selected edges a perfect matching.

The iff does **not** cover any of the following broader notions:

1. ordinary target coverage, where one bridge occurrence need not be used;
2. longer or remote witnesses for an omitted owner;
3. simultaneous edits of the word intended to create the extensions; or
4. degree-two topology or a common lower-owner compiler.

The theorem text states the first two qualifications.  Replacing “repair”
by “fixed-word one-cell witness assignment” would remove the remaining
terminological ambiguity.

Lemma 4.2 is also sound.  For a Johnson path, two consecutive distinct edge
facets of the common owner `V_i` have union `V_i`; the globally distinct
lower-colour hypothesis in particular makes those two facets distinct.  The
cycle argument is identical.  The displayed derivative-extension
hypotheses already contain the required literal chronology.

The current Theorem 4.3 includes the necessary explicit hypothesis

\[
d\ge1,
\]

because Condition 3 invokes `D^(d-1)`.  Its proof by the two Pascal layer
partitions is exact.

## 5. Phase-jump lemmas

### Lemma 5.1

For a strict spiral

\[
P\Vert R^gP\Vert\cdots\Vert R^{(q-1)g}P,
\]

rotation before sheet `tau` leaves `q-tau` sheets after the cut and `tau`
before it.  Hence the chunk lengths `(q-tau)n,tau n` are exact.  Its first
new sheet is `R^(g tau)P`, so the phase equation

\[
g\tau\equiv s\pmod q
\]

is exact.

For the K15 data,

\[
(q,g,s)=(15,4,3),\qquad \tau=12,
\]

and component base lengths 426 and 3 give

\[
1278,5112,9,36.
\]

The final theorem explicitly assumes `gcd(g,q)=1`, chooses
`0<=tau<q`, and separately records `0<tau<q` when both chunks must be
nonempty.  Thus existence and uniqueness of the representative and the
chunk statement have their required hypotheses.

There is one literal indexing correction.  The four affine shifts in the
continuing output coordinate are

\[
5112,5157,36,6426.
\]

The four actual first parent indices of the chunks are instead

\[
5112,0,6426,6390.
\]

The final theorem now labels the first list as actual parent source starts
and the second list as affine shifts.  The chunk lengths and all later
shift-difference identities are unchanged.

The replay script hardcodes `g=4`, base lengths `426,3`, and clean generator
3, then checks their arithmetic.  It does not reconstruct the spiral action,
component cycles, or voltage from the two words.  The final reproducibility
paragraph now says exactly that those parameters are separately
authenticated: the script is independent for the literal zipper and
first-band decks and is an arithmetic consistency check for the imported
strict-spiral provenance.

### Lemma 5.2

Assume

\[
0\le c\le\alpha\le L
\]

and index the displayed retained-high order from output position zero.  Its
chunk lengths are

\[
L-\alpha,\qquad \alpha-c,
\]

so its retained length is `L-c`, and exactly `S+c` parent owners are omitted.
The first chunk has affine shift `alpha`.  At output position `L-alpha`,
the second shift `alpha+S` gives

\[
(L-\alpha)+(\alpha+S)=L+S\equiv0\pmod{L+S}.
\]

Therefore the shift jump is exactly `S`.  The K16 substitution

\[
(L,S,\alpha,c)=(6390,45,5113,4)
\]

gives chunk lengths `1277,5109`, shifts `5113,5158`, and omitted-bank size
49.  No indexing error remains after distinguishing affine shifts from
actual chunk starts.

## 6. Collar identity and conditional rule

For a length-`n` linear word, the exact number of depth-`d` windows
containing position `p` is

\[
\min(p,n-d-1)-\max(0,p-d)+1
\]

when positive.  Under `d<=p<=n-d-1` this is exactly `d+1`, as the final
theorem now states.  The cell

\[
A^{16}_{6389}=z
\]

belongs to the four `D^3` windows beginning at `6386,6387,6388,6389`, and
these are exactly the forward zipper rows.  Hence the finite identity

\[
49=45+(3+1)
\]

is literal.  It does not make `c=d+1` necessary for another lift, and the
theorem correctly avoids that claim.

The Section 7 component-absorption rule is a conditional sufficient theorem.
Its `S` counts occurrence-labelled trace owners in the reserved bank, so the
final phrase “trace-owner mass” is the exact quantity used in Lemma 5.2.
The same child word is assumed to realize all zippers and all four first-band
decks.  Under those antecedents its conclusion follows from Lemma 4.1 and
Theorem 4.3.  Lower-rainbow supplies distinct bridge facets, but does not
itself supply the word, safe phase, residence, deeper shadows, or common-cap
compiler.  The stated open gates correctly retain all of these obligations.

## 7. Final boundary

All corrections identified in the preliminary audit are present in theorem
SHA `bcc8fb18...`.  The exact proved boundary is:

* unconditional for the displayed K15/K16 words: all 49 nested witnesses,
  `P_8 disjoint-union P_90`, and complete ranks eight and nine;
* exact dimension-free iff: fixed-word, degree-exact one-cell witness
  assignment versus perfect matching;
* exact conditional arithmetic: common-phase chunks and component-skip
  shift `S`;
* not proved: an all-dimension component bank, integral overlapping-row
  realization, residence/deep shadows, or common lower compilation.
