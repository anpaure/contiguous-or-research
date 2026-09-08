# Clean-C6 inverse-fan currents telescope on serial paired histories, not on an arbitrary connector tree

**Date:** 2026-08-05  
**Method:** occurrence-deck coboundary calculus; no computation or search  
**Status:** unconditional.  The q3 flag defect is a discrete gradient and
all-depth fan currents telescope when complete paired history states are
literally chained.  A left-profile match alone is insufficient, and a
branching connector tree leaves unpaired divergence states.

## 1. Complete triangular history state

At a changed q1 occurrence, let

\[
 \mathcal L=(L(0),L(1),\ldots),
 \qquad
 \mathcal R=(R(0),R(1),\ldots)                    \tag{1.1}
\]

be its central-truncated left and right prefix-intersection histories.  Thus
`L(0)=R(0)` is the central q1 row, and the target of the owner path with
`u` edges before and `v` edges after is

\[
                         T(u,v)=L(u)\cap R(v).     \tag{1.2}
\]

For any declared affected index set `Omega`, define the occurrence-labelled
triangular state

\[
 \mathscr D_\Omega(\mathcal L,\mathcal R)
   =\sum_{(u,v)\in\Omega}
       [\,u,v,L(u)\cap R(v)\,].                    \tag{1.3}
\]

The depth and occurrence labels in (1.3) are retained.  Equality of target
sets without these labels is a weaker statement.

## 2. One packet is a coboundary

For a clean C6, let `i in Z_3` index the three central rows.  Before the
switch, the state is

\[
 D^-=sum_i\mathscr D_\Omega(\mathcal L_i,\mathcal R_i),
 \tag{2.1}
\]

while the diagonal-to-shifted coupling law gives

\[
 D^+=\sum_i\mathscr D_\Omega(\mathcal L_{i-1\to i},\mathcal R_i).
 \tag{2.2}
\]

Here `L_(i-1->i)` means that the left exterior formerly ending at
`P_(i-1)` is truncated by the new central row `R_i`; it is not merely the
unmodified set sequence `L_(i-1)`.

The signed inverse-fan current is therefore

\[
                         \partial P=D^+-D^-.       \tag{2.3}
\]

At q3 with common first deletion `d` and second left flags `e_i`, its
left-only row is

\[
 \partial_3P
  =\sum_i
   \left([K-\{d,e_{i-1}\}+a_i]
        -[K-\{d,e_i\}+a_i]\right).                 \tag{2.4}
\]

Thus the q3 defect is literally the discrete gradient of the flag
assignment around the active-label triangle.

## 3. Serial telescoping

### Theorem 3.1 (complete-state coboundary theorem)

Let `P_1,...,P_t` be a serial sequence of clean-C6 packets.  Suppose that
for every `j<t` there is an occurrence-preserving identification

\[
                         D_j^+=D_{j+1}^-             \tag{3.1}
\]

of their complete states (1.3), including core, active labels, left and
right histories, depths, and physical occurrence addresses.  Then

\[
             \sum_{j=1}^{t}\partial P_j=D_t^+-D_1^-.       \tag{3.2}
\]

If the state chain closes, `D_t^+=D_1^-`, the total all-depth inverse-fan
current is zero.

#### Proof

Substitute `partial P_j=D_j^+-D_j^-` and cancel each adjacent pair using
(3.1). `square`

For q3 alone, (3.1) reduces to literal identification of the receiving
flag-decorated targets in (2.4).  Three repeated rotations on one
set-identical state return the flag assignment and have zero formal q3
current.  Physical owner simplicity and topology are additional questions.

## 4. Why matching only the left flag is insufficient

### Proposition 4.1 (right-history obstruction)

Suppose two consecutive packets identify every left history but have
different right histories at some depth `v`.  Then their currents need not
cancel, even if all q3 flags agree.

#### Proof

Choose the first `v` and some `u` for which

\[
 L(u)\cap R_{old}(v)\ne L(u)\cap R_{new}(v).       \tag{4.1}
\]

The corresponding occurrence-labelled term of (1.3) appears with opposite
formal signs but different target values, so it does not cancel. `square`

Hence the phrase “the new left profile of one is the old left profile of
the next” is sufficient only on the left-only face `v=0`.  The complete
whole-fan bank requires the paired state `(L,R)`.

## 5. Branching is divergence, not telescoping

At a physical connector vertex, regard every incident packet state as an
incoming or outgoing half-edge labelled by its complete deck `D`.  Literal
cancellation pairs one incoming with one identical outgoing state.

### Theorem 5.1 (branching residual)

If a connector vertex has `p` incoming and `q` outgoing state half-edges,
then after all possible pairwise cancellations at least

\[
                         |p-q|                     \tag{5.1}
\]

state copies remain; with occurrence capacity one, at least

\[
                         p+q-2\min(p,q)=|p-q|       \tag{5.2}
\]

is exact, and additional residuals remain whenever the paired state labels
differ.

Thus the abstract fact that packet supports form a tree does not imply
telescoping.  A tree orientation with branching generally has nonzero
state divergence.  Zero internal current requires an Eulerian state
routing (or explicit duplicating capacity), not merely graphic acyclicity.

#### Proof

Every cancellation consumes one incoming and one outgoing occurrence.
At most `min(p,q)` pairs can be removed.  State-label incompatibility can
only reduce that number. `square`

## 6. Endpoint size

Even on a perfect open serial chain, (3.2) leaves the two endpoint states.
For one punctured edge the complete affected index set has size at most

\[
                         |\Omega|\le\binom{m+1}{2}.          \tag{6.1}
\]

Therefore “only two endpoint states remain” does not by itself mean only
`O(1)` missing targets.  It is an `O(1)` **number of structured triangular
states**, each potentially containing `Theta(m^2)` occurrence tasks.

An additive theorem needs one further statement: the endpoint state is
zero, is already represented by an independent protected bank, or is
compressible by a bounded literal repair.

## 7. Consequence

The serial-coboundary idea is correct and useful, but its exact hypothesis
is complete paired-history regeneration.  The remaining proof target is
not a scalar packet tree.  It is a state-routed connector construction in
which:

1. internal packet outputs equal later inputs occurrencewise;
2. branching has balanced typed capacity; and
3. the final endpoint triangular states vanish or have bounded complete
   damage.

No all-k upper bound is claimed here.

