# K16 gap one: exact external-donor extension and closure-normalized Hall cuts

Date: 2026-07-30  
Lane: K  
Status: general exact theorem; expanded13 is DRAT-verified UNSAT; expanded14
remains an exact open finite model

## 1. Result and scope

Let

```text
scratch/k16_Hfinal_externalblockers_v2.word.blocker2_h38.word
SHA-256 575f9e5b3453618636918cb410cff88390e12c2dd09fc4d635820b40e1bd4880
```

be the authenticated length-12,873 H38 word.  It has exactly 38 holes.  Its
twelve-cell backtracked causal support is

```text
110,111,112,666,667,670,4299,4301,6522,6523,6526,9958.       (1.1)
```

This is the union of cells on one selected source-witness backtrace for each
collateral hole.  It is not asserted to be a minimum or unique causal set.

The arbitrary-nonzero substitution model on (1.1) is already
DRAT-verified UNSAT.  The first atlas-prioritized external donor is position
6524.  The exact model on (1.1) together with 6524, called expanded13 below,
is now also DRAT-verified UNSAT.  Thus no universal word is obtained while
freezing the complement of those thirteen positions.

For the causal12 certificate, the stable hashes are model
`c71b7e94d6dabbd7326adb09c9e14dc2660564e424f3d8064caae23038b38bfa`,
phase-normalized model
`9f5be815fd7a5f0f11bda9df592091b1cbb5c6387d9ece47d0e801486015fc70`,
compressed proof
`53b207e7172271b1b15f5a5b7db0ad2e73cd9c4468557a89a50268d4010a740c`,
decompressed proof content
`51790b463bd39b834465a1418965c694439da235636f9553eab62cbd78965726`,
and verified transcript
`9e38b71ca2f920a38060646b9afdd5b37380abb0596a9529aab41a33f419beb6`.
This corrects a stale compressed-proof hash in the first version of the
causal12 audit note; the formula and `s VERIFIED` transcript were unchanged.

The mathematical result of this note is stronger than a donor census and
more limited than a K16 no-go.  It gives:

1. a necessary-and-sufficient literal one-donor extension theorem;
2. a closure-normalized form-selection CNF;
3. a complete projection to empty-intersection and coordinate non-cover
   certificates;
4. a strict donor-effect cut forced by the smaller support's UNSAT theorem;
5. exact h38 form and cut counts for donors 6524 and 668.

The atlas statement that 6524 is the unique external zero-debt one-edit
donor is not promoted to a multiedit uniqueness theorem.  A debtful donor,
or a donor useful only inside a new multi-edit interval, remains possible.

## 2. Literal interval forms

Let $w=(w_0,\ldots,w_{n-1})$ be a word of nonzero $k$-bit masks and let

\[
                    V=\{p_1<\cdots<p_s\}                 \tag{2.1}
\]

be the editable positions.  Write $G_0,\ldots,G_s$ for the fixed runs
before, between and after them.  Every endpoint suffix/prefix spectrum below
includes the empty choice of OR zero.  Let $F(V)$ be the targets having a witness
inside one fixed run and let

\[
 R(V)=\bigl(2^{[k]}\setminus\{\varnothing\}\bigr)\setminus F(V). \tag{2.2}
\]

Every witness of $T\in R(V)$ meets $V$, and its editable-position
intersection is a nonempty consecutive block $I=[a,b]\subseteq[s]$.
Let $g_{a,b}$ be the OR of the complete internal fixed gaps
$G_a,\ldots,G_{b-1}$.  If $g_{a,b}\nsubseteq T$, this block cannot witness
$T$.  Otherwise let $L_T(a)$ be the largest suffix OR of $G_{a-1}$
contained in $T$, and let $Q_T(b)$ be the largest prefix OR of $G_b$
contained in $T$.  These largest choices exist and are unique because each
endpoint spectrum is a chain.  Put

\[
 B_T(I)=g_{a,b}\vee L_T(a)\vee Q_T(b),\qquad
 N_T(I)=T\setminus B_T(I).                              \tag{2.3}
\]

### Lemma 2.1 (maximal-context exactness)

