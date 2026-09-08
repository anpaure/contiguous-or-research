# Long centered squares: an independent block compiler and integral gate

Date: 2026-09-07. The coefficient-one theorem is still open. This note
proves a literal compiler for a specific proposed integral cover; it does
not assert that the required cover has been selected.

## 1. Arbitrary-set derivative compiler

Let `A_0,A_1,...` be nonempty sets. Fix integers `L>=1` and `1<=p<=u`.
Suppose the source segment through index `L+u-2` is available. Output

\[
 B_j=\bigcup_{v=j}^{j+p-1}A_v,
 \qquad 0\le j<L+u-p.
\]

For every `0<=i<L` and `p<=s<=u`,

\[
 \bigcup_{j=i}^{i+s-p}B_j
       =\bigcup_{v=i}^{i+s-1}A_v.                       \tag{1}
\]

Indeed the source intervals `[j,j+p-1]` on the left have successive starts
and their union is exactly `[i,i+s-1]`. The last output index used is at
most `L+u-p-1`. Every output letter and every witnessing interval is
nonempty. No singleton or cleanliness hypothesis is needed. In particular,
a cyclic source of period `L` can be read periodically in this formula.

## 2. The square and its exact cyclic witnesses

Put `k=2b`. Fix `1<=ell<=b` and partition the ground set into

\[
 F\ \dot\cup\ G\ \dot\cup\ X\ \dot\cup\ Y,
 \quad |F|=|G|=b-\ell+1,
 \quad X=(x_1,\ldots,x_{\ell-1}),\quad
 Y=(y_1,\ldots,y_{\ell-1}).
\]

Here `X,Y` are ordered lists, with all displayed coordinates distinct.
Write `X_[i]={x_1,...,x_i}` and similarly for `Y_[j]`, allowing empty
prefixes. Define the centered square and its complement family by

\[
 R=\{F\cup X_{[i]}\cup Y_{[j]}:0\le i,j<\ell\},
 \qquad R^c=\{[2b]\setminus S:S\in R\}.               \tag{2}
\]

This is a product of two saturated length-`ell` chains on complementary
supports: distribute `F,G` arbitrarily between the supports of `X,Y`.
Its rank center is `b`, regardless of this distribution. The two families
are disjoint because every member of `R` contains the nonempty set `F`
and every member of `R^c` omits `F`.

Take the following cyclic word of `2ell` nonempty set-valued letters:

\[
 (F,\{x_1\},\ldots,\{x_{\ell-1}\},
       G,\{y_{\ell-1}\},\ldots,\{y_1\}).              \tag{3}
\]

A target `F union X_[i] union Y_[j]` is the union of the arc consisting
of the last `j` letters before `F`, the letter `F`, and the first `i`
letters after `F`. It has rank `b-ell+1+i+j` and this arc has length
`1+i+j`. Its complement is witnessed by the complementary arc through
`G`, of length `2ell-1-i-j`.

It follows in both orientations that **every rank-`b+q` target in
`R union R^c` has a cyclic witness of exactly `ell+q` letters**. All these
lengths are between `1` and `2ell-1`. This assertion concerns designated
targets; other windows may contain both caps and have different ranks.

There is an exact purity range. A proper cyclic interval containing neither
cap lies in one singleton gap and has rank at most `ell-1`. An interval
containing both caps also contains one entire singleton gap and has rank
at least `2b-ell+1`. Every other interval contains exactly one cap and
belongs to `R union R^c`. Consequently at every rank
`ell<=s<=2b-ell`, the cyclic word's full rank support is exactly that of
`R union R^c`, including all unintended witnesses.

## 3. Independent linearization of every square

Fix `0<=H<ell`. Apply (1) to (3), with

\[
 L=2\ell,\qquad p=\ell-H,\qquad u=\ell+H.
\]

The resulting nonzero linear block has exactly

\[
                    \boxed{2\ell+2H}                  \tag{4}
\]

letters and realizes all the targets of (2) with rank in `[b-H,b+H]`.
If also `H<=b-ell`, its support at these ranks is exactly the designated
square support: every interval of derivative letters is a contiguous source
union by (1), and a source interval of at least one period has full rank.

Now let `t` such square pairs, with lengths `ell_i>H`, be selected
integrally. Their splits, fixed parts and coordinate orders can all vary.
Set

\[
 M=2\sum_{i=1}^t\ell_i,
 \quad h_q=\binom{2b}{b+q}
   -\left|\binom{[2b]}{b+q}\cap\bigcup_i(R_i\cup R_i^c)\right|.
\]

Concatenate the independent blocks and append one set-valued letter for
each missing band target. Every designated witness stays within its own
block, so the total band-covering length is at most

\[
              \boxed{M+2Ht+\sum_{|q|\le H}h_q.}       \tag{5}
\]

There is no shared-chain, Euler-tour, or common-support requirement in
(5). If `ell_min=min_i ell_i`, then `2Ht<=HM/ell_min`.

