# Stratified support is enough for all-height phase-clock upper monotonicity

**Date:** 2026-08-13  
**Status:** unconditional local theorem.  It weakens the phase-clock
theorem's phase-and-endpoint-refined *count identity* to a finite
support-domination test.  The theorem concerns intervals internal to the
displayed lifted base paths.  Intervals crossing a separately attached
exterior return or closure require the same test after that exterior has
been included in the base closures.

## 1. Base data

Let `F^-` and `F^+` be two finite collections of oriented simple Johnson
paths on a common owner occurrence set.  Each owner occurrence `v` has a
base value `V_v` and a phase

\[
                         \epsilon(v)\in\{0,1\}.       \tag{1.1}
\]

Assume every consecutive pair in either collection has opposite phases.
For an oriented base interval

\[
                         I=(v_1,\ldots,v_s),          \tag{1.2}
\]

write

\[
                         T(I)=\bigcup_{j=1}^sV_{v_j}. \tag{1.3}
\]

Define its **stratified signature** by

\[
 \sigma(I)=
 \begin{cases}
  (T(I),s,\epsilon(v_1)),&s=1,2,\\
  (T(I),s),&s\ge3.
 \end{cases}                                         \tag{1.4}
\]

Let `Sigma^-` and `Sigma^+` be the sets of signatures realized by base
intervals in `F^-` and `F^+`.

## 2. Clock lift

Fix `h>=2`, disjoint clock labels

\[
                         U=\{u_0,\ldots,u_{2h-1}\},  \tag{2.1}
\]

and put, cyclically,

\[
                         D_t=\{u_t,\ldots,u_{t+h-1}\}. \tag{2.2}
\]

Replace an owner occurrence `v` by the oriented block

\[
 \Gamma_v=
 \begin{cases}
  ((V_v,D_0),(V_v,D_1),\ldots,(V_v,D_h)),
       &\epsilon(v)=0,\\
  ((V_v,D_h),(V_v,D_{h+1}),\ldots,(V_v,D_{2h}=D_0)),
       &\epsilon(v)=1.
 \end{cases}                                         \tag{2.3}
\]

Any fixed common core may be adjoined to every displayed owner; it is
suppressed.  Concatenating the blocks along every oriented base path gives
the lifted collections `F^-[h]` and `F^+[h]`.

Let `Deck_w(G)` be the support of unions of all `w` consecutive lifted
owners in `G`.

## 3. The finite support criterion

### Theorem 3.1 (stratified-support phase-clock dilation)

If

\[
                         \boxed{\Sigma^-\subseteq\Sigma^+,}    \tag{3.1}
\]

then for every `h>=2` and every lifted width `w>=1`,

\[
                         \boxed{
 Deck_w(F^-[h])\subseteq Deck_w(F^+[h]).}             \tag{3.2}
\]

Thus old-to-new support monotonicity of the complete lifted internal
upper deck follows from one finite base test independent of `h`.

#### Proof

Take an old lifted interval `J`.  Let

\[
 I=(v_1,\ldots,v_s)                                  \tag{3.3}
\]

be the ordered list of distinct clock blocks met by `J`.  Let `a` be its
first position in `Gamma_(v_1)` and `b` its last position in
`Gamma_(v_s)`, with positions numbered `0,...,h`.  Its base part is
`T(I)`.  Its clock part is the union of the corresponding endpoint block
pieces and every complete intervening block.

If `s=1`, condition (3.1) supplies a new one-owner interval with the same
base value and starting phase.  Take the same positions `a,b`.  Formula
(2.3) gives the identical literal clock union and the same width.

If `s=2`, the phases of both blocks are determined by the starting phase,
because consecutive phases alternate.  Condition (3.1) supplies a new
two-owner interval with the same base union and starting phase.  Again use
the same endpoint offsets `a,b`.  Both endpoint clock arcs, hence their
union, are literal copies; the lifted width is unchanged.

Suppose `s>=3`.  The interval contains every owner position of each
strictly intervening block `Gamma_(v_2),...,Gamma_(v_(s-1))`; at least one
such block exists.  Either half-clock block has full clock union:

\[
                         \bigcup_{t=0}^{h}D_t=U,
 \qquad                 \bigcup_{t=h}^{2h}D_t=U.    \tag{3.4}
\]

Hence the clock part of `J` is all of `U`, independent of phase and endpoint
offsets.  Condition (3.1) supplies a new interval `I'` with the same base
union and the same number `s` of blocks.  Choose endpoint offsets `a',b'`
with

\[
                         a'-b'=a-b.                  \tag{3.5}
\]

For example take `a'=a,b'=b`.  Since every block has length `h+1`, the
lifted width is

\[
                         w=(s-1)(h+1)-a+b+1,         \tag{3.6}
\]

