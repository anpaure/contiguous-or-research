# Independent audit of the conjugate-pairing catalog

## 1. Verdict

The two formal results in `CONJUGATE_PAIRING_CATALOG.md` survive audit:

1. the exact one-set type formula is correct;
2. the stated polynomial-size **multiset** catalog exists with the stated
   additive error and more than enough slack in its constant;
3. the total-variation corollary is correct for `m>=2`;
4. averaging an occurrence multiset over the full coordinate-permutation
   group gives expected target multiplicity one.

Two consequences required correction.

* The catalog theorem controls one-set type marginals.  It does not prove a
  joint source--target allocation and therefore does not, by itself, remove
  the aggregate fixed-pair capacity imbalance.
* Arbitrary coordinate conjugation does not preserve the standard
  binary-RSK radius or RSK-radius purity of a BK cell.  The fractional lemma
  remains valid because it uses only rank transitivity, but a construction
  requiring the original RSK resolution needs an additional transported or
  rebuilt radius certificate.

The source note has been patched to state exactly this scope.

## 2. Exact type formula

Fix a perfect matching `P` with `m` pairs and a set size `t`.  If exactly
`f` pairs are full in `S`, then:

1. choose those pairs in `binom(m,f)` ways;
2. choose `t-2f` of the remaining `m-f` pairs to be split;
3. choose one of the two endpoints in each split pair.

Every other pair is then empty.  Hence

\[
 A_{m,t}(f)=\binom mf\binom{m-f}{t-2f}2^{t-2f}.      \tag{2.1}
\]

The invalid-binomial convention exactly enforces

\[
 0\le f\le\lfloor t/2\rfloor,
 \qquad t-2f\le m-f.
\]

There is no omitted factor for ordering pairs or endpoints.  As a check,
summing (2.1) over `f` gives `binom(2m,t)`, equivalently by taking the
coefficient of `x^t` in

\[
                         (1+2x+x^2)^m=(1+x)^{2m}.
\]

The symmetric group acts transitively on both perfect matchings and
`t`-subsets.  Double counting `(P,S)` therefore proves

\[
 \Pr_P(\phi_P(S)=f)=A_{m,t}(f)/\binom{2m}t             \tag{2.2}
\]

for each **fixed** `S`; no averaging over `S` remains in the conclusion.

Substitution of `t=m` and `t=m-q` gives respectively

\[
 V_f={m!\over f!f!(m-2f)!}2^{m-2f},
\]

and

\[
 T_{f,q}={m!\over f!(f+q)!(m-2f-q)!}2^{m-2f-q}.
\]

Direct enumeration of every perfect matching and subset through `m=5`
reproduced (2.1)--(2.2); at `m=5` this checks 945 matchings.

## 3. Uniform catalog and constants

For a fixed pair `(S,f)`, Hoeffding gives

\[
 \Pr\{|\widehat p_{S,f}-p_{|S|,f}|>\epsilon\}
 \le 2e^{-2K\epsilon^2}.                             \tag{3.1}
\]

There are at most

\[
                          2^{2m}(m+1)                \tag{3.2}
\]

such pairs.  With natural logarithms and

\[
 K=\left\lceil {4(m+\log(m+1)+1)\over\epsilon^2}
   \right\rceil,
\]

the logarithm of the union-bound failure probability is at most

\[
 \log2+2m\log2+\log(m+1)-8(m+\log(m+1)+1)<0.         \tag{3.3}
\]

Thus the numerical constant four is valid and very conservative.

The quantifier over all `2^(2m)` subsets is genuine: the logarithm of the
number of tested events is only linear in `m`.  The conclusion is an
additive `epsilon` estimate for each type coordinate.  It is not a relative
estimate for rare types.

The output is a **multiset**.  Independent sampling can repeat a perfect
matching, and empirical frequencies count catalog indices with
multiplicity.  Nothing in the proof yields the same bound after
deduplicating the catalog, and the source correctly does not claim a set of
distinct matchings.

## 4. Total-variation corollary

For `m>=2`, take `epsilon=m^(-2)`.  The size bound becomes

\[
 K\le 4m^4(m+\log(m+1)+1)+1=O(m^5).                 \tag{4.1}
\]

For each fixed `S`, at most `m+1` type values occur, so

\[
 \|\widehat\mu_S-\mu_{|S|}\|_1
 \le {m+1\over m^2},
 \qquad
 d_{TV}(\widehat\mu_S,\mu_{|S|})
 \le {m+1\over2m^2}.                                \tag{4.2}
\]

This is uniform in `S`.  The restriction `m>=2` only avoids applying
Theorem 2 with `epsilon=1` at `m=1`; the asymptotic statement is unchanged.

## 5. Fractional conjugation lemma

Let the lower occurrence multiset be

\[
                         (L_1,\ldots,L_{N_q}),       \tag{5.1}
\]

