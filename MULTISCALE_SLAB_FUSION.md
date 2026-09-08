# Multiscale slab fusion and its exact barrier

## 1. Outcome

Put

\[
 P_m=[0,m]^4,\qquad L_j=\{x\in P_m:|x|=j\},\qquad
 M_m=|L_{2m}|.
\]

The independent slice fan in `LEX_FACTOR_ITERATION.md` can be fused: all
values of one low coordinate can share one symmetric-chain initialization,
and the overlap of the two low-coordinate slabs can be removed.  The result
is an exact physical word, not only a shadow count.

### Theorem A (fused L-slab completion)

Let

\[
 1\le t\le \left\lfloor {m+1\over2}\right\rfloor,
 \qquad 1\le R\le4m-t,
\]

and define

\[
 \Psi(d)=\left\lceil {d\over2}\right\rceil
          \left(\left\lfloor {d\over2}\right\rfloor+1\right).
\]

There is an explicit nonzero word whose contiguous coordinatewise maxima
contain every point of

\[
                         L_R,L_{R+1},\ldots,L_{R+t}
\]

and whose length is at most

\[
 \boxed{
 |L_R|+t(2m-t+2)(2m+1)-1-m\Psi(t-1).              \tag{1.1}
 }
\]

Relative to the `2t` independent three-box slices, the exact saving is

\[
                  t^2(2m+1)+m\Psi(t-1)+1.          \tag{1.2}
\]

Thus, uniformly for (t=o(m)), the auxiliary cost is

\[
 4tm^2-{9\over4}t^2m+O(tm+t^2),                   \tag{1.3}
\]

where the (O(tm)) term includes the parity error in (Psi(t-1)).
This is a genuine fusion improvement, but it is still

\[
                              \Theta(tm^2).         \tag{1.4}
\]

The latter order cannot be improved by *any* recursion whose missed
central targets are witnessed wholly inside an auxiliary slab word.

For the lower-central band and for Theorem B below, take (R=2m-t).

### Theorem B (sharp separated-slab barrier)

Let (W_R) be the complete coordinate-({1,2}) line spine on (L_R),
and define the central boundary antichain

\[
 \mathcal B_{m,t}=\{y\in L_{2m}:y_1<t\text{ or }y_2<t\}.              \tag{1.5}
\]

For the range in Theorem A,

\[
 \boxed{
 |\mathcal B_{m,t}|
 =tm^2+t(t+2)m+{t(5+3t-5t^2)\over3}.               \tag{1.6}
 }
\]

Suppose a word is formed from (W_R) and an auxiliary physical word (V),
and every target in (mathcal B_{m,t}) is required to have a witness
contained wholly in (V).  The letters of (V) may be organized by an
arbitrary nested, dyadic, overlapping-description, or shared-initialization
slab recursion; only their physical occurrences are counted.  Then

\[
                             |V|\ge|\mathcal B_{m,t}|.                \tag{1.7}
\]

Moreover

\[
 M_m-|L_{2m-t}|
 =t^2m+t-{t(t-1)^2\over2},                         \tag{1.8}
\]

so every such separated construction has total length at least

\[
 \boxed{
 M_m+tm(m+2)-{7t(t^2-1)\over6}.                   \tag{1.9}
 }
\]

For (t=o(m)), this is

\[
                              M_m+(1-o(1))tm^2.     \tag{1.10}
\]

For (t=\alpha m+O(1)), (0<\alpha\le1/2), its excess over width is

\[
             \left(\alpha-{7\over6}\alpha^3\right)m^3+O(m^2),       \tag{1.11}
\]

which is positive.  Hence no internal-slab multiscale recursion can turn
the line spine into a linear-depth (M_m+o(m^3)) construction.  This is a
sharp obstruction for the stated architecture: listing the members of
(mathcal B_{m,t}) literally attains (1.7) for that antichain alone.

The escape has to use intervals which cross the main spine's line seams.
Section 6 gives the exact local portal equation and a precise sufficient
global object.

## 2. The completed line spine

For every ((c,d)\in[0,m]^2), put

\[
 K=R-c-d,\qquad A=\max(0,K-m),\qquad B=\min(m,K).
\]

When (A\le B), form the complete line

