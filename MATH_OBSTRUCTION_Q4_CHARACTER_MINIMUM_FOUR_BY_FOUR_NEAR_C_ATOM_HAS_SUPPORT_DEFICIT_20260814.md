# The q=4 character-minimum four-by-four near-C atom has a support deficit

**Date:** 2026-08-14
**Status:** exact symbolic named-support obstruction with independent H100
replay.  It raises the physical q=4 lower bound from four to five rails per
shore.  It does not classify or construct the five-by-five atom.

## 0. Outcome

For `q=4`, the centre-character lower bound is four rails per shore.  No
physical four-by-four cyclic-window atom can attain it.

There are exactly two equality profiles for the net short/long centre
ledger.  One contains a target centre whose exact toggle-support imbalance
is `-5`; the other contains one whose imbalance is `-8`.  Four physical
rails on a shore give the universal bound `|t_z|<=4`, so both profiles are
impossible before cyclic orders or named-owner exact cover are considered.

Consequently every genuine distance-one near-C one-owner atom using the
two shortest q=4 periods 10 and 11 has at least five rails on each shore.
This is the first owner-semigroup lower bound directly relevant to the
`d=3` / `q=d+1=4` frontier.

## 1. Exact point equation

Let `a_z` and `b_z` be the positive-minus-negative numbers of period-10 and
period-11 rails centred at `z`.  Let `t_z` be the signed number of
noncentre rail toggle supports containing `z`.  A centre contributes its
full period, while a toggle label occurs in exactly four cyclic windows.
Thus every one-owner trade satisfies

\[
             10a_z+11b_z+4t_z=h_z,                \tag{1.1}
\]

where `h_z=1` at the five target labels and zero elsewhere.

If each physical shore has four rails, then

\[
                         |t_z|\le4.                \tag{1.2}
\]

The centre-character theorem already gives net positive and negative mass
at least four.  Physical shore size four therefore forces equality: there
is no aggregate centre/period cancellation and

\[
              \sum_z(|a_z|+|b_z|)=8,qquad
              \sum_za_z=-1,quad\sum_zb_z=1.       \tag{1.3}
\]

## 2. Every equality profile

For q=4 the sharp pointwise supporting inequality is

\[
             {3\over2}h+{1\over2}b\le |a|+|b|.    \tag{2.1}
\]

Multiplying its slack by two gives

\[
                  2|a|+2|b|-b\ge3h.              \tag{2.2}
\]

Equality in the global bound `(1.3)` forces equality at every coordinate.
At an exterior coordinate `h=0`, equality in `(2.2)` gives `(a,b)=(0,0)`.
At a target coordinate, combine equality

\[
                  2|a|+2|b|-b=3                  \tag{2.3}
\]

with the centre congruence `2a+3b=1 mod 4`.  The complete list is

\[
 (a,b,t)=(-1,1,0),\quad(1,1,-5),\quad
          (0,-1,3),\quad(0,3,-8),                 \tag{2.4}
\]

where `t` is then forced by `(1.1)`.

Let the multiplicities of the four states in `(2.4)` be `x,y,z,w` in that
order.  The five target slots and the two sum equations are

\[
 x+y+z+w=5,qquad -x+y=-1,qquad x+y-z+3w=1.      \tag{2.5}

\]

Solving gives exactly two profiles:

\[
\begin{array}{c|cccc}
 &(-1,1,0)&(1,1,-5)&(0,-1,3)&(0,3,-8)\\ \hline
 \mathrm I&2&1&2&0\\
 \mathrm {II}&1&0&3&1.
\end{array}                                       \tag{2.6}

Profile I violates `(1.2)` at its `(1,1,-5)` target.  Profile II violates
it at its `(0,3,-8)` target.  This proves the obstruction.

### Theorem 2.1

No q=4 distance-one near-C trade using periods 10 and 11 has four physical
rails on each shore.  Every such positive one-owner atom has shore size at
least five.

The conclusion permits arbitrarily many exterior labels in the ambient
ground; equality in `(2.2)` forces all of them to have zero net centre
ledger.  At physical shore size four there is no aggregate cancellation,
so no positive/negative exterior centre pair is actually present.

## 3. Correct five-rail gate

At shore size five, net centre mass may be four with one unit of aggregate
centre/period cancellation, or it may be five.  In the first case only
Profile I of `(2.6)` survives the crude support test because `|t|<=5`; the
fifth positive and negative rails lie in one common centre/period class at
the net-ledger level, though their cyclic orders need not agree.
That cancelling pair cannot be centred at the Profile-I target with
`(a,b,t)=(1,1,-5)`: doing so leaves only four negative noncentre rails at
that label, making `t=-5` impossible.  Thus every support-feasible
net-mass-four branch places the cancellation elsewhere.

Thus a proof-safe first search must:

1. include the Profile-I net ledger plus one cancelling short or long rail
   on each shore;
2. solve the exact binary support-incidence equations, in particular the
   target imbalance `t=-5`; and
3. only then impose cyclic q-window named-owner equality and simplicity.

Net-mass-five profiles are a separate branch and cannot be discarded
without their own supporting-plane classification.  No five-by-five
existence claim is made here.

## 4. H100 replay

The verifier independently enumerates every local target equality state,
all five-target global equality profiles with `(1.3)`, and the forced
support values from `(1.1)`.

```text
verifier
  scratch/verify_q4_near_c_four_by_four_support_deficit_20260814.py
  SHA256 6256e7b2107cfe5b933fd6d11c87799525a124dd4f94358bd57c43d3635eaf09

H100 output
  scratch/verify_q4_near_c_four_by_four_support_deficit_20260814.h100.out
  SHA256 7b942af8f0c344f6741674ffe1917ae527866d52f48c386c41c60c26873e6979
```

All enumeration, verification and hashing were run through SSH on H100.
The local Mac was used only to edit, transfer and operate Git.
