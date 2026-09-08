# One screened core occurrence on the actual rotating-hole source forces linear complete compiler damage

Date: 2026-08-01  
Lane: additive-constant regeneration / complete-damage bridge  
Status: exact `H=1` counterexample to the unqualified depth-uniform bridge.  It is embedded in the shortest rail's own maximal erosion source.  It does not refute a globally chosen Pascal spine which avoids this cap/reference-matching configuration.

## 0. Outcome

The shortest rotating-hole rail has a particularly simple depth-`h` source:
one common core `K` plus one cyclic active label at every source position.
This does **not** make its terminal compiler damage bounded.

For every

\[
                            h\ge2,\qquad m\ge h+2,          \tag{0.1}
\]

there are two nonzero source words `A^-`,`A^+` on the exact shortest-rail
caps such that

1. `D^h A^-=D^h A^+` is the complete rank-`m` rotating-hole owner cycle;
2. `A^+` contains one new literal task cell, forced to a unique physical
   position by its carrier cap;
3. one retained old interval row plus the task row screen one redundant
   core-coordinate occurrence from a length-`h` source block; but
4. every reference compiler matching saturating a displayed bank of strict
   lower targets loses at least

   \[
                              h-1                           \tag{0.2}
   \]

   matched cells in the plus state.

Thus no theorem based only on

* shortest-rail owner/q1/residence legality,
* equality of the old and plus middle carriers,
* one legal terminal task cell, and
* local maximal-letter feasibility

can imply an `O(1)` complete-damage bound uniform in `h`.  The missing
positive input must control how the chosen task screen meets the occurrence
rays of a **reference compiler matching**.

This strengthens the separated-interface ray example in
`MATH_THEOREM_A_FIXED_H_RAIL_MATCHED_DAMAGE_SELECTOR_AND_RAY_COUNTEREXAMPLE_20260801.md`:
the owner carrier here is literally the rotating-hole cycle, not an
arbitrary depth-neutral Johnson fragment.

## 1. The actual shortest-rail source

Use the notation of
`MATH_THEOREM_BOOLEAN_HEX_SHORTEST_RESIDENT_RETURN_RAIL_AND_PHASE_DECOUPLING_20260801.md`.
Put

\[
 n=h+3,qquad \Gamma=(z_0,z_1,\ldots,z_{n-1}),             \tag{1.1}
\]

and let `K` be a disjoint core of size

\[
                         |K|=m-h-1\ge1.                    \tag{1.2}
\]

The maximal rail source at integer position `t` is

\[
 P_t=K\cup\{q_t\},\qquad q_t=z_{t+3\pmod n}.              \tag{1.3}
\]

On the finite source interval

\[
                         0\le t\le2h+2                     \tag{1.4}
\]

the `n` consecutive depth-`h` owner windows are the `n` rotating-hole
owners: each is `K` plus `h+1` consecutive active labels, hence the
complement in `K union Gamma` of two consecutive active labels.

Choose one core coordinate `epsilon in K` and put `K0=K-{epsilon}`.  Define
the final plus source by screening `epsilon` from one consecutive block:

\[
 A_t^+=K_0\cup\{q_t\}
        \cup\begin{cases}
              \varnothing,&h\le t\le2h-1,\\
              \{\epsilon\},&\text{otherwise}.
             \end{cases}                                  \tag{1.5}
\]

Define the reference source by adding one redundant occurrence,

\[
 A_h^-=A_h^+\cup\{\epsilon\},\qquad
 A_t^-=A_t^+\quad(t\ne h).                                \tag{1.6}
\]

### Lemma 1.1 (exact carrier and rank preservation)

Every length-`h+1` source interval has the same union in `A^-` and `A^+`,
and that union has rank `m`.  The resulting `n` owners, cyclically closed,
are exactly the shortest rotating-hole owner cycle up to an index shift.

#### Proof

The screened block is bracketed by plus occurrences of `epsilon` at `h-1`
and `2h`, distance `h+1` apart.  Every length-`h+1` interval with starting
point `0,...,n-1=h+2` contains an allowed occurrence.  A window containing position `h`
already contains `h-1` if it starts before `h`, and contains `2h` if it
starts at `h`.  The extra reference occurrence is therefore redundant in
every owner window.

Every other core coordinate occurs everywhere.  The active contribution is
`h+1` consecutive labels of the `n=h+3` cycle.  Hence each owner has size

\[
                         |K|+(h+1)=m,                      \tag{1.7}
\]

and misses exactly two consecutive active labels.  Shifting the source
window removes one active label and adds one, including at cyclic closure,
so this is precisely the rotating-hole Johnson cycle.  \(\square\)

Thus the edit (1.6) is invisible not merely to an abstract middle row but to
the full owner/q1/residence/internal-upper rail object.

## 2. A forced terminal task cell

At position `h`, the maximal carrier cap is

\[
                         P_h=K\cup\{q_h\}.                  \tag{2.1}
\]

Assign the literal task

\[
                         \tau=K_0\cup\{q_h\}               \tag{2.2}
\]

to the singleton cell `[h,h]`.  Its equality row screens `epsilon` out of
`P_h` and gives `A_h^+`.

Only **one** old equality row is needed to screen the rest of the block.  Put

\[
 J=[h+1,2h-1],\qquad
 B=K_0\cup\{q_{h+1},q_{h+2},\ldots,q_{2h-1}\}.             \tag{2.2a}
\]

Assign the old target `B` to the interval cell `J`.  Exactness of this row
forces every source letter in `J` to omit `epsilon`; the task row supplies
the screen at `h`.  Outside `[h,2h-1]` retain the full carrier caps.  The
maximal-letter word is then exactly (1.5).

