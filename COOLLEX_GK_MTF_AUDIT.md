# Cool-lex versus arbitrary Greene--Kleitman chain extensions

This note tests whether the failure of the canonical Greene--Kleitman
projection can be repaired by using the full maximal-chain fiber of every
Greene--Kleitman chain and ordering the middle sets in cool-lex order.

It cannot.  The obstruction survives even if the bottom and top of every
chain are allowed to be arbitrary ordered partitions, not merely arbitrary
permutations.  For `2m` coordinates, exactly `Cat_m` of the
`binomial(2m,m)` directed cool-lex transitions are even existentially
compatible with one move-to-front update.  Hence the cool-lex cycle breaks
into `(1-o(1))W` pieces.

The proof also gives a cheap exact screen for any other proposed combination
Gray code.

## 1. Greene--Kleitman fibers

Represent a middle set by a balanced binary word, with `1` meaning selected.
Greene--Kleitman pairing matches a `0` with a later `1` by the usual stack
rule.  The unpaired positions, in increasing order, are

\[
                         e_1<\cdots<e_{2d};
\tag{1.1}
\]

the first `d` of them are `1` and the last `d` are `0`.  The chain radius is
`d`.  Let `B` be the selected paired positions and `Z` the unselected paired
positions.  The chain is

\[
 B\subset B+e_1\subset\cdots\subset B+e_1+\cdots+e_{2d}.
\tag{1.2}
\]

Its singleton maximal-chain extensions are exactly the permutations

\[
 \pi=(P,e_1,\ldots,e_{2d},Q),
\tag{1.3}
\]

where `P` is an arbitrary permutation of `B` and `Q` an arbitrary
permutation of `Z`.  Its full ordered-partition fiber is obtained by replacing
`P,Q` by arbitrary ordered partitions of `B,Z`; the star positions remain
singleton blocks in the fixed order (1.1).

The radius also has the height description

