# A complementary square closes the common-mate `C8` with exact residence and all-width transparency

**Date:** 2026-08-13  
**Method:** synchronized first-entry orders, an independently ordered
complementary return, and protected-Ore localization  
**Status:** unconditional local and spanning-host theorem.  For the first
time the same literal protected bank is simultaneously all-width
owner-current neutral, two-sided depth-resident, phase-resolved, and odd on
the exported sockets.  This removes the internal run-two obstruction of the
two-slot collar.  It does not by itself identify the two marked sockets with
the inherited recursive MNW terminals or supply the common-cap prefixes.

## 1. Parameters and the common-mate square

Let

\[
 q=d+1\ge 5,\qquad m\ge\max\{q+8,2q+2\}.            \tag{1.1}
\]

Work on a ground set of size `2m-1`, written as the disjoint union

\[
 C\mathbin{\dot\cup}Q\mathbin{\dot\cup}\{a\}
 \mathbin{\dot\cup}Z,
 \qquad |C|=|Z|=m-3,
 \qquad Q=\{q_0,q_1,q_2,q_3\}.                       \tag{1.2}
\]

Indices on the `q`'s are modulo four.  As in the common-mate `C8`, put

\[
\begin{aligned}
 L_j&=C+q_j+q_{j+1},\\
 R_j&=C+q_j+q_{j+1}+q_{j+2},\\
 U_j&=C+a+q_j+q_{j+1}.
\end{aligned}                                        \tag{1.3}
\]

The old phase contains `R_j-L_j-U_j`; its phase-zero switch is

\[
                    L_jR_j\longmapsto L_jR_{j-1}.     \tag{1.4}
\]

Thus the unchanged incoming owner `R_i` enters output path `i` before the
switch and output path `i+1` after it.

Write

\[
 C=\{c_0,\ldots,c_{m-4}\},\qquad
 Z=\{z_0,\ldots,z_{m-4}\},\qquad n=m-1.              \tag{1.5}
\]

Choose

\[
 p_j=c_j,\qquad t_j=c_{j+q},                         \tag{1.6}
\]

and

\[
 d_j=z_{m-4-j}.                                      \tag{1.7}
\]

Condition (1.1) makes the eight core labels in (1.6) and the four neutral
labels in (1.7) distinct.  Let `gamma_j` be the cyclic order of
`C-{p_j}` beginning immediately after `p_j`:

\[
 \gamma_j=(c_{j+1},c_{j+2},\ldots,c_{j-1}).          \tag{1.8}
\]

The label `t_j` is in position `q` of this order.

For the missing pair `\{q_(j+2),q_(j+3)\}`, let `alpha_j` be its
even-indexed member and `beta_j` its odd-indexed member.  Define the
forward departure and arrival orders

\[
\begin{aligned}
 A_j^{\rm out}&=(\gamma_j,a,q_j,q_{j+1}),\\
 B_j^{\rm in}&=(z_0,z_1,\ldots,z_{m-4},\alpha_j,\beta_j).
\end{aligned}                                        \tag{1.9}
\]

Both lists have length `n` and respectively enumerate
`U_j-{p_j}` and `[2m-1]-U_j`.  Starting at `F_(j,0)=U_j`, simultaneously
delete and insert the entries in position `s` to obtain

\[
 F_{j,s}=F_{j,s-1}-A^{\rm out}_{j,s}+B^{\rm in}_{j,s}
 \qquad(1\le s\le n).                               \tag{1.10}
\]

The endpoint is

\[
 B_j:=F_{j,n}=\{p_j\}\cup([2m-1]-U_j).              \tag{1.11}
\]

Put

\[
                         w=n-q.                      \tag{1.12}
\]

The first `n-3` return arrivals consist of `C-{p_j,t_j}` and `q_j`.
For `j=0,1,2`, retain the order induced by `gamma_j-t_j` and insert `q_j`
in position `w`.  For `j=3`, additionally move `c_1,c_2` into positions
`w+1,w+2`, retaining the induced order on every other core label.  Call
this list `rho_j`.  The inequalities in (1.1) make all three positions
legal.

