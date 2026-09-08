# Multi-component even binary-voltage normal form and Waksman size audit

Date: 2026-07-29

Scope: theorem and source audit only.  No solver was run.  The starting
points are `MATH_EVEN_EQUIVARIANT_CT_NORMAL_FORM_20260729.md`,
`MATH_K16_EXACT_BENES_KISSAT_ENCODING_20260729.md`, and
`scratch/search_even_eager_benes_cnf_20260729.cpp`.

## 1. Verdict

The one-component voltage-one `(c,t)` chart has an exact multi-component
extension, but its chronology variable is a **successor permutation with
edge phases**, not a second cyclic ordering of one global `c` word.

For `K=2r`, put `n=K-1` and

\[
 N={1\over n}\binom K r=2\operatorname{Cat}_{r-1}.
\]

An oriented rotation-invariant middle-layer factor is represented exactly
by

\[
 (B_i,t_i,\sigma,p_i)_{i\in[N]},
 \tag{1.1}
\]

where `B_i` is an old-coordinate mask, `t_i` is the fixed-coordinate bit,
`sigma` is a permutation of the `N` quotient slots, and `p_i in Z_n` is the
phase on the successor edge.  The component voltages are cycle sums of the
`p_i`.

For any fixed finite window catalogue, this extension admits a shared-
control Waksman encoding of size

\[
 O\bigl(KLN\log N+K HN\log(HN)\bigr),
 \tag{1.2}
\]

where `L` is the largest requested width and `H` is the number of requested
widths.  Component voltages require only a further
`O(N log N log N)` bit-multiplexer budget (and in the usual word-level
count, `O(N log^2 N)`), not a selector for each voltage tuple.  Thus
arbitrary components and arbitrary component voltages cause no
`n^c` or target-by-window selector blowup.

This is a theorem about an implementable extension.  The current C++ source
does **not** already encode it: it hard-codes successor `j -> j+1`, twisted
wrap of voltage one, and residence clauses on the resulting single cyclic
`c,t` chronology.  Merely deleting its voltage-one wording would be
unsound.

## 2. Exact binary-voltage normal form

Let `X=Z_n`, let `z` be fixed by `rho`, and let `rho(x)=x+1` on `X`.  The
action of `rho` on both old ranks `r` and `r-1` is free, since

\[
 \gcd(n,r)=\gcd(n,r-1)=1.
 \tag{2.1}
\]

For a mask `B subset X` and bit `t`, abbreviate

\[
 U(B,t)=B\cup(\{z\}\text{ if }t=1).
\]

### Theorem 2.1 (oriented multi-component normal form)

There is a bijection, modulo the vertex gauges in Section 3, between:

1. oriented, `rho`-invariant spanning cycle factors of the rank-`r` Johnson
   layer, with no physical cycle of length one or two; and
2. data (1.1) satisfying:

   * `|B_i|+t_i=r` for every `i`;
   * the `N` masks `U_i=U(B_i,t_i)` represent all rotation orbits of
     rank-`r` owners exactly once;
   * `sigma` is a permutation of `[N]`;
   * for every `i`, `U_i` and `rho^{p_i}U_{sigma(i)}` are distinct Johnson
     neighbours;
   * writing `h=sigma^{-1}(i)`, the incoming and outgoing physical
     neighbours at `U_i` are distinct:

     \[
       \rho^{-p_h}U_h\ne\rho^{p_i}U_{\sigma(i)}.
       \tag{2.1a}
     \]

The physical states and successor are

\[
 T_{i,s}=\rho^s U_i,
 \qquad
 F(i,s)=(\sigma(i),s+p_i),
 \qquad (i,s)\in[N]\times\mathbb Z_n.
 \tag{2.2}
\]

If `C=(i_0,...,i_{ell-1})` is a cycle of `sigma`, define

\[
 v_C=\sum_{i\in C}p_i\pmod n,
 \qquad g_C=\gcd(n,v_C).
 \tag{2.3}
\]

Then `C` lifts to exactly `g_C` physical cycles, each of length

\[
 \ell n/g_C.
 \tag{2.4}
\]

Consequently the total physical component count is

\[
 \sum_{C\in\operatorname{cyc}(\sigma)}\gcd(n,v_C).
 \tag{2.5}
\]

#### Proof

