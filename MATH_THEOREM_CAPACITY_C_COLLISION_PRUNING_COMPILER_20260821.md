# Capacity-c collision trimming compiles every low-hole wreath factor

**Date:** 2026-08-21  
**Method:** pure mathematics  
**Status:** exact q=1 compiler; the multisegment and deeper-shadow scope is
stated explicitly

## 0. Outcome

Let

\[
 b=2r+1,\qquad
 \mathcal M=\binom{[b]}r,\qquad
 \mathcal L=\binom{[b]}{r-1},\qquad
 A=|\mathcal M|,\qquad L=|\mathcal L|,
 \tag{0.1}
\]

and let \(\mathscr F\) be an exact middle-wreath factor.  Thus
\(|\mathscr F|=A/b\), and the cyclic rank-\(r\) decks of its rows partition
\(\mathcal M\).  For a row family \(\mathscr S\subseteq\mathscr F\), write

\[
 \mu_{\mathscr S}(T)
   =|\{C\in\mathscr S:T\in\mathsf L(C)\}|,
 \qquad
 Q(\mathscr S)
   =\sum_{T\in\mathcal L}(\mu_{\mathscr S}(T)-1)_+,
 \tag{0.2}
\]

where \(\mathsf L(C)\) is the cyclic rank-\((r-1)\) deck of \(C\).
The quantity \(Q\) is the number of lower occurrences that must be made
dirty in order to leave every occurring lower target at most once.

The main theorem is deliberately elementary.

> **Capacity-pruning compiler.**  For every integer \(1\le c\le b\), there is a
> subfamily \(\mathscr S\subseteq\mathscr F\), obtained by deleting at most
> \(Q(\mathscr F)/c\) whole rows, and a choice of at most \(c\) dirty
> starts in every surviving row, such that all clean rank-\((r-1)\) windows
> are distinct.  The same-start clean rank-\(r\) windows are also distinct,
> and the total number of lost middle/lower flags is at most
>
> \[
>             {bQ(\mathscr F)\over c}+{cA\over b}.
> \tag{0.3}
> \]

Consequently, if \(Q(\mathscr F)=O(A/b)\), then any choice

\[
                 c\longrightarrow\infty,
 \qquad c=o(b)
 \tag{0.4}
\]

retains \((1-o(1))|\mathscr F|\) rows, makes only \(o(b)\) starts dirty in
each surviving row, and loses only \(o(A)\) flags.  In particular, a
low-hole exact factor is already enough: if its number \(h\) of missing
lower targets is \(O(A/b)\), then

\[
 Q(\mathscr F)=A-L+h={2A\over r+2}+h=O(A/b).
 \tag{0.5}
\]

Thus the capacity-one pseudoforest obstruction is not an asymptotic
obstruction once a slowly growing number of punctures per row is allowed.

## 1. Exact capacity-c clean-deck Hall criterion

Fix a row family \(\mathscr S\), and assume \(0\le c\le b\).  Giving a row
at most \(c\) dirty starts is equivalent to choosing at least \(b-c\) of
its lower occurrences as clean.  The clean occurrences chosen across all
rows must have distinct targets.

For \(\mathscr R\subseteq\mathscr S\), abbreviate

\[
 U(\mathscr R)=\bigcup_{C\in\mathscr R}\mathsf L(C),
 \qquad
 Q(\mathscr R)=b|\mathscr R|-|U(\mathscr R)|.
 \tag{1.1}
\]

This agrees with (0.2), since the total number of lower occurrences in
\(\mathscr R\) is \(b|\mathscr R|\).

### Lemma 1.1 (capacitated clean-deck Hall)

There is a target-distinct choice of \(b-c\) clean lower occurrences in
every row of \(\mathscr S\) if and only if

\[
       |U(\mathscr R)|\ge(b-c)|\mathscr R|
       \quad\hbox{for every }\mathscr R\subseteq\mathscr S,
 \tag{1.2}
\]

or equivalently

\[
                   Q(\mathscr R)\le c|\mathscr R|.
 \tag{1.3}
\]

#### Proof

Make \(b-c\) identical demand clones of each row, adjacent to that row's
\(b\) distinct lower targets, and give every target capacity one.  Hall's
condition is (1.2).  It suffices to test unions of complete row-clone
groups: for a fixed set of represented rows, adding all of their clones
increases demand without changing the target neighborhood.  An integral
saturating matching chooses the clean occurrences. \(\square\)

The least capacity needed without deleting rows is therefore

\[
 c^*(\mathscr S)
    =\max_{\varnothing\ne\mathscr R\subseteq\mathscr S}
       \left\lceil{Q(\mathscr R)\over|\mathscr R|}\right\rceil.
 \tag{1.4}
\]