\[
 (A,K-A,c,d),(A+1,K-A-1,c,d),\ldots,(B,K-B,c,d).   \tag{2.1}
\]

Concatenating the nonempty lines gives (W_R), a permutation of (L_R).
For (y\in L_{R+s}), the segment with endpoints

\[
                              y-se_1,\qquad y-se_2                 \tag{2.2}
\]

lies in one line and has maximum (y) whenever

\[
                              y_1,y_2\ge s.          \tag{2.3}
\]

If (0\le s\le t) and (2.3) fails, then

\[
                 y_1<t\quad\text{or}\quad y_2<t.    \tag{2.4}
\]

The old construction appended a complete three-box word for every one of
the (2t) coordinate values in (2.4).  We instead cover their union by two
disjoint thick slabs.

## 3. The exact physical slab word

We use one elementary connector.  If

\[
 C=(c_0<c_1<\cdots<c_p),\qquad D=(0<1<\cdots<q)
\]

are chains, write

\[
 (c_p,0),(c_{p-1},0),\ldots,(c_0,0),
 (c_0,1),\ldots,(c_0,q).                            \tag{3.1}
\]

The interval beginning at ((c_i,0)) in the descending part and ending at
((c_0,j)) in the ascending part has maximum ((c_i,j)).  Thus (3.1)
covers (C\times[0,q]) in (p+q+1) letters.  If ((c_0,0)) is the global
zero, deleting it preserves all nonzero witnesses.

For a box

\[
                  [0,h]\times[0,a]\times[0,b]\times[0,c],
                  \qquad h\le a\le b\le c,
\]

the nested hook decomposition gives an explicit symmetric-chain
decomposition of the first three coordinates into

\[
 (h+1)(a+1)-\Psi((h+a-b)_+)                       \tag{3.2}
\]

chains.  Apply (3.1) to each such chain and the last coordinate, then
concatenate.  This is the explicit word of length

\[
 (h+1)(a+1)(b+c+1)-1-c\Psi((h+a-b)_+).             \tag{3.3}
\]

Every witness is the displayed descending-prefix/ascending-suffix interval
inside one connector.  Thus (3.3) supplies both physical letters and exact
max-window witnesses.

Now take the disjoint L-shaped partition

\[
 \begin{split}
 S_1&=\{x\in P_m:0\le x_1<t\},\\
 S_2&=\{x\in P_m:t\le x_1\le m,\ 0\le x_2<t\}.
 \end{split}                                        \tag{3.4}
\]

The first slab is a box with side lengths (t-1,m,m,m).  Formula (3.3)
gives a nonzero universal word of length

\[
                  t(m+1)(2m+1)-1-m\Psi(t-1).        \tag{3.5}
\]

For the second slab, subtract (t) from the first coordinate.  Its side
lengths, in increasing order, are

\[
                         t-1,m-t,m,m.               \tag{3.6}
\]

The assumed bound on (t) makes this order valid, and

\[
                 (t-1)+(m-t)-m=-1,
\]

so (3.2) has no defect term.  The local zero maps to the required global
point ((t,0,0,0)); retain it rather than deleting it.  The resulting word
has length

\[
                         t(m-t+1)(2m+1).            \tag{3.7}
\]

Concatenate (W_R), the word for (S_1), and the translated word for
(S_2).  If (2.3) holds, (W_R) witnesses the target.  If it fails, (2.4)
puts the target in exactly one of the two regions in (3.4), whose universal
word witnesses it internally.  Adding (3.5) and (3.7) proves (1.1).

The old independent cost was (2t(m+1)(2m+1)).  Subtraction gives (1.2).
Since

\[
                         \Psi(t-1)={t^2\over4}+O(t),
\]

expansion gives (1.3).

### Corollary 3.1 (a symmetric linear band, but not near width)

If (2q\le(m+1)/2), use base rank (R=2m-q) and maximum excess (2q).
The same construction, with (t=2q), covers

\[
                         L_{2m-q},\ldots,L_{2m+q}
\]

in the length obtained from (1.1) after replacing (R) and (t) as
stated.  This is an explicit linear-depth construction for (q=\Theta(m)),
but its auxiliary term is (Theta(m^3)); no near-width claim is made.

