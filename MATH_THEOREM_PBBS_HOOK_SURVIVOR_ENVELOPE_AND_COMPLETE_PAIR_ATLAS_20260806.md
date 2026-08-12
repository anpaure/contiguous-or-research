# Exact hook survivor envelopes give a complete native rank-two atlas

**Date:** 2026-08-06  
**Method:** literal hook leaf-slot algebra, rooted PBBS updates, and
mandatory-core thinning; no search  
**Status:** unconditional in the eventual regime `d>=2`, `d=o(m)`.  Every
rank-two target has a literal occurrence on an untouched depth-`d`
resident PBBS hook component, and all pair targets can be installed
simultaneously on distinct components without changing any owner or q1
edge.  Ranks `3,...,d` remain open.

## 1. Hook coordinates and the depth-`d` source core

Put

\[
 n=2m+1,
 \qquad h=d+1,
 \qquad p=2h-1=2d+1,
 \qquad b=m-h=m-d-1.
\tag{1.1}
\]

Use the standard hook leaf-slot coordinates

\[
 x=(\ell_0,\ldots,\ell_{h-2},t,
       r_{h-2},\ldots,r_0),
 \qquad |x|=b,
\tag{1.2}
\]

with rooted Dyck word

\[
\begin{aligned}
 D_h(x)={}&(10)^{\ell_0}1(10)^{\ell_1}1\cdots
        (10)^{\ell_{h-2}}1(10)^{t+1}\\
 &\quad 0(10)^{r_{h-2}}0\cdots
        0(10)^{r_1}0(10)^{r_0}.
\end{aligned}
\tag{1.3}
\]

The step-two rooted shape map rotates the `p` entries of `x`.  Let `r`
be the physical root of the current phase and let

\[
                         z=r_0
\tag{1.4}
\]

be its terminal occupancy.

### Lemma 1.1 (root and mandatory-core formula)

At the next step-two update the physical root is

