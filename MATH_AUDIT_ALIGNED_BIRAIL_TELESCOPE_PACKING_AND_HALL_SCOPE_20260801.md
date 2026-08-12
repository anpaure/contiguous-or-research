# Audit of aligned-birail telescoping, prospective packing, and the occurrence-Hall boundary

Date: 2026-08-01  
Lane: independent proof audit of the aligned birail proposal  
Status: `GO` for the involution, the aligned signed-counter telescope, the
bounded prospective packing inequality, and the corrected serial implication,
subject to the literal alignment and privacy hypotheses below.  No physical
regeneration, terminal Hall theorem, or `B(k)+O(1)` conclusion is proved.

## 0. Verdict

Four claims survive audit.

1. The displayed row-1 active replacement is literally an involution.  The
   other two authenticated connector rows have the same **conjugacy form**, but
   use the other two transpositions of `a,b,c`; they do not all use one named
   global `tau`.
2. The complete signed lower multiplicity change telescopes simultaneously at
   every depth `2<=s<=d`, provided that the packets are aligned in the strong
   literal sense: the entire fixed base and the two filler profiles are the
   same after identification, not merely their cardinalities.
3. The greedy inequality

   \[
        q>(H-1)(32d+128)
   \]

   is correct for `H` prospectively planted canonical atlases with uniform
   outside-set size `q`, provided every common token is private from the
   **whole support** of every other atlas and physical-address conflicts are
   absent or included as resource tokens.
4. The proof-safe serial conclusion is the terminal
   `chi+lambda_d` bound.  Equal-length replacement, or an independent uniform
   bound on terminal `chi`, is load-bearing.

The main nonimplication is equally important.  Zero signed lower action is an
identity in the free abelian group on target **values**.  It is not an
occurrence-labelled target-to-cell matching and does not imply common-cap
Hall.

## 1. Literal involution

Use bit order `(e,a,b,c,delta,infinity)`, so `a` and `b` are bits one and two.
The authenticated row-1 words are

```text
O = 26 25 0d 19 29 2c 2a 23 0b 13 15 07
N = 26 23 0b 19 29 2a 2c 25 0d 15 13 07.
```

Let `tau_ab` exchange the `a,b` bits.  Entrywise,

```text
26 -> 26, 25 -> 23, 0d -> 0b, 19 -> 19,
29 -> 29, 2c -> 2a, 2a -> 2c, 23 -> 25,
0b -> 0d, 13 -> 15, 15 -> 13, 07 -> 07.
```

Hence

\[
                         N=\tau_{ab}(O),\qquad
                         O=\tau_{ab}(N).                 \tag{1.1}
\]

The coatom expansion and the intersection/union screens commute with label
permutations, so (1.1) also holds for the full expanded packet when its core,
filler order, and screen schedule are fixed.

The other two authenticated rows are conjugate copies:

* row 3 is old-to-new under `tau_ac`;
* row 5 is old-to-new under `tau_bc`.

Thus the correct uniform sentence is "each authenticated row is an
involution under its corresponding active-label transposition."  Saying that
all three use the same named `tau_ab` is false.

This involution gives reversible backtracking at one prepared slot.  It does
not give a new transposition at that fixed slot: the literal old word fixes
the active roles.

## 2. Exact all-depth signed telescope

The authoritative one-packet counter identity is, for `2<=s<=d`,

\[
\begin{aligned}
 \Delta_s(a,b\mid c)
 &= {\bf e}_{K\infty caP_s}-{\bf e}_{K\infty cbP_s}
   +{\bf e}_{K\infty cbS_s}-{\bf e}_{K\infty caS_s},           \tag{2.1}\\
 P_s&=\{f_1,\ldots,f_{d+1-s}\},\qquad
 S_s=\{f_s,\ldots,f_d\}.
\end{aligned}
\]

At depth one, `Delta_1=0`.

Put `B=K union {infinity,c}` and orient the active transition as `x=b` to
`y=a`.  Suppressing the common base `B`, (2.1) becomes

