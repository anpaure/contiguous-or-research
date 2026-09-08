# The odd beta copy is a collar compensator: a monotone terminal accumulator

**Date:** 2026-08-06  
**Method:** one monotone right-to-left sweep, exact signed mass, and a
parity-aware seven-state copy-before-erase register; no computation or search  
**Status:** proof-safe terminal-accumulator theorem.  It removes the obsolete
premise that the copy written by beta must be routed to an opposite source
occurrence.  Its input is the already constructed fully tagged checkpoint:
the ordinary tape is over the guardable alphabet and its only exceptional
blocks are at most three occurrence-labelled midpoints.  Under that exact
input, no residual non-guardable crossing remains.

## 1. Data at the beta checkpoint

Use the block alphabet

\[
 A=00,\quad B=20,\quad C=22,\quad M=11,\quad H=02,
 \qquad \mathcal G=\{20,01,21\}.
\tag{1.1}
\]

For a ternary digit put

\[
 C(x)\in\{A,B,C\},\qquad \epsilon(x)=x-1.
\tag{1.2}
\]

Let the first digit be \(a_1\), let the ordered fixed collar be
\(C(a)|C(b)\), and set

\[
 e=\epsilon(a_1),\qquad
 c=\epsilon(a)+\epsilon(b),\qquad
 q=e+c,\qquad t=|q|.
\tag{1.3}
\]

The balanced-midpoint construction leaves exactly \(t\le3\) exceptional
blocks, all equal to \(M\), in occurrence-labelled physical positions.  All
other blocks between the fixed collar berth and the first selected pair lie
in \(\mathcal G\).  The setup transcript and the deterministic
noncrossing/LIFO rule recover those positions.

Transport the double head \(H|H\) from the berth to the first connector by
the proved double-head theorem.  It crosses both \(\mathcal G\) and \(M\)
literally and restores every crossed block.  Apply the connector-lattice beta
path.  Its endpoint is

\[
                 C^*(a_1)\mid K_0,
                 \qquad K_0=C(a_1)\mid H,
\tag{1.4}
\]

where the first displayed block is the now-final first connector and the
two-block word \(K_0\) lies immediately on the tape side of it.  The latter is
not a target occurrence.  It is the active collar compensator.

If \(q=0\), there is no midpoint and the sweep below contains only ordinary
guardable blocks.

## 2. Exact mass ledger

Assume first \(q\ne0\), and write

\[
                         \sigma=\operatorname {sign}(q).
\tag{2.1}
\]

Every residual source midpoint must become the same target extreme

\[
                         R_\sigma=C(1+\sigma)
                  =\begin{cases}C,&\sigma=1,\\ A,&\sigma=-1.
                    \end{cases}
\tag{2.2}
\]

The mass of a block is the sum of its two digits.  Hence

\[
 \operatorname {mass}(M)=2,qquad
 \operatorname {mass}(R_\sigma)=2+2\sigma,qquad
 \operatorname {mass}(K_0)=4+2e.
\tag{2.3}
\]

After \(j\) midpoint conversions define the required compensator mass by

\[
                         m_j=4+2e-2j\sigma.
\tag{2.4}
\]

At the last conversion,

\[
 \boxed{
 m_t=4+2e-2q=4-2c
      =\operatorname {mass}\bigl(C^*(a)|C^*(b)\bigr).}
\tag{2.5}
\]

Both endpoints in (2.4) lie in \([0,8]\), and the sequence is monotone.
Therefore every \(m_j\) lies in \(\{0,2,4,6,8\}\); an extreme value zero or
eight can occur only at the final index.

For every nonfinal index use the literal representative

\[
 K_j=C(z_j)|H,
 \qquad z_j=a_1-j\sigma,
 \qquad \operatorname {mass}(K_j)=2+2z_j=m_j.
\tag{2.6}
\]

At the final index retain (2.6) when \(0\le z_t\le2\).  If \(z_t=-1\), put
\(K_t=A|A\); if \(z_t=3\), put \(K_t=C|C\).

### Lemma 2.1 (the six local accumulator types)

At a residual occurrence there is a fixed-mass literal path

\[
                         M|K_j\leadsto K_{j+1}|R_\sigma.
\tag{2.7}
\]

The complete endpoint table, before deleting impossible rows for a given
source, is

```
sigma=+1:
  M | A|H  ->  A|A | C
  M | B|H  ->  A|H | C
  M | C|H  ->  B|H | C

sigma=-1:
  M | A|H  ->  B|H | A
  M | B|H  ->  C|H | A
  M | C|H  ->  C|C | A.
```

