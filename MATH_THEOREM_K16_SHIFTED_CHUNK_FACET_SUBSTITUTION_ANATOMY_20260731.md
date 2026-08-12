# The exact `k=16` carrier is a shifted `k=15` carrier with a slot-preserving facet substitution

Date: 2026-07-31  
Status: exact theorem about the promoted `k=15` and `k=16` certificates;
general facet-substitution lemma; no all-`k` lift or new upper bound is claimed

## 0. Verdict

The nonflat depth-three carrier of the exact `k=16` word is not an
unstructured solver artifact.  It is assembled from the exact `k=15`
depth-three carrier by two operations:

1. independently rotate and concatenate its two Johnson-cycle components;
2. on the top-bit rail, delete one complete 45-cycle and four consecutive
   vertices of the large component, and replace those 49 middle vertices by
   their 49 lower edge facets.

The count `49=45+4` is therefore exact and conceptual:

* `45=3*15` is the small parent factor cycle;
* `4=d(16)+1` is one rooted four-edge collar path.

This is the first literal explanation of how the exact even solution escapes
the flat-carrier and same-parent-doubling no-goes.  It uses the Pascal split
between old middle vertices and a new top coordinate joined to old lower
facets.  What remains open is to turn this finite substitution into a
uniform odd-to-even recurrence which also preserves all interval-union and
compiler rows.

There is a clean comparison with all earlier promoted even answers on the
depth-two plateau.  For `k=8,10,12,14`, direct replay gives the full Pascal
split

\[
 D^2A^{2m}
 =\binom{[2m-1]}m
  \;\sqcup\;
  \left(z+\binom{[2m-1]}{m-1}\right).                \tag{0.1}
\]

The plain half is literally the parent middle layer and the marked half is
the complete lower-facet layer.  The exact `k=16` word is the first even
depth-three answer and the first **partial** facet substitution: most marked
entries stay one rank above the child middle layer, while only the selected
49-edge subgraph is lowered.  This identifies the architectural transition
much more sharply than the statement “`k=16` is nonflat.”

## 1. The parent carrier

Let

\[
 A^{15}=\texttt{answers/k15.word},\qquad
 T^{15}=D^3A^{15}.
\]

Then `|T15|=6435=binom(15,8)`, and its entries are every rank-eight set on
`[15]` exactly once.  In the promoted order it splits as

\[
 C_{\rm big}=T^{15}[0:6390],\qquad
 C_{\rm small}=T^{15}[6390:6435].                 \tag{1.1}
\]

Both pieces are literal Johnson cycles, of lengths `6390=426*15` and
`45=3*15`.  The displayed linear parent chronology opens one edge in each
cycle and uses one cross-splice edge between them.

Thus the formerly empirical `426+3` quotient-component law is visible
directly in the final word, without consulting a search checkpoint.

There is also an exact voltage explanation for both lengths.  Let \(\rho\)
be cyclic left rotation of the 15 old coordinates.  Directly in `T15`,

\[
 T^{15}_{i+426}=\rho^4(T^{15}_i)\quad(0\le i<5964),
 \qquad
 T^{15}_{6390+i+3}=\rho^4(T^{15}_{6390+i})
       \quad(0\le i<42).                            \tag{1.2}
\]

The first blocks contain respectively 426 and 3 distinct free rotation
orbits.  Hence the two components quotient to cycles of orders 426 and 3,
both with voltage `+4` in \(\mathbb Z_{15}\).  In general, the full preimage
of a quotient cycle of order `a` and voltage `v` splits into
`gcd(15,v)` components, each with

\[
                    a\,15/\gcd(15,v)                \tag{1.3}
\]