where repetitions are allowed and every `L_i` has rank `m-q`.  For a fixed
target `S` of that rank and a uniform coordinate permutation `pi`,

\[
 \mathbb E\,\operatorname{mult}_S(\pi L_1,\ldots,\pi L_{N_q})
 =\sum_{i=1}^{N_q}\Pr(\pi L_i=S)
 ={N_q\over\binom{2m}{m-q}}=1.                      \tag{5.2}
\]

The upper proof is identical.  This direct derivation makes three
quantifiers explicit.

1. Occurrences, not distinct shadow values, are counted.  If all `N_q`
   original occurrences coincide, one conjugate still has an `N_q`-fold
   collision.
2. The exact average is over all `(2m)!` permutations with equal group
   weight, hence with multiplicity when different permutations give the
   same conjugated system.
3. The claim is an expected marginal degree at each target.  It gives no
   concentration, no low collision count for one conjugate, and no
   simultaneous integral selection.

The proof needs only transitivity of the symmetric group on a rank layer.
The adjective “radius-resolved” was therefore removed from the premise: it
was irrelevant to (5.2) and risked suggesting a false invariance.

## 6. Radius is not invariant under conjugation

An arbitrary permutation of ground coordinates does not preserve binary
RSK shape.  More strongly, it can destroy radius purity even on an actual
BK edge.

For `m=2`, the words

\[
                         0110,qquad0101              \tag{6.1}
\]

are joined by the active odd BK move `tau_3`.  Both have binary-RSK radius
one.  Swap ground coordinates two and three.  Their images are

\[
                         0110,qquad0011,             \tag{6.2}
\]

whose radii are respectively one and two.  Thus a standard-RSK-radius-pure
BK cell need not remain standard-RSK-radius-pure after coordinate
conjugation.

Coordinate relabeling does preserve:

* set ranks and inclusion;
* unions and intersections;
* physical pair-flip/OR relations;
* the rank endpoints and lengths of symmetric chains already constructed
  before relabeling.

Accordingly a completed block can carry its abstract chain-radius label
through conjugation.  What cannot be asserted is that the conjugated middle
vertices still lie in one standard binary-RSK shape class.

## 7. The catalog does not yet solve joint capacity

Theorem 2 says that for each fixed target `S`, its empirical type over the
same polynomial matching multiset approximates the random-matching law.
This simultaneous marginal statement is useful, but it does not provide:

* joint pseudorandomness for several targets;
* a matching between actual middle sources and shadow targets;
* a choice assigning each middle vertex to only one catalog partition;
* control of full block-shadow multiplicity, which depends on orientations,
  direction orders, and within-pair coordinate choices, not only on
  `phi_P`.

Indeed, every perfect matching has exactly `V_f` middle sets and `T_(f,q)`
lower targets of type `f`.  Across `K` full catalog copies these totals are
still

\[
                          K V_f,qquad K T_{f,q}.      \tag{7.1}
\]

Thus taking all catalog copies uniformly does not erase the type-capacity
imbalance.  Mixing can potentially route an individual set through a more
favorable matching, but proving that a simultaneous nonuniform routing
exists is precisely an additional allocation theorem.

There is also a separation between Theorem 2 and Lemma 4.  A perfect
matching does not determine a unique conjugating permutation: pair order,
within-pair swaps, and the arrangement of a block system remain.  Hence the
type catalog cannot be substituted into Lemma 4 to deduce a polynomial
catalog with approximately unit shadow degrees for an arbitrary system.
Lemma 4 uses the full permutation-group average.

## 8. Accepted consequence

The defensible conclusion is:

* polynomially many matchings remove the **pointwise fixed-type rigidity**
  of one native pairing, uniformly over all individual subsets;
* the full coordinate-conjugation average gives exact fractional occurrence
  degree one at every lower and upper target;
* an integral construction still needs a radius-compatible,
  shift-compatible allocation selecting disjoint middle blocks and
  controlling collisions at every required depth.

No asymptotic OR upper bound, shadow-resolved SCD, or polynomial integral
catalog follows from the audited results alone.

## 9. Machine check

`scratch/verify_conjugate_pairing_catalog.py` independently enumerates the
fixed-matching and random-matching laws through `m=5`, tests the full-group
fractional identity on maximally collided lower and upper occurrence
multisets at `m=3`, and verifies the BK-edge radius counterexample.  Its
current output is

```
m=1 matchings=1   subsets=4:    TYPE PASS
m=2 matchings=3   subsets=16:   TYPE PASS
m=3 matchings=15  subsets=64:   TYPE PASS
m=4 matchings=105 subsets=256:  TYPE PASS
m=5 matchings=945 subsets=1024: TYPE PASS
m=3 rank=2 permutations=720: FRACTIONAL PASS
m=3 rank=4 permutations=720: FRACTIONAL PASS
m=2 BK-edge coordinate swap: RADIUS NONINVARIANCE PASS
```
