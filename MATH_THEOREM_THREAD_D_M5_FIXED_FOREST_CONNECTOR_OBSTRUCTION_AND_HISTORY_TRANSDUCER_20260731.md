# The fixed `m=5` residence-clean forest cannot be joined, and the exact replacement is a short-history transducer

Date: 2026-07-31  
Status: proof-carrying finite obstruction for one fixed forest; exact general
connector reduction; no all-`m` construction and no compiler claim

## 0. Verdict

The residence-clean 42-path forest of item 2188 cannot be completed merely
by ordering/reversing its paths and inserting endpoint Johnson seams.  In
fact, a stronger relaxation is impossible: there is no matching of its 84
formal ports, with two free linear boundaries, for which every newly bounded
positive coordinate run has length at least three.  Connectivity, connector
colour injectivity, and all 21 deeper targets were omitted from this
relaxation.

This is therefore a **fixed-body obstruction**, not a return of the old
central residence obstruction.  Item 2188 proves that changing the interior
diamond matching removes all internal defects; the present result proves
that this particular successful matching has the wrong endpoint-run
signature.  A further correlated interior rethread must control both the
internal runs and the exposed rays.

The solver-free fourteen-locked-component theorem in
`MATH_THEOREM_AD_RESIDENCE_REDISTRIBUTION_AUTOMATON_AND_M5_ENDPOINT_LOCK_20260731.md`
is the primary structural proof.  The DRAT result below is an independent,
proof-carrying corroboration and supplies a small verified core; it is not
presented as logically stronger than that obstruction.

The second result below gives the exact corrected connector model for any
future forest.  It is a finite concatenation transducer.  In particular,
deeper coverage cannot in general be encoded by one seam at a time.

## 1. The fixed port system

Let

\[
             {\cal P}=\{P_1,\ldots,P_{42}\}
\]

be the literal paths in
`catalan_m5_residence_rethread_c4c6_candidate_20260731.txt`.  They partition
all 252 vertices of \(J(10,5)\), contain 210 fixed Johnson edges, and have no
positive coordinate run of length one or two bounded inside a path.

Give each path two formal ports.  The two ports of a singleton path are
distinct occurrences even though they carry the same middle vertex.  Two
ports on different paths may be paired when their endpoint masks differ in
exactly two coordinates.  There are

\[
       84\text{ ports},\qquad304\text{ formal Johnson pairs},
       \qquad293\text{ distinct physical Johnson edges}.       \tag{1.1}
\]

Adjoin two formal dummy ports.  Pairing a real port to a dummy declares it a
linear boundary.  A port matching thus selects 41 real seams and two boundary
incidences.  If its component multigraph together with the dummy component
is connected, deleting the dummy gives exactly an ordering and orientation
of the 42 paths as one linear Johnson chronology.  Without connectedness it
is a relaxation into path/cycle components.

## 2. Residence is exactly local at threshold three

### Lemma 2.1 (short-run locality)

Assume every run bounded inside a fixed path has length at least three.  A
port matching produces no new bounded run of length one or two if and only
if all the following literal rows hold for every coordinate.

1. An exposed fixed run of one vertex is extended through one incident seam,
   or touches a dummy boundary.
2. An exposed fixed run of two adjacent vertices is extended through an
   exposed side, or touches a dummy boundary.
3. If a selected seam joins two endpoint vertices both containing the
   coordinate, their two-vertex run has a fixed extension, an extension
   through the other port of a singleton block, or a dummy boundary.

#### Proof

Necessity is immediate.  Conversely, a bad final run contains one or two
vertices.  If its vertices lie in one fixed path, it is either an old
internal run (excluded by hypothesis) or has one of the forms in rows 1--2.
If it crosses a seam, its two vertices are the endpoints of that seam; the
only way that either side can continue through another seam is a singleton
path, exactly row 3.  These exhaust all possibilities. \(\square\)

The frozen CNF encodes exactly:

* one selected incident pair at every real and dummy port;
* at most one formal realization of each physical seam; and
* the three families in Lemma 2.1.

It does **not** impose connectedness, connector palettes, or deeper flags.
It has 472 variables and 10,619 clauses.

### Theorem 2.2 (fixed-forest connector obstruction)

No port matching satisfying Lemma 2.1 exists for the item-2188 forest.
Consequently no ordering and orientation of these 42 intact path bodies,
with Johnson endpoint seams, is residence-safe at threshold three.

#### Proof certificate

Kissat generated an ASCII DRAT proof of UNSAT.  `drat-trim` verified the full
proof and extracted a 68-clause core with 12 proof lemmas.  The extracted
core proof verifies independently:

```text
c 68 of 68 clauses in core
c 11 of 12 lemmas in core using 124 resolution steps
c 0 RAT lemmas in core
s VERIFIED
```

The full solver used 4 MiB RSS.  The verifier used 63 MiB RSS and 0.06 s.
The theorem follows because the certified formula is a relaxation of a
connected chronology. \(\square\)

### Corollary 2.3

The 21 deeper debts cannot be paid by connector chronology alone on this
fixed forest: the residence-compatible connector face is already empty.
This says nothing against another palette-exact interior rethread whose
endpoint rays differ.

## 3. Exact fixed-width flag transducer for the next forest

The obstruction above does not justify weakening the all-depth connector
model.  Here is the exact replacement.

Fix a residence threshold \(D\), a maximum controlled depth \(Q\), put
\(L=\max(D,Q)\), and fix a set \({\cal T}\) of missing signed targets.  For a
literal word \(w\), define

\[
 \Theta_{D,Q}(w)=
 \bigl(
   \min(|w|,L),\ \operatorname{pref}_L(w),\operatorname{suff}_L(w),
   b_D(w),\operatorname{Cov}_{\cal T}(w)
 \bigr),                                                    \tag{3.1}
\]

where:

* `pref` and `suff` retain the indicated number of literal middle masks;
* \(b_D(w)=1\) iff some coordinate has a bounded positive run of length
  less than \(D\); and
* \(\operatorname{Cov}_{\cal T}(w)\) records every target in \({\cal T}\)
  realized by a consecutive union/intersection window of its prescribed
  width.

This state concerns the fixed \((q+1)\)-vertex flag windows only.  It is not
the arbitrary-width OR/AND coverage state used by the physical compiler.

### Theorem 3.1 (short-history concatenation)

There is an associative deterministic product

\[
                 \Theta(u)\star\Theta(v)=\Theta(uv).        \tag{3.2}
\]

It is computed by inspecting only the stored suffix of \(u\), the stored
prefix of \(v\), and the two old coverage sets.

#### Proof

Any new bad run crosses the join.  If its length is below \(D\), the factor
consisting of the run and its bounding zeroes lies in the last \(D\) letters
of \(u\) and the first \(D\) letters of \(v\).  Every new depth-\(q\) witness
with \(q\le Q\) likewise lies in the last \(Q\) letters of \(u\) and the
first \(Q\) letters of \(v\).  The truncated prefix, suffix, and length update
directly.  Thus (3.2) reconstructs exactly the state of the literal
concatenation; associativity follows from associativity of concatenation.
\(\square\)

For fixed path bodies, each orientation has a fixed initial state.  A
Hamilton-path master chooses one orientation per component and legal Johnson
successor arcs.  Propagating (3.2) along the chosen path is therefore an
exact finite-domain formulation of residence and all prescribed fixed-width
flag depths.

## 4. Equivalent history-DNF/CEGAR form

For a target \(T\) of depth \(q\), every new witness has a unique description

\[
  \operatorname{suff}_{a}(P_0),P_1,\ldots,P_{s-1},
  \operatorname{pref}_{b}(P_s),qquad
  a+b+\sum_{i=1}^{s-1}|P_i|=q+1,                         \tag{4.1}
\]

where the \(P_i\) are distinctly indexed oriented paths and consecutive
endpoints are Johnson adjacent.  Its occurrence variable is the conjunction
of the \(s\) selected successor arcs.  Requiring the disjunction of all
occurrence variables realizing \(T\) is exact.  Lazy separation is also
exact: literal replay either accepts the chronology or returns the missing
target and its complete finite list of histories (4.1).

For the item-2188 forest the independent history census gives 21 debts and
no zero-provider debt.  Three targets have genuine two-seam histories:

\[
\begin{array}{c|c|c}
T&\text{one-seam histories}&\text{two-seam histories}\\ \hline
(q=2,\mathrm{lower},704)&8&8\\
(q=2,\mathrm{upper},973)&16&16\\
(q=4,\mathrm{upper},1007)&62&20.
\end{array}                                                \tag{4.2}
\]

Every other debt has only one-seam histories in this particular catalogue.
Thus a one-seam provider model is SAT-sound after literal replay but its
UNSAT result is not an exact all-history obstruction.  The existing builder
`build_catalan_m5_clean_socket_exact_cnf_h2_20260731.py` has been relabelled
accordingly; (3.1)--(4.1) are the complete replacement.