## 4. Why a dyadic slab hierarchy does not improve this architecture

The defect function has the exact representation

\[
                         \Psi(d)=\sum_{j\ge0}(d-2j)_+.               \tag{4.1}
\]

For positive integers (a,b), termwise comparison in (4.1) gives

\[
              \Psi(a+b-1)\ge\Psi(a-1)+\Psi(b-1).                    \tag{4.2}
\]

Indeed, when both terms on the right are positive their sum is smaller
than the left term by (1+2j); when only one is positive the inequality is
immediate.

Consequently, if the first slab (0\le x_1<t) is split into height bands
of sizes (t_1,\ldots,t_r), (sum t_i=t), and each band receives its own
connector word (3.3), then

\[
 \sum_i\bigl[t_i(m+1)(2m+1)-m\Psi(t_i-1)\bigr]
 \ge t(m+1)(2m+1)-m\Psi(t-1).                      \tag{4.3}
\]

Local-zero corrections only favour the one-piece word: every translated
subslab has a nonzero local origin which must be retained.  Thus a dyadic
or multiscale partition of the coordinate values cannot improve the
one-piece SCD connector bound.  More importantly, the next section shows
that *no* internally witnessed slab recursion can improve its
(Theta(tm^2)) order.

## 5. Exact central antichain tax

Every member of (mathcal B_{m,t}) fails the internal line criterion
(2.3) at (s=t).  We first count this family.

Fix (y_1=a<t).  By complement symmetry in the remaining three
coordinates, the number of solutions to

\[
                 y_2+y_3+y_4=2m-a,qquad0\le y_i\le m,
\]

is the rank-((m+a)) coefficient of the three-box, namely

\[
                  \binom{m+a+2}{2}-3\binom{a+1}{2}.                  \tag{5.1}
\]

If (y_1=a<t) and (y_2=b<t), then (a+b\le2t-2\le m), and the number
of pairs ((y_3,y_4)) of sum (2m-a-b) is (a+b+1).  Therefore

