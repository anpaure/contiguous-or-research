# The D5 suffix bank has a static four-clock residence dilation, but no literal successor-tag lift; its exact escape is a three-state reset switchbox

**Date:** 2026-08-14  
**Status:** unconditional finite theorem for the frozen D5 selection at commit
`e02b573`, plus an exact conditional reset reduction.  The four-clock
construction below is a resident recoding of the final output cycle, not a
dynamic lift of the 41 switches.  No three-state reset switchbox is constructed
here.

## 0. Outcome

Let `F-` be the complete lower-owner projection of the post-`T2` factor on
the components touched by the frozen 41-circuit D5 bank, and let `F+` be the
projection after all 41 circuits are toggled.  The frozen selection has SHA-256

```text
94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32.
```

It changes 477 lower incidences and sends 372 touched components to one
12,420-owner component.

The residence boundary is now exact.

1. Most final collar failures are new seams, not inherited defects: 208 of
   244 upper collision events and 165 of 240 lower collision events are new.
2. The final 12,420-owner cycle has a literal depth-two, four-coordinate
   dilation to a simple 37,260-owner cycle.  Its lower positive/zero run minima
   are `(3,3)` and its immediate-upper minima are `(4,2)`.
3. This static dilation cannot be transported backward by its two-history
   clock: all 372 old components have odd length.  The sharper phase-orientation
   system already has a two-equation contradiction inside one selected
   circuit.
4. The more general variable-successor-tag clock is also impossible for this
   selected bank, for every finite tag alphabet and both orientations of the
   final cycle.  Solver-free quotient cores certify the obstruction.
5. The undirected union `G=F- union F+` is exactly 3-chromatic.  On the 477
   selected rows, 265 old/new heads have the same state and 212 require a swap
   between the other two states.  Thus a dynamic escape needs only three
   unoriented reset-cell types, one for each tail state.  Constructing a
   resource-invariant resident reset cell is the sharp remaining gate.

The thirteen-port native MSW common-history theorem does not close this finite
gate: at depth two its numerical hypothesis would require `n>=39`, whereas the
present lifted ground set has size 23, and its direct highest-valley packet
hypothesis is not satisfied by these cross-suffix circuits.

## 1. Inherited defects versus new seams

The provenance replay compares collision events before and after the complete
toggle.  A post-toggle bad two-transition window is **inherited** when it is a
literal old event, **one-seam** when it meets one changed transition, and
**two-seam** when it meets two.

| projected shore | old bad events | new-state bad events | retained inherited | one seam | two seams | genuinely new | old events resolved |
|---|---:|---:|---:|---:|---:|---:|---:|
| immediate upper | 84 | 244 | 36 | 203 | 5 | 208 | 48 |
| lower owner | 126 | 240 | 75 | 164 | 1 | 165 | 51 |

The upper collisions all have singleton value zero; the lower collisions all
have singleton value one.  The marked-seam counts are 181 upper labels and 151
lower labels, with event multiplicities 213 and 166.  Both minimum marked seam
gaps are one.

The changed lower owners are all distinct.  The external lower roles use 474
owners: 471 occur twice and three occur four times.  The untouched upper mates
use 458 owners, with multiplicity at most two.  Thus any reset construction may
be private on the 477 tails, but must coalesce three exceptional external ports
or give them occurrence-distinct tickets.

## 2. Static four-clock dilation

Write the unique final owner trace as

\[
                 T_0,T_1,\ldots,T_{L-1},\qquad L=12420,
\]

with indices cyclically.  Add four fresh coordinates

\[
                 p_0,p_1,q_0,q_1,
\]

and put `c=i mod 2`.  Use the cyclic source word

\[
             W=(T_i,p_c,q_c)_{i=0}^{L-1}.                 \tag{2.1}
\]

The depth-two derivative of `(2.1)` has the three owners per base edge

\[
\begin{aligned}
 A_i&=T_i+p_c+q_c,\\
 B_i&=T_{i+1}+p_c+q_c,\\
 C_i&=T_{i+1}+p_{1-c}+q_c.                         \tag{2.2}
\end{aligned}
\]

The next owner is `A_(i+1)=T_(i+1)+p_(1-c)+q_(1-c)`.  Hence each old
transition is replaced by

```text
base exchange, p exchange, q exchange.                         (2.3)
```

The three consecutive support types in `(2.3)` live in disjoint coordinate
pools.  Every two consecutive lower supports are therefore disjoint.  Every
immediate-upper transition skips across two consecutive lower supports; three
successive support pools are disjoint, so the immediate-upper trace is also
q=2 resident.

Direct verification gives:

```text
ground size                         27
owner rank                          13
owners                           37,260
components                            1
owner simplicity                    yes
immediate-upper simplicity           yes
immediate-lower ticket simplicity     no
lower positive/zero minima          3/3
upper positive/zero minima          4/2.
```