Some literal interval whose editable block is exactly $I$ has OR $T$ if
and only if

\[
 B_T(I)\vee\bigvee_{p\in I}x_p=T.                       \tag{2.4}
\]

#### Proof

Every admissible left suffix is contained in $L_T(a)$, and every
admissible right prefix is contained in $Q_T(b)$.  Replacing them by the
two largest admissible choices cannot introduce a bit outside $T$ and can
only reduce the variable need.  Conversely those two maximal endpoint
choices are literal suffix and prefix intervals.  The internal fixed gaps
are forced.  Hence (2.4) is equivalent to existence of a literal physical
interval.  \(\square\)

Thus one form

\[
                         f=(T,I,B_T(I),N_T(I))           \tag{2.5}
\]

per target and feasible editable block is exact.  No abstract target-only
provider has been introduced.

## 3. Exact literal-section theorem

Choose one form $f_T=(T,I_T,B_T,N_T)$ for each $T\in R(V)$.  For each
editable position define

\[
 C_p=\bigcap_{T:p\in I_T}T,                             \tag{3.1}
\]

with $C_p=[k]$ when no selected form uses $p$.

### Theorem 3.1 (section criterion)

The selected forms are simultaneously realizable by nonzero cell values if
and only if

\[
                         C_p\ne\varnothing\quad(p\in V) \tag{3.2}
\]

and

\[
 \forall T\in R(V)\ \forall e\in N_T:\quad
       \exists p\in I_T\text{ such that }e\in C_p.      \tag{3.3}
\]

When these conditions hold, $x_p=C_p$ at every used position is a
canonical realization.

#### Proof

If $x_p$ lies in a selected $T$-witness, then $x_p\subseteq T$, hence
$x_p\subseteq C_p$.  Nonzeroness gives (3.2).  Every bit in $N_T$ is
absent from the fixed context and must be supplied by some $x_p$, proving
(3.3).

Conversely, $C_p\subseteq T$ for every $p\in I_T$, so the canonical
cells add no forbidden bit to the selected witness.  Condition (3.3)
supplies every bit absent from the context.  Equation (2.4) follows for
every target.  Fixed-only targets retain their original witnesses.
\(\square\)

This also proves target-intersection closure normalization.  Every used
canonical cell belongs to

\[
 \mathcal D_R=\left\{\bigcap\mathcal A:
        \varnothing\ne\mathcal A\subseteq R(V),\
        \bigcap\mathcal A\ne\varnothing\right\}.        \tag{3.4}
\]

Equivalently, a live value $v$ may be enlarged to the intersection of all
repair targets containing it.  This preserves selected witnesses but need
not preserve Hamming distance from an incumbent.

## 4. Complete Hall/non-cover certificate

For a coordinate $e\in[k]$, define the union of selected $e$-omitting
blocks

\[
                      Z_e=\bigcup_{T:e\notin T}I_T.      \tag{4.1}
\]

Then $e\in C_p$ exactly when $p\notin Z_e$.  Theorem 3.1 is therefore
equivalent to

\[
                         \bigcap_{e\in[k]}Z_e=\varnothing \tag{4.2}
\]

and

\[
                         I_T\nsubseteq Z_e
             \quad(T\in R(V),\ e\in N_T).              \tag{4.3}
\]

This is the correct Hall analogue.  A cell-coordinate has unlimited reuse
across witnesses, so ordinary cardinal Hall inequalities are not exact.
For a fixed section, every failure has one of two and only two forms:

* **empty-intersection core:** selected forms sharing a position have target
  intersection zero;
* **coordinate non-cover core:** a selected form needs $e$, while selected
  $e$-omitting forms cover its whole editable block.

Conversely either core makes the section impossible.  Hence these two core
types are a complete projected certificate, not merely necessary cuts.

## 5. One external donor

Write $V=P\cup\{d\}$, where $P$ is the causal support and $d\notin P$
is one external donor.  For a selected section let

\[
 S_d=\{T:d\in I_T\},\qquad K_d=\bigcap_{T\in S_d}T.      \tag{5.1}
\]

