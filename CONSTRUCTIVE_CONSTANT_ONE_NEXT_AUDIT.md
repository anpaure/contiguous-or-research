# Audit of the thin four-box construction and sorted-side corollary

## 1. Verdict

Theorems 1--4 and Corollary 4.1 of
`CONSTRUCTIVE_CONSTANT_ONE_NEXT.md` are correct.  In particular, after
sorting

\[
                         h\le a\le b\le c,
\]

the construction genuinely gives

\[
 \boxed{
 g_4(h,a,b,c)
 \le(h+1)(a+1)(b+c+1)-1.}                         \tag{1.1}
\]

Consequently, for every fixed `delta in (0,1]`, the uniform local
subcritical estimate

\[
 g_4(\boldsymbol\ell)
 \le w(\boldsymbol\ell)+O((1+S)^{3-\delta})        \tag{1.2}
\]

holds throughout the exact regime

\[
             (h+1)(a+1)\le(S+1)^{2-\delta}.        \tag{1.3}
\]

There is no missing permutation factor, zero-side exception, or exponent
loss.  The product in (1.3) is the product of the two shortest augmented
side lengths.  It is also the best bound obtainable by merely choosing
different slice and hook coordinates in Theorems 3--4.

This does not by itself settle the four-box aggregation theorem.  Balanced
height tuples normally have all four heights on the same scale, so their two
shortest augmented sides have product of order `(S+1)^2`, not
`O((S+1)^(2-delta))`.  The sorted thick sector is therefore a real remaining
case, not a measure-zero bookkeeping artifact.

Sections 6--8 of the source concern the separate triangular fold.  They are
outside the requested Theorems 1--4 audit and are not certified by this note.

## 2. Definitions and zero bookkeeping

For

\[
 Q(\boldsymbol\ell)=\prod_i[0,\ell_i],
\]

`g_t(bold ell)` counts a word of **nonzero** product points whose nonempty
contiguous coordinatewise maxima contain every nonzero point.  This
convention is handled consistently.

When all side lengths are zero, the box has no nonzero target and the empty
word has length zero.  Formula (1.1) gives zero.  When only some sides vanish,
the hook and slicing constructions below remain valid without a separate
argument.

Deleting a zero entry from a word preserves every nonzero interval maximum:
remove the zero from the interval and join the remaining two pieces.  They
become contiguous after deletion, and the zero contributed nothing.  This
justifies every `-1` in the construction.

## 3. Audit of Lemma 1: one chain rectangle

Let

\[
 C=(c_0<\cdots<c_p),\qquad D=(d_0<\cdots<d_q).
\]

The proposed word is

\[
 (c_p,d_0),(c_{p-1},d_0),\ldots,(c_0,d_0),
 (c_0,d_1),\ldots,(c_0,d_q).                       \tag{3.1}
\]

It has `(p+1)+q=p+q+1` entries.  For target `(c_i,d_j)`, begin at the unique
descending occurrence `(c_i,d_0)` and end at `(c_0,d_j)`, interpreting the
central entry as the endpoint when `i=0` or `j=0`.  Along this interval the
first coordinate never exceeds `c_i` and attains it at the beginning; the
second never exceeds `d_j` and attains it at the end.  The interval maximum
is exactly the target.

If `(c_0,d_0)` is global zero, deletion preserves all nonzero witnesses as
described in Section 2.  Lemma 1 is therefore valid also for `p=0` or `q=0`.

## 4. Audit of Lemma 2: the hook decomposition

Assume `0<=b<=c`.  For `0<=t<=b`, define

\[
 \begin{split}
 D_t={}&(t,0),(t,1),\ldots,(t,c-t),\\
      &(t+1,c-t),\ldots,(b,c-t).
 \end{split}                                      \tag{4.1}
\]

Every displayed step increases one coordinate by one, so each `D_t` is a
saturated chain.  Its first rank is `t`, its last rank is `b+c-t`, and their
sum is `b+c`; hence it is symmetric.

