# Thread D: exact deep-shadow rows for the phase-free two-rail model

Date: 2026-07-30

Status: proved encoding reduction and proved labelled-frontier CEGAR rows.
The retained K8/K10 candidates were replayed solver-free.  No K16 solve was
run for this note.

## 1. Scope and audit of the existing masters

The normal form in
`MATH_THEOREM_K16_JOINT_QUOTIENT_PATH_PHASE_HISTORY_MODEL_20260730.md`
is exact in its stated class: one A block, one B block, generating voltage
normalized to one, both q1 palettes, and positive residence.  In particular:

* the rooted order formulation in
  `scratch/solve_even_two_rail_joint_history_20260730.py` excludes every
  proper quotient subtour;
* the binary rail positions in
  `scratch/solve_even_two_rail_joint_history_kissat_20260730.py` are also
  exact.  A same-shore selected edge increments its position modulo
  `Q=2^ceil(log2(M+1))>M`, so a same-shore cycle of length at most `M` is
  impossible.  The unique cross edges anchor the two paths at `0` and
  `M-1`;
* in the cycle-cover CEGAR version, for every proper selected component `C`,
  the row

  \[
       \bigvee_{e:\;\operatorname{tail}(e)\in C,
                    \operatorname{head}(e)\notin C}x_e
  \tag{1.1}
  \]

  is necessary for a Hamilton quotient circuit.  Under unit indegree and
  outdegree, the complementary directed cut has the same cardinality, so
  complement-key deduplication is sound.

Neither executable makes a deep-shadow claim.  The full-selected-option
no-good used by the first Thread-D CEGAR is sound, but throws away all the
target automaton structure.  The rows below replace it.

## 2. Exact eager lower-q2/q3 controller at K16

Write `s(u)` and `delta(u)` for the selected successor and voltage increment
at quotient owner `u`.  Treat the top coordinate as the sentinel `bot`,
fixed by rotation.  Define future deletions in the canonical frame of `u`:

\[
 f_1(u)=a(u),\qquad
 f_{j+1}(u)=\operatorname{shift}_{+\delta(u)}
                 f_j(s(u)),
\tag{2.1}
\]

where `shift_delta(bot)=bot` and
`shift_delta(x)=x+delta mod n` for an old coordinate.  The sign is positive:
a canonical label at the successor has absolute phase `g+delta`, and hence
has label `x+delta` in the source frame of phase `g`.

### Lemma 2.1 (residence freezes the lower prefix)

If positive runs have length at least `d+1`, then for `q<=d` the values
`f_1(u),...,f_q(u)` are distinct members of the full middle state at `u`,
and

\[
  \bigcap_{j=0}^{q}T_{s^j(u)}
       =T_u\setminus\{f_1(u),\ldots,f_q(u)\}.
\tag{2.2}
\]

Proof.  A coordinate deleted in these `q` transitions that was absent at
the start had to be inserted after the start; its deletion would terminate
a positive run of length at most `q<=d`.  The same argument excludes a
repeated deletion.  Every transition therefore removes one new member of
the starting state.  The top sentinel obeys the same conclusion because
the two top-changing seams are separated by a shore block of length
`M>d`.  Equation (2.2) follows.  QED.

At K16, `R=8`, `d=3`, and this gives both required depths.  For each owner,
one table maps the ordered pair `(f1,f2)` to its canonical full target orbit,
and one maps `(f1,f2,f3)`.  They have respectively

\[
   (R)_2=56,\qquad (R)_3=336
\]

legal rows per owner.  Coverage is expressed without owner-by-target
Booleans: for each target orbit `t`, introduce a witness-owner integer `w_t`
and impose `Element(w_t,ell_q,t)`.

The exact K16 orbit ledgers are

\[
\begin{array}{c|c|c}
q&\text{full target rank}&\text{target orbits}\\ \hline
2&6&335+201=536\\
3&5&201+91=292.
\end{array}
\tag{2.3}
\]

Starting from the current successor/delta/deletion variables, the complete
eager addition has the following exact semantic size:

* `4N=3,432` future-controller integers: two successor-frame values and
  `f2,f3`;
* `2N=1,716` lower-label integers;
* `536+292=828` witness-owner integers;
* total **5,976 variables and 5,976 constraints**.

The large proto payload is transparent rather than hidden: the two future
`Element` layers contain `2N^2=1,472,328` array references, the coverage
elements contain `828N=710,424`, and the shift/label tables contain
`2,532,816` scalar table entries.  Thus this is only about a five-percent
variable increase over the retained 116,921-variable CP model, but its
serialized and presolve memory must still be remeasured under the remote
memory cap.

Lemma 2.1 must not be used outside `q<=d`.  In particular K8 and K10 have
`d=2`; their q3 regression must use the general automaton below.

## 3. Exact target automata

Every physical directed Johnson arc in the scoped class has a unique label
`e`, namely its selectable quotient transition option.  Selecting `x_e`
enables all rotational lifts of that arc.  Fix one representative of a
target orbit; equivariance makes one representative sufficient even for a
non-free target orbit.

### 3.1 Lower depth q

For a lower target `L` of rank `R-q`, use layered states

\[
  (j,T,I),\qquad 0\le j\le q,
\]

where `T` is the current rank-R middle state, `I` is the intersection so
far, and `L subseteq I subseteq T` is understood along the path.  The
initial states are `(0,T,T)` for all `T superset L`.  A physical arc
`T -> T'` labelled `e` gives

\[
 (j,T,I)\xrightarrow{e}(j+1,T',I\cap T')
\tag{3.1}
\]

whenever `L subseteq T'`.  Accept exactly at layer `q` with `I=L`.  This is
the literal consecutive `(q+1)`-vertex intersection definition and needs
no residence assumption.

### 3.2 Arbitrary upper intervals

For an upper target `S`, use states `(T,U)` with `T subseteq U subseteq S`,
initial states `(T,T)` for every rank-R `T subseteq S`, and transitions

\[
  (T,U)\xrightarrow{e}(T',U\cup T')
\tag{3.2}
\]

for every labelled physical arc `T -> T'` with `T' subseteq S`.  Accept
when `U=S`.  This is the unrestricted accumulated-union recurrence; it does
not replace upper coverage by fixed-width witnesses.

For `|S|=R+q`, the full raw automaton has at most

