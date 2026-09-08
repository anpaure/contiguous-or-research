# A common resident-rail bank makes the q-gon role conversion literal

**Date:** 2026-08-01  
**Lane:** K, q-gon reset algebra / physical role conversion  
**Status:** unconditional local construction.  Four equal-size
four-resource states realize the reflected-reverse q-gon, a literal
complete-reversal role conversion, and the forward q-gon without expanding
or contracting the physical support.  Every state is depth-`d` resident
and globally q1-simple.  The two reversal pairs are all-width transparent;
the individual q-gon rethreads are not graded-all-width transparent.  The
fusion direction is nevertheless upper-support monotone: it deletes no
last internal root-interval target.  Derivative/source, exterior and common
compiler guards remain open.

## 0. Outcome

Fix `q>=3` and `d>=1`.  The construction gives four states

\[
                         H_0,H_1,H_2,H_3                       \tag{0.1}
\]

on exactly

\[
                         q(2d+2)                              \tag{0.2}
\]

atoms each, with the same complete lower, upper, tail and head resource
sets.  Their component counts are

\[
                         1\longrightarrow q\longrightarrow
                         q\longrightarrow1.                  \tag{0.3}
\]

Moreover,

\[
                         H_2=\operatorname{rev}(H_1),
 \qquad                  H_3=\operatorname{rev}(H_0).        \tag{0.4}
\]

Every nonconstant positive coordinate run in every component has length at
least `d+1`.  Thus the q-gon's abstract

\[
             R^{\rm ref}\longrightarrow
             \hbox{role conversion}\longrightarrow F         \tag{0.5}
\]

composition has a literal equal-support depth-`d` realization.  The former
closed-doubleton/expansion-contraction gate is gone.

In the fusion direction `H_2 -> H_3`, every old internal root-interval OR
value survives.  The first graded current is at width `d+3`, where one
occurrence of each saturated two-active-label value is exchanged for a new
three-active-label value.  This one-sided support theorem is stronger than
the original finite observation that the graded decks differ.

## 1. The q ports

Let `S` have rank `m-2`.  Choose distinct labels

\[
                         z,a_0,\ldots,a_{q-1}\notin S         \tag{1.1}
\]

and read `i` modulo `q`.  Put

\[
\begin{aligned}
 A_i&=S+z+a_i, &B_i&=S+a_i+a_{i+1},\\
 L_i&=S+a_i,   &U_i&=S+z+a_i+a_{i+1}.
\end{aligned}                                               \tag{1.2}
\]

Thus both `A_i B_i` and `A_(i+1) B_i` are Johnson edges, with

\[
\begin{aligned}
 A_i\cap B_i&=L_i,&A_i\cup B_i&=U_i,\\
 A_{i+1}\cap B_i&=L_{i+1},&A_{i+1}\cup B_i&=U_i.
\end{aligned}                                               \tag{1.3}
\]

The usual q-gon phases are

\[
 O=\{A_i\to B_i\},qquad N=\{A_i\to B_{i-1}\}.             \tag{1.4}
\]

Their literal reversals are

\[
 \bar O=\{B_i\to A_i\},qquad
 \bar N=\{B_{i-1}\to A_i\}.                               \tag{1.5}
\]

## 2. One common rail template at every port

Choose

\[
                         X=\{x_1,\ldots,x_d\}\subset S       \tag{2.1}
\]

and retain an anchor

\[
                         b\in S-X.                            \tag{2.2}
\]

Choose a common fresh bank

\[
 Y=\{y_1,\ldots,y_d\}
 \quad\hbox{outside }S\cup\{z,a_0,\ldots,a_{q-1}\}.         \tag{2.3}
\]

Hence a sufficient coordinate condition is

\[
                         m\ge d+3,
 \qquad                  k\ge m+q+d-1.                      \tag{2.4}
\]

For the reset value `q=2(d+1)` on a `2m`-point ground, the second condition
is `m>=3d+1`, which holds eventually because `d=Theta(sqrt(m))`.

At port `i`, use `E=A_i`, `F=B_i`, seam base `L_i`,
`delta=z`, and `alpha=a_(i+1)` in the resident long-return formulas.  Thus