For a cell `(x,y)`:

* if `y<=c-x`, it lies in the vertical part of `D_x`;
* if `y>c-x`, then `t=c-y` satisfies `0<=t<x<=b`, and the cell lies in the
  horizontal part of `D_t`.

The alternatives are disjoint and unique.  Thus the hooks partition the
entire `(b+1)(c+1)`-cell rectangle.  The assumption `b<=c` guarantees
`c-t>=0` for every hook.  Lemma 2 is correct in every degenerate case as
well, including `b=0`.

## 5. Audit of Theorem 3: the three-box word

Pair the chain `[0,a]`, which has `a+1` elements and `a` edges, with every
hook `D_t`.  Lemma 1 uses

\[
                             a+|D_t|
\]

entries for that chain rectangle.  Since the `b+1` hooks partition the
`(b+1)(c+1)` rectangle,

\[
 \sum_{t=0}^b(a+|D_t|)
 =(b+1)a+(b+1)(c+1)
 =(b+1)(a+c+1).                                    \tag{5.1}
\]

Every three-box target belongs to exactly one hook rectangle and retains its
internal Lemma 1 witness after the gadgets are concatenated.  The only
global-zero occurrence is the central entry of the `D_0` gadget.  Deleting
it yields

\[
 \boxed{g_3(a,b,c)\le(b+1)(a+c+1)-1},\qquad b\le c. \tag{5.2}
\]

No witness crosses a gadget boundary, so concatenation creates no
contamination issue.  The constructor does work proportional to the emitted
word length.

### Best permutation for a sorted triple

Let `x<=y<=z`.  Applying (5.2) with `x` as the hook-count side gives

\[
                         (x+1)(y+z+1)-1.            \tag{5.3}
\]

This can be obtained either by pairing the chain of height `y` with hooks in
`[0,x]x[0,z]`, or by pairing the chain of height `z` with hooks in
`[0,x]x[0,y]`.

The only other distinct choice has hook-count side `y` and length

\[
                         (y+1)(x+z+1)-1.
\]

The difference before the common `-1` is

\[
 (y+1)(x+z+1)-(x+1)(y+z+1)=z(y-x)\ge0.            \tag{5.4}
\]

Thus (5.3) is the best coordinate permutation available from Theorem 3.

## 6. Audit of Theorem 4: slicing a fourth side

Choose a fourth coordinate of height `h`.  Let a three-box constructor have
length

\[
                         L=K-1,
 \qquad K=(b+1)(a+c+1).
\]

Embed one copy at each constant fourth-coordinate value `s=0,...,h`.

* At `s=0`, the omitted local origin is global zero and need not be restored.
* At each `s>0`, the target `(0,0,0,s)` is nonzero, so prepend exactly that
  literal entry.  Every target with a nonzero first-three-coordinate part
  retains its internal three-box witness.

Different slices need not interact.  Their concatenation is universal and
has length

\[
 (h+1)(K-1)+h=(h+1)K-1.                           \tag{6.1}
\]

Therefore

\[
 \boxed{
 g_4(h,a,b,c)
 \le(h+1)(b+1)(a+c+1)-1},\qquad b\le c.            \tag{6.2}
\]

The proof remains valid for `h=0` and for zero sides in the three-box
factor.

## 7. Independent derivation of the sorted-side corollary

Sort the heights as

\[
                         h\le a\le b\le c.
\]

Slice the height-`h` coordinate.  On the remaining triple, use `a` as the
hook-count side and pair the hooks with either of the other coordinates.
Equation (5.3) gives three-box length

\[
                         (a+1)(b+c+1)-1.
\]

Substitution into (6.1) proves (1.1).

Equivalently, in the variable order of Theorem 3, substitute

\[
                  (a_{\rm chain},b_{\rm hook},c_{\rm hook})=(c,a,b).
\]

