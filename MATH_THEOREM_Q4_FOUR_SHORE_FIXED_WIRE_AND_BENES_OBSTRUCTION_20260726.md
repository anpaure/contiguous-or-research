# The \(Q_4\) four-shore cube has a fixed-point-free opposite, but no
# transverse Beneš layer

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

For the standard common-phase \(Q_4\) factor, let

\[
A=(1\ 3),\qquad B=(2\ 4).
\tag{0.1}
\]

All four twists

\[
\mathrm{id},\quad A,\quad B,\quad AB
\tag{0.2}
\]

are exact neighbour permutations with the same phase classes.  The
opposite permutation

\[
AB=(1\ 3)(2\ 4)
\tag{0.3}
\]

is fixed-point-free.  Thus this square does improve on the earlier
one-transposition shore.

However, it is not a four-way switch.  Its action has the two invariant
wires

\[
\{1,3\},\qquad\{2,4\}.
\tag{0.4}
\]

The only Yang--Baxter identity inside the square is the commuting square
\(AB=BA\).  It does not re-pair the wires.

This defect is statewise.

> **Transverse-layer no-go.**  No full-direction colouring
> \(\delta:Q_4\to[4]\) can have all four transpositions
> \[
> (1\ 3),\ (2\ 4),\ (1\ 2),\ (3\ 4)
> \]
> in its twist bank together with the identity.

Consequently the \(A/B\) square cannot itself be followed by the
transverse matching needed for a two-stage butterfly or Beneš crossbar.
A larger associator must change the phase partition, not merely choose
another shore of the same \(Q_4\) cube.

There is also an exact entropy loss.  In any fixed-frame tensor of these
squares, a completed \(d\)-set has at most \(2^d\) images under all shore
choices.  Including the \(r\) cyclic starting positions gives at most
\(r2^d\) supports.  The aligned paired trace therefore has distinct-code
proportion at most

\[
\boxed{\frac{2r}{2^d}.}
\tag{0.5}
\]

It has asymptotically total collision once
\(d-\log_2r\to\infty\), despite the fixed-point-free opposite shore and
despite an exponential number of full cyclic orders.

Thus the four-shore cube solves local ownership and local displacement,
but provably supplies only one visible switch bit per erased direction.
The physical trace needs two.

## 1. The four exact shores

Use the standard phase colouring from the common-phase \(Q_4\) factor.
Its four phase-pair classes are

\[
\begin{aligned}
C_1&=H,\\
C_2&=1000+H,\\
C_3&=1100+H,\\
C_4&=1110+H,
\end{aligned}
\qquad
H=\langle e_1+e_3,\ e_2+e_4\rangle.
\tag{1.1}
\]

The base outgoing direction at class \(C_i\) is \(i\).  A coordinate
permutation \(\sigma\) is a valid twist exactly when

\[
\{C_i+e_{\sigma(i)}:i\in[4]\}
\tag{1.2}
\]

partitions \(Q_4\).

Both \(C_1,C_3\) are invariant under \(e_1+e_3\), and both
\(C_2,C_4\) are invariant under \(e_2+e_4\).  Therefore replacing
the assigned directions \(1,3\) by \(3,1\), or \(2,4\) by \(4,2\),
does not change the translated partition.  This proves:

### Proposition 1.1

All four permutations in (0.2) belong to the twist bank.  Their
direction words, in common phase, are

\[
\begin{array}{c|c}
\mathrm{id}&1234\,1234\\
A&3214\,3214\\
B&1432\,1432\\
AB&3412\,3412.
\end{array}
\tag{1.3}
\]

Every row is an isometric \(C_8\)-factor.  The pair
\((\mathrm{id},AB)\) is a same-owner double factor with a
fixed-point-free relative permutation.

The last assertion removes the fixed-coordinate subgroup from the
affine trace formula at shallow supports which take at most one member
from each pair in (0.4).  It does not remove the separate support-entropy
cut proved below.

### Proposition 1.2 (fixed-point-free is not phase-rainbow)

Take the opposite shore \(S=AB\), and form a parallel tensor/recursive
product of these \(Q_4\) cells.  Suppose a shallow window visits \(d\)
different bottom cells once each.  Then its aligned affine physical trace
has multiplicity at least

\[
                         2^{d-1}.
\tag{1.4}
\]

#### Proof

In one touched cell, let \(q\) be the selected direction.  The affine
physical trace erases phase coordinates \(q\) and \(Sq\).  The direction
fibre is one coset of \(H\), and

\[
                         e_q+e_{Sq}\in H.
\tag{1.5}
\]

Thus the selected direction and the other two phase bits leave exactly
two possible local phase words, differing by \(e_q+e_{Sq}\).

The \(d\) touched cells give \(d\) independent ambiguity bits.  The full
physical trace supplies only the one global even-context checksum

\[
                         \bigoplus_{i\in SJ}y_i,
\tag{1.6}
\]

which imposes one linear equation on those bits.  Hence at least
\(2^{d-1}\) phase words remain.

Every ambiguity vector has even weight, so it preserves the side schedule
of the parallel recursion.  Each bottom cell is visited only once, and
the alternative point stays in the same direction fibre, so the complete
support \(J\) is unchanged.  The surviving phase words therefore give
literal starts in one physical trace fibre. \(\square\)

This explains why the cross-once \(Q_8\) construction is stronger than
the fixed-point-free \(AB\) shore.  The crossed selected side reveals the
total parity of each touched \(Q_8\) block separately, converting the one
global checksum (1.6) into one local checksum per visit.  Fixed-point-free
displacement alone does not do that.

## 2. Fixed-wire support entropy

Let

\[
\mathcal P=\bigl\{\{1,3\},\{2,4\}\bigr\}.
\tag{2.1}
\]

