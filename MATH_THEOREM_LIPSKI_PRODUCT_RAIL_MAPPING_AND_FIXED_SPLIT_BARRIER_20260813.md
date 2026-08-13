# Lipski's permutation product gives legal rail covers, but a fixed split cannot fractionally factor the owner layer

**Date:** 2026-08-13  
**Primary source:** W. Lipski, Jr., *On strings containing all subsets as
substrings*, Discrete Mathematics 21 (1978), 253--259; local scan
`/Users/amir.nuriyev/Downloads/1-s2.0-0012365X78901577-main.pdf`  
**Method:** literal translation of Lipski's special permutations into cyclic
window decks and an exact split-layer count  
**Status:** unconditional mapping and obstruction.  Lipski supplies an
explicit family of genuine shortest-period pure rails covering every owner
of one fixed support.  Nevertheless, no nonnegative weighting of this
fixed-split family can give equal load to all owners.  Randomizing the split
restores symmetry but gives exactly the already-known complete orbit; it does
not solve integral named-owner rounding.

## 1. Lipski's special collections

A collection of permutations \(\Phi=\{\phi_1,\ldots,\phi_r\}\) of a
finite set \(U\) is **special** when every subset of \(U\) is an initial or
final segment of at least one \(\phi_i\).

Lipski's Lemma 1.1 constructs such a collection on an \(h\)-set with

\[
 r=
 \begin{cases}
 \displaystyle \frac12{h\choose h/2},&h\text{ even},\\[2mm]
 \displaystyle \frac12\left(1+\frac1h\right)
 {h\choose\lfloor h/2\rfloor},&h\text{ odd}.
 \end{cases}
\tag{1.1}
\]

For disjoint \(h\)-sets \(U,V\), he takes special collections
\(\Phi=\{\phi_i\}\) on \(U\) and \(\Psi=\{\psi_j\}\) on \(V\).  His
words \(A_i,B_i\) arrange the full permutations in alternating blocks so
that every ordered pair \((\phi_i,\psi_j)\) appears at one boundary and
every pair \((\phi_i,\overline\psi_j)\) appears at another, where the bar
reverses a permutation.  This is the product mechanism proving his
property \(P_{2h}\).

For the rail application put

\[
 q=h-1,\qquad N=2h=2q+2.
\tag{1.2}
\]

This is exactly the shortest legal pure-rail period.

## 2. Exact conversion to actual cyclic rail orders

Regard a concatenation \(\phi\psi\) as a cyclic order of \(U\dot\cup V\).
Let

\[
 \mathcal L(\Phi,\Psi)
 =\{\phi_i\psi_j,\ \phi_i\overline\psi_j:
        1\le i,j\le r\}.
\tag{2.1}
\]

Every member of (2.1) is a cyclic order of \(N=2q+2\) distinct toggle
labels.  After adjoining an arbitrary disjoint \(c\)-core, it is therefore
one literal legal closed pure rail.

### Theorem 2.1 (Lipski-to-rail cover)

Every \(q\)-subset of \(U\dot\cup V\) occurs as a cyclic \(q\)-window of
at least one order in \(\mathcal L(\Phi,\Psi)\).

#### Proof

Take \(Q\in{U\dot\cup V\choose q}\) and put

\[
 P=Q\cap U,\qquad S=Q\cap V.
\]

Choose \(\phi_i\) for which \(P\) is a prefix or suffix and choose
\(\psi_j\) for which \(S\) is a prefix or suffix.  If the two endpoint
orientations are opposite, \(P\cup S\) crosses one of the two cyclic
boundaries of \(\phi_i\psi_j\).  If they are the same, reversing
\(\psi_j\) makes them opposite, so the set crosses a boundary of
\(\phi_i\overline\psi_j\).  Its length is
\(|P|+|S|=q\), hence it is a cyclic \(q\)-window. \(\square\)

Thus Lipski gives an explicit cover by at most \(2r^2\) actual rails on
one support.  For even \(h\), its total owner-occurrence multiplicity is

\[
 2h\cdot2r^2
 =h{h\choose h/2}^2.
\tag{2.2}
\]

Relative to the \({2h\choose h-1}\) named owners of that fixed support,
(2.2) has average multiplicity

\[
 \frac{h{h\choose h/2}^2}{{2h\choose h-1}}
 =\left(\frac2{\sqrt\pi}+o(1)\right)\sqrt h.
\tag{2.3}
\]

So the construction is a \(\Theta(\sqrt q)\)-fold cover on average, not
an almost-partition.

## 3. The fixed-split fractional obstruction

For \(0\le a\le q\), define the split layer

\[
 \mathcal Q_a
 =\left\{Q\in{U\dot\cup V\choose q}:|Q\cap U|=a\right\},
\qquad
 |\mathcal Q_a|={h\choose a}{h\choose q-a}.
\tag{3.1}
\]

### Lemma 3.1 (every two-block order has the same split ledger)

For arbitrary permutations \(\phi\) of \(U\) and \(\psi\) of \(V\), the
cyclic \(q\)-window deck of \(\phi\psi\) contains exactly two members of
\(\mathcal Q_a\) for every \(a=0,1,\ldots,q\).

#### Proof

For \(1\le a\le q-1\), one window consists of the final \(a\) entries of
\(\phi\) followed by the first \(q-a\) entries of \(\psi\).  The other
crosses the cyclic boundary in the opposite direction, using the final
\(q-a\) entries of \(\psi\) and the first \(a\) entries of \(\phi\).

For \(a=q\), the windows wholly contained in the contiguous \(U\)-block
are its prefix and suffix of length \(q=h-1\), exactly two.  The same
argument in the \(V\)-block gives exactly two windows for \(a=0\).
These \(2(q+1)=2h=N\) windows exhaust the deck. \(\square\)