The hook condition `a<=b` is exactly the sorted-side hypothesis.

### Audit over all slice choices

The same bound results if the height-`a` coordinate is sliced and `h` is the
hook-count side of the remaining triple.  Slicing `b` instead gives, after
removing the common factor `h+1`,

\[
 (b+1)(a+c+1),
\]

which exceeds `(a+1)(b+c+1)` by

\[
                              c(b-a)\ge0.           \tag{7.1}
\]

Slicing `c` gives `(c+1)(a+b+1)`, exceeding it by

\[
                              b(c-a)\ge0.           \tag{7.2}
\]

Thus the product of the two shortest augmented sides in (1.1) is not an
accidental coordinate choice; it is the optimum of this slice-and-hook
scheme.

## 8. Audit of the enlarged subcritical regime

Put

\[
                         S=h+a+b+c.
\]

Since

\[
                         b+c+1\le S+1,
\]

condition (1.3) and the exact construction give

\[
 \begin{aligned}
 g_4(h,a,b,c)
 &\le(h+1)(a+1)(b+c+1)-1\\
 &\le(S+1)^{2-\delta}(S+1)-1\\
 &<(S+1)^{3-\delta}.                               \tag{8.1}
 \end{aligned}
\]

Because `w(bold ell)>=0`, (8.1) implies the required form

\[
 g_4(\boldsymbol\ell)
 \le w(\boldsymbol\ell)+1\cdot(S+1)^{3-\delta}.   \tag{8.2}
\]

The constant is uniform over all sorted height vectors, including zeros and
arbitrarily unequal sides.  This is exactly the hypothesis needed by the
subcritical aggregation theorem on this regime.

The older one-short-side condition

\[
                         h+1\le(S+1)^{1-\delta}
\]

is a special case, because `a+1<=S+1` then implies (1.3).

Conversely, the complement of the certified regime is precisely

\[
             (h+1)(a+1)>(S+1)^{2-\delta}.          \tag{8.3}
\]

Since `h<=a`, this implies

\[
                         a+1>(S+1)^{1-\delta/2};    \tag{8.4}
\]

and since `a+1<=S+1`, it also implies

\[
                         h+1>(S+1)^{1-\delta}.      \tag{8.5}
\]

These are useful consequences, but they do not make the four sides
comparable by constant factors.  The source correctly retains an unequal
thick-sector lemma rather than reducing to equal cubes.

## 9. Aggregation scope

The subcritical aggregation theorem requires a uniform bound for every
height vector.  Corollary 4.1 supplies that bound only on (1.3); a fallback
is still needed on (8.3).

Typical balanced-block SCD chain heights are of order `sqrt(k)`.  For four
independent blocks their ordered heights generally all have this same scale,
so

\[
 (h+1)(a+1)=\Theta(k),qquad (S+1)^2=\Theta(k).
\]

There is no fixed polynomial saving on the product in the generic thick
case.  Correspondingly, for an equal four-box of side `m`, (1.1) is
`Theta(m^3)`, the critical rather than subcritical exponent.  The result is
a substantial exact reduction of the local theorem, not by itself a proof
of `nu(k)=(1+o(1))W(k)`.

## 10. Final ledger

Certified:

* the chain-rectangle gadget and deletion of its unique zero;
* the explicit hook SCD of every unequal two-chain rectangle;
* `g_3(a,b,c)<=(b+1)(a+c+1)-1` for `b<=c`;
* the slice construction for every fourth-side height, including zero;
* the sorted bound `(h+1)(a+1)(b+c+1)-1`;
* optimality of that coordinate choice within the stated scheme; and
* the enlarged product regime `(h+1)(a+1)<=(S+1)^(2-delta)`.

Not certified here:

* the triangular-fold claims in Sections 6--8;
* the open thick-sector lemma; or
* any global constant-one theorem without that remaining local input.