\[
 d=\max_{0\le j\le2m}
   \bigl(\#\{i\le j:w_i=1\}-\#\{i\le j:w_i=0\}\bigr).
\tag{1.4}
\]

## 2. The exact queue-discipline test for maximal extensions

Let `C,D` have middle members `X,Y`, and let `Ext(C),Ext(D)` be their
permutation fibers (1.3).

### Lemma 1 (deletion-word criterion)

There are `pi in Ext(C)`, `sigma in Ext(D)` and one singleton update `{b}`
with

\[
                         \sigma=\operatorname {mtf}_b(\pi),
\tag{2.1}
\]

and `X != Y`, if and only if the following hold.

1. `X,Y` are Johnson neighbours, say
   `Y=X-{a}+{b}`.
2. Some `pi in Ext(C)` places `b` after its first `m` positions, some
   `sigma in Ext(D)` starts with `b`, and
   \[
                         \pi-b=\sigma-b
   \tag{2.2}
   \]
   as ordered words.

In particular, if `C` has positive radius `d`, then necessarily

\[
                         a=e_d.
\tag{2.3}
\]

#### Proof

A singleton move-to-front operation deletes `b` from its old position and
inserts it first, preserving the relative order of every other coordinate.
This is exactly (2.2).  Since `b` starts outside the middle prefix and ends
inside it, the new middle prefix drops precisely the old element in position
`m`, proving the Johnson condition.  In (1.3), position `m` is `e_d` whenever
`d>0`, independently of the permutations `P,Q`; this proves (2.3).  The
converse follows by inserting `b` back into the common deletion word.  QED.

Thus bottom/top permutations do provide real freedom, but they cannot change
the queue boundary: every positive-radius source has one forced departure
coordinate.

## 3. Allowing tied bottom and top blocks

The clean existential criterion for the full ordered-partition fibers is the
quotient-chain theorem from `MTF_TRANSVERSAL.md`.  Write the target chain as

\[
 D=(A,A+f_1,\ldots,A+f_1+\cdots+f_{2r}).
\tag{3.1}
\]

When `A` is nonempty, one move from some state exposing `C` to some state
exposing `D` exists exactly when

\[
                         C-A\quad\hbox{and}\quad D-A
\tag{3.2}
\]

are cross-nested.  Equivalently, every member `S` of `C` satisfies the
prefix-fence condition

\[
 S-A\in\{\varnothing,F_1,\ldots,F_{2r}\}
 \quad\hbox{or}\quad
 F_{2r}\subseteq S-A,
 \qquad F_j=\{f_1,\ldots,f_j\}.
\tag{3.3}
\]

If `A` is empty, the identical statement holds after anchoring at `{f_1}`.
This criterion already incorporates every possible splitting and ordering of
the source bottom and top blocks.  It is therefore the appropriate strongest
local test; failure of (3.3) cannot be repaired by a different maximal-chain
extension.

## 4. Cool-lex fails the prefix fence almost everywhere

The cool-lex successor of a balanced word is obtained by finding the shortest
prefix ending in `010` or `011` and rotating that prefix one place to the
right.  Apart from the two boundary words

\[
                         1^m0^m,
 \qquad                  1^{m-1}0^m1,
\tag{4.1}
\]

write the source uniquely as

\[
 w=1^a0^b1\varepsilon v,
 \qquad a\ge0,\quad b\ge1,\quad\varepsilon\in\{0,1\}.
\tag{4.2}
\]

Its successor is

\[
                         s(w)=\varepsilon1^a0^b1v.
\tag{4.3}
\]

### Lemma 2 (cool-lex fence lemma)

For `m>=2`, the Greene--Kleitman chain of `w` is existentially compatible in
one move-to-front step with the Greene--Kleitman chain of `s(w)` if and only
if `s(w)` has radius zero.

#### Proof

If the target radius is zero, its Greene--Kleitman chain is the singleton
`{s(w)}`.  Its minimum is the entire middle set `A=s(w)`, and after quotienting
by `A` the target chain is just `{emptyset}`.  It is cross-nested with every
source quotient, so (3.2) holds.

For the converse, assume the target radius is positive.  Pair `0`--`1` in
the target (4.3) by the stack rule.  Its unmatched `1` positions are exactly
the successive record-up steps of its height walk, and its unmatched `0`
positions are the residual stack at the end.  Let `A` be its paired selected
positions and `F_j` the unmatched-position prefixes from (3.3).

Substitute the inverse rotation (4.2).  The obstruction can be seen at one
explicit coordinate in each case.

* Let `epsilon=1`.  The target is
  `1^(a+1)0^b1v`.  Coordinate `a+1` is a target-only selected coordinate and
  is one of its unmatched record-up steps.  Coordinate `a+b+1` is selected
  only in the source, but in the target it is the final `0` immediately
  preceding the displayed trailing `1`; those two coordinates are paired.
  Hence `w-A` omits an element of the target star set and contains the
  nonstar coordinate `a+b+1`.
* Let `epsilon=0`.  Coordinate `a+b+1` is again selected only in the source,
  and in the target it is the `0` immediately paired with the displayed `1`
  at coordinate `a+b+2`.  Thus `w-A` contains a nonstar coordinate, so it is
  not a star prefix.  Moreover the only target-zero coordinates selected by
  the source are the changed coordinates (coordinate `1`, when `a>0`, and
  coordinate `a+b+1`); both are paired target zeros.  Therefore `w-A`
  contains none of the target's unmatched-zero stars.  Since the positive
  target radius supplies at least one such upper star, `w-A` does not contain
  the full star set either.

In both cases the source member `S=w` violates (3.3).  It remains to check
the two boundary sources in (4.1).

* The successor of `1^m0^m` is `01^m0^(m-1)`.  Source coordinate `1` is a
  paired target zero, while the source gains none of the unmatched target
  zeros at the upper end of the target chain.  Thus its quotient contains a
  nonstar without containing the full star set.
* The successor of `1^(m-1)0^m1` is `1^m0^m`.  The target minimum is empty,
  so apply the anchored form of (3.3), anchoring at its first star.  The
  source centre contains coordinate `2m` while omitting earlier target
  stars.  After removing the anchor it is neither a star prefix nor a set
  containing all remaining stars.

Both boundary targets have positive radius for `m>=2`, and both fail the
prefix fence.  QED.

The case split in the last paragraph is purely the stack algorithm; it does
not assume the canonical order of `B` or `Z`.  That is exactly why the result
survives arbitrary fiber choices.

### Theorem 3 (exact compatible-edge count)

For `m>=2`, exactly

\[
                         \operatorname {Cat}_m
                         =\frac1{m+1}\binom{2m}{m}
\tag{4.4}
\]

directed edges of the cyclic cool-lex order pass the strongest existential
move-to-front test (3.2).

#### Proof

Cool-lex is a cyclic permutation of all balanced words.  By Lemma 2, a
directed edge is compatible exactly when its target has Greene--Kleitman
radius zero.  Radius-zero balanced words are the nonpositive Dyck words, of
which there are `Cat_m`.  Every such word occurs exactly once as a target in
the cycle.  QED.

### Corollary 4 (macroscopic path-cover obstruction)

Let

\[
                         W=\binom{2m}{m}.
\]

Even after arbitrary bottom/top ordered-partition choices, any path cover
which respects the directed cool-lex order has at least

\[
                         W-\operatorname {Cat}_m
                         =\left(1-\frac1{m+1}\right)W
\tag{4.5}
\]

components.

Indeed, the fixed cyclic order has only `Cat_m` usable directed edges, and a
forest on `W` vertices using at most that many edges has at least the number
of components in (4.5).  Initializing or resetting these components already
costs `Omega(W)`.  Thus cool-lex cannot yield a `W+o(W)` OR word through
Greene--Kleitman chain extensions.

The maximal-permutation version is a fortiori impossible, since every
singleton-state transition is one of the ordered-partition transitions
counted above.  Direct enumeration through `m=5` finds still fewer maximal
fiber transitions, as checked by `gk_extension_mtf_test.cpp`.

## 5. A useful screen for other prefix-shift codes

The negative result is specific to pairing cool-lex with the fixed
Greene--Kleitman SCD; it is not a no-go theorem for every prefix-shift Gray
code or every SCD.  It does give two exact filters which should be applied
before pursuing another candidate.

1. **Permutation-state filter.**  A positive-radius source may delete only
   its canonical coordinate `e_d`, by (2.3), and the deletion words must
   agree as in (2.2).
2. **Tied-state filter.**  Even with arbitrary-mask updates and arbitrary
   bottom/top ordered partitions, the source and target quotient chains must
   pass the prefix fence (3.3).

For a proposed cyclic ordering of the `W` chain centres, let `E` be the
number of directed adjacencies passing the appropriate filter.  Every path
cover constrained to that ordering has at least `W-E` components.  A
near-width construction therefore requires

\[
                         E=W-o(W).
\tag{5.1}
\]

Cool-lex has `E=Cat_m=o(W)`, the opposite extreme.  This identifies the
intrinsic failure: the prefix rotation is a perfectly good combination Gray
code, but it almost never preserves the quotient-prefix geometry imposed by
the Greene--Kleitman chain fibers.