\[
 \Delta_s(x,y)=
 [P_s\cup\{y\}]+[S_s\cup\{x\}]
 -[P_s\cup\{x\}]-[S_s\cup\{y\}].                 \tag{2.2}
\]

Here and below every displayed target also contains the same literal base
`B`.  This qualification is essential.  Equal profile sizes, isomorphic
flags, or separately relabelled bases do not make terms cancel in the literal
target counter.

### Theorem 2.1 (literal aligned telescope)

Suppose prospectively prepared packets have, after one fixed identification,
the same literal `B,P_s,S_s` at every depth and active transitions

\[
                   x_0\longrightarrow x_1\longrightarrow\cdots
                   \longrightarrow x_t.
\]

Then

\[
\begin{aligned}
 \sum_{i=0}^{t-1}\Delta_s(x_i,x_{i+1})
  ={}&[B\cup P_s\cup\{x_t\}]+[B\cup S_s\cup\{x_0\}]\\
    &-[B\cup P_s\cup\{x_0\}]-[B\cup S_s\cup\{x_t\}].       \tag{2.3}
\end{aligned}
\]

The identity holds simultaneously for every `2<=s<=d`.  If `x_t=x_0`, the
complete lower multiplicity-counter change is zero at every audited depth.

#### Proof

The `P_s` terms are the coboundary

\[
 \sum_i\bigl([B\cup P_s\cup\{x_{i+1}\}]
             -[B\cup P_s\cup\{x_i\}]\bigr),
\]

and the `S_s` terms are its reverse.  Both telescope.  The packet uses the
same active transition at every depth, so the same endpoint cancellation
holds for the whole nested flag.  Depth one is unchanged packetwise.  \(\square\)

### Quantifier warning: the quadratic atlas is not this chain

In the canonical `q(q-1)` planted atlas, the roles varied over the outside
set are `c,delta`, while the involutive old/new move transposes the fixed
roles `a,b`.  Formula (2.1) depends on `c` as part of the base.  Therefore the
quadratic atlas does **not**, by itself, supply a sequence
`x_0->...->x_t` satisfying Theorem 2.1.

To combine the two results one still needs a prospective embedding theorem
which aligns the full bases and filler flags while making the transposed roles
form the required chain or circulation.  The existing owner-disjoint triangle
does this algebraically with a common `c` and transitions
`x->y->z->x`, but its repeated q1 socket colours prevent it from being an
unchanged strict-rainbow bank.

## 3. Prospective packing: exact bound and exact scope

For one canonical planted atlas, let

\[
                              L=q(q-1).                         \tag{3.1}
\]

The audited noncommon-token counts in one option are

\[
 (8d+23)+(8d+20)+16+2+3=16d+64.                               \tag{3.2}
\]

They respectively count owner, lower-seam, upper-seam, prefix-support, and
suffix-support tokens.  Every fixed noncommon token has load at most
`2(q-1)` in another canonical atlas.  Consequently one already selected
option excludes at most

\[
                  (16d+64)\,2(q-1)=(32d+128)(q-1)              \tag{3.3}
\]

options of the next atlas.

### Theorem 3.1 (proof-safe bounded-bank packing)

Let there be `H` prospective tasks, each with a canonical atlas of size
`q(q-1)`.  Assume:

1. their physical planted slots are disjoint, or physical-address conflicts
   are included among the counted resource tokens;
2. for every task `i`, every token common to all options of task `i` is
   absent from every option of every task `j!=i`;
3. (3.2) counts every remaining resource whose collision is forbidden; and
4. the choices are made prospectively, so choosing an option is allowed to
   choose its candidate-dependent old phase.

If

\[
                         q>(H-1)(32d+128),                       \tag{3.4}
\]

then one may choose one option per task with no counted cross-task collision.

#### Proof

After `j<H` choices, (3.3) and the union bound exclude at most

\[
                       j(32d+128)(q-1)
\]

