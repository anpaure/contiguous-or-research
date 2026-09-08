# Interval label swaps create minimum runs, and the one-copy gate is a conjugate double rail

**Date:** 2026-08-06  
**Method:** exact Johnson-boundary algebra and one-copy owner accounting; no
computation or search  
**Status:** unconditional local surgery and sharp one-copy obstruction.  A
conjugate two-rail occurrence would install a singleton ticket with only
four boundary-edge changes.  Existence and simultaneous packing of those
rails in the canonical PBBS factor remain open.

## 1. One crossing rectangle

Let

\[
                         T=(T_i)_{i\in\mathbb Z_W}
\]

be a cyclic simple rank-`r` Johnson chronology.  Fix distinct coordinates
`x,y` and put `tau=(x y)`.

Choose a proper interval

\[
                         I=[c,b]
\tag{1.1}
\]

and an earlier index `a<c`.  Assume:

1. `x` has the positive run `[a,b]`;
2. `y` belongs to `T_(c-1)` and is absent from every
   `T_c,...,T_(b+1)`;
3. the transition `T_(c-1)->T_c` deletes `y`; and
4. the transition `T_b->T_(b+1)` deletes `x` and does not insert `y`.

The membership conditions already force the two declared deletions.  They
are listed to fix the transition convention.

Define

\[
 T_i'=
 \begin{cases}
   \tau T_i,&i\in[c,b],\\
   T_i,&i\notin[c,b].
 \end{cases}
\tag{1.2}
\]

### Theorem 1.1 (one-rail endpoint swap)

Every transition of `T'` is a nonloop Johnson transition.  The `x`-run
`[a,b]` is shortened to `[a,c-1]`, while the `y`-run ending at `c-1` is
extended through `b`.

In particular, if

\[
                         c=a+d+1,
\tag{1.3}
\]

then `x` has a positive owner run of exact length `d+1`, so the maximal
depth-`d` antecedent has the singleton letter `{x}` at its unique eroded
position.

All internal immediate lower and upper colours are simply carried by
`tau`.  At the left boundary the upper colour is unchanged and exactly one
lower colour is replaced; at the right boundary the lower colour is
unchanged and exactly one upper colour is replaced.

#### Proof

Internal transitions remain Johnson transitions because `tau` is a graph
automorphism.  Write

\[
 T_c=T_{c-1}-\{y\}+\{z\},\qquad z\notin\{x,y\}.
\]

Since `T_(c-1)` contains both `x,y` and `T_c` contains `x` but not `y`,

\[
 \tau T_c=T_{c-1}-\{x\}+\{z\}.
\]

Thus the new left boundary is the Johnson step which deletes `x` and
inserts `z`.  Its union is the old union `T_(c-1)+z`; its intersection
changes from `T_(c-1)-y` to `T_(c-1)-x`.

Similarly write

\[
 T_{b+1}=T_b-\{x\}+\{w\},\qquad w\ne y.
\]

Because `T_b` contains `x` but not `y`,

\[
 \tau T_b=T_b-\{x\}+\{y\}.
\]

The new right boundary replaces `y` by `w`.  Its intersection is the old
intersection `T_b-x`, while its union changes from `T_b+w` to
`T_b-x+y+w`.

Only `x,y` change membership inside `I`.  Hence the stated run changes
follow.  Equation (1.3) gives
`|[a,c-1]|=d+1`, and the singleton conclusion is the exact run--erosion
criterion. \(\square\)

For positive residence, extending the `y`-run is harmless.  For
biresidence, require additionally that the next insertion of `y` occurs at
least `d+1` owners after `b`; this keeps the residual `y`-gap legal.  The
`x`-gap only grows.

## 2. Why one rail cannot preserve the owner row

The interval `I` consists entirely of owners containing `x` and omitting
`y`.  Therefore

\[
                         V(I)\cap\tau V(I)=\varnothing,
\tag{2.1}
\]

where `V(I)={T_i:i in I}`.

### Proposition 2.1 (one-copy obstruction)

If `T` contains every rank-`r` owner exactly once, the one-rail surgery
(1.2) never preserves that owner multiset.

#### Proof

Every owner in `tau V(I)` already occurs once somewhere in the complete
owner word.  Equation (1.2) removes the owners `V(I)` and adds a second
copy of every owner in `tau V(I)`.  Disjointness (2.1) prevents
cancellation. \(\square\)

Thus a minimum-run actuator cannot be made one-copy merely by changing a
single source/owner interval.  It needs either a second owner rail carrying
the missing transposed vertices or a genuinely nonlocal reassignment.

## 3. The exact `H`-closed double rail

Let `I=[c,b]` and `J=[c',b']` be disjoint intervals of the same length.
Assume their directed owner paths are coordinate-conjugate:

\[
                         T_{c'+t}=\tau T_{c+t}
             \qquad(0\le t\le b-c).
\tag{3.1}
\]

Assume `I` satisfies the crossing conditions of Section 1.  On `J`, assume
the transposed crossing conditions:

* its first internal owner contains `y` and omits `x`;
* its predecessor contains both `x,y` and the entrance deletes `x`;
* its successor contains neither, and the exit deletes `y` without
  inserting `x`.

Apply `tau` on both intervals and nowhere else.

### Theorem 3.1 (conjugate-rail minimum-run rethread)

The resulting chronology has the following exact properties.

1. Every transition remains Johnson.
2. The complete owner multiset is unchanged.
3. The complete multiset of internal lower-`q1` and upper-`q1` colours on
   `I union J` is unchanged.
4. Only the four boundary Johnson edges can change.  Consequently at most
   four old fixed-section edges are punctured.
5. If `c=a+d+1`, the coordinate `x` has an exact `d+1` positive run and
   hence a literal singleton source cell.

#### Proof

The boundary calculation is Theorem 1.1 on `I` and its transposed copy on
`J`.  Internally, applying `tau` to a Johnson path preserves every edge.
Equation (3.1) says more: the transformed path on `I` is exactly the old
path on `J`, and the transformed path on `J` is exactly the old path on
`I`.  Hence the two owner lists exchange, proving item 2, and their
internal intersection/union colour lists exchange, proving item 3.
Only the two entrance and two exit edges are not internal to these lists.
This proves item 4.  Item 5 is Theorem 1.1. \(\square\)

The theorem is `H`-closed in the strongest literal sense: the protected
owner and internal-palette bank is permuted, not merely replaced by an
isomorphic bank.

## 4. A bank of rails and the PBBS consequence

Suppose one can choose, for every ground coordinate `x`, a donor coordinate
`y(x)` and a conjugate pair `(I_x,J_x)` satisfying Theorem 3.1, with
pairwise disjoint boundary edges and with the obvious run/gap margins for
every donor.  Then all surgeries may be applied simultaneously whenever
their interval interiors are disjoint; more generally they may be applied
serially if every later conjugate pair is stated in the current chronology.

The total fixed-section puncture count is at most

\[
                         4k=O(r).
\tag{4.1}
\]

Even the weaker construction using `O(d)` boundary-local changes per
coordinate would give `O(kd)=O(r^(3/2))` punctures.  The inverse-fan profile
packing theorem repairs every paired lower/upper casualty throughout that
entire range.  Thus, after a conjugate-rail bank is found, the singleton
row has no remaining owner-count, immediate-palette, or arbitrary-upper
backup obstruction.

## 5. Exact remaining PBBS occurrence theorem

For a complete owner chronology define `pi_tau(i)` by

\[
                         T_{\pi_\tau(i)}=\tau T_i.
\tag{5.1}
\]

The minimal `tau`-closed position set containing one crossing interval `I`
is `I union pi_tau(I)`.  Theorem 3.1 applies exactly when `pi_tau(I)` is a
directed interval with the required transposed boundary state.

The remaining theorem is therefore:

> **PBBS conjugate crossing-rail theorem.**  For every coordinate `x`, the
> canonical or polynomially repaired PBBS factor contains a crossing
> rectangle `I_x` with `c=a+d+1` and a donor `y`, such that
> `pi_(x y)(I_x)` is a directed transposed crossing interval; the chosen
> pairs have a simultaneous or regenerative disjoint packing.

This is strictly smaller than planting an arbitrary `O(d)` collar and then
repairing an arbitrary perfect matching.  It asks for two correlated PBBS
run/gap rectangles.  It is also sharp for a two-rail partial relabelling:
without interval structure of `pi_tau(I)`, the transposed owner vertices
are scattered and every incident old factor edge becomes a separate
boundary debt.

No theorem currently proves this PBBS occurrence statement.  The
one-coordinate singleton obstruction is therefore reduced, but not yet
closed.

## 6. The terminal braid cannot supply its own conjugate rail

There is a useful exact localization.  On the terminal rigid braid of
ground size `n=2m+1`, write

\[
 O_h=
 \begin{cases}
 P_0(-h),&h\text{ even},\\
 P_2(-h),&h\text{ odd},
 \end{cases}
 \qquad h\in\mathbb Z_{2n}.
\tag{6.1}
\]

Using the standard base shapes

\[
 P_0=\{1,\ldots,m\},\qquad
 P_2=\{1,\ldots,m-1,m+1\},
\]

the directed edge `O_h->O_(h+1)` inserts

\[
                         I_h=-h\pmod n
\tag{6.2}
\]

for every parity.  Its deletion is

\[
 D_h=
 \begin{cases}
 m-h-1,&h\text{ even},\\
 m-h+1,&h\text{ odd}.
 \end{cases}
\tag{6.3}
\]

### Proposition 6.1 (no same-direction conjugate braid segment)

Let `tau` be one coordinate transposition.  There do not exist two
same-direction braid intervals of at least three owners satisfying

\[
                         O_{h+s+t}=\tau O_{h+t}
                         \qquad(0\le t<L),
\tag{6.4}
\]

with `L>=3`, unless `tau` fixes every owner of the first interval.  In
particular a crossing interval on which exactly one of the transposed
coordinates is present has no conjugate partner on the braid itself.

#### Proof

Conjugating the first two directed edges in (6.4) and using (6.2) gives

\[
 \tau(-h-t)=-(h+s+t)\pmod n,
                         \qquad t=0,1.
\tag{6.5}
\]

A transposition cannot agree with a nonzero cyclic translation on two
consecutive points: if both points moved they would have to be exchanged,
which would require simultaneously `s=1` and `s=-1` modulo the odd integer
`n`; if either is fixed then `s=0` modulo `n`.  Hence

\[
                         s\equiv0\pmod n.
\tag{6.6}
\]

If `s` is zero modulo `2n`, the two inserted and deleted labels on the
displayed edges are fixed, and the same is true along the interval;
equation (6.4) can differ only on the transposed coordinates.  A crossing
owner would then contradict (6.4).

The remaining possibility is `s=n` modulo `2n`, which reverses parity.
Equation (6.3) sends the two consecutive deletion labels to their shifts
by `+2` and `-2`, respectively.  Those two assignments are neither fixed
nor a transposition of the two labels when `n` is odd and `n>=5`.  This
again contradicts conjugacy. \(\square\)

Thus a successful conjugate crossing rail must use a residual PBBS
component, a braid-to-residual pair, or an already repaired factor.  The
most explicit terminal braid is not by itself the donor bank.