It can be computed exactly by bipartite matching for successive values of
\(c\), or by the corresponding min-cut density optimization.

There is a stronger, different problem in which every occurring target
must remain clean exactly once.  Its target-to-row flow has capacity-one
incidence arcs and is not characterized by the weaker target-neighborhood
inequalities \(q(\mathcal U)\le c|N(\mathcal U)|\).  The compiler here
allows a target to disappear; only clean-target distinctness is required.

## 2. Delete a violated row family

### Theorem 2.1 (capacity-pruning compiler)

For every finite row family \(\mathscr S_0\) and every integer
\(1\le c\le b\), there is a subfamily
\(\mathscr S\subseteq\mathscr S_0\) such that

1. \(\mathscr S\) satisfies (1.2);
2. \(|\mathscr S_0\setminus\mathscr S|\le Q(\mathscr S_0)/c\); and
3. each surviving row has at most \(c\) dirty starts and all chosen clean
   lower targets are distinct.

#### Proof

Start with \(\mathscr S=\mathscr S_0\).  While (1.3) fails, choose a
violating row family \(\mathscr R\subseteq\mathscr S\) and delete all its
rows.  Since

\[
 \begin{aligned}
 Q(\mathscr S)-Q(\mathscr S\setminus\mathscr R)
   &=b|\mathscr R|-
      \bigl(|U(\mathscr S)|-|U(\mathscr S\setminus\mathscr R)|\bigr)\\
   &\ge b|\mathscr R|-|U(\mathscr R)|\\
   &=Q(\mathscr R)>c|\mathscr R|,
 \end{aligned}
 \tag{2.1}
\]

every deletion pays for more than \(c\) units of the global collision
excess per removed row.  The deleted row families in different iterations
are disjoint.  If any row is deleted, telescoping (2.1) gives

\[
       c|\mathscr S_0\setminus\mathscr S|
          <Q(\mathscr S_0)-Q(\mathscr S)
          \le Q(\mathscr S_0).
 \tag{2.2}
\]

If no row is deleted, the claimed weak bound is immediate.  The process
terminates, and Lemma 1.1 then supplies \(b-c\) clean occurrences per
surviving row.  Mark the other \(c\) starts dirty. \(\square\)

The proof is algorithmic.  A failed matching instance returns a violated
row-clone Hall set; delete its underlying rows and repeat.

## 3. Exact physical q=1 lift

Return to an exact middle factor \(\mathscr F\).  Apply Theorem 2.1, and
for every lower occurrence not chosen by the clean-deck matching delete
the same cyclic start in its row's rank-\(r\) deck.  Every surviving row
has exactly \(b-c\) chosen clean starts.  Their lower windows are distinct
by construction.  Their middle windows are distinct because all middle
windows of the original factor were distinct.  Same-start containment
therefore gives a matching in the middle inclusion graph.

If \(d=|\mathscr F\setminus\mathscr S|\), the construction loses \(bd\)
flags with the deleted rows and \(c|\mathscr S|\) more flags with the dirty
starts.  By (2.2) and \(|\mathscr S|\le|\mathscr F|=A/b\),

\[
 bd+c|\mathscr S|
   \le {bQ(\mathscr F)\over c}+{cA\over b},
 \tag{3.1}
\]

which proves (0.3).  A maximum clean-deck matching may retain more than
\(b-c\) starts in some rows, but (3.1) is the unconditional bound.

For the full exact factor, the total number of lower occurrences is
\(b|\mathscr F|=A\).  If \(h\) lower targets are absent, then exactly
\(L-h\) distinct targets occur, so

\[
 Q(\mathscr F)=A-(L-h)=A-L+h,
 \tag{3.2}
\]

proving (0.5).

## 4. Multisegment scope

Deleting \(d_C\le c\) cyclic starts from a surviving row decomposes its
clean starts into at most \(d_C\) directed cyclic intervals when
\(d_C>0\) (and leaves one cycle when \(d_C=0\)).  Thus the exact object
compiled above is a union of at most \(c\) directed row segments, not one
single punctured row.

If a later construction needs blocks of \(H\) consecutive clean starts,
discarding the length-\(H\) boundary neighborhood of every dirty start
costs at most

\[
                  Hc|\mathscr S|\le {HcA\over b}
 \tag{4.1}
\]

additional starts.  Choose the slowly growing capacity so that

\[
              c\to\infty,\qquad cH=o(b).
 \tag{4.2}
\]

Then (4.1) is \(o(A)\); such a choice exists whenever \(H=o(b)\).

The theorem itself is exact only for the middle/first-shadow same-start
flags.  It does not assert distinctness at depths \(q\ge2\), compile the
abstract GK alternating chains into fixed factor/order atoms, or join the
resulting clean intervals across their dirty boundaries.  Those remain
separate gates.