The three total masses are respectively four, six, and eight.  They are all
nonextreme in the six-coordinate capacity-two path.

#### Proof

For every row,

\[
 \operatorname {mass}(M)+m_j
   =m_{j+1}+\operatorname {mass}(R_\sigma)
\]

by (2.4).  Thus the two endpoints lie in one fixed nonextreme mass layer of
the capacity-two token graph on six consecutive coordinates.  That graph is
connected: repeatedly move one unit from the leftmost prefix excess to the
first later prefix deficit (or perform the reflected move).  The sum of
absolute prefix discrepancies strictly decreases.  Removing loops gives a
simple literal path.  This supplies all six rows.  \(\square\)

This table is the only bounded non-\(\mathcal G\) table in the terminal
sweep.  A residual midpoint is consumed when first encountered; the active
compensator never crosses it.

## 3. The monotone sweep

Starting at the first-connector end, move \(K_0\) monotonically toward the
fixed collar berth.  Process the tape from right to left.

* On a maximal segment over \(\mathcal G\), use the stationary-corridor
  shuttle, leaving the injective marks
  \[
      \mu(20)=11,\qquad\mu(01)=10,\qquad\mu(21)=12
  \]
  on the already crossed side.  Do not erase them yet.
* On meeting the next \(M\), apply the appropriate row of Lemma 2.1.  The
  target \(R_\sigma\) stays on the already processed side, while
  \(K_{j+1}\) continues toward the berth.
* Repeat until all \(t\) midpoints have been consumed.

Thus the residuals are processed in decreasing physical address.  A
completed target is always strictly behind the moving compensator and is
never crossed later.  No address code, payload, or anonymous reservoir is
needed.

When the compensator reaches the berth, (2.5) puts it in the same
four-coordinate mass layer as the required ordered target collar.  If that
mass is zero or eight the layer has one state and \(K_t\) is already the
target.  Otherwise choose a simple fixed-mass path at the named berth

\[
                         K_t\leadsto C^*(a)|C^*(b).
\tag{3.1}
\]

Finally erase every stationary mark by the one-edge inverse of \(\mu\).
The written targets \(A\) or \(C\) do not belong to the mark alphabet, so
they split the marked suffix into unambiguous segments.

### Lemma 3.1 (occurrence decoder)

At every macro checkpoint and strict local state of the sweep, the literal
word and the fixed collar-order record recover the source, the active
address, the number \(j\) of completed residuals, and the local microstep.

#### Proof

At a checkpoint, the processed suffix consists only of stationary marks and
the already written common target \(R_\sigma\).  The unprocessed prefix is
over \(\mathcal G\cup\{M\}\).  Between them lies the active two-block word
\(K_j\).  For \(j<t\), (2.6) contains the literal head \(H=02\); an extreme
headless compensator can occur only after the last \(M\) has been consumed.

The number of target blocks in the processed suffix is \(j\).  The fixed
signed count gives \(\sigma,t\), so (2.6) recovers the active compensator and
the next operation.  Applying \(\mu^{-1}\) to the marked blocks and replacing
the first \(j\) residual addresses by their recorded source value \(M\)
recovers the beta-checkpoint tape.  The stored setup transcript then recovers
the literal original source.

Inside a guardable segment, the stationary-corridor theorem gives the same
decoder.  A segment of length one is bounded by two named objects among a
residual \(M\), a written target, the first-connector endpoint, and the fixed
berth, so the standard fixed-two-end one-interior decoder applies.  At a
six-coordinate accumulator path, the processed suffix boundary and the
fixed order record locate the support; its total mass and \((\sigma,z_j)\)
select one row of the table, and simplicity selects the microstep.  At the
final berth path, the physical berth and the order record play the same
role.

Hence equality of two current states forces equality of source, stage,
active address, and microstep.  \(\square\)

### Theorem 3.2 (monotone terminal accumulator)

From the connector-lattice beta endpoint, the sweep gives a directed,
occurrence-labelled path which simultaneously

1. sends every one of the \(t\le3\) residual midpoint occurrences to its
   required common target extreme;
2. converts the returned copy \(C(a_1)\) and the retained head into the exact
   ordered collar \(C^*(a)|C^*(b)\);
3. restores every ordinary tape block at its physical address; and
4. never asks for an opposite occurrence carrying \(C^*(C(a_1))\).

#### Proof