\[
 P_{i,j}=(L_i-X[1,j])+Y[1,j]+a_{i+1},qquad0\le j\le d,      \tag{2.5}
\]

\[
 Q_{i,0}=(L_i-X)+Y+z,                                      \tag{2.6}
\]

\[
 Q_{i,j}=L_i-\{x_{j+1},\ldots,x_d\}
              +\{y_{j+1},\ldots,y_d\}+z,
 \qquad1\le j\le d.                                      \tag{2.7}
\]

Then

\[
 P_{i,0}=B_i,qquad Q_{i,d}=A_i.                            \tag{2.8}
\]

Let `P_i+` be the directed rail

\[
 B_i=P_{i,0},P_{i,1},\ldots,P_{i,d},Q_{i,0},\ldots,Q_{i,d}=A_i,
\tag{2.9}
\]

and let `P_i-` be its complete reversal from `A_i` to `B_i`.

## 3. Global q1 simplicity across all ports

### Theorem 3.1 (resource-disjoint common-template rails)

The union of all `q` rail interiors and one q-gon phase is a
four-resource matching.  Its root, lower and upper resources are pairwise
distinct across different ports, and every rail resource is distinct from
every direct q-gon resource.

#### Proof

An internal `P_(i,j)` contains the prefix `Y[1,j]` and the active adjacent
pair `{a_i,a_(i+1)}`; an internal `Q_(i,j)` contains `z`, the suffix
`Y[j+1,d]`, and `a_i`.  The `Y` profile first determines `j`, and the active
profile then determines `i`.  It also separates the `P` and `Q` families.
Every internal rail root contains a fresh `y`, while no q-gon root does.

The first-half lower colours are

\[
 S-X[1,j]+Y[1,j-1]+a_i+a_{i+1},                             \tag{3.1}
\]

the central lower colour is

\[
 S-X+Y+a_i,                                                 \tag{3.2}
\]

and the second-half lower colours contain `z` and the corresponding suffix
profile.  These patterns separate ports and families.  The only rail lower
colours without a `y` are the first and last ones; each omits `x_1` or
`x_d`, whereas every direct lower colour `L_i=S+a_i` contains all of `X`.

Every rail upper colour contains a fresh `y`, whereas every direct upper
colour `U_i` contains none.  Prefix/suffix and active-coordinate patterns
again separate the rail upper colours across ports.  This proves all typed
resource claims. \(\square\)

## 4. The four equal-size states

Put

\[
\begin{aligned}
 H_0&=\bar N\ \cup\ \bigcup_i P_i^-,\\
 H_1&=\bar O\ \cup\ \bigcup_i P_i^-,\\
 H_2&=O\ \cup\ \bigcup_i P_i^+,\\
 H_3&=N\ \cup\ \bigcup_i P_i^+.
\end{aligned}                                               \tag{4.1}
\]

In expanded form, the direct atoms are

\[
\begin{array}{c|c}
H_0&B_{i-1}\to A_i\\
H_1&B_i\to A_i\\
H_2&A_i\to B_i\\
H_3&A_i\to B_{i-1}.
\end{array}                                                 \tag{4.2}
\]

### Theorem 4.1 (literal constant-support serial history)

All four states in (4.1) are four-resource matchings with identical
complete typed signatures and exactly `q(2d+2)` atoms.  Their component
counts are (0.3), and the reversal identities (0.4) hold atom by atom.

#### Proof

The q-gon phases use the same direct four-resource palettes.  Rail reversal
does not change any rail palette, and Theorem 3.1 makes the direct and rail
palettes disjoint.  Hence every state has the same signature and size.

In `H_0`, the edge `B_(i-1)->A_i` is followed by the reversed rail
`A_i leadsto B_i`, so the port index advances by one.  All `q` ports form
one cycle.  In `H_1`, `B_i->A_i` closes the reversed rail at the same port,
giving `q` cycles.  `H_2` is the complete reversal of `H_1`, hence also has
`q` cycles.  Finally `H_3` is the complete reversal of `H_0`, hence has one
cycle.  The direct and rail formulas prove the two reversal identities
atomwise. \(\square\)