Use the convention $K_d=[k]$ when $S_d=\varnothing$.

### Theorem 5.1 (one-donor extension)

A completion on $P\cup\{d\}$ exists if and only if there is a literal
section such that

\[
 K_d\ne\varnothing,\qquad C_p\ne\varnothing\ (p\in P), \tag{5.2}
\]

and every demand $e\in N_T$ is supplied either by

\[
 d\in I_T\text{ and }e\in K_d,                         \tag{5.3}
\]

or by a causal position $p\in I_T\setminus\{d\}$ with $e\in C_p$.
The canonical donor value is $x_d=K_d$.

#### Proof

This is Theorem 3.1 with the donor coordinate separated from the other
positions.  The target intersection at $d$ is exactly $K_d$.  \(\square\)

In particular, one donor-using selected target omitting coordinate $e$
poisons the donor for that coordinate in every selected donor witness.
Every other donor witness needing $e$ must then obtain it from a causal cell.

Adding a donor can also destroy fixed-only witnesses.  Precisely,

\[
 R(P)\subseteq R(P\cup\{d\}),\qquad
 \Delta_d=R(P\cup\{d\})\setminus R(P)=F(P)\setminus F(P\cup\{d\}). \tag{5.4}
\]

The surcharge \(\Delta_d\) must be included.  A one-edit atlas of the old
hole set does not detect it.

### Corollary 5.2 (strict donor-effect cut)

Assume the exact $P$-only model is UNSAT, and let $w_d$ be the frozen
incumbent at $d$.  Every augmented solution has $S_d\ne\varnothing$ and
some selected donor form $f=(T,I,B,N)$ satisfies at least one of

\[
                         w_d\nsubseteq T,               \tag{5.5}
\]

or

\[
 \exists e\in N\setminus w_d:\quad
       e\notin C_p\quad\text{for every }p\in I\setminus\{d\}. \tag{5.6}
\]

#### Proof

First replace the realization by the canonical one from Theorem 3.1, so
that every $e\in C_p$ is physically present at $p$.  If neither event occurs
for any selected donor form, reset the donor to $w_d$.  It introduces no
forbidden target bit by failure of (5.5), and
every needed bit absent from $w_d$ remains supplied by another cell by
failure of (5.6).  Every selected literal interval still witnesses its
target.  This gives a $P$-only completion, contradiction.  \(\square\)

Condition (5.5) is a containment break and (5.6) an exclusive-supply break.
This is stronger than the bare clause saying that some form uses the donor.

## 6. Closure-normalized CNF

Introduce a selector $y_f$ for every maximal literal form and an
availability bit $s_{p,e}$ for each editable position and coordinate.  Use
the following clauses.

For every target:

\[
                         \bigvee_{f:T_f=T}y_f.           \tag{6.1}
\]

For every $f$, $p\in I_f$, and $e\notin T_f$:

\[
                         \neg y_f\vee\neg s_{p,e}.       \tag{6.2}
\]

For every $p,e$, add the closure-normalizing reverse clause

\[
 s_{p,e}\vee
       \bigvee_{f:p\in I_f,\ e\notin T_f}y_f.           \tag{6.3}
\]

For every cell:

\[
                         \bigvee_e s_{p,e}.              \tag{6.4}
\]

For every $f$ and every $e\in N_f$:

\[
                         \neg y_f\vee\bigvee_{p\in I_f}s_{p,e}. \tag{6.5}
\]

### Theorem 6.1 (exactness of the normalized CNF)

Clauses (6.1)--(6.5) are satisfiable if and only if the arbitrary-nonzero
substitution model is satisfiable.

#### Proof

From a physical completion choose one realized form per target.  Enlarge
each used cell to the intersection of the targets of selected forms through
it and set $s_{p,e}$ to its characteristic bits.  This satisfies all five
clause types.  Conversely, set $x_p=\{e:s_{p,e}=1\}$.  Clause (6.4) makes
the cell nonzero, (6.2) keeps it inside every selected target, and (6.5)
supplies every missing context bit.  Lemma 2.1 realizes every selected form.
\(\square\)