vertices on free \(\mathbb Z_{15}\)-orbits.  Since
\(\gcd(4,15)=1\), the two orders are exactly `426*15=6390` and
`3*15=45`.  Thus 45 is not merely observed arithmetic: it is the connected
primitive-voltage lift of the three remaining quotient orbits.  Their
canonical representatives are `0x0ce7`, `0x0cf3`, and `0x0e73`.
Indeed, each quotient circuit adds `v` to the fibre coordinate, whose
additive order is `15/gcd(15,v)`; multiplying by the quotient order proves
(1.3).

## 2. The child carrier

Put

\[
 A^{16}=\texttt{answers/k16.word},\qquad
 T^{16}=D^3A^{16},\qquad z=2^{15}.
\]

The top-bit indicator along `T16` has exactly three runs:

\[
                 1^{6390}0^{6435}1^{45}.            \tag{2.1}
\]

After deleting `z`, filter the entries of `T16` into the plain and marked
subsequences.  Both have length 6435.

### Theorem 2.1 (plain shifted-chunk identity)

The plain subsequence is exactly

\[
 T^{15}[5112:6390]\,
 T^{15}[0:5112]\,
 T^{15}[6426:6435]\,
 T^{15}[6390:6426].                                  \tag{2.2}
\]

Hence it traverses the large parent cycle from one cut and the small parent
cycle from another cut, without changing any parent set.

### Theorem 2.2 (marked facet-substitution identity)

The marked subsequence is

\[
 T^{15}[5113:6390]\,
 T^{15}[0:5109]\,
 F_0,F_1,\ldots,F_{48},                              \tag{2.3}
\]

where every `F_i` has rank seven.  The omitted rank-eight parent sets are
exactly

\[
 T^{15}[5109:5113]\ \sqcup\ T^{15}[6390:6435].      \tag{2.4}
\]

The first four facets are

\[
 F_i=T^{15}_{5108+i}\cap T^{15}_{5109+i},
             \qquad 0\le i<4,                       \tag{2.5}
\]

the lower edge colours of a rooted four-edge path in the large component.
The remaining 45 facets are, in one cyclic rotation,

\[
 \{F_4,\ldots,F_{48}\}
 =\{X_i\cap X_{i+1}:X_i\in C_{\rm small}\}.        \tag{2.6}
\]

Their literal order is the small lower-shadow cycle rotated by 35 positions.
Here “literal order” means order in the **filtered marked subsequence**.
In the physical row, the four path facets occupy `T16[6386:6390]`, the
whole plain rail occupies `T16[6390:12825]`, and the 45 cycle facets occupy
`T16[12825:12870]`.  In particular the two substituted pieces are separate:
`F_3` and `F_4` are not Johnson adjacent.  The 49 facets are distinct.  Their
containment graph against the 49 omitted
rank-eight sets has a perfect matching; its left-degree profile is

\[
                       1^1 2^{17}3^{31},             \tag{2.7}
\]

and its right-degree profile is

\[
                       1^1 2^{18}3^{29}4^1.          \tag{2.8}
\]

Consequently `T16` has the exact profile

\[
 6435\text{ plain rank-8}
 \;\sqcup\;
 6386\text{ top-marked rank-9}
 \;\sqcup\;
 49\text{ top-marked rank-8},                       \tag{2.9}
\]

and all 12870 entries are distinct.

There is a stronger cross-row identity.  The top-containing rank-eight
targets are naturally rank-seven subsets of `[15]`.  Their distinct counts
in `D^q A16`, for `q=0,1,2,3`, are

\[
                         1,\ 2,\ 6388,\ 49.           \tag{2.10}
\]

The first three sets are nested.  The depth-two deck and the 49 depth-three
facets satisfy

\[
 \mathcal F_2\cup\mathcal F_3=\binom{[15]}7,
 \qquad |\mathcal F_2\cap\mathcal F_3|=2.            \tag{2.11}
\]

Thus the number of genuinely new top-middle targets first appearing at
depths `0,1,2,3` is exactly

\[
                         1,\ 1,\ 6386,\ 47.           \tag{2.12}
\]