For clarity about the final implication, the far-rank bridge repair already
proved in master Appendix A.4 has length

\[
 O\left((1+H/\sqrt b)e^{-H^2/(16b)}W(2b)\right)+O(b)
\]

for `sqrt(b)<=H<=b-2`, and covers all targets with rank distance at least
`H` from the middle. Thus the following integral selection conditions
would prove coefficient one:

\[
 M\le(1+o(1))W(2b),\qquad
 \sqrt b\ll H\ll\ell_{\min},\qquad
 \sum_{|q|\le H}h_q=o(W(2b)).                          \tag{6}
\]

The repair bound is an input from the master, not reproved here. The
construction and proof of (1)--(5) are complete in this note.

## 4. Exact cross-rank incidence and its limitation

For `0<=q<ell`, one square has `ell-q` rank-`b+q` targets. Each such
target contains exactly `q+1` middle targets of that square: in prefix
coordinates the former has `i+j=ell-1+q`, and its contained middle
indices run from `ell-1-j` to `i`, inclusive. The complementary square
has the same count. There are no cross-orientation containment flags:
each orientation contains its own nonempty fixed cap, `F` or `G`, which
every target of the other orientation omits.

Under uniform coordinate symmetrization let `D_0` be the weight/number of
square pairs containing a fixed middle target, and `lambda_(0,q)` the
weight/number containing a prescribed inclusion flag `T subset U` of
ranks `b,b+q`. Rank-flag transitivity and double counting give

\[
 \boxed{\frac{\lambda_{0,q}}{D_0}
       =\frac{(q+1)(\ell-q)}{\ell\binom bq}.}         \tag{7}
\]

For `q=1`, this is `2(ell-1)/(ell b)`. A pair's full `H`-band support
has exactly

\[
 R_H=2\bigl((2H+1)\ell-H(H+1)\bigr)                 \tag{8}
\]

targets. In the regime (6), the product of (8) and the adjacent-flag ratio
is of order `H ell/b`, which diverges. Therefore an unstructured
growing-uniformity matching theorem that requires
`R_H*(maximum normalized pair codegree)=o(1)`, at the central degree
normalization `D_0`, cannot be justified by these estimates. The unmodified
all-band hypergraph also has unequal degrees across ranks; no regularity
claim is being made. This is a theorem-application obstruction only. It is
not a proof against a correlated integral cover. The nesting structure
would have to be used explicitly.

## 5. A finite fractional band cover with no short-side exception

Here is an exact interface with the companion convex-profile construction.
Use its notation `G_q`, `w_a=G_(a-1)-2G_a+G_(a+1)`, with `m=b`, central
height `M_0=(1+epsilon)W(2b)`, and splice position `z`. Thus `w_(b+1)=1`,
`sum a*w_a=M_0`, and `w_a=0` for `a<z-1`.

Choose integers `0<=H<z-1`, and assume

\[
 B_H=\binom{2b}{b+H}>b+1,\qquad
 \gamma={B_H\over B_H-(b+1)}.
\]

Discard the length-`b+1` atom entirely, do not add either singleton patch,
and give each remaining length-`a` coordinate orbit total weight
`gamma*w_a/2`. Every remaining pair is disjoint and has `z-1<=a<=b`.
Its ordinary total incidence at offset `q` is

\[
 \gamma\sum_{a\le b}w_a(a-|q|)_+
 =\gamma\{G_{|q|}-(b+1-|q|)\}
 \ge\gamma\{B_q-(b+1)\}\ge B_q
 \quad(|q|\le H),                                    \tag{9}
\]

where `B_q=binom(2b,b+q)` and the last inequality uses `B_q>=B_H`.
Coordinate transitivity turns (9) into ordinary fractional coverage of
every individual band target. Its principal charge is exactly

\[
 M_{\rm frac}=\gamma\{M_0-(b+1)\}.                   \tag{10}
\]

Compiling each orbit member by (4), with its fractional weight unchanged,
gives a fractional cover by **actual finite word blocks** whose weighted
length is at most

\[
 \boxed{\left(1+{H\over z-1}\right)
           \gamma\{M_0-(b+1)\}.}                    \tag{11}
\]

This last object is a fractional collection of blocks, not one word.
It cannot be concatenated at fractional cost.

In the fixed-`epsilon` limit followed by sufficiently slow
`epsilon -> 0`, the companion proof gives
`z-1=Theta(sqrt(k/epsilon))`. Choose
`sqrt(k)<<H<<sqrt(k/epsilon)`, also `H=o(k)`. Then `B_H` grows
exponentially in `k`, so `gamma=1+o(1)`, and (11) is `(1+o(1))W(k)`.
This eliminates short-side and within-pair-duplicate caveats from the
fractional band input. It also exhibits the promised literal block for
every possible selected square.

What is still missing is a correlated **integral** selection satisfying
(6), or a different construction achieving the same final word length.
The convex profile and (11) do not supply that selection.

Executable finite checks: `scripts/check_centered_square_compiler_20260907.py`.