The orbit-transversal condition and freeness show that (2.2) contains each
rank-`r` owner exactly once.  The edge condition makes every successor a
Johnson edge.  Since `sigma` is bijective, `F` has one successor and one
predecessor at every owner.  Equation (2.1a) makes these two undirected
incidences distinct and therefore gives a simple spanning cycle factor.

Conversely, orient each physical cycle.  Such orientations may be chosen
`rho`-equivariantly.  Indeed, choose an orientation on one cycle in every
orbit of cycles and transport it by `rho`.  A stabilizer of a cycle has odd
order, whereas reversal has order two, so no stabilizer element reverses
the transported orientation.  Choose one owner representative `U_i` from
each free owner orbit.  Equivariance gives a unique quotient successor
orbit `sigma(i)` and unique phase `p_i`; bijectivity of the physical
successor makes `sigma` a permutation, while simplicity gives (2.1a).
This recovers (1.1).

After one quotient lap around `C`, the sheet phase has increased by `v_C`.
Translation by `v_C` on `Z_n` has `g_C` cycles of length `n/g_C`, proving
(2.4)--(2.5).  ∎

The local Johnson condition can be written without XOR ambiguity.  Put

\[
 S_i=|\rho^{p_i}B_{\sigma(i)}\setminus B_i|,
 \qquad
 E_i=|B_i\setminus\rho^{p_i}B_{\sigma(i)}|.
\]

Then it is exactly

\[
(S_i,E_i)=
\begin{cases}
(1,1),&t_i=t_{\sigma(i)},\\
(0,1),&(t_i,t_{\sigma(i)})=(0,1),\\
(1,0),&(t_i,t_{\sigma(i)})=(1,0).
\end{cases}
\tag{2.6}
\]

Thus Theorem 2.2 of the one-component chart survives edge by edge.  What
does not survive is its fixed residue-class transversal: the target slot is
now `sigma(i)`, not `i+1`.

### Relation to the old `(c,t)` chart

The `KN` bits `(B_i,t_i)` have exactly the same raw count as `(c,t)`:

\[
 KN=(n+1)N=nN+N=W+N.
 \tag{2.7}
\]

For the single quotient cycle

\[
 \sigma(j)=j+1\pmod N,qquad p_j=0\ (j<N-1),\qquad p_{N-1}=1,
 \tag{2.8}
\]

flattening the old-coordinate membership matrix gives the original
`c` word and its twisted wrap.  Thus `(c,t)` is the fixed-successor,
voltage-one specialization of Theorem 2.1, not a WLOG representation of an
arbitrary equivariant factor.

## 3. Exact gauge and voltage invariants

Changing the chosen representative at slot `i` by

\[
 U_i'=\rho^{q_i}U_i
\]

changes the edge phases by the coboundary

\[
 p_i'=p_i+q_i-q_{\sigma(i)}.
 \tag{3.1}
\]

Every component voltage (2.3) is therefore gauge invariant.  Reversing one
oriented quotient component changes its voltage from `v_C` to `-v_C`.
A global old-coordinate multiplier `x -> a x`, where `a` is a unit modulo
`n`, multiplies **every** component voltage by the same `a`.

Hence the exact equivalence relation on the voltage tuple (not a complete
invariant of the underlying factor) is generated by:

1. permutation of components;
2. independent sign changes `v_C -> -v_C`;
3. one common multiplication by `a in Z_n^*`.

This yields the following scope audit.

### WLOG statements

* Choosing one representative per owner orbit and applying arbitrary
  coboundary gauges (3.1) is WLOG.
* For one quotient component whose voltage is a unit, a global coordinate
  multiplier makes that voltage one.  This is the precise WLOG used by the
  existing `(c,t)` theorem at the Boolean-cube level.  Inside a restricted
  framed or directed catalogue it is WLOG only after proving that the
  catalogue is closed under that multiplier.
* With several components, one chosen unit component may be normalized to
  voltage one.

### Sufficient subclasses, not WLOG statements

* `sigma` having one component is not WLOG.
* Every `v_C` being a unit is not WLOG.  A nonunit voltage is a valid factor
  component and merely gives more physical lift cycles.
* Even if every `v_C` is a unit, setting every voltage to one is not WLOG.
  After normalizing one voltage, the remaining relative voltage ratios
  survive up to signs.
* A cap on the number of quotient or physical components is a construction
  hypothesis justified only by a separate seam/compiler theorem.