The complete return departure order is

\[
 \bigl(Z-\{d_j\}\text{ in increasing order},
        q_{j+3},d_j,q_{j+2}\bigr),                   \tag{1.13}
\]

and the complete return arrival order is

\[
 \bigl(\rho_j,q_{j+1},t_j,a\bigr).                  \tag{1.14}
\]

Starting at `G_(j,0)=B_j`, let `G_(j,s)` be the states after the first
`s` return exchanges.  Direct cancellation gives

\[
\begin{aligned}
G_{j,n-3}&=(C-t_j)+d_j+q_j+q_{j+2}+q_{j+3},\\
G_{j,n-2}&=(C-t_j)+d_j+q_j+q_{j+1}+q_{j+2},\\
G_{j,n-1}&=R_j,\\
G_{j,n}&=U_j.
\end{aligned}                                        \tag{1.15}
\]

The protected owner cycle is

\[
 \mathcal C_j=(F_{j,0},F_{j,1},\ldots,F_{j,n},
                G_{j,1},\ldots,G_{j,n-1}).           \tag{1.16}
\]

Its final Johnson edge is `R_j-U_j`, through the required lower socket
`L_j`.  Thus (1.16), with every Johnson edge subdivided by its intersection,
is already a closed properly phased incidence cycle; no artificial closure
edge is appended.

## 2. Exact residence

### Lemma 2.1 (position formula)

Consider a complementary square of length `2n`.  If an `A`-side label is
deleted at forward position `u` and restored at return position `v`, its
zero and positive cyclic run lengths are

\[
                         n-u+v,\qquad n+u-v.          \tag{2.1}
\]

For a `B`-side label inserted at `u` and deleted at `v`, the same two
numbers occur in the opposite order.  Hence both runs have length at least
`q` whenever

\[
                         |u-v|\le n-q.               \tag{2.2}
\]

#### Proof

Between the two events the trace crosses the remaining `n-u` forward
states and the first `v` return states.  The complementary arc has the
remaining `2n-(n-u+v)=n+u-v` states.  The `B`-side calculation reverses
zero and one. \(\square\)

### Theorem 2.2 (two-sided depth residence in both phases)

Every nonconstant coordinate on every old cycle \(\mathcal C_j\) has one
positive run and one zero run, both of length at least `q=d+1`.  After the
switch (1.4), the one merged cycle has the same two-sided lower bound.

#### Proof

For an ordinary core label, inserting `q_j` and deleting `t_j` shift its
return position from its forward position by at most two.  The only further
changes are the two controlled moves `c_1,c_2` on path three.  The
exceptional core label `t_j` has positions

\[
                         u=q,\qquad v=n-1.            \tag{2.3}
\]

The active label `q_j` moves from forward position `n-1` to return
position `n-q`; the positions of `a,q_(j+1)` move by at most two.  An
ordinary `Z`-label moves by at most one, `d_j` by at most four, and the two
missing active labels by at most three.  The special moves on path three
have displacement at most `q+1`.  Consequently

\[
 |u-v|\le\max\{n-q-1,q+1,4\}\le n-q                \tag{2.4}
\]

by (1.1).  Lemma 2.1 proves the claim for the four old cycles.  The
permanent coordinate `p_j` is constant there.

It remains to check the four new splices.  For a core coordinate variable
on both adjacent paths, let `u_(j+1)` be its forward departure position on
the next path and `v_j` its return arrival position on the current path.
The new boundary positive run has length

\[
                         n-v_j+u_{j+1}.              \tag{2.5}
\]

For the splices `j=0,1,2`, the cyclic core orders differ by one position,
and (2.5) is at least `n-3`.  At the wrap splice `3 -> 0`, the only two
wrapping labels are `c_1,c_2`; their prescribed return positions
`w+1,w+2` make (2.5) exactly `q`.  A coordinate permanent on either side
only has a longer run.  The late label `t_j` meets the next path at a
forward position at least `q-1`, so its two boundary pieces also total at
least `q`.

