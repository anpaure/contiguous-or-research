# Audit of the \(\mathbb Z_4^r\) tensor successor and packet collisions

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Identify the vertices in a product of \(r\) oriented local \(C_4\)'s with
\(\mathbb Z_4^r\), and consider

\[
 F(x)=x+e_{\jmath(x)},\qquad
 \jmath(x)=1+\left(\sum_{i=1}^r x_i\bmod r\right).
\tag{0.1}
\]

The proposed statement is false for asymptotic \(r\):

\[
 \boxed{F\text{ is a }C_{4r}\text{-factor with cyclic block schedule}
 \iff r\mid4.}
\tag{0.2}
\]

Thus it works only for \(r=1,2,4\).  For every other \(r\ge3\), \(F\)
is not even injective.  The first counterexample is at \(r=3\):

\[
 F(0,0,0)=F(1,3,0)=(1,0,0).
\tag{0.3}
\]

For the valid values of \(r\), and also for the existing Hamming
\(C_{4r}\)-factor with the same projected block schedule, the lower and
upper \(q\)-shadow maps are injective across all product cells of one
canonical packet for every \(q\le r\).

They are not injective across canonical packets.  A collision already
occurs for \(r=2,q=1\), both below and above.  The phase checksum in
(0.1) does not distinguish it.

A precise sufficient repair is a persistent cycle tag.  The collision
graph of \(C_{4r}\)-blocks through depths \(q\le Q\) has maximum degree at
most

\[
 8rQ\binom{m+Q+1}{Q}.
\tag{0.4}
\]

It can therefore be coloured with

\[
 g=O\!\left(
 Q\log\frac{e(m+Q)}Q+\log(rQ)
 \right)
\tag{0.5}
\]

bits.  If these \(g\) bits can be carried by a guard which is visible in
every emitted shadow of its cycle, cross-cycle collisions disappear.  Its
total length cost is \(O(gW/r)=o(W)\) whenever

\[
                         Q\log\frac{em}{Q}=o(r).
\tag{0.6}
\]

Constructing such a persistent guard inside the original untagged set
system is an additional interface theorem; graph colouring alone does not
create it.

## 1. The wrap obstruction

Use the representatives \(0,1,2,3\) for \(\mathbb Z_4\) coordinates and
write

\[
                         s(x)=\sum_i x_i\bmod r.
\tag{1.1}
\]

When \(F\) increments a coordinate which is \(0,1,\) or \(2\), the
integer-coordinate sum increases by one.  When it increments \(3\) to
\(0\), the sum changes by \(-3\).  Therefore

\[
 s(Fx)=s(x)+1\pmod r\quad\text{for every }x
 \iff -3\equiv1\pmod r
 \iff r\mid4.
\tag{1.2}
\]

This congruence is exactly what the claimed cyclic schedule needs.

### Proposition 1.1 (complete classification)

The map \(F\) in (0.1) partitions \(\mathbb Z_4^r\) into cycles of length
\(4r\), with block schedule

\[
 1,2,\ldots,r,\ 1,2,\ldots,r,\ 1,2,\ldots,r,\ 1,2,\ldots,r,
\tag{1.3}
\]

up to cyclic rotation, if and only if \(r\in\{1,2,4\}\).

#### Proof: the positive direction

Assume \(r\mid4\).  Equation (1.2) shows that the chosen block advances
by one at every step.  Consequently every block is incremented exactly
once in \(r\) steps:

\[
                         F^r(x)=x+\mathbf1.
\tag{1.4}
\]

It follows that \(F^{4r}(x)=x\).  If \(t=ar+b<4r\), with
\(0\le b<r\), then after \(t\) steps \(b\) coordinates have been
incremented \(a+1\) times and the remaining coordinates \(a\) times.
For \(b>0\) these cannot all vanish modulo four; for \(b=0\), they vanish
only when \(4\mid a\).  Thus the first return is at \(4r\).

Every local \(C_4\) alternates its two physical cube directions.  In any
\(2r\) consecutive steps of (1.3), each block is used twice and hence
each of its two directions is used once.  The resulting \(C_{4r}\) is
therefore isometric in \(Q_{2r}\).  All \(F\)-orbits have this form, so
they factor the vertex set.

#### Proof: the negative direction

Assume \(r\nmid4\), and put

\[
                         j'=1+(4\bmod r).
\tag{1.5}
\]

