# The q4 k17 rank-seven mark language is the full binary shift at periods ten and eleven, while the exact census has a sharp run gate

**Date:** 2026-08-14

**Status:** exact local theorem, sharp projected type-run criterion, and
explicit all-face schedule theorem.  Every binary mark word of period ten
or eleven has a literal lift to the 72-state five-core automaton.  The
frozen nine-type census is not automatic for an arbitrary collection of
such words: its unmarked type-ID projection has the exact run language and
integer gate below.  Nevertheless, all fourteen mixed faces have independently replayed
exact-census schedules with all 286 unmarked positions cyclically
three-separated.  For a future selected quotient factor, choosing a
three-separated representative of every doubled lower-q2 orbit reduces to
2-SAT.  A general 2-SAT solution still needs either the displayed canonical
mask multiset or a final exact-census state refinement.

## 0. Result

Call a schedule position **unmarked** when its rank-seven occurrence is not
the chosen representative of its orbit.  In the notation of
`MATH_THEOREM_Q4_K17_ALL_MIXED_FACES_HAVE_PURE_CORE_CYCLE_SCHEDULES_20260814.md`,
this is

\[
 U(i)=1
 \quad\Longleftrightarrow\quad r(s_i)=0
 \quad\Longleftrightarrow\quad
 k_2(s_i)=1
 \quad\Longleftrightarrow\quad
 \operatorname{type}(s_i)\in\{0,3,6\}.             \tag{0.1}
\]

The exact unmarked type counts are

\[
                    (n_0,n_3,n_6)=(139,20,127),
              \qquad n_0+n_3+n_6=286.              \tag{0.2}
\]

There are three conclusions.

1. Every one of the `2^10=1,024` directed period-ten binary words and every
   one of the `2^11=2,048` directed period-eleven binary words has a literal
   closed lift in the exact 72-state automaton.  Up to directed rotation,
   these are respectively all `108` and all `188` binary necklaces.
2. After imposing `(0.2)`, the only legal unmarked-to-unmarked type arcs are

   \[
                              0\to6,qquad3\to3,qquad3\to6.     \tag{0.3}
   \]

   This gives the exact projected type-ID run allocation criterion in
   Section 2.  In
   particular there can be at most `20+127=147` unmarked-to-unmarked
   adjacencies, so the 286 unmarked positions occupy at least 139 cyclic
   runs (apart from the convention for an all-unmarked component).
3. For every mixed face `0<=t<=13`, there is an exact 1,430-position
   schedule with the frozen nine-type count vector

   \[
             (139,297,8,20,20,140,127,237,442),       \tag{0.4}
   \]

   exactly `143-11t` period-ten cycles, exactly `10t` period-eleven cycles,
   and all 286 unmarked positions at pairwise cyclic distance at least
   three on their own cycles.  Literal state words for all fourteen faces
   are frozen and independently replayed.

Thus the rank-seven coupling has no local binary-necklace obstruction.  Its
first type-level obstruction is the small global run/census gate, and there
is an explicit isolated target family on every scalar face.

## 1. The full binary mark shift

The literal five-core states and transitions are those of the frozen
pure-core theorem.  A state is an ordered partition
`K=(K_0,K_1,K_2)` of five labels and

\[
             K\longrightarrow K'
       \quad\Longleftrightarrow\quad
             K'_1\subseteq K_0,qquad K'_2\subseteq K_1.       \tag{1.1}
\]

There are 72 states and 793 directed arcs.  The exhaustive replay fixes a
binary word `w`, restricts position `i` to the 40 unmarked states when
`w_i=1` and to the 32 marked states when `w_i=0`, and performs exact cyclic
reachability including the last-to-first wrap.  It finds a literal witness
for every word of both allowed periods.  No reversal is used.

This theorem is stronger than merely finding some schedules, but it must
not be confused with the exact-census statement.  Selecting an arbitrary
lift independently on every rail need not add to `(0.4)`.

## 2. Exact projected unmarked type-run language and integer criterion

Projecting `(1.1)` to the nine core profiles gives exactly `(0.3)` among
the three unmarked types.  Hence a nonconstant cyclic unmarked run is one
of

\[
\begin{array}{c|l}
L=1 & 0,\ 3,\ 6,\\
L=2 & 06,\ 33,\ 36,\\
L\ge3 & 3^L,\ 3^{L-1}6.
\end{array}                                                     \tag{2.1}
\]

An all-unmarked cycle is necessarily `3^N`, since neither `0` nor `6` can
lie on a directed all-unmarked cycle.

Here is a sharp aggregate test at the nine-type quotient.  Let

* `h` be the number of positions in all-unmarked cycles;
* `a` be the number of length-one runs in all other cycles;
* `b` be the number of length-two runs;
* `ell` be the number of runs of length at least three; and
* `S` be the total length of those `ell` long runs.

Necessarily

\[
                        h+a+2b+S=286.                \tag{2.2}
\]

The unmarked positions admit an assignment of type IDs with exactly the
census `(0.2)` and the projected arcs `(0.3)` if and only if `h<=20` and
there are integers `x,z,q` satisfying