Among active labels, `q_j` is the unique label dropped at the splice from
path `j` to path `j+1`.  It was restored at position `w=n-q`, so its
terminal run has length exactly `q`.  The labels `q_(j+1),q_(j+2)` cross
the splice and only gain length; `q_(j+3)` is absent there.  The coordinate
`a` has a forward run of length at least `n-2`, and every `Z`-coordinate is
absent at a splice.  Internal zero gaps are unchanged by the reconnection.
This proves two-sided residence in the switched cycle. \(\square\)

Thus this bank avoids the immutable run-two defect of the former neutral
rail.  It proves both the positive-run and zero-gap inequalities needed for
literal depth-`d` intersection and union flags.

## 3. Resource simplicity and exposure

### Lemma 3.1 (four disjoint induced incidence cycles)

For every `m,q` satisfying (1.1):

1. all owners in the four cycles (1.16) are distinct;
2. all intervening rank-`m-1` intersections are distinct;
3. all adjacent rank-`m+1` unions are distinct; and
4. within any one cycle, a rank-`m-1` set lies below at most two cycle
   owners, and a rank-`m` set lies above at most two selected lower
   vertices.

Consequently the protected bank has

\[
 e_m=16m-16,\qquad \alpha_m\le8,\qquad\beta_m\le8.  \tag{3.1}
\]

#### Proof

Here is a complete signature check.  On either monotone half of one path,
states at positions differing by `h` exchange `h` distinct departure
labels for `h` distinct arrival labels.  Their Johnson distance is therefore
`h`.  On the forward core block, after `s` steps the deleted core labels
form the proper cyclic interval

\[
                         \{c_{j+1},\ldots,c_{j+s}\}. \tag{3.2}
\]

Translations of a proper cyclic interval are distinct.  Across the four
paths at one return position, the active `Q`-signature is one of the four
distinct missing pairs before position `w`, and one of the four distinct
three-sets after `q_j` is restored.  The final exchange changes it to the
four distinct triples `R_j-C`.  Thus the controlled `c_1,c_2` moves on path
three create no collision.  Sets at different positions have different
pairs

\[
                         (|V\cap C|,|V\cap Z|),      \tag{3.3}
\]

except in the final four positions.  Those positions are separated by the
private signatures `(p_j)`, `(t_j,d_j)`, and the four distinct active
triples in (1.15).  A forward state and a nonterminal
return state cannot agree: equality of the two coordinates in (3.3) would
simultaneously require `s+t=m-4` and `s+t=m-3`.

The same comparison after deleting, respectively adjoining, the unique
exchange label proves the assertions for lower intersections and upper
unions.  The only numerically coincident forward/return boundary signature
would compare `Z-{z_(m-4)}` with `Z-{z_0}`; these are different.  At the
return tail the lower facets are, successively,

\[
\begin{aligned}
 &(C-t_j)+d_j+q_j+q_{j+2},\\
 &R_j-t_j,\\
 &L_j,
\end{aligned}                                        \tag{3.4}
\]

which are separated by `t_j,d_j` and then by the active index.  This also
shows directly that no closing facet is reused by the opposite path.

Finally, the monotone-half distance calculation, the count contradiction
in (3.3), and the three tail signatures above show that the radius-one
neighbourhood of a fixed lower set meets any one path in at most the two
endpoints of one edge in one cycle.  The dual statement follows from the
adjacent-union signatures.  Summing the per-cycle bound over four cycles
gives `alpha_m,beta_m<=8`.  There are `2m-2` owner transitions, hence
`4m-4` incidence edges, in each cycle, giving (3.1). \(\square\)

The constants in (3.1) are deliberately conservative.  Literal replay of
the displayed construction gives `alpha_m=beta_m=3` throughout the tested
range, but the stronger numerical value is not needed below.

## 4. All-width current and socket action

### Theorem 4.1 (resident all-width odd actuator)

Switching (1.4) on the four protected cycles has all of the following
properties simultaneously.