### Theorem 3.2 (no fixed-split fractional factor)

Let \(\mathcal B\) be any multiset of cyclic orders on \(U\dot\cup V\)
in which every order consists of one contiguous \(U\)-block and one
contiguous \(V\)-block.  There is no nonnegative weighting
\(w:\mathcal B\to\mathbb R_{\ge0}\) for which every \(q\)-subset has
weighted window load one.

This applies in particular to every catalogue extracted from Lipski's
\(A_i,B_i\) construction.

#### Proof

Put \(Z=\sum_{\sigma\in\mathcal B}w_\sigma\).  By Lemma 3.1, the total
weighted load in every split layer is the same number:

\[
 \sum_{Q\in\mathcal Q_a}
 \sum_{\sigma:Q\in\mathcal D_q(\sigma)}w_\sigma
 =2Z
 \qquad(0\le a\le q).
\tag{3.2}
\]

If every owner had load one, the left side would equal
\(|\mathcal Q_a|\).  But already

\[
 |\mathcal Q_0|={h\choose h-1}=h,
\tag{3.3}
\]

whereas

\[
 |\mathcal Q_1|
 ={h\choose1}{h\choose h-2}
 =\frac{h^2(h-1)}2,
\tag{3.4}
\]

and these are unequal for \(h\ge3\).  Hence no such weighting exists.
\(\square\)

The obstruction is robust.  If every owner load were in
\([1-\varepsilon,1+\varepsilon]\), (3.2) for layers zero and one would
force

\[
 \varepsilon\ge
 \frac{|\mathcal Q_1|-|\mathcal Q_0|}
      {|\mathcal Q_1|+|\mathcal Q_0|}
 =1-O(h^{-2}).
\tag{3.5}
\]

Thus a fixed Lipski split cannot even approximate the named-owner
fractional checkpoint with vanishing relative error.

## 4. Why randomizing the split gives no new orbit

Randomly relabel a fixed two-block cyclic order on an \(N\)-set.  The
resulting distribution is invariant under \(S_N\), which acts transitively
on cyclic orders.  It is therefore the uniform distribution on all cyclic
orders.  Equivalently, all cyclic orders are copies of one abstract rail
template under coordinate injections.

Consequently, if the \(U,V\) split and labels in Lipski's construction are
fully symmetrized, the resulting owner hypergraph is exactly the
parameterized period-\(N\) carousel orbit already studied.  Its named-owner
degree is regular and its maximum relative owner codegree is

\[
 \frac{2}{R(k-R)}.
\tag{4.1}
\]

The random-shell checkpoint theorem gives the same conclusion in a sparse
sample: owner loads \(1+e^{-\Omega(q)}\) and pair loads \(O(k^{-2})\).
Lipski does not improve either number after symmetrization; before
symmetrization, Theorem 3.2 prevents fractional feasibility.

## 5. Relation to the two word models

Let \(s_k\) denote Lipski's minimum length: the letters are single
coordinates, and every \(Y\subseteq[k]\) must occur as the set of exactly
\(|Y|\) consecutive letters.  A singleton-letter word is a special case of
the present set-valued-letter model.  Moreover, Lipski's requirement fixes
the witnessing interval length to \(|Y|\), whereas the present OR model does
not impose that extra restriction.  Consequently the model comparison is

\[
                     s_k\ge \nu(k).                 \tag{5.1}
\]

This direction is important: a lower bound for Lipski's more restrictive
model does **not** give a lower bound for \(\nu(k)\).

The abstract of the primary paper records

\[
 \left(\sqrt{\frac{2}{\pi k}}+o(k^{-1/2})\right)2^k
 \ \le s_k\le\
 \left(\frac2\pi+o(1)\right)2^k .                  \tag{5.2}
\]

By Stirling,

\[
 W(k)=\binom{k}{\lfloor k/2\rfloor}
      =\left(\sqrt{\frac{2}{\pi k}}+o(k^{-1/2})\right)2^k.
\tag{5.3}
\]

Thus Lipski's lower asymptotic is at the Sperner scale, but it cannot be
transported through (5.1).  His constructive upper bound is also much
weaker for the present problem than the already proved set-valued estimate

\[
 \nu(k)\le(\sqrt2+o(1))W(k)
 =\left(\frac{2}{\sqrt{\pi k}}+o(k^{-1/2})\right)2^k
 =o(2^k).                                             \tag{5.4}
\]

In particular, the \( (2/\pi+o(1))2^k\) singleton-word construction does
not improve the current set-valued bound.

## 6. Exact consequence for the named-order gate

Lipski's construction is useful in one limited sense: it is an explicit,
small compared with \((N-1)!\), catalogue which guarantees at least one
legal rail order through every eligible owner on a fixed support.  It may
serve as a candidate bank inside a future absorber.

It does not supply any of the following:

1. a fractional perfect matching of one fixed shell split;
2. an owner-disjoint selection of its rail orders;
3. an exact factor of the complete fixed-support \(q\)-layer; or
4. a new orbit after the split is randomized.

In particular its long words \(A_i,B_i\) cannot themselves be used as
rail cycles: they repeat every ground label many times, whereas a pure
rail toggle order uses each support label once.  Cutting those words into
adjacent permutation pairs gives the legal rails of Section 2 and is
subject to the split obstruction of Section 3.

Therefore the named-owner program remains

\[
 \boxed{
 \text{complete/symmetrically sampled carousel orbit}
 +\text{growing-uniformity matching}
 +\text{overlapping-core absorber}.}
\tag{6.1}
\]

The Lipski product neither solves nor refutes that global program; it
rules out the tempting fixed-bipartition shortcut exactly.
