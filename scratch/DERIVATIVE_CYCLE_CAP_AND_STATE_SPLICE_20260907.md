# Derivative cycles: exact cap accounting and state splices

Date: 2026-09-07.  This note audits whether general cyclic linearization can
improve the independent `2H` overhead in the centered-square band compiler.
It cannot do so by itself.  The note also gives an exact sufficient splice
criterion under which the beginning of the next component replaces some of
the copied derivative prefix.  It does not construct a family satisfying
that criterion and does not prove coefficient one.

## 1. Exact derivative cap size

Fix a centered square pair of side `ell<=b`.  Its cyclic source word is a
partition of the ground set into `m=2ell` nonempty blocks

\[
 A=(F,x_1,\ldots,x_{\ell-1},G,y_{\ell-1},\ldots,y_1),
 \qquad |F|=|G|=b-\ell+1,                            \tag{1}
\]

where the displayed `x` and `y` blocks are singletons.  Let `0<=H<ell`,
put

\[
 p=\ell-H,
 \qquad B_i=\bigcup_{j=0}^{p-1}A_{i+j}\quad(i\bmod 2\ell),          \tag{2}
\]

and regard `B` as a cyclic word of period `m`.  A `B`-interval of length
`r` is the same union as the corresponding `A`-interval of length
`p+r-1`.  Hence all square targets in ranks `b-H,...,b+H` have designated
`B`-witnesses of lengths `1,...,2H+1`.

Because `p<=ell`, a `p`-block source interval contains at most one cap.
If it contains a cap, its cardinality is

\[
 (b-\ell+1)+(p-1)=b-H;                              \tag{3}
\]

if it contains no cap, its cardinality is `p<=b-H`.  Thus

\[
 \boxed{\max_i|B_i|=b-H,\qquad\bigcup_iB_i=[2b].}    \tag{4}
\]

The general cyclic-linearization estimate therefore gives length at most

\[
             2\ell+b+H-1,                           \tag{5}
\]

namely cap-aware overhead `b+H-1`.

For this partition source one can calculate the actual scan in that proof.
Choose a largest derivative letter `Z=B_s` and cut immediately after it.
The source blocks outside `Z` are the `m-p=ell+H` consecutive blocks on the
complementary source arc.  As the derivative window advances after the
cut, exactly the next one of these source blocks appears for the first
time.  Therefore the scan has exactly `ell+H` nonempty fresh blocks and
appends all but the last.  Its exact output length is

\[
 \boxed{2\ell+(\ell+H-1)=3\ell+H-1.}                \tag{6}
\]

This is smaller than (5) when `ell<b`, because the other large cap is one
fresh block rather than `b-ell+1` singleton blocks.  It is nevertheless no
better than the existing band-only unwrapping

\[
                         2\ell+2H.                  \tag{7}
\]

Indeed, (6) minus (7) is `ell-H-1>=0`, with equality only at
`ell=H+1`.  Thus applying arbitrary cyclic linearization after the OR
derivative removes no compiler gate and gives no asymptotic saving.

## 2. Exact direct-continuation splice criterion

There is one legitimate way for a following component to save copied
letters.  The following statement applies to arbitrary cyclic set-words,
not just square derivatives.

Let `C=(C_0,...,C_(m-1))` be cyclic, let `1<=R<=m`, and suppose only its
cyclic intervals of length at most `R` must be retained.  Cut after
`C_(m-1)` and write

\[
 P_r=\bigcup_{j=0}^{r-1}C_j,\qquad P_0=\varnothing.
\]

Let `D=(D_0,D_1,...)` be the beginning of the next component and put

\[
 Q_s=\bigcup_{j=0}^{s-1}D_j,\qquad Q_0=\varnothing.
\]

Choose `0<=d<=R-1` and set `a=R-1-d`.  After the full period of `C`, copy
only `C_0,...,C_(a-1)` and then begin `D`.  Every designated wrapping
interval of `C` of length at most `R` survives by direct continuation if

\[
 \boxed{
 C_{m-1}\cup P_a\cup Q_s
   =C_{m-1}\cup P_{a+s}\qquad(1\le s\le d).}         \tag{8}
\]

Proof.  Prefix lengths at most `a` use the literal copied prefix.  A
wrapping interval using `a+s` prefix positions instead meets
`C_0,...,C_(a-1),D_0,...,D_(s-1)`.  Its old suffix contains `C_(m-1)`, so
(8) makes its union unchanged.  Conversely, the old interval consisting
of `C_(m-1)` followed by `a+s` prefix letters shows that (8) is necessary
for this particular direct-continuation realization. `square`

For centered-square derivatives take `R=2H+1`.  A junction satisfying (8)
saves exactly `d` of the usual `2H` copied letters.  Chaining `t`
components with junction savings `d_1,...,d_(t-1)` and unwrapping the last
component normally gives total length

\[
 \boxed{
 2\sum_i\ell_i+2Ht-\sum_{i=1}^{t-1}d_i.}            \tag{9}
\]

All witnesses asserted here remain literal intervals.  Equation (9) is a
compiler theorem conditional on the displayed state equalities, not a
selection theorem.

Condition (8) matches a whole nested state, not merely one cap.  Equality
of `C_(m-1)` with a cap or equality of its cardinality does not suffice:
already `s=1` requires the same union after adding the first next-component
letter.

## 3. The state for a square derivative

The condition has a transparent source-block form.  Reindex (2) so that

\[
 Z=B_{-1}=A_{-1}\cup A_0\cup\cdots\cup A_{p-2}
\]

precedes the cut.  Then

\[
 \boxed{
 Z\cup P_r=\bigcup_{j=-1}^{p+r-2}A_j.}              \tag{10}
\]

Thus each further required state introduces exactly the next source block
`A_(p+r-2)`.  When `2H<=ell-1`, the cut can be placed so that `Z` contains
a cap and all of the next `2H` fresh blocks are singletons.  In that useful
orientation the state to be supplied is precisely a rank-by-rank nested
chain

\[
 Z\subset Z+x_1'\subset\cdots\subset
 Z+\{x_1',\ldots,x_{2H}'\}.                         \tag{11}
\]

Consequently a full zero-copy junction is possible only when the first
`2H` cumulative unions of the next derivative component reproduce (11)
modulo `Z`, in the sense of (8).  This can be substantially weaker than
letterwise equality, because coordinates already in `Z` are masked, but it
is much stronger than matching a cap or a phase label.

The criterion gives a precise target for a correlated component selection:
average compiler overhead falls below `2H` exactly to the extent that
positive-length terminal states can be paired with compatible initial
states.  Neither the fixed-four adjacent matching nor middle-slot phase
labels currently enforce these nested equalities.  No saving may therefore
be charged from those constructions without an additional state-matching
argument.

## 4. Scope

The necessity assertion in Section 2 is only for preserving each broken
cyclic witness by the displayed direct continuation.  A target might have
an unrelated witness elsewhere in a larger global word, so (8) is not a
lower bound on unrestricted words.  Conversely, whenever (8) holds, the
saving in (9) is unconditional and requires no cleanliness or singleton
hypothesis.

The older erosion/dilation compiler already handles arbitrary chronologies
under its positive-run condition.  The result here does not replace or
strengthen that coverage theorem; its new content is the exact cap
calculation (4)--(7) and the auditable junction-state accounting (8)--(11).
