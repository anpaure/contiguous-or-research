# Touch number, binary residue, and the exact face-glue gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction and obstruction.  The
note proves an exact binary-weight lower bound on the number of compensation
cells which must meet a residue-carrying source cell, specializes it sharply
to the two-touch case, and characterizes connectedness of two traces by a
bipartite face-adjacency graph.  It does **not** prove that the central
binomial residue always has large weight, construct a valid two-touch
selector when the residue has weight at most two, or close residence, global
dicut realization, macro Hall, palette, or compiler gates.

## 1. Setup and the trace theorem

Put

\[
 V=\binom{[2r]}r,\qquad W_r=|V|=\binom{2r}r,
 \qquad q_M=2^M,                                             \tag{1.1}
\]

and assume

\[
                         M>\nu_2(W_r).                        \tag{1.2}
\]

Let `C` be a cell of a perfect pairing `R`, of dimension `m>=M`.  Thus
`C` is an induced `m`-cube and `|C|=2^m` is zero modulo `q_M`.

Let `U subsetneq C` be nonempty.  Suppose `U` has an exact extension by
whole cells selected from two further perfect-pairing partitions `P,Q`:
the selected cells are pairwise disjoint, disjoint from `U`, and cover
`V-U`.

Call a selected cell **touching** when it has nonempty intersection with
`C`, and let `t` be the number of touching selected cells.  Since selected
cells are disjoint, their traces partition the unselected part of `C`:

\[
       C\setminus U=(K_1\cap C)\mathbin{\dot\cup}\cdots
                       \mathbin{\dot\cup}(K_t\cap C).         \tag{1.3}
\]

The pair-cell trace-decomposition theorem says that, for each `i`, there
are nonnegative integers `a_i,b_i` such that

\[
 K_i\cap C\text{ is a union of }2^{b_i}
 \text{ pairwise edge-isolated }a_i\text{-faces},             \tag{1.4}
\]

and consequently

\[
                         |K_i\cap C|=2^{e_i},
                         \qquad e_i=a_i+b_i.                  \tag{1.5}
\]

The statement applies equally to selected `P`- and selected `Q`-cells.

## 2. The exact touch-number lower bound

For an integer `z` in `[0,2^M)`, write `wt_2(z)` for the number of ones in
its `M`-bit binary expansion.  Define the **negative central residue**

\[
             \eta_M(r)=(-W_r)\bmod 2^M,
             \qquad 1\le\eta_M(r)<2^M.                       \tag{2.1}
\]

It is nonzero by (1.2).

### Lemma 2.1 (adding powers cannot create more ones than summands)

For arbitrary nonnegative integers `e_1,...,e_t`,

\[
 \operatorname{wt}_2\left(
    \left(\sum_{i=1}^t2^{e_i}\right)\bmod2^M
                          \right)\le t.                       \tag{2.2}
\]

#### Proof

Discard terms with `e_i>=M`, which are zero modulo `2^M`.  Starting from
zero, add the remaining powers one at a time in `M`-bit arithmetic.  Adding
`2^e` either changes one zero bit to one, increasing the weight by one, or
changes a nonempty run of ones beginning at bit `e` to zeros and changes the
next zero to one, increasing the weight by at most one.  Overflow only
deletes a final carry.  After at most `t` additions the weight is at most
`t`. \(\square\)

### Theorem 2.2 (binary touch bound)

If

\[
                         |U|\equiv W_r\pmod {2^M},            \tag{2.3}
\]

then every exact extension satisfies

\[
                  \boxed{t\ge\operatorname{wt}_2(\eta_M(r)).} \tag{2.4}
\]

#### Proof

Equations (1.3), (1.5), and `m>=M` give

\[
 \eta_M(r)
   \equiv-|U|
   \equiv |C|-|U|
   =\sum_{i=1}^t2^{e_i}pmod {2^M}.                           \tag{2.5}
\]

Apply Lemma 2.1. \(\square\)