Clause (6.3) is an equisatisfiable canonicalization, not an assignment-wise
implicate for the original cell bits: it expands each cell to the maximal
safe target intersection.  It is valid here because the change budget is
unbounded.  At-most-one form per target is unnecessary; extra true forms may
always be turned off provided the $s$-bits are recomputed from the remaining
selected forms.

Eliminating the $s$-variables gives the complete cuts

\[
                         \bigvee_{f\in\mathcal H}\neg y_f \tag{6.6}
\]

whenever the forms in \(\mathcal H\) share a cell and their targets have
empty intersection, and

\[
                         \neg y_f\vee
                         \bigvee_{g\in\mathcal H}\neg y_g \tag{6.7}
\]

whenever $f$ needs coordinate $e$ and the blocks of $e$-omitting forms
in \(\mathcal H\) cover $I_f$.  Inclusion-minimal families suffice.
Every minimal family in (6.6) has size at most $k$, and every minimal cover
in (6.7) has size at most \(|I_f|\).  Equations (4.2)--(4.3) prove
completeness.

There are also useful direct binary implicates.  Two forms $f,g$ conflict
if their blocks meet and $T_f\cap T_g=\varnothing$, or if

\[
 I_f\subseteq I_g\text{ and }N_f\nsubseteq T_g,         \tag{6.8}
\]

or symmetrically.  In (6.8), every cell capable of supplying the indicated
bit of $N_f$ is forced inside $T_g$, which omits that bit.

The strict donor-effect corollary can be added with auxiliaries for (5.6):
require the disjunction of all selected containment-break forms and all
selected form/coordinate pairs having no non-donor supplier.  This is a
sound learned cut derived from the smaller support's certified UNSAT result.

## 7. Exact h38 calibration: donor 6524

The causal12 and expanded13 maps have the same 94 residual targets, so

\[
                         \Delta_{6524}=\varnothing.      \tag{7.1}
\]

The exact form census is

\[
\begin{array}{c|r}
\text{model}&\text{maximal forms}\\ \hline
\text{causal12}&1649\\
\text{expanded13 avoiding 6524}&1629\\
\text{expanded13 using 6524}&327\\
\text{expanded13 total}&1956.
\end{array}                                             \tag{7.2}
\]

Exactly 20 causal12 forms crossed fixed position 6524.  Making 6524
variable removes those fixed-crossing forms and introduces 327 donor forms,
a net gain of 307.

In the expanded13 editable order, positions 6522, 6523, 6524 and 6526 have
indices 8, 9, 10 and 11.  Every one of the 94 targets has the three donor
blocks

\[
                         [8,10],\ [9,10],\ [10,10].      \tag{7.3}
\]

Exactly 15 targets also admit

\[
                         [8,11],\ [9,11],\ [10,11],     \tag{7.4}
\]

through the surviving fixed cell 6525.  Thus every donor interaction is
literal and localized to this four-position packet, although its target
choices are globally coupled to every other collar.

The 94-target nonzero intersection closure has exactly 1,035 states.
Causal12 UNSAT forces $S_d\ne\varnothing$, so the expanded13 donor-state
split needs precisely these 1,035 nonzero states, not 65,535 arbitrary
masks.  Without that smaller-support theorem, one must add the unused/FULL
state.  For a fixed state $K$, each donor form keeps only the punctured
causal demand $N_f\setminus K$, subject to $K\subseteq T_f$; requiring
the selected donor targets to have exact intersection $K$ makes this split
equisatisfiable.

The target family contains 15 empty pairs and 5,741 minimal empty triples
having no empty pair.  Expanding by donor forms gives 135 binary form cuts
and 206,739 ternary form cuts.  The sixteen variables
$s_{6524,e}$, with (6.2)--(6.4), encode all of these and all higher
empty-intersection cuts at once.  Among the 53,301 unordered donor-form
pairs, 46,518 satisfy one of the direct binary conflict tests above; 13,353
of those use the same editable block.

The incumbent donor value is

\[
                         w_{6524}=\mathtt{9019}.          \tag{7.5}
\]

