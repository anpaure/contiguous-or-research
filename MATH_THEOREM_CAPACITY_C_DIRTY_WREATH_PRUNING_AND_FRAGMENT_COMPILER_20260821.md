# Capacity-`c` dirty wreath pruning and the fragmented-ribbon compiler

**Date:** 2026-08-21  
**Method:** pure mathematics; the finite checker is an audit only  
**Status:** exact capacity-Hall theorem, exact pruning bound, and exact
within-row ribbon pairing; the hypothesis `Q=O(Cat_r)` and every nested-depth
extension remain separate gates

## 0. Outcome

Put

\[
 b=2r+1,\qquad
 \mathcal M=\binom{[b]}r,\qquad
 \mathcal L=\binom{[b]}{r-1},\qquad
 N=|\mathcal M|,
 \tag{0.1}
\]

and let \(\mathscr F\) be an exact middle-wreath factor.  Thus every row
\(C\in\mathscr F\) is a cyclic order on \([b]\), its \(b\) rank-\(r\)
windows form a wreath, and these middle-window families partition
\(\mathcal M\).  Write

\[
 m=|\mathscr F|=N/b=\operatorname{Cat}_r
 \tag{0.2}
\]

and let \(\mathsf L(C)\) be the set of the \(b\) cyclic
rank-\((r-1)\) windows of \(C\).

For \(\mathscr S\subseteq\mathscr F\), define

\[
 \mu_{\mathscr S}(T)
   =|\{C\in\mathscr S:T\in\mathsf L(C)\}|,
 \qquad
 Q(\mathscr S)
   =\sum_T(\mu_{\mathscr S}(T)-1)_+.
 \tag{0.3}
\]

Because every row has \(b\) distinct lower windows,

\[
 Q(\mathscr S)
   =b|\mathscr S|-
      \left|\bigcup_{C\in\mathscr S}\mathsf L(C)\right|.
 \tag{0.4}
\]

The main theorem is the following.

> **Capacity-`c` pruning theorem.**  Let \(1\le c<b\) and put
> \(Q=Q(\mathscr F)\).  One can delete fewer than \(Q/c\) factor rows
> and, in every remaining row, mark exactly \(c\) starts dirty so that all
> same-start rank-\((r-1)\)/rank-\(r\) flags at the clean starts are
> mutually target-disjoint.  The number of clean flags is at least
> \[
>             N-cm-bQ/c.                                      \tag{0.5}
> \]
> Moreover, after discarding at most another \(c\) clean flags per retained
> row, the surviving flags split into genuine ribbon pairs whose middle
> endpoints are disjoint.  The number of ribbon-paired flags is at least
> \[
>             N-2cm-bQ/c.                                     \tag{0.6}
> \]

Consequently, if

\[
                         Q(\mathscr F)\le K m                 \tag{0.7}
\]

for an absolute constant \(K\), then taking, for example,
\(c=\lceil\sqrt b\rceil\) gives

