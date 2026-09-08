# A common de Bruijn vertex fuses source circuits without changing any short cell

**Date:** 2026-08-05  
**Method:** literal word spelling at a shared order-`d` de Bruijn state; no
computation or search  
**Status:** unconditional.  If cyclic source circuits share one literal
ordered `d`-letter history, their Euler splice preserves, occurrence by
occurrence, every cyclic source interval of length at most `d+1`.  Hence a
zero-position common-history fusion preserves all owner windows and the
complete short-cell lower compiler.  Only intervals longer than `d+1`, and
therefore the arbitrary-upper/opening interface, can change.

## 1. Literal setup

Let `Sigma` be any alphabet.  Its letters may themselves be nonempty subsets
of a coordinate set; equality below is literal equality in `Sigma`, not merely
equality of their unions.

Fix `d>=1`.  Let

\[
 H=(h_1,\ldots,h_d)\in\Sigma^d                                      \tag{1.1}
\]

be a vertex of the order-`d` de Bruijn digraph.  For `1<=a<=c`, let `C_a`
be a closed directed walk based at `H`, with appended-letter spelling

\[
 X^{(a)}=(x^{(a)}_1,\ldots,x^{(a)}_{L_a}).                         \tag{1.2}
\]

Assume `L_a>=d`.  Since the walk returns to `H`, its last `d` appended
letters are exactly

\[
 (x^{(a)}_{L_a-d+1},\ldots,x^{(a)}_{L_a})=H.                       \tag{1.3}
\]

The cyclic word spelled by `C_a` is `X^(a)`.  Concatenate the walks at their
common base vertex in any order.  The resulting Euler splice has cyclic
spelling

\[
 X=X^{(1)}X^{(2)}\cdots X^{(c)}.                                  \tag{1.4}
\]

Repeated labelled edges are allowed: this is an occurrence statement.

For a cyclic word `Y`, let `Sub_{<=s}(Y)` denote the multiset of all based
cyclic contiguous subwords of lengths `1,...,s`.

## 2. Exact short-deck preservation

### Theorem 2.1 (common-vertex short-deck fusion)

With the notation above,

\[
 \boxed{
   \operatorname{Sub}_{\le d+1}(X)
     =\mathop{\dot\bigcup}_{a=1}^{c}
        \operatorname{Sub}_{\le d+1}(X^{(a)}) .}
                                                                    \tag{2.1}
\]

The bijection retains the old abstract component label, cyclic base offset,
length and literal letter sequence of every occurrence.  A cut-crossing
occurrence can move physically to the preceding component block in the
concatenated word; its abstract old base label is transported by the
bijection rather than identified with that new physical position.

#### Proof

Fix a component `a`, a based cyclic interval of `X^(a)`, and a length
`ell<=d+1`.

If the interval does not cross the chosen cut immediately before
`x^(a)_1`, it appears literally inside the block `X^(a)` in (1.4).

If it crosses that cut, write it as `uv`, where `u` is a suffix of
`X^(a)` and `v` is a prefix beginning at `x^(a)_1`.  Since `v` is nonempty,

\[
 |u|\le \ell-1\le d.                                                \tag{2.2}
\]

By (1.3), `u` is the corresponding suffix of the common history `H`.
Immediately before the block `X^(a)` in the spliced cyclic word lies the end
of another closed walk based at `H` (cyclically, also when `a=1`).  Its final
`d` letters are again the literal word `H`.  Therefore the same suffix `u`
is immediately followed by the same prefix `v`, so the occurrence `uv`
survives literally.

This maps every based short occurrence of every component into `X`.  For a
fixed length, an interval not crossing a block cut keeps its physical base;
the unique interval crossing into block `a` is assigned the corresponding
old cyclic interval of component `a`.  Hence every final physical base has
one preimage and two old labelled bases cannot collide.  Conversely every
based interval of `X` of length at most `d+1` belongs to the image for the
component containing its first post-cut letter; the same common-history
argument handles a block boundary.  Thus the map is a multiset bijection,
proving (2.1).  \(\square\)

The threshold is sharp.  A crossing interval of length `d+2` may use
`d+1` letters before the cut, and the letter immediately preceding the
common history need not agree in two components.

## 3. Consequence for OR words

Now take `Sigma` to be the nonempty subsets of `[k]` and evaluate a source
subword by union of its letters.  Let `D` be the consecutive-union operator.

### Corollary 3.1 (owner and lower-compiler preservation)

Suppose each component source word `A^(a)` satisfies

\[
                         D^dA^{(a)}=T^{(a)}.                        \tag{3.1}
\]

If the components share the literal history `H` and are fused as above,
then:

1. every rank-`r` owner occurrence (a source interval of length `d+1`)
   survives with the same value;
2. every source-cell occurrence of length at most `d` survives with the same
   value, width and component tag;
3. every occurrence-labelled matching from strict-lower targets to those
   short cells transports verbatim; and
4. the fusion adds no source position.

#### Proof

Apply Theorem 2.1 and then take unions of the literally equal subwords.
Items 1 and 2 use lengths `d+1` and at most `d`, respectively.  The
occurrence bijection transports every matching edge, and (1.4) has length
`sum_a L_a`.  \(\square\)

In particular, no new q1/Johnson condition is needed for the **source-side**
lower compiler.  Consecutive owner sets across a rethreaded component seam
need not intersect in rank `r-1`; the physical length-`d` source cell at that
seam is nevertheless the same literal history cell as before.

### Corollary 3.2 (exact remaining cut exposure)

Under a common-history fusion, any lost OR value must have had all of its
old witnesses on source intervals of length at least `d+2` crossing one of
the chosen component cuts.

Thus, after componentwise factorization and a complete short-cell compiler,
the only remaining witness-preservation problem at the fusion is the long
upper deck (including the eventual linear opening).

#### Proof

Every interval of length at most `d+1` is preserved by Theorem 2.1.  An
interval not crossing a cut is a literal subword of its old component block
in the splice.  Hence only longer cut-crossing intervals can disappear.
\(\square\)

## 4. PBBS application boundary

`MATH_THEOREM_RESIDENT_JOHNSON_FORCED_PAIRS_AND_COMMON_HISTORY_CRITERION_20260805.md`
reduces equality of two length-`d` histories to the explicit containments

\[
 F_j^{(1)}\cup F_j^{(2)}
   \subseteq P_j^{(1)}\cap P_j^{(2)}
 \qquad(0\le j<d).                                                \tag{4.1}
\]

Whenever those containments hold, the history furnished there may be used
as `H` above.  The present theorem then removes the owner/short-lower/common-
compiler rows from the component-fusion interface.  It does **not** prove
(4.1) for the braid and residual PBBS components, and it does not protect:

* arbitrary upper witnesses on intervals longer than `d+1`;
* a later linear opening of the final cyclic word; or
* any typed external route whose validity depends on physical data outside
  the short source cell itself.

Those are separate long-cut and typed-cap gates.