It is not contained in 81 of the 94 donor target masks, accounting for 258
of 327 donor forms.  Those are static containment-break forms.  The remaining
13 masks and 69 forms can be essential only through the exclusive-supply
branch (5.6).

The exhaustive one-edit provider atlas has restricted but useful scope.  It
freezes positions 0, 111 and 6522, evaluates 2,046,050 deduplicated useful
edits, and finds 78 debt-free edits at positions 666, 667, 9958 and 6524.
Thus 6524 is the unique debt-free useful one-edit position outside causal12
under that freeze.  Its sixteen debt-free values are exactly

\[
             \mathtt{0003}\vee s,\qquad s\subseteq\mathtt{9018}, \tag{7.6}
\]

and every one fills only target $38175=\mathtt{951f}$, through the literal
interval [6523,6524].  They have one atlas-level target effect but normalize
to three simultaneous-model closure states

\[
                         \mathtt{0013},\quad
                         \mathtt{001b},\quad
                         \mathtt{901b}.                 \tag{7.7}
\]

Therefore quotienting all sixteen to one value would be unsound in the
simultaneous multiedit model.

The closure-normalized expanded13 CNF has

\[
\begin{array}{c|r}
\text{form selectors}&1956\\
\text{availability bits}&13\cdot16=208\\
\text{variables}&2164\\ \hline
\text{target menus}&94\\
\text{containment clauses}&22736\\
\text{closure reverse clauses}&208\\
\text{nonzero clauses}&13\\
\text{supply clauses}&14029\\
\text{clauses}&37080.
\end{array}                                             \tag{7.8}
\]

This removes the thirteen irrelevant unbounded-budget change variables from
the original 2,177-variable/37,093-clause encoding.

## 8. Expanded13 exact UNSAT certificate

Expanded13 allows arbitrary nonzero values at exactly

```text
110,111,112,666,667,670,4299,4301,6522,6523,6524,6526,9958.
```

In particular, 111 and 6522 are editable; only the one-edit provider atlas
froze them.  The exact physical formula has 94 repair targets, 1,956 forms,
2,177 variables and 37,093 clauses.  CaDiCaL returned UNSAT after 463.67
seconds with 47.11 MiB maximum RSS.  `drat-trim` independently verified the
retained proof after 702.484 seconds:

```text
36736 of 37093 input clauses in core
9084841 of 11441361 lemmas in core
586081681 resolution steps
0 RAT lemmas
s VERIFIED
```

Frozen hashes are:

\[
\begin{array}{ll}
\text{model CNF}&
\mathtt{73a426dcb8586ef70dc23902d52caad628a3b63190e411b24f53b144ded8b715},\\
\text{phase-normalized CNF}&
\mathtt{4fd869f73ddb6b19b1874875adcc8a5e801810d5c37f04b3fe5e2b96aae46bab},\\
\text{DRAT proof}&
\mathtt{35c7754ffe5c773c4b65d65b560bcb70f3f8e612730275c35c7d75bf18008d19},\\
\text{proof-check transcript}&
\mathtt{a68356b379f4f0f4121760492b90ae388709543628a9abfa530c798eeb27a4d3}.
\end{array}                                             \tag{8.1}
\]

Consequently every completion rooted at this h38 word changes at least one
cell outside expanded13.  This does not identify that cell, and it does not
exclude another thirteen-cell support with a different donor.

## 9. Expanded14 and donor 668

Expanded14 additionally makes position 668 variable.  Its residual target
family is still the same 94 targets, so \(\Delta_{668}=\varnothing\).  The
exact model has

\[
 2261\text{ forms},\quad2499\text{ variables},\quad44368\text{ clauses}. \tag{9.1}
\]

Of the forms, 1,940 avoid 668 and 321 use it.  Every target has the three
local blocks ending at 668; 13 targets also have the three blocks crossing
the surviving fixed position 669 to editable position 670.  Thus adding 668
removes 16 old fixed-crossing forms, introduces 321 donor forms, and gains
305 forms net.

The closure-normalized encoding has

\[
 2485\text{ variables},\qquad44354\text{ clauses},      \tag{9.2}
\]

