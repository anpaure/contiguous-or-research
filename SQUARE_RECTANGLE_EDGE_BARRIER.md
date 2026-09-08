# The full-square rectangle word has a quadratic edge barrier

## 1. The overstrong square problem

Put

\[
   G_R=[0,R]^2\cap\mathbb Z^2,
   \qquad |G_R|=(R+1)^2.
\]

Let `q_square(R)` be the least excess `|W|-|G_R|` of a word over
`G_R` which contains every grid point and in which every axis-parallel
integer rectangle is the coordinatewise bounding box of a contiguous
subword.

This problem cannot have subquadratic excess.

### Theorem 1 (elementary-edge barrier)

For every `R>=1`,

\[
             q_{\rm square}(R)\ge R^2.                 \tag{1.1}
\]

For `R>=2`, parity sharpens this to

\[
             q_{\rm square}(R)\ge R^2+2R-3.           \tag{1.2}
\]

### Proof

Consider a grid edge `xy`.  The two-point set `{x,y}` is itself an
axis-parallel integer rectangle.  A subword with exactly this bounding box
can use only the two letters `x,y`, and it must use both.  Somewhere inside
that subword there is consequently a consecutive transition `xy` or `yx`.
Thus every edge of the square grid must occur among the consecutive
transitions of `W`.

The grid has

\[
                     E_R=2R(R+1)                       \tag{1.3}
\]

edges, while a word of length `n` has only `n-1` transitions.  Hence
`n>=E_R+1`, which after subtracting `(R+1)^2` proves (1.1).

For the refinement, call a transition a grid transition when its two
letters form a grid edge.  Suppose there are `E_R+d` grid transitions, so
that `d` of them are repetitions beyond one compulsory occurrence of every
edge, and let `x` be the number of other transitions.  Cutting at those
`x` other transitions decomposes the grid transitions into at most `x+1`
trails.

The `(R+1)`-by-`(R+1)` grid has `4(R-1)` odd-degree vertices when `R>=2`.
Adding one repeated edge changes the number of odd vertices by at most two.
On the other hand, a union of at most `x+1` trails has at most `2(x+1)`
odd vertices.  Therefore

\[
        4(R-1)-2d\le2(x+1),
        \qquad d+x\ge2R-3.                             \tag{1.4}
\]

Since `n-1=E_R+d+x`, this gives

\[
 n\ge E_R+2R-2,
 \qquad
 n-(R+1)^2\ge R^2+2R-3.                               \tag{1.5}
\]

This parity refinement is sharp for the *edge-covering subproblem*: the
edges of a connected graph with `o>0` odd vertices can be partitioned into
`o/2` trails.  Here `o/2=2R-2`; concatenating those trail words has exactly
`E_R+2R-2` letters.  It need not cover the larger rectangles, so (1.2) is
only a lower bound for `q_square`.  QED.

### Corollary 2

Installing one full-square rectangle word in every sector of radii
`R=0,...,m` already costs at least

\[
       \sum_{R=0}^m R^2
       ={m(m+1)(2m+1)\over6}=\Theta(m^3)               \tag{1.6}
\]

extra occurrences per orientation.  It therefore cannot prove a
`width+o(m^3)` four-box theorem.

The square reformulation in `FOUR_BOX_INTACT_BLOCK_BARRIER.md` remains a
correct description of extrema.  Requiring every rectangle separately in
every sector is the overstrong step.

## 2. Why the triangular tail problem escapes

The actual triangular alphabet is

\[
 \mathcal T_R=\{(0,0)\}\cup
 \{(r,x):1\le r\le R,\ 0\le x<r\},                    \tag{2.1}
\]

and its demanded rectangles are only

\[
                         [u,r]\times[0,x],
 \qquad 0\le u<r\le R,\quad0\le x<r.                 \tag{2.2}
\]

Among these, the only two-point rectangles are

\[
                         [r-1,r]\times\{0\},
 \qquad 1\le r\le R.                                 \tag{2.3}
\]

Thus elementary rectangles force only the `R` consecutive edges of the
bottom spine, not the `Theta(R^2)` edges of the triangular grid.  There is
no elementary-edge obstruction to a word of length

\[
                         |\mathcal T_R|+O(R).          \tag{2.4}
\]

The independently proved lower bound `rho(R)>=R/4-O(1)` comes from portal
and peak-run constraints, not from the false full-square edge demand.

Likewise, the natural middle diagonal in each hook rectangle already makes
its central-square targets into subintervals of one path.  The correct
positive construction must preserve those path intervals and add only the
bottom-anchored residual triangular families.

## 3. Sector shear: the providers form equivalence classes

In one nonnegative sector write

\[
 X_c(a,b)=(c+a,m-c-b,b,m-a),
 \qquad (a,b)\in[0,m-c]^2.                             \tag{3.1}
\]

The join and meet of a rectangle `Q=[A,B]x[C,D]` are

\[
 \begin{aligned}
 J(c,Q)&=(c+B,m-c-C,D,m-A),\\
 M(c,Q)&=(c+A,m-c-D,C,m-B).                            \tag{3.2}
 \end{aligned}
\]

Consequently, whenever the displayed rectangles remain legal sector
rectangles,

\[
 \begin{aligned}
 J(c,[A,B]\times[C,D])
  &=J(c+t,[A,B-t]\times[C-t,D]),                       \tag{3.3}\\
 M(c,[A,B]\times[C,D])
  &=M(c+t,[A-t,B]\times[C,D-t]).                       \tag{3.4}
 \end{aligned}
\]

Equation (3.3) permits `-h<=t<=w` before boundary restrictions, where
`w=B-A` and `h=D-C`; (3.4) permits `-w<=t<=h`.  Thus a target is not a
rectangle tied to one square.  It is an equivalence class of sheared
rectangles in neighboring sectors, and only one legal representative has
to occur.

The elementary case makes the correction especially transparent.  In the
bulk, the horizontal edge

\[
       (c,[A,A+1]\times\{C\})                         \tag{3.5}

has the same upper join color as the vertical edge

\[
       (c+1,\{A\}\times[C-1,C]),                      \tag{3.6}

and the same lower meet color as the vertical edge

\[
       (c-1,\{A+1\}\times[C,C+1]).                    \tag{3.7}

The precise qualifications are only that the shifted edge lie in the
neighboring legal sector square.  Boundary failures form the surface
defect already visible in the hook construction.

Hence demanding all elementary rectangles in every square asks for both
providers of the same first-shadow target.  The actual four-box problem asks
for one provider from each shear class.  This is why its first shadows are
compatible with a near-Hamilton middle row even though the isolated full
square requires about twice as many transitions as vertices.

## 4. Correct replacement target

The square-word target should be replaced by the following quotient
problem.

* Keep the natural diagonal intervals which already cover the central
  squares.
* For every residual upper join class, choose one legal representative of
  (3.3); for every residual lower meet class, choose one representative of
  (3.4).
* Arrange the chosen representatives in a common word on the disjoint union
  of all sector alphabets, allowing a transition at a sector seam to serve
  the two neighboring classes in (3.6)--(3.7).
* Require the chosen lower meet intervals to survive the linked variable
  factor and coordinate-pin conditions.

The existing bottom-anchored triangular allocation is one explicit choice
of representatives for the residual tails.  Its still-open problem is a
near-once superposition compatible with the preserved central diagonals and
the common factor band.  Proving all rectangles in each isolated sector is
neither necessary nor asymptotically possible.
