# A shortest resident return rail for the Boolean-hex cycle actuator

Date: 2026-08-01  
Status: exact local theorem.  The return rail is shortest among
four-resource-private resident Johnson collars, its complete higher-width
deck is explicit, and the paid/carried distinction removes the need for a
phase-common compiler.  No Pascal theorem producing these collars is
claimed.

## 0. Outcome

Let

\[
 e=(L,U,E,F),\qquad E=L+d_0,\quad F=L+a,\quad U=L+a+d_0
\tag{0.1}
\]

be the target atom of a ternary Boolean hex.  Here `L` has size `m-1`.
Let `h` be the required residence depth; thus every non-boundary positive
coordinate run must have length at least `h+1`.

For

\[
 1\le h\le m-2,\qquad
 x_0,\ldots,x_{h-1}\in L\setminus\{b\}\text{ distinct},\qquad
 y\notin U\cup\{c\},                                      \tag{0.2}
\]

there is a return path from `F` to `E` with exactly `h+2` Johnson edges.
Adjoining `EF` makes a cycle on `h+3` vertices on which every nonconstant
coordinate has one positive run of length exactly `h+1`.  The collar uses
no lower or upper colour of the ternary packet.  Moreover:

* every interval of at least three collar vertices has the same union;
* the collar prefix and suffix decks each have only three states; and
* `h+2` is the minimum possible length for a private resident return path.

For one fixed target and one fixed ternary-hex choice `(b,c)`, the
construction has exactly

\[
                         (m-2)(m-2)_h                  \tag{0.3}
\]

ordered realizations.

Thus residence and the internal arbitrary-width upper deck are not the
obstruction for this actuator.

There is nevertheless a sharp unary warning.  The old and new physical
phases do **not** have equal clipped boundary-run records and do not have
the same socket pairing.  Hence the naked actuator is not U3- or U4-neutral
in the strong unary sense.

For the additive-constant spine this equality is unnecessary.  The old
phase may be carried only as an auxiliary owner/q1 state, while the all-new
phase is terminally physicalized and compiled afresh.  In that
phase-decoupled use, only separate old/plus residence and upper certificates,
and a plus-state terminal cap certificate, are required.

## 1. The rotating-hole rail

Use the ternary packet notation

\[
 O=\{AB,CD,EF\},\qquad N=\{AF,CB,ED\},                 \tag{1.1}
\]

where

\[
 A=U-b,\quad B=L-b+a+c,\quad
 C=L-b+c+d_0,\quad D=L+c.                              \tag{1.2}
\]

Put

\[
                         Z=L+a+d_0+y.                  \tag{1.3}
\]

The following cyclic list has `h+3` distinct labels:

\[
 z_0=a,\quad z_1=y,\quad z_2=d_0,\quad
 z_{j+3}=x_j\ (0\le j<h).                              \tag{1.4}
\]

Indices below are modulo `h+3`.  Define

\[
                         V_i=Z\setminus\{z_i,z_{i+1}\}.
\tag{1.5}
\]

Then

\[
 V_0=E,\qquad V_1=F,                                   \tag{1.6}
\]

and the directed return rail is

\[
 {\cal R}: V_1\longrightarrow V_2\longrightarrow\cdots
           \longrightarrow V_{h+2}\longrightarrow V_0. \tag{1.7}
\]

In the more expanded notation its vertices are

\[
\begin{aligned}
 F&=L+a,\\
 P&=L-x_0+a+y,\\
 K_j&=L-\{x_{j-1},x_j\}+a+d_0+y\quad(1\le j<h),\\
 Q&=L-x_{h-1}+d_0+y,\\
 E&=L+d_0.
\end{aligned}                                           \tag{1.8}
\]

For `h=1` the `K`-list is empty.

The choices in (0.2) consist of one of the `m-2` legal exterior labels
`y` and an ordered `h`-tuple from the `m-2` legal labels of
`L-{b}`.  This proves (0.3).

### Theorem 1.1 (private four-resource rail)

Every edge in (1.7) is a Johnson edge.  Its lower and upper colours are

\[
 \ell_i=Z\setminus\{z_i,z_{i+1},z_{i+2}\},\qquad
 u_i=Z\setminus\{z_{i+1}\},                            \tag{1.9}
\]