The lower zero minimum is witnessed by `p0` and the upper zero minimum two is
also witnessed by `p0`.  Thus the sharp upper gap two comes from the repeated
fresh clock anchors, not from inherited D5 geometry.  The positive minima are
witnessed by old coordinate zero.

The state clock in `(2.3)` is a square, not `K3`: its states run through

```text
p0q0, p1q0, p1q1, p0q1, ... .                              (2.4)
```

Only three of the four square states occur per base exchange, explaining the
factor `3L` rather than `4L`.

This construction is deliberately static.  It preserves the one-component
topology by edge subdivision and embeds all 12,420 original immediate-upper
screen colours injectively.  It does not exhibit one common source bank whose
two states realize both `F-` and `F+`, and its immediate-lower tickets are not
simple.  It therefore cannot be cited as a dynamic actuator or as a complete
palette/current repair.

## 3. Exact no-go for literal common-history clocks

### 3.1 Two histories fail twice

Every touched component of `F-` is odd:

```text
330 components of length 23
 42 components of length 115.                                (3.1)
```

Consequently no tag alternating between two literal histories can close on
even one old component.

There is a second, local obstruction.  Give each old component a binary phase
offset and each selected circuit one common splice phase.  Every removed edge
gives one XOR equation between those variables.  In selected `edge_index=3`,
two removed labels in the same old component give

```text
label 10100101110111111000000, row 13: required XOR 0
label 10101100110111111000000, row  0: required XOR 1.         (3.2)
```

Thus the phase system contains a length-two inconsistent cycle even if the
odd closure obstruction `(3.1)` is ignored.

### 3.2 Arbitrary successor tags also fail

The variable-successor-tag clock allows a finite tag set `P`.  After choosing
one orientation of every old component and one of the two orientations of the
final cycle, it requires

\[
 t(s^-(v))=t(s^+(v))\ne t(v)\qquad(v\in V),             \tag{3.3}
\]

where `s-` and `s+` are the two successor maps.  Equality in `(3.3)` is what
keeps the terminal tag of the block for `v` unchanged when its successor is
rethreaded.

Equation `(3.3)` has no solution in either final orientation.  The exact SAT
encoding first rejects tag alphabets of sizes one through eight.  More
decisively, it encodes a tag by 14 independent bits.  Since

\[
                         2^{14}>12420,                       \tag{3.4}
\]

14 bits can give every equality class a private tag.  Therefore UNSAT is not
an alphabet bound: for every choice of old orientations, the equalities in
`(3.3)` contract the endpoints of a required tag-change edge.

An independent solver-free replay certifies two inclusion-minimal quotient
cores:

| final orientation | owner equations | old components | orientations replayed | result |
|---|---:|---:|---:|---|
| forward | 86 | 4 | 16 | every orientation has a quotient loop |
| reverse | 96 | 5 | 32 | every orientation has a quotient loop |

Deleting any one of the 86 or 96 owner equations admits a loop-free
orientation.  For the forward core, the first loop-equality-path lengths over
the 16 orientations have histogram

```text
4:2, 11:2, 12:8, 57:4.
```

For the reverse core they have histogram

```text
2:8, 11:18, 12:2, 14:2, 61:2.
```

This proves an alphabet-independent no-go for the literal
variable-successor-tag block, not a no-go for every multi-lane or
state-reset switchbox.

## 4. Exact three-state reset boundary

Forget orientations and let `G` be the simple graph whose vertices are the
12,420 touched owners and whose edges are the suppressed owner transitions of
either `F-` or `F+`.  Its exact census is

```text
old edges                         12,420
new edges                         12,420
union edges                       12,897
degree 2 / 3 / 4          11,486 / 914 / 20.          (4.1)
```

Every old component in `(3.1)` is an odd cycle, so `chi(G)>=3`.  The frozen
certificate gives a literal proper 3-colouring of every edge in `(4.1)`, so

\[
                              \boxed{\chi(G)=3}.              \tag{4.2}
\]

For each selected row, write `(a,b,c)` for the states of its changed tail,
old external head, and new external head.  The exact histogram is

```text
011:90  012:34  021:36  022:9
100:104 102:38  120:36  122:7
200:40  201:33  210:35  211:15.                      (4.3)
```

There are 265 pass rows with `b=c` and 212 nontrivial reset rows with
`b!=c`.  In the latter case properness forces `{a,b,c}={0,1,2}`.  Reversal
identifies `b->c` with `c->b`, leaving exactly three unoriented reset types:

```text
tail 0 switches ports {1,2}
tail 1 switches ports {0,2}
tail 2 switches ports {0,1}.                         (4.4)
```

### Theorem 4.1 (conditional three-state reset reduction)

