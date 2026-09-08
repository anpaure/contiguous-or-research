# Compressed prefix/suffix decks are sufficient for upper transparency

Date: 2026-08-01  
Status: exact replacement and composition theorem.  This weakens the
pointwise prefix/suffix-signature interface.  It does not construct the
required Pascal packets or prove `nu(k) <= B(k)+O(1)`.

## 0. Outcome

For a word fragment `X=(X_1,...,X_h)`, define its three **coverage decks**

\[
 \begin{aligned}
  \mathcal P(X)&=\{X_1\cup\cdots\cup X_j:1\le j\le h\},\\
  \mathcal S(X)&=\{X_j\cup\cdots\cup X_h:1\le j\le h\},\\
  \mathcal I(X)&=\{X_i\cup\cdots\cup X_j:1\le i\le j\le h\}.
 \end{aligned}                                                   \tag{0.1}
\]

The following four unary conditions on a replacement `X -> Y` are enough
to preserve every old interval union in every exterior context:

\[
 \boxed{
 \mathcal P(X)\subseteq\mathcal P(Y),\qquad
 \mathcal S(X)\subseteq\mathcal S(Y),\qquad
 \mathcal I(X)\subseteq\mathcal I(Y),\qquad
 \bigcup X=\bigcup Y.}                                           \tag{0.2}
\]

Unlike equality of the ordered prefix/suffix sequences, (0.2) ignores the
length of every plateau in the two nested chains.  This is the correct
coverage-level invariant: the universal-word problem asks that a value
occur somewhere, not at the same address.

Consequently, a buffered packet need not export every coordinate's exact
first/last occurrence time.  It is enough to export its *distinct* prefix
and suffix union chains, check internal-deck dominance locally, and certify
the residence boundary state separately.

## 1. One-fragment replacement

For arbitrary words `L,X,R`, write `L X R` for their concatenation.  Empty
exterior words are allowed.  Let `Cov(A)` be the set of unions of nonempty
contiguous intervals of `A`.

### Theorem 1.1 (compressed-deck replacement)

If `X,Y` satisfy (0.2), then for every exterior context `L,R`,

\[
                         \operatorname{Cov}(LXR)
                         \subseteq
                         \operatorname{Cov}(LYR).                 \tag{1.1}
\]

The fragments need not have the same length for (1.1).  Equal length is
imposed only when the ambient construction must keep the word length fixed.

#### Proof

Partition an old interval according to how it meets `X`.

* An interval disjoint from `X` is unchanged.
* An interval contained in `X` has value in `mathcal I(X)`, hence occurs in
  `Y` by internal-deck dominance.
* An interval entering `X` from the left and ending in `X` is the union of
  one fixed suffix of `L` and one member of `mathcal P(X)`.  The same prefix
  value occurs in `Y`, so the same total value occurs in `L Y`.
* The right-crossing case is identical using `mathcal S(X)`.
* An interval crossing both boundaries is the union of a suffix of `L`, the
  total union of `X`, and a prefix of `R`.  Equality of the two total unions
  preserves it literally.

These cases exhaust all intervals. \(\square\)

### Corollary 1.2 (arbitrary compatible composition)

Suppose finitely many pairwise-disjoint fragments are replaced, and each
replacement satisfies (0.2) at the moment it is applied.  Then the final
word covers every interval-union value of the initial word.

#### Proof

Apply Theorem 1.1 sequentially.  Its exterior context is arbitrary, so
earlier replacements do not invalidate a later application. \(\square\)

The corollary does not require the packets' boundary-chain values to be
pairwise disjoint.  Physical/topological compatibility is a separate row.

## 2. Strict improvement over pointwise signatures

Let

```text
X = 1, 1, 12, 12, 1
Y = 1,12, 12, 12, 1.
```

Then

\[
 \mathcal P(X)=\mathcal P(Y)=\{1,12\},\quad
 \mathcal S(X)=\mathcal S(Y)=\{1,12\},\quad
 \mathcal I(X)=\mathcal I(Y)=\{1,12\},                   \tag{2.1}
\]

and both total unions are `12`.  Thus both directions satisfy (0.2).  But
the ordered prefix sequences differ at the second position, so the full
pointwise signature `Sigma(X)=Sigma(Y)` fails.

The coordinate `2` is absent at both fragment boundaries in both words,
and its sole internal run has length two in `X` and three in `Y`.  Thus, at
minimum residence threshold two, even the relevant boundary state and
internal-run legality agree while the pointwise signature still fails.

This is precisely the freedom supplied by resident rail padding: plateau
lengths may change without changing any available crossing-union value.

## 3. Residence is a separate finite boundary state

Theorem 1.1 concerns union coverage only.  For a minimum positive-run
threshold `q`, attach to a fragment, for every coordinate,

* its exact leading positive-run length;
* its exact trailing positive-run length;
* whether the whole fragment contains the coordinate; and
* the assertion that every internal positive run has length at least `q`.

If old and new equal-length fragments have the same first three boundary
data and the new fragment satisfies the fourth assertion, replacement
preserves minimum-`q` residence across both boundaries.  If the even/birail
construction also constrains gaps, attach the same data to the coordinatewise
complements.

For a fixed threshold one may cap leading/trailing lengths at `q`; values
above the threshold are equivalent.  Hence residence contributes only a
finite per-coordinate boundary state and does not restore the discarded
prefix/suffix plateau timings.

## 4. Packet-energy consequence

For a fragment of length `h`, each of `mathcal P(X)` and `mathcal S(X)` is a
nested chain with at most `h` distinct values.  The external upper guard can
therefore be represented by `O(h)` tokens.  The `Theta(h^2)` internal
interval comparisons in `mathcal I(X) subseteq mathcal I(Y)` are a **unary
option-validity test**; they are not resources shared between packets.

Consequently, if a buffered C6 macro has `h=O(D)` and every exported chain,
residence, topology, and compiler token has external menu load `O(m^3)`, its
typed-token row energy remains

\[
                              O(Dm^3),                            \tag{4.1}
\]

exactly the scale required by the sparse-C6 extraction theorem.  The new
criterion is strictly easier to satisfy than pointwise first/last-time
equality, but it does not by itself prove that quadratic packet menus remain.

## 5. Revised lean packet interface

In the transparent-unused-basis composition theorem, replace the old upper
condition

```text
Sigma(X)=Sigma(Y) and I(X) subseteq I(Y)
```

by the four deck conditions (0.2).  Keep unchanged:

1. the finite residence boundary state;
2. the common physical connector/topology state;
3. preservation of the fixed trace-guarded compiler matching; and
4. distinct deletion representatives in its unused-cell bank.

The proof of composition is now Corollary 1.2 rather than same-address
induction.  The exact remaining construction problem becomes:

> Produce `O(D)`-seam macros with quadratic `(b,c)` menus satisfying deck
> dominance, residence state, one common connector, and one unused compiler
> representative, with prescribed-list row energy `O(Dm)`.

This removes first/last *timing equality* from the missing theorem.  It does
not remove the two genuinely global gates: prescribed task-to-anchor spread
and the unused-prefix/compiler Hall row.

## 6. Audit

Run

```bash
python3 scratch/audit_compressed_prefix_suffix_deck_transparency_20260801.py
```

The audit exhausts every pair of length-three fragments over the nonempty
subsets of a two-element universe and every exterior word of length at most
two.  It checks (1.1) for every pair satisfying (0.2), and verifies the
strict example in Section 2.