for the corresponding consecutive vertices `V_i,V_(i+1)`.

All rail lower colours are distinct, all rail upper colours are distinct,
and neither family meets the corresponding palette of `O` or `N`.
All internal rail vertices are different from `A,B,C,D`.  Consequently

\[
                         G^-=O\cup{\cal R},\qquad
                         G^+=N\cup{\cal R}              \tag{1.10}
\]

are four-resource matchings with identical complete typed palettes.

#### Proof

Consecutive missing pairs in (1.5) share exactly one label.  This gives
(1.9), and proves Johnson adjacency.  The shared labels on the rail edges
are

\[
                     d_0,x_0,\ldots,x_{h-1},a,          \tag{1.11}
\]

so the upper colours are distinct.  The missing triples in (1.9) are
distinct consecutive triples in the label cycle, so the lower colours are
distinct as well.

The omitted edge `V_0V_1=EF` has upper colour `Z-y=U` and lower colour
`Z-\{a,y,d_0\}=L`.  Hence neither target colour occurs on the rail.  The
other two packet upper colours contain `c`, whereas no rail upper colour
does.  The only possible equality between a rail lower colour and
`L-b+a` would be the first rail triple with `x_0=b`; this is excluded by
(0.2).  The remaining non-target packet lower colour contains `c`, and
again cannot occur on the rail.  This proves palette privacy.

Every nonendpoint rail vertex contains `y`; `A,B,C,D` do not contain `y`
because `y!=c`.  The endpoints are the intended `E,F`, and (0.2) also
separates the first lower colour from the `b`-packet.  Thus the physical
roles are private.  Finally `res(O)=res(N)` is the ternary-hex identity, so
(1.10) has equal complete typed palettes.  \(\square\)

## 2. Exact residence and optimality

### Theorem 2.1 (threshold residence in both physical phases)

On the old cycle

\[
                         V_0,V_1,\ldots,V_{h+2},V_0,    \tag{2.1}
\]

every nonconstant coordinate has a unique positive cyclic run of length
exactly `h+1`.

In the new physical phase the two paths are

\[
 A,V_1,V_2,\ldots,V_{h+2},V_0,D,\qquad C,B.             \tag{2.2}
\]

Neither path has a positive internal coordinate run shorter than `h+1`.
Every shorter positive run in (2.2) meets an external endpoint and is
therefore a clipped boundary run.

#### Proof

In (2.1), each label `z_i` is absent from exactly the two consecutive
vertices `V_(i-1),V_i` and is present on the other

\[
                         (h+3)-2=h+1                 \tag{2.3}
\]

vertices.  Coordinates of `Z` not in the label list are present
throughout, and coordinates outside `Z` are absent throughout.  This proves
the old-cycle statement.

Cutting the cycle at `EF` turns every selected `x_j` run into two runs
meeting the two ends of the rail.  Appending `A` and `D` only extends those
clipped runs.  The coordinate `y` has the internal run
`V_2,...,V_(h+2)` of length `h+1`.  The coordinate `d_0` has one left
endpoint singleton at `A` and the internal run ending at `E` of length
`h+1`.  The coordinate `a` has one leading clipped run and no internal
short run.  The coordinate `b` has one trailing clipped run, while `c`
occurs only at the right endpoint `D`.  Every other coordinate is constant
or has only endpoint-clipped pieces.  On `C,B`, a changing coordinate
occurs only at an endpoint.  This proves (2.2).  \(\square\)

### Theorem 2.2 (shortest private resident return)

Let `R` be any simple Johnson return path from `F` to `E` such that
`O union R` is a four-resource matching.  If every nonconstant positive
coordinate run on the cycle `EF union R` has length at least `h+1`, then
`R` has at least `h+2` edges.  The rail (1.7) attains equality.

#### Proof

Let `W` be the first vertex after `F` on `R`.  If `d_0 in W`, Johnson
adjacency forces

\[
                         F\cup W=F+d_0=U,              \tag{2.4}
\]

which repeats the upper colour of `EF`, contrary to four-resource
injectivity.  Thus `d_0` is absent at the two consecutive cycle vertices
`F,W`, but is present at `E`.  Its zero run has length at least two and one
of its positive runs has length at least `h+1`.  The cycle therefore has at
least `h+3` vertices, so its return path has at least `h+2` edges.
Theorem 2.1 shows equality for (1.7).  \(\square\)