Lemma 2.1 supplies every residual conversion and (2.5) supplies exact final
collar mass.  The stationary-corridor theorem supplies every guardable
segment, including a headless final compensator: after the last residual its
return segment contains no further exceptional block.  Lemma 3.1 proves
occurrence labelling and pairwise source-disjointness.  Equation (3.1) and
the one-edge mark erasures give the literal target.  \(\square\)

## 4. A seven-state parity-aware collar-order register

The beta-only phase may use all seven mass-three states of the protected
root/boundary triple.  The fixed double head or returned compensator together
with the fully tagged tape separates this phase from the old linkage even at
the two states whose root/boundary coordinates alone would not do so.

Relative to the base state \(Q_0=021\), split the seven states by path parity:

\[
 \mathcal Q_0=\{021,201,120,102\},\qquad
 \mathcal Q_1=\{012,210,111\}.
\tag{4.1}
\]

Explicit base paths are

```
even:
  021
  021 -> 111 -> 201
  021 -> 111 -> 120
  021 -> 012 -> 102

odd:
  021 -> 012
  021 -> 111 -> 201 -> 210
  021 -> 111.
```

Every arrow is one adjacent unit transfer and all states have mass three.
Each parity class contains at least three states.

For fixed \(s=a+b\), order the at most three possible pairs \((a,b)\) as in
the usual fibres

```
s=0: (0,0)
s=1: (0,1),(1,0)
s=2: (0,2),(1,1),(2,0)
s=3: (1,2),(2,1)
s=4: (2,2).
```

Let \(P\) be the physical-edge parity of the deterministic setup transcript
from the literal source collar to the beta checkpoint, excluding the
register-writing path.  Inject the ordered-pair classes into
\(\mathcal Q_P\).  This simultaneously records collar order and chooses a
register route of parity \(P\).

### Lemma 4.1 (the same parity is paid on teardown)

The monotone accumulator and collar retirement have the same physical-edge
parity \(P\) as the setup transcript.

#### Proof

Use the standard bipartite potential

\[
                  \Phi(x_1\ldots x_N)=\sum_i i x_i\pmod2.
\]

On either orientation of a fixed two-coordinate block, a midpoint
\(M=11\) has odd potential while each extreme \(A=00,C=22\) has even
potential.  Thus changing a source extreme to its setup midpoint and
changing that midpoint to its target extreme are both odd.  Every collar
code and every head has two even digits, so the source-collar-to-head and
head-to-target-collar endpoint differences are both even.  The setup and
teardown shuttles traverse the same block distances in opposite directions,
hence have equal parity; every temporary stationary mark is written and
later erased.  Ordinary tagged blocks are unchanged between the two
checkpoints, so their absolute coordinate orientation is irrelevant.
Summing over the deterministic LIFO transcript proves equality of the two
parities.
\(\square\)

### Theorem 4.2 (order, beta entry, and literal target endpoint)

Write the selected state of \(\mathcal Q_P\) while the source collar is still
literal, hold it fixed through beta and the monotone accumulator, and erase
it only after the exact target collar in (3.1) is literal.  Then

* setup plus register writing has parity \(P+P=0\), so the connector-lattice
  beta path is entered at its required literal source endpoint;
* teardown plus register erasure has parity \(P+P=0\), so the literal target
  endpoint produced by beta is retained; and
* at every intermediate checkpoint, \((s,Q)\) recovers the ordered source
  collar, while the literal target collar labels the record-erasure phase.

No extra parity mark or spare protected coordinate is used.

#### Proof

The parity statements follow from Lemma 4.1 and (4.1).  Injectivity follows
because each fixed-\(s\) fibre has size at most three and each parity class
has at least three states.  During record writing the literal source collar
labels the path.  During beta and accumulation, \((s,Q)\) labels it.  During
erasure the literal ordered target collar labels it.  This is exactly the
copy-before-erase decoder.  \(\square\)

## 5. Consequence and audit boundary

The theorem closes the previously stated odd terminal interfaces:

* the beta copy is not assigned to an opposite occurrence;
* all \(0,1,2,3\) residual cases use one formula;
* residual occurrences are consumed monotonically and are never crossed;
* the only local exceptional table is the six-row table in Lemma 2.1;
* the final collar is ordered, not merely mass-correct; and
* collar order and both endpoint parities use the existing three-coordinate
  register.

The theorem does not construct the earlier fully tagged checkpoint.  It
uses, as proved inputs, the balanced-midpoint setup, its occurrence-labelled
LIFO transcript, the fixed double-head berth and transport, and the exact
connector-lattice beta path.  Subject to those already separated inputs, the
terminal odd accumulator itself has no remaining reservoir, occurrence,
non-\(\mathcal G\), or parity premise.
