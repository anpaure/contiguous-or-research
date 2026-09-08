# A resident owner trace is a delayed Johnson queue lift of its depth-`d` intersection trace

**Date:** 2026-08-05  
**Method:** exact sliding-intersection and FIFO event calculus; no computation
or search  
**Status:** unconditional normal form.  A rank-`r` Johnson trace with no
coordinate reinsertion inside `d` transitions projects to a rank-`(r-d)`
Johnson trace.  Conversely, a lower Johnson trace satisfying one explicit
length-`d` queue-avoidance condition lifts to a rank-`r` Johnson trace whose
maximal depth-`d` antecedent is exactly the shifted lower trace.  Owner
Hamiltonicity becomes injectivity of the resulting flag sequence.  This
identifies a concrete positive construction target for the canonical-lock
free-bank problem; it does not prove that target exists.

## 1. From owners to the delayed lower trace

Let

\[
 T=(T_i)_{i\in\mathbb Z_L}
\]

be a cyclic simple rank-`r` Johnson trace, written

\[
 T_{i+1}=T_i-\{D_i\}+\{I_i\}.                                 \tag{1.1}
\]

Fix `1<=d<r`.  Assume that every nonconstant positive run and every zero
gap of every coordinate has length at least `d+1`.  Equivalently for the
calculation below, the deletion labels in any `d` consecutive transitions
are distinct, no one of them is reinserted inside the same owner window,
and an inserted coordinate survives through the next `d+1` owners.  This is
the cyclic biresidence hypothesis already verified on the terminal PBBS
components.

Define the forward depth-`d` intersection trace

\[
 S_i=\bigcap_{h=0}^{d}T_{i+h}.                                  \tag{1.2}
\]

### Theorem 1.1 (sliding-intersection Johnson law)

For every `i`,

\[
 S_i=T_i\setminus\{D_i,D_{i+1},\ldots,D_{i+d-1}\},             \tag{1.3}
\]

so `|S_i|=r-d`, and

\[
 \boxed{S_{i+1}=S_i-\{D_{i+d}\}+\{I_i\}.}                     \tag{1.4}
\]

Thus `S` is itself a cyclic Johnson trace, with lower deletion and insertion
labels

\[
                         a_i=D_{i+d},\qquad b_i=I_i.             \tag{1.5}
\]

#### Proof

Starting from `T_i`, the next `d` owner transitions delete the distinct
coordinates `D_i,...,D_(i+d-1)`.  By the no-cancellation hypothesis, each is
absent from at least one owner in (1.2), while every other coordinate of
`T_i` remains throughout that window.  This proves (1.3).

In passing from (1.2) at `i` to the window based at `i+1`, the old first
owner is removed and the new last owner is added.  Formula (1.3), or a
direct event comparison, shows that the newly excluded coordinate is
`D_(i+d)` and that `I_i`, absent from `T_i` but present throughout
`T_(i+1),...,T_(i+d+1)`, is the newly included coordinate.  This is (1.4).
The two labels are distinct because both sets have rank `r-d`.  \(\square\)

## 2. Exact converse: the FIFO queue lift

Now begin with a cyclic rank-`t` Johnson trace

\[
 S_{i+1}=S_i-\{a_i\}+\{b_i\},
 qquad t=r-d.                                                     \tag{2.1}
\]

Define the delayed deletion queue

\[
 Q_i=\{a_{i-d},a_{i-d+1},\ldots,a_{i-1}\}.                       \tag{2.2}
\]

Assume the following literal queue conditions for every `i`:

\[
 |Q_i|=d,qquad Q_i\cap S_i=\varnothing,qquad b_i\notin Q_i.     \tag{2.3}
\]

Put

\[
                         T_i=S_i\mathbin{\dot\cup}Q_i.            \tag{2.4}
\]

### Theorem 2.1 (delay-`d` queue lift)

The word `T` is a cyclic rank-`r` Johnson trace and

\[
 \boxed{T_{i+1}=T_i-\{a_{i-d}\}+\{b_i\}.}                       \tag{2.5}
\]

Moreover,

\[
 \boxed{S_i=\bigcap_{h=0}^{d}T_{i+h}.}                           \tag{2.6}
\]

Its maximal depth-`d` antecedent is therefore the shifted lower trace

\[
 P_j=\bigcap_{h=0}^{d}T_{j-h}=S_{j-d},                            \tag{2.7}
\]

and

\[
                         D^dP=T.                                  \tag{2.8}
\]

#### Proof

The queue update is

\[
 Q_{i+1}=Q_i-\{a_{i-d}\}+\{a_i\}.                               \tag{2.9}
\]

Here `a_i in S_i`, while (2.3) makes `Q_i` disjoint from `S_i` and excludes
the new lower insertion `b_i` from the old queue.  Combining (2.1) and
(2.9), the copies of `a_i` exchange shores and cancel setwise:

\[
 \begin{aligned}
 T_{i+1}
  &=(S_i-a_i+b_i)\mathbin{\dot\cup}(Q_i-a_{i-d}+a_i)\\
  &=T_i-a_{i-d}+b_i,
 \end{aligned}                                                    \tag{2.10}
\]

which proves (2.5) and the Johnson property.

In the owner window `T_i,...,T_(i+d)`, every member of `Q_i` is deleted,
one per transition, and is therefore absent from a later owner.  Every
newly inserted `b_i,...,b_(i+d-1)` is absent from the first owner.  A member
of `S_i` remains in the owner trace through the transition where it leaves
`S`; the queue delays its owner deletion by exactly `d` transitions.
Consequently every member of `S_i` lies in all `d+1` displayed owners, and
no member outside `S_i` does.  This proves (2.6).

Equation (2.7) is (2.6) with the index shifted.  Finally,

\[
 \bigcup_{h=0}^{d}P_{i+h}
   =\bigcup_{h=0}^{d}S_{i-d+h}
   =S_i\cup\{a_{i-d},\ldots,a_{i-1}\}=T_i,                       \tag{2.11}
\]

where the middle equality follows by reversing the `d` exchanges in
(2.1).  This is (2.8).  \(\square\)

The lift automatically gives every nonconstant positive owner run length at
least `d+1`: after a coordinate leaves the lower trace, it remains in the
queue for `d` more transitions.  A zero-gap floor is an additional separation
condition on successive lower insertions and deletions of the same coordinate;
it is not asserted by (2.3) alone.

## 3. Owner Hamiltonicity is flag injectivity

The lower trace and its event word determine the queue and therefore the
owner trace uniquely.  Since the number of rank-`r` owners is

\[
                         W={k\choose r},                            \tag{3.1}
\]

a length-`W` queue lift uses every owner exactly once if and only if

\[
                         (S_i,Q_i)\longmapsto S_i\cup Q_i           \tag{3.2}
\]

is injective on the `W` positions.

### Corollary 3.1 (exact owner criterion)

Under (2.3), a cyclic lower walk of length `W` lifts to a rank-`r` owner
Hamilton cycle precisely when

\[
                         S_i\cup Q_i\ne S_j\cup Q_j
                         \quad(i\ne j).                            \tag{3.3}
\]

No separate owner-surjectivity check is then needed.

#### Proof

Theorem 2.1 gives `W` rank-`r` owners.  They are all distinct exactly under
(3.3), and there are exactly `W` possible rank-`r` sets.  \(\square\)

## 4. A duplicate-block construction target

Let

\[
 M={k\choose r-d},qquad U=W-M.                                  \tag{4.1}
\]

The values of the maximal antecedent are exactly the shifted values of `S`
by (2.7).  Hence the canonical-lock fibre condition for a proposed free bank
`R` is simply

\[
 \forall X\in{[k]\choose r-d}\quad
       \exists i\notin R\text{ with }S_i=X.                      \tag{4.2}
\]

This suggests the following concrete strengthening of the current PBBS
fibre-hitting gate.

### Duplicate-block flag-cycle target

Construct a length-`W` cyclic lower Johnson walk `S` such that:

1. every rank-`(r-d)` vertex occurs at least once;
2. there is a set `R` of exactly `U-O(W/d)` positions, partitioned into
   intervals of length at most `d`, and every value appearing in `R` also
   appears outside `R`;
3. the queue conditions (2.3) hold; and
4. the lifted owners (3.3) are distinct.

Then `R` automatically satisfies the exact canonical-lock transversal
(4.2).  The short-gap mandatory-core theorem reduces the remaining lower
compiler to a local positive-hit atlas inside those blocks.

A particularly transparent sufficient shape is:

* one outside occurrence of every lower vertex (a Hamilton transversal of
  the value set), followed cyclically by
* `U-O(W/d)` duplicate occurrences grouped into depth-sized blocks, with
  `O(W/d)` separators.

The existence of an ordinary Hamilton cycle in `J(k,r-d)` is not enough:
conditions (2.3) and (3.3) are the exact additional delayed-colour and flag
constraints.  Conversely, those are now the only owner-layer constraints;
there is no hidden factorization condition.

## 5. Scope

This theorem closes an algebraic reduction, not the all-`k` construction.
It proves that the canonical maximal-antecedent/free-bank problem may be
attacked as one coloured Johnson flag cycle.  It does not prove:

* the duplicate-block flag-cycle target;
* the local exact-value atlas inside the resulting blocks;
* arbitrary upper support, component joining or a safe linear opening; or
* a typed external common-cap router.

Its value is the quantifier collapse: instead of choosing a rank-`r` owner
trace and then analyzing opaque depth-`d` occurrence fibres, one may choose
the rank-`(r-d)` value walk first.  Its last `d` deletion labels determine
the owner trace by the explicit FIFO formula (2.4).