The theorem is incidence-aware in exactly the needed sense.  The full
selected cells may be much larger than their traces and may cross the
boundary of `C`; only the literal, disjoint traces in (1.3) are counted.
No assumption that a selected cell is contained in `C` is made.

### Corollary 2.3 (sharp two-touch residue gate)

A two-touch extension is possible only if

\[
                    \operatorname{wt}_2(\eta_M(r))\le2.       \tag{2.6}
\]

Writing `s=nu_2(W_r)` and `L=M-s`, condition (2.6) is equivalent to

\[
 {\eta_M(r)\over2^s}=1
 \quad\text{or}\quad
 {\eta_M(r)\over2^s}=1+2^d
 \quad(1\le d<L).                                            \tag{2.7}
\]

Equivalently, for the odd part `u=W_r/2^s`,

\[
 u\equiv-1
 \quad\text{or}\quad
 u\equiv-1-2^d\pmod {2^L}.                                  \tag{2.8}
\]

#### Proof

The residue `eta_M(r)` has exact valuation `s`, so its lowest nonzero bit is
bit `s`.  An integer of weight at most two with that valuation has exactly
the forms in (2.7).  Multiplication by `2^s` and negation modulo `2^M`
gives (2.8). \(\square\)

Thus the two-touch problem is automatically impossible unless the negative
central residue is a one-bit or two-bit integer.  This condition is only
necessary: it says nothing about disjoint full cells, connected traces,
residence, or the one-way dicut labels.

### Proposition 2.4 (exact odd-unit sparsity)

For fixed `L`, among the `2^(L-1)` odd residue classes modulo `2^L`, exactly

\[
                    \sum_{j=1}^t\binom{L-1}{j-1}              \tag{2.9}
\]

classes have negative residue of binary weight at most `t`.  In particular,
only `L` odd classes pass the two-touch gate.

Also, for every odd integer `u`,

\[
 \operatorname{wt}_2((-u)\bmod2^L)
  =L-\operatorname{wt}_2((u-1)\bmod2^L).                     \tag{2.10}
\]

#### Proof

Negation permutes the odd residue classes.  An odd `L`-bit integer of weight
`j` has its least significant bit fixed to one and its other `j-1` ones in
arbitrary positions, giving `binom(L-1,j-1)` choices.  Summing proves (2.9).

If `a=u mod2^L`, then `a` is odd and

\[
                   2^L-a=(2^L-1)-(a-1).                      \tag{2.11}
\]

The right side is the bitwise complement, in `L` bits, of `a-1`.  This is
(2.10). \(\square\)

This sparsity statement is not a distributional claim about central
binomial coefficients.  It only quantifies how exceptional the admissible
residue classes are inside the ambient odd-unit group.

## 3. The exact two-trace connectivity gate

Now specialize to `t=2`.  Put

\[
                   T_i=K_i\cap C\qquad(i=1,2),                \tag{3.1}
\]

and write the trace decomposition (1.4) as

\[
                   T_i=\mathop{\dot\bigcup}_{F\in\mathcal F_i}F.
                                                                    \tag{3.2}
\]

Each `F` is an induced cube face.  There is no cube edge between distinct
members of the same family `mathcal F_i`.

Define the **face-glue graph** `H(K_1,K_2;C)` to be the bipartite graph with
shores `mathcal F_1,mathcal F_2`, joining `F_1` to `F_2` when at least one
cube edge of `C` has one endpoint in each face.

### Theorem 3.1 (exact connectedness criterion)

The complementary trace

\[
                          C\setminus U=T_1\mathbin{\dot\cup}T_2 \tag{3.3}
\]

is connected in the cube graph of `C` if and only if the face-glue graph
`H(K_1,K_2;C)` is connected.

In the two-touch setting both trace families are nonempty, so `H` has at
least two vertices.  Connectedness therefore already excludes every
isolated face vertex; no separate boundary convention is needed.

#### Proof

Every face in (3.2) is connected.  Contract each such face in the induced
cube graph on `T_1 union T_2`.  There are no edges between distinct faces
of one family, by the trace theorem.  The contracted graph is therefore
exactly `H`.  Contracting connected vertex sets preserves connectedness.
This proves the equivalence. \(\square\)