The qualifier "private" is essential.  Without the q1 upper-colour
condition, adding `d_0` immediately and deleting `a` at the end gives a
shorter residence pattern but repeats the target upper colour `U`.

## 3. Exact arbitrary-width deck

The construction is a small wreath over a fixed core.  Put

\[
 K=L\setminus\{x_0,\ldots,x_{h-1}\},\qquad
 \Gamma=\{z_0,\ldots,z_{h+2}\}.                       \tag{3.0}
\]

Then

\[
 V_i=K\cup\{z_{i+2},z_{i+3},\ldots,z_{i+h+2}\},       \tag{3.0a}
\]

with cyclic indices.  Thus `V_i` is an `(h+1)`-window in the cyclic order
of the `h+3` active labels.  In particular, if

\[
                         W_j=K\cup\{z_j\},             \tag{3.0b}
\]

then

\[
                         V_i=\bigcup_{t=0}^{h}W_{i+2+t}. \tag{3.0c}
\]

So the old rail cycle has an explicit depth-`h` erosion source; residence
is not only necessary here but constructively factorized.

### Theorem 3.1 (three-window saturation)

Every interval of at least three consecutive rail vertices has union `Z`.
Equivalently,

\[
 \bigcup_{t=i}^jV_t=Z\qquad\text{whenever }j-i+1\ge3   \tag{3.1}
\]

inside the linear rail (1.7).

Its nonempty prefix-union states are exactly

\[
             F=Z-\{y,d_0\},\qquad Z-d_0,\qquad Z,     \tag{3.2}
\]

and its suffix-union states are exactly

\[
             E=Z-\{a,y\},\qquad Z-a,\qquad Z.         \tag{3.3}
\]

In particular the complete width-`q>=2` internal upper deck of the rail is
the singleton `{Z}`.

#### Proof

The complement in `Z` of a union of vertices is the intersection of their
missing pairs.  Three consecutive edges of the simple label cycle (1.4)
have empty common intersection.  Hence every three consecutive vertices
already have union `Z`, and longer intervals cannot lose elements.  The
first two rail vertices miss the common label `d_0`; the last two miss the
common label `a`.  This gives (3.2)--(3.3).  \(\square\)

### Corollary 3.2 (complete local higher deck of the two phases)

Internally, the old cycle has only the higher-width value `Z`.  On the new
long path in (2.2), intervals of at least three vertices have exactly the
three possible unions

\[
                         Z,\qquad Z-a+c,\qquad Z+c.     \tag{3.4}

\]

The second value is realized by `Q,E,D`; the third by the four-vertex
suffix preceding `D`; all intervals of at least three vertices not reaching
`D` have union `Z` once they include three rail vertices.

Thus the local phase switch loses no old internal `q>=2` value.  It adds
the two displayed `c`-values.  This statement is local to the actuator
components; it does not assert external prefix/suffix dominance after the
components are spliced into a larger word.

### Corollary 3.3 (exact ray ticket)

For any fixed external fragment order, all crossing intervals involving
the rail are computed by

\[
 S\cup W\cup P,                                        \tag{3.5}

\]

where `S` is a suffix union of the left fragment, `P` is a prefix union of
the right fragment, and `W` is the union of whole intervening fragments.
The rail contribution to `S` or `P` has only the three states
(3.2)--(3.3).  Therefore the rail's arbitrary-width upper interface is a
constant-size pair of nested rays, independent of `h`.

For a protected target, preservation is still governed by the exact
last-witness criterion: it needs an old witness avoiding every cut or a new
crossing witness.  A "ticket per ray" is sufficient only when a ticket is
a complete ladder certificate for all protected targets on that ray.  One
named mask at the end of a ray does not certify the other targets, and
separate targetwise exceptional-label sets do not imply a global star
cover.

## 4. Strong unary U1--U4 audit

The rail solves internal residence, but the naked actuator is not a unary
transparent slot.

### Proposition 4.1 (U3 and U4 fail without a joint interface)

