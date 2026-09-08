# A phase-synchronized crossed `Q_8` associator

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The crossed recursion formerly used in
`MATH_THEOREM_DOUBLE_FACTOR_RECURSION_AND_DOUBLE_ERASURE_HALL_CUT_20260726.md`
is false: it compares parent directions at two different owners.  There is,
however, a different crossed construction which is exact.

The correction is forced.  Start with the alternating product `P_0` of one
parent factor and prescribe the fixed-point-free coordinate involution

\[
 \Xi(Li)=R(Si),\qquad \Xi(Ri)=L(Si).
\]

The only possible same-owner partner is obtained by applying `Xi` to the
*actual direction of `P_0` at that owner*.  For the standard common-phase
`Q_4` factor and

\[
                         S=(1\ 3)(2\ 4),
\]

this forced partner is a neighbour permutation whose components are
isometric `C_16`'s.  Hence it gives an explicit valid same-owner double
factor on `Q_8` with fixed-point-free relative direction permutation.

The proof is a phase synchronization identity: after every pair of moves,
the two `Q_4` phases rotate by `-1` and `+1`, respectively.  This is the
first genuine transverse associator.  It is not the invalid operation which
applies `G_1` to the other owner.

No physical shadow decoder is claimed here.  Also, the pair is not shown to
be bidirectional, so it cannot be fed without further work into a recursion
which requires an incoming-direction identity.

## 1. The forced crossed partner

Let `G` be a neighbour permutation of `Q_h`, with outgoing direction
function

\[
                         G(y)=y+e_{\delta(y)}.
\]

For `(u,v) in Q_h^L x Q_h^R`, put

\[
                         \epsilon(u,v)=|u|+|v|\pmod2
\]

and define the alternating product

\[
 P_0(u,v)=
 \begin{cases}
   (G(u),v),&\epsilon=0,\\
   (u,G(v)),&\epsilon=1.
 \end{cases}                                             \tag{1.1}
\]

Fix a coordinate permutation `S in S_h`, and let

\[
 \Xi(Li)=R(Si),\qquad \Xi(Ri)=L(Si).                       \tag{1.2}
\]

If a neighbour map `P_1` is to satisfy the pointwise same-owner identity

\[
                         \delta_{P_1}(z)=\Xi\delta_{P_0}(z), \tag{1.3}
\]

then it is uniquely forced to be

\[
 P_1(u,v)=
 \begin{cases}
   (u,v+e_{S\delta(u)}),&\epsilon=0,\\
   (u+e_{S\delta(v)},v),&\epsilon=1.
 \end{cases}                                             \tag{1.4}
\]

### Lemma 1.1 (ownership is automatic)

The map `P_1` in (1.4) is a neighbour permutation for every direction
colouring `delta`, whether or not `delta` itself defines a permutation.

#### Proof

On the even shore, `u` is fixed and, for each fixed `u`, the map on `v` is
translation by the one fixed vector `e_(S delta(u))`.  It is therefore a
bijection from the appropriate parity shore of the `v`-cube to the opposite
shore.  On the odd shore the identical argument holds with `u` and `v`
interchanged.  Thus both shore restrictions are bijections.  Equation
(1.3) follows directly from (1.1)--(1.4).  \(\square\)

This lemma isolates the old error.  The invalid recursion used
`S delta(v)` at an even owner, although (1.3) forces `S delta(u)` there.

## 2. A general phase-synchronization criterion

Suppose the vertices of `Q_h` have a phase map

\[
                         \phi:Q_h\longrightarrow\Omega
\]

with the following properties.

1. Vertex parity is a function `b:Omega -> Z_2` of the phase.
2. The outgoing direction is a function `d:Omega -> [h]`, and `d` is a
   bijection.
3. Translation by coordinate `i` induces a well-defined phase permutation
   `tau_i`, so
   \[
      \phi(y+e_i)=\tau_i\phi(y).
   \]

Put `a=S d`.  Assume that there is an `h`-cycle `rho` on `Omega`, reversing
`b`, such that whenever `b(c)=b(c')`,