Every member of \(\langle A,B\rangle\) preserves each block of
\(\mathcal P\).  Hence, for any \(J\subseteq[4]\),

\[
\bigl(|J\cap\{1,3\}|,\ |J\cap\{2,4\}|\bigr)
\tag{2.2}
\]

is shore-invariant.  Only a block met in exactly one point can change,
and then it has two images.  Therefore

\[
|\{gJ:g\in\langle A,B\rangle\}|
=2^{s(J)},
\tag{2.3}
\]

where \(s(J)\) is the number of split blocks of \(\mathcal P\).
In particular,

\[
|\{gJ:g\in\langle A,B\rangle\}|\le2^{|J|}.
\tag{2.4}
\]

Now tensor the square over a fixed partition of \(r\) directions into
two-point wires, and allow arbitrary context-dependent shore choices in
every cell and every layer, provided every layer preserves these wires.
For one base cyclic \(d\)-interval, each of its \(d\) selected directions
has at most two possible mates, so (2.4) tensorizes:

\[
\#\{\text{images of one base \(d\)-interval}\}\le2^d.
\tag{2.5}
\]

There are at most \(r\) base cyclic intervals.  Hence the complete
support library has size

\[
L_d\le r2^d.
\tag{2.6}
\]

An aligned paired physical trace records a support \(J\) and the two
outside bit strings \(p|_{J^c},x|_{J^c}\).  Thus it has at most

\[
r2^d\,2^{2(r-d)}
\tag{2.7}
\]

values on \(2^{2r-1}\) even-context starts.  Dividing proves (0.5).

### Corollary 2.1

No fixed-wire composition of the \(Q_4\) four-shore cubes gives
near-injective aligned traces at any depth satisfying

\[
d-\log_2r\longrightarrow\infty.
\tag{2.8}
\]

The conclusion permits arbitrary Boolean control functions and
arbitrarily many repeated layers.  What fails is not the number of full
orders; it is the number of distinct interval supports.

## 3. A transverse second layer is impossible on \(Q_4\)

We use the local period law for twist banks:

### Lemma 3.1

If both \(\mathrm{id}\) and \((i\ j)\) are valid twists of a colouring
\(\delta\), then

\[
C_i+(e_i+e_j)=C_i,\qquad
C_j+(e_i+e_j)=C_j.
\tag{3.1}
\]

#### Proof

Compare the two translated-colour partitions.  All classes except
\(C_i,C_j\) have the same translate.  After translating the remaining
equality by \(e_i\), one gets

\[
C_i\mathbin{\dot\cup}(C_j+e_i+e_j)
=(C_i+e_i+e_j)\mathbin{\dot\cup}C_j.
\]

Disjointness forces each of \(C_i,C_j\) to be invariant under the
displayed translation. \(\square\)

### Theorem 3.2 (no two transverse perfect-matching layers)

There is no full-direction colouring \(\delta:Q_4\to[4]\) whose twist
bank contains

\[
\mathrm{id},\ (1\ 3),\ (2\ 4),\ (1\ 2),\ (3\ 4).
\tag{3.2}
\]

#### Proof

Lemma 3.1 gives the period subspaces

\[
\begin{aligned}
H_1&=\langle e_1+e_3,e_1+e_2\rangle,\\
H_2&=\langle e_2+e_4,e_2+e_1\rangle,\\
H_3&=\langle e_3+e_1,e_3+e_4\rangle,\\
H_4&=\langle e_4+e_2,e_4+e_3\rangle.
\end{aligned}
\tag{3.3}
\]

Every \(H_i\) is a two-dimensional subspace of the even shore
\(E_4\), and the four \(H_i\)'s are pairwise distinct.  Since every
colour is used, every \(C_i\) is a nonempty union of \(H_i\)-cosets and
therefore has size at least four.  The four disjoint classes partition
the sixteen vertices, so each \(C_i\) is exactly one affine coset of
\(H_i\).

Each \(H_i\) lies in \(E_4\), so each \(C_i\) lies wholly in one parity
shore.  Each shore has eight vertices and is therefore the disjoint
union of exactly two of the \(C_i\)'s.

But two affine planes in the three-dimensional affine space \(E_4\)
are disjoint only when they are parallel, i.e. have the same direction
subspace.  The \(H_i\)'s are pairwise distinct.  Thus no two \(C_i\)'s
can partition one parity shore, a contradiction. \(\square\)

By relabelling, the same proof excludes any two distinct perfect
matchings of \(K_4\): their union is a four-cycle, and the four incident
star-period spaces are pairwise distinct.

## 4. Yang--Baxter verdict and the surviving object

The \(A/B\) square satisfies

\[
R_AR_B=R_BR_A
\tag{4.1}
\]

because the switches are disjoint.  This is a commuting square, not the
braid relation needed to change wire frames.  Theorem 3.2 shows that a
second transverse square cannot live in the same \(Q_4\) phase
partition.  Therefore iterating the local four-shore cube, even with
arbitrary context bits, remains a fixed-wire network and is subject to
Corollary 2.1.

A genuine Beneš-style escape must use a larger owner trade with two
different phase kernels.  Equivalently, it needs an associator which
changes the wire matching between layers while preserving the exact
row/column Latin equations.  Such an associator cannot be obtained by
choosing another one of the four shores in (0.2).

The smallest surviving finite target is therefore:

> Find a common-owner factor trade on \(Q_8\) or larger which carries the
> \(\{13,24\}\) wire frame to a transverse frame, satisfies the
> predecessor identity needed by the parity lift, and has a
> fixed-point-free opposite shore.  Two alternating frame layers would
> then be the first network capable of exposing two support bits per
> erased direction.