The smallest algebraic obstruction already has two quotient components:
voltages `(1,u)` with `u notin {1,-1}` cannot both be made one by a common
multiplier and independent reversals.  At `n=15`, `(1,2)` is such an
example.  The audited `k=16` two-cycle factor with quotient voltages `2` and
`9` is stronger: the second voltage is nonunit and hence cannot become a
unit under any allowed normalization.

There is also a smallest literal even-dimensional factor obstruction at
`K=6`, `n=5`: on each of the two shores take the quotient loops generated
by old masks `{0,1}` with voltage one and `{0,2}` with voltage two (using
complements on the other shore).  Their four voltages are `(1,2,1,2)`;
all are units and every lift is a physical five-cycle, but the sign classes
`{1,4}` and `{2,3}` are disjoint.  At `K=4`, `U(3)={+1,-1}`, so no such
all-unit obstruction survives independent reversal.  This exact example
shows that simultaneous voltage one is already a proper subclass at the
first possible even dimension.

## 4. Windows and residence for arbitrary voltages

For each quotient start `i`, define aligned owner words recursively by

\[
 Q_{i,0}=U_i,
 \qquad
 Q_{i,h+1}=\rho^{p_i}Q_{\sigma(i),h}.
 \tag{4.1}
\]

Equivalently,

\[
 Q_{i,h}=\rho^{p_i+p_{\sigma(i)}+\cdots+p_{\sigma^{h-1}(i)}}
           U_{\sigma^h(i)}.
 \tag{4.2}
\]

For a physical start `(i,s)`, the `h`th state is exactly
`rho^s Q_{i,h}`.  Crucially, for every fixed quotient slot `i`, **all**
`s in Z_n` occur among the physical states of the full lifted factor,
regardless of `v_C` and regardless of `gcd(n,v_C)`.  Nonunit voltage only
distributes these phases among several physical cycles.

Let

\[
 L_C=|C|n/\gcd(n,v_C)
 \tag{4.3}
\]

be the length of each physical lift cycle over quotient component `C`.
A width-`w` interval is **one-pass eligible** at a slot of `C` exactly when
`w<=L_C`.  Following the successor for more than `L_C` states repeats a
letter and is not an interval in an opening which uses that physical cycle
once.

### Theorem 4.1 (active component/voltage-independent orbit cover)

Fix a finite width set `D`.  The full lifted factor covers a required
rotation orbit by a one-pass lower intersection or upper union of width
`w in D` if and only if one of the quotient words

\[
 \bigcap_{0\le h<w}Q_{i,h}
 \quad\hbox{or}\quad
 \bigcup_{0\le h<w}Q_{i,h}
 \tag{4.4}
\]

at a slot `i` whose component satisfies `w<=L_C` lies in that orbit.  The
number of active quotient inputs at width `w` is exactly

\[
 M_w=\sum_C |C|\,\mathbf1_{\{w\le L_C\}}.
 \tag{4.5}
\]

#### Proof

When `w<=L_C`, the interval beginning at `(i,s)` is the common rotation by
`rho^s` of the aligned words in (4.1), with no repeated physical letter.
Intersection and union commute with this common rotation.  As `s` ranges
through the physical starts over slot `i`, it ranges over all of `Z_n`.
Thus (4.4) generates exactly its complete target orbit.  If `w>L_C`, every
successor string of `w` states repeats the start cycle and cannot occur in a
one-pass opening.  This proves both directions and (4.5).  ∎

The existing partial-permutation lemma therefore applies to the **active**
words.  With variable component lengths one may retain `N` fixed wires at
each width (or `HN` flattened upper wires), attach one activity bit to every
word, route it through the same cover network, and force every designated
target output to be active.  Inactive wires are exact padding.  This avoids
a component identifier or voltage selector at the cover gate.  Short target
orbits cause repeated physical occurrences but do not change the
equivalence.

This equivalence is at the cyclic-factor level.  It does not assert that one
fixed choice of a cut in every physical cycle preserves all active cyclic
windows simultaneously.  A literal opened chronology must additionally
forbid or charge the windows crossing those cuts and then join the resulting
paths; that is a separate boundary/compiler condition.

Activity itself is fixed-depth at a fixed width.  Since the owner states are
all distinct, the physical successor returns to its start after `h` steps
exactly when `Q_{i,h}=Q_{i,0}`.  Hence

\[
 A_{i,w}=1
 \quad\Longleftrightarrow\quad
 Q_{i,h}\ne Q_{i,0}\quad(1\le h<w).
 \tag{4.6}
\]