1. The signed occurrence-labelled owner-union current is zero at every
   width.
2. Every old and switched owner trace is two-sided depth-`d` resident.
3. The four old cycles become one cycle.
4. On the incoming sockets the output action is the odd four-cycle
   `i -> i+1`.

#### Proof

For `0<=s<=n`, the accumulated forward union on output `j` is

\[
 \bigcup_{h=0}^sF_{j,h}
 =U_j\cup\{B^{\rm in}_{j,1},\ldots,B^{\rm in}_{j,s}\}. \tag{4.1}
\]

Fix the unchanged incoming owner `R_i`.  Initially

\[
 R_i\cup U_i=R_i\cup U_{i+1}
 =C+a+q_i+q_{i+1}+q_{i+2}.                          \tag{4.2}
\]

All `Z`-labels enter the four forward paths at identical positions.  The
only active label missing from (4.2) is `q_(i+3)`.  It is missing from both
outputs `i` and `i+1`, and its parity places it at the same one of the last
two positions in both lists (1.9).  Hence

\[
 R_i\cup\bigcup_{h=0}^sF_{i,h}
 =R_i\cup\bigcup_{h=0}^sF_{i+1,h}                  \tag{4.3}
\]

for every `s`.  At `s=n` either side is the full ground set.  Every longer
crossing interval therefore remains full throughout the return.  Intervals
not crossing a switched incidence are copied literally.  This proves
all-width current zero.

The switch changes no owner and Theorem 2.2 verifies the reconnected cyclic
coordinate traces.  Before the switch the
output beginning at `U_j` returns to `R_j`.  Afterwards incoming `R_i`
enters `U_(i+1)` and returns to `R_(i+1)`.  Thus the first-return action is
the four-cycle `i->i+1`, and the four old components merge into one.
\(\square\)

Marking the alternating sockets `R_0,R_2` gives identity first return in
the old phase and their transposition in the switched phase.  Hence this is
also a literal crossed two-terminal actuator, not merely an abstract odd
sign.

## 5. Spanning phased host

### Corollary 5.1 (automatic ordered-two-SDR coinstantiation)

For every sufficiently large `m` satisfying (1.1), the complete protected
bank (1.16) is contained in a spanning two-factor of `ML_m`, with its
alternating phases fixed.  Switching (1.4) gives a second ordered two-SDR
and retains every conclusion of Theorem 4.1.

#### Proof

By Lemma 3.1,

\[
 e_m=O(m)=2^{o(m)},\qquad \alpha_m,\beta_m=O(1)=o(m). \tag{5.1}
\]

The subexponential low-exposure coinstantiation theorem in
`MATH_OBSTRUCTION_AND_REDUCTION_ALLWIDTH_C8_RESIDENCE_MNW_CAP_COINSTANTIATION_20260813.md`
therefore extends the four properly phased protected cycles to a spanning
two-factor for all sufficiently large `m`.  Protected lower vertices are
saturated, so the four new incidences in (1.4) are absent before the switch.
Alternating each old cycle fixes the required ordered phases. \(\square\)

## 6. Exact remaining interface

This theorem closes, in one literal bank,

\[
 \boxed{\text{all-width current}+
        \text{two-sided residence}+
        \text{phased host}+
        \text{odd/crossed socket action}.}           \tag{6.1}
\]

It supersedes the residence obstruction of the two-slot all-width collar.
It does not yet prove the complete `B(k)+O(1)` construction.  The remaining
joint rows are:

1. replace or cut the two marked returns so that their labels are the
   inherited recursive MNW terminals, obeying
   \(\theta_1=\theta_0\circ s\) rather than merely an isomorphic private
   copy;
2. plant the literal private claim-to-port prefixes in the same bank and
   prove the typed full-port gammoid cut; and
3. select the global positive owner/lower flag factor in which this
   protected bank is reserved.

The first row is now a terminal-labelling problem, not a residence or
all-width algebra problem.  The last row remains the dominant global
positive-semigroup gate.