## 5. Separate arbitrary-width OR/AND automaton

Arbitrary-width coverage has a different exact state.  It should not be
silently inferred from Section 3.  For an upper target \(T\), put

\[
 A_T^+(w)=\left\{\bigcup s:
       s\text{ is a nonempty suffix of }w,\ \bigcup s\subseteq T\right\},
                                                               \tag{5.1}
\]

and let \(c_T^+(w)\) record whether some nonempty interval of \(w\) has union
exactly \(T\).  Appending one mask \(x\) gives

\[
 A_T^+(wx)=
 \begin{cases}
  \{x\}\cup\{a\cup x:a\in A_T^+(w)\},&x\subseteq T,\\
  \varnothing,&x\not\subseteq T,
 \end{cases}                                                  \tag{5.2}
\]

with elements outside the principal ideal of \(T\) discarded, and

\[
             c_T^+(wx)=c_T^+(w)\vee[T\in A_T^+(wx)].          \tag{5.3}
\]

For a lower target \(T\), dually put

\[
 A_T^-(w)=\left\{\bigcap s:
       s\text{ is a nonempty suffix of }w,\ T\subseteq\bigcap s\right\},
                                                               \tag{5.4}
\]

and update by

\[
 A_T^-(wx)=
 \begin{cases}
  \{x\}\cup\{a\cap x:a\in A_T^-(w)\},&T\subseteq x,\\
  \varnothing,&T\nsubseteq x,
 \end{cases}                                                  \tag{5.5}
\]

with \(c_T^-(wx)=c_T^-(w)\vee[T\in A_T^-(wx)]\).

### Theorem 5.1 (exact arbitrary-width state)

Equations (5.1)--(5.5), over every protected target, accept exactly the
arbitrary-width consecutive-union/intersection coverage requirement.
Transitions of a fixed path block compose associatively.

#### Proof

Every nonempty suffix of \(wx\) is either \(x\), or a nonempty suffix of
\(w\) followed by \(x\).  This proves (5.2) and (5.5).  An interval ending at
the new position realizes \(T\) exactly when the updated active set contains
\(T\); all older intervals are remembered by the coverage bit.  Induction on
the letters proves exactness.  A block transition is the composition of its
letter transitions, so concatenating blocks is associative. \(\square\)

For a closed-form block update, also store its total union \(U(v)\) and total
intersection \(I(v)\).  Then the suffixes inherited across the whole block
are respectively

\[
 \{a\cup U(v):a\in A_T^+(u)\},\qquad
 \{a\cap I(v):a\in A_T^-(u)\},                               \tag{5.6}
\]

whenever they remain in the appropriate ideal/filter; the block's own
active sets and coverage bits are united with these values while its stored
letter-transition function records crossings ending inside the block.
Formula (5.6) is useful for compression, but the letterwise form is the
fail-closed definition.

This automaton verifies arbitrary-width coverage of a proposed chronology.
It still does not choose erosion/compiler cells or prove the downstream
common-cap Hall matching.

## 6. Reproducibility and scope

Run the solver-free semantic/history audit with

```text
python3 scratch/threadD_audit_m5_fixedforest_connector_obstruction_20260731.py
```

Important hashes:

```text
fixed forest candidate  95d1d410b392bde4b1ca78f78bf1180836dbbd1a4022829dca034776e63289ed
CNF                     56e75ad69031c2ec15e403193745531812dc28989ebe759289860161f88fa963
full DRAT proof         04f1def8c24f07416bde3fbf9953882ea720480d5607ce3200be6ba58dbb7e05
68-clause core CNF      fffc31f73830c8f99550428fa85eee145889cd59097d3d33b70e6514377b89b1
core DRAT proof         b0a20e5d6c0dd5a89dcd6c7a5564381b3ac1ef4597a6afedd8b5665e99e32863
audit script            728f7d5caf4115108c05c6b89665a0333f5245b9b7237a648a917da1f89b5e74
audit JSON              024176c071c254d6a9e1d263ea98795e1bcd3a4be53a1f84c67c667c90987e02
```

To reverify the extracted proof from the workspace root:

```text
drat-trim \
  scratch/threadD_m5_connector_fixedforest_20260731/fixedforest.core.cnf \
  scratch/threadD_m5_connector_fixedforest_20260731/fixedforest.core.drat
```

This note proves no compiler Hall statement, no endpoint voltage statement,
and no all-`m` rethread theorem.  The exact next finite target is a new
palette-exact interior matching whose exposed path rays make the port
residence face nonempty, followed by the complete history transducer and
only then the compiler.
