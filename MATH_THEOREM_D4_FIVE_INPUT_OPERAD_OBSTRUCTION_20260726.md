# Five-input `D_4` operad packets: equal size, but no dense common-port suspension

Date: 2026-07-26

This note audits the proposed root-aligned packet

\[
                 P[A_1,A_2,A_3,A_4,A_5],
                 \qquad P\in\mathcal D_4,             \tag{0.1}
\]

where the five ordered spectator trees are fixed and the outer four-node
binary-tree skeleton `P` varies over its fourteen bracketings.

The combinatorial fibre is genuine: all fourteen trees have the same
size and the spectators keep their planar order.  The existing
port-substitution theorem nevertheless does **not** lift through this
five-input operation.  The early spectator slots move in the absolute
Dyck coordinate order when `P` changes, so there is no common local
eight-coordinate set and no fixed exterior port state.  A one-node
spectator in slot two gives a complete ten-coordinate counterexample.

Under the literal token-preserving common-port interface, only the last
two spectator slots are position-stable.  Even granting every such packet,
their total incidence is at most

\[
                       \left({7\over32}+o(1)\right)C_s, \tag{0.2}
\]

so they cannot partition all but `o(C_s)` roots.  The already proved
right-suffix, first-insertion-visible subfamily is smaller, of density
`7/128+o(1)`.

Thus the proposed five-input root skeleton does not supply the missing
dense parent-aligned bank.  A row-dependent multi-input construction is
not ruled out, but it would require a new global `X/Y` composition theorem;
it is not a suspension of the finite `D_4` factor through the existing
common-port functor.

## 1. Catalan operad notation

Encode a full ordered binary tree `T` with `t` internal nodes by its full
prefix word

\[
                         \widehat w(T)\in\{1,0\}^{2t+1}, \tag{1.1}
\]

where `1` is an internal node and `0` is a leaf.  The word has `t` ones
and `t+1` zeros.  Deleting its last zero gives the usual Dyck word
`w(T)` of semilength `t`.

The nonsymmetric operad composition in (0.1) replaces the `i`-th zero of
`widehat w(P)` by `widehat w(A_i)`.  Hence

\[
       |P[A_1,\ldots,A_5]|
               =4+\sum_{i=1}^5|A_i|,                 \tag{1.2}
\]

independently of `P`.  Since the leaves are ordered from left to right,
the tuple `(A_1,...,A_5)` is neither permuted nor absorbed when the outer
bracketing changes.  In particular every fixed tuple gives fourteen
distinct trees of one common size.

This proves the positive set-theoretic part of the proposal.  It does not
yet give a common Boolean-coordinate interface.

## 2. The moving-slot obstruction

Let `lambda_i(P)` be the position of the `i`-th zero in the nine-letter
full word `widehat w(P)`.  Directly over the fourteen Dyck words of
semilength four,

\[
\begin{array}{c|c}
i&\{\lambda_i(P):P\in\mathcal D_4\}\\ \hline
1&\{2,3,4,5\}\\
2&\{4,5,6\}\\
3&\{6,7\}\\
4&\{8\}\\
5&\{9\}.
\end{array}                                                   \tag{2.1}
\]

If `n_i=|A_i|`, replacement of the preceding leaves adds
`2(n_1+...+n_(i-1))` symbols.  Thus the first coordinate of spectator
`A_i` occurs at

\[
        \lambda_i(P)+2\sum_{k<i}n_k,                  \tag{2.2}
\]

which is independent of `P` only for `i=4,5`.

### Proposition 2.1 (no general five-input common-port functor)

If a nonempty spectator occupies one of the slots `1,2,3`, the literal
token-preserving operad family (0.1) is not, in general, a common aligned
`D_4` port cylinder.  Consequently equality of the small `D_4` `X/Y`
ledgers does not imply equality of the five-input lifted ledgers.

#### Proof

A common aligned port cylinder requires one fixed local coordinate set
`J` of size eight, one fixed exterior selected set `O`, and roots

\[
                            O\cup\iota(P),
                            \qquad P\in\mathcal D_4,   \tag{2.3}
\]

under one row-independent coordinate injection `iota`.  In particular
every coordinate of a fixed spectator must retain the same physical label
in all fourteen rows.  Formula (2.2) fails this requirement in slots
`1,2,3`.  The explicit ten-coordinate obstruction in Section 3 shows
that this is not merely a choice-of-notation issue.  \(\square\)

The statement is about the existing common-port suspension.  Allowing a
different embedding in every row removes (2.3), but then neither the
local `X` ledger nor the local `Y` ledger has one common physical
push-forward.  Exactness would have to be proved again from scratch.

## 3. A complete `s=5` port-ledger counterexample

Take the one-node spectator with Dyck word `10` in input slot two and
leave the other four inputs empty.  Replacing the second zero in each
full `D_4` word by `100` gives the fourteen Dyck words

