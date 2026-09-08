# A four-shore `Q_4` twist cube with a fixed-point-free opposite shore

Date: 2026-07-26

Method: exact algebra only.

## 0. Outcome

The standard two-cycle factor of `Q_4` has not merely the previously used
twist `(2 4)`, but two independent same-vertex direction twists

\[
                 A=(1\ 3),\qquad B=(2\ 4).
\]

For every `epsilon=(epsilon_1,epsilon_2) in F_2^2`, twisting the outgoing
direction at every vertex by

\[
                 S_\epsilon=A^{\epsilon_1}B^{\epsilon_2}
\]

again gives an exact factor of `Q_4` into two isometric `C_8`'s.  Thus the
same sixteen owners admit four exact shores.  The opposite-shore twist

\[
                 AB=(1\ 3)(2\ 4)
\]

is fixed-point-free on the four directions.  This removes the particular
"at least half the directions are fixed" obstruction proved for a tensor
of one-bit `(2 4)` braids.

The four shores share a common phase modulo four, and every four-step
half-cycle has the shore-independent port

\[
                 x\longmapsto x+\mathbf1.
\]

They also yield genuinely nonlinear parity-complete maps and hence exact
pair-clustered `C_16`-factors of `Q_8`.

This is a local positive theorem, not yet the Gaussian trace theorem.  A
single `Q_4` block is information-theoretically too small.  The precise
remaining question is whether overlapping four-shore layers compose as a
high-rate switch network while preserving owner exactness.  Disjoint
fixed blocks do not suffice, because changing only the internal order of a
fully contained block does not change the underlying completed support.

## 1. The standard syndrome factor

Let `V=F_2^4`.  Write `G=F_2^2=<alpha,beta>` and define

\[
 Qe_1=Qe_3=\alpha,\qquad Qe_2=Qe_4=\beta.             \tag{1.1}
\]

Identify the four values of `G` with the four directions by

\[
 0\leftrightarrow1,\quad
 \alpha\leftrightarrow2,\quad
 \alpha+\beta\leftrightarrow3,\quad
 \beta\leftrightarrow4.                              \tag{1.2}
\]

Let `delta_0(x)` be the direction corresponding to `Qx`.  Then the
successor

\[
                         G_0(x)=x+e_{\delta_0(x)}       \tag{1.3}
\]

is the standard factor from the common-phase `Q_4` table.  Indeed, the
syndrome values evolve as

\[
 0\longmapsto\alpha\longmapsto\alpha+\beta
 \longmapsto\beta\longmapsto0,                       \tag{1.4}
\]

so the direction word is `1234 1234`.

Put

\[
                         A=(1\ 3),\qquad B=(2\ 4),    \tag{1.5}
\]

and let `H=<A,B> congruent F_2^2`.

## 2. Four exact shores

For `S in H`, define

\[
                         G_S(x)=x+e_{S\delta_0(x)}.    \tag{2.1}
\]

### Theorem 2.1 (four-shore twist cube)

Every `G_S` is a neighbor permutation of `Q_4` whose components are two
isometric `C_8`'s.  Its direction word on every component is

\[
                         S(1)S(2)S(3)S(4)
                         S(1)S(2)S(3)S(4).            \tag{2.2}
\]

Consequently the four factors `G_I,G_A,G_B,G_{AB}` are four exact
partitions of the same sixteen-owner support.

#### Proof

Both generators only interchange directions with equal columns in
(1.1).  Hence, for every `u in {1,2,3,4}` and every `S in H`,

\[
                         Qe_{Su}=Qe_u.                \tag{2.3}
\]

It follows that the syndrome of `G_Sx` is obtained from `Qx` by the same
transition (1.4) as for `G_0`.  During the first four moves the selected
directions are therefore

\[
                         S(1),S(2),S(3),S(4),         \tag{2.4}
\]

which are all four directions once each.  Thus

\[
                         G_S^4x=x+\mathbf1.           \tag{2.5}
\]

Since `Q1=0`, the next four directions repeat (2.4), and `G_S^8x=x`.
No shorter positive prefix returns: before time four it toggles a
nonempty proper subset of four distinct coordinates, at time four it is
at the complement, and between times four and eight it has toggled the
complement of a nonempty proper subset.  Hence every orbit has length
eight.  A doubled-permutation direction word is an isometric `C_8`, and
the orbits of a permutation partition all sixteen vertices. \(\square\)