### Corollary 3.2 (a mandatory cross-edge budget)

If the two-touch complementary trace is connected and

\[
                   |\mathcal F_i|=2^{b_i},                    \tag{3.4}
\]

then there are at least

\[
                         2^{b_1}+2^{b_2}-1                    \tag{3.5}
\]

distinct cross-face adjacencies between the two trace families.

#### Proof

A connected graph on `2^(b_1)+2^(b_2)` vertices has at least one fewer
edges than vertices. \(\square\)

This is the exact geometric content missing from the scalar two-bit
condition.  A cell whose trace splits into many nonshared-overlay faces
requires a correspondingly large alternating bank of cube adjacencies to
the other trace.

## 4. A sufficient face-chain criterion for an interval

Connectedness is necessary but not sufficient for `C-U` to occur as one
cyclic interval of a Hamilton cycle of `C`.  The following literal condition
is a useful sufficient replacement.

### Proposition 4.1 (face-chain concatenation)

Suppose all faces in `mathcal F_1 union mathcal F_2` can be ordered

\[
                         F_1,F_2,\ldots,F_h                  \tag{4.1}
\]

so that consecutive faces belong to opposite trace families.  Suppose for
each `j<h` there is a cube edge `y_j x_(j+1)` from `F_j` to `F_(j+1)`, and
each face `F_j` has a Hamilton path from `x_j` to `y_j` (with the unused
endpoint at `j=1` or `j=h` chosen arbitrarily).  Require all listed port
vertices to have their declared incidences and require the two ports in an
internal face to be distinct whenever that face has more than one vertex.

Then `T_1 union T_2` has a Hamilton path, obtained by concatenating the face
paths and the cross-face edges.  Hence, if its complementary owner set `U`
also has a Hamilton path whose endpoints are joined to the two endpoints of
this path by two distinct cube edges, `C` has a Hamilton cycle in which `U`
and `C-U` are the two cyclic intervals.

If in addition every constituent face path and the path on `U` has at least
`D` vertices, all those paths are internally `D`-resident, and every
displayed seam passes the literal length-`D` collar test, the resulting
Hamilton cycle is `D`-resident.  Without the constituent length bound, a
short transition interval can cross more than one seam; in that case a
global multi-seam collar check is required instead.

#### Proof

The faces are disjoint and the paths exhaust them one at a time.  Each
displayed cross edge joins the terminal vertex of one path to the initial
vertex of the next.  Their concatenation is therefore one simple Hamilton
path of `T_1 union T_2`.  Adding the complementary Hamilton path and the two
boundary edges gives one Hamilton cycle of `C`.  Under the last hypotheses,
consecutive seams are separated by at least `D` transition positions.
Hence every transition interval of length less than `D` is either internal
to one piece or meets exactly one certified seam, so the full transition
word is `D`-resident. \(\square\)

The collar hypothesis is deliberately literal; ordinary connectedness of
the face-glue graph does not imply residence.

## 5. The sharpened two-touch target

The resident nested-difference problem with exactly two compensation cells
can survive only if all four rows below hold simultaneously.

1. **Two-bit arithmetic:** `wt_2(eta_M(r))<=2`.
2. **Global dicut:** the full `P,Q` block labels satisfy the zero--zero and
   one--one-free incidence equations, not merely their restriction to `C`.
3. **Face glue:** `H(K_1,K_2;C)` is connected; a face-chain certificate such
   as Proposition 4.1 suffices for interval chronology.
4. **Residence:** all internal paths and all seams pass the same physical
   length-`D` collar test.

If the first row fails, no choice of pairings or outside compensation can
repair the two-touch architecture.  If it passes, the other three rows
remain genuine correlated conditions; this note makes no existence claim.

More generally, Theorem 2.2 identifies the correct touch complexity of the
residue:

\[
 \boxed{\text{any exact pair-cell construction needs at least
        }\operatorname{wt}_2((-W_r)\bmod2^M)\text{ cells touching }C.}
                                                                    \tag{5.1}
\]