Suppose that for each tail state in `(4.4)` there is one bounded protected
switchbox with the following interface.

1. Its pass and swap states use the same owner, immediate-upper, and required
   lower resource bank.
2. Both states and all exposed terminal collars are q=2 biresident.
3. The swap permutes precisely the two other-state ports while fixing the
   tail socket; its inverse uses the same bank.
4. Its old-to-new q2 target current is support-monotone.
5. Private tail occurrences compose disjointly, while equal external roles
   may coalesce up to multiplicity four without identifying occurrence
   tickets.

Then the 41-circuit D5 bank admits a dynamic q2-resident reset lift with the
same `372 -> 1` component action.  It uses the pass state on the 265 pass rows
and the appropriate switchbox in `(4.4)` on the 212 reset rows.

#### Proof

The certificate in `(4.2)` makes every old and new factor edge join distinct
states.  Formula `(4.3)` exhausts the 477 changed rows.  Pass rows retain the
same port state.  Every remaining row is exactly one of the three switches in
`(4.4)`.  Items 1 and 5 make the simultaneous substitution resource exact;
items 2 and 4 give residence and q2 support.  Item 3 realizes exactly the
original incidence toggle, so suppressing each protected switchbox recovers
`F+`.  The frozen traversal of `F+` therefore supplies the same component
action.  \(\square\)

The hypotheses are intentionally an interface, not a hidden construction.
In particular, a box which changes its internal bank when it chooses the
other successor does not satisfy item 1; that is exactly the failure caught
by `(3.3)`.

## 5. `K3` switchboxes and the thirteen-port theorem

Representing a state by two of three labels makes the state graph
`J(3,2)=K3`.  Bare `K3` cannot be q=2 resident: the supports of any two
consecutive `K3` edges intersect.  A `K3 x Q_s` construction can therefore
solve the graph/owner residence layer only if the payload supplies separating
Johnson moves between state seams and all terminal routings traverse one
fixed owner bank.  A successful construction must still pass the
immediate-palette and q2-current clauses of Theorem 4.1.  The square clock in
Section 2 proves that two fresh separating support pools are sufficient for a
single fixed chronology; it does not provide the required three-terminal
fixed-bank router.

The thirteen universal ports theorem concerns canonical native MSW rows,
highest-valley parent packets, and the inequality `n>=13(d+1)`.  At the
present depth `d=2`, the finite D5 ground size 23 violates that inequality.
Moreover the D5 cross-suffix circuits have not been shown to be same-start
direct packet cuts.  Hence that theorem cannot be used to bypass the no-go in
Section 3.  An asymptotic host could use its ports only after a reset template
has supplied the missing literal histories.

## 6. Frozen H100 certificate

All substantive execution, SAT solving, exhaustive orientation replay, and
hashing was performed on H100.  The principal artifacts are:

| artifact | SHA-256 |
|---|---|
| frozen D5 selection | `94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32` |
| defect provenance output | `98d2b9242df698cc042b4b4fbff23e72e1f29849ed52fcbf8ae71cc14e10b5da` |
| static four-clock output | `5052cbf34c8a30b61346e173bb1caa0eb78f985e0e337b740a657702601c8480` |
| state/phase certificate | `05552624784b67253b9f7d07b3e37c63cb25254d9b80872835952c38ba9605c1` |
| successor-tag UNSAT output | `ebe7466e5f5a42ad8f331fa15b55d4b3ff886bd6d9db148fca86dc6447ec0e53` |
| inclusion-minimal tag cores | `a3057383999192185c492fec32878965b54bec0b8c07cf7ff616ff050e919923` |
| solver-free core replay | `ae5798bdfb0a8172aed5faac393d8129ac3ce497550ce305fbe48089591f65a6` |
| independent three-state replay | `cf1672b98e6c4c18c29162611eb023e7f719be97a2bf15b6a7677b6acff745e3` |
| aggregate hostile audit | `2252786824f0353a7b6056a004f04f95948b64c76724fde779a82d83d6fba2fb` |

The aggregate audit source has SHA-256

```text
3dc2598081ec097d1c64ea72c9ac96f26eb4d8d1e06ab93132fd9f155ae692a2.
```

## 7. Sharp remaining gate

The present D5 topology and q2-support theorem survives intact, and a static
resident output chronology exists with constant overhead.  What remains is
strictly smaller than an unstructured history search:

\[
 \boxed{\text{construct one fixed-bank resident three-terminal reset
 switchbox for each tail state, and audit its palette/q2 current.}}
\]

The literal two-history and arbitrary successor-tag routes are closed by the
quotient obstructions above.  A successful next construction must be
multi-lane or internally resource-permuting, such as a protected
`K3 x Q_s` switchbox; more aligned copies of the same successor-dependent
block cannot work.