The bridge is therefore not merely a replacement for omitted parent
middles.  It is the exact completion of a nearly perfect depth-two facet
deck: 47 repairs plus the two boundary repetitions present in this
certificate.  This identifies the
coupling between the nonflat middle row and the lower compiler which a
uniform even-lift proof must preserve.

#### Proof

Equations (2.1)--(2.12) are literal sequence and deck identities, replayed by the
audit in Section 5.  The containment matching is obtained by an independent
augmenting-path algorithm on the `49 x 49` graph.  No construction metadata
or solver model is used.  \(\square\)

## 3. Why the substitution preserves the slot count

The finite identity is an instance of a general elementary lemma.

### Lemma 3.1 (cycle/path facet substitution)

Let `V_0,...,V_(s-1)` be a rank-`r` Johnson cycle whose lower edge colours

\[
                         E_i=V_i\cap V_{i+1}          \tag{3.1}
\]

are distinct.  Then `E_0,...,E_(s-1)` is a rank-`r-1` Johnson cycle and has
the same length `s`.

Likewise, for a Johnson path `V_0,...,V_t` with distinct lower edge colours,
the `t` facets

\[
                         E_i=V_{i-1}\cap V_i,
                         \qquad1\le i\le t,          \tag{3.2}
\]

form `t` vertices (and `t-1` edges) of a rank-`r-1` Johnson path and may
replace exactly the `t` nonroot vertices `V_1,...,V_t` without changing the
number of slots.

#### Proof

For the cycle, consecutive facets `E_i,E_(i+1)` are distinct rank-`r-1`
subsets of the common rank-`r` vertex `V_(i+1)`.  For the path, consecutive
facets `E_i,E_(i+1)` are distinct rank-`r-1` subsets of the common vertex
`V_i`.  In either case they differ by one exchange and are Johnson adjacent.
The cyclic assertion includes the last--first pair.  For the path, `E_i`
is contained in its nonroot head `V_i`; for the cycle, `E_i` is contained
in the head `V_(i+1)` (indices modulo `s`).  These assign the facets
slot-for-slot to the asserted parent vertices.  \(\square\)

For `k=16`, apply the cycle part to all 45 vertices of `C_small`, and the
rooted-path part to the four vertices following `T15[5108]`.  These are the
two separate slot-preserving lower-edge-colour images described above; the
lemma does not assert a physical edge between them.  This proves
the structural identity

\[
                  49=45+4                            \tag{3.3}
\]

without any search arithmetic.

## 4. Exact scope and the new recurrence target

The theorem explains the promoted optimum, but it is not yet an all-`k`
construction.  A uniform lift must still prove all of the following.

1. The odd parent carrier has selectable Johnson-cycle components and rooted
   path collars with distinct lower edge colours and compatible ports.  The
   slot algebra does not require the selected components to be small.
2. Replacing their vertices by facets can be realized as the depth-`d`
   derivative of a word of the exact child length.
3. The mixed-rank child chronology covers every deeper upper target.
4. The erosion envelopes admit the integral lower compiler.
5. The necessary cuts can be selected recursively, rather than extracted
   from a completed certificate.

The correct even target is therefore no longer “double one flat parent and
repair a collar.”  It is:

> **Facet-substitution even-lift theorem.**  Starting from an odd carrier
> decomposed into a controlled collection of cycles/rooted paths, replace a
> slot-balanced lower-shadow family by
> top-marked facets and braid it with one plain traversal so that the exact
> child residence, deep-shadow, and compiler conditions hold.

The exact `k=16` certificate proves that this target is nonempty at the first
even depth-three case.

## 5. Audit

Run

```text
python3 scratch/audit_k16_shifted_chunk_facet_bridge_20260731.py
```

The script independently recomputes both depth-three rows, proves the two
parent cycles, verifies every chunk identity, reconstructs both lower-shadow
pieces, checks the `49 x 49` containment matching, and freezes the structural
payload in

```text
scratch/k16_shifted_chunk_facet_bridge_20260731.audit.json
```