This uses `O(KNw)` equality gates once the aligned states are present.

Positive residence also remains fixed-depth.  By the project convention, a
maximal cyclic one-run includes a whole all-one physical cycle; depth `d`
requires every such run to have length at least `d+1`.  If `d+2` aligned
states have been built, then for every start `i`, coordinate bit `x`
(including `z`), and `1<=ell<=d`, first forbid

\[
 0,1^\ell,0
 \quad\text{in}\quad
 Q_{i,0}(x),Q_{i,1}(x),\ldots,Q_{i,\ell+1}(x).
 \tag{4.7}
\]

For nonconstant traces these are exactly all short maximal one-runs.  They
do not see a whole all-one cycle because it has no zero boundary.  The exact
additional rows are, for every `1<=h<=d`,

\[
 Q_{i,h}=Q_{i,0}
 \quad\Longrightarrow\quad
 \neg\bigwedge_{0\le j<h}Q_{i,j}(x).
 \tag{4.8}
\]

Equation (4.8) says that a physical cycle of length at most `d` may not be
monochromatic one in coordinate `x`.  (Cycles of length one or two are
already excluded at the factor level, but retaining their rows is harmless.)
Together (4.7)--(4.8) are necessary and sufficient for positive residence.
As `x` ranges over old coordinates, common phase is absorbed by translating
`x`, so these rows check every coordinate on every physical lift cycle,
including patterns crossing a quotient lap.  For fixed `d` they cost
`O(KNd^2)` clauses/gates after (4.1).  Thus retaining the old cyclic-run
clauses on one global `c` word would be wrong, but exact multi-component
residence does not require unbounded path enumeration.  A declared
zero-residence condition has the analogous complemented rows with its
declared zero-run threshold.

## 5. Shared-control Waksman encoding

Let `S(m)` be the switch count of the exact recursive network used in
`search_even_eager_benes_cnf_20260729.cpp`.  Before the implementation's
syntactic-identical-word elision, it obeys

\[
 S(1)=0,
 \qquad
 S(m)=2\lfloor m/2\rfloor
      +S(\lceil m/2\rceil)+S(\lfloor m/2\rfloor).
 \tag{5.1}
\]

Induction gives

\[
 S(m)\le m\lceil\log_2m\rceil.
 \tag{5.2}
\]

For `m=858`, the audited implementation has `S(858)=8078`; for `m=5148`,
it has `S(5148)=61680`.

### 5.1 Successor and aligned-state propagation

Use one Waksman network on `N` wires to define `sigma`.  Reuse its switch
controls whenever another field is routed.  If `P_sigma` denotes the
resulting routing operator, then (4.1) is implemented by