options of the next task.  This is strictly smaller than `q(q-1)` under
(3.4), so one option remains.  Continue greedily.  \(\square\)

The privacy assumption in item 2 is stronger than merely requiring the
common-token sets of two atlases to be disjoint.  If a common token of atlas
`i` occurs as a noncommon token of atlas `j`, selecting that option of `j`
can still kill all `q(q-1)` options of `i`.

The theorem is only a bounded prospective U1--U4 packing statement.  Its
token ledger does not include the `O(d^2)` compiler incidence footprint,
trace guards, occurrence-labelled common-cap resources, or regeneration.

## 4. Signed counters are not occurrence Hall

The vector `Delta_s` lies in the free abelian group on lower target values.
Equation (2.3) says how many times each value is gained or lost in the
packet interiors.  In a closed circulation, those multiplicities return
exactly.

A compiler instead uses an occurrence-labelled incidence graph (or, after
all common-cap conflicts are imposed, an occurrence-labelled conflict
hypergraph):

\[
  \text{lower target}\quad\longleftrightarrow\quad
  \text{physical short-window address under one guarded cap}.                 \tag{4.1}
\]

Counter equality forgets all right-hand vertices in (4.1).  Equal target
multiplicities can migrate to different addresses, collide for one usable
cell, lose a trace guard, or lie outside the fixed common cap.  The exact
native-column analysis makes the missing condition a return-Hall matching;
in the planted maximal erosion its local return graph is empty, despite the
two-chain signed identity.  The separate provider-switch audit also exhibits
external host graphs in which the same local switch improves, preserves, or
worsens maximum matching rank.

Thus none of the following follows from signed telescoping:

* preservation of a previously fixed compiler matching;
* equality of maximum matching rank;
* a bounded common-cap deficiency;
* a transport permutation of physical provider cells.

The terminal Hall row must be stated and proved separately.

## 5. Correct serial implication

Let `Gamma` be a graph whose vertices are literal physical chronologies and
whose edges are replacements checked in their **current** chronology.  Let
`u(T)` be the full upper-language defect, `chi(T)` the number of uncontracted
extra source positions, and `lambda_d(T)` the exact terminal lower-compiler
deletion number.  For a genuinely closed safe component,

\[
 \boxed{
 \nu(k)\le B(k)+u(T_0)+
   \min_{T\in\operatorname{Comp}_\Gamma(T_0)}
       \bigl(\chi(T)+\lambda_d(T)\bigr).}                       \tag{5.1}
\]

This is the correct form of the proposed serial theorem.  A usable edge of
`Gamma` must preserve owners, simple topology, depth-`d` residence, the full
exterior interval-union language, and the declared boundary state; its
result must expose any next proposed old phase.

For the mixed-coatom replacement, old and new words have equal length, so a
literal replacement has `Delta chi=0`.  A prospectively prepared sequence of
such replacements has terminal `chi=0` only if the packets actually replace
allocated equal-length slots rather than being appended as new material.

For split-letter, insertion, or halo-building moves, a constant cost per move
does not suffice.  One must prove that old splits contract or recycle so that
terminal `chi=O(1)`.  Otherwise the cost accumulates along the serial walk.

Consequently, an upper-complete starting chronology and a reachable terminal
state with

\[
                        \chi(T)+\lambda_d(T)\le C                \tag{5.2}
\]

give `nu(k)<=B(k)+C`.  Signed telescoping may help explain why the value-level
damage in (5.2) need not grow with the number of moves, but it does not prove
the occurrence term `lambda_d(T)<=C`.

## 6. Final proof-safe statement

The strongest conclusion supported by the current ledgers is

\[
 \boxed{
 \begin{array}{c}
 \text{aligned active lower counters are endpoint currents;}\\
 \text{every fixed prospective U1--U4 bank packs for large }k;\\
 \text{physical regeneration and terminal occurrence Hall remain open.}
 \end{array}}
\]

In particular, this audit does not prove `nu(k)=B(k)+O(1)`, `B(k)+1`, or
exact equality.

