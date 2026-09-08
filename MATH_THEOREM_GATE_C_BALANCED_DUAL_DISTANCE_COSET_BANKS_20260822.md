# Gate C: balanced three-rank coset banks with growing dual distance

**Status (2026-08-22).**  Every assertion below is proved.  The linear
coset resolution can be chosen to have two properties simultaneously:

1. its kernel avoids every three-rank tour-collision difference; and
2. its dual distance exceeds any `H=o(b/log b)`.

Hence every coset is a three-rank-disjoint coherent-tour bank of size
`2^b/poly(b)`, and its initial states are exactly `H`-wise uniform.  For a
fixed pairing and order, all cosets consequently have identical low-order
target-incidence profiles.  Those profiles can depend on the pairing when
two or more ground coordinates are tested.  The one-coordinate profile is
pairing-independent: every ground coordinate occurs in exactly half of
every bank's middle targets.  Any target-disjoint union of whole banks
therefore preserves coordinate-star balance exactly; the elementary
half-star obstruction cannot be the residual of such a selection.

This is a local invariant, not the missing cross-pairing matching theorem.
Higher-order correlations can still obstruct a near-factor.

Fix odd `b>=3`, one perfect pairing `P={P_0,...,P_(b-1)}`, and one directed
cyclic order.  Let `T(x)`, `x in F_2^b`, be its coherent tours and put

\[
 M_b=2b^3+8b^2-16b.                                    \tag{0.1}
\]

As in the three-rank Cayley audit, there is a collision set
`B subseteq F_2^b\setminus{0}` with

\[
                         |\mathcal B|\le M_b,           \tag{0.2}
\]

such that two different state tours share a target at rank `b-1`, `b`, or
`b+1` if and only if their XOR lies in `B`.

## 1. Simultaneous primal and dual separation

Let the integer `H=H_b` satisfy

\[
                         1\le H=o(b/\log b),             \tag{1.1}
\]

and put

\[
                         r=\left\lceil\log_2(4M_b)\right\rceil.  \tag{1.2}
\]

For all sufficiently large `b`, one has `r<b`.

### Theorem 1.1 (balanced separating code)

There is a full-rank linear map

\[
                         A:\mathbb F_2^b\longrightarrow\mathbb F_2^r    \tag{1.3}
\]

such that, for `C=ker A`,

\[
 \boxed{\mathcal C\cap\mathcal B=\varnothing,
        \qquad d(\mathcal C^\perp)>H.}                 \tag{1.4}
\]

#### Proof

Choose the `r` rows of `A` independently and uniformly in `F_2^b`.  For a
fixed nonzero `h`, `Pr(Ah=0)=2^(-r)`, so

\[
 \Pr(\ker A\cap\mathcal B\ne\varnothing)
 \le M_b2^{-r}\le {1\over4}.                           \tag{1.5}
\]

For a fixed nonzero row coefficient `u in F_2^r`, the vector `uA` is
uniform in `F_2^b`.  Therefore

\[
 \Pr\bigl(\exists\,0\ne u:\operatorname{wt}(uA)\le H\bigr)
 \le (2^r-1)2^{-b}\sum_{j=0}^H{b\choose j}.            \tag{1.6}
\]

The standard estimate

\[
                         \sum_{j=0}^H{b\choose j}
                         \le(H+1)(eb/H)^H              \tag{1.7}
\]

and (1.1) make the logarithm of the right side of (1.6) equal to
`-b+o(b)`, because `r=O(log b)`.  It is therefore below `1/4` for all
sufficiently large `b`.  With positive probability neither bad event
occurs.  The second event includes `uA=0`, so its failure also says that
the rows have full rank.  Their span is `C^perp`, proving (1.4).
\(\square\)

Every coset of `C` has exactly

\[
                         |\mathcal C|=2^{b-r}
                         \ge {2^b\over8M_b}             \tag{1.8}
\]