with 27,721 containment and 16,301 supply clauses.  The incumbent is
$w_{668}=\mathtt{022d}$.  It gives static containment breaks for 82 target
masks and 261 donor forms; the other 12 masks and 60 forms require the
exclusive-supply branch.

Because expanded13 is now certified UNSAT, every expanded14 solution must
strictly activate position 668 in the sense of Corollary 5.2.  It does not
follow that position 6524 must also be used.  The exact expanded14 solve was
still running when this note was frozen; (9.1)--(9.2) are model theorems, not
a SAT or UNSAT verdict.

Stable expanded14 model hashes at freeze time are:

\[
\begin{array}{ll}
\text{stats}&
\mathtt{a351d9b055d9771c6190c43565c8aaf35017d41ff075e29f70c052ff69e9dffc},\\
\text{model CNF}&
\mathtt{a70510d368ba22f6f590d6a110629bf90db35c67abb50ba9af750d97943e9cf8},\\
\text{model map}&
\mathtt{14706c2e25d6c25a74701c43a96162fc433f599334c7105ca391b42ada9d974c},\\
\text{phase-normalized CNF}&
\mathtt{b7c11e8c6c331a60affb029e1c1c3853c92b3884161e11ddb94bfd7654f3a754}.
\end{array}                                             \tag{9.3}
\]

No hash of the still-growing proof stream is authoritative.

## 10. Independent light audit

The solver-free audit

```text
scratch/audit_k16_h38_external_donor_normalform_20260730.py
SHA-256 67f92c2f58304cec0ec63d3bcf44828d55a3ca5213299f07db1bfe1c0336227a
```

hash-checks the source, causal map, expanded13 map and provider atlas; then
reconstructs the structural and form counts in Section 7, including the
1,035 closure states, 15/5,741 empty-intersection census, 46,518 binary
conflicts, incumbent containment-break census and normalized CNF ledger.  It
does not
audit the solver time, DRAT proof or proof-check transcript in Section 8.
Its output is

```text
scratch/k16_h38_external_donor_normalform_20260730.audit.json
SHA-256 0a6d2cdae2988a45b01775ed9cc8b0d31a8991ddf40f18ee41c04a68755d5bd2
payload SHA-256 4d88214cf7e5cb7cd48394388a9875d4643ed4d388f40411ab7f690c53b3a713
```

An independent canonical-cell implementation adds the 208 reverse rows
(6.3) directly to the original expanded13 CNF and independently reconstructs
the physical target/form family:

```text
scratch/ad_k16_external_h38_expanded13_blocker_strengthening_20260730/model.canonical.cnf
  SHA 7ef805b9b6665e2c87bed3e18bb573ece33dc07f64e40716f2dd8c09fa85e294
scratch/ad_k16_external_h38_expanded13_blocker_strengthening_20260730/model.canonical.audit.json
  SHA 33d18cd67612eff8f3c2ad409fa9c31b0baf43833c600d59717479574aa278d3
scratch/ad_k16_external_h38_expanded13_blocker_strengthening_20260730/model.canonical.independent_audit.json
  SHA 1f75b0ebb1a7a73220cdc05bae05ff7c2059fca22112789cf91d105002d97e8f
```

Those files retain the original change variables, so they have 37,301
clauses rather than the compact 37,080-clause ledger (7.8).  Both encodings
implement the same closure theorem.

## 11. Exact boundary

The proved conclusions are:

* causal12 and causal12 plus 6524 are exact UNSAT supports;
* every expanded14 completion, if one exists, must make 668 essential by a
  containment or exclusive-supply break;
* one/two-donor feasibility is exactly a partitioned form-selection problem
  with empty-intersection and coordinate non-cover cores;
* the normalized CNF and all displayed cuts preserve literal contiguous-OR
  realizability and nonzero-cell integrality.

Not proved are:

* expanded14 SAT or UNSAT;
* uniqueness of 6524 or 668 among simultaneous multiedit donors;
* a global lower bound of fourteen changed cells;
* impossibility of another length-12,873 word;
* the exact K16 lower bound.

The global bracket remains

\[
                         12873\le\nu(16)\le12874.       \tag{11.1}
\]
