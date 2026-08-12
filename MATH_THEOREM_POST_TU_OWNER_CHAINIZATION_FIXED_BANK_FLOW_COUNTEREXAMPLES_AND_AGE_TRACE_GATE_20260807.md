# Post-TU owner chainization: a fixed-bank flow theorem, abstract counterexamples, and the separate age-trace gate

**Date:** 2026-08-07  
**Status:** unconditional exact reductions, an exact positive theorem after
an ambient chain bank is fixed, and explicit counterexamples to generic
TU-to-chain rounding.  The sharp complete-central Boolean/Ferrers
chainization remains open.  Static chainization is kept separate from
literal age-trace chronology throughout.

## 0. Outcome

Let \(\mathcal P\) be a family of strict-lower targets and let
\(\mathcal O\subseteq\binom{[k]}R\) be the available owner bank.  The
post-TU input is a map

\[
 \phi:\mathcal P\longrightarrow\mathcal O,
 \qquad S\subset\phi(S),
 \qquad |\phi^{-1}(T)|\le d.
\tag{0.1}
\]

There are three different questions.

1. **Capacity:** does a map (0.1) exist?
2. **Static chainization:** can it be chosen so every fibre
   \(\phi^{-1}(T)\) is an inclusion chain?
3. **Chronology:** can the owner chains be ordered, aged, and refined into
   the suffix flags of one literal source trace?

The answers do not collapse.

* Capacity does not imply static chainization in general, even after an
  arbitrary global reassignment of all targets.
* Once a target-disjoint ambient chain bank is fixed, choosing the Ferrers
  boundary so that no chain retains more than \(d\) targets is again an
  ordinary integral flow problem.  Its exact min-cut system is given in
  Theorem 4.1 below.
* Static chainization does not imply chronology.  Chronology imposes a
  cross-owner sliding cocycle which already fails on two consecutive
  columns at depth two.

For the intended complete middle owner layer, the elementary
counterexamples below do not settle the question.  There the static problem
is exactly a sharp bounded-chain partition of a Boolean half, with a
co-chosen Ferrers puncture.  The capacity-TU theorem supplies no rounding
of that configuration hypergraph.

## 1. Exact static object

For \(T\in\mathcal O\), let \(\mathfrak C_d(T)\) be the family of chains

\[
 C=(S_1\subsetneq\cdots\subsetneq S_t\subset T),
 \qquad 0\le t\le d,
\tag{1.1}
\]

drawn from \(\mathcal P\).  The empty chain is allowed.  Static
chainization is exactly the problem of choosing one \(C_T\in
\mathfrak C_d(T)\) for every owner so that the nonempty \(C_T\)'s partition
\(\mathcal P\).

Equivalently, it is an exact matching in the configuration hypergraph with
edges

\[
 \{T\}\cup C,
 \qquad T\in\mathcal O,\quad C\in\mathfrak C_d(T).
\tag{1.2}
\]

Replacing a chain column in (1.2) by \(d\) independent owner slots gives
the bipartite TU relaxation (0.1).  That projection forgets every
comparability constraint in a fibre.

For a *fixed* capacity assignment \(\phi\), put

\[
 F_T=\phi^{-1}(T)
\]

and let \(h(F_T)\) be the height of the induced inclusion poset.  The
largest number of assigned edges which can be retained without changing
owners is exactly

\[
 \boxed{\sum_{T\in\mathcal O}h(F_T).}
\tag{1.3}
\]

Indeed, a retained fibre is a chain in \(F_T\), and maximum chains may be
chosen independently at different owners.  Thus owner-local sorting or
uncrossing has an exact loss formula, and that loss can be macroscopic even
when the original containment flow is perfect.

## 2. Capacity does not imply chainization in general

### Proposition 2.1 (complete owner-layer counterexample)

Take

\[
 k=4,\qquad R=3,\qquad d=2,
 \qquad\mathcal O=\binom{[4]}3.
\]

Let

\[
 \mathcal P=
 \{1,2,3,12,13,14,23,24\},
\tag{2.1}
\]

where, for example, \(12\) denotes \(\{1,2\}\).  There is a saturated
capacity-two containment assignment:

\[
\begin{array}{c|c}
123&1,12\\
124&2,24\\
134&13,14\\
234&3,23.
\end{array}
\tag{2.2}
\]

Nevertheless no capacity-two owner-chain assignment exists, even after
arbitrary reassignment.

#### Proof

There are eight targets and four owners, so every owner would have to
receive two targets.  A two-element chain of distinct strict subsets of a
three-set must use two different ranks.  Hence every owner chain would use
one singleton and one pair.  Four such chains require four singleton
targets, while (2.1) contains only three.  This contradiction is independent
of the original assignment (2.2).  \(\square\)

This example uses an owner rank above the largest Boolean rank; its rank-two
target shore has size five while the owner shore has size four.  It proves
that there is no theorem for arbitrary \((k,R)\) saying that containment
capacity alone rounds to chains.  It does not refute the intended central
case, where every lower rank has size at most the owner rank.

### Proposition 2.2 (two universal-list owners; all elementary cuts pass)

There is also a counterexample in which scalar capacity, per-rank capacity,
and the ordinary width cut all pass.

Take the two rank-five owners

\[
 T_5=\{1,2,3,4,5\},
 \qquad
 T_6=\{1,2,3,4,6\},
\]

and capacity \(d=2\).  Every target in

\[
 A_1=\{1\}\subset A_2=\{1,2\}\subset A_3=\{1,2,3\},
 \qquad B=\{4\}
\tag{2.3}
\]

is contained in both owners.  Thus all target lists are identical and an
ordinary saturated assignment exists, for example

\[
 T_5\leftarrow A_1,A_2,
 \qquad
 T_6\leftarrow A_3,B.
\tag{2.4}
\]

But no chain assignment exists.  The three \(A_i\)'s require at least two
chains under a length-two cap, while \(B\) is incomparable with every
\(A_i\) and therefore requires a third chain.  Only two owner chains are
available.

The target poset in (2.3) has size four, width two, and owner capacity
\(2\cdot2=4\).  Hence it passes both

\[
 |\mathcal P|\le d|\mathcal O|
 \quad\text{and}\quad
 \operatorname{width}(\mathcal P)\le|\mathcal O|.
\]

It is the smallest obstruction with two owners, \(d=2\), and these two
inequalities: on at most three elements a width-two poset can be split into
two chains of size at most two.  The example shows that even maximally
generous containment lists do not make scalar capacity and Dilworth width
sufficient for bounded chainization.

Its scope is a conditioned two-owner bank.  In the complete central
Boolean problem many additional owners remain available, so Proposition
2.2 is a black-box rounding obstruction, not a central-layer no-go.

## 3. Why no ordinary exchange theorem is available

For one owner, the families of targets which form chains of size at most
\(d\) constitute a hereditary set system, but not a matroid.  Already for
\(d=2\), inside any owner containing \(\{1,2,3\}\), the two feasible sets

\[
 I=\bigl\{\{1\},\{1,2\}\bigr\},
 \qquad
 J=\bigl\{\{3\}\bigr\}
\tag{3.1}
\]

satisfy \(|I|>|J|\), while neither element of \(I\setminus J\) can be
adjoined to \(J\): both are incomparable with \(\{3\}\).  Thus the matroid
augmentation axiom fails.

The usual lattice meet/join uncrossing is also unavailable.  Replacing two
incomparable named targets \(S,U\) by \(S\cap U,S\cup U\) changes the target
multiset, may move a target into the owner rank, and may duplicate a target
already used elsewhere.  The post-TU problem must preserve every named
target exactly once.