\[
 \begin{split}
 |\mathcal B_{m,t}|
 &=2\sum_{a=0}^{t-1}
   \left[\binom{m+a+2}{2}-3\binom{a+1}{2}\right]
   -\sum_{a,b=0}^{t-1}(a+b+1)\\
 &=tm^2+t(t+2)m+{t(5+3t-5t^2)\over3},             \tag{5.2}
 \end{split}

which proves (1.6).

The family is an antichain.  In a word of length (n), chosen intervals
with pairwise incomparable maxima have distinct left endpoints and distinct
right endpoints: containment of one interval in another would imply
containment of their maxima.  Hence at most (n) members of an antichain
can be represented.  Applying this to the auxiliary physical word (V)
proves (1.7), regardless of how many logical slab gadgets share its
positions.

The rank coefficient at distance (t) from the middle is

\[
 |L_{2m-t}|=\binom{2m-t+3}{3}-4\binom{m-t+2}{3}.    \tag{5.3}
\]

Taking finite differences, or expanding (5.3), gives

\[
 M_m-|L_{2m-t}|=t^2m+t-{t(t-1)^2\over2},           \tag{5.4}
\]

which is (1.8).  Finally (5.2) minus (5.4) is exactly

\[
                    tm(m+2)-{7t(t^2-1)\over6}.     \tag{5.5}
\]

This proves (1.9)--(1.11).

There is a useful quantitative interpretation.  Suppose the letters of
(W_R) are retained and the final word has length (M_m+e).  It has only

\[
                  M_m-|L_R|+e
\]

additional physical positions.  At most that many boundary central targets
can be supplied as new singleton letters.  Every remaining member of
(mathcal B_{m,t}) must use a genuinely non-line interval.  For (t=o(m))
and (e=o(tm^2)), this is ((1-o(1))|\mathcal B_{m,t}|) targets.  Thus a
near-width construction must make portal intervals do essentially all of
the boundary work; a more economical auxiliary universal word is not
enough.

## 6. The exact portal escape

The needed cross-spine mechanism has a simple exact local equation.

### Lemma 6.1 (complementary-line corner portal)

Let (v\in L_R), and let (i,i',j,j') be four distinct coordinates.
Assume the following points are legal:

\[
 A_h=v-he_i+he_{i'}\quad(0\le h\le a),
 \qquad
 B_h=v+he_j-he_{j'}\quad(0\le h\le b).             \tag{6.1}
\]

Place the two line pieces consecutively as

\[
              A_a,A_{a-1},\ldots,A_1,v,B_1,\ldots,B_b.              \tag{6.2}
\]

Then for every (0\le u\le a) and (0\le w\le b), the interval from
(A_u) through (B_w) has maximum

\[
                              v+ue_{i'}+we_j.        \tag{6.3}
\]

#### Proof

On the suffix (A_u,\ldots,v), coordinate (i) is maximized at (v)
and coordinate (i') at (A_u), giving (v+ue_{i'}).  On the prefix
(v,\ldots,B_w), coordinate (j) is maximized at (B_w) and coordinate
(j') at (v), giving (v+we_j).  The other coordinates are fixed.
Taking the maximum of the two pieces gives (6.3).  \(\square\)

One transition between complementary line directions therefore supplies a
whole Cartesian rectangle of upper targets.  It uses the rank-(R) spine
letters themselves; it pays no auxiliary antichain tax.

This suggests the following exact sufficient object.

### Definition 6.2 (bounded-overlap portal braid)

A depth-(t) portal braid on (L_R) is a physical word made from oriented
coordinate-pair line segments such that

1. every point of (L_R) occurs;
2. its total number of occurrences is (|L_R|+E);
3. consecutive complementary segments meet as in (6.2); and
4. every target in (L_R\cup\cdots\cup L_{R+t}) is either the maximum of
   an interval inside one segment or belongs to one of the seam rectangles
   (6.3).

### Proposition 6.3 (portal-braid reduction)

If a depth-(t) portal braid exists with (E=o(m^3)), then the whole band
(L_R,\ldots,L_{R+t}) has a word of length

\[
                           |L_R|+o(m^3)\le M_m+o(m^3).                \tag{6.4}
\]

In particular, a bounded-overlap braid with (E=O(m^2)) settles every
linear depth (t=\Theta(m)) covered by its rectangle tiling.

#### Proof

The word in the definition is already the desired physical word.  Base
targets are singleton letters.  Internal-line targets use their assigned
segments, and portal targets use Lemma 6.1.  The stated occurrence count
gives (6.4).  \(\square\)

This is the correct multiscale target.  A seam with arm lengths (a,b)
supplies ((a+1)(b+1)) portal values and automatically includes every
smaller depth in the same rectangle.  Thus long seams can service all
dyadic scales simultaneously; one must not build an independent word at
each scale.

The remaining theorem is combinatorial rather than algebraic:

> Partition, with only (O(m^2)) repeated endpoints, the rank-(R) layer
> into alternating complementary line segments whose corner rectangles
> tile all line-missed targets.

Raw capacity is sufficient: (Theta(m^2)) seams with arms of order (m)
carry (Theta(m^4)) rectangle cells, the order of the whole upper band.
The unresolved issue is simultaneous assignment without contamination or
large endpoint multiplicity.  This formulation also explains exactly why
the separated slab recursion fails: it throws away the seam rectangles and
re-initializes the same lower-dimensional word at every boundary scale.

## 7. Status

Proved here:

* the explicit fused L-slab word (1.1), with exact physical max-window
  witnesses;
* its exact saving (1.2) over the independent slice fan;
* one-piece optimality inside the partitioned SCD-connector slab class;
* the exact boundary-antichain formula (1.6);
* the sharp separated-slab lower bound (1.9); and
* the exact complementary-line portal equation and reduction.

Not proved here:

* a bounded-overlap portal-rectangle tiling;
* a linear-depth (M_m+o(m^3)) word; or
* a full four-box universal word of width plus lower order.

The mathematical conclusion is nevertheless decisive for the architecture:
multiscale **slab** fusion improves constants but cannot improve the
(tm^2) order.  Multiscale **seam** fusion can escape that barrier because
one physical transition carries a two-parameter family at all smaller
depths.  The next proof attempt should therefore work on the portal-braid
tiling, not on a more elaborate hierarchy of internally universal slabs.