Thus the three moves

\[
 H_0\xrightarrow{\ R^{\rm ref}\ }H_1
 \xrightarrow{\ \text{complete cycle reversal}\ }H_2
 \xrightarrow{\ F\ }H_3                                  \tag{4.3}
\]

never expand or contract the physical position set.  The middle move is
the missing literal role conversion between reversed and forward typed
ports.

## 5. Residence in all four states

### Theorem 5.1 (componentwise depth-`d` residence)

Every nonconstant positive run in every component of every `H_j` has length
at least `d+1`.

On the `q` small cycles `H_1,H_2`, the resident-return theorem gives exact
`d+1` runs for `x_j,y_j,z,a_(i+1)`; `a_i` and `S-X` are constant on their
port cycle.

On the large cycles `H_0,H_3`:

* every `y_j` has one internal run of length `d+1` per port;
* the two boundary pieces of `x_j` on consecutive reversed rails join to a
  run of length exactly `d+1`;
* `z` has one run of length `d+1` at the `A_i` end of every rail;
* each active `a_i` has one run of length `3d+3`, consisting of the
  `a_i` end-run in port `i-1` followed by the entire port-`i` rail;
* `S-X` is constant one and all unused coordinates are constant zero.

#### Proof

The small-cycle statement is the exact trace calculation for the resident
long rail.  In a reversed rail, the `x_j` trace has a positive initial
piece of length `d-j+1` at `A_i` and a positive terminal piece of length
`j` at `B_i`.  The cross edge `B_(i-1)->A_i` joins a terminal piece to the
next initial piece, giving `d+1`.  The `y_j` trace is the unchanged internal
complementary block.  The `z` trace is the `Q` half adjacent to `A_i`.

Coordinate `a_i` is the terminal `alpha` run on port `i-1`, of length
`d+1`, and is permanent through all `2d+2` vertices of port `i`; the next
cross edge leaves it.  Its total is `3d+3`.  The remaining assertions are
immediate from (2.5)--(2.7).  Reversal transfers the calculation between
`H_0,H_3` and between `H_1,H_2`. \(\square\)

The anchor `b` lies in every root, so every component has a nonempty maximal
depth-`d` antecedent.

## 6. Exact all-width statements—and the remaining upper gate

### Theorem 6.1 (endpoint and middle reversal transparency)

The pair `H_0,H_3` consists of one cycle and its reversal.  The pair
`H_1,H_2` consists of the same `q` small cycles reversed componentwise.
Therefore each pair has identical complete componentwise cyclic
interval-union spectra at every width.  Their maximal depth-`d` antecedents
also reverse, so every derivative-row inventory and every internal
target--cell incidence transports within each pair.

This theorem applies to the **compound endpoint trade** `H_0<->H_3` and the
middle role-conversion trade `H_1<->H_2`.  It does not say that the
individual q-gon rethreads `H_0<->H_1` or `H_2<->H_3` preserve deeper OR
decks.  They generally do not.

The independent replay below found a deeper internal OR difference between
`H_0` and `H_1` in every one of its 30 parameter cases, while width two
agrees exactly by Theorem 3.1.  Thus (4.3) is a literal constant-support
history in the four-resource/residence fibre, but it is not yet a path in
the all-width-safe chronology graph unless the endpoint rethreads are
treated as one protected compound macro or their deeper casualties have
external witnesses.

### Theorem 6.2 (first q-gon OR current)

Let `D_w(H)` denote the multiset of unions of `w` consecutive roots,
summed over all cycle components of `H`.  Then

\[
                  D_w(H_2)=D_w(H_3)\qquad(1\le w\le d+2), \tag{6.1}
\]

and the first nonzero current occurs at width `d+3`.  Put

\[
 C_i=S\cup Y\cup\{z,a_i,a_{i+1}\},\qquad
 D_i=S\cup Y\cup\{z,a_{i-1},a_i,a_{i+1}\}.          \tag{6.2}
\]

Then, as a signed multiset,