A legal elementary owner exchange can only swap or reroute existing named
targets.  For example, targets \(S\) at owner \(T\) and \(U\) at owner
\(T'\) may be swapped when

\[
 S\subset T',\qquad U\subset T.
\tag{3.2}
\]

Such four-cycle moves preserve capacity and containment, but there is no
monotone local potential forcing them to end in chains: Propositions 2.1
and 2.2 have no chainized endpoint at all.  In the central Boolean case a
successful exchange theorem must exploit the complete normalized geometry
and allow global alternating configuration paths, not merely owner-local
sorting or a matroid exchange axiom.

## 4. A positive theorem once an ambient chain bank is fixed

There is one important setting in which the post-TU gate returns to an
ordinary integral flow.

Let \(\mathscr D\) be a target-disjoint family of ambient inclusion chains.
Every \(C\in\mathscr D\) has a distinct containing owner \(T_C\), and has
at most one target \(S_{C,s}\) at each lower rank \(s\).  Write

\[
 I_C=\{s:S_{C,s}\text{ exists}\}.
\]

Assume the ambient chains cover the complete lower target bank under
consideration.  At rank \(s\), prescribe a residual count \(n_s\); the
other targets at that rank will be placed in the boundary.

### Theorem 4.1 (exact fixed-chain-bank flow)

One can choose exactly \(n_s\) rank-\(s\) targets from the ambient bank so
that every ambient chain retains at most \(d\) targets if and only if, for
every set \(J\) of lower ranks,

\[
 \boxed{
 \sum_{s\in J}n_s
 \le
 \sum_{C\in\mathscr D}
       \min\bigl(d,|J\cap I_C|\bigr).}
\tag{4.1}
\]

Whenever (4.1) holds, the selection is integral and the retained targets,
assigned to the owners \(T_C\), are already ownerwise nested.

#### Proof

Make a network with one left vertex for every rank \(s\), supply \(n_s\),
one right vertex for every ambient chain \(C\), capacity \(d\), and a
unit-capacity edge \(sC\) exactly when \(s\in I_C\).  Sending one unit on
\(sC\) means retaining the unique cell \(S_{C,s}\).

For a set \(J\) of rank vertices, a chain \(C\) can accept at most

\[
 \min(d,|J\cap I_C|)
\]

units from those ranks.  Hence (4.1) is necessary.  Conversely, in a
source--rank--chain--sink cut, minimize independently at every chain:
placing \(C\) on the source side costs \(d\), while placing it on the sink
side costs \(|J\cap I_C|\).  The minimum contribution is their minimum.
Thus (4.1) is exactly the max-flow min-cut system.  All capacities are
integral, so a maximum flow is integral.  Its used cells give the required
selection.  \(\square\)

### Corollary 4.2 (the fixed-bank excess cut)

Put \(\ell_C=|I_C|\), and suppose the ambient chains partition a lower bank
of total size \(\Lambda=\sum_C\ell_C\).  If only \(h\) targets may be sent
to the boundary, the all-ranks instance of (4.1) forces

\[
 \Lambda-h
 \le\sum_C\min(d,\ell_C),
\]

or equivalently

\[
 \boxed{
 h\ge\sum_{C\in\mathscr D}(\ell_C-d)_+.}
\tag{4.2}
\]

Thus unused capacity on short ambient chains cannot be transferred to long
ambient chains.  This is exactly why taking one fixed symmetric-chain
decomposition and merely truncating its lower pieces does not achieve the
sharp Ferrers boundary: the right side of (4.2) measures its whole
overlength tail, whereas the optimal triangular boundary has only
\(O(d^2)\) targets.  A sharp proof needs cross-chain splicing or a genuinely
new chain bank.

Theorem 4.1 is a genuine rounding theorem, but its hypothesis contains the
hard combinatorial choice: the ambient target-disjoint chain bank has
already been supplied.  The original containment TU flow constructs no
such bank.

## 5. Exact status for the complete central Boolean layer

Now take \(R\) to be a largest Boolean rank and

\[
 W=\binom{k}R,
 \qquad
 \mathcal O=\binom{[k]}R.
\]

Let \(\mathcal B\) be a chosen boundary family and
\(\mathcal P=\mathcal L\setminus\mathcal B\).  Appending the owner to each
ownerwise target chain gives the following exact equivalence:

\[
 \boxed{
 \begin{array}{c}
 \mathcal P\text{ has a depth-}d\text{ owner-chain assignment}\\[1mm]
 \Longleftrightarrow\\[1mm]
 \mathcal P\mathbin{\dot\cup}\mathcal O
 \text{ has a partition into }W\text{ inclusion chains,}\\
 \text{each containing exactly one rank-}R\text{ owner and having size}
 \le d+1.
 \end{array}}
\tag{5.1}
\]

The forward implication appends each distinct owner.  Conversely, the
rank-\(R\) layer is an antichain of size \(W\), so any \(W\)-chain
partition places exactly one owner in each chain; deleting those tops gives
the owner flags.

When the boundary is empty and \(d=\lceil|\mathcal L|/W\rceil\), (5.1) is
a sharp one-sided uniform-chain problem for a Boolean half.  When the
Ferrers boundary is nonempty, the named punctures must be co-chosen with
the bounded partition.  This is precisely the configuration problem which
the capacity flow forgets.

The complete central geometry removes the elementary defects in Section 2:
every lower rank has size at most \(W\), and normalized matching supplies
strong expansion between complete levels.  But those facts do not choose
one correlated bounded chain partition.  The approximately uniform theorem
of Sudakov--Tomon--Wagner gives an asymptotically sharp packing with an
exceptional family; it does not give the exact all-chain maximum in (5.1).
See [Uniform chain decompositions and
applications](https://arxiv.org/abs/1911.09533).
Accordingly:

\[
 \boxed{
 \text{Sections 2--3 disprove a generic rounding principle, but do not
 disprove the complete central Ferrers instance.}}
\tag{5.2}
\]

If one full central owner-chain factor is found, every subfamily obtained
by deleting additional targets inherits a factor simply by deleting those
targets from their chains.  Therefore the real exceptional-dimension issue
is to choose the small prescribed Ferrers boundary *in alignment with* one
sharp factor, not to round every possible residual family separately.

## 6. Chainization is not chronology

Let \(A_1,A_2,\ldots\) be source letters and define the suffix-union table

\[
 Q_{j,t}=A_{j-t+1}\cup\cdots\cup A_j.
\tag{6.1}
\]

Every column is nested in \(t\), but consecutive columns additionally obey
the exact sliding cocycle

\[
 \boxed{
 Q_{j,t}=Q_{j-1,t-1}\cup Q_{j,1}
 \qquad(t\ge2).}
\tag{6.2}
\]

Conversely, a triangular table satisfying (6.2) is realized by the unique
letters \(A_j=Q_{j,1}\).  Thus (6.2), not separate columnwise nestedness,
is the chronology condition.

The smallest failure already occurs at depth two.  Prescribe

\[
 Q_{1,1}=\{3\},
 \qquad
 Q_{2,1}=\{1\}\subset Q_{2,2}=\{1,2\}.
\tag{6.3}
\]

Every displayed endpoint family is nested, but (6.2) forces

\[
 Q_{2,2}=Q_{1,1}\cup Q_{2,1}=\{1,3\},
\]

contradicting (6.3).  Appending arbitrary containing owners cannot repair
this already-failed lower cell.

In the age-class formulation, a chain assigned to state \(i\) must first
be refined to a weak depth-\(d\) flag

\[
 F^i_0\subseteq\cdots\subseteq F^i_{d-1},
\]

with difference classes \(D^i_t\).  Along a Johnson transition deleting
\(\alpha_i\), literal transport further requires

\[
 \alpha_i\in D^i_{d-1},
 \qquad
 D^{i+1}_{t+1}\subseteq D^i_t
 \quad(0\le t<d-1).
\tag{6.4}
\]

These are cross-owner survivor constraints.  A static chain factor supplies
neither the age positions nor (6.4).

## 7. Strongest proved post-TU statement

The exact logical frontier is

\[
\begin{array}{c}
\text{capacity-}d\text{ containment flow}\quad\text{(TU, proved)}\\
\Downarrow\quad\text{not a valid generic rounding implication}\\
\text{depth-}d\text{ owner-chain configuration matching}\\
\Downarrow\quad\text{additional independent gate}\\
\text{weak age-flag refinement and sliding cocycle}\\
\Downarrow\\
\text{one literal physical chronology.}
\end{array}
\tag{7.1}
\]

Theorem 4.1 identifies one exact positive route: first construct a suitable
ambient chain bank, then use its ordinary integral flow to choose the
Ferrers residual cells.  Without that prechainization, the capacity
assignment cannot be uncrossed by a black-box local or matroid theorem.
For the complete central Boolean instance the right target remains a
specialized global flag-matching or chain-splicing theorem, followed by the
separate age-trace test (6.2)/(6.4).