\[
                         r'=r-(2z+1)\pmod n.
\tag{1.5}

For the source position whose envelope is the intersection of the next
`h=d+1` owners, the mandatory core is

\[
                         \boxed{F=\{r,r-2z\}.}
\tag{1.6}

The braces in (1.6) denote a set: it is the singleton `{r}` when `z=0`.

#### Proof

Apply the first-maximum rooted update directly to (1.3).  The terminal
bank `(10)^z` contributes `2z` physical steps, followed by the one root
step, giving (1.5).  Iterating the same displayed hook factorization
through the next `h` centered transitions shows that the exit deletion
after the `h`-owner window is

\[
                         r-2z=r'+1.
\]

(The intervening distinguished deletions are the successive nonfree
spine/compulsory-leaf up-steps.)  The source mandatory core consists
exactly of the entrance insertion `r` and this exit deletion.  This proves
(1.6).  `square`

Summing (1.5) through one complete slot rotation gives

\[
 r_p-r_0=-\sum_{j=0}^{p-1}(2z_j+1)
         =-(2b+p)=-(2m-1)\equiv2\pmod n,
\tag{1.7}
\]

recovering `tau^p=rho^2` without a convention-dependent action-angle
identification.

## 2. Exact zero-terminal survivor envelope

Assume now that `z=r_0=0`.  List the `b` free leaves in the remaining
`p-1=2h-2` slots, with multiplicity, by

\[
                         1\le c_1\le\cdots\le c_b\le p-1.
\tag{2.1}
\]

Thus the number of indices `i` with `c_i=j` is the occupancy of the
`j`-th nonterminal slot in (1.2).

### Theorem 2.1 (survivor-envelope formula)

After rotating coordinates so that `r=0`, the depth-`d` envelope at this
loop position is

\[
                         \boxed{
 P=\{0\}\cup\{c_i+2i:1\le i\le b\}.}
\tag{2.2}

Consequently the map from zero-terminal hook phases to envelopes is a
bijection

\[
 \boxed{
 x\longleftrightarrow
 P=\{0\}\cup J,
 \quad
 J\in\binom{\{3,4,\ldots,n-3\}}b,
 \quad J\text{ has no consecutive elements}.}
\tag{2.3}

#### Proof

In the literal word (1.3), the up-step of the `i`-th free leaf occurs at
offset

\[
                         w_i=c_i+2i.
\tag{2.4}

Indeed `c_i` counts the nonterminal spine slots passed, while the `i`
free peaks encountered up to and including this one contribute `2i`
physical positions.  Direct first-maximum updating through the next `h`
owners deletes each of the `h` spine/compulsory up-steps once and deletes
none of the free-leaf up-steps.  The current root is inserted at the
entrance and, because `z=0`, is deleted only at the exit.  Hence precisely
the root and the labels (2.4) lie in every one of the `h` owners, proving
(2.2).

Now

\[
 w_1\ge3,
 \qquad
 w_b\le(p-1)+2b=2m-2=n-3,
\]

and

\[
                         w_{i+1}-w_i
 =(c_{i+1}-c_i)+2\ge2.
\]

Thus `J` is a nonconsecutive `b`-subset of the displayed path.  Conversely,
if `3<=w_1<...<w_b<=n-3` and successive differences are at least two, put

\[
                         c_i=w_i-2i.
\]

Then `1<=c_1<=...<=c_b<=p-1`, recovering a unique weak composition with
terminal entry zero.  This proves the bijection.  `square`

The count from (2.3) is

\[
 \binom{(2m-4)-b+1}{b}
 =\binom{m+d-2}{b}
 =\binom{m+d-2}{2d-1},
\tag{2.5}
\]

agreeing exactly with the mountain-fibre zero-terminal ledger.

## 3. Which targets fit in a loop envelope?

For a general root `r`, let

\[
 I_r=\{r+3,r+4,\ldots,r+n-3\}
\tag{3.1}
\]

in cyclic order.  Theorem 2.1 says that loop envelopes are exactly
`{r} union J`, where `J` is an independent `b`-set in the path `I_r`.

### Proposition 3.1 (exact loop-ticket criterion below the deadline)

Let `S` be nonempty with `|S|<=d`.  A zero-terminal hook loop can carry
`S` in one thinned source cell if and only if there is an `r in S` such
that

1. `S\setminus{r} subseteq I_r`; and
2. `S\setminus{r}` contains no consecutive coordinates.

#### Proof

Necessity is immediate from (2.3).  For sufficiency put
`Q=S\setminus{r}`.  The path `I_r` has length `2m-4` and independence
number `m-2`.  Any independent set of size `q` in a path extends to one
of size at least `(m-2)-q`: start with a maximum independent set and, for
each prescribed vertex absent from it, insert that vertex and delete at
most its two neighbours, losing at most one in size.  Here

\[
 q\le d-1,
 \qquad
 (m-2)-q\ge m-d-1=b.
\]

Thus `Q` extends to an independent `b`-set `J` in `I_r`.  Theorem 2.1
gives an envelope containing `S`, and Lemma 1.1 gives mandatory core
`{r}`.  The one-cell ticket theorem permits thinning that cell to `S`.
`square`

For pairs this criterion is especially simple.  A pair of cyclic distance
at least three has a one-cell loop ticket.  Pairs of distance one or two
do not.

## 4. The two missing pair distances

Both exceptional pair orbits have equally explicit native tickets.

### Proposition 4.1 (distance two in one cell)

Choose a hook phase with terminal occupancy `z=1`.  Lemma 1.1 gives

\[
                         F=\{r,r-2\}.
\tag{4.1}
\]

Since `F subseteq P`, the one-cell ticket theorem allows the source letter
to be thinned to this exact distance-two pair.

### Proposition 4.2 (adjacent pair in two cells)

Choose a hook angle having two consecutive zero terminal slots.  At the
corresponding consecutive source positions, Lemma 1.1 gives singleton
mandatory cores

\[
                         \{r\},\qquad\{r-1\},
\tag{4.2}

because (1.5) advances the root by `-1` when `z=0`.  Thin the two source
letters to those singletons.  Their length-two interval has union

\[
                         \{r,r-1\}.
\tag{4.3}

The changed block has length two, at most `d`, so mandatory-core
localization preserves the complete owner row.

## 5. Abundant distinct component choices

The constructions above are not isolated.

* For an adjacent pair, fixing two consecutive terminal occupancies to
  zero leaves
  \[
                           \binom{b+p-3}{p-3}
  \]
  relative hook phases.
* For a distance-two pair, fixing the terminal occupancy to one leaves
  \[
                           \binom{b+p-3}{p-2}
  \]
  phases.
* For a distance `q>=3`, write the desired nonroot coordinate as
  `q=c_i+2i`.  If `q=2a+1`, take `i=a,c_i=1`; if `q=2a`, take
  `i=a-1,c_i=2`.  Keep `c_1,...,c_i` fixed at `c_i` and choose the
  remaining nondecreasing entries freely in `[c_i,p-1]`.  This gives at
  least
  \[
   \binom{b-i+p-c_i-1}{p-c_i-1}
  \tag{5.1}
  \]
  loop phases containing the desired pair.

Uniformly for `3<=q<=m`, (5.1), divided by the at most `np` rooted
occurrences in one component, tends to infinity faster than any polynomial
in `m`.  The same is true of the first two displayed counts.  Therefore a
greedy choice can assign a **different untouched hook component** to each
of the `binom(n,2)=O(n^2)` pair targets.

The action partition is `(h,1^b)` with `b>=2` eventually, so none of these
components is touched by the full rigid one-/two-soliton rotation rethread.

## 6. Complete simultaneous pair atlas

### Theorem 6.1 (native rank-two closure)

For all sufficiently large `m`, the canonical PBBS factor contains a
family of mutually distinct untouched hook components and a depth-`d`
antecedent on each selected component such that every pair

\[
                         \{a,b\}\in\binom{[n]}2
\]

occurs on its own literal source interval.

Every distance-at-least-three pair uses one thinned loop cell, every
distance-two pair uses one thinned `z=1` cell, and every adjacent pair uses
two consecutive thinned loop cells.  On each component the changed bank
has length at most two, so `D^dA=T` remains exact.  Because different pair
targets use different components, all choices compose simultaneously.

No owner, q1 edge, component, or inherited owner-interval upper witness is
changed.

#### Proof

Propositions 3.1, 4.1, and 4.2 give one literal construction for every
pair.  Section 5 supplies more than polynomially many candidate components
for each target, so greedily avoid the fewer than `binom(n,2)` components
used earlier.  Apply the short-block atlas theorem independently on each
chosen component.  `square`

## 7. Remaining low-rank gate

Ranks one and two are now closed natively:

\[
                         \boxed{|S|=1,2.}
\]

For `3<=|S|<=d`, the exact one-cell criterion remains

\[
                         F_t\subseteq S\subseteq P_t,
\]

and Theorem 2.1 completely describes its loop subfamily.  Multi-cell
intervals can additionally combine consecutive loop cores as in
Proposition 4.2.  The next problem is therefore a finite hook-language
question: characterize unions of the mandatory cores (1.6) over a short
source interval and prove a component-level Hall theorem for those
interval tickets.

The rank-two theorem shows that the first structural zeros of the loop
envelope are repairable without any PBBS rethread.  It does not yet prove
the analogous statement for all higher low targets.