\[
 D_{d+3}(H_3)-D_{d+3}(H_2)
       =\sum_{i\in\mathbb Z_q}(e_{D_i}-e_{C_i}).     \tag{6.3}
\]

The two ranks in (6.2) are respectively `m+d+1` and `m+d+2`.
For `q>=4` the `D_i` are pairwise distinct and have one occurrence each
in `D_(d+3)(H_3)`; for `q=3` they are one common value of multiplicity
three in that width.  No
`D_i` occurs anywhere in `H_2`, at any width.  Every `C_i` still occurs in
`H_3`, so the negative part of (6.3) removes one occurrence rather than the
last witness of `C_i`.

#### Proof

In `H_2`, port `i` has the cyclic order

\[
 A_i,B_i=P_{i,0},P_{i,1},\ldots,P_{i,d},
 Q_{i,0},\ldots,Q_{i,d-1}.                           \tag{6.4}
\]

In `H_3`, the only change is that the direct edge leaving `A_i` enters
`B_(i-1)` and then follows the rail of port `i-1`.

A window not crossing a direct edge is common to both histories.  Consider
a window crossing `A_i -> B_(i-1)` in `H_3`, with `r` vertices on the
incoming side and `s` on the outgoing side.  If `r+s<=d+2`, its incoming
part is a suffix of the `Q_i` half and its outgoing part is a prefix of the
`P_(i-1)` half.  Its `X,Y` profile depends only on `(r,s)`, and its active
label union is

\[
                         \{z,a_{i-1},a_i\}.
\]

This is exactly the corresponding crossing window at port `i-1` of
`H_2`.  Such a short window cannot meet two direct edges, proving (6.1).

At width `d+3`, all crossing types except one obey the same port shift.
The exceptional type contains the `d+2` vertices ending at `A_i` and the
one direct successor.  Its two versions are

\[
 (P_{i,d},Q_{i,0},\ldots,Q_{i,d}=A_i,B_i)\quad\hbox{in }H_2,
\]

and

\[
 (P_{i,d},Q_{i,0},\ldots,Q_{i,d}=A_i,B_{i-1})\quad\hbox{in }H_3.
                                                                  \tag{6.5}
\]

The unions in (6.5) are `C_i` and `D_i`.  The opposite extreme crossing
type, with one incoming vertex and `d+2` outgoing vertices, supplies the
same `C_i` family in both histories after shifting the port index.  This
proves the complete current (6.3).

Every component of `H_2` is contained in

\[
                         S\cup Y\cup\{z,a_j,a_{j+1}\}
\]

for one `j`, so it cannot contain a `D_i`.  Distinctness and the stated
multiplicities follow from the cyclic triples of distinct `a` labels.
\(\square\)

Since `H_0=rev(H_3)` and `H_1=rev(H_2)`, Theorem 6.2 also gives

\[
 D_w(H_0)=D_w(H_3),\qquad D_w(H_1)=D_w(H_2)          \tag{6.6}
\]

at every width.  Thus `H_0 -> H_1` has the negative of the current in
(6.3), `H_1 -> H_2` has zero current, and `H_2 -> H_3` has (6.3).  The two
individual topology changes cancel only in the complete endpoint trade.

### Corollary 6.3 (the fusion direction is upper-support monotone)

Let `Deck(H)` be the **set** (not the graded multiset) of unions of
nonempty cyclic root intervals, taken over all components of `H`.  Then

\[
                              Deck(H_2)\subseteq Deck(H_3). \tag{6.7}
\]

Thus the topology-changing direction `H_2 -> H_3`, which fuses the `q`
port cycles into one, deletes no last internal root-interval witness.  It
may change the width and multiplicity of a witness, and it creates the new
`D_i` targets in (6.2).

#### Proof

For widths at most `d+2`, Theorem 6.2 gives equality even as multisets.
On one `H_2` port cycle, any interval of width at least `d+2` has union

\[
                         C_i=S\cup Y\cup\{z,a_i,a_{i+1}\}. \tag{6.8}
\]