\[
 {\#\{\text{unpaired or deleted flags}\}\over N}
 \le {2c\over b}+{K\over c}=O_K(b^{-1/2})=o(1).              \tag{0.8}
\]

This removes the exact one-puncture pseudoforest requirement at a vanishing
cost.  The sufficient input (0.7) is precisely a first-shadow statement at
the natural Catalan scale.  If \(h_1\) is the number of missing lower
targets in the full factor, then

\[
 Q(\mathscr F)
   =N-|\mathcal L|+h_1
   ={2N\over r+2}+h_1.                                       \tag{0.9}
\]

Since \(2N/(r+2)<4m\), the bound \(h_1=O(m)\) implies (0.7).
In particular, the C8 energy target
\(\Phi-(N-|\mathcal L|)=O(N/r)\) is strong enough, because the exact
energy identity implies \(h_1=O(N/r)=O(m)\).

The theorem is only a rank-\((r-1)\)/rank-\(r\), or `q=1`, compiler.
It does not assert simultaneous collision-freeness of deeper nested flags.

## 1. The exact capacity-`c` Hall criterion

Fix \(\mathscr S\subseteq\mathscr F\).  A **capacity-\(c\) dirty-start
choice** chooses \(c\) of the \(b\) starts in every row and retains the
other \(b-c\) same-start flags.

### Theorem 1.1 (capacity-`c` clean-deck Hall theorem)

The following are equivalent.

1. There is a capacity-\(c\) dirty-start choice on \(\mathscr S\) for
   which all retained lower targets are distinct.
2. For every row subfamily \(\mathscr A\subseteq\mathscr S\),

   \[
      (b-c)|\mathscr A|
      \le
      \left|\bigcup_{C\in\mathscr A}\mathsf L(C)\right|.
   \tag{1.1}
   \]

3. For every \(\mathscr A\subseteq\mathscr S\),

   \[
                         Q(\mathscr A)\le c|\mathscr A|.
   \tag{1.2}
   \]

#### Proof

Make \(b-c\) demand clones of every row \(C\), all adjacent to the
\(b\) targets in \(\mathsf L(C)\), and give each lower target capacity
one.  A matching saturating all row clones chooses \(b-c\) different
lower targets from each row and never chooses the same target in two rows.
Its complement in each row is exactly a set of \(c\) dirty starts.
Capacitated Hall is (1.1), proving the equivalence of 1 and 2.

Using (0.4), inequality (1.1) is equivalent to

\[
 b|\mathscr A|-Q(\mathscr A)\ge(b-c)|\mathscr A|,
\]

which is (1.2).  \(\square\)

For \(c=1\), Theorem 1.1 is the row-subfamily form of the exact
pseudoforest compiler.  For growing \(c\), no pseudoforest hypothesis is
needed; all Hall-dense parts can instead be pruned cheaply.

There is an important edge-capacity distinction.  One must **not** replace
(1.1)--(1.2) by the superficially similar target-side inequalities

\[
 \sum_{T\in\mathcal U}(\mu(T)-1)
       \le c|N(\mathcal U)|.                                \tag{1.3}
\]

Cloning a target demand \(\mu(T)-1\) times and giving a row capacity \(c\)
would allow two clones of the same target to use the same row--target
occurrence, although that occurrence can be dirtied only once.  The true
network has unit capacity on every occurrence edge.  The row-clone
formulation in the proof of Theorem 1.1 builds this unit occurrence
capacity in automatically, and its exact Hall cuts are the row-subfamily
cuts (1.1).

## 2. Pruning all Hall violations

The elementary monotonicity below is the key point.

### Lemma 2.1 (deleting rows pays their internal duplicate demand)

For \(\mathscr A\subseteq\mathscr S\),

\[
 Q(\mathscr S)-Q(\mathscr S\setminus\mathscr A)
                         \ge Q(\mathscr A).                  \tag{2.1}
\]

#### Proof

Fix a lower target \(T\), and let \(x\) and \(y\) be its numbers of
occurrences in \(\mathscr A\) and
\(\mathscr S\setminus\mathscr A\), respectively.  Its contribution to
the left side of (2.1) is

\[
 (x+y-1)_+-(y-1)_+
 =\begin{cases}
   x,&y\ge1,\\
   (x-1)_+,&y=0,
  \end{cases}
\]

which is at least \((x-1)_+\), its contribution to
\(Q(\mathscr A)\).  Sum over \(T\).  \(\square\)

### Theorem 2.2 (exact violation-pruning bound)

Let \(Q=Q(\mathscr F)\).  There is a row set
\(\mathscr S\subseteq\mathscr F\) such that

\[
       |\mathscr F\setminus\mathscr S|<Q/c                  \tag{2.2}
\]

and \(\mathscr S\) satisfies all capacity-\(c\) Hall inequalities
(1.1).

#### Proof

Start with \(\mathscr S_0=\mathscr F\).  If (1.2) fails, choose any
violating subfamily \(\mathscr A_i\subseteq\mathscr S_i\) and put
\(\mathscr S_{i+1}=\mathscr S_i\setminus\mathscr A_i\).  Lemma 2.1 gives

\[
 Q(\mathscr S_i)-Q(\mathscr S_{i+1})
 \ge Q(\mathscr A_i)>c|\mathscr A_i|.                        \tag{2.3}
\]

The deleted row sets are disjoint.  Summing (2.3) through termination and
using \(Q(\mathscr S_i)\ge0\) gives

\[
 c|\mathscr F\setminus\mathscr S|<Q(\mathscr F),
\]

which is (2.2).  At termination there is no violating subfamily, so
Theorem 1.1 constructs the clean flags.  \(\square\)

### Corollary 2.3 (clean-flag loss)

The construction in Theorem 2.2 retains at least

\[
 (b-c)|\mathscr S|
 \ge N-cm-bQ/c                                                \tag{2.4}
\]

mutually target-disjoint same-start inclusion flags.

#### Proof

The omitted flags consist of \(c\) per retained row and all \(b\) flags
in a deleted row.  Bound these by \(cm+bQ/c\) using (2.2).  The middle
targets are distinct because \(\mathscr F\) is an exact middle factor; the
lower targets are distinct by Theorem 1.1.  \(\square\)

There is also a simpler, slightly weaker construction which does not search
for Hall cuts.  It is useful as an independent robustness fallback.

### Proposition 2.4 (heavy-row fallback)

Let

\[
 \mathcal D=\{T:\mu_{\mathscr F}(T)\ge2\},\qquad
 E=\sum_{T\in\mathcal D}\mu_{\mathscr F}(T).
 \tag{2.5}
\]

Then \(|\mathcal D|\le Q\) and

\[
                         E=Q+|\mathcal D|\le2Q.              \tag{2.6}
\]

Delete every row containing more than \(c\) members of \(\mathcal D\).
Fewer than \(2Q/c\) rows are deleted.  In every remaining row, dirty every
start whose lower target belongs to \(\mathcal D\).  At most \(c\) starts
per row are dirtied, and every retained lower target is globally unique.

#### Proof

Every target in \(\mathcal D\) contributes \(\mu(T)-1\) to \(Q\), so
\(|\mathcal D|\le Q\), and summing
\(\mu(T)=(\mu(T)-1)+1\) proves (2.6).  The sum, over rows, of the numbers
of incident targets in \(\mathcal D\) is \(E\).  Hence fewer than
\(E/c\le2Q/c\) rows are heavy.  After they are deleted, dirtying all
remaining occurrences of targets in \(\mathcal D\) uses at most \(c\)
starts in a row.  Every clean target was outside the original repeated set
and therefore has multiplicity at most one.  \(\square\)

This fallback loses at most \(2bQ/c\) flags in deleted rows and at most
\(2Q\) explicitly repeated starts before any optional padding of the dirty
sets.  It already gives an \(o(N)\) clean-flag loss when \(Q=O(m)\),
\(c\to\infty\), and \(c=o(b)\).  Theorem 2.2 is sharper: it retains exactly
\(b-c\) flags per surviving row and has deleted-row term \(bQ/c\).

## 3. Pairing the clean starts into genuine ribbons

The clean flags in Corollary 2.3 are already a matching in the middle
inclusion graph.  The next step records exactly what additional physical
structure survives inside each cyclic order.

### Lemma 3.1 (the within-row odd graph is one cycle)

Let \(M_i\), \(i\in\mathbb Z_b\), be the rank-\(r\) cyclic windows of
one row.  Then \(M_i\cap M_j=\varnothing\) exactly when

\[
                         j-i\equiv r\text{ or }r+1\pmod b.
 \tag{3.1}
\]

Consequently the graph on the \(b\) starts joining disjoint middle
windows is a single \(C_b\).

#### Proof

Two length-\(r\) proper cyclic intervals in a cycle of length \(2r+1\)
are disjoint exactly at the two offsets in (3.1).  These are the two
directions of the same edge because \(r+1\equiv-r\pmod b\).  Since
\(\gcd(r,2r+1)=1\), repeatedly adding \(r\) visits all starts.  \(\square\)

### Lemma 3.2 (multi-punctured row pairing)

After deleting any nonempty set of \(c\) starts from the cycle in
Lemma 3.1, the remaining graph has at most \(c\) path components and has a
matching leaving at most \(c\) vertices unmatched.

#### Proof

Deleting \(c\) vertices from a cycle leaves at most \(c\) nonempty path
components.  A maximum matching of a path leaves at most one vertex
unmatched.  \(\square\)

### Theorem 3.3 (fragmented-ribbon compiler)

The clean flags produced by Corollary 2.3 can be reduced by at most
\(c|\mathscr S|\le cm\) flags and partitioned into ribbon pairs

\[
 \{(M_i,L_i),(M_j,L_j)\},\qquad M_i\cap M_j=\varnothing.
 \tag{3.2}
\]

All middle and lower targets of all these ribbons are mutually distinct,
and the number of paired flags is at least

\[
                         N-2cm-bQ/c.                         \tag{3.3}
\]

#### Proof

Apply Lemma 3.2 independently in every retained row to the clean starts.
Discard the at most \(c\) unmatched starts.  Every matched edge gives
(3.2), which is a genuine ribbon because each \(L_i\subset M_i\) is the
same-start lower facet and the two middle endpoints are disjoint.  Removing
flags cannot spoil the target-disjointness from Corollary 2.3.  Combining
its loss bound with at most \(cm\) further discards proves (3.3).
\(\square\)

The exact physical object supplied by Theorem 3.3 is a target-disjoint
collection of ribbon pairs, partitioned row-by-row into matchings of the
odd-cycle paths left by the dirty starts.  Each ribbon remembers its common
cyclic order, so the result is stronger than an abstract ribbon matching.
It is weaker than a disjoint union of complete one-punctured wreath decks:
one row may contribute several path fragments.  Any later product-atom
compiler must either accept these fragments directly or pay for their
component resets.  The present theorem does not silently assert that
additional lift.

## 4. The Catalan-scale sufficient condition

Let

\[
 h_1=|\{T\in\mathcal L:\mu_{\mathscr F}(T)=0\}|.
\]

The full factor has exactly \(N=bm\) lower-window occurrences, while its
support has size \(|\mathcal L|-h_1\).  Therefore

\[
 Q(\mathscr F)=N-|\mathcal L|+h_1
 ={2N\over r+2}+h_1.                                        \tag{4.1}
\]

Also

\[
 {2N/(r+2)\over m}={2b\over r+2}<4.                          \tag{4.2}
\]

Hence \(h_1=O(m)\) is equivalent, up to an absolute additive
\(<4m\), to \(Q(\mathscr F)=O(m)\).

For the convex first-shadow energy

\[
 \Phi(\mathscr F)=\sum_T\binom{\mu_{\mathscr F}(T)}2,
\]

the exact identity

\[
 \Phi-(N-|\mathcal L|)
 =h_1+\sum_{\mu(T)\ge3}\binom{\mu(T)-1}2                    \tag{4.3}
\]

shows that the proposed C8 local-minimum conclusion

\[
                   \Phi-(N-|\mathcal L|)=O(N/r)             \tag{4.4}
\]

implies \(h_1=O(N/r)=O(m)\), then (0.7), and finally the
\(1-O(r^{-1/2})\) fragmented-ribbon family of Theorem 3.3.

Thus the remaining positive gate on this route is no longer exact
one-puncture co-design.  It is the Catalan-scale energy or hole bound
(4.4), followed by a separately verified physical compiler for the
resulting \(O(\sqrt r)\) row fragments.

## 5. Scope

The proved content is:

1. the exact capacity-\(c\) Hall criterion (1.1)--(1.2);
2. deletion of all Hall violations using fewer than \(Q/c\) rows;
3. the exact clean-flag loss \(cm+bQ/c\);
4. the exact extra ribbon-pairing loss at most \(cm\);
5. the normalized loss bound \(2c/b+Q/(cm)\); and
6. the implication from a Catalan-scale first-shadow hole or energy bound
   to a coefficient-one `q=1` fragmented-ribbon family.

The note does **not** prove (4.4) for the canonical factor or its C8 switch
component.  It does not prove simultaneous capacity-Hall selection for
nested depths \(q\ge2\).  It does not turn the row fragments into the final
ordered physical product atoms or a universal word.  Those quantifiers are
separate.

## 6. Checker

The finite audit is

```text
scratch/audit_capacity_c_dirty_wreath_pruning_and_fragment_compiler_20260821.py
```

It checks the capacity-Hall equivalence, the pruning charge, the clean-flag
loss, and the within-row odd-cycle matching on the canonical factors through
\(b=9\).  The computation is an audit only; the proofs above are
solver-independent.