\[
 \tau_{a(c)}(c')=\rho(c'),\qquad
 \tau_{a(\rho(c'))}(c)=\rho^{-1}(c).                       \tag{2.1}
\]

### Theorem 2.1 (phase-synchronized cross)

If every component of `G` is an isometric `C_(2h)` and (2.1) holds, then
every component of the forced map `P_1` in (1.4) is an isometric
`C_(4h)`.  Consequently `(P_0,P_1,Xi)` is a same-owner double-factor
certificate in dimension `2h`; `Xi` is fixed-point-free.

#### Proof

Start at an even owner and inspect two moves of `P_1`.  Write

\[
                         c_t=\phi(u_t),\qquad c'_t=\phi(v_t).
\]

The two phases have the same parity.  The first move uses right direction
`a(c_t)`, and the second uses left direction `a(c'_(t+1))`.  By (2.1),

\[
                         c'_{t+1}=\rho(c'_t),\qquad
                         c_{t+1}=\rho^{-1}(c_t).             \tag{2.2}
\]

Thus, in the first `h` two-move blocks, the right directions are

\[
                         a(c_0),a(\rho^{-1}c_0),\ldots
\]

and the left directions are

\[
                         a(\rho c'_0),a(\rho^2c'_0),\ldots.
\]

Because `rho` is an `h`-cycle and `a` is a bijection, each list uses every
parent coordinate exactly once.  After `2h` moves both `u` and `v` have
been complemented.  The phases have returned, so the next `2h` directions
repeat the first `2h`, returning to the starting vertex.  No earlier return
is possible because before `2h` moves some coordinate has been used once,
and at `2h` moves the state is the complement.  The resulting word is a
doubled permutation of all `2h` coordinates, so the component is an
isometric `C_(4h)`.

The same conclusion for `P_0` follows from `P_0^2(u,v)=(G(u),G(v))`.
Equation (1.3) is Lemma 1.1, and (1.2) has no fixed coordinate. \(\square\)

## 3. Verification for the common-phase `Q_4` factor

Let

\[
 H=\langle e_1+e_3,e_2+e_4\rangle
\]

and index the four phase classes by `Z_4`:

\[
 C_0=H,\quad C_1=e_1+H,\quad
 C_2=e_1+e_2+H,\quad C_3=e_2+H.                    \tag{3.1}
\]

The standard factor has outgoing direction

\[
                         d(c)=c+1\quad(\bmod 4),             \tag{3.2}
\]

in the representatives `1,2,3,4`.  Vertex parity is `b(c)=c mod 2`.
Choose

\[
                         S=(1\ 3)(2\ 4),                    \tag{3.3}
\]

so `a(c)=S d(c)=d(c+2)`, and take `rho(c)=c+1`.

Coordinates `1,3` induce the same translation on `Q_4/H`, and coordinates
`2,4` induce the other one.  If `c,c'` have the same parity, then direct
inspection of the four Gray phases gives

\[
                         \tau_{a(c)}(c')=c'+1.               \tag{3.4}
\]

Now `c` and `c'+1` have opposite parity, and the second translation gives

\[
                         \tau_{a(c'+1)}(c)=c-1.              \tag{3.5}
\]

These are exactly (2.1).

### Corollary 3.1 (explicit corrected `Q_8` double factor)

Let `G` be the standard common-phase `Q_4` factor with word
`1234 1234`.  On `Q_8=Q_4^L x Q_4^R`, define

\[
 P_0(u,v)=
 \begin{cases}
  (G(u),v),&\epsilon=0,\\
  (u,G(v)),&\epsilon=1,
 \end{cases}
\]

and

\[
 P_1(u,v)=
 \begin{cases}
  (u,v+e_{S\delta(u)}),&\epsilon=0,\\
  (u+e_{S\delta(v)},v),&\epsilon=1,
 \end{cases}
 \qquad S=(1\ 3)(2\ 4).                              \tag{3.6}
\]

Then `P_0` and `P_1` are `C_16`-factors, every component is isometric, and

\[
 \delta_{P_1}(z)=\Xi\delta_{P_0}(z),\qquad
 \Xi(Li)=R(Si),\quad\Xi(Ri)=L(Si).                         \tag{3.7}
\]

In particular `Xi` is a fixed-point-free same-owner direction involution.

This is a literal `Q_8` associator: it changes the left/right **top-level**
frame and is not itself a shore inside one `Q_4` cell.  It does not destroy
the bottom two-point wire partition.  Indeed every admissible `S` in
Proposition 3.2 permutes the two `Q_4` wires `A,B`, and `Xi` consequently
permutes the four global wires `L A,L B,R A,R B`.  A recursion using only
this primitive therefore remains imprimitive at the bottom scale; no
full-Beneš or physical trace conclusion follows from the associator alone.

### Proposition 3.2 (classification of phase-only coordinate corrections)

For the standard `Q_4` phase colouring, let

\[
                         A=\{1,3\},\qquad B=\{2,4\}.
\]

The forced crossed partner (1.4) is an isometric `C_16`-factor for every
starting owner if and only if `S` either preserves the unordered pair
`{A,B}` blockwise or interchanges `A` and `B`.  Equivalently,

\[
                         S\in S_2\wr S_2\le S_4.                \tag{3.8}
\]

Thus exactly eight of the twenty-four coordinate permutations give a
phase-synchronized cross.  The choice `S=(1 3)(2 4)` above is one of them;
even `S=id` works, because the left/right exchange in `Xi` is already
fixed-point-free.

#### Proof

For a phase `c in Z_4`, put

\[
 s_c=
 \begin{cases}
 +1,&S(d(c))\in A\text{ for }c\text{ even, or }S(d(c))\in B
                                      \text{ for }c\text{ odd},\\
 -1,&\text{otherwise}.
 \end{cases}
\]

At an even composite owner the two phases `c,c'` have the same parity.
One two-move block of (1.4) induces exactly

\[
       (c,c')\longmapsto
       \bigl(c-s_{c'+s_c},\ c'+s_c\bigr)\pmod4.                 \tag{3.9}
\]

If `S` preserves `A,B`, then every `s_c=+1`, and (3.9) is
`(c-1,c'+1)`.  If `S` interchanges the two blocks, every `s_c=-1`, and
(3.9) is `(c+1,c'-1)`.  The proof of Corollary 3.1 applies in either case.

Otherwise, since `S` maps exactly two coordinates into each of `A,B`, the
sign word has exactly one negative even phase and one negative odd phase.
They are adjacent on the four-cycle.  Up to rotating and reversing the
phase labels, the sign word is either

\[
                         (-,-,+,+)
 \quad\text{or}\quad    (-,+,+,-).                              \tag{3.10}
\]

In the first case (3.9) has the two-cycle

\[
                         (0,0)\longleftrightarrow(3,3).
\]

In the second it has the six-cycle

\[
 (0,0)\to(1,3)\to(2,0)\to(1,1)\to(0,2)\to(3,1)\to(0,0).
\]

The corresponding right or left phase repeats before it has traversed all
four values, so a physical direction repeats before all eight directions
have appeared.  That component is not an isometric `C_16`.  Hence no other
`S` works for every owner. \(\square\)

## 4. Exact boundary

The result proves only the outgoing same-owner double-factor statement.
Its incoming directions are not obtained from those of `P_0` by `Xi`: at
an even owner, `P_0^{-1}` reads the incoming parent direction at `v`, while
`P_1^{-1}` uses the outgoing phase direction at `v`.  Thus the present pair
is not automatically a bidirectional certificate.

There is a useful refinement with a *different* incoming frame.  Choosing
the reflection `S=(2 4)` gives outgoing frame `cross(S)` and incoming frame
`cross(S(1 2 3 4))`; both are fixed-point-free involutions.  See
`MATH_THEOREM_TWO_SIDED_PHASE_FRAME_CHANGING_Q8_PRIMITIVE_20260726.md`.
They are unequal, so this does not contradict the preceding statement.

Nor does the theorem decode a literal lower or upper physical target.  In
particular, it does not adjoin the completed support `J` as invisible
metadata.  Those are separate gates.

What is settled is the precise question left open by the crossed-recursion
audit: full phase equality can replace the invalid parity-only comparison,
and the standard `Q_4` quotient supplies exactly the required synchronizer.

There is a surviving fixed-wire boundary as well.  Proposition 3.2 forces
every phase-only `S` to lie in `S_2 wr S_2`, so the corrected `Q_8`
primitive can re-pair the two child blocks but cannot split the bottom
two-coordinate wires.  A genuinely universal switch network still needs a
later associator with a different bottom phase kernel.
