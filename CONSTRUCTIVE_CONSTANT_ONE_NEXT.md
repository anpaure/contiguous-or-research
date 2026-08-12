# Constructive constant-one route: thin four-boxes and a sparse fold

## 1. Outcome and theorem ledger

For a chain box

\[
 Q(\boldsymbol\ell)=\prod_{i=1}^t[0,\ell_i]
\]

write `g_t(bold ell)` for the minimum length of a nonzero word whose
contiguous coordinatewise maxima contain every nonzero box point.  Put

\[
                         S=\sum_i\ell_i.
\]

The subcritical aggregation theorem says that a uniform estimate

\[
 g_4(\boldsymbol\ell)
 \le w(\boldsymbol\ell)+O((1+S)^{3-\delta})          \tag{1.1}
\]

for one fixed `delta>0` would imply

\[
                         \nu(k)=(1+o(1))W(k).
\]

This note does not prove (1.1) for every four-box.  It proves two explicit
constructive reductions.

### Proved result A: a two-shortest-sides subcritical regime

Let

\[
                         h=\min_i\ell_i.
\]

There is a deterministic word satisfying

\[
 \boxed{
 g_4(\boldsymbol\ell)
 \le (h+1)(S+1)^2-1.}                               \tag{1.2}
\]

More precisely, after removing the side of height `h` and renaming the
remaining heights `a,b,c` with `b<=c`,

\[
 \boxed{
 g_4(h,a,b,c)
 \le (h+1)(b+1)(a+c+1)-1.}                          \tag{1.3}
\]

Consequently, for every fixed `delta in (0,1]`, (1.1) already holds on the
entire regime

\[
                         h+1\le(S+1)^{1-\delta}.     \tag{1.4}

\]

This includes all zero-side boxes and every family with a polynomially
sublinear shortest side.  It is uniform in all other side lengths.

There is a stronger sorted-side consequence.  If

\[
                         h\le a\le b\le c,
\]

then the remaining coordinates may be permuted in Theorem 3 so that the
hook factor is the second-smallest side.  This gives

\[
 \boxed{
 g_4(h,a,b,c)
 \le (h+1)(a+1)(b+c+1)-1.}                         \tag{1.4a}
\]

Therefore (1.1) holds on the larger regime

\[
             (h+1)(a+1)\le (S+1)^{2-\delta}.       \tag{1.4b}
\]

So a four-box can remain genuinely hard only when its **two shortest**
sides are simultaneously large in product.  The former one-short-side
criterion (1.4) is an immediate special case.

### Proved result B: the triangular fold is free above height one

For the triangular arm alphabet `T_R`, there is a single-valued fold
section which transports every target with

\[
                         u\ge1,\qquad x\ge2          \tag{1.5}
\]

without increasing word length.  Adding each of the `R` cells absent from
the section exactly once makes the word spanning, still with no increase in
excess over the triangular alphabet size.

Thus the full two-letter expansion of every lower peak is unnecessary.
The only target families responsible for recursive loss are

\[
 u=0,\qquad x=0,\qquad x=1.                       \tag{1.6}

\]

An explicit standalone boundary completion gives the unconditional
recurrence

\[
 \rho(R)\le\rho(R-1)+2R-1+\left\lceil\frac R2\right\rceil, \tag{1.7}
\]

where `rho(R)` is the minimum repetition excess of a spanning triangular
word.  This recurrence is not subquadratic; its value is that it removes the
uncontrolled peak-occurrence term from the older block-lift recurrence and
identifies exactly what must be superposed.

### Still conjectural

No construction here handles the sorted thick sector

\[
             (h+1)(a+1)>(S+1)^{2-\delta}           \tag{1.8}

\]

with error `O(S^(3-delta))`.  No `o(width)` wreath recursion is proved.
The smallest direct four-box lemma now sufficient for constant one is the
thick-sector lemma in Section 5.  The smallest triangular lemma supporting
the known fan architecture is the boundary-superposition lemma in Section
8.

## 2. A chain-rectangle word

The basic gadget is elementary but useful because it is exact for unequal
chains.

### Lemma 1 (one rectangle of two chains)

Let

\[
 C=(c_0<c_1<\cdots<c_p),\qquad
 D=(d_0<d_1<\cdots<d_q)
\]

be chains in join-semilattices.  The word

\[
 (c_p,d_0),(c_{p-1},d_0),\ldots,(c_0,d_0),
 (c_0,d_1),\ldots,(c_0,d_q)                         \tag{2.1}
\]