and is therefore the same for `I'`.  Its clock union is also `U` by
(3.4), while its base union is `T(I)`.  It gives a new witness of the old
literal lifted value at width `w`.

The three cases prove (3.2).  \(\square\)

### Corollary 3.2 (counts are unnecessary)

The theorem requires neither equality nor domination of multiplicities of
the signatures in (1.4).  A single new realization of each old signature
is enough.  In particular, first/last occurrence names and endpoint-cut
booleans need not be retained once their only effect on the lift is the
clock union described above.

## 4. Why unrefined base support is insufficient

For intervals meeting one or two clock blocks, the literal clock union
depends on the initial phase.  Thus inclusion only after forgetting
`epsilon(v_1)` need not lift.  Conversely, retaining phase for `s>=3` is
unnecessary because the complete intervening block shields both endpoints
by (3.4).

The precise finite object is therefore the two-row refinement

\[
 \{(T,1,\epsilon),(T,2,\epsilon)\}
 \quad\text{together with}\quad
 \{(T,s):s\ge3\},                                   \tag{4.1}
\]

not the fully occurrence-refined current used in the earlier sufficient
theorem.

## 5. Closure boundary

The proof treats every interval inside the lifted oriented paths.  If the
paths are closed by additional return fragments, apply Theorem 3.1 to the
**complete oriented base closures**, including those fragments.  It is not
enough that the interior path test passes: an interval may cross a return,
and a return may change the first/last block list or introduce a clock state
outside (2.3).

A sufficient exterior condition is literal transport of each return with
the same base values, phases, and constant endpoint clock anchor.  More
generally the return-augmented base closures must satisfy (3.1).  This is
the exact remaining host interface in applications.

## 6. The oriented `T_2` relay certificate

Consider the five canonical semilength-six MSW paths used by the frozen
two-hex `T_2` relay.  Write `F_x` and `R_x` for the forward and reverse
endpoints of the path rooted at `x`.  After the two incidence switches, the
five z-free residual paths have endpoint pairs

\[
 F_0F_{11},\quad F_2R_{62},\quad F_1R_0,\quad
 F_{62}R_{11},\quad R_1R_2.                         \tag{6.1}
\]

The fixed complementary endpoint returns therefore orient the five new
segments, in the order `(x_0,x_2,x_1,x_62,x_11)`, by the mask

\[
                         11010_2=26,                 \tag{6.2}
\]

or by its global reversal `00101_2=5`.  Use the same orientation mask on
the five old paths.

### Proposition 6.1 (finite internal certificate)

With either orientation in `(6.2)`, the old and new z-free path collections
satisfy `(3.1)`.  More explicitly:

* for `s=1`, the owner supports are identical;
* for `s=2`, the supports of `(T,epsilon(first))` are identical, with
  `792` signatures on each side; and
* for `s>=3`, every old `(T,s)` occurs on the new side.

The complete stratified supports have sizes

\[
                         |\Sigma^-|=2382,qquad
                         |\Sigma^+|=2404.            \tag{6.3}
\]

Thus Theorem 3.1 gives internal all-width support monotonicity for the
oriented `T_2` phase-clock lift at **every** height `h>=2`.

#### Proof

Only five old owner edges change.  With the orientations forced by (6.1),
their union values and starting phases are permuted as follows; every
listed phase is zero:

\[
\begin{array}{c|c|c}
\text{old path/position}&T&\text{new path/position carrying }T\\ \hline
x_0,3&101011010101&x_1,3\\
x_2,3&101011001101&x_0,5\\
x_1,1\text{ (reversed)}&101001011101&x_{11},1\\
x_{62},5&101010001111&x_2,3\\
x_{11},5&100011001111&x_{62},5.
\end{array}                                             \tag{6.4}
\]

All unchanged edges are literal.  This proves the `s<=2` assertions.
The `s>=3` assertion is the finite interval-union comparison on the five
affected paths; all other canonical paths are literal.  Direct substitution
of their displayed owner rows gives the inclusion and the counts (6.3).
The endpoint pairing (6.1) shows that this is the actual fixed-return
orientation, not five independently chosen path reversals.  Theorem 3.1
then proves the all-height conclusion.  \(\square\)

The proposition is an internal z-free theorem.  A complete odd-wreath
actuator additionally contains the unchanged complementary returns and the
vertical endpoint edges.  Intervals crossing those returns are not covered
by (6.3); they must be included in the closure-augmented signature test of
Section 5, or protected by a literal full-union/transport argument.

## 7. Audit scope

The finite `T_2` certificate and direct clock expansions were audited on
H100.  The expansions have zero old-support loss for every `2<=h<=12`;
they are checks of Proposition 6.1 and Theorem 3.1, not an extrapolation in
`h`.  Without the orientation (6.2), the naive canonical directions lose
clock-refined fibers already at `h=2,3`, demonstrating that the phase row
in (1.4) is substantive.