\[
 {R+q\choose R}2^q
\quad\text{states and}\quad
 {R+q\choose R}2^qRq
\quad\text{transitions}.
\tag{3.3}

At K16 these bounds for q=2,3,4,5,6,7 are respectively

```text
states       180      1,320       7,920      41,184      192,192      823,680
transitions 2,880     31,680     253,440   1,647,360    9,225,216   46,126,080
```

The q8 target is the full coordinate set and is automatic from exact middle
ownership, so its 3,294,720-state raw automaton should never be built.
These counts rule out eager all-target upper automata.  They support lazy,
candidate-specific separation.

## 4. Labelled reachable-frontier row

Let `A_T` be either target automaton above, with initial set `I_T`, accepting
set `F_T`, and transition labels in the master option set.  For a decoded
candidate `X`, let `Reach_X(T)` be the closure of `I_T` under transitions
whose label belongs to `X`.  If no accepting state is reachable, define

\[
 B_X(T)=\{e:\ p\xrightarrow e p',\quad
             p\in Reach_X(T),\ p'\notin Reach_X(T)\}.
\tag{4.1}
\]

Then add the single positive row

\[
                 \boxed{\bigvee_{e\in B_X(T)}x_e.}
\tag{4.2}
\]

### Theorem 4.1 (soundness)

Every future selection that covers `T` satisfies (4.2).

Proof.  An accepting path begins in `I_T subseteq Reach_X(T)` and ends
outside `Reach_X(T)`.  Its first transition leaving the reachable set has a
label in `B_X(T)`, and that label is selected by the future solution.  QED.

Closure also proves `B_X(T) cap X` is empty.  Thus the candidate violates
the row, while the row preserves every compiler-ready carrier.  It is one
constraint with no auxiliary variables and is strictly more informative
than the full-candidate no-good.  For a proof-replayable checkpoint, record

```text
target kind/depth, canonical target, selected-option hash,
reachable-state hash, sorted frontier option IDs and frontier hash.
```

An independent checker regenerates the labelled physical arcs, recomputes
the closure, checks that no accept state is present, and verifies the exact
frontier.  In a DIMACS lane the row is already a clause.  In CP-SAT it is a
`BoolOr` over the same option literals.

For high-rank upper targets, a cheaper first separator is the superset row
consisting of every currently unselected option having some physical lift
entirely inside `S`.  It is sound, but (4.2) dominates it.  The exact
frontier should be generated remotely when its candidate-specific state
closure exceeds the local-light budget.

## 5. Solver-free K8/K10 regression

The independent implementation is

```text
scratch/audit_threadD_deep_shadow_component_rows_20260730.py
scratch/threadD_deep_shadow_component_rows_20260730.audit.json
```

It reconstructs every selectable physical arc and its unique option label,
replays the retained carriers, independently computes all lower-q2/q3 and
arbitrary-width upper holes, and checks automaton acceptance against the
direct audit for **every** target orbit (K8: 6 lower and 15 upper rows; K10:
19 lower and 46 upper rows for each of two fresh carriers).  It then
validates every missing-target frontier.

Results:

* K8: zero lower-q2 holes, zero lower-q3 holes, and zero arbitrary upper
  holes.  No separator is generated.
* the fresh Thread-D K10 phase-free q1+residence carrier: three physical lower-q2
  holes forming one rotation orbit represented by `73`; its exact frontier
  has 52 option literals.  Nine physical upper-rank7 holes form one orbit
  represented by `687`; its frontier has 153 option literals.  Both
  frontiers are nonempty and disjoint from the selected option set.
* the independently generated binary-order K10 carrier has nine physical
  lower-q2 holes forming one orbit represented by `37`; its frontier has
  176 option literals.  It has no lower-q3 or arbitrary-upper hole.
* neither fresh K10 carrier is compiler-ready because each misses a lower-q2
  orbit.  This does not contradict the separately retained
  compiler-passing K10 artifact.

The first fresh carrier's two frontier hashes are independently identical
to those frozen by
`scratch/threadD_lower_fixed_depth_labelled_boundary_k8_k10_20260730.audit.json`
and
`scratch/threadD_upper_accumulated_union_separator_k8_k10_20260730.audit.json`:

```text
lower rep 73: 2d4a7961cf42e37ac332eda3217a4dbc9c2ae8e16ced560a36f8ec8ecf6a620b
upper rep687: 3cd15439839401fc23a8b06798e84c8f4b5526ef9586df989ab5feb3a1ebe0fb
```

Audit payload SHA-256:

```text
ed0f3836b2c9b5f59a4779181bb297621714ac2ea9ce2108732b67ee76547605
```

## 6. Integration order and claim discipline

1. Keep the exact q1/history/base connectivity model unchanged.
2. In the CP lane, install the K16 forward-deletion q2/q3 controller before
   solving, after measuring its serialized model and presolve memory.  In
   the DIMACS lane, use the general frontier separator for lower rows to
   avoid a large one-hot controller.
3. Decode and physically replay every candidate.  Audit lower q2 and q3 by
   literal intersections and all upper ranks by the accumulated-union
   recurrence.
4. For every missing target orbit, add (4.2), persist its replay data, and
   warm-start only from the fully decoded option assignment.
5. A candidate is compiler-ready only after independent physical replay has
   zero q1, lower-q2, lower-q3, and arbitrary-upper holes, followed by the
   separate exact compiler/Hall and literal-word verifier.
6. Runtime or memory exhaustion is `UNKNOWN`.  A scoped UNSAT claim requires
   an independently checkable SAT proof format (for example DRAT/LRAT) for
   the base model plus all replayed necessary rows; a bare CP-SAT UNSAT line
   is not a proof certificate.