Indeed the port is the length-`2d+2` wreath of the resident-return theorem,
and `d+2` consecutive roots already contain its complete active support.
The value `C_i` occurs in `H_3` by Theorem 6.2 (explicitly, the opposite
extreme crossing window in its proof).  Hence every longer `H_2` value has
an `H_3` witness, proving (6.7). \(\square\)

This is a target-support statement, not full all-depth transparency.
The graded current (6.3) is nonzero, and maximal-antecedent/derivative
occurrences and a fixed compiler matching are not identified by (6.7).
In the reverse split `H_0 -> H_1`, the `D_i` values are genuine target
casualties because no `H_1` component can contain three consecutive active
`a` labels.

### Corollary 6.4 (reversal-quotient fusion)

By
`MATH_THEOREM_GLOBAL_REVERSAL_QUOTIENT_INDUCTION_AND_RELATIVE_PHASE_OBSTRUCTION_20260801.md`,
an existential induction state may be quotiented by simultaneous reversal
of the complete source word, exterior, witnesses and compiler.  In that
quotient,

\[
                         [H_0]=[H_3],\qquad [H_1]=[H_2].    \tag{6.9}
\]

Hence the middle role-conversion step is gauge.  Choose `H_2` as the
representative of the `q`-component orbit and apply the topology-changing
fusion directly to `H_3`, obtaining the one-component orbit:

\[
                         [H_1]=[H_2]\longrightarrow
                         [H_3]=[H_0].                       \tag{6.10}
\]

One terminal compiler for `H_3` suffices; its global reflection certifies
`H_0`.  No fixed-address intersection of the two phase compiler graphs is
required.  This quotient does not remove relative phase bits between
several components, the nonzero graded current (6.3), lower
derivative/source obligations, component parity, or eventual cut debt.

## 7. Exact remaining scope

The construction removes two earlier gates:

1. no opposite intermediate edge pair is selected simultaneously, so the
   q-gon closed-doubleton obstruction is gone;
2. all four stages use exactly the same `q(2d+2)` physical roots, so no
   expansion/contraction credit is needed.

It also supplies q1 simplicity, residence, and all-width reversal at the
compound endpoints.  It does **not** yet supply:

* an embedding of the `O(qd)` roots into a spanning coefficient-one owner
  factor;
* derivative/source-cell witnesses and a common compiler across either
  individual q-gon rethread (the fusion direction itself is internally
  upper-support monotone by Corollary 6.3);
* phase-common cross-rail/cross-packet interval unions after opening;
* one terminal compiler for the chosen oriented child (a common-cap
  intersection is needed only for a named local switch against a frozen
  exterior);
* a bounded-state regenerative Pascal lift;
* a `k=17`, all-`k`, or additive-constant upper bound.

For the reset choice `q=2(d+1)`, the packet uses `4(d+1)^2=O(d^2)=O(k)`
roots.  Its scalar size is compatible with an additive-constant programme,
but the protected global host remains the decisive theorem.

## 8. Independent H100 `-O3` replay

`scratch/audit_qport_resident_rail_role_converter_20260801.cpp` constructs
all four literal states for

\[
                         1\le d\le5,qquad3\le q\le8.
\]

It verifies every typed resource, global q1 simplicity, component counts,
both reversal identities, every coordinate run, nonempty maximal
factorization, and every-width OR equality for both reversal pairs.  It
also checks the deeper-OR inequality across the q-gon rethread.

The H100 command was

```text
g++ -std=c++20 -O3 -Wall -Wextra -pedantic \
  scratch/audit_qport_resident_rail_role_converter_20260801.cpp \
  -o /dev/shm/audit_qport_resident_rail_role_converter_20260801
/dev/shm/audit_qport_resident_rail_role_converter_20260801
```

The frozen verdict is

```text
PASS_QPORT_RESIDENT_RAIL_ROLE_CONVERTER cases=30 d=1..5 q=3..8
signatures=exact q1=globally_simple topology=1_to_q_to_q_to_1
constant_atoms=q(2d+2) residence>=d+1
endpoint_and_middle=complete_reversals OR=all_widths factor=PASS
endpoint_deeper_OR_differences=30/30
```