In the old phase the component beginning at socket `A` is the two-vertex
path `A,B`.  Coordinate `a` is present on that whole component, so its
leading and trailing positive-run lengths are both two and its
whole-fragment flag is one.

In the new phase the component beginning at `A` is the long path in (2.2).
Its leading `a`-run has length `h+2` and stops before `Q`; the
whole-fragment flag is zero.  After clipping at `h+1`, these records are
still different (for `h=1` the whole-fragment flag separates them).
Therefore strong phase-neutral U3 fails.

The old socket relation is

\[
                         A\mapsto B,\qquad C\mapsto D,   \tag{4.1}
\]

whereas the new relation is

\[
                         A\mapsto D,\qquad C\mapsto B.   \tag{4.2}
\]

Thus unary same-relation U4 also fails.  Upper-ray tickets can address U1
and U2 only; no collection of upper tickets can repair either (4.1)--(4.2)
or the clipped-run mismatch.

This does not make the actuator unusable.  It says that the two phases must
be treated by a joint stateful interface, or—more economically for the
bounded spine—physicalized separately as in the next section.

## 5. Phase-decoupled regenerative composition

The paid/carried distinction removes three unnecessarily strong equalities.

### Theorem 5.1 (auxiliary/terminal phase decoupling)

Suppose a bounded recursive record contains a private bank of old collared
states `G^-` and their palette-identical all-new states `G^+`.  Assume:

1. the **old auxiliary state** has its own legal owner/q1 realization and
   every residence or upper-witness identity explicitly needed by the next
   recursive transition;
2. the **all-new terminal state** has some (not necessarily related)
   physical chronology of length at most `B(k)+s`, with its own residence
   and complete upper-witness certificates;
3. only the all-new terminal chronology has a common-cap compilation, with
   terminal repair family `H`.

Then

\[
                         \nu(k)\le B(k)+s+R(H).          \tag{5.1}
\]

The following are not hypotheses:

* equality of the old and new upper witness occurrences;
* equality of clipped boundary-run records across phases;
* one compiler matching surviving the phase change; or
* legality of every intermediate subset of actuator toggles.

Only the declared old auxiliary state is carried to the successor.  The
terminal cap and terminal witness occurrences are paid in dimension `k`
and forgotten.

#### Proof

The ternary-hex identity identifies the complete abstract owner/q1 resource
set of the two phases, so the all-new factor is a legal central replacement.
By hypothesis 2 it is physicalized afresh; no sequence of unary slot
replacements in the old chronology is being asserted.  Hypothesis 3 makes
this new chronology a defective terminal OR word of length `B(k)+s` whose
only missing family is `H`.  Append a shortest repair word for `H`.
This gives (5.1).

The old realization is used only in the auxiliary transition to the next
state.  The bounded-spine theorem does not transport the terminal compiler,
terminal upper occurrences, or terminal repair word.  Hence none of the
four cross-phase equalities listed above enters the induction.  \(\square\)

The bounded-eviction form of the last step is proved separately in
`MATH_THEOREM_BOUNDED_COMPILER_EVICTION_AND_PHASE_DECOUPLING_20260801.md`:
it is enough that the plus-state complete damage set meets only a bounded
number of cells of one reference compiler matching.

### Corollary 5.2 (reduced guarded-collar target)

For a phase-decoupled additive-constant proof, a resident return rail needs
only:

1. a separately valid old auxiliary residence/upper export record;
2. a separately valid all-new terminal residence/upper record; and
3. bounded terminal common-cap deficiency on the all-new chronology.

Theorem 2.1 supplies the internal residence part in both phases, and
Theorem 3.1 compresses the rail's upper interface to two three-state rays.
What remains is exterior attachment and separate phase service—not a
phase-common U1--U5 certificate.

This corollary is an implication, not a proof that the same-parity Pascal
child exports the required bounded bank.

## 6. Replay

Run

```text
python3 scratch/audit_boolean_hex_shortest_resident_return_rail_20260801.py
```

The dependency-free replay checks `1<=h<=m-2` for `3<=m<=10`: all set
ranks, Johnson edges, typed palette equality and injectivity, physical
component shapes, exact cyclic residence, absence of forbidden internal
runs in the new paths, three-window saturation, the complete local higher
deck (3.4), and the naked U3 boundary mismatch.