states.  The first half of (1.4) makes its tours jointly target-disjoint at
all three central ranks.  The same kernel has no words of weight one or
two, so its cosets still give the exact fourfold middle resolution.

## 2. Exact `H`-wise state uniformity

### Lemma 2.1 (dual distance and projections)

For every coordinate set `J subseteq[b]` with `|J|<=H`, the projection of
`C` onto `F_2^J` is surjective.  Consequently every pattern on `J` occurs
exactly `|C|/2^|J|` times in every coset of `C`.

#### Proof

If the projection were not surjective, a nonzero linear functional on
`F_2^J` would annihilate it.  Extending that functional by zero outside
`J` would give a nonzero word of `C^perp` of weight at most `H`, contrary
to (1.4).  A surjective linear projection has equal-sized fibers, and
translation gives the coset statement. \(\square\)

## 3. Coset-independent low-order target loads

Index the `q=b(b-1)` middle targets of one tour by their ordered empty and
doubled pairs `(t,i)`.  For a fixed index, every split pair `P_j` contributes
the selected bit

\[
                         x_j+c_{t,i}(j),                 \tag{3.1}
\]

where the constant is independent of `x`; the empty and doubled pairs do
not depend on the corresponding state bits.

Fix a ground-coordinate set `S subseteq Omega` with `|S|<=H`.  For one
index `(t,i)`, the condition that its middle target contain `S` is either
impossible, automatic on some exceptional pairs, or prescribes one state
bit for each split pair met by `S`.  It prescribes at most `|S|<=H` bits.
Lemma 2.1 therefore shows that its number of solutions in a coset is
independent of the coset.  Summing over all `(t,i)` proves:

### Theorem 3.1 (balanced low-order middle profiles)

For every `S subseteq Omega` with `|S|<=H`, every coset bank for the fixed
pairing and order contains the same number of middle targets containing
`S`.  This common number is the average over all `2^b` initial states for
that pairing and order; for `|S|>=2` it need not be independent of the
pairing.

The same assertion holds separately at ranks `b-1` and `b+1`: their fixed
pair-occupancy signatures again make containment of `S` a system of at
most `|S|` state-bit prescriptions.  Since each coset bank is rankwise
target-disjoint, these occurrence counts are counts of distinct targets.

For one coordinate `a in P_j`, the middle count is especially simple.  Of
the `q` ordered indices, `b-1` have `P_j` empty, `b-1` have it doubled, and
`(b-1)(b-2)` have it split.  The three contributions per state average to

\[
 0+(b-1)+{(b-1)(b-2)\over2}={q\over2}.                 \tag{3.2}
\]

Thus every coset bank `Z` of size `|C|` satisfies

\[
 \boxed{|{T\in Z:a\in T\}|={q|\mathcal C|\over2}}     \tag{3.3}
\]

for every ground coordinate `a`.  A target-disjoint union of whole banks
has the same exact half-star balance, and so does its middle residual.

## 4. Scope

Theorem 3.1 supplies a deterministic within-pairing invariant through every
fixed order `H`: coset choice cannot bias any target statistic depending on
at most `H` initial pair bits.  Across different pairings only the
one-coordinate consequence is automatically common.  In particular the
known coordinate-star edge-free residual cannot be generated by a
target-disjoint selection of whole banks.

This does not prove that a compatible bank remains inside every residual
having those low-order balances.  Nor does it select disjoint banks across
different pairings, control literal windows at every offset, or prove SCD
extendability.  The immediate open theorem remains a cross-pairing
three-rank bank near-factor, now with an exact growing family of invariants
available for its nibble or absorption argument.

The companion checker
`scratch/verify_gate_c_balanced_dual_distance_coset_banks_20260822.py`
constructs the exact collision set from pair-occupancy signatures, finds a
finite separating map with dual distance three, and verifies the algebraic
conditions and the exact one-coordinate load formula.