has length `p+q+1` and contains every point `(c_i,d_j)` as the maximum of
a contiguous interval.

#### Proof

Start at `(c_i,d_0)` in the descending part and stop at `(c_0,d_j)` in the
ascending part.  The first-coordinate maximum is `c_i`, the second-coordinate
maximum is `d_j`, and no larger coordinate occurs between them.  The cases
`i=0` or `j=0` use the corresponding subinterval ending or beginning at the
central entry `(c_0,d_0)`.  \(\square\)

If `(c_0,d_0)` is the global zero, deleting that entry preserves every
nonzero interval maximum: the entries on its two sides become adjacent and
zero contributed no coordinate.

## 3. An explicit quadratic word for every three-chain box

Assume `0<=b<=c`.  The rectangle `[0,b]x[0,c]` has the following explicit
symmetric-chain decomposition.  For `0<=t<=b`, let

\[
\begin{split}
 D_t={}&(t,0),(t,1),\ldots,(t,c-t),\\
      &(t+1,c-t),(t+2,c-t),\ldots,(b,c-t).
\end{split}                                          \tag{3.1}

The corner `(t,c-t)` occurs only once.

### Lemma 2 (the hooks partition the rectangle)

The `b+1` chains `D_0,...,D_b` are pairwise disjoint and partition
`[0,b]x[0,c]`.

#### Proof

For a cell `(x,y)`, if `y<=c-x`, it lies in the vertical part of `D_x`.
If `y>c-x`, put `t=c-y`.  Then `0<=t<x<=b`, and `(x,y)` lies in the
horizontal part of `D_t`.  These two cases are disjoint and give a unique
chain.  Each displayed step increases one coordinate by one, and the first
and last ranks of `D_t` sum to `b+c`, so the chains are saturated and
symmetric.  \(\square\)

Pair the full chain `[0,a]` with each `D_t` and use Lemma 1.  Concatenate the
`b+1` resulting gadgets.

### Theorem 3 (uniform three-box construction)

For `b<=c`,

\[
 \boxed{
 g_3(a,b,c)\le(b+1)(a+c+1)-1.}                      \tag{3.2}

\]

The constructor is explicit and output-linear.

#### Proof

The gadget for `D_t` has length

\[
                         a+|D_t|.
\]

The hooks partition a rectangle of `(b+1)(c+1)` points.  Summing over `t`
therefore gives

\[
 (b+1)a+(b+1)(c+1)=(b+1)(a+c+1).                   \tag{3.3}
\]

The unique global-zero entry occurs in the `D_0` gadget and may be deleted,
giving (3.2).  Every target belongs to one chain rectangle and retains its
internal witness from Lemma 1.  \(\square\)

Permuting the three coordinates and taking the best choice only improves
(3.2).  In particular,

\[
                         g_3(a,b,c)=O((1+a+b+c)^2)   \tag{3.4}

\]

uniformly, including zero and extremely unequal sides.

## 4. Slice the shortest fourth coordinate

Let the fourth side have minimum height `h`, and call the other heights
`a,b,c`, with `b<=c`.  For each `s in {0,...,h}`, embed the word of Theorem
3 in the slice whose fourth coordinate is constantly `s`.

For `s=0`, its omitted local origin is the omitted global zero.  For every
`s>0`, prepend the one literal point `(0,0,0,s)`, because that target is
nonzero while the three-box constructor omits its local origin.

### Theorem 4 (thin-side four-box construction)

The concatenation of these `h+1` slice words is universal and has length at
most

\[
\begin{aligned}
 &(h+1)\big((b+1)(a+c+1)-1\big)+h\\
 &\qquad=(h+1)(b+1)(a+c+1)-1.                       \tag{4.1}
\end{aligned}

#### Proof

Fix a nonzero four-box target and let `s` be its fourth coordinate.  If one
of its first three coordinates is nonzero, its first-three-coordinate part
has a witnessing interval inside the `s`-slice copy of Theorem 3.  Every
entry of that interval has fourth coordinate `s`, so its complete maximum is
the requested four-tuple.  If its first three coordinates vanish, then
`s>0` and the prepended literal point witnesses it.  Concatenation cannot
destroy an interval internal to one slice.  The length calculation is
immediate.  \(\square\)

Since both factors in `(b+1)(a+c+1)` are at most `S+1`, (1.2) follows.
Under (1.4),

\[
 g_4(\boldsymbol\ell)
 \le(S+1)^{1-\delta}(S+1)^2
 =(S+1)^{3-\delta}.                                 \tag{4.2}

\]

Thus the troublesome uniformity over zero and unbalanced height vectors in
the aggregation theorem is not merely bookkeeping: a complete explicit
subcritical word is now available throughout the thin regime.

### Corollary 4.1 (sorted two-side strengthening)

Sort the four heights as

\[
                         h\le a\le b\le c.
\]

In Theorem 3, apply the hook decomposition to the side of height `a`, take
the side of height `b` as the other hook coordinate, and pair those hooks
with the chain of height `c`.  Equivalently, substitute
`(a,b,c)=(c,a,b)` into (3.2).  Slicing in the height-`h` coordinate gives

\[
 g_4(h,a,b,c)\le(h+1)(a+1)(b+c+1)-1.               \tag{4.3}
\]

Since `b+c+1<=S+1`, the condition

\[
                         (h+1)(a+1)\le(S+1)^{2-\delta}
\]

implies `g_4=O((S+1)^(3-delta))`.  Only boxes with two jointly thick
shortest directions remain for the four-box theorem.

## 5. Exact remaining four-box lemma

Fix one `delta>0`.  By Theorem 4, the following statement alone would imply
the full uniform local estimate (1.1).

### Thick four-box lemma (open)

After sorting `h<=a<=b<=c`, for every height vector satisfying

\[
 (h+1)(a+1)>(S+1)^{2-\delta},                       \tag{5.1}

\]

construct a word of length

\[
 w(\boldsymbol\ell)+O((S+1)^{3-\delta}).            \tag{5.2}

\]

Indeed, Corollary 4.1 handles the complementary vectors with the same
exponent.  This reduction removes every degenerate box and every box whose
two shortest directions have polynomially subcritical product from the hard
local theorem.  It does not reduce (5.1) to equal cubes: the four remaining
sides may still differ by polynomial factors, and projecting a cube word
generally introduces a leading-width mismatch.

The depth-truncated fan theorem is a genuine word in the equal-cube case,
but it presently covers only a central band.  A thick-box proof must reuse
its long upper and lower witnesses rather than append the outer targets
literally.

## 6. A sparse section of the triangular fold

Write

\[
 \mathcal T_R=\{P_0\}\cup
 \{E_{s,y}:1\le s\le R,\ 0\le y<s\},
 \qquad P_s=E_{s,0}.

\]

Targets are bounding boxes

\[
                         [u,r]\times[0,x],
 \qquad0\le u<r\le R,\quad0\le x<r.                \tag{6.1}

\]

The usual fold has two preimages over every nonzero lower peak.  For all
targets above height one, only one preimage is needed.  Define the
single-valued section

\[
\begin{aligned}
 \psi_R(P_a)&=P_{a+1},\\
 \psi_R(E_{a,b})&=E_{a+1,b+1}\qquad(b\ge1).
\end{aligned}                                        \tag{6.2}

### Theorem 5 (zero-overhead high-target lift)

If a word `W` is universal for `T_(R-1)`, then the entrywise word
`psi_R(W)` covers every target of `T_R` with

\[
                         u\ge1,\qquad x\ge2.         \tag{6.3}

\]

It has exactly `|W|` entries.

#### Proof

Fold the desired target to

\[
                         [u-1,r-1]\times[0,x-1].     \tag{6.4}

\]

Here `x-1>=1`.  Choose a lower witnessing interval.  Every first coordinate
in its entrywise image increases by one, so the new extrema are `u,r`.

The lower witness contains a peak because its minimum height is zero; that
peak maps to height zero under `psi_R`.  It also contains a cell of height
`x-1>=1`; that cell maps to height `x`.  Every other positive-height cell
increases by one and remains at most `x`, while every peak stays at height
zero.  Thus the image of the same contiguous interval has bounding box
exactly `[u,r]x[0,x]`.  No entry was duplicated or inserted.  \(\square\)

If `W` is spanning, the image of the complete lower alphabet consists
exactly of

\[
 \{P_1,\ldots,P_R\}
 \cup\{E_{s,y}:2\le y<s\le R\}.                     \tag{6.5}

\]

The missing upper cells are

\[
                         P_0,E_{2,1},E_{3,1},\ldots,E_{R,1}, \tag{6.6}

\]

exactly `R` cells.  Appending each once then makes the lifted word spanning.
If the spanning word `W` has excess `q` over `|T_(R-1)|`, the resulting
partial universal word
has length

\[
 |W|+R=|\mathcal T_R|+q.                            \tag{6.7}

\]

Hence all repetition excess is localized to the target families omitted by
(6.3), not to the growth of the alphabet.

## 7. An unconditional boundary-completion recurrence

Two standalone words cover the complementary target families.

First, the standard boundary scaffold

\[
 \mathcal B_R=
 P_R,P_{R-1},\ldots,P_0,
 E_{2,1},E_{3,2},\ldots,E_{R,R-1}                   \tag{7.1}

\]

has length `2R` and covers every target with `u=0` or `x=0`.

Second, scan `s=R,R-1,...,2`, output `E_(s,1)`, output `P_s` when `s` is
odd, and finally output `P_1`.  This parity corridor has length

\[
                         R-1+\left\lceil\frac R2\right\rceil \tag{7.2}

\]

and covers every strict target with `x=1`.  Indeed, start at `E_(r,1)` and
scan downward.  Since `u<r`, the integer interval `[u,r]` contains an odd
label.  If an emitted odd peak occurs above `u`, continue through
`E_(u,1)` and stop there.  If the only useful odd label is `u`, continue
through `P_u`; for `u=1`, use the terminal `P_1`.  In every case a peak
supplies height zero, a first-column cell supplies height one, the visited
row labels have minimum `u` and maximum `r`, and no row outside `[u,r]`
is used.

The three regimes

\[
 \{u\ge1,x\ge2\},\qquad
 \{u=0\text{ or }x=0\},\qquad
 \{u\ge1,x=1\}                                      \tag{7.3}

\]

are disjoint and exhaustive.  Therefore

\[
 \psi_R(W)\Vert\mathcal B_R\Vert\mathcal X_R        \tag{7.4}

\]

is a universal spanning word whenever `W` is.  Its excess satisfies (1.7),
because `|T_R|-|T_(R-1)|=R`.

This recurrence is a proved construction, but summing its `Theta(R)` loss
per level gives only `Theta(R^2)` excess.  It does not solve the triangular
or four-box asymptotic problem.

## 8. Smallest missing superposition lemma

Theorem 5 changes the constructive target.  One no longer needs to expand
every occurrence of every lower peak.  The new first-column cells (6.6) are
compulsory alphabet growth, not repetition.  What costs repetition is using
them while simultaneously retaining:

* a clean pure-peak realization of all `x=0` targets;
* enough peak--first-column portals for all `x=1` targets; and
* the `u=0` diagonal fan.

A quantitatively sufficient statement is the following.

### Boundary-superposition lemma (open)

For some fixed `epsilon>0`, there is an invariant family of universal
spanning words such that the sparse lift at level `R`, together with the `R`
new cells in (6.6), can be reordered and repaired to cover (1.6) while
preserving the high-target witnesses, using at most

\[
                         O(R^{1-\epsilon})           \tag{8.1}

\]

new repeated positions.

This would give

\[
                         \rho(R)=O(R^{2-\epsilon})   \tag{8.2}

\]

by summing the recurrence.  Across the `Theta(m)` threshold diagonals of the
four-box fan, the corresponding triangular repetition would be
`O(m^(3-epsilon))`, which is the subcritical scale sought by the aggregation
theorem.  A complete four-box proof would still have to couple the reflected
lower family, factorization, and unequal thick boxes; (8.1) is a sufficient
local braid lemma, not an asserted equivalence for all constructions.

The parity corridor shows why a literal standalone repair costs linear
overhead, while Theorem 5 shows exactly where sharing must occur.  Existing
lower bounds force a linear total excess `rho(R)=Omega(R)` but do not force a
linear **increment at every level**.  Therefore (8.1) is not contradicted by
the portal ledger.

## 9. Relation to the wreath route

The wreath program has a different smallest missing lemma: round the
antipodal typed cyclic-order fractional factor while leaving `o(W)` absolute
holes and preserving the required depth profile.  The available spread
estimates do not supply that diagonal-strength nibble.  No new wreath
rounding theorem is claimed here.

The constructive advances proved in this note are instead:

1. a complete subcritical solution for all polynomially thin four-boxes;
2. an exact reduction of the uniform four-box problem to its thick sector;
3. a zero-overhead triangular lift for every target above height one; and
4. an unconditional peak-multiplicity-free recurrence localizing all loss
   to three boundary layers.