This screen is rank-correct and occurrence-labelled:

\[
                         |B|=|K_0|+(h-1)=m-3.              \tag{2.2b}
\]

Its active labels form a proper directed arc of the `n=h+3` cycle, whose
next occurrence starts beyond the finite source word.  Hence `J` is the
unique old and plus witness of `B`.  The edge `B-J` survives unchanged.
Thus one retained old cap row plus one new task row forces the hostile cap
state; there is no hidden bank of `Theta(h)` screening tasks.

The task position is forced.  The active word `q_t` has period `n=h+3`,
but the next occurrence of `q_h` is at

\[
                         h+n=2h+3,                          \tag{2.3}
\]

one position beyond the finite source word.  Hence `[h,h]` is the only
interval whose plus union is `tau`.

The screening rows are part of the final cap state.  They are needed for
the lower bound: owner equality alone permits moving the redundant
`epsilon` occurrence into the damaged ray.  This is exactly why marginal
rail legality does not control complete compiler damage.

## 3. The forced matched ray

For `1<=j<h`, put

\[
 I_j=[h,h+j],\qquad
 S_j=\bigcup_{t=h}^{h+j}A_t^-
     =K_0\cup\{\epsilon,q_h,q_{h+1},\ldots,q_{h+j}\}.       \tag{3.1}
\]

These are strict lower targets.  Indeed,

\[
 |S_j|=|K|+j+1=m-h+j\le m-1.                              \tag{3.2}
\]

All `I_j` have compiler width at most `h`.

### Theorem 3.1 (linear complete-damage lower bound)

For each `1<=j<h`, `I_j` is the unique reference interval realizing
`S_j`, while `S_j` is absent from the complete plus word.  Consequently,
every reference compiler matching saturating the targets
`S_1,...,S_(h-1)` uses the distinct cells `I_1,...,I_(h-1)`, and every
complete plus-state damage set satisfies

\[
                         |D\cap C(M_0)|\ge h-1.             \tag{3.3}
\]

The task cell `[h,h]` is different from all these damaged cells.

#### Proof

The active labels in `S_j` form the directed cyclic arc

\[
                         q_h,q_{h+1},\ldots,q_{h+j}         \tag{3.4}
\]

of length `j+1<n`.  Inside the finite source interval (1.4), this arc occurs
consecutively only at positions `h,...,h+j`: its previous occurrence starts
before zero, and its next occurrence starts at `h+n=2h+3`, beyond the word.
An interval beginning earlier or ending later introduces an active label
outside (3.4), while a shorter interval misses an endpoint label.  Therefore
the active part alone forces `I_j`.

In the reference word, `I_j` contains the extra `epsilon` at `h`, proving
that its union is `S_j`.  In the plus word, no position of `I_j` carries
`epsilon`: its next allowed occurrence is the guarded position `2h`, and
`h+j<=2h-1`.  Hence

\[
                  \bigcup_{t\in I_j}A_t^+=S_j-\{\epsilon\}.\tag{3.5}
\]

Any plus interval containing `epsilon` uses position `h-1` or `2h`; its
active union contains the guard label `q_(h-1)` or `q_(2h)`, neither of
which belongs to (3.4).  Thus no plus interval realizes `S_j`.

The targets are distinct and have unique reference cells, so every matching
saturating them contains all displayed edges.  All fail in the plus state,
which forces (3.3).  \(\square\)

This is a literal complete-damage result, not the symmetric-difference
count of source positions: only one source occurrence changes, but it lies
on `h-1` forced matched cells.

## 4. Exact scope

The theorem refutes the following unqualified implication:

\[
\begin{array}{c}
\text{one legal shortest rail + one legal task cell + exact owner equality}
\\\Downarrow\\
\text{some uniformly bounded complete-damage charge}.
\end{array}                                               \tag{4.1}
\]

It also shows that allowing the terminal cap to differ from the carried cap
does not help by itself: the final cap can force the bad ray.

It does **not** prove that every integrated Pascal child has linear damage.
A global construction may jointly choose

* another task occurrence;
* a cap state with diffuse core-coordinate providers;
* a reference matching which avoids heavily loaded occurrence rays; or
* duplicate witnesses for the targets `S_j`.

The task occurrence is unique and the matching is forced in this family,
so any positive theorem must explicitly exclude at least one of these
features.  The weakest honest positive row remains the retainable-submatching
condition

\[
 \min_\theta\left(|M_0|-max\{|F|:\operatorname{CQ}(\theta,F)\}\right)=O(1),
                                                               \tag{4.2}
\]

or a sufficient diffuse occurrence-load estimate relative to `M0`.

In particular, the raw rail menu `(m-2)(m-2)_h`, its constant upper-ray
signature, and the fixed-H q1 planting theorem do not imply (4.2).

## 5. Audit

Run

```text
python3 scratch/audit_h1_rotating_hole_complete_damage_linear_nogo_20260801.py
```

The dependency-free replay checks `2<=h<=30`, using `m=h+3`.  It verifies:

* the complete cyclic rank-`m` rotating-hole owner sequence;
* equality of every depth-`h` owner in the old and plus sources;
* the unique terminal task cell;
* the ranks and widths of every `S_j`;
* uniqueness of every reference witness; and
* absence of every `S_j` in the plus word.

The construction and proof work verbatim for every `m>=h+2` by enlarging
the common core.

Canonical audit payload SHA-256:

```text
651c4879e9e5832657e70485b2612a0c59e0971a51321ed737ec246b135a3942
```
