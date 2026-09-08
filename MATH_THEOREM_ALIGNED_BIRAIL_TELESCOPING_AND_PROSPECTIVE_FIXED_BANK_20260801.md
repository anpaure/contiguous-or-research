# Aligned birail damage telescopes; bounded prospective banks pack

Date: 2026-08-01  
Status: unconditional signed-action and prospective-packing theorems, plus a
corrected conditional `B(k)+O(1)` implication.  Physical regeneration and
terminal occurrence Hall remain open.

## 0. Quantifier correction

The quadratic mixed-coatom atlas is prospective.  Its `q(q-1)` choices have
different old words.  After a literal old chronology is fixed, the ordered
active data are fixed (or have only the two inverse orders under a fixed
owner set).  Consequently the atlas is not a quadratic neighbourhood of a
frozen chronology, and it does not generate a full symmetric orbit there.

Any serial use must prepare the successive old slots jointly.  The results
below retain exactly that prospective quantifier.

## 1. The literal active packet is an involution

One authenticated active twelve-owner pair is

```text
O = 26 25 0d 19 29 2c 2a 23 0b 13 15 07
N = 26 23 0b 19 29 2a 2c 25 0d 15 13 07
```

with six-coordinate hexadecimal masks.  Let `tau_ab` exchange active
coordinates `1` and `2`.  Entry by entry,

\[
                              N=\tau_{ab}(O).
\]

The endpoints `26,07` contain both active coordinates and are fixed by
`tau_ab`.  The other two authenticated active rethreads are conjugate
copies: row 3 uses `tau_ac` and row 5 uses `tau_bc`.  Thus each move at one
fixed slot is an involution under its corresponding active-label
transposition,

\[
                              O\longleftrightarrow N.
\]

Applying it twice backtracks.  A different transposition needs a different
prospectively exposed old slot.

## 2. Exact all-depth telescoping

At every lower depth `2<=s<=d`, write the full literal fixed base as
`B=K union {infinity,c}` and the two nested filler profiles as `P_s,S_s`.
A packet with active transition `x -> y` has signed value-multiset action

\[
 \Delta_s(x,y)=
 [B\cup P_s\cup\{y\}]+[B\cup S_s\cup\{x\}]
 -[B\cup P_s\cup\{x\}]-[B\cup S_s\cup\{y\}].     \tag{2.1}
\]

This is the minimum two-old/two-new action proved by the planted packet
audit.

### Theorem 2.1 (aligned birail telescoping)

For a prospectively prepared aligned sequence

\[
                        x_0\to x_1\to\cdots\to x_t
\]

using the same literal base `B` and the same profile pair at depth `s`, the
total signed action is

\[
 \boxed{
 \sum_{i=0}^{t-1}\Delta_s(x_i,x_{i+1})
 = [B\cup P_s\cup\{x_t\}]+[B\cup S_s\cup\{x_0\}]
  -[B\cup P_s\cup\{x_0\}]-[B\cup S_s\cup\{x_t\}].} \tag{2.2}
\]

#### Proof

The `P_s` terms form the telescoping sum

\[
 \sum_i([P_s\cup\{x_{i+1}\}]-[P_s\cup\{x_i\}]),
\]

and the `S_s` terms telescope in the opposite direction. \(\square\)

The same active transition occurs at every depth, so (2.2) holds
simultaneously for all `s=2,...,d`.  Internal labels cancel.  A closed
aligned circulation `x_t=x_0` has zero signed lower value-multiset action at
every depth.

Literal alignment is load-bearing: equal profile cardinalities, isomorphic
flags, or separately relabelled bases do not cancel in the free abelian
group on literal target values.

The quadratic atlas does not itself furnish such a chain.  In the canonical
`q(q-1)` atlas the varying roles are `c,delta`, while the involution swaps the
fixed roles `a,b`; moreover `c` belongs to the base `B`.  A separate
prospective embedding theorem must align the entire bases and filler flags
while exposing transitions `x_0->...->x_t`.  The known owner-disjoint
triangle has the desired algebraic circulation, but repeats q1 socket
colours and hence is not yet a strict-rainbow bank.

