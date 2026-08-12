# The central Pascal ladder blocks one-chain vertical contraction

Date: 2026-07-25

This note audits the proposed two-stage proof of the proportional tight-atom
matching lemma:

1. solve the (a+c=1) cover correlations by an integral nested-chain flow;
2. apply a matching or edge-colouring argument to the remaining
   (O(m^{-2})) cross-column overlap.

The second-order estimate is correct after *all* cover pairs are removed.
The issue is that a nested-chain resolution cannot remove all those pairs.
Already between the two central ranks, the cover pairs form one connected
Pascal ladder across the whole physical row.  A chain resolution chooses at
most one of the two parents of each upper interval, whereas the physical row
uses both.  The unchosen half still has normalized codegree
\(\Theta(1/m)\).

Thus the proposed two-stage argument is circular unless its first stage is
strengthened from a nested-chain flow to a whole-row (two-parent Pascal)
resolution.  That strengthened first stage is essentially the remaining
physical bundling theorem.

## 1. Exact central slot system

Keep the notation of
`PROPORTIONAL_TIGHT_ATOM_GAUSSIAN_REDUCTION_20260725.md`.  Let

\[
 \ell=m+b+H
\]

be the injective-word length.  Division of \(W\) by \(b\) gives, exactly for
all sufficiently large \(m\),

\[
 b_0=b_1=b.
\tag{1.1}
\]

Consequently the central slots of every atom are forced to be

\[
 P_i=[i,i+m-1],\qquad U_i=[i,i+m],
 \qquad 0\le i<b.
\tag{1.2}
\]

There is no freedom in the choice of \(I_0,I_1\): both equal
\(\{0,\ldots,b-1\}\).

The cover incidences inside the atom are

\[
 P_i\subset U_i\quad(0\le i<b),
 \qquad
 P_{i+1}\subset U_i\quad(0\le i<b-1).
\tag{1.3}
\]

They form the connected alternating path

\[
 P_0-U_0-P_1-U_1-\cdots-P_{b-1}-U_{b-1}.
\tag{1.4}
\]

In particular, the \(a+c=1\) graph is not a disjoint union of the
same-start chains \(P_i\subset U_i\).  The left-extension incidences
\(P_{i+1}\subset U_i\) link consecutive starts and connect the whole row.

In fact the central ladder connects the entire multiradius atom.  Recall
that

\[
 I_q=\bigcup_{d\ge \rho(q)}J_d,
 \qquad \rho(q)=\max\{-q,q-1\}.
\tag{1.5}
\]

If \(q<0\) and \(i\in I_q\), then \(i\in I_{q+1}\), and the slot at
\((i,q)\) is covered by the same-start slot at \((i,q+1)\).  Iterating
joins it to \(P_i\).  If \(q>1\) and \(i\in I_q\), then
\(i\in I_{q-1}\), and the same-start slot at \((i,q-1)\) is covered by
the slot at \((i,q)\).  Iterating joins it to \(U_i\).  Hence:

\[
 \boxed{\text{The full slot graph formed by all }a+c=1\text{ pairs in one
 atom is connected.}}
\tag{1.6}
\]

Thus literal equivalence contraction of *all* first-order pairs contracts
the whole \(\kappa\)-vertex atom, not \(b\) independent vertical columns.

## 2. Exact central cover codegree

Let \(A\in\binom{[n]}m\) and
\(B\in\binom{[n]}{m+1}\) with \(A\subset B\).  Let \(E\) denote the number
of labelled injective words, and let degrees and codegrees be in the
labelled proportional-atom multihypergraph.

### Proposition 2.1

For every such cover pair,

\[
 \boxed{
 \frac{\deg(A,B)}{\deg(A)}
 =\frac{\deg(A,B)}{\deg(B)}
 =\frac{2b-1}{b(m+1)}.}
\tag{2.1}
\]

In particular the normalized cover codegree is
\((2+o(1))/m\).

### Proof

There are exactly \(2b-1\) compatible ordered slot pairs:

\[
 (P_i,U_i)\quad(0\le i<b),
 \qquad
 (P_{i+1},U_i)\quad(0\le i<b-1).
\tag{2.2}
\]

For a fixed compatible pair, the number of words realizing \(A,B\) is

\[
 m!\,(m)_{\ell-m-1}.
\tag{2.3}
\]

Indeed, order the elements of \(A\) in its \(m\) positions, put the unique
element of \(B\setminus A\) in the added endpoint, and fill the remaining
positions injectively from the other \(m\) coordinates.  Distinct slot-pair
events are disjoint.

On the other hand,

\[
 \deg(A)=b\,m!\,(m+1)_{\ell-m},
\tag{2.4}
\]

and

\[
 \deg(B)=b\,(m+1)!\,(m)_{\ell-m-1}.
\tag{2.5}
\]

Since

\[
 (m+1)_{\ell-m}=(m+1)(m)_{\ell-m-1},
\]

substitution of (2.3)--(2.5) proves (2.1).  \(\square\)

This is the intrinsic target-pair codegree.  It already includes both
possible endpoint representations, so choosing one preferred slot
orientation does not divide (2.1) by two.

## 3. A nested resolution leaves first-order overlap