\[
\begin{array}{llll}
1111010000,&1110110000,&1110100100,&1110100010,\\
1101110000,&1101100100,&1101100010,&1101001100,\\
1101001010,&1011110000,&1011100100,&1011100010,\\
1011001100,&1011001010.
\end{array}                                                   \tag{3.1}
\]

Among the ten coordinate columns of (3.1), only column `1` is constantly
one and only column `10` is constantly zero.

On the other hand, the fourteen `D_4` root words have exactly one
constantly-one column and one constantly-zero column.  If (3.1) had the
cylinder form (2.3), the one external selected coordinate and one external
unselected coordinate would add one more constant column of each type.
Thus a semilength-five `D_4` cylinder necessarily has exactly two
constantly-one and two constantly-zero columns.  The family (3.1) has
only one of each, even after an arbitrary common coordinate permutation.

### Corollary 3.1

The slot-two one-node operad family has no common `D_4` port interface.
In particular, there is no way to obtain its fourteen lifted paths by
adjoining one fixed exterior selected coordinate to the fourteen paths of
the explicit `D_4` factor.

This obstruction occurs at the endpoint-root ledger, before any
lower-shadow or cap calculation.

For comparison, inserting the one-node spectator in slots four or five
does give two constantly-one and two constantly-zero columns; these are
the terminal positions singled out by (2.1).  Slot five is the familiar
right suffix `P -> P10`.

## 4. The aligned incidence ceiling

Suppose we insist on the literal token-preserving common-port interface.
Equation (2.1) forces

\[
                              A_1=A_2=A_3=\varnothing. \tag{4.1}
\]

Conversely these two terminal slots do give a common root cylinder.  If
`p_1...p_8` is the Dyck word of `P`, then `p_8=0` is leaf four and the
deleted final zero is leaf five.  The composed Dyck word is

\[
            p_1\cdots p_7\,w(A_4)\,0\,w(A_5).        \tag{4.2}
\]

The eight local coordinates are `p_1,...,p_7` and the displayed zero;
all coordinates in the two spectator words form one fixed exterior.

The ordered pair `(A_4,A_5)` has total size `s-4`.  The number of such
pairs is

\[
 [z^{s-4}]C(z)^2=C_{s-3}.                             \tag{4.3}
\]

Every pair produces an edge of fourteen roots.  Therefore, even if all
these edges were disjoint, their union would contain at most

\[
                         14C_{s-3}
                 =\left({7\over32}+o(1)\right)C_s.    \tag{4.4}
\]

This is bounded away from `C_s`; hence no selection of the aligned
five-input packets can cover all but `o(C_s)` roots.

If one also requires the local first insertion to remain the first
insertion of the global rooted path under the proved unary context
functor, the visibility lemma forces `A_4` to be empty as well.  The only
proved family is the right-suffix cylinder

\[
                         \{PB:P\in\mathcal D_4,
                                  B\in\mathcal D_{s-4}\},       \tag{4.5}
\]

whose total incidence is

\[
                         14C_{s-4}
                   =\left({7\over128}+o(1)\right)C_s. \tag{4.6}
\]

Allowing a future genuine multi-input composition theorem might make some
slot-four packets boundary-visible as well.  Even granting every one of
them, the ceiling (4.4) remains far below one.

## 5. The overlapping root-skeleton hypergraph

Without the common-port restriction, the number of ordered five-spectator
tuples of total size `s-4` is

\[
 E_s=[z^{s-4}]C(z)^5
     ={5\over2s-3}\binom{2s-3}{s-4}.                 \tag{5.1}
\]

These define a fourteen-uniform hypergraph on `D_s`.  Its average vertex
degree is

\[
                       {14E_s\over C_s}\longrightarrow{35\over8}. \tag{5.2}
\]

The fibres overlap: an unmarked tree can have more than one outer
four-node skeleton/decorations decomposition.  Thus (5.1) is not a
partition.  Since the degree scale is bounded, the usual high-degree
nibble does not turn it into an almost-perfect matching.

Even an independently proved near-perfect matching in this abstract
hypergraph would not overcome Sections 2--3: most of its edges have no
common physical port injection, so the existing `D_4` factor has no
certified five-input `X/Y` lift on them.

## 6. Exact conclusion

The root-skeleton proposal passes two tests:

1. all fourteen bracketings have equal total size; and
2. the ordered spectator tuple is retained in the free nonsymmetric
   binary operad.

It fails the test needed by the present factor theorem:

3. generic spectator tuples do not give one fixed local coordinate set,
   one fixed exterior set, or one common `X/Y` push-forward.

The smallest failure is the slot-two one-node family (3.1).  Restricting
to the only position-stable slots leaves at most `7/32+o(1)` of the roots,
and the proved first-insertion-visible suffix family leaves only
`7/128+o(1)`.

Therefore the explicit `D_4` factor cannot be promoted to an asymptotically
dense parent-boundary packet bank by the naive five-input operad
substitution.  The remaining escape is genuinely new: construct a
row-dependent multi-input path trade and verify its complete global
state/colour ledgers directly.