### Corollary 2.2 (fixed-point-free opposite shore)

At every owner `x`, the outgoing directions in the opposite shores
`G_S` and `G_{ABS}` are related by the fixed-point-free permutation

\[
                         AB=(1\ 3)(2\ 4).             \tag{2.6}
\]

In particular no direction is invisible to the opposite-shore change.

This is exactly the property absent from the one-bit `B=(2 4)` primitive,
which fixes directions `1,3`.

## 3. Common four-phase and common antipodal ports

Let `c_4(x) in Z_4` be the index of `Qx` in the oriented cycle (1.4).
Equation (2.3) gives, simultaneously for all four shores,

\[
                         c_4(G_Sx)=c_4(x)+1.          \tag{3.1}
\]

Thus the factors have one common phase modulo four.  Equation (2.5) also
gives the shore-independent half-cycle port

\[
                         x\stackrel{4\ {m moves}}{\longmapsto}
                         x+\mathbf1.                  \tag{3.2}
\]

The qualification "modulo four" matters.  The factors need not share a
single `Z_8` phase coloring, and common ports alone do not prove that
arbitrary partial cycle choices preserve an owner factor.  What (3.1)--
(3.2) do provide is the exact finite datum needed for a possible
multilayer, antipodally doubled switch compiler.

## 4. Nonlinear parity-complete maps

Let

\[
 E=\{p\in F_2^4:|p|\equiv0\pmod2\}.
\]

Choose functions `a,b:E -> F_2` satisfying

\[
 a(p)=a(p+e_1+e_3),\qquad
 b(p)=b(p+e_2+e_4).                                  \tag{4.1}
\]

Define

\[
 d_p(x)=A^{a(p)}B^{b(p)}\delta_0(x),\qquad
 F_p(x)=x+e_{d_p(x)}.                                \tag{4.2}
\]

### Theorem 4.1 (two-bit nonlinear complete mapping)

Every row `F_p` is an exact two-`C_8` factor.  For every fixed `x`,

\[
                         T_x(p)=p+e_{d_p(x)}          \tag{4.3}
\]

is a bijection from the even shore to the odd shore of `Q_4`.
Conversely, within the four-shore ansatz (4.2), bijectivity for every `x`
forces the two invariances in (4.1).

#### Proof

The row assertion is Theorem 2.1.  Fix `x`.  If `delta_0(x)` lies in
`{1,3}`, the selected direction depends only on `a(p)`.  For an odd
target `q`, its only possible predecessors using these two directions are

\[
                         p_1=q+e_1,\qquad p_3=q+e_3.  \tag{4.4}
\]

Exactly one maps to `q` precisely when

\[
                         a(p_1)=a(p_3).               \tag{4.5}
\]

Since `p_1+p_3=e_1+e_3`, this is the first invariance in (4.1).
The same argument for the pair `{2,4}` gives the second invariance.
The two cases cover all four syndrome phases, proving sufficiency and
necessity. \(\square\)

The functions in (4.1) need not be affine.  For example

\[
                         a(p)=p_2p_4,\qquad
                         b(p)=p_1p_3                 \tag{4.6}

\]

are invariant under the required translations and are genuinely
quadratic on the three-dimensional even shore.  The parity-complete lift
therefore gives an exact physical factor of `Q_8` into sixteen isometric
`C_16`'s with genuinely nonlinear context dependence.

## 5. What this does and does not solve

The theorem removes two possible false obstructions:

1. exact row cycles and exact parity-column ownership do not force an
   affine direction array;
2. a local exact twist primitive need not leave a positive fraction of
   directions fixed between opposite shores.

It does not yet give the required trace code.  Inside one fixed quartet,
the completed support of a window containing the whole quartet is
independent of its internal shore.  Therefore a tensor over disjoint
quartets still has only boundary-scale support information.

The surviving finite-to-asymptotic gate is now precise:

> Arrange overlapping quartet layers, using the two independent switches
> `A` and `B`, so that their composition is an exact owner factor and the
> induced direction-order network has rate-one completed-support entropy.

At the word level the two generators are independent `2 x 2` switches,
so a butterfly or Beneš network can generate arbitrary coordinate
permutations.  The unproved content is physical: successive overlapping
layers must be shown to preserve the partition of cube owners and the
isometric doubled-permutation cycle structure.  A Yang--Baxter/common-
collar identity would prove this; an invariant of the common-owner tiling
would refute it.