\[
\begin{aligned}
 &x\ge0,\quad z\ge0,\quad x+z\le b,\quad 0\le q\le\ell,\\
 &x\le139,qquad x+z+q\le127,\\
 &2x+z+q\ge266-a.                                  \tag{2.3}
\end{aligned}

Here `x` is the number of length-two runs assigned `06`, `z` the number
assigned `36`, and `q` the number of long runs ending in `6`.  The remaining
length-two runs are `33`; the singleton counts are forced to be

\[
 u_0=139-x,qquad
 u_6=127-x-z-q,qquad
 u_3=a-266+2x+z+q.                                  \tag{2.4}
\]

Conditions `(2.3)` are precisely the nonnegativity conditions for all of
these choices.  Conversely, the choices explicitly build every projected
type-ID run in `(2.1)`, so the test is sufficient as well as necessary at
that quotient.  Equation `(2.2)` then forces the remaining type-3 count to
be `20-h`.

This iff does **not** assert that an arbitrarily chosen type-ID allocation
lifts to compatible labelled states across the marked boundaries, nor that
the six marked-type counts can then be met.  Those are literal-state/global
census questions.  Section 3 supplies them for the displayed canonical
mask family by independent certificates; Section 5 retains them as a
residual refinement for a generic 2-SAT mask family.

Two useful quick cuts follow:

\[
        \#(U\to U)\le147,qquad
        \sum_{L\ge3}(L-1)\le20-h.                  \tag{2.5}
\]

They explain why packed masks fail even though every individual binary
necklace lifts when its type counts are unconstrained.  For example, a
large all-unmarked component consumes only type 3, of which the frozen
census has twenty copies.  Likewise, 143 disjoint length-two runs cannot
realize `(139,20,127)`: choosing 139 copies of `06` already uses 139 copies
of type 6.

## 3. Exact isolated schedules on all fourteen faces

For face `t`, put

\[
             a_t=143-11t,qquad b_t=10t,qquad
             c_t=a_t+b_t=143-t.                    \tag{3.1}
\]

Take `c_t` cycles in the required period families.  On every cycle put
unmarked positions at phases `0` and `3`.  On the first `2t` cycles also put
an unmarked position at phase `6`.  This gives

\[
                   2(143-t)+2t=286                 \tag{3.2}
\]

unmarked positions.  In periods ten and eleven, the cyclic gaps of every
two-position mask are at least `3`, while the three-position masks have
gaps `(3,3,4)` or `(3,3,5)`.  Thus every pair of unmarked positions on a
cycle has cyclic distance at least three.

The H100 search fixed these masks, used a literal 72-state variable at each
position, imposed every arc and cyclic wrap of `(1.1)`, and imposed all nine
equalities `(0.4)`.  It returned an exact schedule on every face.  The
independent replay reconstructs the state catalogue without importing the
search source and checks:

* all 20,020 literal state positions across the fourteen certificates;
* every one of their directed arcs and cyclic wraps;
* every mark bit against type IDs `0,3,6`;
* every distance-three condition;
* each face's exact period counts and 286 unmarked positions; and
* the complete nine-type census `(0.4)` face by face.

This is an existence theorem for the displayed canonical mask multiset.
It is not a claim that every three-separated mask multiset has an exact
nine-type lift.

## 4. The primary pure-period-ten interface is a 1,430-variable exact cover

The live reflection owner master is on the pure face `t=0`.  On this face
the canonical theorem has exactly 143 period-ten cycles, and every one has
exactly two unmarked positions at phases

\[
                              \{\delta,\delta+3\}\pmod {10}.    \tag{4.1}
\]

This makes the factor-to-schedule coupling especially small.  Once a
143-column owner factor is selected, introduce

\[
                   y_{Q,\delta}\in\{0,1\}
       \qquad(Q\text{ a selected rail},\ \delta\in\mathbb Z_{10}).       \tag{4.2}
\]

Delete an option `(Q,delta)` if either `L_Q^(3)(delta)` or
`L_Q^(3)(delta+3)` is a singleton-load orbit.  Each remaining option covers
the two doubled-orbit IDs at these positions.  Impose

\[
\begin{aligned}
       \sum_{\delta\in\mathbb Z_{10}}y_{Q,\delta}&=1
                         &&\text{for every selected rail }Q,\\
       \sum_{Q,\delta} y_{Q,\delta}
          \#\{j\in\{\delta,\delta+3\}:q_Q(j)=A\}&=1
                         &&\text{for every doubled orbit }A.    \tag{4.3}
\end{aligned}

There are only `143*10=1,430` binary variables, 143 rail rows, and 286
doubled-orbit rows.  An option which contains both occurrences of the same
doubled orbit has coefficient two in its orbit row and is therefore
automatically impossible.

### Theorem 4.1

The exact cover `(4.3)` is feasible if and only if the selected pure
period-ten factor can be coupled to the canonical `t=0` certificate so that
every singleton rank-seven occurrence is marked and the two occurrences of
every doubled orbit have opposite mark status.

Indeed, a solution chooses one directed phase on each rail and covers every
doubled orbit exactly once by an unmarked occurrence.  Conversely any such
canonical coupling records exactly one variable on every rail and obeys
the orbit rows.  All 143 certified state cycles have binary mask `{0,3}`;
they may be bijected arbitrarily with the 143 rails and rotated by the
chosen phases.  Their global literal state words already have the exact
nine-type census `(0.4)`.  Thus `(4.3)`, unlike the generic 2-SAT screen
below, closes the complete rank-seven schedule coupling on the live `t=0`
face.

## 5. The generic doubled-orbit isolated selector is 2-SAT

Now fix any selected period-ten/eleven quotient factor whose lower-q2 loads
are exactly

\[
                         858\times1,qquad286\times2.            \tag{5.1}
\]

For every doubled rank-seven orbit `A`, let its two occurrences be `p_A`
and `q_A` and introduce one Boolean variable `x_A`.  Interpret

\[
        x_A=1\Longleftrightarrow p_A\text{ is unmarked},
   \qquad
        x_A=0\Longleftrightarrow q_A\text{ is unmarked}.        \tag{5.2}
\]

Thus every doubled orbit automatically has exactly one unmarked occurrence,
and every singleton orbit is forced marked.  Associate to each doubled
occurrence `p` the literal `lambda_p` which is true exactly when `p` is the
chosen unmarked occurrence.

For any two distinct doubled occurrences `p,q` lying on the same period-`N`
rail at cyclic distance at most two, add

\[
                          \neg\lambda_p\vee\neg\lambda_q.       \tag{5.3}
\]

These are ordinary 2-CNF clauses.  They are sufficient and necessary for
the chosen 286 occurrences to be pairwise cyclically three-separated.
Consequently the isolated representative gate is a linear-time implication
graph test after the quotient factor is known.

If this 2-SAT instance is satisfiable, then:

1. every singleton rank-seven occurrence is marked;
2. exactly one occurrence of every doubled orbit is unmarked;
3. the 286 unmarked positions are isolated and hence automatically pass
   the exact unmarked run criterion `(2.3)` with `a=286`; and
4. every rail mask has a literal local state-cycle lift by Section 1.

For a complete exact-census schedule one must additionally show that the
resulting mask multiset is the canonical family of Section 3 up to directed
rotations and same-period cycle permutation, or solve the residual
72-state exact-census refinement with those fixed masks.  This scope is
important: raw 2-SAT satisfiability alone does not prove the six marked-type
counts in `(0.4)`.

## 6. Exact remaining scope

This theorem removes three possible false obstructions:

* there is no forbidden period-ten or period-eleven binary mark necklace;
* the projected unmarked type-ID census is completely characterized by a
  three-variable integer run test; and
* every mixed face has an explicit exact-census target with isolated
  unmarked positions.

The remaining factor-dependent work is first to obtain the actual selected
quotient cover.  On the live `t=0` face, one then runs the grouped exact
cover `(4.3)`; on a general mask family one may first run the 2-SAT screen
`(5.3)` and then match/refine the resulting masks to an exact state
schedule.  Lower-q2 coverage by itself decides neither finite instance.
This theorem also does not select the quotient factor, fuse its rail
components, or solve the later rank-two through rank-six suffix payloads.

## 7. H100 certificates

All enumeration, search, replay, compilation, and hashing ran through SSH
on H100.  The local Mac was used only for reading, editing, transfer, and
Git.

Full binary-word enumeration and literal cyclic reachability:

```text
scratch/analyze_q4_k17_rank7_mark_necklaces_20260814.py
SHA-256 7475e388b7b12cb879ca2f7b4bbd370b80ce1254ab881ac3aba410ff39e58f86

scratch/analyze_q4_k17_rank7_mark_necklaces_20260814.h100.out
SHA-256 381980e74a8161a12518cd3f053be7578a6a68f097a777b2bbb82f204bca4354
```

The exact-census search, literal fourteen-face certificate, and independent
replay are:

```text
scratch/test_q4_k17_rank7_prescribed_masks_20260814.py
SHA-256 4356834b157cc9ee76531e908a4a2ff2bd6d75d7faea1cd7a5d3584fe35f7ff5

scratch/q4_k17_rank7_isolated_masks_faces0_13_20260814.certificate.json
SHA-256 4bd5e27f6fe0eed0e7c74a8364d0f93bd470b443a51745fd6ccfe6559ad7d49f

scratch/search_q4_k17_rank7_isolated_masks_faces0_13_20260814.h100.out
SHA-256 62746cd081e025504822281e97c47c4dae824166d9eb8aeee05a0b462804eea8

scratch/replay_q4_k17_rank7_isolated_masks_faces0_13_20260814.py
SHA-256 1c3c9c9dff05378fe64a6b39a430d4601ee7cfd72622e3cadd949945669f3c1e

scratch/replay_q4_k17_rank7_isolated_masks_faces0_13_20260814.h100.out
SHA-256 cf27169939b7c8a09af4f9da0b21a4ddb3d3b46eb5f346fb6997732e66c0e917
```