This is a nonaccumulation theorem: the residual consists only of the two
endpoint rails.  It is not an occurrence theorem.  Packet cells live at
different physical addresses, so (2.2) does not identify target--cell
incidences or imply a common-cap matching.

## 3. Fixed-number prospective packing

For one planted atlas put

\[
                              L=q(q-1).
\]

One option uses at most `16d+64` noncommon U1--U4 resource tokens, and a
fixed noncommon token appears in at most `2(q-1)` options of another atlas.
If the common anchor skeletons of two tasks are private, one selected option
therefore excludes at most

\[
                         (32d+128)(q-1)               \tag{3.1}
\]

options of the other task.

### Theorem 3.1 (greedy bounded-bank packing)

Let `H` prospective packet tasks have the full `q(q-1)` atlases above.
Assume their physical planted slots are disjoint (or address collisions are
counted as tokens), and every token common to one atlas is absent from the
entire support of every other atlas.  Then they have pairwise
noncommon-token-disjoint choices whenever

\[
                         q>(H-1)(32d+128).            \tag{3.2}
\]

#### Proof

After `j<H` choices, the union bound from (3.1) excludes fewer than

\[
                         j(32d+128)(q-1)
\]

options of the next task.  Since it has `q(q-1)` options, one remains if
`q>j(32d+128)`. \(\square\)

For central parameters `q=Theta(k)` and `d=Theta(sqrt(k))`, every fixed `H`
eventually satisfies (3.2).  The privacy condition is stronger than
pairwise-disjoint common-token sets: a token common to one atlas cannot even
occur noncommonly in an option of another.  The audited token ledger also
does not include trace guards, physical common-cap addresses, or the
`O(d^2)` occurrence-incidence footprint.

## 4. Correct serial implication

The proof-safe serial bound is

\[
 \nu(k)\le B(k)+u(T_0)+
 \min_{T\in\operatorname{Comp}_\Gamma(T_0)}
       \bigl(\chi(T)+\lambda_d(T)\bigr),             \tag{4.1}
\]

where `chi` is the uncontracted extra-position charge and `lambda_d` is the
terminal occurrence-labelled compiler deletion number.

### Theorem 4.1 (regenerating aligned-birail criterion)

Suppose that for all sufficiently large `k` there is an upper-complete
resident chronology `T_0` and a prospectively prepared serial sequence of
mixed-coatom moves satisfying:

1. every move is a literal equal-length replacement, so `chi=0` throughout;
2. after each move the resulting chronology exposes the old phase of the
   next move;
3. routing chains are aligned to one literal `B,P_s,S_s` system at every
   depth;
4. common anchors are private or certified incumbent-safe;
5. every move preserves the full exterior interval-union language, owners,
   topology and residence; and
6. the final guarded target--cell incidence graph has matching deficiency at
   most an absolute constant `C`.

Then

\[
                              \nu(k)\le B(k)+C.
\]

If `C=0`, then `nu(k)=B(k)`.

#### Proof

Conditions 1--5 give a walk in the physical safe component with unchanged
upper defect zero and `chi=0`.  Theorem 2.1 shows that internal signed lower
value damage does not accumulate, although condition 6 is still needed for
physical occurrences.  Solve the compiler only at the terminal chronology
and apply (4.1).  The general lower bound gives equality when `C=0`.
\(\square\)

If split-letter or insertion packets are used instead, condition 1 must be
replaced by a proof that all split positions contract/recycle and terminal
`chi=O(1)`.  A constant cost per serial move is not enough.

## 5. Exact remaining theorem

The two unconditional results remove two former concerns:

* aligned lower value damage is an endpoint current, not a quantity linear
  in the number of moves;
* noncommon U1--U4 collisions do not obstruct any fixed prospective bank.

The remaining statement is precisely:

\[
 \boxed{
 \begin{array}{c}
 \text{prospectively plant a regenerating aligned slot sequence with}\\
 \text{private/common-safe anchors and prove terminal occurrence Hall.}
 \end{array}}
\]

Signed telescoping cannot replace the last Hall row.  The exact condition is

\[
 |N_{E_{\rm all}}(X)\setminus D^*|\ge|X|
 \quad\text{for every lower-target family }X,
\]

in one common guarded cap state.