Then \(j'\ne1\).  Let \(z=e_1\), let \(x=0\), and let \(y\) have value
one in coordinate \(1\), value three in coordinate \(j'\), and zero
elsewhere.  Clearly

\[
                         \jmath(x)=1,\qquad F(x)=e_1=z.
\tag{1.6}
\]

But \(\sum_i y_i=4\), so \(\jmath(y)=j'\), and incrementing its
\(j'\)-coordinate wraps \(3\) to zero.  Hence \(F(y)=e_1=z\), while
\(x\ne y\).  Thus \(F\) is not injective.  At \(r=3\) this is exactly
(0.3). \(\square\)

The obstruction is structural.  A phase function on a directed local
four-cycle which increases by one modulo \(r\) at every edge can exist
only if \(4=0\) in \(\mathbb Z_r\).

## 2. The correct large-\(r\) block schedule

The failure of (0.1) does not remove the useful schedule.  Suppose

\[
                         h=2r
\tag{2.1}
\]

is a power of two.  In the Hamming \(C_{2h}=C_{4r}\)-factor of \(Q_h\),
order the \(2r\) physical directions as

\[
 (1,0),(2,0),\ldots,(r,0),
 (1,1),(2,1),\ldots,(r,1).
\tag{2.2}
\]

The standard direction word repeats (2.2) twice.  After projecting
\((i,\eta)\mapsto i\), its block schedule is exactly

\[
                         1,2,\ldots,r
\tag{2.3}
\]

repeated four times.  Every window of at most \(r\) steps uses distinct
blocks, and every window of at most \(2r\) steps uses distinct physical
directions.  Thus the existing Hamming theorem supplies the large-\(r\)
factor which (0.1) was intended to produce, though without its scalar
checksum.

An external clock also repairs (0.1): on
\(\mathbb Z_4^r\times\mathbb Z_r\),

\[
 G(x,t)=(x+e_{t+1},t+1)
\tag{2.4}
\]

has \(C_{4r}\)-orbits with the desired schedule.  It uses an \(r\)-fold
cover of the original support, so it is not a coefficient-one replacement
without a further quotient or clock-encoding theorem.

## 3. Exact injectivity inside one tensor packet

Fix one of the two local associator resolutions.  Orient its six local
four-cycles, and write

\[
 \gamma_K(z),\qquad K\in[6],\ z\in\mathbb Z_4
\tag{3.1}
\]

for their middle vertices.  Directly from the local frame,

\[
 (K,z)\longmapsto
 \gamma_K(z)\cap\gamma_K(z+1)
\tag{3.2}
\]

is injective over all 24 oriented edges; the analogous union map is also
injective.  Indeed, the four big squares have lower patterns consisting
of one special and two reservoir coordinates, while the two reservoir
squares have two special and one reservoir coordinate, and all labelled
patterns within each class are distinct.  Complementing this argument
proves the upper statement.

Take a product cell tuple
\(\mathbf K=(K_1,\ldots,K_r)\), a phase vector
\(x\in\mathbb Z_4^r\), and any cycle factor whose block schedule has no
repeat in \(q\le r\) consecutive steps.  Its lower \(q\)-shadow has, in
each changed block \(i\),

\[
 \gamma_{K_i}(x_i)\cap\gamma_{K_i}(x_i+1),
\tag{3.3}
\]

and has the unchanged middle state \(\gamma_{K_i}(x_i)\) in every other
block.  Local block weights distinguish changed blocks from unchanged
ones.  Equations (3.1)--(3.2) then recover every \(K_i,x_i\).

### Theorem 3.1 (packetwise shadow injectivity)

For every \(q\le r\), the lower and upper \(q\)-shadow maps are injective
over all starts and all product cells in one fixed tensor-packet
resolution, both for the valid instances of (0.1) and for the corrected
Hamming schedule (2.2).

This is stronger than cellwise injectivity: different product cells in
the same packet cannot collide.

## 4. The smallest canonical-packet collision

Packetwise injectivity does not recover the canonical packet itself.
Here is an explicit collision already at \(r=2,q=1\), where (0.1) is
valid.

Use three physical 8-blocks in the order \(A<B<C\).  In each block use
the oriented local square

\[
 z_0=acuw,\quad z_1=bcuw,\quad z_2=bduw,\quad z_3=aduw.
\tag{4.1}
\]

Its first lower and upper decorations are

\[
                         \ell=cuw,\qquad u=abcuw.
\tag{4.2}
\]

Choose all earlier blocks ineligible and freeze a common outside core of
the needed size.

### Lower collision

Let the target have local restrictions

\[
                         R_A=\ell,\quad R_B=\ell,\quad R_C=z_0.
\tag{4.3}
\]

It has two middle extensions:

\[
 \begin{array}{c|ccc|c}
 &A&B&C&\text{first two eligible blocks}\\ \hline
 S_A&z_0&\ell&z_0&A,C\\
 S_B&\ell&z_0&z_0&B,C.
 \end{array}
\tag{4.4}
\]

In the product coordinates of either packet, both sources have phase
\((0,0)\).  Hence \(\jmath=1\), and the successor changes the first
selected block.  Both lower shadows are exactly \(R\).

### Upper collision

Let the upper target have

\[
                         T_A=u,\quad T_B=u,\quad T_C=z_0.
\tag{4.5}
\]

The two middle sources

\[
 \begin{array}{c|ccc|c}
 &A&B&C&\text{first two eligible blocks}\\ \hline
 S'_A&z_0&u&z_0&A,C\\
 S'_B&u&z_0&z_0&B,C
 \end{array}
\tag{4.6}
\]

again have phase \((0,0)\), and their first upper shadows both equal
\(T\).

Thus neither the local edge injectivity nor the scalar phase checksum
recovers the canonical packet.  The same construction with many
\(\ell\)-blocks gives arbitrarily large collision multiplicity.

## 5. A precise persistent-tag repair

Let \(\mathscr C\) be any exact \(C_{4r}\)-factor of the retained middle
support.  Define its depth-\(Q\) collision graph \(\Gamma_Q\):

* vertices are the cycles of \(\mathscr C\);
* two cycles are adjacent if they have a common lower or upper
  \(q\)-shadow for some \(1\le q\le Q\).

A fixed cycle has \(4r\) starting positions, two signs, and \(Q\) depths,
so it supplies at most \(8rQ\) relevant shadow occurrences.  A lower
rank-\((m-q)\) target lies in at most

\[
                         \binom{m+q+1}{q}
\tag{5.1}
\]

middle \(m\)-sets, and an upper rank-\((m+q)\) target contains at most
\(\binom{m+q}{q}\) middle \(m\)-sets.  Since every middle set belongs to
one cycle,

\[
 \boxed{
 \Delta(\Gamma_Q)
 \le
 8rQ\binom{m+Q+1}{Q}.}
\tag{5.2}
\]

Greedy colouring therefore assigns every cycle a colour of

\[
 g=
 \left\lceil
 \log_2\!\left(
 1+8rQ\binom{m+Q+1}{Q}
 \right)
 \right\rceil
 =
 O\!\left(
 Q\log\frac{e(m+Q)}Q+\log(rQ)
 \right)
\tag{5.3}
\]

bits so that colliding cycles have different colours.

### Guard condition

Assume the block-to-array interface can attach these \(g\) colour bits to
each cycle in a form which

1. is unchanged throughout that cycle block;
2. is visible in every lower and upper shadow emitted by the block; and
3. costs \(O(g)\) additional array entries per cycle.

Then equality of two tagged shadows forces equality of their tags, hence
their cycles are nonadjacent in \(\Gamma_Q\); within a cycle,
Theorem 3.1 recovers the start.  Thus all tagged shadow maps through depth
\(Q\) are globally injective.

There are \(W/(4r)\) cycles.  The total guard cost is

\[
 O\!\left(\frac{gW}{r}\right)=o(W)
\tag{5.4}
\]

under (0.6).

This is an exact sufficient condition and an exact cost calculation.  It
does not assert that the original set-union representation already
contains such persistent tags.  Realizing the tags without changing the
target masks is the remaining guard-interface gate.

## 6. Final audit

The autonomous successor (0.1) cannot be the asymptotic tensor factor:
the local \(4\)-cycle wrap destroys its clock unless \(r\mid4\).  The
existing Hamming factor supplies the intended block schedule for all
admissible large \(r\), and its \(q\le r\) shadows are exactly injective
inside each canonical tensor packet.

The first genuine collision is cross-packet, not cross-cell.  It appears
at \(r=2,q=1\) and survives the proposed checksum.  A persistent
cycle-colour guard would remove all such collisions at \(o(W)\) cost in
the regime \(Q\log(em/Q)=o(r)\); constructing that guard in the untagged
model is the sharply isolated remaining problem.