An integral nested-chain resolution induces, at the central transition,
a matching \(M\) in the bipartite inclusion graph between the rank-\(m\)
and rank-\((m+1)\) targets: every selected lower target has at most one
selected successor, and every selected upper target has at most one selected
predecessor.

### Theorem 3.1 (one-flow residual)

For every matching \(M\) in the central inclusion graph and every
proportional atom \(e\), at least \(b-1\) of the \(2b-1\) ladder incidences
in (1.3) do not belong to \(M\).  Moreover

\[
 \frac1b\sum_{A\in e\cap\binom{[n]}m}
 \ \sum_{\substack{B\in e\cap\binom{[n]}{m+1}\\
                    A\subset B,\ (A,B)\notin M}}
 \frac{\deg(A,B)}{\deg(A)}
 \ge
 \left(1-\frac1b\right)\frac{2b-1}{b(m+1)}.
\tag{3.1}
\]

In particular the residual normalized row sum is

\[
 \boxed{\Omega(1/m),}
\tag{3.2}
\]

not \(O(m^{-2})\).

### Proof

The ladder (1.4) has \(b\) vertices on each side.  A matching contains at
most \(b\) of its \(2b-1\) edges, so at least \(b-1\) remain.  Each remaining
edge contributes the common value (2.1) exactly once to the double sum in
(3.1).  Divide by \(b\).  \(\square\)

The same conclusion holds if the abstract proportional Boolean packing of
Theorem 4.1 in
`MATH_ATTACK_A_PROPORTIONAL_ATOM_HALL_AUDIT_20260725.md` is used for the
first stage.  Its central transition is precisely such a (partial) matching,
so it contracts at most one parent per upper target.

There is an even more direct slot version.  Contracting the same-start
links \(P_i\subset U_i\) leaves all \(b-1\) links
\(P_{i+1}\subset U_i\).  Contracting the left-extension links instead
leaves the same-start links.  No orientation of the one-dimensional chain
flags removes both sides of the Pascal diamonds.

## 4. Why a uniform \(O(m^{-2})\) remainder requires the whole ladder

Suppose cover incidences are declared `contracted', and all undeclared
target pairs remain in the residual codegree calculation.  By Proposition
2.1, even one undeclared cover pair \(A\subset B\) has normalized codegree

\[
 \frac{2b-1}{b(m+1)}=\Theta(1/m).
\tag{4.1}
\]

Every cover pair occurs in some labelled atom: place \(A\) in a central
slot, place \(B\setminus A\) at either adjacent endpoint, and fill the
remaining word positions injectively.  Therefore a *uniform* residual
maximum-row-sum estimate of order \(O(m^{-2})\) can be obtained by literal
pair deletion only if every central cover incidence is handled.

But the central inclusion graph is \((m+1)\)-regular on both sides.  A
single nested resolution handles one matching layer, only a
\(1/(m+1)\) fraction of all its edges.  Even a decomposition into perfect
matching layers would require all \(m+1\) layers to remove every cover
pair.  Those layers are not disjoint chain owners: each Boolean target
participates in all of them.

At the slot level the same fact appears as connectivity.  Contracting all
edges of (1.4) identifies all \(2b\) central slots of one atom into one
component, and (1.6) then attaches every other designated slot.  Thus the
only literal equivalence contraction which removes all first-order links
contracts the entire atom.  It supplies no smaller-rank residual
hypergraph to which an ordinary edge-colouring theorem could be applied.

## 5. Correct remaining positive theorem

The valid second-order estimate is

\[
 \sum_{Q:\ |P\setminus Q|+|Q\setminus P|\ge2}
 \frac1{\binom{|P|}{|P\setminus Q|}
          \binom{n-|P|}{|Q\setminus P|}}
 =O(m^{-2}).
\tag{5.1}
\]

What fails is the proposed mechanism for reaching its hypothesis.  The
first-order pairs must be solved as a two-parent Pascal object, not as
independent nested chains.

A sufficient replacement would be a theorem of the following form.

> **Whole-row Pascal resolution theorem.**  Round the uniform fractional
> proportional-atom packing to physical tight rows while resolving the
> complete alternating cover ladders at every adjacent pair of ranks; after
> this simultaneous ladder resolution, use the genuinely non-cover overlap
> (5.1) to leave \(o(p/\sqrt m)\) rows unmatched.

The central two-rank instance of the ladder resolution is supplied by an
exact wreath factor: its rank-\(m\) and rank-\((m+1)\) cyclic intervals form
disjoint alternating cycles.  Extending that resolution through the
Gaussian band is exactly the cyclic/Pascal synchronization problem.  It is
not supplied by the integral nested-flow theorem.

Hence the precise audited boundary is

\[
 \boxed{
 \begin{array}{c}
 \text{the non-cover overlap is already }O(m^{-2}),\\[1mm]
 \text{but one-chain vertical flow leaves }\Theta(m^{-1})
 \text{ cover overlap};\\[1mm]
 \text{removing it while preserving atoms is the whole-row bundling gate.}
 \end{array}}
\tag{5.2}
\]

No contradiction to the proportional matching lemma is proved.  The note
rules out only the proposed shortcut from nested-flow integrality to a
second-order edge-colouring theorem.