\[
 Q_{h+1,i}=\rho^{p_i}(P_\sigma Q_h)_i.
 \tag{5.3}

Let `b=ceil(log_2 n)`.  The `p_i` use `Nb` bits.  Invalid binary phase codes
are forbidden.  Building `L-1` successor layers uses at most

\[
 \boxed{
 S(N)+2K(L-1)S(N)+Nb+nbN(L-1)}
 \tag{5.4}
\]

Boolean variables before rank/Johnson comparators.  Here one switched
`K`-bit field uses two `K`-bit mux outputs per switch, and one old-coordinate
barrel rotation uses `nb` muxes per word.  The corresponding mux clauses are
at most

\[
 8K(L-1)S(N)+4nbN(L-1),
 \tag{5.5}
\]

plus `N(2^b-n)` invalid-phase clauses.

At `K=16`, `n=15`, `N=858`, `b=4`, and `L=13`, (5.4) equals

\[
 8078+3,101,952+3,432+617,760
 =3,731,222.
 \tag{5.6}
\]

This is a sizeable but controlled addition to the audited 3,984,274-variable
fixed-successor CNF.  It is not a Cartesian target-selector expansion.

### 5.2 Exact component voltages without component selectors

Component data can be certified by a rooted-cycle annotation.  Give every
slot:

* a root label `a_i in [N]`;
* an order `h_i in {0,...,N-1}`;
* a phase potential `q_i in Z_n`;
* a root flag `R_i`.

Route the corresponding fields at `sigma(i)` through the **same** Waksman
controls and impose:

\[
 a_{\sigma(i)}=a_i,qquad a_i\le i,qquad
 R_i\Longleftrightarrow a_i=i,
 \tag{5.7}
\]

\[
 R_i\Longrightarrow h_i=0,qquad
 \neg R_{\sigma(i)}\Longrightarrow h_{\sigma(i)}=h_i+1,
 \tag{5.8}
\]

and `h_i>0` for nonroots.  A cycle with no root would make the integer order
increase strictly around a closed loop; two roots on one cycle would have
two different indices equal to the same propagated root label.  Hence each
cycle has exactly one root, necessarily its minimum-index slot.

Set `q_i=0` at a root.  On a nonclosing edge impose

\[
 q_{\sigma(i)}=q_i+p_i\pmod n.
 \tag{5.9}
\]

On the unique edge entering root `j`, record

\[
 V_j=q_i+p_i\pmod n.
 \tag{5.10}
\]

Then `V_j` is exactly the component voltage.  A table at roots can impose
any allowed voltage set, calculate `gcd(n,V_j)`, count physical lift
components, or exclude the physical length-two case.  Omitting that table
allows all voltages exactly.

If `a=ceil(log_2N)`, routing the root label, order, potential, and root flag
once costs at most

\[
 2(2a+b+1)S(N)
 \tag{5.11}
\]

mux variables, plus `N(2a+b+1)` stored field bits and
`O(N(a+b))` comparator/addition gates.  For `N=858`, `a=10`, (5.11) is
`403900`.  This is near-linear and replaces any explicit enumeration of
the `n^c` voltage tuples.

The rooted annotation is needed only if the model constrains or reports
component voltages.  If arbitrary voltages are allowed, (5.7)--(5.10) can
be omitted: the selected `p_i` already define them.  Exact simple-factor
scope must still exclude a lifted two-cycle.  Since `n` is odd and a
physical self-loop already fails the Johnson row, the only remaining case is

\[
 \sigma^2(i)=i,quad \sigma(i)\ne i,quad
 p_i+p_{\sigma(i)}=0\pmod n.
 \tag{5.12}
\]

This can be forbidden by one two-successor local row per slot, or by the
rooted length/voltage table.  Omitting both would encode a directed
permutation with possible doubled Johnson edges, not a simple cycle factor.

If the `c` quotient components are already identified, the same information
can instead be stored directly in `c ceil(log_2 n)` voltage bits, with one
modular sum per component.  For directed all-unit voltage tuples, common
global scaling leaves exactly `phi(n)^(c-1)` labelled relative-voltage
classes.  Therefore every exact encoding that distinguishes those classes
needs at least

\[
 (c-1)\log_2\varphi(n)
 \tag{5.13}
\]

bits of information.  Thus one constant-size global "voltage-one" selector
cannot be exact, while a Cartesian one-hot enumeration of all
`phi(n)^c` tuples is unnecessary.  The edge phases or the `O(c log n)`
component residues have the correct information scale.

### 5.3 Orbit-cover networks

The existing Waksman cover gates retain their partial-permutation logic.  For
a family of `P` padded quotient words and `D<=P` required target orbits,
route an activity bit with each `K`-bit word and force it true at each of the
first `D` designated outputs.  Independent phase rotators plus one such
partial-permutation network use at most

\[
 (1+2(K+1))S(P)+KbP
 \tag{5.14}
\]

variables, apart from output unit clauses and the activity comparators in
(4.6).  If every input is a priori active, the activity track is omitted and
the old bound `(1+2K)S(P)+KbP` is recovered.  There is no selector factor
depending on the number of chronology components or their voltages.

For middle, `q1`, and fixed-depth `q2`, `P=N`; in a simple factor their
widths one, two, and three are automatically active.  For an upper width
catalogue of `H` widths, flattening gives `P=HN`, with inactive padding as
in Theorem 4.1.  Return equalities can be shared over widths: precompute
`Q_{i,h}=Q_{i,0}` for `h<L` in `O(KNL)` gates and form each activity bit by
prefix ANDs.  Combining (5.4), (5.11), and (5.14)
proves (1.2), with the rooted-voltage term added only when requested.

## 6. Where selector blowup does and does not return

### Arbitrary components and arbitrary voltages

They do not create selector blowup.  The successor is one permutation and
the phases are `N` bounded integers.  Component sums are consequences of
these variables.  Fixed-depth flags are generated by repeated application
of the same selected successor, and orbit coverage uses the same partial-
permutation lemma as before.

An alternative exact base is the sparse quotient-edge catalogue already
audited at `k=16`: 27,456 undirected edge-orbit variables (or 54,912
directed arcs, including the 56 directed versions of valid quotient loops),
858 degree rows, and 1,528 `q1` cover rows.  The smaller count 54,856 applies
only after those loops are forbidden in the single quotient-Hamilton model.
That catalogue
natively permits every component and voltage.  Its difficulty is not the
base size but composing longer windows without enumerating branching paths;
the shared-successor Waksman propagation is an exact way to avoid that path
tuple expansion.

### Arbitrary interval widths

This is a different issue.  With a fixed catalogue, `H,L=O(1)` and the
widening is near-linear in `N` up to logarithms.  If every width
`2,...,N` is materialized, then `H,L=Theta(N)` and there are already
`Theta(N^2)` literal start-width pairs.  The shared-Waksman construction has
size

\[
 O(KN^2\log N),
 \tag{6.1}
\]

not near-linear.  It still avoids the old target-by-window Cartesian product,
but no claim of a compact all-width theorem follows.  A reachability or
accumulated-union automaton would be a separate result.

### Fixed catalogue scope

For a declared width set, the Waksman orbit-cover condition is exactly
equivalent to physical orbit coverage for that set, now even with arbitrary
components and voltages by Theorem 4.1.  Restricting the set to
`{2,3,4,6,9,13}` remains only a sufficient catalogue subclass.  UNSAT would
mean no factor in the declared structured model whose witnesses use those
widths; it is not an arbitrary-upper or arbitrary-word theorem.

## 7. Source audit and implementation boundary

The following lines of structure in
`scratch/search_even_eager_benes_cnf_20260729.cpp` are intrinsically
single-component:

1. lines 292--297, `column(j)`, read the global flattened `c` trace at the
   fixed linear slot `j`;
2. lines 229--279 use `columns[j+1]`, `columns[j+2]`, and `columns[j+s]`,
   hard-coding the successor and every longer window;
3. lines 318--329 impose residence on the two global cyclic words `c,t`;
4. lines 330--340 index the start/end transversal by the fixed residue class
   `j`;
5. there is no shared-control successor network or edge-phase field.

In addition, lines 441--483 make `word_switch()` create or elide its control
while routing one particular word.  A shared successor must first build a fixed
switch topology and control array, then replay those controls on every mask,
root, order, and potential field.  Per-field syntactic switch elision is not
sound for shared routing (although an identical field pair may copy its
outputs while retaining the topology control for other fields).

The existing four cover networks themselves are reusable after their raw
word inputs are replaced by (4.1).  A sound widening therefore requires:

1. `KN` explicit quotient-state bits (the same base count as `W+N`);
2. one shared-control successor Waksman and `N` phase fields;
3. Johnson rows between `Q_0` and `Q_1`;
4. fixed-depth residence rows (4.7)--(4.8), replacing the global `c,t` run
   rows;
5. aligned words (4.1), with activity rows (4.6), as inputs to the existing
   cover networks;
6. the existing exact middle-orbit cover network, to enforce the owner
   transversal;
7. optionally, rooted annotations (5.7)--(5.10).

If item 7 is omitted, the direct two-cycle exclusion (5.12) is mandatory.

No current SAT/UNSAT artifact has this widened scope.  The result here is an
exact theorem and encoding-size proof, not an implementation or feasibility
claim.

## 8. Sharp proved boundary

Proved:

1. Theorem 2.1 is an exact multi-component normal form for
   rotation-invariant even middle-layer factors.
2. Equations (2.3)--(2.5) give every component voltage and physical lift
   count exactly.
3. The global normalization freedom is only common unit scaling plus
   componentwise orientation signs; simultaneous voltage-one is not WLOG.
4. Theorem 4.1 preserves literal lower/upper orbit coverage for arbitrary
   component voltages.
5. Fixed-depth residence and fixed-width shadow catalogues have a
   shared-successor Waksman encoding of the stated near-linear size.
6. Root/order/potential annotations enforce arbitrary component-voltage
   predicates without a voltage-tuple selector expansion.

Not proved:

1. feasibility of the widened `k=16` model;
2. a bounded-component or unit-per-component theorem;
3. completeness of the six-width upper catalogue;
4. an all-width near-linear encoding;
5. a safe opening, compiler completion, or literal length-12873 word.
